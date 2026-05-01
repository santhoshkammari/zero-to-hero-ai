# Diffusion Models Research Summary

## Key Concepts to Cover (concept ladder):
1. The core intuition: destroying vs reconstructing (sand castle analogy)
2. Forward process - adding noise step by step (q distribution, Markov chain)
3. The closed-form trick: jumping to any timestep (reparameterization, alpha_bar)
4. Reverse process - learned denoising (p_theta, predicting noise)
5. Why noise prediction works (uniform loss scale across timesteps)
6. Score prediction vs noise prediction (Tweedie formula, score = gradient of log density)
7. The training loop (dead simple MSE)
8. DDPM sampling (1000 steps, slow)
9. DDIM - deterministic sampling, fewer steps (ODE view)
10. Classifier-free guidance (the technique that made text-to-image work)
11. Latent diffusion (VAE + U-Net + CLIP = Stable Diffusion)
12. ControlNet (spatial conditioning via zero convolutions)
13. Consistency models (one-step generation, self-consistency property)
14. Flow matching / rectified flows (straight paths, the future)

## Running Example: Photo restoration service
- Start with a family photo
- Show how noise destroys it
- Show how the model learns to undo it
- Extend to text-guided generation

## Key Analogies:
1. Sand castle analogy: kicking over a sand castle is easy, rebuilding it requires understanding what castles look like
2. Radio tuning analogy: denoising is like tuning a radio - at high static you hear the general melody, at low static you hear the lyrics

## Vulnerability moments:
- Admit procrastination on understanding the math
- Admit confusion about score vs noise prediction equivalence
- Acknowledge no one fully understands why the simple MSE loss works so well
- Confess that the ELBO derivation is where most people's eyes glaze over
- Still developing intuition for why flow matching is better

## Rest stop placement:
- After the training loop section (you now know enough to train a basic diffusion model)
