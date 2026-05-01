# Entropy & Surprise — Key Findings

## Core Intuition
- Entropy = average surprise. Low probability events carry high surprise (information).
- Shannon (1948): H(X) = -Σ p(xᵢ) log₂ p(xᵢ)
- Fair coin = 1 bit. Biased 99% coin ≈ 0.08 bits. Fair die ≈ 2.58 bits.
- Maximum entropy = all outcomes equally likely. Minimum = one outcome certain.

## Why Log?
- Shannon was thinking about binary communication channels
- Log makes information additive: two independent events = sum of their information
- This is deeply satisfying — if I flip two fair coins, I need 2 bits, not some weird product

## Differential Entropy
- Continuous version: h(X) = -∫ p(x) log p(x) dx
- CAN be negative (peaked distributions)
- Gaussian: h = ½ log(2πeσ²)

## Conditional & Joint Entropy
- H(Y|X) = remaining uncertainty about Y after knowing X
- Chain rule: H(X,Y) = H(X) + H(Y|X)
- Decision trees: information gain = H(Y) - H(Y|X) — this is literally entropy reduction

## ML Applications
- Decision tree splitting (ID3, C4.5) = information gain at every node
- Entropy regularization in RL (SAC) — encourages exploration
- Maximum entropy models (MaxEnt) — least-biased distribution matching constraints
