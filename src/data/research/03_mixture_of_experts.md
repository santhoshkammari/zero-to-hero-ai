# Mixture of Experts: The Sparse Scaling Revolution

> *How conditional computation broke the "bigger model = slower inference" assumption and reshaped the economics of large language models.*

---

## Table of Contents

1. [Why This Matters](#why-this-matters)
2. [Historical Context](#historical-context)
3. [Core Architecture — Technical Deep Dive](#core-architecture--technical-deep-dive)
4. [Mixtral — The MoE That Changed Everything](#mixtral--the-moe-that-changed-everything)
5. [DeepSeek MoE — Extreme Sparsity](#deepseek-moe--extreme-sparsity)
6. [Router Deep Dive](#router-deep-dive)
7. [Engineering Challenges](#engineering-challenges)
8. [Impact & Where MoE Appears Now](#impact--where-moe-appears-now)
9. [Key Papers & Sources](#key-papers--sources)
10. [Concepts for Knowledge Tree](#concepts-for-knowledge-tree)

---

## Why This Matters

For years, the dominant paradigm in deep learning was simple: **make the model bigger, make it better**. The scaling laws discovered by Kaplan et al. (2020) showed that model performance improves predictably with parameter count, dataset size, and compute. But there was an uncomfortable corollary — a model with 10× the parameters requires roughly 10× the FLOPs at inference time. You could build GPT-4-class models, but serving them cost a fortune.

**Mixture of Experts (MoE) broke this assumption.**

The core insight is devastatingly simple: **not every input needs every parameter**. A 600-billion-parameter model can achieve its quality while activating only 20 billion parameters per token. The remaining parameters sit idle — *sparse*, waiting for the inputs that need them. The result:

- **Training is faster**: MoE models achieve the same loss as dense models with 2–7× less compute.
- **Inference is cheaper**: Only a fraction of parameters are active per forward pass.
- **Total capacity scales independently of per-token cost**: You can add more experts without increasing the compute per token.

This isn't a marginal optimization. MoE represents a **paradigm shift** from dense computation to conditional computation — the idea that different parts of a network should activate for different inputs. It's why DeepSeek-V3 (671B total, 37B active) can compete with models that cost 10× more to train. It's why Mixtral 8×7B (47B total, 13B active) outperformed Llama 2 70B while being faster to run. And it's why, as of 2025, virtually every frontier lab has adopted MoE as their default architecture.

The "bigger = slower" assumption is dead. **Bigger can now mean smarter without being slower.**

---

## Historical Context

### The Original MoE (Jacobs et al., 1991)

The Mixture of Experts concept predates deep learning as we know it. In 1991, Robert Jacobs, Michael Jordan, Steven Nowlan, and Geoffrey Hinton published **"Adaptive Mixtures of Local Experts"** — a paper that introduced the idea of a system composed of multiple specialist networks, each handling different subsets of the input space.

The original formulation was elegant:
- A set of **expert networks**, each a simple neural net
- A **gating network** that produces a probability distribution over experts
- The final output is a weighted combination of expert outputs

```
y = Σᵢ g(x)ᵢ · Eᵢ(x)
```

Where `g(x)ᵢ` is the gating weight for expert `i` and `Eᵢ(x)` is the output of expert `i`. Both the experts and the gating network are trained jointly via backpropagation. The gating network learns to *partition the input space*, assigning different regions to different experts.

This was fundamentally an **ensemble method with learned specialization** — each expert becomes responsible for a different "mode" of the data distribution. But in 1991, networks were small, and the computational savings of sparse activation were negligible.

### The Gap Years (1991–2016)

Between the original paper and the modern MoE revolution, two lines of research laid the groundwork:

1. **MoEs as Components (Eigen, Ranzato, Ilya, 2013)**: Rather than treating the entire model as a mixture of experts, this work explored using MoE as a *layer* within a deeper network. This was the crucial conceptual shift — MoE became a modular component you could insert into any architecture.

2. **Conditional Computation (Bengio et al., 2013–2015)**: Yoshua Bengio's group explored the idea of dynamically activating or deactivating network components based on the input. This established the theoretical framework for *sparse activation* — the notion that you don't need to run every parameter for every input.

### Shazeer et al. (2017) — MoE Meets Scale

The modern MoE era began with **"Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"** by Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean.

This paper made MoE practical at scale by applying it to a 137-billion-parameter LSTM (the dominant NLP architecture at the time). The key innovations:

- **Sparsity via top-k gating**: Instead of computing all experts for every input, only the top-k experts (by gating score) are activated. This makes the system genuinely sparse — if `g(x)ᵢ = 0`, expert `i` is never computed.
- **Noisy top-k gating**: Adding tunable Gaussian noise before the top-k selection to encourage exploration and load balancing.
- **Scaling to thousands of experts**: The paper demonstrated MoE layers with up to 4096 experts, achieving massive model capacity with manageable compute.

The gating mechanism introduced here became the template for all future work:

```
H(x)ᵢ = (x · Wg)ᵢ + StandardNormal() · Softplus((x · Wₙₒᵢₛₑ)ᵢ)    # Add noise
KeepTopK(v, k)ᵢ = vᵢ if vᵢ is in top k, else -∞                      # Sparsify
G(x) = Softmax(KeepTopK(H(x), k))                                      # Normalize
```

The results were compelling for machine translation, but the paper was honest about the challenges: training instability, communication overhead across devices, and difficulty balancing load across experts. These challenges would define the next seven years of MoE research.

### GShard (Lepikhin et al., 2020) — MoE for Transformers

**GShard** was Google's first major effort to bring MoE into the Transformer era. The paper scaled transformers beyond 600 billion parameters by replacing every other FFN layer with a MoE layer using top-2 gating.

Key contributions:
- **Top-2 routing with random second expert**: The highest-scoring expert is always chosen; the second expert is selected probabilistically proportional to its gating weight.
- **Expert capacity**: A fixed buffer size per expert, determined by `(tokens_per_batch / num_experts) × capacity_factor`. Tokens exceeding capacity are dropped (sent via residual connection to the next layer).
- **Parallel computation patterns**: GShard introduced efficient sharding strategies for distributing MoE layers across TPUs.

The concept of **expert capacity** was crucial — since tensor shapes must be statically determined at compile time (especially on TPUs), you can't dynamically resize buffers based on routing decisions. You must pre-allocate a fixed capacity per expert and accept that some tokens will overflow.

### Switch Transformer (Fedus et al., 2022) — Simplicity Wins

The **Switch Transformer** was a landmark paper that dramatically simplified MoE and proved that simple approaches work better than complex ones. Published by William Fedus, Barret Zoph, and Noam Shazeer at Google, it challenged several assumptions:

**Key insight: Top-1 routing is sufficient.** Previous work assumed you needed at least two experts per token to allow the gating network to learn meaningful routing. Switch Transformer showed that routing to a single expert works just as well, while being:
- Computationally cheaper (half the expert computation per token)
- Communication-efficient (tokens only travel to one device)
- Easier to balance (each token goes to exactly one expert)

The paper formalized the **expert capacity formula**:

```
Expert Capacity = (tokens_per_batch / num_experts) × capacity_factor
```

With capacity factors as low as 1.0–1.25 performing well. It also introduced:

- **Simplified load-balancing loss**: An auxiliary loss encouraging uniform routing.
- **Selective precision**: Training experts in bfloat16 while keeping the router in full precision (the router's softmax is sensitive to numerical precision).
- **Scaling to 1.6 trillion parameters**: The Switch-C model with 2048 experts, achieving 4× pre-training speedup over T5-XXL.

The Switch Transformer demonstrated that MoE's benefits hold across scales — from 2 experts to 2048, the fundamental tradeoffs remain consistent.

### The Scaling Wall: Dense Models Get Expensive

By 2023, the scaling wall for dense models had become a crisis:

| Model | Parameters | Training Cost (est.) | Active per Token |
|-------|-----------|---------------------|-----------------|
| GPT-3 | 175B | ~$4.6M | 175B (100%) |
| PaLM | 540B | ~$8–12M | 540B (100%) |
| Llama 2 70B | 70B | ~$2M | 70B (100%) |
| Mixtral 8×7B | 47B | Undisclosed | 13B (28%) |
| DeepSeek-V3 | 671B | ~$5.6M | 37B (5.5%) |

The economics are stark. DeepSeek-V3 has nearly 4× the total parameters of PaLM but uses only 7% of PaLM's active parameters per token — and was trained for potentially less cost. MoE didn't just bend the scaling curve; it broke it.

---

## Core Architecture — Technical Deep Dive

### What Is an "Expert"?

In the context of Transformer-based MoE, an **expert is simply a feed-forward network (FFN)**. Nothing more exotic. In a standard Transformer block, you have:

```
Attention → LayerNorm → FFN → LayerNorm
```

In an MoE Transformer block, the FFN is replaced by multiple FFNs (experts) plus a router:

```
Attention → LayerNorm → Router → [Expert₁, Expert₂, ..., Expertₙ] → Combine → LayerNorm
```

Each expert has the same architecture as the original FFN — typically two linear layers with a non-linearity (ReLU, SwiGLU, GELU):

```python
class Expert(nn.Module):
    def __init__(self, d_model, d_ff):
        self.w1 = nn.Linear(d_model, d_ff)
        self.w2 = nn.Linear(d_ff, d_model)
        self.act = nn.SiLU()

    def forward(self, x):
        return self.w2(self.act(self.w1(x)))
```

The crucial point is that **experts share no parameters with each other**. Each expert is an independent FFN. The self-attention mechanism, layer norms, embedding layers, and output projection are all **shared across tokens** regardless of routing. This is why Mixtral 8×7B has 47B total parameters, not 8×7B = 56B — the shared components (attention, embeddings) account for the difference.

### The Router / Gating Mechanism

The router is the brain of the MoE layer. It takes a token's hidden representation and decides which expert(s) should process it. The most common implementation is a simple linear layer followed by softmax:

```python
class Router(nn.Module):
    def __init__(self, d_model, num_experts, top_k):
        self.gate = nn.Linear(d_model, num_experts, bias=False)
        self.top_k = top_k

    def forward(self, x):
        # x: [batch_size, seq_len, d_model]
        logits = self.gate(x)                          # [batch_size, seq_len, num_experts]
        scores = F.softmax(logits, dim=-1)             # Probability distribution over experts
        top_k_scores, top_k_indices = scores.topk(self.top_k, dim=-1)
        top_k_scores = top_k_scores / top_k_scores.sum(dim=-1, keepdim=True)  # Renormalize
        return top_k_scores, top_k_indices
```

The router is learned jointly with the rest of the model — its parameters (the weight matrix `Wg`) are updated through standard backpropagation. The routing decision is **per-token, per-layer**: every token independently selects its experts at every MoE layer.

**Top-k routing** is the standard approach:
- **Top-1**: Each token goes to exactly one expert (Switch Transformer)
- **Top-2**: Each token goes to two experts, outputs weighted-summed (GShard, Mixtral)
- **Top-k (k > 2)**: More experts per token, higher compute, potentially more capacity

The MoE layer output for a single token is:

```
y = Σᵢ∈TopK gᵢ · Eᵢ(x)
```

Where `gᵢ` is the renormalized gating weight and `Eᵢ(x)` is the output of expert `i`.

### Load Balancing — Why Experts Collapse Without It

The single most critical challenge in MoE training is **expert collapse** (also called the "rich get richer" problem). Here's what happens without intervention:

1. Early in training, due to random initialization, some experts receive slightly more tokens than others.
2. Experts that process more tokens get more gradient signal and improve faster.
3. The router learns that these experts are better and sends *even more* tokens to them.
4. Other experts stagnate from lack of training signal.
5. The system converges to a state where 1–2 experts handle most tokens and the rest are wasted.

This is catastrophic — you've paid the memory cost of N experts but only use 1–2 of them. The solution is **auxiliary load-balancing losses**.

#### The Standard Auxiliary Loss

The most common formulation (from Switch Transformer) encourages each expert to receive an equal fraction of tokens:

```
L_balance = α · N · Σᵢ fᵢ · Pᵢ
```

Where:
- `N` = number of experts
- `fᵢ` = fraction of tokens routed to expert `i` (the actual distribution)
- `Pᵢ` = average router probability for expert `i` (the predicted preference)
- `α` = hyperparameter controlling the strength of the balance loss

This loss is minimized when routing is uniform (`fᵢ = 1/N` for all `i`). It's added to the main language modeling loss during training.

The hyperparameter `α` is critical:
- Too small → experts collapse, some experts dominate
- Too large → routing becomes too uniform, negating the benefit of specialization
- Typical values: 0.01 to 0.1

#### Router Z-Loss (ST-MoE)

The **ST-MoE** paper introduced an additional stabilizing mechanism: the **router z-loss**. This penalizes large logit values entering the gating softmax:

```
L_z = (1/B) · Σⱼ (log Σᵢ exp(xⱼ,ᵢ))²
```

Where `xⱼ,ᵢ` is the router logit for token `j` and expert `i`, and `B` is the batch size.

Why does this help? Large logits before softmax cause:
- **Numerical instability** in the exponential function
- **Very peaked distributions** that resist exploration
- **Rounding errors** that accumulate, especially in mixed-precision training

The z-loss keeps logit magnitudes small, leading to smoother probability distributions and more stable training. This is especially important when using bfloat16 for expert computation while keeping the router in float32.

### Capacity Factor and Token Dropping

In hardware-efficient MoE implementations, each expert has a fixed **capacity** — the maximum number of tokens it can process per batch. This is necessary because tensor shapes must be known at compile time (especially on TPUs and for efficient GPU kernels).

```
Expert Capacity = ⌈(tokens_per_batch / num_experts) × capacity_factor⌉
```

The **capacity factor** (CF) is a tunable hyperparameter:
- **CF = 1.0**: Perfectly balanced allocation, no buffer
- **CF = 1.25**: 25% buffer for imbalance (common default)
- **CF > 1.5**: Large buffer, more memory/communication overhead

When a token is routed to an expert that has reached capacity, the token is **dropped** — it passes through the layer via the residual connection without any expert processing. Token dropping is:
- **Lossy**: The token misses the FFN computation entirely
- **Surprisingly okay**: Switch Transformer showed quality holds with up to 10–11% token dropping
- **Potentially regularizing**: Random dropping during training may act like dropout
- **Bad at inference**: You generally set higher capacity factors during inference to avoid dropping

The capacity factor creates a fundamental tradeoff: higher CF → fewer dropped tokens but more wasted computation and memory; lower CF → more dropped tokens but leaner execution.

### Expert Utilization and Specialization

An important empirical question is: **what do experts actually learn?**

Research from the ST-MoE paper revealed:
- **Encoder experts** tend to specialize in syntactic/shallow patterns: punctuation, proper nouns, specific token types
- **Decoder experts** show less clear specialization, handling more semantic/task-level patterns
- **Multilingual models**: Despite intuition, experts do NOT specialize by language — load balancing ensures tokens from all languages reach all experts

This means experts are more like **general-purpose processors that develop slight preferences** rather than highly specialized modules. The specialization is real but subtle — more like preference than hard partitioning.

Scaling the number of experts shows **diminishing returns**:
- Going from 2 → 8 experts: significant quality improvement
- Going from 8 → 64 experts: moderate improvement
- Going from 64 → 256 experts: small improvement
- Going from 256 → 2048 experts: marginal improvement

But each expert added still contributes something, and the compute cost per token stays constant — you're only paying more memory.

---

## Mixtral — The MoE That Changed Everything

### Why Mixtral Was a Turning Point

Before Mixtral, MoE was seen as a Google-internal technique — something that worked on TPU pods but wasn't practical for the open-source community. Mixtral 8×7B, released by Mistral AI in December 2023, changed that narrative overnight. It was:

1. **Open-weight** (Apache 2.0 license)
2. **Practically deployable** (fit on consumer/prosumer hardware)
3. **Demonstrably superior** to models with 5× the active parameters
4. **Simple** — no exotic tricks, just solid MoE engineering

### Architecture Details

Mixtral 8×7B is architecturally identical to Mistral 7B, with one modification: **every FFN layer is replaced by a MoE layer with 8 experts**.

| Specification | Value |
|---------------|-------|
| **Total parameters** | 46.7B |
| **Active parameters per token** | ~12.9B |
| **Number of experts per layer** | 8 |
| **Experts selected per token** | 2 (top-2 routing) |
| **Number of layers** | 32 |
| **Hidden dimension** | 4096 |
| **FFN intermediate dimension** | 14336 (per expert) |
| **Attention heads** | 32 |
| **KV heads** | 8 (Grouped Query Attention) |
| **Context length** | 32,768 tokens |
| **Vocabulary size** | 32,000 |
| **Attention mechanism** | Sliding Window Attention (SWA) |

The naming "8×7B" is slightly misleading — it's not 8 copies of a 7B model. The shared components (attention, embeddings, layer norms) are common across all routing paths. Each expert is only the FFN portion (~5.6B parameters for 8 experts × ~700M per expert FFN), plus the shared components account for the rest.

### Top-2 Routing Per Token Per Layer

Mixtral uses straightforward top-2 routing:

1. For each token at each MoE layer, the router computes scores over all 8 experts
2. The top-2 experts by score are selected
3. Each expert processes the token independently
4. Outputs are weighted by the (renormalized) router scores and summed

```
y = g₁ · E_top1(x) + g₂ · E_top2(x)
```

Where `g₁ + g₂ = 1` after renormalization of the top-2 softmax scores.

This means that at each layer, a token can be processed by any 2 of 8 experts — giving C(8,2) = 28 possible combinations per layer. Across 32 layers, the combinatorial space of possible routing paths is enormous (28³² ≈ 10⁴⁶), allowing the model to express incredibly diverse computation patterns.

### Why It Beat Llama 2 70B with Less Compute

The performance comparison was striking:

| Benchmark | Mixtral 8×7B | Llama 2 70B |
|-----------|-------------|-------------|
| MMLU (5-shot) | 70.6% | 69.8% |
| GSM8K (math) | 74.4% | 56.8% |
| HumanEval (code) | 40.2% | 29.9% |
| ARC-Challenge | 85.8% | 85.1% |
| HellaSwag | 86.7% | 87.3% |
| TruthfulQA | 46.6% | 44.9% |

Mixtral matched or exceeded Llama 2 70B on most benchmarks while using only ~13B active parameters per token (versus 70B). The inference speed advantage is roughly 5× for the same batch size, and the per-token compute is 80% less.

Why does this work? Three factors:

1. **Parameter efficiency**: The 47B total parameters store more knowledge than a 13B dense model, even though only 13B are active at a time. Different experts can store different knowledge, and the router selects the relevant subset.

2. **Compute efficiency**: At inference, you're doing roughly 2 × 7B FFN computations per layer, plus the shared attention — so the actual FLOPs are similar to a ~12–14B dense model.

3. **Training signal**: During training, every expert receives gradient signal from a substantial fraction of tokens. With 8 experts and top-2 routing, each expert sees ~25% of tokens on average — enough to learn meaningful representations.

### Training Methodology

Mistral AI disclosed limited training details. What is known:
- Trained on a diverse multilingual corpus
- Pre-training followed standard autoregressive language modeling
- A fine-tuned instruction-following variant (Mixtral 8×7B Instruct) was released simultaneously
- The instruction variant used DPO (Direct Preference Optimization) for alignment
- The model demonstrated particularly strong multilingual, math, and code capabilities

---

## DeepSeek MoE — Extreme Sparsity

### The DeepSeekMoE Architecture

While Mixtral demonstrated that MoE works with 8 coarse-grained experts, DeepSeek took a radically different approach: **extreme fine-grained expert segmentation**. The core philosophy is that more, smaller experts allow for more flexible and precise routing.

The DeepSeekMoE architecture (introduced in the DeepSeekMoE paper, January 2024) has two key innovations:

#### 1. Fine-Grained Expert Segmentation

Instead of N experts with top-K routing, DeepSeekMoE uses **mN experts with top-mK routing**. The total expert capacity and compute stay the same, but each expert is smaller and the combinations are more flexible.

**Intuition**: Imagine you need to combine knowledge about "Python programming" and "scientific computing." With 8 coarse experts, you might get an expert that knows both but is imprecise at each. With 64 fine-grained experts, you can activate one expert specializing in Python syntax and another specializing in numerical methods — a more precise combination.

In DeepSeek-V2:
- 160 routed experts per layer (compared to Mixtral's 8)
- 6 experts activated per token
- Each expert is much smaller, but the total computation per token is similar

#### 2. Shared Expert Isolation

DeepSeekMoE introduces **shared experts** — a subset of experts that are always active for every token, regardless of routing decisions.

```
y = Σᵢ∈shared Eᵢ(x) + Σⱼ∈TopK gⱼ · Eⱼ(x)
```

The shared experts capture **common knowledge** that all tokens need (basic language structure, common patterns), freeing the routed experts to focus on **specialized knowledge** without redundancy. This is analogous to having a "general knowledge" module plus "specialist" modules.

### DeepSeek-V2: The MLA + MoE Combination

DeepSeek-V2 (May 2024) combined the DeepSeekMoE architecture with another innovation: **Multi-head Latent Attention (MLA)**.

| Specification | DeepSeek-V2 |
|---------------|-------------|
| **Total parameters** | 236B |
| **Active parameters** | 21B |
| **Routed experts per layer** | 160 |
| **Shared experts per layer** | 2 |
| **Active routed experts** | 6 |
| **Context length** | 128K |
| **KV cache compression** | 93.3% reduction via MLA |

MLA compresses the key-value cache into a low-dimensional **latent vector**, dramatically reducing the memory cost of long-context inference. The KV cache — typically the bottleneck for serving long sequences — was reduced by 93.3% compared to standard multi-head attention.

DeepSeek-V2 achieved performance comparable to or better than models 3× its active size, while reducing training cost by 42.5% compared to DeepSeek 67B (their previous dense model) and boosting inference throughput by 5.76×.

### DeepSeek-V3: 671B Total, 37B Active

DeepSeek-V3 (December 2024) scaled the architecture further and introduced several groundbreaking innovations:

| Specification | DeepSeek-V3 |
|---------------|-------------|
| **Total parameters** | 671B |
| **Active parameters** | 37B |
| **Experts per layer** | 256 routed + 1 shared |
| **Active routed experts** | 8 per token |
| **Training data** | 14.8 trillion tokens |
| **Training cost** | 2.788M H800 GPU hours (~$5.6M) |
| **Training stability** | Zero irrecoverable loss spikes, zero rollbacks |

#### Auxiliary-Loss-Free Load Balancing

Perhaps DeepSeek-V3's most important innovation is **eliminating the auxiliary load-balancing loss entirely**. Instead, they use a **bias term in the routing mechanism**:

Rather than adding a loss term to force uniform expert usage, DeepSeek-V3 adds a learnable bias to each expert's routing score. This bias is adjusted dynamically during training — if an expert is underutilized, its bias increases, making it more likely to be selected. If overutilized, the bias decreases.

This approach is superior because:
- **No hyperparameter tuning** for auxiliary loss weight (α)
- **No tension** between the main training objective and the balancing objective
- **More stable training** — the balance emerges naturally from the routing dynamics
- **Better expert utilization** — each expert receives tokens it's actually suited for, not tokens forced by a loss function

The results speak for themselves: DeepSeek-V3's training was remarkably stable, with **zero irrecoverable loss spikes** and **zero rollbacks** across the entire training run — an unprecedented achievement for a model of this scale.

#### Multi-Token Prediction (MTP)

DeepSeek-V3 was trained with a **multi-token prediction objective**: instead of predicting only the next token, the model learns to predict multiple future tokens simultaneously. This:
- Provides richer gradient signal per training step
- Forces the model to develop deeper sequential understanding
- Can be leveraged at inference time for speculative decoding (predicting several tokens in parallel)

#### Training Cost Revolution

The most eye-catching number: **2.788 million H800 GPU hours** for the complete training pipeline. At estimated H800 cloud rates, this translates to approximately $5.6 million — a fraction of what comparable models cost. For context, Meta reportedly spent $20–30M training Llama 3 405B (a dense model with lower benchmark scores).

This efficiency comes from the combination of:
- MoE sparsity (only 37B/671B parameters active per token)
- FP8 mixed-precision training
- Efficient pipeline parallelism and communication overlap
- Auxiliary-loss-free load balancing (no training instability overhead)

---

## Router Deep Dive

The router is the most researched and debated component of MoE. Every routing strategy involves a fundamental tradeoff: **specialization** (sending tokens to the best expert) versus **load balance** (spreading tokens evenly).

### Learned Routing (Token Choice)

The standard approach, used by Shazeer (2017), GShard, Switch Transformer, and Mixtral:

```
scores = Softmax(x · Wg)
top_k_experts = TopK(scores, k)
```

Each token "chooses" its experts based on learned router weights. This is the **token-choice** paradigm.

**Advantages:**
- Intuitive and simple
- Each token gets the experts most relevant to it
- Router learns useful specialization patterns

**Disadvantages:**
- Inherently prone to load imbalance (popular experts get overloaded)
- Requires auxiliary losses or capacity mechanisms
- Token dropping when experts are at capacity

### Hash Routing / Deterministic Routing

An alternative that eliminates learned routing entirely: assign tokens to experts based on a **deterministic function** (hash of token position, token identity, etc.).

The **BASE layers** paper (Lewis et al., 2021) explored routing based on token position within the sequence. **Hash routing** takes this further — using a hash function to distribute tokens pseudo-randomly.

**Advantages:**
- Perfect load balance by construction
- No auxiliary losses needed
- No trainable router parameters
- Extremely simple implementation

**Disadvantages:**
- No input-dependent specialization — routing ignores token content
- Generally worse quality than learned routing
- Can't adapt routing based on context

Hash routing establishes an important **lower bound** — it shows how much of MoE's benefit comes from having multiple experts at all (capacity) versus having the *right* expert for each input (routing quality). Surprisingly, hash routing works reasonably well, suggesting that a significant fraction of MoE's benefit comes from raw capacity rather than intelligent routing.

### Expert Choice Routing (Zhou et al., 2022)

A clever inversion of the standard approach: **instead of tokens choosing experts, experts choose tokens**.

In the standard (token-choice) paradigm:
- Each token selects its top-k experts
- Some experts get overloaded, others underutilized

In expert-choice routing:
- Each expert selects its top-k tokens from the entire batch
- Every expert processes exactly the same number of tokens (perfect balance)
- A single token can be routed to zero, one, or many experts

```python
# Token-choice: each token picks top-k experts
token_scores = softmax(tokens @ router_weights)  # [num_tokens, num_experts]
top_k_experts = token_scores.topk(k, dim=1)      # each token picks k experts

# Expert-choice: each expert picks top-k tokens  
expert_scores = softmax(tokens @ router_weights)  # [num_tokens, num_experts]
top_k_tokens = expert_scores.topk(k, dim=0)       # each expert picks k tokens
```

**Advantages:**
- **Perfect load balance** by construction (no auxiliary loss needed)
- **Variable computation per token**: Important tokens can be processed by many experts, trivial tokens by fewer
- **2× faster training convergence** than Switch Transformer top-1 (reported in the paper)
- **No token dropping**: Every expert is fully utilized

**Disadvantages:**
- A token might not be selected by any expert (requires residual fallback)
- Non-causal: experts see the entire batch, which can be problematic for autoregressive generation
- Communication patterns are less predictable

Expert-choice routing was validated at scale and showed improved training convergence time by more than 2× compared to Switch Transformer's top-1 routing, at the same computational cost.

### Soft MoE (Puigcerver et al., 2023)

**Soft Mixture of Experts** (from Google, published at ICLR 2024) takes a completely different approach: **fully differentiable, implicit soft assignment**.

Instead of hard routing decisions (token goes to expert A or expert B), Soft MoE computes weighted combinations of *all* tokens and passes these combinations to experts:

```
# Standard MoE: route individual tokens to specific experts
# Soft MoE: create "soft tokens" as weighted sums of all tokens

dispatch_weights = softmax(tokens @ Φ)           # [num_tokens, num_slots]
soft_tokens = dispatch_weights.T @ tokens          # weighted combinations
expert_outputs = experts(soft_tokens)              # process soft tokens
combine_weights = softmax(tokens @ Φ)             # combine back
final_output = combine_weights @ expert_outputs    # reconstruct per-token outputs
```

Each expert processes a **fixed number of "slots"** — synthetic inputs that are weighted combinations of all real tokens. This eliminates:
- Token dropping (all information is preserved through soft combinations)
- Load imbalance (each expert gets exactly the same number of slots)
- Training instability (no hard routing decisions, fully differentiable)
- The need for auxiliary losses

**Results in vision**: Soft MoE Huge/14 with 128 experts had 40× more parameters than ViT Huge/14 with only 2% increased inference time and substantially better quality. It outperformed both dense Transformers (ViTs) and standard MoEs (Tokens Choice, Experts Choice).

**Limitations:**
- Primarily validated in vision (ViT), not yet widely adopted for language models
- The soft combination means tokens lose their individual identity within expert processing
- Computation of dispatch/combine weights scales with sequence length × number of slots

### Why Routing Decisions Matter

The choice of routing strategy has profound implications:

1. **Specialization vs. uniformity**: Learned routing enables experts to specialize; hash routing forces uniformity. The ideal is somewhere between — experts should specialize, but not to the point of collapse.

2. **Training dynamics**: Hard routing decisions (top-k) create non-differentiable boundaries. The model must learn to route tokens correctly, but incorrect routing means the wrong expert processes the token, giving unhelpful gradients. Soft MoE avoids this by making routing fully differentiable.

3. **Inference efficiency**: At inference (especially autoregressive generation), routing one token at a time is common. Token-choice routing works naturally here; expert-choice and soft MoE require adaptation for single-token inference.

4. **Communication patterns**: In distributed settings, routing determines which tokens need to be sent to which devices. Predictable routing → less communication overhead. Expert-choice gives perfectly balanced communication; token-choice can create hotspots.

---

## Engineering Challenges

MoE models are theoretically elegant but brutally difficult to engineer at scale. The gap between "MoE on a single GPU" and "MoE across a thousand GPUs" involves solving some of the hardest systems problems in deep learning.

### Expert Parallelism Across GPUs

The standard parallelism strategies (data, tensor, pipeline) all have MoE-specific variants:

**Data Parallelism**: Each GPU has a copy of all experts, data is split across GPUs. Simple but defeats the purpose — you need enough memory per GPU to hold all experts.

**Tensor Parallelism**: Each expert is split across multiple GPUs. Works but creates fine-grained communication for every expert computation.

**Expert Parallelism**: The MoE-native approach. Different experts live on different GPUs. Each GPU hosts a subset of experts. Tokens are routed to the GPU that holds their target expert.

```
GPU 0: Experts 0, 1       GPU 1: Experts 2, 3
GPU 2: Experts 4, 5       GPU 3: Experts 6, 7
```

In practice, **hybrid parallelism** is used — combining expert parallelism for MoE layers with data parallelism for shared layers (attention, embeddings). The shared layers are replicated across GPUs; the expert layers are distributed.

### All-to-All Communication Overhead

Expert parallelism requires **all-to-all communication** — every GPU needs to send tokens to every other GPU (since any token might be routed to any expert). This is the most expensive collective operation:

```
Step 1: Route tokens (each GPU runs the router locally)
Step 2: All-to-All dispatch (send tokens to the GPUs hosting their target experts)
Step 3: Expert computation (each GPU processes tokens with its local experts)
Step 4: All-to-All combine (send expert outputs back to the originating GPUs)
```

The communication volume scales with `batch_size × hidden_dim × num_gpus`. For large clusters, this can become the bottleneck. Mitigation strategies include:

- **Communication-computation overlap**: Start sending tokens for layer N while computing layer N-1
- **Hierarchical all-to-all**: First communicate within a node (NVLink), then across nodes (InfiniBand)
- **Reduced precision for communication**: Send activations in bfloat16/FP8 even if computation is in FP32
- **Topology-aware routing**: FasterMoE (2022) showed that routing tokens preferentially to experts on nearby GPUs reduces communication latency by up to 17×

### Load Balancing in Distributed Training

Load balancing in a distributed MoE has two dimensions:

1. **Token balance**: Each expert should receive roughly the same number of tokens (handled by auxiliary losses or expert-choice routing)
2. **Compute balance**: Each GPU should do roughly the same amount of work (requires even distribution of experts + balanced routing)

If expert 0 receives 50% of all tokens and expert 7 receives 2%, GPU 0 becomes a bottleneck while GPU 3 sits idle — even though the auxiliary loss says overall balance is "fine" (because balance is measured globally, not per-GPU).

Solutions:
- **Capacity factors**: Hard limit on tokens per expert per GPU
- **Dynamic expert replication**: Popular experts are replicated to additional GPUs (at the cost of memory)
- **Load-aware routing**: Route tokens considering current expert load, not just affinity
- **DeepSeek-V3's bias term approach**: Adjusts routing biases dynamically based on actual utilization

### Inference Optimization for MoE

MoE inference has unique challenges compared to dense models:

#### The Memory Problem
All experts must be loaded in memory, even though only a fraction are active. Mixtral 8×7B requires ~90GB in FP16 (equivalent to a 47B dense model) but only activates ~13B parameters per token. You pay the memory cost of the full model but only use a fraction.

#### Expert Offloading
For deployment on limited hardware, **expert offloading** stores inactive experts on CPU memory or disk and loads them to GPU on demand:

- Predict which experts will be needed (using the router)
- Prefetch those experts to GPU while computing the current layer
- Evict unused experts back to CPU

This enables running large MoE models on hardware that couldn't fit all experts simultaneously, at the cost of latency from CPU→GPU transfers.

#### Expert Caching
Build on offloading: maintain a **cache of recently-used experts** on GPU. Since routing patterns exhibit temporal locality (certain experts are activated more frequently for certain types of text), caching can achieve high hit rates:

- LRU (Least Recently Used) caching of experts on GPU
- Predictive prefetching based on router scores from previous layers
- Hierarchical caching: hot experts on GPU, warm experts in CPU RAM, cold experts on disk

#### Batching for MoE Inference
Standard batched inference is less efficient for MoE because different tokens in the batch may route to different experts, creating small, irregular matrix multiplications. Solutions:

- **Token grouping**: Group tokens by their routing decisions to create larger, more efficient batches per expert
- **MegaBlocks kernels**: Express MoE layers as **block-sparse matrix operations** that handle variable-size expert assignments efficiently on GPUs
- **Padding and wasted compute**: Accept some wasted computation by padding expert batches to uniform sizes

#### Speculative Decoding with MoE
MoE models are natural candidates for speculative decoding: use a smaller dense model (or a single-expert subset) to speculate several tokens, then verify with the full MoE model. DeepSeek-V3's multi-token prediction training objective directly enables this.

### MegaBlocks: Efficient Sparse Training

**MegaBlocks** (November 2022, Stanford/NVIDIA) addressed the GPU efficiency problem head-on. The key insight: traditional MoE implementations use **batched dense matrix multiplication**, which assumes all experts process the same number of tokens. When token assignments are imbalanced (they always are), this wastes computation on padding.

MegaBlocks instead expresses MoE layers as **block-sparse matrix operations**:
- Variable-size token assignments per expert are packed into a sparse matrix
- GPU-optimized block-sparse GEMM kernels process the irregular workload efficiently
- No token dropping is needed — all tokens are processed regardless of imbalance

This approach achieved significant speedups over standard MoE implementations and is now incorporated into frameworks like Megatron-LM.

### FasterMoE: Topology-Aware Routing

**FasterMoE** (March 2022) analyzed MoE performance in distributed systems and found that network topology matters enormously:

- GPUs within a node communicate via NVLink (fast)
- GPUs across nodes communicate via InfiniBand (slower)
- The all-to-all pattern doesn't distinguish between near and far GPUs

FasterMoE introduced **topology-aware gating**: when multiple experts have similar scores, prefer the expert hosted on a nearby GPU. This reduced end-to-end training latency by up to 17× on large clusters, with minimal quality impact.

---

## Impact & Where MoE Appears Now

### The 2024–2025 MoE Landscape

MoE has gone from "Google's internal technique" to "everyone's default architecture" in roughly two years. Here's the current landscape:

#### Mixtral Series (Mistral AI)
- **Mixtral 8×7B** (Dec 2023): 47B total, 13B active, 8 experts, top-2. The model that proved MoE works open-source.
- **Mixtral 8×22B** (Apr 2024): 141B total, 39B active, 8 experts, top-2. Scaled up version competing with GPT-4-class models.

#### DeepSeek Series
- **DeepSeekMoE 16B** (Jan 2024): 16B total, ~2.8B active, 64 experts. Proved fine-grained MoE.
- **DeepSeek-V2** (May 2024): 236B total, 21B active, 160 experts. MLA + MoE combination.
- **DeepSeek-V3** (Dec 2024): 671B total, 37B active, 256 experts. Auxiliary-loss-free, multi-token prediction.

#### Qwen3 (Alibaba Cloud, 2025)
- **Qwen3-30B-A3B**: 30B total, 3B active, 128 experts, top-8
- **Qwen3-235B-A22B**: 235B total, 22B active, 128 experts, top-8
- Notable for using 128 experts with 8 active — an even more sparse configuration than most

#### Grok-1 (xAI, March 2024)
- 314B total parameters, 8 experts per layer, top-2 routing (~79B active)
- 64 transformer layers, released under Apache 2.0
- The largest open-weight MoE at time of release

#### DBRX (Databricks, March 2024)
- 132B total parameters, 16 experts, top-4 routing
- "Fine-grained" MoE with more experts and more active experts than Mixtral
- 36B active parameters, optimized for enterprise use cases

#### Snowflake Arctic (Snowflake, April 2024)
- **Hybrid Dense-MoE architecture**: 10B dense transformer + 128-expert MoE MLP
- 480B total parameters, 17B active (top-2 gating)
- Designed for enterprise tasks (SQL generation, coding)
- Demonstrates the trend toward domain-specific MoE models

#### Jamba (AI21 Labs, March 2024)
- Hybrid SSM-Transformer-MoE architecture
- Combines Mamba (State Space Model) blocks with MoE Transformer blocks
- 52B total parameters, 12B active
- Novel: first model to combine SSM with MoE

### Multimodal MoE Models

MoE has expanded beyond text:

- **LLaVA-MoE (2024)**: Extends the LLaVA vision-language model with MoE layers. Different experts can specialize in visual reasoning vs. textual understanding, improving efficiency for multimodal tasks.

- **Unified-IO 2 (Allen AI)**: Multimodal MoE handling text, images, audio, and actions with expert specialization across modalities.

- **MoE in diffusion models**: Recent work applies MoE to image generation, where different experts handle different visual concepts or styles.

### MoE in Vision: V-MoE

**V-MoE (Vision MoE)**, published by Google in 2021, was the first major application of MoE to computer vision. It applied sparse MoE to the Vision Transformer (ViT):

- **Architecture**: Standard ViT with FFN layers replaced by MoE layers
- **Scale**: Up to 15B parameters, achieving 90.35% on ImageNet
- **Efficiency**: Matched state-of-the-art dense networks with as little as 50% of the compute at inference
- **Priority routing**: A novel extension allowing the model to prioritize certain image patches over others, enabling adaptive per-image compute

V-MoE demonstrated that MoE's benefits extend beyond NLP — the principle of conditional computation is universal.

### The Trend: "Everyone Uses MoE Now"

As of mid-2025, the landscape is clear:

1. **All frontier labs have adopted MoE** or are actively developing MoE models
2. **The sparse-to-dense ratio is increasing**: From Mixtral's 28% activation (13B/47B) to DeepSeek-V3's 5.5% (37B/671B)
3. **Fine-grained experts are winning**: The trend moves from 8 coarse experts to 128–256 fine-grained experts
4. **MoE + other innovations**: MoE is being combined with MLA (DeepSeek), SSMs (Jamba), multi-token prediction, and novel attention mechanisms
5. **Infrastructure has caught up**: Frameworks like Megatron-LM, DeepSpeed, and vLLM now have first-class MoE support for training and inference

The question is no longer "should we use MoE?" but "how should we configure our MoE?" The dense model may soon be the exception rather than the rule for frontier-scale AI.

---

## Key Papers & Sources

### Foundational Papers

1. **Adaptive Mixtures of Local Experts** — Jacobs, Jordan, Nowlan, Hinton (1991)
   - https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf
   - The original MoE paper. Introduced expert networks with gating.

2. **Learning Factored Representations in a Deep Mixture of Experts** — Eigen, Ranzato, Sutskever (2013)
   - https://arxiv.org/abs/1312.4314
   - MoEs as components within deeper networks.

3. **Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** — Shazeer et al. (2017)
   - https://arxiv.org/abs/1701.06538
   - The paper that made MoE practical at scale. Top-k gating, noisy routing.

### Scaling and Architecture Papers

4. **GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding** — Lepikhin et al. (2020)
   - https://arxiv.org/abs/2006.16668
   - MoE for Transformers at 600B+ scale. Top-2 routing, expert capacity.

5. **Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** — Fedus, Zoph, Shazeer (2022)
   - https://arxiv.org/abs/2101.03961
   - Simplified MoE with top-1 routing. 1.6T parameter model. 4× speedup over T5-XXL.

6. **GLaM: Efficient Scaling of Language Models with Mixture-of-Experts** — Du et al. (2021)
   - https://arxiv.org/abs/2112.06905
   - GPT-3 quality at 1/3 the energy cost. Decoder-only MoE.

7. **ST-MoE: Designing Stable and Transferable Sparse Expert Models** — Zoph et al. (2022)
   - https://arxiv.org/abs/2202.08906
   - Router z-loss for stability. Expert specialization analysis. Fine-tuning insights.

### Routing Innovation Papers

8. **Mixture-of-Experts with Expert Choice Routing** — Zhou et al. (2022)
   - https://arxiv.org/abs/2202.09368
   - Experts choose tokens instead of tokens choosing experts. 2× faster convergence.

9. **From Sparse to Soft Mixtures of Experts** — Puigcerver et al. (2023, ICLR 2024)
   - https://arxiv.org/abs/2308.00951
   - Fully differentiable routing. Eliminates token dropping and load imbalance.

10. **BASE Layers: Simplifying Training of Large, Sparse Models** — Lewis et al. (2021)
    - https://arxiv.org/abs/2103.16716
    - Balanced assignment of sparse experts. Linear assignment for optimal routing.

### Model-Specific Papers

11. **Mixtral of Experts** — Jiang et al. (2024)
    - https://arxiv.org/abs/2401.04088
    - 8×7B architecture. Top-2 routing. Outperforms Llama 2 70B.

12. **DeepSeekMoE: Towards Ultimate Expert Specialization** — Dai et al. (2024)
    - https://arxiv.org/abs/2401.06066
    - Fine-grained expert segmentation. Shared expert isolation.

13. **DeepSeek-V2: A Strong, Economical, and Efficient MoE Language Model** — DeepSeek-AI (2024)
    - https://arxiv.org/abs/2405.04434
    - MLA + DeepSeekMoE. 236B/21B active. 93.3% KV cache reduction.

14. **DeepSeek-V3 Technical Report** — DeepSeek-AI (2024)
    - https://arxiv.org/abs/2412.19437
    - 671B/37B active. Auxiliary-loss-free balancing. Multi-token prediction.

### Systems and Efficiency Papers

15. **MegaBlocks: Efficient Sparse Training with Mixture-of-Experts** — Gale et al. (2022)
    - https://arxiv.org/abs/2211.15841
    - Block-sparse GPU kernels for MoE. No token dropping.

16. **FasterMoE: Modeling and Optimizing Training of Large-Scale Dynamic Pre-Trained Models** — He et al. (2022)
    - https://dl.acm.org/doi/10.1145/3503221.3508418
    - Topology-aware gating. 17× speedup in distributed MoE training.

17. **Scaling Vision with Sparse Mixture of Experts (V-MoE)** — Riquelme et al. (2021)
    - https://arxiv.org/abs/2106.05974
    - 15B parameter vision model. 90.35% ImageNet. Priority routing.

### Surveys and Overviews

18. **A Survey on Mixture of Experts in Large Language Models** — Cai et al. (2024, TKDE 2025)
    - https://arxiv.org/abs/2407.06204
    - Comprehensive taxonomy of MoE designs, algorithms, and systems.

19. **Mixture of Experts Explained** — Sanseviero et al. (2023)
    - https://huggingface.co/blog/moe
    - Excellent practical guide to MoE concepts, training, and inference.

20. **Mixture-of-Experts Meets Instruction Tuning** — Shen et al. (2023)
    - https://arxiv.org/abs/2305.14705
    - MoEs benefit more from instruction tuning than dense models.

---

## Concepts for Knowledge Tree

1. **Mixture of Experts (MoE)** — Architecture using multiple specialist sub-networks with learned routing
2. **Sparse Activation** — Only activating a subset of model parameters per input
3. **Conditional Computation** — Dynamically selecting which computations to perform based on input
4. **Gating Network / Router** — Learned module that assigns tokens to experts
5. **Top-k Routing** — Selecting the k highest-scoring experts per token
6. **Expert Collapse** — Failure mode where most tokens route to few experts
7. **Auxiliary Load-Balancing Loss** — Extra loss term encouraging uniform expert utilization
8. **Router Z-Loss** — Penalty on large router logits for training stability
9. **Expert Capacity** — Fixed maximum number of tokens an expert can process per batch
10. **Capacity Factor** — Multiplier controlling the buffer size per expert
11. **Token Dropping** — Discarding tokens that exceed expert capacity limits
12. **Expert Parallelism** — Distributing different experts across different devices
13. **All-to-All Communication** — Collective operation shuffling tokens between devices for expert processing
14. **Fine-Grained Expert Segmentation** — Using many small experts instead of few large ones (DeepSeek)
15. **Shared Experts** — Always-active experts capturing common knowledge (DeepSeekMoE)
16. **Expert Choice Routing** — Experts select tokens instead of tokens selecting experts
17. **Soft MoE** — Fully differentiable routing via weighted token combinations
18. **Noisy Top-k Gating** — Adding noise before top-k selection for exploration
19. **Multi-head Latent Attention (MLA)** — KV cache compression via latent projection (DeepSeek)
20. **Auxiliary-Loss-Free Balancing** — Dynamic bias terms replacing explicit balance losses (DeepSeek-V3)
21. **Multi-Token Prediction** — Training objective predicting multiple future tokens
22. **Expert Offloading** — Storing inactive experts on CPU/disk, loading on demand
23. **Block-Sparse Operations** — GPU-efficient kernels for variable-size expert assignments (MegaBlocks)
24. **Topology-Aware Routing** — Preferring experts on nearby GPUs to reduce communication (FasterMoE)
25. **Expert Specialization** — The degree to which individual experts develop distinct competencies
26. **Dense-MoE Hybrid** — Architectures combining dense and MoE layers (Arctic, Jamba)
27. **Vision MoE (V-MoE)** — Applying sparse MoE to Vision Transformers
28. **MoE Distillation** — Compressing a sparse MoE into a smaller dense model
29. **Expert Merging / Aggregation** — Combining expert weights post-training to reduce inference cost
30. **Grouped Query Attention (GQA)** — Sharing KV heads across query heads, commonly paired with MoE

---

## Appendix: MoE Architecture Comparison Table

| Model | Year | Total Params | Active Params | Experts | Active/Token | Routing | Key Innovation |
|-------|------|-------------|---------------|---------|-------------|---------|----------------|
| Shazeer et al. | 2017 | 137B | ~2B | 4096 | Top-2 | Noisy top-k | First large-scale MoE |
| GShard | 2020 | 600B | ~15B | 2048 | Top-2 | Random 2nd expert | Parallel MoE on TPUs |
| Switch Transformer | 2021 | 1.6T | ~0.1B | 2048 | Top-1 | Simplified routing | Top-1 sufficient |
| GLaM | 2021 | 1.2T | ~97B | 64 | Top-2 | Learned gating | GPT-3 at 1/3 energy |
| V-MoE | 2021 | 15B | ~3B | 32 | Top-2 | Priority routing | MoE for vision |
| ST-MoE | 2022 | 269B | ~? | 64 | Top-2 | Z-loss stabilized | Stable training, analysis |
| Mixtral 8×7B | 2023 | 47B | 13B | 8 | Top-2 | Learned softmax | Open-weight MoE |
| Mixtral 8×22B | 2024 | 141B | 39B | 8 | Top-2 | Learned softmax | Scaled Mixtral |
| Grok-1 | 2024 | 314B | ~79B | 8 | Top-2 | Learned | Largest open MoE (at release) |
| DBRX | 2024 | 132B | 36B | 16 | Top-4 | Fine-grained | Enterprise MoE |
| Arctic | 2024 | 480B | 17B | 128 | Top-2 | Dense+MoE hybrid | Domain-specific MoE |
| DeepSeekMoE 16B | 2024 | 16B | 2.8B | 64 | Top-6 | Fine-grained | Expert segmentation |
| DeepSeek-V2 | 2024 | 236B | 21B | 160+2 | Top-6 | Fine-grained + shared | MLA + MoE |
| DeepSeek-V3 | 2024 | 671B | 37B | 256+1 | Top-8 | Aux-loss-free | Bias-term balancing, MTP |
| Qwen3-235B | 2025 | 235B | 22B | 128 | Top-8 | Learned | Thinking + non-thinking modes |
| Jamba | 2024 | 52B | 12B | 16 | Top-2 | Learned | SSM + MoE hybrid |

---

## Appendix: The Mathematics of MoE Routing

### Standard Gating Function

Given input token representation `x ∈ ℝᵈ` and router weight matrix `Wg ∈ ℝᵈˣⁿ` (where n is number of experts):

```
Router logits:   h = x · Wg                    ∈ ℝⁿ
Gating scores:   G(x) = Softmax(h)             ∈ ℝⁿ
Top-k selection: Ĝ(x) = TopK(G(x), k)         ∈ ℝⁿ  (zeros for non-selected experts)
Renormalization: ĝ(x) = Ĝ(x) / Σᵢ Ĝ(x)ᵢ      ∈ ℝⁿ
```

### MoE Layer Output

```
y = Σᵢ₌₁ⁿ ĝ(x)ᵢ · Eᵢ(x)
```

Since ĝ(x)ᵢ = 0 for non-selected experts, only k expert forward passes are computed.

### Noisy Top-k Gating (Shazeer 2017)

```
H(x)ᵢ = (x · Wg)ᵢ + ε · Softplus((x · Wₙₒᵢₛₑ)ᵢ)     where ε ~ N(0, 1)
G(x) = Softmax(KeepTopK(H(x), k))
```

### Auxiliary Load Balance Loss (Switch Transformer)

```
L_aux = α · N · Σᵢ₌₁ᴺ fᵢ · Pᵢ

where:
  fᵢ = (1/T) · Σⱼ₌₁ᵀ 𝟙[argmax G(xⱼ) = i]    (fraction of tokens routed to expert i)
  Pᵢ = (1/T) · Σⱼ₌₁ᵀ G(xⱼ)ᵢ                   (average router probability for expert i)
  T = total tokens in batch
  N = number of experts
```

This product `fᵢ · Pᵢ` is differentiable through `Pᵢ` (even though `fᵢ` involves argmax) and is minimized when both are uniform at 1/N.

### Router Z-Loss (ST-MoE)

```
L_z = (1/T) · Σⱼ₌₁ᵀ (log Σᵢ₌₁ᴺ exp(hⱼ,ᵢ))²
```

Penalizes large logit values, improving numerical stability especially with mixed-precision training.

### Expert Choice Formulation

Instead of `TopK` over experts (per token), apply `TopK` over tokens (per expert):

```
S = X · Wg                                    # [T × N] score matrix
For each expert i:
    selected_tokens_i = TopK(S[:, i], C)       # Select C highest-scoring tokens
    expert_output_i = Eᵢ(X[selected_tokens_i]) # Process selected tokens
```

Where C = expert capacity = T × k / N (guaranteed balanced).

### Soft MoE Formulation

```
Dispatch:  D = Softmax(X · Φ, dim=tokens)      # [T × S] dispatch weights
Slots:     Z = Dᵀ · X                           # [S × d] soft token combinations
Expert:    Y = MoE(Z)                            # [S × d] expert outputs
Combine:   C = Softmax(X · Φ, dim=slots)        # [T × S] combine weights  
Output:    O = C · Y                              # [T × d] final outputs
```

Where S = number of slots per expert × number of experts, and Φ ∈ ℝᵈˣˢ are learnable parameters.

---

*Last updated: 2025. This document synthesizes research from 20+ papers and technical sources to provide a comprehensive view of the MoE landscape.*
