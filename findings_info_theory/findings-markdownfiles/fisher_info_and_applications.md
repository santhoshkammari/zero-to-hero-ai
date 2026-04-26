# Fisher Information & Bigger Picture Applications — Key Findings

## Fisher Information
- I(θ) = E[(∂/∂θ log p(x;θ))²]
- Measures how sensitive a distribution is to parameter changes
- High Fisher info = sharp curvature = data is informative about θ
- Cramér-Rao bound: Var(θ̂) ≥ 1/I(θ) — fundamental limit on estimation

## Natural Gradient Descent
- Regular GD: treats parameter space as Euclidean (flat)
- Natural GD: θ ← θ - η F⁻¹ ∇L — adjusts for geometry of distribution space
- Step size measured in distribution change, not raw parameter change
- K-FAC: practical approximation of natural gradient

## Elastic Weight Consolidation (EWC)
- Catastrophic forgetting: train on task B, forget task A
- EWC: use diagonal of Fisher matrix to identify "important" params for task A
- L_EWC = L_new + (λ/2) Σ Fᵢ(θᵢ - θ*ᵢ)²
- Params with high Fisher info change less during new task training

## MDL & Compression
- Minimum Description Length: best model = best compressor
- Total cost = bits for model + bits for data given model
- L1/L2 regularization, dropout, pruning = model compression in info-theoretic terms
- Bias-variance tradeoff restated in bits

## Variational Inference
- Find q(z) to minimize D_KL(q(z)‖p(z|x))
- Intractable → maximize ELBO instead
- VAE loss = reconstruction + KL(encoder posterior ‖ prior)
- Normalizing flows, diffusion models = making q(z) more flexible
