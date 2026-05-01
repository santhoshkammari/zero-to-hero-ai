# Classic Generative Models - Research Notes

## Key Concepts to Cover (Concept Ladder)

1. **Bedrock**: What does "generative" mean? Discriminative vs generative models.
2. **Autoencoders**: Vanilla (compress-reconstruct), denoising (corrupt-then-fix), sparse (penalty on activations)
3. **VAEs**: From AE to probabilistic - ELBO derivation, reparameterization trick, latent space smoothness
4. **GANs**: Minimax game, training dynamics, mode collapse, Wasserstein GAN
5. **Conditional Generation**: cGAN, CVAE - controlling what gets generated
6. **Normalizing Flows**: Change of variables, coupling layers, RealNVP, Glow
7. **Energy-Based Models**: Unnormalized densities, score matching, Langevin dynamics

## Running Example
A photo studio that learns to generate portrait photos. Start tiny: 3x3 pixel grayscale images.

## Key Insights from Research
- VAE ELBO: log p(x) >= E[log p(x|z)] - KL(q(z|x) || p(z)). Two terms fighting each other.
- Reparameterization: z = mu + sigma * epsilon. Move randomness outside the computation graph.
- GAN mode collapse: generator finds one "trick" and keeps repeating it
- Wasserstein distance: "minimum work to morph one dirt pile into another" - smooth gradients even when distributions don't overlap
- Normalizing flows: invertible transforms with tractable Jacobian determinants. Coupling layers split input, transform one half conditioned on the other.
- EBMs: p(x) = exp(-E(x))/Z. Z is intractable. Score matching sidesteps Z by learning gradient of log p(x).
- Langevin dynamics: iterative sampling using the score function + noise

## Analogies
1. **Sculptor analogy**: AE = sculptor who carves from a block (compression). VAE = sculptor who learns the "space of all possible sculptures." GAN = forger vs. art critic.
2. **Dirt pile analogy**: Wasserstein distance = minimum work to reshape one dirt pile into another.
3. **River/landscape analogy**: EBMs define an energy landscape. Low energy = likely data. Langevin dynamics = rolling a ball downhill with some random jostling.
