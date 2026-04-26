# LLM Families & Architecture Research Summary

## Key Insights for Rewrite

### GPT Evolution
- GPT-1 (117M): Proved unsupervised pretraining transfers. 12 layers, 768 hidden.
- GPT-2 (1.5B): Zero-shot via scale. 48 layers, 1600 hidden. "Language models are unsupervised multitask learners."
- GPT-3 (175B): Few-shot in-context learning. 96 layers, 12288 hidden. $4.6M training cost.
- InstructGPT/3.5: RLHF alignment. Powered early ChatGPT.
- GPT-4: Rumored ~1.8T MoE. Multimodal. Passes bar exam.
- GPT-4o: Omni-modal. Natively handles text+vision+audio.
- Key thesis: Architecture barely changed. Scale + training signal is the bet.

### LLaMA Evolution (CORRECTED from web search)
- LLaMA-1 actually DID use RoPE, RMSNorm, and SwiGLU (from the paper). Web search was wrong.
- LLaMA-1: 7B-65B, trained on 1-1.4T tokens public data. Applied Chinchilla scaling.
- LLaMA-2: Added GQA for 70B model. Commercial license. RLHF chat variants.
- LLaMA-3: 8B/70B/405B, 15T tokens. 128K vocab. All models use GQA.

### Mistral/Mixtral
- Mistral-7B: Sliding window attention (W=4096), GQA. Beat LLaMA-2 13B.
- Mixtral 8x7B: 8 expert FFNs, 2 active per token. 46.7B total, ~13B active.
- Rolling KV cache: fixed-size circular buffer.
- Effective receptive field = L layers × W window = 32 × 4096 = 131K.

### Architecture Innovations
- RoPE: Rotary position embeddings. Encode via rotation. q_m · k_n depends on (m-n).
- ALiBi: Linear bias on attention scores. Simpler. Better extrapolation.
- GQA: Middle ground between MHA (all heads have KV) and MQA (shared KV).
- SwiGLU: Gated activation. More expressive than GELU. Three weight matrices.
- Pre-norm with RMSNorm: Stable training, clean gradient flow.
- Parallel attention+FFN (GPT-J style): x = x + Attention(LN(x)) + FFN(LN(x))

### DeepSeek MLA
- Multi-head Latent Attention: Compress KV into low-dim latent space.
- Reduces KV cache dramatically.

### Running Example Idea
- Build a "model zoo" scenario: we're an ML team choosing/building an LLM for a startup.
- Start with 3 team members trying to pick a model. Grow complexity.
