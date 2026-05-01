# Parameter-Efficient Fine-Tuning & The Open-Source Training Revolution

> *How LoRA, QLoRA, and a wave of open-weight models turned 70 B parameter customization from a
> million-dollar cloud bill into a weekend project on a single GPU.*

---

## Why This Matters

In 2022, fine-tuning a large language model meant renting a cluster of A100 GPUs for weeks.
By mid-2024, researchers were fine-tuning 70 B parameter models on a **single 48 GB GPU** —
sometimes even on a free-tier Colab notebook with 16 GB of VRAM — and publishing results that
rivalled full fine-tuning baselines. Three things converged to make this possible:

1. **Parameter-efficient fine-tuning (PEFT)** methods that train < 1 % of parameters.
2. **Quantisation breakthroughs** that compress 16-bit weights to 4 bits with near-zero quality loss.
3. **Open-weight model releases** (Llama, Mistral, Qwen, DeepSeek) that gave researchers
   something worth fine-tuning in the first place.

The combined effect has been a *democratisation of model customisation*. Startups, academics,
hobbyists — anyone with a specific domain and a modest GPU budget — can now build specialised
models that out-perform general-purpose APIs on their particular task. This chapter explains how.

---

## Full Fine-Tuning Recap

Before diving into efficiency tricks, it helps to remember what "full" fine-tuning actually
involves, and why it is expensive.

### What happens during full fine-tuning

Given a pre-trained model with parameters **θ** and a downstream dataset **D**, we minimise a
task-specific loss:

```
θ* = argmin_θ  𝔼_(x,y)∼D [ L(f_θ(x), y) ]
```

Every parameter in every layer receives a gradient. The optimiser (typically AdamW) maintains
**two additional states per parameter** — the first moment (mean) and the second moment
(variance). For a 7 B-parameter model in FP32:

| Component         | Per-param bytes | Total (7 B) |
|-------------------|-----------------|-------------|
| Model weights     | 4               | 28 GB       |
| Gradients         | 4               | 28 GB       |
| Optimiser state 1 | 4               | 28 GB       |
| Optimiser state 2 | 4               | 28 GB       |
| **Total**         |                 | **112 GB**  |

A **70 B model** scales this to over **1 TB** — requiring multi-node setups or aggressive
memory tricks even in FP16.

### When you still need full fine-tuning

- **Domain shift is extreme** — the model needs to learn a fundamentally new vocabulary
  or reasoning style (e.g., translating between rare languages, scientific notation systems).
- **You are training from scratch or doing continued pre-training** on a very large corpus.
- **You have the compute budget** and want the absolute best downstream performance —
  full fine-tuning still wins by a small margin in head-to-head comparisons.
- **Architecture modifications** — adding new attention heads, changing the tokeniser,
  or inserting new layers all require full gradient flow.

For the vast majority of practical use-cases — instruction-following, domain-specific QA,
style transfer, function calling — PEFT methods close the gap to within 1-2 % of full
fine-tuning at a fraction of the cost.

---

## LoRA — Low-Rank Adaptation

**Paper:** Hu et al., *"LoRA: Low-Rank Adaptation of Large Language Models"*, 2021
([arXiv:2106.09685](https://arxiv.org/abs/2106.09685))

### The key insight: weight updates are low-rank

The authors begin with a striking empirical observation: when you fine-tune a large pre-trained
model, the **weight update matrix ΔW** has an intrinsically low rank. That is, even though
ΔW lives in a d × k dimensional space, it can be well-approximated by a matrix of rank r,
where r ≪ min(d, k).

Intuitively, pre-training already places the model in a good region of parameter space. Fine-
tuning only needs to make a *relatively small correction*, and that correction lies on a
low-dimensional manifold. This is the theoretical justification for LoRA: if the update is
low-rank anyway, why not *parameterise* it as such from the start?

### How LoRA works

For a pre-trained weight matrix **W₀** ∈ ℝ^(d×k), LoRA replaces the full update with a
factored product:

```
W = W₀ + ΔW = W₀ + B · A
```

Where:
- **A** ∈ ℝ^(r×k) — initialised from a small Gaussian, projects input down to rank r
- **B** ∈ ℝ^(d×r) — initialised to zero (so ΔW = 0 at start of training)
- **r** — the LoRA rank, a hyperparameter (commonly 4, 8, 16, 32, or 64)

During a forward pass:

```
h = W₀ · x + (α / r) · B · A · x
```

The scaling factor **α/r** (where α is a constant, often set equal to r or 2×r) controls
the magnitude of the adaptation relative to the frozen weights.

**Only A and B are trainable.** W₀ is frozen and never receives gradients.

### Where to apply LoRA

In a standard Transformer, each attention layer has four projections — Q, K, V, and O — and
each feed-forward block has two dense layers. The original paper applies LoRA to the attention
projections (typically Q and V). Later work showed benefits from also applying it to K, O,
and the FFN layers. The Hugging Face PEFT library makes it trivial to target any linear layer.

### Rank selection and its impact

| Rank (r) | Trainable params (7 B model, Q+V) | Typical quality | Notes |
|----------|-----------------------------------|-----------------|-------|
| 4        | ~4.2 M (0.06 %)                  | Good for simple tasks | May underfit complex domains |
| 8        | ~8.4 M (0.12 %)                  | Strong baseline  | Most common default |
| 16       | ~16.8 M (0.24 %)                 | Near full FT     | Sweet spot for many tasks |
| 32       | ~33.6 M (0.48 %)                 | Diminishing returns begin | Use for hard tasks |
| 64       | ~67.2 M (0.96 %)                 | Plateau          | Rarely needed |

**Key finding from ablation studies:** Performance rises steeply from r = 1 to r = 8, then
plateaus. Going beyond r = 32 rarely helps and can even hurt if the dataset is small (over-
fitting to noise in the low-data regime).

The **alpha (α)** hyperparameter scales the LoRA contribution. A common heuristic:

```
α = 2 × r      (e.g., r=16 → α=32)
```

When α = r, the effective learning rate for LoRA matches the base learning rate. When α > r,
LoRA's update is amplified; when α < r, it is damped.

### Memory savings explained

For a 7 B model fine-tuned with LoRA (r = 16, Q + V only):

| Component                  | Full FT    | LoRA       |
|---------------------------|------------|------------|
| Frozen weights (FP16)     | —          | 14 GB      |
| Trainable params (FP16)   | 14 GB      | ~34 MB     |
| Gradients                 | 14 GB      | ~34 MB     |
| Optimiser (Adam, FP32)    | 56 GB      | ~136 MB    |
| Activations (batch=1)     | ~2 GB      | ~2 GB      |
| **Total**                 | **~86 GB** | **~16 GB** |

The savings come from three places:
1. **No gradients** for frozen parameters.
2. **No optimiser states** for frozen parameters.
3. Trainable parameter count is ~0.2 % of total.

### Merging LoRA weights back

After training, you can merge the adaptation permanently:

```python
W_merged = W₀ + (α / r) * B @ A
```

The resulting model is **identical in architecture** to the original — no adapter layers, no
extra forward-pass overhead, no inference latency penalty. You can also keep adapters
separate and swap them at serving time (multi-LoRA serving), which is useful for multi-tenant
deployments where different customers have different fine-tuned behaviour.

**Multi-adapter serving** frameworks like **LoRAX**, **S-LoRA**, and **vLLM** can serve
hundreds of LoRA adapters from a single base model in GPU memory, dynamically composing
the right adapter per request.

---

## QLoRA — Quantized LoRA

**Paper:** Dettmers et al., *"QLoRA: Efficient Finetuning of Quantized Language Models"*, 2023
([arXiv:2305.14314](https://arxiv.org/abs/2305.14314))

QLoRA takes LoRA's parameter efficiency and combines it with aggressive weight quantisation,
enabling fine-tuning of models that would otherwise not fit in GPU memory at all.

### 4-bit NormalFloat (NF4) quantisation

Standard 4-bit integer quantisation divides the value range into 16 equally spaced buckets.
This works poorly for neural network weights, which follow an approximately **normal
distribution** centred around zero. Most buckets end up empty, while the dense central
region is coarsely represented.

**NF4** (NormalFloat4) solves this by placing quantisation levels at the **quantiles of the
standard normal distribution**. Concretely:

1. Assume weights are normally distributed: w ~ N(0, σ²)
2. Compute the 16 quantile points of N(0, 1) that divide the distribution into 16 equally
   probable regions.
3. Map each weight to the nearest quantile point.
4. Store a per-block scaling factor σ to recover the original scale.

This ensures that **information-theoretically optimal** use is made of the 4-bit budget —
each quantisation bin contains roughly the same probability mass.

### Double quantisation

Even with NF4, each block of (typically) 64 weights needs a FP32 scaling constant. For a
65 B model, these constants alone consume ~0.5 GB. **Double quantisation** quantises the
scaling constants themselves to 8-bit, with a second-level scaling constant shared across
256 first-level constants. This saves an additional ~0.37 bits per parameter:

```
Memory per param = 4 bits (NF4) + 0.127 bits (quantised scale) ≈ 4.13 bits
```

Versus 4.5 bits with un-quantised scaling constants.

### Fine-tuning 65 B models on a single 48 GB GPU

Combining NF4 + double quantisation + paged optimisers (which offload optimiser states to
CPU RAM on demand), QLoRA enables the following:

| Model size | Base weight memory (NF4) | LoRA + optimizer | Total VRAM |
|-----------|--------------------------|------------------|------------|
| 7 B       | ~3.5 GB                 | ~0.2 GB          | ~6 GB      |
| 13 B      | ~6.5 GB                 | ~0.4 GB          | ~10 GB     |
| 33 B      | ~16.5 GB                | ~0.8 GB          | ~22 GB     |
| 65 B      | ~32.5 GB                | ~1.5 GB          | ~41 GB     |

A **65 B model fine-tuned on a single A6000 (48 GB)**. Before QLoRA, this required at
minimum 4 × A100 80 GB GPUs. The cost reduction is roughly **16×**.

### The democratisation impact

QLoRA's release in May 2023 was a watershed moment. Within weeks:

- The **Guanaco** family of chatbots, trained with QLoRA on the OASST1 dataset, matched
  ChatGPT on the Vicuna benchmark while training on a single GPU in under 24 hours.
- Hundreds of domain-specific LoRA adapters appeared on Hugging Face — medical, legal,
  coding, finance — all trained by individuals or small teams.
- The fine-tuning ecosystem (Axolotl, LLaMA-Factory, Unsloth) standardised around QLoRA
  as the default training configuration.
- **Unsloth** later pushed this further, achieving 2× speed-ups over standard QLoRA through
  custom Triton kernels and fused operations.

---

## DoRA — Weight-Decomposed LoRA

**Paper:** Liu et al., *"DoRA: Weight-Decomposed Low-Rank Adaptation"*, ICML 2024 Oral
([arXiv:2402.09353](https://arxiv.org/abs/2402.09353))

### The problem with standard LoRA

LoRA applies an additive low-rank update: W' = W + BA. Both the **magnitude** (how large
the weights are) and the **direction** (which subspace they point in) are coupled in the
same update. Analysis of full fine-tuning reveals that magnitude and direction evolve
**independently** — sometimes in opposite directions. LoRA's coupled update struggles to
replicate this pattern.

### Decomposing into magnitude and direction

DoRA decomposes each weight matrix using a **weight normalisation** inspired reparameterisation:

```
W = m · (V / ‖V‖_c)
```

Where:
- **m** ∈ ℝ^d — a learnable **magnitude vector** (one scalar per output dimension)
- **V** ∈ ℝ^(d×k) — a **direction matrix**
- **‖V‖_c** — column-wise norm of V

During fine-tuning:
- **m** is trained directly (full-rank, but only d parameters — negligible cost).
- **V** is updated via LoRA: V' = V₀ + BA (same low-rank factorisation as standard LoRA).

The forward pass becomes:

```
h = m · ((V₀ + BA) / ‖V₀ + BA‖_c) · x
```

### Why this improves over standard LoRA

By decoupling magnitude from direction:

1. **Magnitude can change freely** without being constrained by the low-rank bottleneck.
2. **Directional updates** can focus purely on rotating the weight vectors, which is where
   most of the task-specific information resides.
3. The learning dynamics more closely **mirror full fine-tuning**, narrowing the gap.

### Performance comparison

On commonsense reasoning benchmarks (LLaMA-7B/13B):

| Method        | Avg accuracy | Trainable params |
|---------------|-------------|------------------|
| Full FT       | 80.4 %      | 100 %            |
| LoRA (r=32)   | 78.6 %      | 0.83 %           |
| **DoRA (r=32)** | **79.7 %** | **0.84 %**       |

DoRA consistently closes about **half the gap** between LoRA and full fine-tuning across
tasks, with negligible additional parameter overhead (just the magnitude vector m). It has
been adopted in Hugging Face PEFT and is a drop-in replacement for LoRA in most training
frameworks.

**No extra inference cost:** After training, the magnitude and normalised direction can be
fused back into a single weight matrix, identical to standard LoRA merging.

---

## Adapter Methods Zoo

LoRA is the most popular PEFT method, but it is far from the only one. Here is a survey of
the major alternatives and when each is most appropriate.

### Prefix Tuning

**Paper:** Li & Liang, *"Prefix-Tuning: Optimizing Continuous Prompts for Generation"*, 2021
([arXiv:2101.00190](https://arxiv.org/abs/2101.00190))

- **Mechanism:** Prepend learnable "prefix" vectors to the key and value matrices at **every**
  Transformer layer. These prefixes act as virtual tokens that steer the attention computation.
- **Trainable params:** Only the prefix vectors — typically < 0.1 % of total parameters.
- **Strengths:** Very parameter-efficient; works well for generation tasks (summarisation,
  translation).
- **Weaknesses:** Can struggle with discriminative tasks; sensitive to prefix length; does
  not modify the actual weight matrices.

### Prompt Tuning

**Paper:** Lester et al., *"The Power of Scale for Parameter-Efficient Prompt Tuning"*, 2021
([arXiv:2104.08691](https://arxiv.org/abs/2104.08691))

- **Mechanism:** Learn a small set of **soft token embeddings** prepended to the input at the
  **embedding layer only** (not at every layer like prefix tuning).
- **Trainable params:** Extremely small — a few thousand to a few hundred thousand.
- **Strengths:** Simplest PEFT method; excellent for multi-task serving (each task = a
  different prompt).
- **Weaknesses:** Performance degrades significantly for models under ~10 B parameters.
  At scale (100 B+), it approaches full fine-tuning quality.

### (IA)³ — Infused Adapter by Inhibiting and Amplifying Inner Activations

**Paper:** Liu et al., *"Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper
than In-Context Learning"*, 2022 ([arXiv:2205.05638](https://arxiv.org/abs/2205.05638))

- **Mechanism:** Learn **three scaling vectors** that element-wise multiply the keys, values,
  and FFN intermediate activations. No new layers, no attention modification — just learned
  per-element gates.
- **Trainable params:** Tiny — three vectors per layer, typically ~0.01 % of total.
- **Strengths:** Extremely efficient; excels in **few-shot** settings where data is scarce;
  adds zero latency at inference.
- **Weaknesses:** Less expressive than LoRA for complex adaptations; limited community tooling
  compared to LoRA.

### Comparison: when to use what

| Method         | Params trained | Best regime        | Inference overhead | Multi-task? |
|----------------|---------------|--------------------|--------------------|-------------|
| Full FT        | 100 %         | Unlimited data     | None               | No          |
| LoRA           | 0.1-1 %       | Medium data        | None (after merge) | Yes (swap)  |
| DoRA           | 0.1-1 %       | Medium data        | None (after merge) | Yes (swap)  |
| QLoRA          | 0.1-1 %       | Memory-constrained | None (after merge) | Yes (swap)  |
| Prefix Tuning  | < 0.1 %       | Generation tasks   | Small              | Yes         |
| Prompt Tuning  | < 0.01 %      | Scale ≥ 10 B       | None               | Yes         |
| (IA)³          | < 0.01 %      | Few-shot           | None               | Yes         |

### Combining methods

Methods are not mutually exclusive. Common combinations include:

- **QLoRA + gradient checkpointing** — the de facto standard for consumer GPU training.
- **LoRA + prefix tuning** — sometimes yields small gains on generation benchmarks.
- **Multiple LoRA adapters** composed at inference time — e.g., one for style, one for domain.

The Hugging Face **PEFT library** provides a unified API for all these methods, making
experimentation straightforward.

---

## Training Infrastructure

Even with PEFT methods, training at scale requires careful orchestration of memory, compute,
and communication. The modern training stack has converged around a few key technologies.

### DeepSpeed ZeRO Stages

**ZeRO** (Zero Redundancy Optimizer), developed by Microsoft, is the most widely used memory
optimisation framework for distributed training. It works by **partitioning** the redundant
copies of model state across GPUs.

In standard data-parallel training, **every GPU** holds a complete copy of:
- Model parameters (θ)
- Gradients (∇θ)
- Optimiser states (m, v for Adam)

For a 7 B model in mixed precision, this means ~112 GB **per GPU** — wildly redundant when
you have 8 GPUs each holding identical copies.

#### ZeRO Stage 1: Optimiser State Partitioning

- **What's partitioned:** Optimiser states (Adam m and v) are split across N GPUs.
- **Each GPU stores:** Full parameters + full gradients + 1/N of optimiser states.
- **Memory reduction:** ~4× for Adam (optimiser states are ~2/3 of total memory).
- **Communication overhead:** Minimal — only an all-gather after the optimiser step.

#### ZeRO Stage 2: Gradient Partitioning

- **What's partitioned:** Optimiser states + gradients.
- **Each GPU stores:** Full parameters + 1/N of gradients + 1/N of optimiser states.
- **Memory reduction:** ~8× vs baseline.
- **Communication:** Reduce-scatter during backward pass (efficient, overlaps with compute).

#### ZeRO Stage 3: Parameter Partitioning

- **What's partitioned:** Everything — parameters, gradients, optimiser states.
- **Each GPU stores:** 1/N of parameters + 1/N of gradients + 1/N of optimiser states.
- **Memory reduction:** Linear in N — theoretically unlimited model size.
- **Communication:** All-gather before each forward/backward layer, reduce-scatter after.
  Higher communication volume, but enables models that don't fit on any single GPU.

#### ZeRO-Infinity: CPU and NVMe Offloading

- Extends Stage 3 by offloading partitions to **CPU RAM** or **NVMe SSDs**.
- Enables training **trillion-parameter models** on clusters with limited GPU memory.
- Trade-off: PCIe bandwidth becomes the bottleneck; throughput drops significantly.
- Best used for very large models where GPU memory is the hard constraint.

**Summary table:**

| Stage     | Optimizer states | Gradients   | Parameters  | Offload      |
|-----------|-----------------|-------------|-------------|--------------|
| Baseline  | Replicated      | Replicated  | Replicated  | No           |
| Stage 1   | Partitioned     | Replicated  | Replicated  | No           |
| Stage 2   | Partitioned     | Partitioned | Replicated  | No           |
| Stage 3   | Partitioned     | Partitioned | Partitioned | Optional     |
| Infinity  | Partitioned     | Partitioned | Partitioned | CPU + NVMe   |

### FSDP (Fully Sharded Data Parallel)

PyTorch's native answer to DeepSpeed ZeRO Stage 3. Key differences:

- **Native PyTorch integration** — no external library needed (torch.distributed.fsdp).
- **Shards parameters, gradients, and optimiser states** across ranks.
- **On-the-fly gathering:** Parameters are all-gathered just before each layer's forward
  pass, then immediately discarded. This keeps peak memory to ~1/N of the full model.
- **Hybrid sharding:** Can shard within a node but replicate across nodes, reducing
  inter-node communication while still saving memory.

**FSDP vs DeepSpeed in practice (2024):**

| Feature              | DeepSpeed ZeRO      | PyTorch FSDP         |
|---------------------|---------------------|----------------------|
| Integration         | External library    | Native PyTorch       |
| CPU/NVMe offload    | Mature              | Experimental         |
| Tensor parallelism  | Via Megatron        | Via DTensor          |
| Pipeline parallelism| Supported           | Via PiPPy            |
| Ecosystem           | Hugging Face, etc.  | Hugging Face, etc.   |
| Ease of use         | Config-driven       | API-driven           |
| Maturity at scale   | Proven (BLOOM, etc.)| Rapidly improving     |

Most Hugging Face Trainer users can switch between them with a single flag.

### Mixed Precision Training

Modern GPUs have specialised hardware (Tensor Cores) that operate fastest at reduced
precision. The key formats:

**FP32 (32-bit float):**
- Sign: 1 bit, Exponent: 8 bits, Mantissa: 23 bits
- Full range and precision; standard training baseline
- ~2× slower than FP16 on Tensor Cores

**FP16 (16-bit float):**
- Sign: 1 bit, Exponent: 5 bits, Mantissa: 10 bits
- 2× memory savings, 2-8× compute speed-up on Tensor Cores
- **Problem:** Limited dynamic range (max ~65504) causes overflow in loss/gradient scaling
- **Solution:** Loss scaling — multiply loss by a large constant, compute gradients, then
  divide back. AMP (Automatic Mixed Precision) handles this automatically.

**BF16 (bfloat16 / Brain Floating Point):**
- Sign: 1 bit, Exponent: 8 bits, Mantissa: 7 bits
- Same exponent range as FP32 — **no overflow issues**
- Slightly less precision than FP16, but much more stable in practice
- **The default for modern LLM training** (used for Llama, Mistral, etc.)
- Requires Ampere (A100) or newer GPUs

**FP8 (8-bit float) — Hopper generation (H100):**
- Two variants: E4M3 (range-focused) and E5M2 (precision-focused)
- 2× memory savings over FP16, massive throughput on H100 Tensor Cores
- Still experimental for training; becoming standard for inference
- Requires careful per-tensor scaling and format selection

### Gradient Checkpointing

A memory-compute trade-off that **recomputes** intermediate activations during the backward
pass instead of storing them.

**Without checkpointing:** Store all activations → O(L) memory for L layers.
**With checkpointing:** Store activations at √L checkpoint boundaries, recompute the rest →
O(√L) memory, but ~33 % more compute.

In practice, this is the single most impactful memory optimisation for LoRA/QLoRA training,
often reducing activation memory by 60-70 %. It is enabled by default in most training
frameworks (Hugging Face Trainer, Axolotl).

### Gradient Accumulation

Simulates larger batch sizes without requiring more GPU memory:

```python
effective_batch_size = micro_batch_size × gradient_accumulation_steps × num_gpus
```

Instead of updating weights after every micro-batch, gradients are **accumulated** over K
steps and applied once. This is essential when:

- Memory constrains micro_batch_size to 1 or 2
- The task benefits from large batch sizes (e.g., contrastive learning, RLHF)
- You want to match a reference training recipe's batch size on fewer GPUs

---

## The Open-Weight Ecosystem

The other half of the fine-tuning revolution is having models **worth fine-tuning**. The
2023-2024 period saw an unprecedented release of powerful open-weight models.

### Llama Series: How Meta Changed the Game

**Llama 1 (February 2023):**
- 7 B, 13 B, 33 B, 65 B parameters
- Released under a research-only licence (leaked within days)
- Trained on 1.4 T tokens of publicly available data
- **Impact:** Ignited the open-source LLM movement. Within weeks, Alpaca, Vicuna, and dozens
  of derivatives appeared. Proved that open models could compete with GPT-3.

**Llama 2 (July 2023):**
- 7 B, 13 B, 70 B parameters (plus chat-tuned variants)
- **Commercial licence** (with a 700 M monthly active user threshold for Meta approval)
- Trained on 2 T tokens; 40 % more data than Llama 1
- RLHF-aligned chat models included
- **Impact:** Became the de facto base model for the open-source community. Microsoft
  partnership brought it to Azure. Hundreds of fine-tunes on Hugging Face.

**Llama 3 (April 2024):**
- 8 B and 70 B (with 405 B coming later)
- Trained on 15 T tokens — 7.5× more than Llama 2
- New tokeniser with 128 K vocabulary (vs 32 K for Llama 2)
- Grouped Query Attention (GQA) for efficient inference
- **Impact:** Set new SOTA for open models at each size class. The 70 B model competed
  with GPT-4 on many benchmarks.

### Mistral and the European AI Push

**Mistral 7B (September 2023):**
- Released under **Apache 2.0** — the most permissive licence in the open LLM space
- Introduced **Sliding Window Attention** for efficient long contexts
- Out-performed Llama 2 13 B despite being half the size
- **Impact:** Proved that architectural efficiency could compensate for raw scale.

**Mixtral 8×7B (December 2023):**
- Sparse Mixture-of-Experts: 46.7 B total parameters, but only 12.9 B active per token
- Apache 2.0 licence
- Matched or beat Llama 2 70 B while being 5× faster at inference
- **Impact:** Mainstreamed the MoE architecture for the open-source community.

**Mistral Large and beyond:**
- Larger models moved to more restrictive licences (MNPL)
- Positioned as a European sovereign AI alternative
- Strong GDPR compliance and multilingual European language support

### Qwen, Yi, DeepSeek: The Chinese Open-Weight Wave

**Qwen (Alibaba):**
- Qwen 1, 1.5, 2, 2.5, 3 series — rapid iteration
- Sizes from 0.5 B to 110 B parameters
- Newest releases under **Apache 2.0** — genuinely permissive
- 119-language multilingual support
- Excels at math and code (92 %+ on AIME 2025, 88 %+ on HumanEval)
- Most downloaded open-weight LLM family on Hugging Face by mid-2025

**Yi (01.AI):**
- Yi-34 B was among the first open models to compete with GPT-3.5 across the board
- Bilingual (English/Chinese) focus
- Apache 2.0 licence for smaller models

**DeepSeek:**
- DeepSeek-V2 introduced **Multi-head Latent Attention (MLA)** — a KV-cache compression
  technique that dramatically reduces inference memory
- DeepSeek-R1: "Reasoning-first" model with explicit chain-of-thought, **MIT licence**
- DeepSeek-V3: MoE architecture with 671 B total / 37 B active parameters
- **Impact:** Proved that Chinese labs could match frontier performance at a fraction of
  the training cost; MIT licence is the most permissive in the space.

### Why Open Weights ≠ Open Source

The Open Source Initiative (OSI) defines open source with specific criteria: free
redistribution, access to source code, right to create derivatives, no field-of-use
restrictions, and no discrimination against persons or groups.

Most "open" LLMs fail at least one criterion:

| Model      | Licence              | Weights | Training code | Training data | Truly OSI? |
|-----------|----------------------|---------|---------------|---------------|------------|
| Llama 3   | Llama Community      | ✅      | ✅            | ❌            | ❌         |
| Mistral 7B| Apache 2.0           | ✅      | ❌            | ❌            | ⚠️          |
| Qwen 3    | Apache 2.0           | ✅      | ✅            | ❌            | ⚠️          |
| DeepSeek  | MIT                  | ✅      | ✅            | ❌            | ⚠️          |
| OLMo      | Apache 2.0           | ✅      | ✅            | ✅            | ✅         |
| Pythia    | Apache 2.0           | ✅      | ✅            | ✅            | ✅         |

**The critical missing piece:** Almost no one releases the full training dataset. Without it,
you cannot truly reproduce the model — only fine-tune it. Projects like **OLMo** (Allen AI)
and **Pythia** (EleutherAI) are notable exceptions.

### Licensing Landscape

| Licence          | Commercial | Modify | Redistribute | Field-of-use limits         |
|------------------|-----------|--------|-------------|------------------------------|
| Apache 2.0       | ✅         | ✅      | ✅           | None                         |
| MIT              | ✅         | ✅      | ✅           | None                         |
| Llama Community  | ✅*        | ✅      | ✅           | 700 M MAU limit; no competing models |
| Gemma ToS        | ✅         | ✅      | ✅           | Safety restrictions          |
| MNPL (Mistral)   | ✅*        | ✅      | ⚠️           | Commercial restrictions      |
| CC BY-NC 4.0     | ❌         | ✅      | ✅           | Non-commercial only          |

\* With conditions.

**Practical advice:** Always read the actual licence file in the repository — Hugging Face
model cards sometimes simplify or misrepresent licence terms.

---

## Synthetic Data & Data Curation

If PEFT methods are the engine of the fine-tuning revolution, **data** is the fuel. The 2023-
2024 period saw a fundamental rethinking of where training data comes from and how much you
need.

### Using Strong Models to Generate Training Data

The **knowledge distillation** pipeline has become standard:

```
Strong teacher model (GPT-4, Claude)
        ↓
    Generate responses to diverse prompts
        ↓
    Filter for quality (automated + human)
        ↓
    Fine-tune open student model (Llama, Mistral)
```

This is sometimes called **model distillation via synthetic data**. The ethical and legal
implications are debated, but the practical impact is undeniable — it enables small teams to
create high-quality instruction-following datasets without massive human annotation budgets.

**Important caveat:** Many model licences (OpenAI ToS, Anthropic ToS) restrict using outputs
to train competing models. The legality of this restriction and its enforceability varies by
jurisdiction.

### Self-Instruct and the Alpaca Approach

**Self-Instruct** (Wang et al., 2022, [arXiv:2212.10560](https://arxiv.org/abs/2212.10560)):

1. Start with ~175 seed tasks (human-written instruction/output pairs).
2. Prompt a strong LLM to generate **new instructions** inspired by the seeds.
3. Use the same LLM to generate **outputs** for those instructions.
4. Filter for quality (dedup, length, coherence).
5. Iterate to build a large, diverse dataset.

**Stanford Alpaca** applied this pipeline using text-davinci-003 to generate 52 K instruction-
following examples, then fine-tuned LLaMA-7B. The result — trained for under $600 — produced
a chatbot that approached GPT-3.5 quality on many tasks.

The approach has been refined many times:
- **WizardLM:** Iteratively evolves instructions to increase complexity (Evol-Instruct).
- **Orca:** Uses system prompts to elicit step-by-step reasoning from the teacher.
- **OpenHermes:** Curates synthetic data from multiple teacher models with diverse prompting
  strategies.

### LIMA: "Less Is More for Alignment"

**Paper:** Zhou et al., *"LIMA: Less Is More for Alignment"*, 2023
([arXiv:2305.11206](https://arxiv.org/abs/2305.11206))

The **Superficial Alignment Hypothesis**: Almost all of a language model's knowledge and
capabilities are learned during pre-training. Alignment (instruction-following, safety,
format) is a **thin veneer** that can be taught with a surprisingly small number of examples.

**Evidence:** LIMA fine-tuned LLaMA-65 B on only **1,000 carefully curated examples** (no
RLHF, no PPO, no DPO) and produced outputs that human evaluators preferred over GPT-4
in 19 % of comparisons and rated as equivalent in another 24 %. Key findings:

- **Quality over quantity:** 1,000 excellent examples beat 52,000 mediocre ones.
- **Diversity matters:** The 1,000 examples were hand-picked for diversity of topics,
  formats, and difficulty levels.
- **No RLHF needed** for basic alignment — though RLHF still helps for safety.

LIMA permanently changed how the community thinks about fine-tuning data. It shifted the
focus from "how much data?" to "how good is the data?"

### Data Quality > Data Quantity: The Phi Series Lesson

**Microsoft Phi series** (Phi-1, Phi-1.5, Phi-2, Phi-3):

The Phi models are a masterclass in data-centric AI. Key principles:

1. **"Textbook-quality" data:** Training data is filtered and synthesised to match the
   clarity, structure, and pedagogical quality of university textbooks.
2. **Synthetic data as curriculum:** Phi-1 (1.3 B) was trained on code "textbooks"
   generated by GPT-3.5 and outperformed models 10× its size on HumanEval.
3. **Data mixtures matter:** Phi-2 (2.7 B) carefully blended web data with curated
   "textbook" and "exercise" data — and matched Llama 2-70 B on some reasoning benchmarks.
4. **Scale data quality, not just data quantity:** Phi-3-mini (3.8 B) matched Mixtral
   8×7B on multiple benchmarks, despite being 12× smaller.

The Phi lesson: **A 3 B model trained on excellent data can outperform a 70 B model trained
on internet noise.** This inverts the scaling laws — or rather, shows that scaling laws
apply to *effective training tokens*, not raw token count.

### Decontamination and Benchmark Leakage

As the community generates more synthetic data and trains on larger web crawls, a serious
problem has emerged: **benchmark contamination** — test set questions or answers appearing in
training data, artificially inflating evaluation scores.

**Types of contamination:**
- **Direct contamination:** Exact benchmark examples in training data.
- **Indirect contamination:** Paraphrased or semantically similar examples.
- **Temporal contamination:** Training data created after the benchmark, influenced by
  published benchmark questions/solutions.

**Detection methods (2024):**
- **N-gram overlap:** Simple but catches only exact matches.
- **Perplexity-based detection:** If a model has suspiciously low perplexity on a benchmark
  example, it may have seen it during training.
- **Guided instruction prompting:** Probing whether the model can identify the source dataset
  of a test question.
- **Performance-based detection (CONSTAT):** If performance on a benchmark doesn't generalise
  to rephrased versions, contamination is likely.
- **LiveBench:** A continuously refreshed benchmark designed to be contamination-free.

**Best practices for practitioners:**
1. Always check for n-gram overlap between your training data and evaluation benchmarks.
2. Use multiple benchmarks — contamination in one is unlikely to affect all.
3. Prefer dynamic benchmarks (LiveBench, Chatbot Arena) over static ones (MMLU, HellaSwag).
4. Report your decontamination methodology when publishing results.
5. Be skeptical of models that dramatically outperform their size class on specific benchmarks
   — the signal may be contamination, not capability.

---

## Putting It All Together: A Practical Fine-Tuning Recipe (2024)

For practitioners who want to fine-tune a model today, here is the standard stack:

```
1. Choose base model:     Llama 3 8B/70B, Qwen 2.5, Mistral 7B, etc.
2. Choose PEFT method:    QLoRA (4-bit NF4 + LoRA r=16-32)
3. Prepare data:          1K-50K high-quality instruction/output pairs
4. Training framework:    Axolotl / LLaMA-Factory / Unsloth / HF Trainer
5. Distributed strategy:  Single GPU? QLoRA. Multi-GPU? FSDP or DeepSpeed ZeRO-2.
6. Precision:             BF16 (if Ampere+), FP16 (otherwise)
7. Memory tricks:         Gradient checkpointing + accumulation (steps=4-16)
8. Evaluate:              Task-specific eval + held-out set + human evaluation
9. Deploy:                Merge LoRA weights → quantise to GGUF/AWQ → vLLM/Ollama
```

**Typical training times:**

| Model    | Method    | GPU         | Dataset   | Time     |
|----------|-----------|-------------|-----------|----------|
| 7-8 B    | QLoRA r16 | 1× RTX 4090 | 10 K examples | 2-4 hours |
| 13 B     | QLoRA r16 | 1× A100 40G  | 50 K examples | 8-12 hours |
| 70 B     | QLoRA r16 | 1× A100 80G  | 10 K examples | 24-48 hours |
| 70 B     | LoRA r32  | 8× A100 80G  | 100 K examples | 12-24 hours |

---

## Key Papers & Sources

### Core PEFT Papers
1. **LoRA** — Hu et al., 2021 — [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
2. **QLoRA** — Dettmers et al., 2023 — [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
3. **DoRA** — Liu et al., 2024 — [arXiv:2402.09353](https://arxiv.org/abs/2402.09353)
4. **Prefix Tuning** — Li & Liang, 2021 — [arXiv:2101.00190](https://arxiv.org/abs/2101.00190)
5. **Prompt Tuning** — Lester et al., 2021 — [arXiv:2104.08691](https://arxiv.org/abs/2104.08691)
6. **(IA)³** — Liu et al., 2022 — [arXiv:2205.05638](https://arxiv.org/abs/2205.05638)
7. **AdaLoRA** — Zhang et al., 2023 — [arXiv:2303.10512](https://arxiv.org/abs/2303.10512)
8. **PEFT Survey** — Xu et al., 2023 — [arXiv:2304.14999](https://arxiv.org/abs/2304.14999)

### Training Infrastructure
9. **ZeRO** — Rajbhandari et al., 2020 — [arXiv:1910.02054](https://arxiv.org/abs/1910.02054)
10. **ZeRO-Infinity** — Rajbhandari et al., 2021 — [arXiv:2104.07857](https://arxiv.org/abs/2104.07857)
11. **FSDP** — Zhao et al., 2023 — [pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/)
12. **Mixed Precision Training** — Micikevicius et al., 2018 — [arXiv:1710.03740](https://arxiv.org/abs/1710.03740)
13. **Gradient Checkpointing** — Chen et al., 2016 — [arXiv:1604.06174](https://arxiv.org/abs/1604.06174)

### Open-Weight Models
14. **Llama** — Touvron et al., 2023 — [arXiv:2302.13971](https://arxiv.org/abs/2302.13971)
15. **Llama 2** — Touvron et al., 2023 — [arXiv:2307.09288](https://arxiv.org/abs/2307.09288)
16. **Llama 3** — Meta AI, 2024 — [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)
17. **Mistral 7B** — Jiang et al., 2023 — [arXiv:2310.06825](https://arxiv.org/abs/2310.06825)
18. **Mixtral** — Jiang et al., 2024 — [arXiv:2401.04088](https://arxiv.org/abs/2401.04088)
19. **Qwen** — Bai et al., 2023 — [arXiv:2309.16609](https://arxiv.org/abs/2309.16609)
20. **DeepSeek-V2** — DeepSeek AI, 2024 — [arXiv:2405.04434](https://arxiv.org/abs/2405.04434)
21. **Yi** — 01.AI, 2024 — [arXiv:2403.04652](https://arxiv.org/abs/2403.04652)

### Synthetic Data & Alignment
22. **Self-Instruct** — Wang et al., 2022 — [arXiv:2212.10560](https://arxiv.org/abs/2212.10560)
23. **Alpaca** — Taori et al., 2023 — [crfm.stanford.edu/2023/03/13/alpaca.html](https://crfm.stanford.edu/2023/03/13/alpaca.html)
24. **LIMA** — Zhou et al., 2023 — [arXiv:2305.11206](https://arxiv.org/abs/2305.11206)
25. **Phi-1** — Gunasekar et al., 2023 — [arXiv:2306.11644](https://arxiv.org/abs/2306.11644)
26. **Phi-2** — Microsoft Research, 2023 — [microsoft.com/research/blog/phi-2](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/)
27. **Phi-3** — Abdin et al., 2024 — [arXiv:2404.14219](https://arxiv.org/abs/2404.14219)
28. **WizardLM (Evol-Instruct)** — Xu et al., 2023 — [arXiv:2304.12244](https://arxiv.org/abs/2304.12244)
29. **Orca** — Mukherjee et al., 2023 — [arXiv:2306.02707](https://arxiv.org/abs/2306.02707)

### Contamination & Evaluation
30. **Benchmark Contamination Survey** — 2024 — [arXiv:2406.04244](https://arxiv.org/abs/2406.04244)
31. **LiveBench** — White et al., 2024 — [arXiv:2406.19314](https://arxiv.org/abs/2406.19314)
32. **LLMSanitize** — 2024 — [arXiv:2403.19808](https://arxiv.org/abs/2403.19808)

### Tools & Libraries
33. **Hugging Face PEFT** — [github.com/huggingface/peft](https://github.com/huggingface/peft)
34. **bitsandbytes** — [github.com/TimDettmers/bitsandbytes](https://github.com/TimDettmers/bitsandbytes)
35. **DeepSpeed** — [github.com/microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed)
36. **Axolotl** — [github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl)
37. **Unsloth** — [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)
38. **LLaMA-Factory** — [github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

---

## Concepts for Knowledge Tree

1. Parameter-Efficient Fine-Tuning (PEFT)
2. Full Fine-Tuning (gradient computation, optimizer states)
3. Low-Rank Adaptation (LoRA)
4. Low-rank matrix factorisation (A and B matrices)
5. LoRA rank selection and ablation
6. LoRA alpha scaling factor
7. LoRA weight merging (adapter fusion)
8. Multi-LoRA serving (S-LoRA, LoRAX)
9. QLoRA (Quantized LoRA)
10. NormalFloat4 (NF4) quantisation
11. Double quantisation
12. Paged optimisers (CPU offloading)
13. DoRA (Weight-Decomposed LoRA)
14. Weight decomposition (magnitude vs direction)
15. Prefix tuning (learnable key/value prefixes)
16. Prompt tuning (soft token embeddings)
17. (IA)³ (learned activation scaling)
18. AdaLoRA (adaptive rank allocation)
19. DeepSpeed ZeRO (Stage 1, 2, 3, Infinity)
20. Optimizer state partitioning
21. Gradient partitioning
22. Parameter partitioning / sharding
23. CPU and NVMe offloading
24. Fully Sharded Data Parallel (FSDP)
25. Mixed precision training (FP32, FP16, BF16, FP8)
26. Automatic Mixed Precision (AMP) / loss scaling
27. Gradient checkpointing (activation recomputation)
28. Gradient accumulation (effective batch size)
29. Open weights vs open source (OSI definition)
30. Llama model series (1, 2, 3)
31. Mistral / Mixtral (Sliding Window Attention, MoE)
32. Qwen series (multilingual, math/code)
33. DeepSeek (Multi-head Latent Attention, MoE)
34. Self-Instruct (synthetic instruction generation)
35. Knowledge distillation via synthetic data
36. Superficial Alignment Hypothesis (LIMA)
37. Textbook-quality data (Phi series)
38. Data quality vs data quantity trade-off
39. Benchmark contamination / data leakage
40. Decontamination methods (n-gram, perplexity, CONSTAT)
41. Dynamic benchmarks (LiveBench, Chatbot Arena)
42. Model licensing (Apache 2.0, MIT, Llama Community, CC BY-NC)
43. Evol-Instruct (WizardLM complexity evolution)
44. Mixture-of-Experts (MoE) sparse activation

---

*Last updated: 2025. Built from 15+ deep reads of primary papers, technical blogs, and
framework documentation.*
