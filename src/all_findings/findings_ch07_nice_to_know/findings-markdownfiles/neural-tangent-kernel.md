# Neural Tangent Kernel (NTK)

## Core Idea (Jacot et al., 2018)
- In the infinite-width limit, neural network training with gradient descent = kernel regression with a specific kernel (the NTK)
- Weights barely move from initialization → "lazy training" regime
- Network becomes effectively linear in its parameters
- The NTK stays constant during training (doesn't change as weights change)

## Why It Matters
- Makes neural network training mathematically tractable
- Provides convergence guarantees for wide networks
- Explains why wide networks can be analyzed with kernel methods

## The Catch
- Real networks operate in a "rich" or "feature learning" regime
- Weights move substantially, representations change — that's where the magic happens
- NTK theory explains a regime that practical deep learning has moved BEYOND
- Feature learning (what makes deep learning powerful) is exactly what NTK doesn't capture

## Interview Angle
- Know it exists, know what "lazy training" means
- Understand why it's theoretically important but practically limited
- Connection to: infinite width limits, Gaussian processes, kernel methods

## Key Formula
- K(x, x') = ∇_θ f(x; θ) · ∇_θ f(x'; θ)
- The kernel is the inner product of gradients of network output w.r.t. parameters
