# Modern LLM Architecture: Beyond the Original Transformer

## Why This Matters

The 2017 paper "Attention Is All You Need" introduced the Transformer architecture that launched
the modern AI revolution. But if you look at what actually runs inside GPT-4, Llama 3, Mistral,
DeepSeek-V2, or Gemini — almost every component has been redesigned. The positional encodings
are different. The attention mechanism is different. The normalization is different. The activation
functions are different. Even the basic block structure has changed.

Today's frontier LLMs share the Transformer's DNA — self-attention over sequences — but the
engineering decisions that make them work at scale have diverged dramatically from the original
blueprint. Understanding these decisions is what separates someone who "knows about Transformers"
from someone who can actually reason about why a 70B-parameter model runs efficiently on 8 GPUs,
why it can handle 128K tokens of context, and why it generates coherent text at 100+ tokens
per second.

This document covers every major architectural decision in modern LLMs: from tokenization to
inference optimization. Each section explains not just *what* changed, but *why* — the engineering
constraints and empirical results that drove each evolution.

**The modern LLM recipe (as of 2024):**
- Byte-level BPE tokenization (32K–128K vocabulary)
- RoPE (Rotary Position Embeddings) for position encoding
- Grouped Query Attention (GQA) for efficient KV caching
- Pre-norm with RMSNorm for training stability
- SwiGLU activation in the FFN blocks
- Decoder-only architecture
- Cosine or WSD learning rate scheduling
- FlashAttention + PagedAttention for inference

Every one of these choices was earned through painful experimentation at scale. Let's understand why.

---

## Tokenization Evolution

Tokenization is the first decision in any LLM pipeline, and it's more consequential than most
people realize. The tokenizer determines how efficiently the model "sees" text, how well it
handles different languages, and even how much compute you spend per input.

### BPE (Byte-Pair Encoding): The Foundation

Byte-Pair Encoding was adapted from a data compression algorithm (Gage, 1994) and introduced
to NLP by Sennrich et al. (2015). The algorithm is elegantly simple:

1. Start with a vocabulary of individual characters
2. Count all adjacent pairs in the training corpus
3. Merge the most frequent pair into a new token
4. Repeat until you reach the desired vocabulary size

**Example:**
```
Corpus: "low lower lowest"
Step 1: Characters → {l, o, w, e, r, s, t, ...}
Step 2: Most frequent pair: (l, o) → merge into "lo"
Step 3: Most frequent pair: (lo, w) → merge into "low"
...continues until vocab size reached
```

The brilliance of BPE is that common words become single tokens (efficient), while rare words
get broken into subword pieces (no out-of-vocabulary problem). "unbreakable" might become
["un", "break", "able"] — each piece is meaningful.

**Limitation:** Classic BPE operates at the character level and is case-sensitive. It doesn't
handle Unicode characters in a language-agnostic way, which matters enormously for multilingual
models.

### SentencePiece: Language-Agnostic Tokenization

Google's SentencePiece (Kudo & Richardson, 2018) solved the multilingual problem by treating
the input as a raw byte stream — including whitespace as a regular symbol (represented as ▁).

Key innovations:
- **No pre-tokenization required.** Classic BPE assumes text is already split into words by
  whitespace. SentencePiece works on raw sentences, making it essential for languages without
  word boundaries (Japanese, Chinese, Thai).
- **Supports both BPE and Unigram LM** algorithms for building the vocabulary.
- **Unicode-aware** by design, handling any writing system.

SentencePiece became the tokenizer of choice for models like T5, LLaMA, and many multilingual
LLMs. It enabled training a single model that handles English, Chinese, Arabic, and code
simultaneously.

### Byte-Level BPE: No Unknown Tokens, Ever

GPT-2 introduced byte-level BPE, which operates on raw bytes (0-255) rather than Unicode
characters. This is a subtle but powerful change:

```
Traditional BPE:  text → Unicode characters → merge pairs → tokens
Byte-level BPE:   text → UTF-8 bytes → merge pairs → tokens
```

**Why this matters:**
- **Every possible input is representable.** There's no "unknown token" — even binary data,
  corrupted text, or novel emoji can be tokenized.
- **Robustness.** The model never encounters something it literally can't represent.
- **Universality.** All languages, all scripts, all encodings work through the same 256 base
  byte vocabulary.

**Tradeoff:** Byte-level tokens don't always align with linguistic units. A Chinese character
might be 3 bytes, meaning 3 base tokens before any merging. This makes the initial vocabulary
less "meaningful" but the merging process recovers efficiency for common patterns.

### tiktoken: Production-Grade Speed

OpenAI's tiktoken is the tokenizer behind GPT-3.5, GPT-4, and the ChatGPT API. It implements
byte-level BPE with a Rust backend optimized for production:

- **3-6x faster** than equivalent Python tokenizers
- Exposes specific encoding schemes: `cl100k_base` (GPT-4), `o200k_base` (GPT-4o)
- Designed for token counting and cost estimation in API contexts

tiktoken isn't architecturally novel — it implements the same byte-level BPE algorithm — but
its engineering matters because tokenization speed directly impacts serving latency.

### Tokenizer-Free Approaches: The Byte-Level Frontier

A growing research direction asks: what if we skip tokenization entirely?

**ByT5 (Google, 2021):**
- Processes raw UTF-8 bytes directly — every byte is a "token"
- No tokenizer, no vocabulary, no preprocessing pipeline
- Handles all languages, scripts, and even binary data natively
- **Problem:** Sequences become ~4x longer (each character = 1-4 bytes), making attention
  quadratically more expensive

**MegaByte (Google DeepMind, 2023):**
- Solves the sequence length problem with a hierarchical approach
- Chunks bytes into fixed-size groups (e.g., 128 bytes)
- A local model processes within chunks; a global model processes across chunks
- Can handle sequences up to **1 million bytes** efficiently
- Demonstrates that tokenizer-free models can match tokenizer-based models at scale

**Why this matters for the future:** Tokenizers are a source of brittleness. They create
artifacts (tokenization boundaries affect model behavior), they're language-biased (English
gets more efficient tokenization than most languages), and they add a preprocessing step
that can fail. Byte-level models eliminate all of this.

### Vocabulary Size: A Critical Hyperparameter

The choice of vocabulary size creates a fundamental tension:

| Vocab Size | Sequence Length | Embedding Table | Softmax Cost | Multilingual Coverage |
|------------|----------------|-----------------|--------------|----------------------|
| 8K         | Long           | Small (~16MB)   | Fast         | Poor                 |
| 32K        | Medium         | Medium (~64MB)  | Medium       | Good                 |
| 50K        | Medium-Short   | Large (~100MB)  | Slower       | Good                 |
| 100K       | Short          | Very Large      | Expensive    | Excellent            |
| 128K+      | Very Short     | Huge            | Very Expensive| Excellent           |

**Real-world choices:**
- GPT-2: 50,257 tokens (byte-level BPE)
- LLaMA: 32,000 tokens (SentencePiece)
- LLaMA 3: 128,000 tokens (tiktoken-style)
- GPT-4: 100,000 tokens (cl100k_base)
- Gemma: 256,000 tokens

**The engineering tradeoff:**
- **Larger vocabulary** → shorter sequences → less compute per example → but larger embedding
  table and more expensive softmax output layer
- **Smaller vocabulary** → longer sequences → more compute in attention (quadratic) → but
  smaller embedding table and cheaper output layer

The trend is toward larger vocabularies (100K+) because:
1. Modern hardware handles large softmax efficiently
2. Shorter sequences mean less KV cache memory during inference
3. Better coverage of multilingual text and code
4. Each token carries more semantic information

---

## Positional Encoding Evolution

Transformers process all tokens in parallel — they have no inherent notion of sequence order.
Without positional encoding, "the cat sat on the mat" and "mat the on sat cat the" would produce
identical representations. Positional encoding is how we inject sequence order into the model.

### Absolute Sinusoidal: The Original (2017)

The original Transformer used fixed sinusoidal functions:

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

Each position gets a unique vector, added to the token embedding. Different dimensions
oscillate at different frequencies, creating a unique "fingerprint" for each position.

**Problems:**
- Fixed maximum sequence length (determined at training time)
- No extrapolation — performance degrades rapidly beyond training length
- Position information is *added* to semantic information, creating interference

### Learned Positional Embeddings

BERT and GPT-2 used learned position embeddings — a trainable lookup table mapping position
index to a vector. This is simple and works well within the training length.

**Problems remain:**
- Still fixed maximum length (512 for BERT, 1024-2048 for early GPT)
- No extrapolation beyond training length
- Position 0 and position 1023 have no meaningful geometric relationship

### RoPE (Rotary Position Embeddings): The Modern Standard

RoPE, introduced by Su et al. (2021) in the RoFormer paper, is now the dominant position
encoding in modern LLMs (LLaMA, Mistral, Qwen, Gemma, and many more). It works by
**rotating** query and key vectors rather than adding a position vector.

**The core idea:**
Instead of adding position information to embeddings, RoPE *rotates* query (Q) and key (K)
vectors in 2D subspaces by an angle proportional to their position.

**How it works mathematically:**

For a d-dimensional embedding, RoPE treats consecutive pairs of dimensions as 2D planes.
For each pair (x₁, x₂) at position m:

```
[x₁']   [cos(mθ)  -sin(mθ)] [x₁]
[x₂'] = [sin(mθ)   cos(mθ)] [x₂]
```

Where θ is a frequency that varies by dimension:
```
θᵢ = 10000^(-2i/d)     for dimension pair i
```

Low-frequency dimensions capture long-range position; high-frequency dimensions capture
fine-grained local position.

**Why RoPE won:**

1. **Relative position encoding.** When computing attention scores (dot product of rotated Q
   and K), the rotation angles subtract: the score depends only on the *relative* distance
   between positions, not their absolute positions. This is exactly what attention needs.

2. **No additional parameters.** RoPE is a deterministic transformation — no learned weights.
   This means zero additional memory cost.

3. **Graceful with context extension.** Because RoPE encodes relative position, it can be
   extended beyond training length with techniques like:
   - **Position interpolation:** Scale position indices to fit within training range
   - **NTK-aware scaling:** Adjust the base frequency to handle longer contexts
   - **YaRN (Yet another RoPE extensioN):** Combines interpolation and NTK scaling
   - **Dynamic NTK:** Adapt frequency scaling based on sequence length

4. **Hardware-friendly.** Rotation is just a matrix multiplication on 2D pairs — extremely
   efficient on GPUs and TPUs.

**Context length extension with RoPE:**
```
Original LLaMA:        4,096 tokens (trained length)
With position interp:  32,768 tokens (8x extension)
With YaRN:            128,000 tokens (32x extension)
Code Llama:           100,000 tokens (with fine-tuning)
```

This is why RoPE determines context length — the encoding scheme dictates how far the model
can "see" and how gracefully it degrades beyond its training distribution.

### ALiBi (Attention with Linear Biases)

ALiBi (Press et al., 2021) takes a completely different approach: it adds no position encoding
to embeddings at all. Instead, it modifies attention scores directly.

**How ALiBi works:**
```
AttentionScore(i,j) = Q_i · K_j - m · |i - j|
```

Each attention head has a fixed slope `m` (a head-specific constant). Tokens farther apart
get a linear penalty subtracted from their attention score. Different heads use different
slopes, allowing some heads to focus locally and others globally.

**Key property:** ALiBi requires *zero* learned parameters and *zero* extra computation
beyond the bias addition. It extrapolates extremely well to longer sequences because the
linear penalty is well-defined at any distance.

**ALiBi vs RoPE:**

| Property              | RoPE                          | ALiBi                        |
|-----------------------|-------------------------------|------------------------------|
| Where applied         | Q and K vectors (rotation)    | Attention scores (additive)  |
| Parameters            | None (deterministic)          | None (fixed slopes)          |
| Relative encoding     | Yes (through rotation)        | Yes (through distance bias)  |
| Extrapolation         | Good (with extensions)        | Excellent (native)           |
| Used in               | LLaMA, Mistral, Qwen, Gemma  | BLOOM, MPT                   |
| Dominance (2024)      | **Winner**                    | Less common                  |

**Why RoPE won over ALiBi:** Despite ALiBi's simpler extrapolation story, empirical results
at large scale showed RoPE achieving better perplexity. Combined with context extension
techniques (YaRN, NTK scaling), RoPE achieves both good extrapolation and strong base
performance. The field converged on RoPE as the default.

---

## Attention Variants

The attention mechanism is the heart of the Transformer, and it's also the biggest bottleneck
for inference. Modern LLMs have redesigned attention primarily to solve one problem: the
**KV cache**.

### The KV Cache Problem

During autoregressive generation, each new token requires attending to all previous tokens.
To avoid recomputing all key (K) and value (V) projections at every step, we cache them.
This is the **KV cache**.

**Memory cost of KV cache:**
```
KV cache size = 2 × num_layers × num_heads × head_dim × sequence_length × precision_bytes
```

For LLaMA 2 70B with full MHA:
```
= 2 × 80 × 64 × 128 × seq_len × 2 bytes (fp16)
= ~2.6 MB per token
= ~2.6 GB for 1024 tokens
= ~10.5 GB for 4096 tokens (PER REQUEST)
```

When you're serving thousands of concurrent requests, KV cache memory becomes the dominant
constraint — not model weights, not compute. This is why attention variants that reduce
KV cache size are so important.

### Multi-Head Attention (MHA): The Original

Standard multi-head attention from "Attention Is All You Need":

```
Q = X · W_Q    →  split into h heads
K = X · W_K    →  split into h heads  
V = X · W_V    →  split into h heads

For each head i:
    Attention_i = softmax(Q_i · K_i^T / √d_k) · V_i

Output = Concat(Attention_1, ..., Attention_h) · W_O
```

Each head has its own Q, K, and V projections. For a model with 64 heads, you cache 64
separate K and 64 separate V tensors per layer.

### Multi-Query Attention (MQA): Radical Compression

Shazeer (2019) proposed MQA: keep multiple query heads but share a **single** K and V
projection across all heads.

```
Q = X · W_Q    →  split into h heads (64 separate Q projections)
K = X · W_K    →  1 shared K projection
V = X · W_V    →  1 shared V projection

For each head i:
    Attention_i = softmax(Q_i · K^T / √d_k) · V   ← same K,V for all heads
```

**KV cache reduction:** 64x smaller (from 64 KV pairs per layer to 1).

**The catch:** Significant quality degradation on complex reasoning tasks. All heads seeing
the same K and V limits the model's ability to attend to different types of information
simultaneously.

**Used in:** PaLM, Falcon, early StarCoder.

### Grouped Query Attention (GQA): The Sweet Spot

Ainslie et al. (2023) found the middle ground: instead of 1 shared KV pair (MQA) or 64
separate KV pairs (MHA), group query heads together to share KV projections.

```
64 query heads → grouped into 8 groups of 8
Each group of 8 query heads shares 1 K and 1 V projection
Total: 8 KV pairs per layer (instead of 64 for MHA or 1 for MQA)
```

**KV cache reduction:** 8x smaller than MHA (for 8 KV groups with 64 heads).

**Why GQA won:**
1. **Quality nearly matches full MHA.** The model retains enough diversity in KV
   representations to maintain strong reasoning.
2. **Dramatic memory savings.** 8x reduction in KV cache means 8x more concurrent requests
   per GPU, or 8x longer context per request.
3. **Existing models can be "upconverted."** You can take a pre-trained MHA model and
   convert it to GQA by mean-pooling adjacent KV heads, then fine-tune briefly.
4. **Hardware-friendly.** The grouped structure maps well to GPU tensor core operations.

**Real-world adoption:**
- LLaMA 2 70B: 8 KV heads for 64 query heads (8:1 ratio)
- LLaMA 3: GQA across all model sizes
- Mistral 7B: 8 KV heads for 32 query heads (4:1 ratio)
- Gemma: GQA
- Qwen 2: GQA

GQA is now the default for essentially all new production LLMs.

### Sliding Window Attention (Mistral's Approach)

Mistral 7B introduced sliding window attention: each token attends only to the previous W
tokens (window size), not the entire sequence.

```
Standard causal attention:  Token at position i attends to positions [0, 1, ..., i]
Sliding window (W=4096):    Token at position i attends to positions [i-4096, ..., i]
```

**Key insight:** Information propagates through layers. With L layers and window size W,
effective receptive field = L × W. Mistral with 32 layers and W=4096 has an effective
field of 131,072 tokens.

**Engineering benefits:**
- KV cache is bounded: only need to store W tokens per layer, regardless of sequence length
- Memory is O(W) not O(N) — enabling processing of arbitrarily long sequences
- Cache can be implemented as a circular buffer (rolling cache) for constant memory

**The tradeoff:** Direct attention is limited to the window. Information from beyond the
window must "hop" through intermediate layers, which introduces some degradation for
very long-range dependencies.

### Multi-Head Latent Attention (DeepSeek MLA)

DeepSeek-V2 introduced MLA, one of the most innovative attention designs in recent LLMs.
The core idea: compress KV representations into a low-rank latent space before caching.

**How MLA works:**

```
Standard: Cache K and V directly (high-dimensional)

MLA:
1. Project K and V into a shared low-rank "latent" representation:
   c_kv = X · W_dkv        ← compressed joint KV, much smaller dimension
   
2. At attention time, expand back:
   K = c_kv · W_uk          ← reconstruct K from compressed representation
   V = c_kv · W_uv          ← reconstruct V from compressed representation
   
3. Cache only c_kv (the compressed representation)
```

**Why this is brilliant:**
- The compressed representation `c_kv` is dramatically smaller than storing full K and V
  separately for all heads
- DeepSeek-V2 achieves KV cache compression comparable to MQA while maintaining MHA-level
  quality
- The low-rank bottleneck acts as an information bottleneck, forcing the model to learn
  efficient representations

**KV cache comparison for DeepSeek-V2 (236B params):**
```
Full MHA:  would require ~100+ GB KV cache for long contexts
GQA (8x):  ~12.5 GB
MLA:        ~5.6 GB (with 512-dim latent per layer)
```

MLA is still relatively new but represents a promising direction — achieving the memory
efficiency of MQA with the quality of MHA through learned compression.

### FlashAttention: The Implementation Revolution

FlashAttention (Dao et al., 2022) isn't an architectural change to attention — it computes
the exact same mathematical operation. What it changes is *how* attention is computed,
matching the GPU memory hierarchy.

**The GPU memory hierarchy problem:**
```
GPU SRAM (on-chip):   ~20 MB,    ~19 TB/s bandwidth    ← fast but tiny
GPU HBM (off-chip):   ~80 GB,    ~2 TB/s bandwidth     ← large but slow
```

Standard attention materializes the full N×N attention matrix in HBM, then reads it back
for softmax, then reads again for value multiplication. This creates a massive I/O bottleneck.

**FlashAttention's approach:**
1. Tile the Q, K, V matrices into blocks that fit in SRAM
2. Compute attention for each block entirely in SRAM (including softmax via online normalization)
3. Write only the final output to HBM — never materialize the full attention matrix

**Results:**
- 2-4x speedup over standard attention
- Memory usage drops from O(N²) to O(N) — no full attention matrix stored
- Enables training with much longer sequences on the same hardware
- FlashAttention-2 adds further optimizations for work partitioning across GPU warps
- FlashAttention-3 leverages Hopper architecture features (wgmma, TMA)

FlashAttention is now the default attention implementation in every major framework
(PyTorch, JAX, TensorRT) and is essential for practical LLM training and inference.

---

## Normalization & Activation

### LayerNorm: The Baseline

Layer Normalization (Ba et al., 2016) normalizes activations across features:

```python
def layer_norm(x, gamma, beta):
    mean = x.mean(dim=-1, keepdim=True)
    var = x.var(dim=-1, keepdim=True)
    x_norm = (x - mean) / sqrt(var + eps)
    return gamma * x_norm + beta
```

Two operations: (1) center by subtracting mean, (2) scale by dividing by standard deviation.
Then apply learned affine parameters (gamma, beta).

### RMSNorm: Simpler, Faster, Just as Good

Zhang & Sennrich (2019) showed that the mean-centering step in LayerNorm isn't necessary.
RMSNorm normalizes only by the root mean square:

```python
def rms_norm(x, gamma):
    rms = sqrt(mean(x^2) + eps)
    return gamma * (x / rms)
```

**What's removed:**
- No mean computation (saves one reduction operation)
- No mean subtraction (saves one elementwise operation)
- No beta (shift) parameter (fewer learned parameters)

**Why this matters at scale:**
- ~10-15% faster than LayerNorm per normalization call
- In a 70B model with hundreds of norm operations per forward pass, this adds up
- Empirically matches LayerNorm's training dynamics and final quality

**Adoption:** LLaMA, LLaMA 2, LLaMA 3, Mistral, Gemma, Qwen, DeepSeek — essentially
every modern open-source LLM uses RMSNorm.

### DeepNorm: Scaling to Extreme Depths

DeepNorm (Wang et al., 2022) addresses training stability for very deep Transformers
(1000+ layers). It modifies both the residual connection and initialization:

```
Standard:   x + Sublayer(Norm(x))
DeepNorm:   x · α + Sublayer(Norm(x))     ← scale residual by α > 1
```

Combined with specific initialization scaling (Xavier init divided by a factor), DeepNorm
stabilizes training of models with up to 1000 layers without gradient explosion.

**Used in:** Some specialized deep models, but not widely adopted for standard LLMs where
depths of 32-96 layers are typical and RMSNorm suffices.

### Pre-Norm vs Post-Norm

This is one of the most impactful architectural decisions, despite being "just" the order
of operations:

**Post-Norm (Original Transformer):**
```
x → Attention → Add(x) → LayerNorm → FFN → Add → LayerNorm
```

**Pre-Norm (Modern LLMs):**
```
x → LayerNorm → Attention → Add(x) → LayerNorm → FFN → Add(x)
```

**Why pre-norm won decisively:**

1. **Training stability.** Pre-norm ensures that the residual pathway is "clean" — gradients
   flow directly through the residual connection without passing through normalization. This
   prevents gradient explosion in deep models.

2. **No learning rate warmup tricks needed.** Post-norm models require careful warmup schedules
   and lower learning rates to avoid early training instability. Pre-norm is robust from step 1.

3. **Scales to deeper models.** Post-norm becomes increasingly unstable beyond ~12 layers
   without special tricks. Pre-norm trains stably at 80+ layers.

4. **Empirical quality.** At the same depth and width, pre-norm matches or slightly exceeds
   post-norm quality, while being much easier to train.

**The one advantage of post-norm:** Some research suggests post-norm achieves slightly better
final quality in encoder-only models (BERT-style), possibly because the normalization after
the residual creates a stronger regularization effect. But for autoregressive LLMs, pre-norm
is universally preferred.

### SwiGLU: Why It's Everywhere

The feed-forward network (FFN) in each Transformer block was originally:

```
FFN(x) = W₂ · ReLU(W₁ · x + b₁) + b₂
```

Modern LLMs use SwiGLU (Shazeer, 2020), a gated activation:

```
SwiGLU(x) = (W₁ · x) ⊙ Swish(W₂ · x)

where Swish(z) = z · σ(z)       ← σ is sigmoid
```

**Breaking this down:**
- The input x is projected through TWO separate weight matrices (W₁ and W₂)
- One projection (W₂ · x) is passed through the Swish activation
- The other projection (W₁ · x) acts as a "gate" via element-wise multiplication
- The gate controls what information flows through

**Why SwiGLU dominates:**

1. **Gating is powerful.** The element-wise multiplication allows the network to selectively
   suppress or amplify different features. This is more expressive than simply applying an
   activation function.

2. **Swish is smooth.** Unlike ReLU (which has a hard zero for negative inputs), Swish is
   smooth and non-monotonic: slightly negative inputs get slightly negative outputs. This
   improves gradient flow.

3. **Empirical superiority.** Shazeer (2020) tested GELU, ReLU, Swish, SwiGLU, GeGLU, and
   ReGLU across multiple model sizes. SwiGLU consistently achieved the best perplexity —
   typically 0.5-1.0 points better than GELU.

4. **The FFN dimension adjustment.** Because SwiGLU uses two projections (W₁ and W₂) plus
   an output projection (W₃), it has 50% more parameters than a standard FFN with two matrices.
   To maintain the same parameter count, models reduce the FFN hidden dimension from 4× model
   dimension to (8/3)× model dimension: `d_ff = (8/3) × d_model ≈ 2.67 × d_model`.

**Adoption:** LLaMA (all versions), Mistral, Gemma, PaLM, Qwen, Falcon — SwiGLU is the
default FFN activation for modern LLMs.

### GeGLU and Other Gated Variants

SwiGLU isn't the only gated activation:

```
GeGLU(x)  = (W₁ · x) ⊙ GELU(W₂ · x)    ← uses GELU instead of Swish
ReGLU(x)  = (W₁ · x) ⊙ ReLU(W₂ · x)    ← uses ReLU instead of Swish
```

GeGLU performs nearly as well as SwiGLU in most benchmarks. The key insight is that the
**gating mechanism** (the ⊙ multiplication) matters more than the specific activation
function used on the gate.

---

## Architecture Decisions

### Decoder-Only vs Encoder-Decoder

The original Transformer was encoder-decoder (for machine translation). BERT used
encoder-only. GPT used decoder-only. For LLMs, decoder-only won. Here's why:

**Decoder-only architecture:**
```
Input tokens → [Causal Self-Attention → FFN] × L → Output logits
```

Each token can only attend to previous tokens (causal mask). Prediction is always
"given everything before, predict the next token."

**Why decoder-only won for LLMs:**

1. **Unified task formulation.** Every task becomes text generation: Q&A, translation,
   summarization, coding — all are "continue this text." No need for task-specific heads
   or encoder-decoder cross-attention.

2. **In-context learning.** Decoder-only models naturally support few-shot prompting.
   You prepend examples and the model "continues" with the answer. This doesn't map
   cleanly to encoder-decoder.

3. **Training simplicity.** One objective (next token prediction), one architecture,
   one data pipeline. Every token in every training sequence produces a training signal.
   Encoder-decoder wastes compute on the encoder for tasks that don't need bidirectional
   context.

4. **Scaling efficiency.** All parameters participate in every forward pass. In
   encoder-decoder, the encoder parameters are "wasted" during generation (you only
   run the encoder once but the decoder many times).

5. **KV cache simplicity.** Only one attention mechanism to cache (self-attention),
   versus encoder-decoder which requires caching both self-attention and cross-attention.

**Where encoder-decoder still has advantages:**
- Tasks with distinct input/output structures (translation, ASR)
- When bidirectional context over the input is critical
- T5 and FLAN-T5 showed competitive performance with encoder-decoder at moderate scale

But the trend is clear: GPT-4, LLaMA, Mistral, Claude, Gemini (text) — all decoder-only.

### Parallel Attention + FFN (GPT-J Style)

Standard Transformer blocks are sequential: attention first, then FFN:

```
Standard:   x → Attention(Norm(x)) + x → FFN(Norm(·)) + · → output
```

GPT-J (EleutherAI, 2021) introduced parallel blocks:

```
Parallel:   x → [Attention(Norm(x)) + FFN(Norm(x))] + x → output
```

Both attention and FFN receive the (differently normalized) input simultaneously, and their
outputs are summed with the residual.

**Benefits:**
- **Faster.** Attention and FFN can execute in parallel on GPU, reducing wall-clock time
  per layer by up to 15%.
- **Better gradient flow.** Both pathways provide direct gradients to the input.
- **Empirically equivalent quality.** PaLM showed this at 540B scale — parallel blocks
  match sequential blocks in quality.

**Adoption:** PaLM (Google), GPT-J, GPT-NeoX, some Mistral variants.
Not universal (LLaMA uses sequential), but gaining traction.

### Tied vs Untied Embeddings

**Tied embeddings:** The input embedding matrix and the output projection matrix (before
softmax) share the same weights.

```
Tied:     embed(token) = W[token]
          logits = hidden · W^T       ← same W

Untied:   embed(token) = W_in[token]
          logits = hidden · W_out^T   ← different W_in, W_out
```

**Tying saves memory:** For a 128K vocabulary with d=4096, the embedding matrix is
~1GB (fp16). Tying means you only store one copy.

**Modern trend:** Most large models (LLaMA 3, Mistral) **do not tie** embeddings.
At billion-parameter scale, the 1GB savings is marginal compared to total model size,
and untied embeddings allow the input and output to learn different representations.

**Exception:** Smaller models (< 1B params) often tie embeddings because the savings
are proportionally more significant.

### Model Depth vs Width Trade-offs

For a fixed parameter budget, how do you allocate between layers (depth) and hidden
dimension (width)?

**Empirical findings:**

| Model Size | Typical Depth | Typical Width | Attention Heads |
|------------|--------------|---------------|-----------------|
| 1B         | 24 layers    | 2048          | 16              |
| 7B         | 32 layers    | 4096          | 32              |
| 13B        | 40 layers    | 5120          | 40              |
| 70B        | 80 layers    | 8192          | 64              |
| 405B       | 126 layers   | 16384         | 128             |

**Key insights:**
- **Depth wins for reasoning.** Deeper models (more layers) develop stronger compositional
  reasoning and long-range dependency handling. Each layer adds another "step" of computation.
- **Width wins for memorization.** Wider models (larger hidden dim) can store more factual
  knowledge in their parameters.
- **Too deep = instability.** Beyond ~100 layers, training becomes difficult without
  special techniques (DeepNorm, careful initialization, very precise learning rate tuning).
- **Too wide = diminishing returns.** Quadrupling width doesn't quadruple quality; the
  gains are sub-linear.

**The modern heuristic:** Scale depth and width together, keeping the ratio roughly
constant (d_model ≈ 128 × num_heads, num_layers ≈ d_model/64 for large models).

---

## Training at Scale

### Learning Rate Scheduling

The learning rate schedule is one of the most critical training hyperparameters. Two
schedules dominate modern LLM training:

**Cosine Schedule (with warmup):**
```
Phase 1 (warmup):  lr linearly increases from 0 to lr_max over W steps
Phase 2 (decay):   lr = lr_min + 0.5 * (lr_max - lr_min) * (1 + cos(π * t / T))
```

The learning rate smoothly decays from `lr_max` to `lr_min` following a cosine curve.
This is the schedule used by LLaMA, GPT-3, PaLM, and most major LLMs.

**Why cosine works:** The smooth decay prevents sudden changes in optimization dynamics.
The learning rate is high when the loss surface is rough (early training) and low when
fine-tuning representations (late training).

**WSD Schedule (Warmup → Stable → Decay):**
```
Phase 1 (warmup):  lr linearly increases to lr_max
Phase 2 (stable):  lr held constant at lr_max  
Phase 3 (decay):   lr decays (cosine or linear) to lr_min
```

WSD adds a stable phase where the learning rate doesn't change. This can be useful for:
- Continuing training (you can extend the stable phase)
- Models that need more time at peak learning rate
- MiniCPM and some recent Chinese LLMs use WSD

**Typical values:**
```
GPT-3 175B:    lr_max = 6e-5,  warmup = 375 steps
LLaMA 2 70B:   lr_max = 1.5e-4, warmup = 2000 steps, cosine decay to 1.5e-5
Mistral 7B:    lr_max = 5e-5,  warmup = 2000 steps, cosine decay
```

### Gradient Clipping and Training Stability

Large model training is plagued by loss spikes — sudden jumps in training loss that can
destabilize or crash training runs that took weeks and millions of dollars of compute.

**Gradient clipping** is the primary defense:

```python
# Global norm clipping (most common)
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

**How it works:** If the total gradient norm exceeds `max_norm`, all gradients are scaled
down proportionally. This prevents any single batch from causing catastrophically large
parameter updates.

**Standard values:** Most LLMs use `max_norm = 1.0`. Some use 0.5 for extra stability.

**Other stability techniques:**
- **Loss spike detection:** Monitor loss and roll back to a previous checkpoint if a
  spike exceeds a threshold
- **Gradient accumulation:** Average gradients over multiple micro-batches to reduce
  variance before each parameter update
- **BF16 precision:** Brain Float 16 has the same exponent range as FP32 (unlike FP16),
  preventing overflow during training. This is why BF16 replaced FP16 for LLM training.
- **Z-loss regularization:** PaLM added a small penalty on the log-partition function
  of the softmax to prevent logits from growing too large

### Data Mixing and Curriculum Learning

Modern LLMs train on diverse data: web text, books, code, scientific papers, conversations.
How you mix these sources dramatically affects model quality.

**Data mixing ratios (approximate, from published models):**

| Source           | LLaMA 1 | LLaMA 2 | Typical Range |
|------------------|---------|---------|---------------|
| Web (CommonCrawl)| 67%     | ~90%    | 60-90%        |
| Code (GitHub)    | 4.5%    | ~5%     | 3-10%         |
| Wikipedia        | 4.5%    | ~2%     | 2-5%          |
| Books            | 4.5%    | ~2%     | 2-5%          |
| ArXiv/Papers     | 2.5%    | ~1%     | 1-3%          |
| StackExchange    | 2.0%    | ~1%     | 1-3%          |

**Curriculum learning** orders data presentation during training:
- **Simple→Complex:** Start with cleaner, simpler data (Wikipedia, books) and gradually
  introduce noisier web data
- **Domain scheduling:** Increase code/math ratio in later training stages to "specialize"
- **Quality filtering ramps:** Start with loose quality filters, tighten as training progresses

**Data repetition matters:** Muennighoff et al. (2023) showed that repeating data beyond
~4 epochs causes degradation. This puts a floor on how much unique data you need:
```
7B model (Chinchilla optimal):   ~140B tokens needed
70B model (Chinchilla optimal):  ~1.4T tokens needed
405B model:                      ~15T tokens needed
```

### Scaling Laws: Chinchilla and Beyond

Scaling laws predict how model performance improves as you increase compute, parameters,
and data.

**Kaplan et al. (2020) — Original Scaling Laws:**
- Loss scales as a power law with model size: L(N) ∝ N^(-0.076)
- Loss scales as a power law with data: L(D) ∝ D^(-0.095)
- Conclusion: Prioritize model size over data (train big models on less data)
- **This led to GPT-3:** 175B parameters trained on "only" 300B tokens

**Hoffmann et al. (2022) — Chinchilla Scaling Laws:**
- Revised the optimal allocation: parameters and tokens should scale equally
- **The Chinchilla ratio:** ~20 tokens per parameter
- A 70B model should train on ~1.4T tokens (not 300B like GPT-3 would suggest)
- **Chinchilla (70B, 1.4T tokens) outperformed Gopher (280B, 300B tokens)** despite
  being 4x smaller

**Beyond Chinchilla (2023-2024):**

The field moved beyond Chinchilla-optimal in two ways:

1. **Inference-optimal scaling (Sardana & Frankle, 2023):** Chinchilla optimizes for
   training compute. But if your model will be used for billions of inference queries,
   it's worth training a **smaller model on more data** (reducing inference cost).
   LLaMA 3 8B trained on 15T tokens — 1875 tokens per parameter, nearly 100x the
   Chinchilla ratio.

2. **Data-constrained scaling:** We're running out of high-quality text data. When you
   can't increase data, you invest more compute in better data curation, augmentation,
   and training techniques rather than pure scaling.

**Key scaling law results:**
```
Model         Parameters  Tokens    Tokens/Param  Chinchilla Ratio
GPT-3         175B        300B      1.7           0.09x
Chinchilla    70B         1.4T      20            1.0x (optimal)
LLaMA 2 70B   70B         2.0T      29            1.4x
Mistral 7B    7B          ~8T       1143          57x
LLaMA 3 8B    8B          15T       1875          94x
LLaMA 3 405B  405B        15T       37            1.9x
```

The trend is clear: modern models are trained **far beyond** Chinchilla-optimal, especially
at smaller sizes, because inference cost matters more than training cost.

### MuP (Maximal Update Parameterization)

The biggest practical problem in LLM training: hyperparameter tuning. A single training
run of a 70B model costs millions of dollars. You can't afford to sweep learning rates.

**MuP (Yang et al., 2022) solves this:**

The key insight: if you parameterize your model correctly (specifically, how weights are
initialized and how learning rates scale with width), then **hyperparameters transfer from
small models to large models**.

**How it works:**
1. Train a small "proxy" model (e.g., 10M parameters) with a full hyperparameter sweep
2. Find optimal learning rate, weight decay, batch size, etc.
3. Scale up to 1B, 10B, 70B parameters using MuP's scaling rules
4. **Use the exact same hyperparameters** — they transfer

**MuP's scaling rules (simplified):**
- Input embedding: scale by 1
- Hidden layer weights: scale initialization by 1/√width
- Output layer weights: scale learning rate by 1/width
- Attention logits: scale by 1/√d_head

**Impact:** MuP saves potentially millions of dollars per training run by eliminating
the need for expensive hyperparameter searches at scale. Cerebras and several other
organizations have adopted it for production training.

---

## Inference Optimization

Training a model is expensive but it happens once. Inference happens billions of times.
The engineering of efficient inference is what makes LLMs practical products.

### KV Cache and Memory Management

As discussed in the attention section, the KV cache is the dominant memory cost during
inference. Here's the full picture:

**Prefill phase:** Process the entire input prompt at once. All Q, K, V are computed in
parallel. This is compute-bound (GPU cores are busy).

**Decode phase:** Generate tokens one at a time. Each new token computes Q, but K and V
come from the cache. This is memory-bound (limited by memory bandwidth, not compute).

**Memory breakdown for serving LLaMA 2 70B:**
```
Model weights:          ~140 GB (fp16)
KV cache per request:   ~2.6 MB per token
1000 concurrent requests × 4K context: ~10.4 TB KV cache needed

This doesn't fit on any single server.
```

**Memory management strategies:**
- **KV cache quantization:** Store KV cache in INT8 (4x reduction) or even INT4 (8x)
- **Prefix caching:** System prompts shared across requests can share KV cache entries
- **KV cache eviction:** Drop KV entries for tokens the model is unlikely to attend to
- **KV cache offloading:** Move KV cache to CPU RAM or NVMe when GPU memory is full

### vLLM's PagedAttention

The single most important inference optimization of 2023. PagedAttention (Kwon et al., 2023)
applies operating system virtual memory concepts to KV cache management.

**The problem with naive KV caching:**
- Each request pre-allocates KV cache for maximum possible sequence length
- If max length is 4096 but actual generation is 200 tokens, 95% of allocated memory is wasted
- This "internal fragmentation" means you can serve far fewer concurrent requests

**PagedAttention's solution:**

Borrow the concept of virtual memory paging from operating systems:

1. **Divide KV cache into fixed-size "pages"** (blocks of, say, 16 tokens)
2. **Allocate pages on demand** — only when tokens are actually generated
3. **Pages can be non-contiguous** — like virtual memory, physical memory doesn't need
   to be sequential
4. **Free pages instantly** when a request completes

**Results:**
- Near-zero internal fragmentation
- 2-4x more concurrent requests on the same hardware
- Efficient memory sharing for beam search (beams can share common prefix pages)
- Enables prefix caching (shared system prompt pages)

**vLLM's overall architecture:**
```
Requests → Scheduler → [PagedAttention Engine] → Token Sampler → Responses
              ↓
    Page Table Manager (allocate/free KV cache pages)
```

vLLM processes up to 24x more throughput than HuggingFace Transformers for serving, making
it the standard for production LLM serving.

### Continuous Batching

Traditional batching waits for a fixed number of requests and processes them together.
This is wasteful because:
- Short requests finish before long ones → GPU sits idle waiting for the batch to complete
- Late-arriving requests wait until the current batch finishes

**Continuous batching (iteration-level batching):**
- After each decode step, check for completed and new requests
- Remove completed requests immediately (free their KV cache)
- Insert new requests into the batch immediately
- The batch composition changes at every step

```
Step 1: [req1, req2, req3, req4]    ← req1 finishes
Step 2: [req5, req2, req3, req4]    ← req5 joins, req3 finishes  
Step 3: [req5, req2, req6, req4]    ← req6 joins
```

**Impact:** 10-20x improvement in throughput compared to static batching, because GPUs
never idle waiting for the slowest request in a batch.

Implemented in: vLLM, TensorRT-LLM, TGI (Text Generation Inference).

### Tensor Parallelism vs Pipeline Parallelism

When a model doesn't fit on one GPU, you need parallelism. Two main strategies:

**Tensor Parallelism (TP):**
- Split individual layers across GPUs
- Each GPU holds a "slice" of every weight matrix
- GPUs must communicate within each layer (all-reduce operations)

```
Layer with d=8192 on 4 GPUs:
GPU 0: columns [0:2048]
GPU 1: columns [2048:4096]
GPU 2: columns [4096:6144]
GPU 3: columns [6144:8192]
```

**Best for:** Small number of GPUs with fast interconnect (NVLink).
**Drawback:** Communication-heavy; requires high-bandwidth GPU-to-GPU links.

**Pipeline Parallelism (PP):**
- Split layers across GPUs (each GPU holds a range of complete layers)
- GPUs form a pipeline — output of one GPU feeds into the next

```
80-layer model on 4 GPUs:
GPU 0: layers 0-19
GPU 1: layers 20-39
GPU 2: layers 40-59
GPU 3: layers 60-79
```

**Best for:** Many GPUs, especially across nodes with slower interconnect.
**Drawback:** Pipeline "bubbles" — GPUs sit idle while waiting for upstream/downstream data.
Mitigated by micro-batching.

**In practice:** Most production systems use **both**:
```
8 GPUs per node:  Tensor Parallelism (TP=8, fast NVLink)
Multiple nodes:   Pipeline Parallelism (PP across nodes, slower network)
```

For LLaMA 2 70B serving:
```
TP=8 on 8× A100 80GB: Model fits, full tensor parallelism
PP=2, TP=4 on 8× A100 40GB: Split layers across 2 pipeline stages, each using 4 GPUs for TP
```

### Speculative Decoding

Autoregressive generation is inherently sequential: each token depends on the previous one.
This means the GPU is massively underutilized during decode — generating one token uses
<1% of available compute.

**Speculative decoding** exploits this by using a small "draft" model to speculate ahead:

```
Step 1: Draft model quickly generates K candidate tokens: [t1, t2, t3, t4, t5]
Step 2: Target model verifies all K tokens in one parallel forward pass
Step 3: Accept all tokens that match (e.g., [t1, t2, t3] accepted, t4 rejected)
Step 4: Resume from t4 position with the target model's distribution
```

**Why it works:**
- The draft model is 10-100x smaller and faster
- The target model's verification is parallel (not sequential) — it processes all K
  candidate tokens at once
- If the draft model is good (accepts most candidates), you effectively generate
  K tokens in the time of 1 target model forward pass
- **Mathematically lossless:** The verification step guarantees the output distribution
  is identical to the target model's distribution

**Typical speedup:** 2-3x for well-matched draft/target pairs.

**Variants:**
- **Self-speculative decoding:** Use early exit from the target model as the "draft"
- **Medusa:** Add extra heads to the target model that predict multiple future tokens
- **Eagle:** Use a more sophisticated draft architecture trained to match the target

**Used in:** Production at Google (PaLM serving), Apple (on-device LLMs), Meta (Llama
serving), and most inference engines.

### Quantization for Inference

Modern inference heavily uses quantization to reduce model size and increase throughput:

```
FP32:   4 bytes per parameter → 280 GB for 70B model
FP16:   2 bytes → 140 GB
INT8:   1 byte  → 70 GB
INT4:   0.5 byte → 35 GB  ← fits on single 40GB GPU!
```

**Key quantization methods:**
- **GPTQ:** Post-training quantization using second-order information (Hessian). Fast,
  works well for INT4/INT3.
- **AWQ (Activation-Aware):** Preserves "salient" weights (those with large activations)
  at higher precision.
- **GGUF/llama.cpp:** Mixed-precision quantization optimized for CPU inference. Various
  quant levels from Q2 to Q8.
- **SmoothQuant:** Migrates quantization difficulty from activations to weights by
  mathematically smoothing activation outliers.

**Quality impact:**
```
FP16:    100% baseline quality
INT8:    ~99.5% quality (negligible degradation)
INT4:    ~97-99% quality (slight degradation, acceptable for most uses)
INT3:    ~93-97% quality (noticeable degradation)
INT2:    ~85-93% quality (significant degradation)
```

---

## Putting It All Together: The Modern LLM Blueprint

Here's what a state-of-the-art LLM looks like in 2024, with each component traced to
the section above:

```
┌─────────────────────────────────────────────────────────┐
│                    INPUT TEXT                            │
├─────────────────────────────────────────────────────────┤
│  Tokenizer: Byte-level BPE (128K vocab)                 │
│  → Token IDs → Embedding lookup (untied, d=8192)        │
│  → NO explicit positional embedding added                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─── Transformer Block (×80 layers) ─────────────┐    │
│  │                                                 │    │
│  │  Input x                                        │    │
│  │  ├── RMSNorm(x)                                 │    │
│  │  ├── GQA Self-Attention                         │    │
│  │  │   ├── Q: 64 heads (d_head=128)               │    │
│  │  │   ├── KV: 8 groups (d_head=128)              │    │
│  │  │   ├── Apply RoPE to Q and K                  │    │
│  │  │   ├── FlashAttention (causal mask)           │    │
│  │  │   └── Output projection                      │    │
│  │  ├── + x (residual connection)                  │    │
│  │  │                                              │    │
│  │  ├── RMSNorm(·)                                 │    │
│  │  ├── SwiGLU FFN                                 │    │
│  │  │   ├── Gate: W_gate · x                       │    │
│  │  │   ├── Up:   W_up · x                        │    │
│  │  │   ├── Swish(Gate) ⊙ Up                      │    │
│  │  │   └── W_down · (·)                          │    │
│  │  └── + residual                                 │    │
│  │                                                 │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  Final RMSNorm → Output projection (untied) → logits   │
├─────────────────────────────────────────────────────────┤
│  Softmax → Token probabilities → Sample/Greedy decode   │
├─────────────────────────────────────────────────────────┤
│  Detokenize → OUTPUT TEXT                               │
└─────────────────────────────────────────────────────────┘
```

**Training configuration:**
```
Optimizer:       AdamW (β1=0.9, β2=0.95, ε=1e-8, wd=0.1)
LR Schedule:     Cosine decay (warmup 2000 steps, peak 1.5e-4, min 1.5e-5)
Batch size:      4M tokens (via gradient accumulation)
Precision:       BF16 mixed precision
Gradient clip:   max_norm=1.0
Parallelism:     TP=8 within node, PP across nodes
Data:            15T tokens (web, code, books, papers)
```

**Inference configuration:**
```
Engine:          vLLM with PagedAttention
Attention:       FlashAttention-2
KV cache:        Quantized to INT8
Batching:        Continuous batching
Parallelism:     TP=8 for 70B+ models
Decoding:        Speculative decoding (draft model = 1B)
Quantization:    INT4 (AWQ) for edge deployment
```

---

## Key Papers & Sources

### Foundational Architecture
- **"Attention Is All You Need"** (Vaswani et al., 2017) — The original Transformer
  https://arxiv.org/abs/1706.03762
- **"Language Models are Unsupervised Multitask Learners"** (GPT-2, Radford et al., 2019)
  https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **"Language Models are Few-Shot Learners"** (GPT-3, Brown et al., 2020)
  https://arxiv.org/abs/2005.14165

### Tokenization
- **"Neural Machine Translation of Rare Words with Subword Units"** (BPE, Sennrich et al., 2015)
  https://arxiv.org/abs/1508.07909
- **"SentencePiece: A simple and language independent subword tokenizer"** (Kudo & Richardson, 2018)
  https://arxiv.org/abs/1808.06226
- **"ByT5: Towards a Token-Free Future"** (Xue et al., 2021)
  https://arxiv.org/abs/2105.13626
- **"MegaByte: Predicting Million-Byte Sequences with Multiscale Transformers"** (Yu et al., 2023)
  https://arxiv.org/abs/2305.07185

### Positional Encoding
- **"RoFormer: Enhanced Transformer with Rotary Position Embedding"** (RoPE, Su et al., 2021)
  https://arxiv.org/abs/2104.09864
- **"Train Short, Test Long: Attention with Linear Biases"** (ALiBi, Press et al., 2021)
  https://arxiv.org/abs/2108.12409
- **"YaRN: Efficient Context Window Extension"** (Peng et al., 2023)
  https://arxiv.org/abs/2309.00071
- **"Extending Context Window of Large Language Models via Positional Interpolation"** (Chen et al., 2023)
  https://arxiv.org/abs/2306.15595

### Attention Variants
- **"Fast Transformer Decoding: One Write-Head is All You Need"** (MQA, Shazeer, 2019)
  https://arxiv.org/abs/1911.02150
- **"GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"** (Ainslie et al., 2023)
  https://arxiv.org/abs/2305.13245
- **"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"** (Dao et al., 2022)
  https://arxiv.org/abs/2205.14135
- **"FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"** (Dao, 2023)
  https://arxiv.org/abs/2307.08691
- **"DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"** (MLA)
  https://arxiv.org/abs/2405.04434

### Normalization & Activation
- **"Root Mean Square Layer Normalization"** (RMSNorm, Zhang & Sennrich, 2019)
  https://arxiv.org/abs/1910.07467
- **"On Layer Normalization in the Transformer Architecture"** (Pre-norm analysis, Xiong et al., 2020)
  https://arxiv.org/abs/2002.04745
- **"GLU Variants Improve Transformer"** (SwiGLU, GeGLU, Shazeer, 2020)
  https://arxiv.org/abs/2002.05202
- **"DeepNet: Scaling Transformers to 1,000 Layers"** (DeepNorm, Wang et al., 2022)
  https://arxiv.org/abs/2203.00555

### Scaling Laws & Training
- **"Scaling Laws for Neural Language Models"** (Kaplan et al., 2020)
  https://arxiv.org/abs/2001.08361
- **"Training Compute-Optimal Large Language Models"** (Chinchilla, Hoffmann et al., 2022)
  https://arxiv.org/abs/2203.15556
- **"Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer"** (MuP, Yang et al., 2022)
  https://arxiv.org/abs/2203.03466
- **"Scaling Data-Constrained Language Models"** (Muennighoff et al., 2023)
  https://arxiv.org/abs/2305.16264

### Model Reports
- **"LLaMA: Open and Efficient Foundation Language Models"** (Touvron et al., 2023)
  https://arxiv.org/abs/2302.13971
- **"Llama 2: Open Foundation and Fine-Tuned Chat Models"** (Touvron et al., 2023)
  https://arxiv.org/abs/2307.09288
- **"The Llama 3 Herd of Models"** (Meta, 2024)
  https://arxiv.org/abs/2407.21783
- **"Mistral 7B"** (Jiang et al., 2023)
  https://arxiv.org/abs/2310.06825
- **"PaLM: Scaling Language Modeling with Pathways"** (Chowdhery et al., 2022)
  https://arxiv.org/abs/2204.02311

### Inference Optimization
- **"Efficient Memory Management for Large Language Model Serving with PagedAttention"** (Kwon et al., 2023)
  https://arxiv.org/abs/2309.06180
- **"Fast Inference from Transformers via Speculative Decoding"** (Leviathan et al., 2022)
  https://arxiv.org/abs/2211.17192
- **"GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"** (Frantar et al., 2022)
  https://arxiv.org/abs/2210.17323
- **"AWQ: Activation-aware Weight Quantization"** (Lin et al., 2023)
  https://arxiv.org/abs/2306.00978
- **"SmoothQuant: Accurate and Efficient Post-Training Quantization for LLMs"** (Xiao et al., 2022)
  https://arxiv.org/abs/2211.10438

### Blogs and Explainers
- **Lilian Weng's "Large Transformer Model Lessons"**
  https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/
- **Jay Alammar's "The Illustrated Transformer"**
  https://jalammar.github.io/illustrated-transformer/
- **Hugging Face Blog: "Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA"**
  https://huggingface.co/blog/4bit-transformers-bitsandbytes
- **vLLM Blog: "vLLM: Easy, Fast, and Cheap LLM Serving"**
  https://blog.vllm.ai/2023/06/20/vllm.html

---

## Concepts for Knowledge Tree

1. **Byte-Pair Encoding (BPE)** — Subword tokenization algorithm that iteratively merges frequent character pairs
2. **SentencePiece** — Language-agnostic tokenizer operating on raw text including whitespace
3. **Byte-level BPE** — BPE operating on raw bytes (0-255) rather than Unicode characters
4. **tiktoken** — OpenAI's production tokenizer library with Rust backend
5. **Tokenizer-free models** — Models (ByT5, MegaByte) operating directly on raw bytes
6. **Vocabulary size trade-off** — Tension between sequence length, embedding size, and coverage
7. **Rotary Position Embedding (RoPE)** — Position encoding via rotation of Q/K vectors in 2D subspaces
8. **ALiBi** — Position encoding via linear attention score biases proportional to token distance
9. **Context length extension** — Techniques (YaRN, NTK, interpolation) to extend RoPE beyond training length
10. **Multi-Head Attention (MHA)** — Original attention with separate Q/K/V per head
11. **Multi-Query Attention (MQA)** — Shared single K/V across all query heads
12. **Grouped Query Attention (GQA)** — Groups of query heads sharing K/V projections
13. **KV cache** — Cached key/value tensors from previous tokens during autoregressive generation
14. **Sliding Window Attention** — Each token attends only to a fixed window of recent tokens
15. **Multi-Head Latent Attention (MLA)** — Low-rank compression of KV representations (DeepSeek-V2)
16. **FlashAttention** — IO-aware attention using tiled computation to minimize HBM access
17. **RMSNorm** — Simplified normalization using only root mean square (no mean subtraction)
18. **Pre-norm vs Post-norm** — Placement of normalization relative to attention/FFN sublayers
19. **DeepNorm** — Scaled residual connections for training very deep Transformers
20. **SwiGLU activation** — Gated activation combining Swish and element-wise multiplication
21. **Gated Linear Units (GLU)** — Family of activations using element-wise gating mechanisms
22. **Decoder-only architecture** — Single autoregressive decoder stack (vs encoder-decoder)
23. **Parallel attention + FFN** — Computing attention and FFN simultaneously (GPT-J/PaLM style)
24. **Tied vs untied embeddings** — Sharing or separating input embedding and output projection weights
25. **Depth vs width trade-off** — Allocating parameters between layers and hidden dimension
26. **Cosine learning rate schedule** — Smooth learning rate decay following cosine function
27. **WSD schedule** — Warmup → Stable → Decay learning rate schedule
28. **Gradient clipping** — Bounding gradient norms to prevent training instability
29. **Chinchilla scaling laws** — Optimal compute allocation: parameters and tokens scale equally
30. **Beyond-Chinchilla training** — Training smaller models on far more data for inference efficiency
31. **MuP (Maximal Update Parameterization)** — Hyperparameter transfer from small to large models
32. **Data mixing ratios** — Proportional sampling of different data sources during training
33. **Curriculum learning** — Ordering training data from simple to complex
34. **PagedAttention** — OS-style virtual memory paging for KV cache management
35. **Continuous batching** — Dynamic insertion/removal of requests at every decode step
36. **Tensor parallelism** — Splitting individual layers across GPUs
37. **Pipeline parallelism** — Splitting model layers across GPUs in pipeline fashion
38. **Speculative decoding** — Using a draft model to propose tokens verified by the target model
39. **Post-training quantization** — Reducing model precision (INT8/INT4) after training
40. **BF16 training** — Using Brain Float 16 precision for training stability (same exponent as FP32)
41. **Prefill vs decode phases** — Compute-bound prompt processing vs memory-bound token generation
42. **GPU memory hierarchy** — SRAM (fast, small) vs HBM (slow, large) and their impact on algorithms
