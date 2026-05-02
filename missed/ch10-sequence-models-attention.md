# Missing Topics: Ch10 Sequence Models Attention

Now I have comprehensive knowledge of what's covered and what's missing. Let me write the findings file.

Based on my thorough analysis, here's what Chapter 10 currently covers and what's missing:

**COVERED (well):**
- RNN, LSTM, GRU fundamentals ✅
- Seq2Seq, Bahdanau/Luong attention ✅
- Self-attention, QKV, multi-head attention, scaled dot-product ✅
- Sinusoidal, learned, RoPE positional encodings ✅
- Pre-Norm vs Post-Norm ✅
- SwiGLU/GELU in FFN ✅
- BERT, GPT, scaling, Chinchilla ✅
- RoBERTa, ALBERT, DeBERTa family tree ✅
- SSMs, S4, Mamba, Mamba-2 ✅
- FlashAttention (1&2 mentioned), KV cache, MQA, GQA, PagedAttention ✅
- Sparse attention (Longformer, BigBird), Linear attention (Performer, Linformer) ✅
- Reformer, Transformer-XL, XLNet ✅
- MoE (basic coverage in Nice to Know) ✅
- Neural Turing Machines, DNC (basic coverage) ✅
- RetNet, RWKV ✅
- Speculative decoding ✅
- RL: MDP, value functions, Q-learning, DQN, Policy gradients, REINFORCE, Actor-Critic, PPO, RLHF, DPO (brief), Model-based RL (brief) ✅
- Interpretability: probing, BERTology, mechanistic interpretability ✅

**MISSING/UNDERSERVED:**

Here is my compiled analysis:

---

# Ch 10 — Sequence Models & Attention: Missing Topics

## Summary

Chapter 10 is impressively comprehensive on core topics (RNN→LSTM→Seq2Seq→Transformer→BERT/GPT→SSM pipeline, FlashAttention, KV cache, MQA/GQA, and RL fundamentals). However, several important areas are either entirely absent or only mentioned in passing. The biggest gaps are: (1) **ALiBi positional encoding** — the main competitor to RoPE, completely absent; (2) **Sliding Window Attention** — used by Mistral/Gemma, not discussed; (3) **Temporal Convolutional Networks / WaveNet** — an important RNN alternative, absent; (4) **RMSNorm** — used by nearly all modern LLMs, absent; (5) **Retrieval-Augmented Models** (RETRO, kNN-LM) — absent; (6) **Multi-modal Transformers / Vision Transformers** — absent from this chapter; (7) **GRPO** and deeper DPO/alignment coverage; (8) **Offline RL**; (9) **Encoder-Decoder models** like T5/BART deserve more than a single sentence.

---

## 1. Positional Encoding Depth — ALiBi Missing

### What's Covered
- Sinusoidal PE (good depth) — `self-attention-the-transformer.html:522-547`
- Learned PE (brief) — `self-attention-the-transformer.html:549-553`
- RoPE (good depth) — `self-attention-the-transformer.html:555-573`
- Relative PE mentioned in Transformer-XL context — `nice-to-know.html:307-311`

### What's Missing

**ALiBi (Attention with Linear Biases)** — Entirely absent. ALiBi (Press et al., 2022) is a major positional encoding method used by BLOOM, MPT, and other production models. Unlike RoPE (which multiplies rotations into Q/K), ALiBi adds a simple linear bias to attention scores proportional to the distance between tokens: `softmax(q_i · K^T + α_i · [0, -1, -2, ..., -(i-1)])`. The slope α is fixed per head as a geometric sequence. Key advantages: (a) no learned parameters, (b) excellent length extrapolation — models trained on 1024 tokens can generalize to 2048+, (c) simpler implementation than RoPE. ALiBi is a **very common interview question** because it illustrates the tradeoff between learned/sinusoidal/rotary/bias-based position methods.

> **Interview Q**: "Compare RoPE, ALiBi, and sinusoidal PE. Which extrapolates to longer sequences better?" — This question is unanswerable from the current chapter alone.

**Relative Position Bias (T5-style)** — T5 uses a learned relative position bias added to attention logits, with buckets for different distance ranges. This is different from both ALiBi (fixed linear bias) and Transformer-XL relative PE. Currently only a passing mention in the Transformer-XL context.

**Context Length Extrapolation** — The chapter doesn't discuss the general problem of training on short contexts and inferring on long ones. Methods like YaRN (Yet another RoPE extension), NTK-aware scaling, and Position Interpolation for extending RoPE context windows are highly relevant for practitioners.

### Suggested Addition
A comparison table/subsection in the Positional Encoding section:
| Method | Where Applied | Learned? | Extrapolation | Used By |
|--------|-------------|----------|---------------|---------|
| Sinusoidal | Added to input | No | Poor | Original Transformer |
| Learned | Added to input | Yes | None | BERT, GPT-1/2 |
| Relative (T5) | Added to attn logits | Yes (bucketed) | Moderate | T5, Flan-T5 |
| RoPE | Rotation on Q/K | No | Good (with scaling) | LLaMA, Mistral, Qwen |
| ALiBi | Linear bias on attn logits | No | Excellent | BLOOM, MPT |

---

## 2. Sliding Window Attention (SWA) — Missing

### What's Missing
Sliding Window Attention is used by **Mistral 7B**, **Gemma**, and many production models. Each token attends only to the W nearest tokens (e.g., W=4096). With L layers and window W, information can propagate across L×W tokens through the residual stream. This is distinct from Longformer (which combines local + global tokens) — SWA is pure local attention with no global tokens, relying on layer stacking for long-range flow.

The chapter covers Longformer/BigBird in the sparse attention section (`interpretability-efficient-architectures.html:401`) but never mentions the simpler SWA pattern that's actually more widely deployed. SWA reduces KV cache memory from O(n) to O(W) per layer, which is a major inference optimization.

> **Source**: Mistral 7B paper (Jiang et al., 2023) — SWA with W=4096, 32 layers gives effective context of 131K tokens.

---

## 3. RMSNorm — Missing

### What's Covered
- Pre-Norm vs Post-Norm LayerNorm — good coverage (`self-attention-the-transformer.html:595-633`)

### What's Missing
**RMSNorm (Root Mean Square Layer Normalization)** — Used by LLaMA, LLaMA 2/3, Mistral, Gemma, and virtually every modern open-source LLM. RMSNorm simplifies LayerNorm by removing the mean-centering step:

```
RMSNorm(x) = x / RMS(x) * γ,  where RMS(x) = sqrt(mean(x²))
```

This is ~10-15% faster than full LayerNorm because it skips computing the mean for centering. The empirical finding (Zhang & Sennrich, 2019) is that the re-centering in LayerNorm is unnecessary — the re-scaling alone provides sufficient normalization.

This is a **standard interview question**: "What normalization does LLaMA use and why?" The chapter mentions Pre-Norm but never discusses RMSNorm specifically.

**QK-Norm** — Normalizing queries and keys before computing attention scores. Used in Gemma 2 and some recent models to prevent attention logit growth. Not mentioned.

**DeepNorm** — Used for training very deep transformers (1000+ layers). Modifies residual connections with a scaling factor. Not mentioned.

---

## 4. Temporal Convolutional Networks (TCN) / WaveNet — Missing

### What's Missing
The chapter goes RNN → LSTM → GRU → Transformer, completely skipping the **causal convolution** branch that was a major RNN alternative from 2016-2018:

**WaveNet** (van den Oord et al., 2016) — DeepMind's breakthrough for audio generation. Uses **dilated causal convolutions** — convolutions that look only at past timesteps (causal) with exponentially increasing dilation rates (1, 2, 4, 8, 16...) to capture long-range dependencies. Receptive field grows exponentially with depth while parameter count grows linearly. This architecture directly inspired TCNs and is a conceptual ancestor to SSMs.

**TCN (Temporal Convolutional Networks)** (Bai et al., 2018) — Formalized the causal convolution approach as a general sequence modeling architecture. Key insight from the paper "An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling": TCNs matched or outperformed LSTMs on most standard benchmarks while being parallelizable during training.

**Why this matters**: TCNs/WaveNet represent the "convolution" path in the sequence modeling family tree (RNN path → LSTM/GRU, Convolution path → WaveNet/TCN, Attention path → Transformer, SSM path → S4/Mamba). The chapter covers the RNN, Attention, and SSM paths well but completely omits the convolution path. SSMs themselves use convolution as a key computational trick (covered in `state-space-models-mamba.html:368`), so TCNs provide important context.

> **Interview Q**: "What alternatives to RNNs existed before the Transformer, and why did they lose?" — Cannot be fully answered without TCNs.

---

## 5. Retrieval-Augmented Models — Missing

### What's Missing
No coverage of models that augment the transformer with retrieval:

**kNN-LM** (Khandelwal et al., 2020) — Augments a pretrained LM with nearest-neighbor lookup over a datastore of (context embedding, next token) pairs. The final prediction is `p(y|x) = λ · p_kNN(y|x) + (1-λ) · p_LM(y|x)`. Key insight: you can improve a language model's predictions without any additional training, just by giving it access to a large memory.

**RETRO** (Borgeaud et al., 2022) — DeepMind's Retrieval-Enhanced Transformer. Retrieves relevant chunks from a 2 trillion token database during forward pass. Uses cross-attention to condition generation on retrieved passages. Achieves GPT-3-level performance with 25× fewer parameters. This is the architectural foundation for understanding modern RAG systems.

**Why this matters**: RAG (Retrieval-Augmented Generation) is one of the most widely deployed LLM patterns in production. Understanding the architectural foundations (kNN-LM, RETRO) helps practitioners understand why RAG works and what its limitations are. The chapter covers attention and generation well but never discusses how retrieval integrates into the architecture.

---

## 6. Multi-Modal Transformers / Vision Transformers — Missing

### What's Missing
The chapter mentions that transformers have "taken over computer vision" (`self-attention-the-transformer.html:277`) but never explains how.

**Vision Transformer (ViT)** (Dosovitskiy et al., 2021) — Splits images into 16×16 patches, linearly embeds them, adds positional encodings, and processes with a standard transformer encoder. Demonstrated that the inductive biases of CNNs (locality, translation equivariance) aren't necessary — pure attention can match or beat CNNs with sufficient data. This is the single most important cross-domain application of transformers.

**CLIP** (Radford et al., 2021) — Contrastive Language-Image Pre-training. Trains paired image and text encoders with a contrastive objective. Foundation for multi-modal AI.

**Audio Transformers** — Whisper (Radford et al., 2022) uses an encoder-decoder transformer for speech recognition, treating audio as mel spectrogram patches (similar to ViT's image patches).

**Why this matters**: Understanding how transformers generalize beyond text to vision and audio is crucial for modern AI interviews and practice. ViT is one of the top-5 most cited ML papers ever.

> **Interview Q**: "How would you apply the transformer architecture to images?" — Unanswerable from current chapter.

---

## 7. Encoder-Decoder Models (T5, BART) — Underserved

### What's Covered
T5 and BART get exactly one sentence: "T5 and BART use the full encoder-decoder" (`self-attention-the-transformer.html`). DistilBERT is mentioned in the BERT/GPT section.

### What's Missing
**T5 (Text-to-Text Transfer Transformer)** (Raffel et al., 2020) — Unifies ALL NLP tasks as text-to-text. Classification, summarization, translation, QA — all framed as "input text → output text." The T5 paper is also one of the most important ablation studies in deep learning, systematically comparing pre-training objectives, architectures, dataset sizes, and transfer strategies. Key findings: (a) encoder-decoder outperforms decoder-only at equivalent compute for many tasks, (b) span corruption is a better pre-training objective than language modeling for encoder-decoders.

**BART** (Lewis et al., 2019) — Denoising autoencoder using full encoder-decoder. Pre-trained by corrupting text (deletion, masking, shuffling, rotation) and reconstructing the original. Excels at generation tasks.

**Flan-T5 / Instruction Tuning** — Flan-T5 showed that instruction-tuning an encoder-decoder model produces strong zero-shot performance. This bridges the gap between BERT-style and GPT-style.

---

## 8. Deeper RL Coverage — GRPO, Offline RL, Multi-Agent

### What's Covered
The RL section is quite comprehensive: MDP, Bellman, Q-learning, DQN, REINFORCE, Actor-Critic, PPO, RLHF, DPO (brief mention), Model-Based RL (brief).

### What's Missing

**GRPO (Group Relative Policy Optimization)** — Used by DeepSeek-R1 (2024). Eliminates the critic network entirely by sampling multiple responses per prompt and using group-relative advantages. This is a **very hot interview topic** in 2024-2025. The key equation: for each prompt, sample G responses, compute rewards R_1...R_G, then advantage A_i = (R_i - mean(R)) / std(R). Train with a clipped objective like PPO but without any value network.

**DPO Depth** — Currently gets one paragraph (`reinforcement-learning.html:1217`). DPO deserves more: the loss function, why it's equivalent to RLHF under certain assumptions, practical differences (no reward model, no RL loop, just supervised learning on preference pairs). The Bradley-Terry preference model underlying DPO is important.

**Offline RL / Batch RL** — Learning from fixed datasets without further environment interaction. Critical for real-world applications where online exploration is expensive or dangerous. Key algorithms: CQL (Conservative Q-Learning), IQL (Implicit Q-Learning), Decision Transformer (uses transformer architecture to frame RL as sequence modeling — directly relevant to this chapter!).

**Decision Transformer** (Chen et al., 2021) — Frames RL as sequence modeling: conditions a transformer on (return, state, action) tuples and autoregressively generates actions. No value functions, no Bellman equations — pure sequence prediction. This is the perfect bridge between the transformer and RL sections of this chapter.

**Multi-Agent RL (MARL)** — Not mentioned at all. Increasingly important for AI safety, game AI, and multi-LLM systems.

**Inverse RL / RLHF Connection** — The chapter covers RLHF but doesn't explain the Inverse RL foundation: learning a reward function from demonstrations. This is the theoretical basis for reward model training in RLHF Stage 2.

---

## 9. Mixture of Experts — Needs More Depth

### What's Covered
Basic MoE concept in Nice to Know (`nice-to-know.html:395-413`), mentions Mixtral and routing.

### What's Missing
- **Load balancing loss** — The auxiliary loss that prevents all tokens from routing to the same expert. This is critical to MoE training and a common interview question.
- **Expert parallelism** — How MoE models are distributed across GPUs (different from tensor/pipeline parallelism).
- **Capacity factor** — What happens when an expert is "full" and tokens get dropped.
- **Router architecture** — Top-k routing, soft routing, expert choice routing.
- **Switch Transformer** (Fedus et al., 2022) — Simplified MoE by routing each token to exactly 1 expert (top-1 routing), showing this works as well as top-2 while being simpler.

> **Interview Q**: "How do you prevent expert collapse in MoE training?" — Not answerable from current coverage.

---

## 10. Transformer Training Tricks & Modern Architecture Recipes

### What's Covered
- Pre-Norm vs Post-Norm ✅
- SwiGLU/GELU in FFN ✅
- Learning rate warmup mentioned in passing

### What's Missing

**RMSNorm** (covered above in §3)

**Sandwich Norm / Sub-LN** — Places normalization both before AND after the attention/FFN sublayers. Used in some very deep transformers to stabilize training.

**QK-Norm** — Normalizing Q and K before dot product. Used in Gemma 2 to prevent attention logit explosion at scale.

**Logit Soft-Capping** — Capping attention logits with `tanh(logits/cap) * cap`. Used in Gemma 2 to prevent outlier attention scores.

**Parallel Attention + FFN** — Computing attention and FFN in parallel rather than sequentially: `x + Attention(Norm(x)) + FFN(Norm(x))`. Used by PaLM and GPT-J/NeoX. ~15% faster with minimal quality loss.

**Tied Embeddings** — Sharing the input embedding matrix with the output projection (lm_head). Used by many models to reduce parameter count. Important for understanding model size.

**μP (Maximal Update Parameterization)** — Principled initialization and learning rate scaling that allows hyperparameters to transfer across model sizes. Important for efficient hyperparameter search.

---

## 11. Attention Sink Phenomenon — Missing

**Attention Sinks** (Xiao et al., 2023) — Discovery that the first few tokens in a sequence receive disproportionately high attention scores regardless of their content. This happens because softmax must distribute probability mass somewhere, and initial tokens become "sinks." Practical implication: for streaming/infinite-length generation, keeping the first few tokens in the KV cache (even when evicting middle tokens) maintains quality. This is directly relevant to the KV cache discussion already in the chapter.

---

## 12. Ring Attention / Sequence Parallelism — Missing

For very long sequences that don't fit in a single GPU's memory, **Ring Attention** (Liu et al., 2023) distributes the sequence across devices in a ring topology, overlapping communication and computation. **Sequence Parallelism** is the general paradigm. These are important for understanding how million-token context windows are achieved in practice (e.g., Gemini's 1M context).

---

## 13. Knowledge Distillation for Transformers — Underserved

DistilBERT is mentioned as a practical choice (`bert-gpt-the-two-paradigms.html`) but knowledge distillation itself — the technique of training a small "student" model to mimic a large "teacher" model — is never explained. This is one of the most important techniques for deploying transformers in production.

---

## 14. Decoding Strategies — Underserved

### What's Covered
- Beam search (in seq2seq section) ✅
- Greedy/beam briefly mentioned

### What's Missing
- **Top-k sampling** — Sample from the top-k highest probability tokens
- **Top-p (nucleus) sampling** — Sample from the smallest set of tokens whose cumulative probability exceeds p
- **Temperature scaling** — Division of logits by temperature T before softmax
- **Repetition penalty** — Penalizing tokens that have already appeared
- **Contrastive decoding** — Using the difference between a large and small model's predictions
- **Min-p sampling** — Recent alternative to top-p

These are **extremely common interview questions** for anyone working with LLMs: "Explain the difference between top-k and top-p sampling" or "What does temperature do?"

---

## 15. Transformer Computation Analysis — Missing

A dedicated analysis of transformer computational complexity that practitioners need:

- **Prefill vs Decode phases** — During inference, the prefill phase processes all input tokens in parallel (compute-bound), while the decode phase generates one token at a time (memory-bound). This distinction is critical for understanding inference optimization.
- **Arithmetic intensity** — Why prefill is compute-bound but decode is memory-bandwidth-bound
- **FLOPs estimation** — For a model with L layers, d_model dimensions, and n tokens: ~`2 * n * L * (12 * d² + n * d)` FLOPs per forward pass
- **Memory breakdown** — Model weights vs KV cache vs activations. For a 7B model, KV cache for 4K context ≈ 1GB with fp16.

> **Interview Q**: "Why is LLM inference memory-bound during token generation?" — Critical systems question, not covered.

---

## Priority Ranking for Addition

| Priority | Topic | Why |
|----------|-------|-----|
| 🔴 HIGH | ALiBi positional encoding | Major PE method, common interview Q, directly extends existing PE section |
| 🔴 HIGH | RMSNorm | Used by every modern LLM, simple addition to existing norm section |
| 🔴 HIGH | Sliding Window Attention | Used by Mistral/Gemma, fits naturally in efficient architectures section |
| 🔴 HIGH | Decoding strategies (top-k, top-p, temperature) | Extremely common interview topic, practical daily knowledge |
| 🔴 HIGH | Prefill vs Decode inference phases | Critical for LLM systems understanding |
| 🟡 MED | TCN / WaveNet | Important sequence modeling branch, missing from the evolutionary narrative |
| 🟡 MED | GRPO + deeper DPO | Hot 2024-25 topic, DeepSeek-R1 |
| 🟡 MED | Decision Transformer | Perfect bridge between transformer + RL sections |
| 🟡 MED | T5/BART encoder-decoder depth | Currently just one sentence for major model family |
| 🟡 MED | Retrieval-Augmented Models (RETRO, kNN-LM) | Foundation for RAG, increasingly important |
| 🟡 MED | ViT / multi-modal connection | Cross-domain transformer application, very common interview Q |
| 🟡 MED | MoE depth (load balancing, routing) | Extends existing coverage with practical details |
| 🟡 MED | Attention Sinks | Extends existing KV cache discussion naturally |
| 🟢 LOW | Offline RL / Batch RL | Niche but important for RL completeness |
| 🟢 LOW | Ring Attention / Sequence Parallelism | Infrastructure topic, may fit better in systems chapter |
| 🟢 LOW | Parallel Attention+FFN, QK-Norm, Sandwich Norm | Architecture minutiae, nice-to-know level |
| 🟢 LOW | Knowledge Distillation mechanics | May fit better in an LLM deployment chapter |
| 🟢 LOW | μP parameterization | Advanced training recipe |

---

## Sources Consulted
- Lilian Weng, "The Transformer Family v2" (2023) — https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/
- Sebastian Raschka, "LLM Reading List" (2023) — https://sebastianraschka.com/blog/2023/llm-reading-list.html
- Cameron Wolfe, "Decoder-Only Transformers" — https://cameronrwolfe.substack.com/p/decoder-only-transformers-the-workhorse
- Lin et al., "A Survey of Transformers" (2021) — arXiv:2106.04554
- Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models" (2023) — arXiv:2305.13245
- Press et al., "ALiBi: Train Short, Test Long" (2022) — arXiv:2108.12409
- Xiao et al., "Efficient Streaming Language Models with Attention Sinks" (2023)
- Shazeer, "GLU Variants Improve Transformer" (2020) — SwiGLU
- Zhang & Sennrich, "Root Mean Square Layer Normalization" (2019) — RMSNorm
- Raffel et al., "Exploring the Limits of Transfer Learning with T5" (2020)
