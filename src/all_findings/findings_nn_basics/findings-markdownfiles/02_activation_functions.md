# Activation Functions — Key Findings

## Why Nonlinearity
- Without activation: W2(W1x) = (W2W1)x = Wx — depth collapses to single linear transform
- Activation breaks this collapse, enabling each layer to carve new nonlinear boundaries

## ReLU — The Workhorse
- f(x) = max(0, x)
- Gradient = 1 for x > 0, 0 for x <= 0
- Sparse activation (~50% zeros) acts as implicit regularization
- Computationally trivial: comparison + branch
- Dying ReLU: 20-40% neurons can die with bad init or high LR

## Leaky ReLU / PReLU / ELU
- Leaky: f(x) = x if x > 0 else 0.01x — dead neurons can recover
- PReLU: learnable negative slope α
- ELU: exponential curve for negatives, pushes mean activations toward zero

## Sigmoid
- σ(x) = 1/(1+e^-x), range (0,1)
- Max gradient = 0.25 at x=0 — vanishing gradient killer
- 5 layers: 0.25^5 ≈ 0.001 gradient
- Only use: binary classification output layer

## Tanh
- Range (-1, 1), zero-centered (better than sigmoid)
- Max derivative = 1.0 (vs sigmoid's 0.25)
- Still saturates at extremes
- Lives on in LSTM/GRU gates

## GELU — Transformer Default
- GELU(x) = x · Φ(x) where Φ is standard normal CDF
- Smooth probabilistic gating — each input scaled by probability of being positive
- Small negative values get small nonzero output (vs ReLU's hard zero)
- Better gradient flow, works well with layer normalization
- Used in BERT, GPT, ViT

## SiLU/Swish
- SiLU(x) = x · σ(x) — self-gated activation
- Nearly identical to GELU in shape
- From Google Brain 2017 via automated search
- Used in EfficientNet, some diffusion models

## Softmax
- Operates across entire vector, produces probability distribution
- Temperature scaling: T < 1 sharpens, T > 1 flattens
- Standard for multi-class output

## Weight Initialization
- Xavier/Glorot: Var = 1/(n_in + n_out) — for sigmoid/tanh
- He/Kaiming: Var = 2/n_in — for ReLU (compensates for zeroed negatives)
- Bad init → vanishing/exploding activations → dead neurons or NaN loss
