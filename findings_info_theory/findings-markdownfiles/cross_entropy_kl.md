# Cross-Entropy & KL Divergence — Key Findings

## Cross-Entropy
- H(P, Q) = -Σ p(x) log q(x)
- "How many bits to encode samples from P using a code optimized for Q"
- If Q = P, cross-entropy equals entropy (optimal). If Q ≠ P, it's higher (wasted bits).
- Binary CE: -[y log(q) + (1-y) log(1-q)]
- THIS IS THE STANDARD CLASSIFICATION LOSS. nn.CrossEntropyLoss() in PyTorch.
- Minimizing cross-entropy = maximum likelihood estimation (MLE). Same thing, different lens.

## KL Divergence
- D_KL(P‖Q) = Σ p(x) log[p(x)/q(x)]
- "Extra bits" — overhead of using Q instead of P
- KEY IDENTITY: H(P,Q) = H(P) + D_KL(P‖Q)
- Since H(P) is constant during training: min cross-entropy ≡ min KL divergence

## Forward vs Reverse KL (CRITICAL for interviews)
- Forward KL(P‖Q): mode-covering. Q must spread to cover all of P. Used in MLE.
- Reverse KL(Q‖P): mode-seeking. Q collapses onto high-density regions of P. Used in VI.
- With multimodal P and unimodal Q: forward → Q sits between modes. reverse → Q picks one mode.
- This asymmetry is WHY variational inference produces underdispersed posteriors.

## Jensen-Shannon Divergence
- JSD(P‖Q) = ½ D_KL(P‖M) + ½ D_KL(Q‖M), M = ½(P+Q)
- Symmetric, bounded [0, 1] with log₂, sqrt is a proper metric
- Original GAN loss ≈ JSD between real and generated distributions
- Problem: vanishing gradients when distributions don't overlap → Wasserstein distance
