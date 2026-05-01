# Gradient Descent Core Insights

## Key Mental Models
- Loss landscape as a terrain you navigate blindfolded — you can only feel the slope at your feet
- The gradient is a vector of partial derivatives pointing UPHILL — you step in the NEGATIVE direction
- Update rule: θ = θ - α * ∇L(θ) — everything else is a variation on this

## Three Variants (Accuracy vs Speed Tradeoff)
1. **Batch GD**: Full dataset gradient, smooth but expensive per step
2. **SGD (pure)**: One sample, noisy but cheap — noise actually helps escape bad minima
3. **Mini-batch SGD**: The practical sweet spot (32-512 samples). This is what everyone actually uses when they say "SGD"

## Critical Insight: SGD Noise is a Feature
- Stochastic noise acts as implicit regularization
- Helps escape saddle points and sharp minima
- Smaller batches → more noise → tend to find flatter, better-generalizing minima
- This is why just cranking up batch size doesn't always help

## The Learning Rate is Everything
- Too high: divergence, NaN losses
- Too low: painfully slow, stuck in bad minima
- The "Karpathy constant" 3e-4 for Adam — folklore that works empirically
- For SGD: start ~0.1 and decay
- Learning rate finder: exponentially increase LR for one epoch, pick steepest descent point
