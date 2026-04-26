# Manifold Hypothesis

## Core Idea
- Real-world high-dimensional data concentrates near low-dimensional manifolds
- A 64x64 image = 12,288 dimensions, but meaningful images occupy a tiny fraction
- The "degrees of freedom" (pose, lighting, stroke width) are far fewer than pixel count

## Why It Matters for Deep Learning
- Neural networks learn to "unfold" these manifolds into flat, separable representations
- Explains why overparameterized networks don't always overfit — they learn manifold structure
- Autoencoders, GANs explicitly model this manifold
- This is the theoretical justification for representation learning

## The Tension with Curse of Dimensionality
- Curse says high dimensions are bad
- Manifold hypothesis says "yes, but data doesn't actually fill those dimensions"
- These two ideas together explain why deep learning works despite theoretical concerns

## Interview Angle
- "Why do deep networks work in high dimensions?" → manifold hypothesis
- Connects to: dimensionality reduction, feature learning, generalization
