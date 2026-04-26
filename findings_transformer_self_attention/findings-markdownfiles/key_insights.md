# Key Insights for Self-Attention & Transformer Rewrite

## sqrt(d_k) Scaling
- If Q,K elements are standard normal, dot product variance = d_k
- Large d_k → large dot products → softmax saturates → vanishing gradients
- Dividing by sqrt(d_k) normalizes variance back to ~1
- Vaswani et al quote: "We suspect that for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients"

## RoPE (Rotary Position Embeddings)
- Instead of adding position, rotate Q and K vectors by angle proportional to position
- Each dimension pair treated as 2D coordinates, rotated by pos × θ_i
- Key insight: dot product Q·K at positions m,n → rotation angles partially cancel → depends only on relative distance (m-n)
- Complex notation: z_k' = z_k · e^(iθ_k·p), inner product gives e^(iθ_k(p-q)) factor
- Used by LLaMA, Mistral, Qwen

## Pre-LN vs Post-LN
- Post-LN (original): LayerNorm(x + SubLayer(x)) — harder to train deep
- Pre-LN (modern): x + SubLayer(LayerNorm(x)) — clean residual identity shortcut
- Pre-LN allows stable training without warmup tricks, even 100+ layers
- GPT-2, GPT-3, LLaMA all use Pre-LN

## FFN as Key-Value Memory
- Geva et al. 2021: "Transformer Feed-Forward Layers Are Key-Value Memories"
- First linear layer = keys, nonlinearity = selector, second linear layer = values
- Factual knowledge stored in FFN weights, not attention patterns
- Meng et al. 2022: can surgically edit factual associations in GPT

## Multi-Head Attention Specialization
- Clark et al. 2019: specific heads correspond to syntax (direct objects, determiners) and coreference
- Some heads focus on syntactic dependencies (subject-verb)
- Some heads focus on coreference (pronoun → antecedent)
- Some heads encode positional/local patterns (attending to adjacent tokens)

## Residual Stream Interpretation
- All computation flows through the residual stream
- Attention heads and MLPs "write" feature vectors to this stream
- Each layer reads from and adds to the stream — information accumulates
- Original embedding travels through entire network, each layer adds delta

## SwiGLU
- Formula: SwiGLU(x) = (xW1) · Swish(xW2) where Swish(z) = z·σ(z)
- Gating mechanism: data-dependent on/off switching
- Used by LLaMA, PaLM — replaces ReLU/GELU in FFN blocks
- Shazeer 2020: "GLU Variants Improve Transformer"
