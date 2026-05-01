# Efficient LLM Inference: Making Giants Run on Laptops

## Why This Matters

A 70-billion-parameter model in FP16 requires **140 GB** of memory just to store its weights. That exceeds the capacity of every consumer GPU and most professional ones. Serving such a model demands clusters of A100s or H100s costing $100K+. Yet the reasoning capabilities of these models are transformative—code generation, mathematical proof, multilingual translation, agentic workflows.

The central tension of 2024–2025 AI is this: **the most capable models are too expensive for most people to run**. Efficient inference techniques resolve this tension. They allow a 70B model to run on a gaming laptop, a 7B model to run on a phone, and production APIs to serve millions of users without bankrupting the operator.

This document covers the full stack of efficiency techniques—from the mathematics of quantization to the systems engineering of memory management—that make modern LLM deployment possible.

### The Inference Bottleneck: Memory, Not Compute

Before diving into solutions, we must understand the problem. Autoregressive LLM inference is fundamentally **memory-bandwidth bound**, not compute-bound.

During token generation, for each new token the model must:
1. Load all model weights from GPU HBM (High Bandwidth Memory) into compute units
2. Perform a relatively small matrix-vector multiplication (batch size 1)
3. Write results back

For a 7B parameter model in FP16:
- **Weights to load per token**: 14 GB
- **FLOPs per token**: ~14 GFLOPs (roughly 2 × parameter count)
- **A100 bandwidth**: 2 TB/s → can load weights in ~7ms
- **A100 compute**: 312 TFLOPS → could compute in ~0.05ms

The arithmetic intensity (FLOPs/byte) is approximately **1**—far below the ~150 ratio needed to saturate an A100's compute. This means **we are waiting on memory reads, not math**. Every byte we remove from model weights directly translates to faster inference.

This is why quantization works so well: reducing weights from 16-bit to 4-bit gives a near-linear **4× speedup** for token generation, because we're loading 4× fewer bytes through the bandwidth bottleneck.

---

## Quantization Fundamentals

### What Is Quantization?

Quantization maps high-precision floating-point numbers to lower-precision representations. In the context of neural networks, this primarily means converting model weights (and optionally activations) from their training precision to a smaller format.

**The precision hierarchy:**

```
FP32 (32 bits) → FP16/BF16 (16 bits) → INT8 (8 bits) → INT4 (4 bits) → INT2 (2 bits)
   4 bytes          2 bytes              1 byte          0.5 bytes       0.25 bytes
```

Each step roughly halves memory. A 70B model goes from:
- **FP32**: 280 GB (doesn't fit on any single GPU)
- **FP16**: 140 GB (needs 2× A100-80GB)
- **INT8**: 70 GB (fits on 1× A100-80GB)
- **INT4**: 35 GB (fits on consumer RTX 4090 with 24GB... almost)
- **Mixed INT4**: ~25-40 GB depending on method (fits on high-end consumer hardware)

### The Mathematics of Uniform Quantization

The simplest quantization scheme maps a continuous range [α, β] to N discrete levels:

```
Quantize:    q = round((x - z) / s)
Dequantize:  x̂ = q × s + z

where:
  s = (β - α) / (2^b - 1)     [scale factor]
  z = round(-α / s)            [zero point]
  b = target bit width
```

For **symmetric quantization** (common for weights centered near zero):
```
s = max(|x|) / (2^(b-1) - 1)
z = 0
```

For **asymmetric quantization** (handles skewed distributions):
```
s = (max(x) - min(x)) / (2^b - 1)
z = round(-min(x) / s)
```

**Example**: Quantizing to INT4 symmetric
- Weight range: [-0.5, 0.5]
- 4-bit signed range: [-8, 7] (or [-7, 7] for symmetric)
- Scale: 0.5 / 7 ≈ 0.0714
- Weight 0.3 → round(0.3 / 0.0714) = round(4.2) = 4
- Dequantized: 4 × 0.0714 = 0.286 (error: 0.014)

### Group Quantization

A single scale factor per entire tensor is too coarse—different regions have different distributions. **Group quantization** divides each weight matrix row into groups of g elements (typically g = 32, 64, or 128), with each group having its own scale and zero point.

```
For weight matrix W of shape [out_features, in_features]:
  Number of groups = in_features / g
  Each group: W[i, j:j+g] gets its own (scale, zero_point)
  
Storage: quantized_weights + (num_groups × 2 × param_size) for scales/zeros
```

Smaller groups → better accuracy, more overhead. The sweet spot is typically **g = 128** for INT4, providing a good balance between accuracy and storage overhead (scales stored in FP16 add ~0.375 bits per weight effectively).

### Why Low Precision Works: Weight Distributions

Neural network weights are not uniformly distributed. They follow approximately **Gaussian distributions** centered near zero, with most values clustered tightly:

```
Typical LLM weight distribution:
  - ~68% of weights fall within ±1 standard deviation
  - ~95% within ±2 standard deviations
  - ~99.7% within ±3 standard deviations
  - Long tails with rare but important outliers
```

This concentration means that 4-bit quantization with 16 discrete levels can represent the vast majority of weights with acceptable error. The information content of most weights is far below 16 bits.

Empirically, researchers have found that for well-trained LLMs:
- **FP32 → FP16**: Essentially lossless for inference
- **FP16 → INT8**: <1% perplexity increase with proper calibration
- **FP16 → INT4**: 1-3% perplexity increase with advanced methods (GPTQ, AWQ)
- **FP16 → INT3**: Noticeable degradation, requires careful handling
- **FP16 → INT2**: Significant quality loss, only viable for less critical layers

### The Outlier Problem

The biggest challenge in LLM quantization isn't the typical weights—it's the **outliers**. Transformers exhibit a peculiar phenomenon: certain channels (dimensions) in activations and weights develop values 10-100× larger than the mean.

These outliers are **systematic**: they appear in specific channels across all tokens and all layers. They emerge during training as the model learns to use these channels for important features (possibly related to attention sink mechanisms or residual stream norms).

**Why outliers break quantization:**
```
Without outliers: weights in range [-0.1, 0.1]
  INT4 step size: 0.2/15 ≈ 0.013 → fine granularity

With outlier: weights in range [-0.1, 5.0]
  INT4 step size: 5.1/15 ≈ 0.34 → most weights map to 0
  The 99.9% of weights near zero lose all resolution!
```

A single outlier can destroy quantization quality for an entire group or tensor.

### Post-Training Quantization (PTQ) vs Quantization-Aware Training (QAT)

**Post-Training Quantization (PTQ):**
- Quantize a pre-trained model without further training
- Uses a small calibration dataset (128-512 samples) to determine optimal scales
- Fast: minutes to hours, no GPU training required
- Methods: GPTQ, AWQ, SmoothQuant, round-to-nearest (RTN)
- Trade-off: may lose quality at very low bit-widths

**Quantization-Aware Training (QAT):**
- Simulate quantization during training/fine-tuning
- Model learns to be robust to quantization noise
- Uses "fake quantization" nodes: quantize → dequantize in forward pass, straight-through estimator for gradients
- Expensive: requires full training infrastructure
- Results: consistently better than PTQ, especially at INT4 and below

```python
# Fake quantization in forward pass (QAT)
def fake_quantize(x, scale, zero_point, bits=4):
    q_min, q_max = 0, 2**bits - 1
    x_q = torch.clamp(torch.round(x / scale + zero_point), q_min, q_max)
    x_dq = (x_q - zero_point) * scale  # dequantize
    return x_dq  # same dtype as input, but with quantization error

# Gradient flows through via straight-through estimator:
# d_loss/d_x ≈ d_loss/d_x_dq (pretend quantize is identity for backward)
```

**When to use which:**
- PTQ is the default for deploying existing models—fast and good enough
- QAT is used when building models specifically designed for edge/mobile deployment
- QAT is essential when pushing below 4 bits or when PTQ quality is unacceptable

---

## GPTQ — Gradient-Based Post-Training Quantization

### The OBS Foundation

GPTQ (Frantar et al., 2022) builds on the **Optimal Brain Surgeon (OBS)** framework from the 1990s neural network pruning literature. OBS provides a principled way to remove or modify weights while minimizing the impact on the loss function.

The key insight: when you quantize (modify) one weight, you can **compensate** by adjusting other weights. The optimal compensation is determined by the Hessian matrix of the loss with respect to the weights.

### Mathematical Framework

Consider a linear layer with weight matrix **W** ∈ ℝ^(d_out × d_in) and input matrix **X** ∈ ℝ^(n × d_in). The layer output is **Y = XW^T**.

The quantization objective is to find quantized weights **Ŵ** that minimize the squared error:

```
argmin_Ŵ ||WX^T - ŴX^T||²_F
```

This is equivalent to minimizing, for each row **w** of **W**:

```
argmin_ŵ (w - ŵ)^T H (w - ŵ)

where H = X^T X is the Hessian of the squared error
```

The Hessian **H** captures the sensitivity of the output to weight perturbations. A large diagonal entry H_ii means weight w_i is sensitive—quantization errors there will propagate strongly.

### The GPTQ Algorithm

GPTQ processes weights **column by column** (one input dimension at a time), performing three steps for each column:

```
For each column q = 1, 2, ..., d_in:
    1. QUANTIZE: Round w_q to nearest quantization level
       ŵ_q = quantize(w_q)
       
    2. ERROR: Compute quantization error
       δ_q = w_q - ŵ_q
       
    3. COMPENSATE: Update remaining unquantized columns
       w_{q+1:} -= δ_q × (H^{-1}_{q, q+1:} / H^{-1}_{qq})
```

Step 3 is the magic: it redistributes the quantization error from column q across all remaining columns q+1, ..., d_in, using the Hessian inverse to determine optimal redistribution weights.

**Why column-by-column?** Processing in order allows using a Cholesky decomposition of H^{-1}, which can be computed once and used incrementally—avoiding the O(d³) cost of full matrix inversion at each step.

### Block-Wise Processing

For practical efficiency, GPTQ processes columns in **blocks** of size B (typically B = 128):

```
For each block of B columns:
    1. Quantize all B columns using the OBS update within the block
    2. Apply the accumulated error correction to all remaining columns
    
This reduces memory access patterns and allows batched operations,
achieving ~3-4 hours for quantizing a 175B parameter model on a single GPU.
```

### Practical Performance

GPTQ achieves remarkable results at 4-bit quantization:

| Model | FP16 PPL | GPTQ-4bit PPL | Degradation |
|-------|----------|---------------|-------------|
| LLaMA-7B | 5.68 | 5.85 | +3.0% |
| LLaMA-13B | 5.09 | 5.20 | +2.2% |
| LLaMA-30B | 4.10 | 4.17 | +1.7% |
| LLaMA-65B | 3.53 | 3.58 | +1.4% |

The trend is clear: **larger models quantize better**. With more parameters, each individual weight carries less unique information, making quantization error more tolerable.

### GPTQ Limitations

- **Calibration sensitivity**: Results depend on the calibration data distribution
- **Order dependence**: Column ordering affects final quality (addressed by random permutation)
- **No activation quantization**: Only quantizes weights, activations remain in FP16
- **Static**: Quantization is fixed after calibration; doesn't adapt to input

---

## AWQ — Activation-Aware Weight Quantization

### The Key Insight: Not All Weights Are Equal

AWQ (Lin et al., 2023) starts from a powerful observation: **a small fraction of weights (0.1-1%) are disproportionately important for model quality**, and their importance can be identified by examining activation magnitudes.

The reasoning is straightforward. For a linear layer y = Wx:
- If activation x_j is consistently large across inputs, then weight column W[:,j] has outsized influence on the output
- Quantization error in W[:,j] gets amplified by the large activation
- These "salient" weights need protection

### Identifying Salient Weights

AWQ computes per-channel activation magnitudes from calibration data:

```
s_j = mean(|x_j|) across calibration samples

Salient channels: those where s_j is significantly above average
(typically top 1% of channels by activation magnitude)
```

### The Scaling Trick

Rather than keeping salient weights in higher precision (which complicates hardware), AWQ uses a clever **per-channel scaling** approach:

```
Original:  y = W × x
Scaled:    y = (W × diag(s)) × (diag(s)^{-1} × x)
         = W' × x'

where s is a per-channel scaling vector
```

By choosing scaling factors appropriately:
- **Salient weight channels are scaled up** before quantization → they get more quantization levels allocated to their actual range
- **Activations are scaled down** correspondingly → mathematically equivalent
- The quantization then naturally allocates more precision to the channels that matter

### Optimal Scale Search

AWQ searches for the optimal scaling factor per channel:

```
For each channel j:
    s*_j = argmin_s || Q(w_j × s) × (x_j / s) - w_j × x_j ||²
    
where Q(·) is the quantization function
```

This can be solved efficiently via grid search over a small range (typically s ∈ [0.1, 10] with ~20 candidates).

The key mathematical property: scaling doesn't change the full-precision result (it's mathematically identical), but it **changes the quantization grid alignment**, putting more resolution where it matters.

### AWQ vs GPTQ: When Each Wins

| Aspect | GPTQ | AWQ |
|--------|------|-----|
| **Approach** | Error compensation via Hessian | Protect salient weights via scaling |
| **Speed (quantization)** | Slower (Hessian computation) | Faster (simple scaling search) |
| **Speed (inference)** | Similar | Slightly faster (simpler dequant) |
| **Calibration data** | More sensitive | Less sensitive |
| **Quality at 4-bit** | Excellent | Excellent (often slightly better) |
| **Quality at 3-bit** | AWQ edges ahead | Better on very low bit |
| **Hardware friendliness** | Good | Excellent (no special dequant logic) |

**Rule of thumb**: AWQ tends to perform slightly better for very low-bit quantization (3-bit) and is faster to apply. GPTQ has a longer track record and extensive tooling. In practice, both achieve similar quality at 4-bit.

---

## SmoothQuant — Taming Activation Outliers

### The Activation Quantization Problem

GPTQ and AWQ only quantize **weights**. But for maximum throughput (especially with batched inference), quantizing **activations** to INT8 unlocks hardware-accelerated integer matrix multiplication (INT8 tensor cores are ~2× faster than FP16 on modern GPUs).

The problem: activation quantization is much harder than weight quantization because activations have extreme outliers in specific channels.

### The Migration Strategy

SmoothQuant (Xiao et al., 2022) introduces a mathematically elegant solution: **migrate the quantization difficulty from activations to weights**.

```
Original:     Y = X × W^T
Smoothed:     Y = (X × diag(s)^{-1}) × (diag(s) × W^T)
            = X̃ × W̃^T

where s_j = max(|X[:,j]|)^α / max(|W[j,:]|)^(1-α)
and α ∈ [0, 1] controls the migration strength (typically α = 0.5)
```

**Before smoothing:**
- Activations: extreme outliers in certain channels (range [-100, 100])
- Weights: well-behaved (range [-1, 1])
- Activations are hard to quantize, weights are easy

**After smoothing:**
- Activations: outliers reduced (range [-10, 10])
- Weights: slightly larger range (range [-10, 10])
- Both are moderately easy to quantize!

The transformation is mathematically lossless—only the quantization step introduces error. By equalizing the difficulty, both can be effectively quantized to INT8, enabling W8A8 (8-bit weights, 8-bit activations) inference with hardware acceleration.

---

## GGUF and the Local Inference Ecosystem

### The llama.cpp Revolution

In March 2023, Georgi Gerganov released **llama.cpp**—a C/C++ implementation of LLaMA inference that could run entirely on CPU. This was revolutionary because:

1. **No GPU required**: Pure CPU inference using AVX2/AVX-512/ARM NEON SIMD instructions
2. **Quantization built-in**: Models compressed from day one
3. **Minimal dependencies**: No Python, no PyTorch, no CUDA
4. **Cross-platform**: macOS, Linux, Windows, Android, iOS

llama.cpp democratized local LLM inference overnight, enabling millions of users to run LLMs on consumer hardware.

### The GGUF Format

**GGUF** (GGML Universal Format) is the successor to GGML, designed as a self-contained model format:

```
GGUF File Structure:
├── Magic Number ("GGUF")
├── Version (currently v3)
├── Metadata (key-value pairs)
│   ├── Architecture (llama, falcon, mpt, etc.)
│   ├── Context length
│   ├── Embedding dimension
│   ├── Number of layers
│   ├── Vocabulary and tokenizer data
│   ├── Quantization type per tensor
│   └── ... (all model hyperparameters)
├── Tensor Info (name, shape, dtype, offset for each tensor)
└── Tensor Data (the actual quantized weights, memory-mapped)
```

Key design choices:
- **Self-contained**: Everything needed for inference is in one file (no separate tokenizer files)
- **Memory-mappable**: Tensor data can be mmap'd directly, enabling instant model loading
- **Extensible**: New quantization types and architectures can be added without format changes
- **Alignment**: Data is aligned to allow efficient SIMD operations

### K-Quant Methods

The "k-quant" family represents llama.cpp's sophisticated quantization schemes, far more nuanced than simple round-to-nearest:

**Naming convention: Q{bits}_K_{size}**
- **Q**: Quantized
- **{bits}**: Primary bit width (2, 3, 4, 5, 6, 8)
- **K**: K-quant family (vs. older Q{bits}_0, Q{bits}_1 methods)
- **{size}**: S (Small), M (Medium), L (Large) — refers to accuracy/size trade-off

| Method | Bits/Weight | Model Size (7B) | Quality | Use Case |
|--------|-------------|-----------------|---------|----------|
| Q2_K | 2.63 | ~2.8 GB | Poor | Extreme compression only |
| Q3_K_S | 3.44 | ~3.4 GB | Acceptable | Memory-constrained |
| Q3_K_M | 3.91 | ~3.6 GB | Fair | Memory-constrained |
| Q4_K_S | 4.58 | ~4.1 GB | Good | Balanced default |
| **Q4_K_M** | **4.85** | **~4.4 GB** | **Very Good** | **Recommended default** |
| Q5_K_S | 5.52 | ~4.8 GB | Very Good | Quality-focused |
| Q5_K_M | 5.69 | ~5.0 GB | Excellent | Quality-focused |
| Q6_K | 6.57 | ~5.5 GB | Near-FP16 | Maximum quality |
| Q8_0 | 8.50 | ~7.2 GB | ≈FP16 | Essentially lossless |

**How K-quants achieve better quality:**

The "M" (mixed) variants use **importance-based mixed precision**:
- Attention layers (which are more sensitive) get higher precision (e.g., Q6_K)
- Feed-forward layers (more robust) get lower precision (e.g., Q4_K)
- The embedding and output layers often kept at higher precision
- This "mixed" strategy achieves better quality at the same average bit-width

**Block structure (Q4_K_M example):**
```
Each block of 256 weights:
  - 8 "super-blocks" of 32 weights each
  - Each super-block has its own 6-bit scale and 6-bit minimum
  - Weights are 4-bit within each super-block
  - Block-level scale and minimum stored in FP16
  
Effective bits/weight: 4 + overhead ≈ 4.85 bits
```

### Running 70B Models on Consumer Hardware

With GGUF quantization, previously impossible deployments become routine:

```
LLaMA-2-70B at Q4_K_M:
  - Size: ~40 GB
  - Runs on: 64GB RAM system (CPU) at ~3-5 tokens/sec
  - Runs on: 2× RTX 3090 (48GB VRAM total) at ~15-20 tokens/sec
  - Runs on: Mac M2 Ultra (192GB unified memory) at ~10-15 tokens/sec

LLaMA-2-7B at Q4_K_M:
  - Size: ~4.4 GB
  - Runs on: Raspberry Pi 5 (8GB) at ~2-3 tokens/sec
  - Runs on: iPhone 15 Pro at ~10-15 tokens/sec
  - Runs on: Any laptop with 8GB+ RAM
```

The **GPU offloading** feature in llama.cpp allows splitting layers between GPU and CPU—put as many layers on GPU as VRAM allows, overflow to CPU. This makes partial GPU acceleration available on any hardware combination.

---

## Knowledge Distillation for LLMs

### The Teacher-Student Framework at Scale

Knowledge distillation (Hinton et al., 2015) transfers capabilities from a large "teacher" model to a smaller "student" model. The student learns not just the correct answer, but the teacher's **probability distribution** over all possible answers—the "dark knowledge" in the soft labels.

For LLMs, the standard distillation loss combines:

```
L = α × L_KD + (1 - α) × L_CE

where:
  L_KD = KL(p_teacher(τ) || p_student(τ))   [distillation loss]
  L_CE = -Σ y_true × log(p_student)           [hard label loss]
  τ = temperature (typically 1-4)
  α = balancing weight (typically 0.5-0.9)
```

**Temperature scaling** softens the probability distributions:
```
p_i(τ) = exp(z_i / τ) / Σ_j exp(z_j / τ)

At τ = 1: normal softmax (peaky distribution)
At τ = 4: softened (more uniform, reveals inter-class relationships)
```

The soft labels contain rich information: when a teacher assigns 30% probability to "cat" and 5% to "tiger" for an image of a cat, the student learns that cats and tigers are visually similar—information absent from the hard label.

### Black-Box vs White-Box Distillation

**White-box distillation** requires full access to teacher internals:
- Match logit distributions (classic KD)
- Match intermediate hidden states (layer-by-layer alignment)
- Match attention patterns
- More efficient knowledge transfer
- Requires: open weights, matching architectures, significant compute

**Black-box distillation** only uses teacher outputs:
- Generate training data using the teacher (prompt → response pairs)
- Fine-tune student on teacher-generated data
- Can distill from closed-source APIs (GPT-4, Claude)
- Simpler but less efficient
- Example: Alpaca (Stanford) distilled GPT-3.5 outputs into LLaMA-7B

Most practical LLM distillation today is **black-box**: teams generate high-quality datasets using large models, then fine-tune smaller models on this data. This is sometimes called "synthetic data training" rather than distillation, but the mechanism is identical.

### Distilling Reasoning: DeepSeek R1 → R1-Distill

DeepSeek's R1 distillation (January 2025) represents a landmark in **reasoning distillation**:

**Teacher**: DeepSeek-R1 (671B MoE, 37B active per token)
- Trained with reinforcement learning to develop explicit chain-of-thought reasoning
- Produces long reasoning traces with self-reflection, verification, and backtracking

**Distillation process:**
1. Generate ~800,000 high-quality reasoning traces from R1 on diverse problems
2. Each trace includes explicit `<think>...</think>` reasoning steps
3. Fine-tune smaller dense models on these traces via supervised learning
4. **No RL used for student models**—pure supervised distillation

**Student models and results:**

| Student Model | Parameters | Base Architecture | AIME 2024 (pass@1) | MATH-500 |
|--------------|------------|-------------------|---------------------|----------|
| R1-Distill-Qwen-1.5B | 1.5B | Qwen2.5-1.5B | 28.9% | 83.9% |
| R1-Distill-Qwen-7B | 7B | Qwen2.5-7B | 55.5% | 92.8% |
| R1-Distill-Llama-8B | 8B | Llama-3.1-8B | 50.4% | 89.1% |
| R1-Distill-Qwen-14B | 14B | Qwen2.5-14B | 69.7% | 93.9% |
| R1-Distill-Qwen-32B | 32B | Qwen2.5-32B | 72.6% | 94.3% |

The R1-Distill-Qwen-32B **outperforms OpenAI's o1-mini** on multiple reasoning benchmarks—a distilled open-source model beating a proprietary frontier model. This demonstrates that reasoning capabilities can be effectively transferred through distillation.

### Distilling Capabilities vs Distilling Knowledge

An important distinction:

**Knowledge distillation**: Transfer factual knowledge (what the model knows)
- "Paris is the capital of France"
- Primarily captured in model parameters
- Requires similar or larger training data coverage

**Capability distillation**: Transfer reasoning patterns (how the model thinks)
- Chain-of-thought reasoning, self-verification, error correction
- Can be transferred with relatively few examples
- The reasoning pattern generalizes to new problems

DeepSeek R1 distillation is primarily **capability distillation**—the small models don't have the same factual knowledge as the 671B teacher, but they acquire the **reasoning methodology** (think step-by-step, verify, backtrack).

This is analogous to the difference between giving someone an encyclopedia (knowledge) versus teaching them the scientific method (capability). The latter is far more powerful per training dollar.

---

## Small Language Models (SLMs)

### The Paradigm Shift: Data Quality > Model Size

The SLM revolution of 2024 proved that **data quality dominates model size** for practical performance. A 3B model trained on carefully curated data can match or exceed a 70B model trained on raw web crawls for many tasks.

### The Phi Series (Microsoft): Textbook-Quality Data

Microsoft's Phi series is the canonical example of the "small but mighty" approach:

**Phi-1** (June 2023): 1.3B parameters
- Trained on "textbook quality" code data
- Outperformed models 10× its size on coding benchmarks
- Key insight: synthetic "textbook" data generated by GPT-4 for teaching

**Phi-2** (December 2023): 2.7B parameters
- Mixed textbook-quality web data + synthetic data
- Matched Llama-2-70B on reasoning benchmarks
- 25× smaller, comparable performance

**Phi-3** (April 2024): 3.8B / 7B / 14B parameters
- Phi-3-mini (3.8B): trained on 3.3 trillion tokens of heavily filtered data
- Phi-3-small (7B): trained on 4.8 trillion tokens
- **Two-phase training**:
  - Phase 1: General knowledge from curated web sources
  - Phase 2: Reasoning-heavy training with increased synthetic/instructional data
- Architecture: Standard decoder-only Transformer (similar to Llama-2)
- Post-training: SFT + DPO for alignment

**The data filtering pipeline:**
```
Raw Web Data (petabytes)
    ↓ LLM-based quality scoring
    ↓ Educational value filtering
    ↓ Deduplication (exact + near-duplicate)
    ↓ Safety filtering
    ↓ Diversity balancing
Curated Dataset (trillions of tokens, but much higher quality)
    ↓
    + Synthetic textbook data (from GPT-4)
    + Synthetic exercise/reasoning data
    ↓
Final Training Mix
```

The lesson from Phi: **you can compensate for fewer parameters by training on higher-quality data**. A 3.8B model seeing each high-quality token learns more per parameter than a 70B model seeing each low-quality token.

### Gemma (Google): Distilled Gemini Knowledge

Google's Gemma family brings Gemini-level knowledge to small form factors:

**Gemma 1** (February 2024): 2B and 7B parameters
- Decoder-only Transformer
- Trained on high-quality filtered web data
- SentencePiece tokenizer (32K vocabulary)
- 2K context window
- Optimized for efficient inference (INT8, BF16 quantization support)

**Gemma 2** (June 2024): 2B, 9B, and 27B parameters
- Novel architecture improvements (interleaving local and global attention)
- Knowledge distillation from larger Gemini models
- Significantly improved benchmark performance

**Key design decisions:**
- Aggressive data filtering using Gemini as a quality judge
- Emphasis on safety alignment (RLHF, red-teaming)
- Open weights with permissive licensing

### When SLMs Beat Large Models

SLMs don't just approximate large models—they **outperform** them in specific scenarios:

1. **Latency-critical applications**: A 3B model responds in 50ms; a 70B model takes 2 seconds. For real-time applications (autocomplete, live translation), the SLM wins.

2. **Domain-specific fine-tuning**: A 7B model fine-tuned on medical data outperforms GPT-4 on medical QA. Small models are easier and cheaper to specialize.

3. **On-device privacy**: Processing data locally eliminates data transmission. A phone-based SLM never sends your data to the cloud.

4. **Cost at scale**: Serving a 3B model costs ~50× less per token than serving a 175B model. At millions of queries per day, this dominates.

5. **Multi-model architectures**: Use SLMs for classification/routing, large models for complex reasoning. The SLM handles 90% of queries, the large model handles 10%.

### The Scaling Law Paradox

Chinchilla scaling laws (Hoffmann et al., 2022) predict optimal model size for a given compute budget. But these laws assumed **fixed data quality**. The Phi results suggest a modified scaling law:

```
Traditional:  L(N, D) = A/N^α + B/D^β + E
Phi insight:  L(N, D, Q) = A/N^α + B/(D×Q)^β + E

where Q is a data quality multiplier (Q > 1 for curated data)
```

Higher Q effectively multiplies your data budget, allowing smaller models to achieve the loss previously only achievable by larger models. This is a fundamental shift in how we think about model design.

---

## Speculative Decoding

### The Problem: Autoregressive Bottleneck

Standard LLM inference generates one token at a time, where each token requires a full forward pass through the model. For a 70B model, each forward pass takes ~50-100ms, limiting generation to ~10-20 tokens/second regardless of hardware parallelism.

The GPU is massively underutilized during single-token generation (arithmetic intensity ≈ 1, vs. ~150 needed for full utilization). **We're paying for all that compute capacity but only using a fraction.**

### The Speculative Decoding Solution

Speculative decoding (Leviathan et al., 2022; Chen et al., 2023) exploits a key asymmetry: **verifying a sequence is cheaper than generating it**.

**Core algorithm:**

```
Input: target model M_large, draft model M_small, prompt x

1. DRAFT: M_small generates K candidate tokens autoregressively
   [t₁, t₂, ..., t_K] = M_small.generate(x, K)
   Cost: K × (small model forward pass) ≈ cheap

2. VERIFY: M_large processes ALL K+1 positions in ONE forward pass
   [p₁, p₂, ..., p_{K+1}] = M_large.forward(x + [t₁, ..., t_K])
   Cost: 1 × (large model forward pass) ≈ same as generating 1 token

3. ACCEPT/REJECT: For each candidate token:
   If p_large(t_i) / p_small(t_i) ≥ random uniform:
       Accept t_i, continue to t_{i+1}
   Else:
       Reject t_i, sample replacement from adjusted distribution
       Stop checking remaining candidates

4. Output accepted tokens + one new token from adjusted distribution
```

**Why verification is cheap:** The large model processes all K candidate tokens in parallel (they're known, so attention can be computed in one batch), unlike generation where each token depends on the previous one.

### The Mathematical Guarantee

The acceptance-rejection scheme ensures that **the output distribution is identical to the large model's distribution**. This is not an approximation—it's mathematically exact.

```
Acceptance probability for token t_i at position i:
  accept_prob = min(1, p_large(t_i) / p_small(t_i))

If rejected, sample from adjusted distribution:
  p_adjusted(t) = max(0, p_large(t) - p_small(t)) / Z
  where Z normalizes the distribution
```

This is a **rejection sampling** scheme that provably produces samples from p_large, regardless of p_small's quality. If p_small closely matches p_large, most tokens are accepted and we get large speedups. If p_small is poor, we fall back to generating one token at a time (no worse than baseline).

### Speedup Analysis

Expected tokens per large model forward pass:
```
E[tokens] = 1/(1-α) × (1 - α^(K+1))

where α = average acceptance rate
      K = number of draft tokens
```

If draft model matches target 70% of the time (α = 0.7) with K = 5:
```
E[tokens] = (1/0.3) × (1 - 0.7^6) ≈ 3.33 × 0.882 ≈ 2.94 tokens per step
```

This gives roughly a **2-3× speedup** with no quality degradation. In practice, speedups of 2-3× are common for well-matched draft-target pairs.

### Medusa: Multiple Decoding Heads

**Medusa** (Cai et al., 2024) eliminates the need for a separate draft model by adding lightweight "heads" directly to the target model:

```
Standard Transformer:
  hidden_states → lm_head → next_token_logits

Medusa Transformer:
  hidden_states → lm_head    → token_0 logits (standard next token)
               → medusa_head_1 → token_1 logits (2 tokens ahead)
               → medusa_head_2 → token_2 logits (3 tokens ahead)
               → medusa_head_3 → token_3 logits (4 tokens ahead)

Each medusa_head is a small MLP (1-2 layers, same hidden dim)
```

**Advantages over standard speculative decoding:**
- No separate draft model needed (simpler deployment)
- Draft and verify share the same forward pass
- Medusa heads add <1% parameters
- Tree-structured verification: generate multiple candidate continuations and verify them all in one pass

**Tree attention in Medusa:**
Rather than a single draft sequence, Medusa considers a **tree** of possible continuations (top-k from each head), then uses a modified attention mask to verify the entire tree in one forward pass. This significantly increases the expected number of accepted tokens.

---

## KV Cache Optimization

### What Is the KV Cache?

In autoregressive generation, each token needs to attend to all previous tokens. Without caching, generating the N-th token requires recomputing attention for all N-1 previous tokens—O(N²) total work for generating N tokens.

The **KV cache** stores the Key and Value projections of all previously processed tokens:

```
For each layer l, at step t:
  K_cache[l] = [K₁, K₂, ..., K_t]   # shape: [t, num_heads, head_dim]
  V_cache[l] = [V₁, V₂, ..., V_t]   # shape: [t, num_heads, head_dim]

New token only computes:
  q_new = W_Q × x_new              # query for new token
  k_new = W_K × x_new              # new key
  v_new = W_V × x_new              # new value
  
  K_cache[l].append(k_new)
  V_cache[l].append(v_new)
  
  attention = softmax(q_new @ K_cache[l]^T / √d) @ V_cache[l]
```

This reduces per-token computation from O(N) to O(1) for the projection step (though attention still scales with sequence length).

### Why the KV Cache Is a Bottleneck

The KV cache grows linearly with sequence length and **dominates memory** for long contexts:

```
KV Cache Size = 2 × num_layers × num_heads × head_dim × seq_len × dtype_size

For LLaMA-2-70B (FP16) at 4096 tokens:
  = 2 × 80 × 64 × 128 × 4096 × 2 bytes
  = 10.7 GB per sequence!

For 128K context (GPT-4 level):
  = 2 × 80 × 64 × 128 × 131072 × 2 bytes
  = 343 GB per sequence!!
```

With batched serving (multiple users), the KV cache for each concurrent user compounds. Serving 100 users with 4K context on a 70B model requires **over 1 TB** of KV cache memory alone.

### Multi-Query Attention (MQA)

**Multi-Query Attention** (Shazeer, 2019) is the most aggressive KV cache reduction technique:

```
Standard Multi-Head Attention:
  Q: [batch, seq, num_heads, head_dim]
  K: [batch, seq, num_heads, head_dim]    # separate K per head
  V: [batch, seq, num_heads, head_dim]    # separate V per head

Multi-Query Attention:
  Q: [batch, seq, num_heads, head_dim]    # multiple query heads
  K: [batch, seq, 1, head_dim]            # SINGLE K shared across all heads
  V: [batch, seq, 1, head_dim]            # SINGLE V shared across all heads
```

**KV cache reduction: num_heads × smaller** (e.g., 64× for LLaMA-2-70B)

This is a dramatic reduction—but it can hurt model quality because all attention heads are forced to use identical K/V representations, reducing the model's ability to attend to different aspects of the input simultaneously.

**Models using MQA**: PaLM, Falcon, StarCoder

### Grouped Query Attention (GQA)

**Grouped Query Attention** (Ainslie et al., 2023) is the practical compromise between full Multi-Head Attention and Multi-Query Attention:

```
Full MHA:  num_kv_heads = num_q_heads        (e.g., 64 KV heads)
MQA:       num_kv_heads = 1                   (1 KV head)
GQA:       num_kv_heads = num_q_heads / G     (e.g., 8 KV heads with G=8)

Each KV head serves a GROUP of G query heads:
  Q heads [0..7]  → share KV head 0
  Q heads [8..15] → share KV head 1
  ...
  Q heads [56..63] → share KV head 7
```

**KV cache reduction: G × smaller** (8× for G=8)

GQA achieves nearly the same quality as full MHA while providing significant memory savings. It has become the **de facto standard** for new LLMs:

**Models using GQA**: LLaMA-2 (70B), LLaMA-3, Mistral, Gemma 2, Phi-3

For LLaMA-2-70B with GQA (8 KV heads instead of 64):
```
KV Cache (GQA) = 2 × 80 × 8 × 128 × 4096 × 2 = 1.34 GB  (vs. 10.7 GB for MHA)
```

### Paged Attention (vLLM)

**Paged Attention** (Kwon et al., 2023) applies operating system memory management principles to KV cache management:

**The fragmentation problem:**
In naive implementations, KV cache memory is pre-allocated for the maximum possible sequence length. A request that uses 100 tokens wastes memory allocated for 4096 tokens—**97.5% wasted**.

```
Naive allocation:
  Request 1: [####............] (100/4096 tokens used = 2.4% utilization)
  Request 2: [########........] (200/4096 tokens used = 4.9% utilization)
  Request 3: [##..............] (50/4096 tokens used = 1.2% utilization)
  
  Average memory utilization: ~3%
```

**Paged Attention solution:**
KV cache is divided into fixed-size **pages** (blocks), each holding K/V for a fixed number of tokens (e.g., 16 tokens per page). Pages are allocated on-demand and can be non-contiguous in physical memory.

```
Page Table (like OS virtual memory):
  Logical sequence    →  Physical pages
  Request 1: [0,1,2,3,4,5,6]    →  pages [17, 42, 3, 89, 12, 55, 31]
  Request 2: [0,1,2,...,12]      →  pages [6, 78, 23, ...]
  
  Pages allocated only when needed
  Pages freed when request completes
  No pre-allocation waste!
```

**Benefits:**
- **Near-zero memory waste**: Pages allocated exactly as needed
- **Memory sharing**: Requests with shared prefixes (system prompts) can share physical pages (copy-on-write)
- **Efficient batching**: Pack more concurrent requests per GPU
- **Dynamic memory**: Handle variable-length sequences without pre-allocation

**Impact**: vLLM achieves **2-4× higher throughput** than naive serving approaches, primarily by serving more concurrent requests with the same GPU memory.

### Sliding Window Attention

**Sliding Window Attention** (used by Mistral, Longformer) restricts each token to attending only to a local window of W preceding tokens:

```
Full attention:          Token i attends to tokens [0, 1, ..., i]
Sliding window (W=4096): Token i attends to tokens [max(0,i-4096), ..., i]

For position i = 10000 with W = 4096:
  Full attention: attend to 10000 tokens
  Sliding window: attend to 4096 tokens
```

**KV cache benefit**: Only need to store W tokens of KV cache, regardless of total sequence length. The cache becomes a **ring buffer**:

```
Ring buffer KV cache (W = 4096):
  Position 0-4095:    fill normally
  Position 4096:      overwrite position 0
  Position 4097:      overwrite position 1
  ...
  
  Memory is constant: O(W) instead of O(N)
```

**Information propagation**: Even though each token only attends locally, information propagates through layers. After L layers with window W, information from token j can reach token i if |i - j| ≤ L × W. For typical LLMs with 32 layers and W = 4096, effective context reaches 131,072 tokens.

**Mistral 7B** uses sliding window attention with W = 4096, achieving strong long-context performance while keeping KV cache bounded.

---

## Flash Attention: Memory-Efficient Exact Attention

### The IO Bottleneck

Standard attention implementation materializes the full N × N attention matrix in GPU HBM:

```
Standard attention:
  S = Q @ K^T          # [N, N] matrix — stored in HBM
  P = softmax(S)        # [N, N] matrix — stored in HBM
  O = P @ V            # [N, d] — stored in HBM

Memory: O(N²) for the attention matrix
For N = 32K: 32768² × 2 bytes = 2 GB per head per layer!
```

The attention matrix is computed in HBM, read back for softmax, written again, then read for the V multiplication. Each step involves slow HBM reads/writes.

### Flash Attention: Tiling for SRAM

**FlashAttention** (Dao et al., 2022) computes exact attention without ever materializing the N × N matrix, using IO-aware tiling:

```
Algorithm (simplified):
  Split Q into blocks of size B_r (row blocks)
  Split K, V into blocks of size B_c (column blocks)
  
  For each Q block:
    Initialize running softmax statistics (max, sum)
    For each K, V block:
      Load Q block, K block, V block into SRAM
      Compute block attention: S_block = Q_block @ K_block^T
      Update running softmax max and sum (online softmax)
      Compute partial output: O_block += softmax_block @ V_block
    Rescale output with final softmax statistics
    Write O block to HBM
```

**Key innovations:**
1. **Online softmax**: Compute softmax incrementally across blocks without needing the full row
2. **No N² materialization**: Only block-sized attention matrices exist, fitting in SRAM
3. **Minimal HBM access**: Q, K, V are each read from HBM once; O is written once

**Block sizes** are chosen to exactly fill available SRAM (typically ~100KB per streaming multiprocessor on modern GPUs).

**Performance impact:**
- **Memory**: O(N) instead of O(N²)
- **Speed**: 2-4× faster than standard attention (fewer HBM accesses)
- **Enables**: Longer context lengths without running out of memory

**FlashAttention-2** (Dao, 2023) further optimized parallelism and reduced non-matmul FLOPs, achieving near-optimal GPU utilization.

---

## Putting It All Together: The Efficient Inference Stack

The techniques in this document compose to form a complete efficient inference stack:

```
Layer 1: Model Architecture
  └── GQA/MQA (reduce KV cache by 8-64×)
  └── Sliding window attention (bound KV cache at O(W))
  └── Efficient FFN designs (SwiGLU, etc.)

Layer 2: Model Compression
  └── Quantization (GPTQ/AWQ/GGUF: 4× memory reduction)
  └── Knowledge distillation (10-100× parameter reduction)
  └── Pruning (structured/unstructured)

Layer 3: Inference Engine
  └── FlashAttention (2-4× attention speedup)
  └── Continuous batching (maximize throughput)
  └── Paged attention / vLLM (2-4× memory efficiency)
  └── Speculative decoding (2-3× generation speed)

Layer 4: Hardware Optimization
  └── CPU: AVX2/AVX-512/NEON SIMD (llama.cpp)
  └── GPU: Tensor cores, CUDA graphs
  └── Apple Silicon: Metal compute, unified memory
  └── Custom ASICs: Groq, Cerebras
```

**Example: Running LLaMA-3-70B on a laptop with 64GB RAM:**
1. GGUF Q4_K_M quantization → 40GB model size ✓
2. llama.cpp with SIMD optimization → efficient CPU inference ✓
3. Memory-mapped loading → instant startup ✓
4. Result: ~3-5 tokens/sec, usable for interactive chat

**Example: Serving 1000 concurrent users with LLaMA-3-8B:**
1. AWQ INT4 quantization → 5GB model fits on single GPU
2. vLLM with paged attention → handle 1000 concurrent KV caches
3. Continuous batching → maximize GPU utilization
4. GQA in model → 8× smaller KV cache per user
5. Result: Thousands of tokens/sec aggregate throughput on single A100

---

## Key Papers & Sources

### Foundational Papers
1. **"GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"** — Frantar et al., 2022. https://arxiv.org/abs/2210.17323
2. **"AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"** — Lin et al., 2023. https://arxiv.org/abs/2306.00978
3. **"SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"** — Xiao et al., 2022. https://arxiv.org/abs/2211.10438
4. **"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"** — Dao et al., 2022. https://arxiv.org/abs/2205.14135
5. **"FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"** — Dao, 2023. https://arxiv.org/abs/2307.08691
6. **"Efficient Memory Management for Large Language Model Serving with PagedAttention"** — Kwon et al., 2023. https://arxiv.org/abs/2309.06180
7. **"GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"** — Ainslie et al., 2023. https://arxiv.org/abs/2305.13245
8. **"Fast Transformer Decoding: One Write-Head is All You Need"** (Multi-Query Attention) — Shazeer, 2019. https://arxiv.org/abs/1911.02150

### Speculative Decoding
9. **"Fast Inference from Transformers via Speculative Decoding"** — Leviathan et al., 2022. https://arxiv.org/abs/2211.17192
10. **"Accelerating Large Language Model Decoding with Speculative Sampling"** — Chen et al., 2023. https://arxiv.org/abs/2302.01318
11. **"Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"** — Cai et al., 2024. https://arxiv.org/abs/2401.10774

### Knowledge Distillation
12. **"Distilling the Knowledge in a Neural Network"** — Hinton et al., 2015. https://arxiv.org/abs/1503.02531
13. **"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"** — DeepSeek-AI, 2025. https://arxiv.org/abs/2501.12948
14. **"A Survey on Knowledge Distillation of Large Language Models"** — 2023. https://arxiv.org/abs/2402.13116

### Small Language Models
15. **"Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone"** — Abdin et al., 2024. https://arxiv.org/abs/2404.14219
16. **"Gemma: Open Models Based on Gemini Research and Technology"** — Google DeepMind, 2024. https://arxiv.org/abs/2403.08295
17. **"Textbooks Are All You Need"** (Phi-1) — Gunasekar et al., 2023. https://arxiv.org/abs/2306.11644

### Scaling Laws & Efficiency
18. **"Training Compute-Optimal Large Language Models"** (Chinchilla) — Hoffmann et al., 2022. https://arxiv.org/abs/2203.15556
19. **"LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale"** — Dettmers et al., 2022. https://arxiv.org/abs/2208.07339
20. **"The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits"** (BitNet) — Ma et al., 2024. https://arxiv.org/abs/2402.17764

### Open-Source Tools & Implementations
21. **llama.cpp** — https://github.com/ggerganov/llama.cpp
22. **vLLM** — https://github.com/vllm-project/vllm
23. **GPTQ implementation** — https://github.com/IST-DASLab/gptq
24. **AWQ implementation** — https://github.com/mit-han-lab/llm-awq
25. **Hugging Face Optimum** — https://huggingface.co/docs/optimum

---

## Concepts for Knowledge Tree

1. **Quantization** — Reducing numerical precision of model parameters to decrease memory and compute requirements
2. **Post-Training Quantization (PTQ)** — Quantizing a pre-trained model without additional training using calibration data
3. **Quantization-Aware Training (QAT)** — Training with simulated quantization to produce models robust to precision reduction
4. **Symmetric Quantization** — Quantization where the zero point is fixed at zero, suitable for zero-centered distributions
5. **Asymmetric Quantization** — Quantization with a learnable zero point, handling skewed distributions
6. **Group Quantization** — Applying separate scale/zero-point parameters to subgroups of weights for finer granularity
7. **GPTQ** — Hessian-based post-training quantization using optimal brain surgeon error compensation
8. **AWQ (Activation-Aware Weight Quantization)** — Quantization that protects salient weights identified by activation magnitudes
9. **SmoothQuant** — Technique that migrates quantization difficulty from activations to weights via per-channel scaling
10. **GGUF Format** — Self-contained model file format for llama.cpp supporting quantized inference
11. **K-Quants** — Family of mixed-precision quantization methods in llama.cpp with importance-based bit allocation
12. **Knowledge Distillation** — Training a small student model to replicate a large teacher model's behavior
13. **Soft Labels / Dark Knowledge** — Teacher's output probability distribution containing inter-class relationship information
14. **Black-Box Distillation** — Distillation using only teacher outputs, not internal representations
15. **White-Box Distillation** — Distillation with access to teacher hidden states, attention maps, and gradients
16. **Reasoning Distillation** — Transferring chain-of-thought reasoning patterns from teacher to student
17. **Small Language Models (SLMs)** — Models under ~14B parameters designed for efficiency without sacrificing capability
18. **Data Quality Scaling** — The principle that data quality can compensate for model size in training effectiveness
19. **Speculative Decoding** — Using a fast draft model to propose tokens verified by a large target model
20. **Rejection Sampling (in speculative decoding)** — Acceptance criterion ensuring output matches target model distribution exactly
21. **Medusa Decoding** — Adding multiple lightweight prediction heads to enable parallel token verification
22. **KV Cache** — Stored key and value projections from previous tokens to avoid redundant computation
23. **Multi-Query Attention (MQA)** — Sharing a single KV head across all query heads to minimize cache size
24. **Grouped Query Attention (GQA)** — Sharing KV heads among groups of query heads as a compromise between MHA and MQA
25. **Paged Attention** — OS-inspired memory management for KV caches using fixed-size pages allocated on demand
26. **FlashAttention** — IO-aware tiled attention algorithm that avoids materializing the N×N attention matrix
27. **Sliding Window Attention** — Restricting attention to a local window of tokens for bounded memory and compute
28. **Memory-Bandwidth Bound** — The condition where inference speed is limited by data transfer rate, not computation
29. **Arithmetic Intensity** — Ratio of compute operations to memory accesses, determining the inference bottleneck
30. **Continuous Batching** — Dynamically adding/removing requests from a batch for maximum GPU utilization
31. **Weight Outliers** — Extreme-magnitude weights/activations that disproportionately harm quantization accuracy
32. **Straight-Through Estimator (STE)** — Gradient approximation treating quantization as identity in the backward pass
33. **Temperature Scaling (Distillation)** — Softening teacher output distributions to reveal inter-class relationships
34. **Synthetic Data Training** — Using LLM-generated data to train smaller models, a form of implicit distillation
35. **Mixed-Precision Inference** — Using different bit-widths for different layers based on sensitivity analysis
36. **CPU Inference (SIMD)** — Running LLMs on CPUs using vectorized instructions (AVX2, AVX-512, NEON)
37. **Unified Memory Architecture** — Apple Silicon design where CPU and GPU share memory, enabling efficient large model inference
38. **Model Sharding** — Splitting a model across multiple devices for inference when it exceeds single-device memory
