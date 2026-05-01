# Cross-Entropy Derivation from First Principles

## The Chain: Probability → Likelihood → Log-Likelihood → Cross-Entropy
1. Model outputs probability p for each sample
2. Likelihood = product of probabilities assigned to what actually happened
3. Log-likelihood = sum of log-probabilities (log turns product → sum)
4. Negative log-likelihood = cross-entropy loss

## Why Logarithm?
- Converts multiplicative probability to additive "surprise" (information theory)
- -log(0.99) ≈ 0.01 (barely surprised), -log(0.01) ≈ 4.6 (catastrophically wrong)
- Asymmetric punishment: confident wrong predictions destroyed
- log is monotonic → maximizing log-likelihood ≡ maximizing likelihood

## KL Divergence Connection
- H(P,Q) = H(P) + D_KL(P||Q)
- For hard labels (one-hot), H(P) = 0
- So minimizing cross-entropy = minimizing KL divergence
- KL divergence = information-theoretic distance between distributions

## Numerical Stability
- log(0) = -∞ → never compute sigmoid/softmax then log separately
- Use fused operations: binary_cross_entropy_with_logits, CrossEntropyLoss
- Identity: log(sigmoid(z)) = z - softplus(z) — avoids explicit sigmoid
