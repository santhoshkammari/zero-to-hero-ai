# Generative AI Breakthroughs: Beyond Basic Diffusion

> **Flow Matching, Consistency Models, Rectified Flow, DiT, Video Generation, and the New Frontier**

---

## Why This Matters

Diffusion models revolutionized generative AI—DALL-E 2, Stable Diffusion, Midjourney all proved that
iteratively denoising random noise could produce photorealistic images. But they had a fundamental
problem: **they were slow**. Generating a single image required 50–1000 sequential denoising steps,
each one a full neural network forward pass. A 1024×1024 image might take 30 seconds on a high-end GPU.

Between 2023 and 2025, a cascade of breakthroughs shattered this bottleneck:

- **Flow Matching** replaced the curved, stochastic diffusion paths with straight, deterministic
  trajectories—needing far fewer steps for the same quality
- **Consistency Models** showed you could map *any* noise level directly to clean data in a
  **single step**, matching multi-step diffusion quality
- **Rectified Flow** provided a principled way to *straighten* existing flow paths iteratively
- **Diffusion Transformers (DiT)** replaced U-Net backbones with Transformers, unlocking the
  scaling laws that made GPT successful
- **Video generation** went from 4-second clips to minutes of coherent footage (Sora, Kling, Runway)
- **3D generation** and **autoregressive image models** opened entirely new paradigms

These aren't incremental improvements. They represent a fundamental rethinking of *how* generative
models transform noise into structure. This document traces the mathematical ideas behind each
breakthrough.

---

## Diffusion Models Recap

Before understanding what came next, we need a solid grasp of what diffusion models do and where
they struggle.

### The Forward Process: Systematically Destroying Data

Given a data sample **x₀** (e.g., an image), diffusion models define a **forward process** that
gradually adds Gaussian noise over T timesteps:

```
q(xₜ | xₜ₋₁) = N(xₜ; √(1 - βₜ) · xₜ₋₁, βₜ · I)
```

where βₜ is a **variance schedule** (typically increasing from ~0.0001 to ~0.02). After enough
steps, xₜ becomes indistinguishable from pure Gaussian noise.

**The key mathematical trick**: you can skip directly to any timestep t without iterating:

```
q(xₜ | x₀) = N(xₜ; √(ᾱₜ) · x₀, (1 - ᾱₜ) · I)
```

where ᾱₜ = ∏ₛ₌₁ᵗ (1 - βₛ) is the cumulative product of noise retention. This means:

```
xₜ = √(ᾱₜ) · x₀ + √(1 - ᾱₜ) · ε,    where ε ~ N(0, I)
```

This closed-form "jump to any noise level" is what makes training efficient—you don't need to
simulate T steps for each training example.

### The Reverse Process: Learning to Denoise

The generative process runs this in reverse. Starting from pure noise xₜ ~ N(0, I), we learn
a neural network to iteratively remove noise:

```
pθ(xₜ₋₁ | xₜ) = N(xₜ₋₁; μθ(xₜ, t), Σθ(xₜ, t))
```

**What does the network actually predict?** There are three equivalent parameterizations:

1. **Predict the noise** ε: The network εθ(xₜ, t) predicts the noise that was added.
   This is the DDPM formulation (Ho et al., 2020).
2. **Predict the clean data** x₀: The network directly outputs a denoised estimate.
3. **Predict the score** ∇ₓ log p(xₜ): The gradient of the log-probability density,
   telling us which direction leads to higher-probability (cleaner) data.

These are mathematically related. The noise prediction ε and score ∇ₓ log p(xₜ) are
connected by:

```
∇ₓₜ log q(xₜ) = -ε / √(1 - ᾱₜ)
```

### Score Matching and Denoising Score Matching

**Score matching** (Hyvärinen, 2005) trains a model to estimate ∇ₓ log p(x) without knowing
the normalizing constant of p(x). The objective:

```
L = E_p(x) [ ‖sθ(x) - ∇ₓ log p(x)‖² ]
```

The problem: we don't know ∇ₓ log p(x) for real data. **Denoising score matching** (Vincent, 2011)
sidesteps this by adding noise and matching the score of the *noised* distribution:

```
L_DSM = E_{x₀~p_data, xₜ~q(xₜ|x₀)} [ ‖sθ(xₜ, t) - ∇ₓₜ log q(xₜ | x₀)‖² ]
```

Since q(xₜ | x₀) is Gaussian, we know its score analytically:

```
∇ₓₜ log q(xₜ | x₀) = -(xₜ - √(ᾱₜ) · x₀) / (1 - ᾱₜ) = -ε / √(1 - ᾱₜ)
```

This is exactly why training a noise predictor εθ is equivalent to score matching.

### DDPM: The Workhorse

**DDPM** (Ho, Jain, Abbeel, 2020) uses the simplified training objective:

```
L_simple = E_{t, x₀, ε} [ ‖ε - εθ(xₜ, t)‖² ]
```

Training: sample x₀ from data, sample t uniformly from {1,...,T}, sample ε ~ N(0,I),
compute xₜ, predict εθ(xₜ, t), minimize MSE.

Sampling: start from xₜ ~ N(0,I), iteratively denoise for T steps (typically T=1000).

**The bottleneck**: 1000 sequential forward passes at inference time.

### DDIM: Fewer Steps via Deterministic Sampling

**DDIM** (Song, Meng, Ermon, 2020) reinterprets diffusion as a *non-Markovian* process,
enabling deterministic sampling with a **subsampled** set of timesteps:

```
xₜ₋₁ = √(ᾱₜ₋₁) · x̂₀ + √(1 - ᾱₜ₋₁) · εθ(xₜ, t)
```

where x̂₀ = (xₜ - √(1-ᾱₜ) · εθ(xₜ, t)) / √(ᾱₜ) is the predicted clean image.

The breakthrough: instead of 1000 steps, DDIM can use 50 or even 20 steps by selecting
a subsequence of timesteps. Quality degrades but the speed-quality tradeoff was transformative.

**Insight**: DDIM converts the stochastic sampling process into solving a **probability flow ODE**.
This connection to ODEs opened the door to flow matching.

### Classifier-Free Guidance (CFG)

**CFG** (Ho & Salimans, 2022) is perhaps the single most impactful trick for conditional generation.
The idea: train a single model that can be both conditional and unconditional by randomly dropping
the conditioning signal during training (replacing the text prompt with ∅ some fraction of the time).

At inference, combine both predictions:

```
ε̃θ(xₜ, t, c) = εθ(xₜ, t, ∅) + w · (εθ(xₜ, t, c) - εθ(xₜ, t, ∅))
```

where w > 1 is the **guidance scale**. This amplifies the "direction" from unconditional to
conditional, pushing the model toward outputs that more strongly match the condition c.

**In score function form**:

```
s_CFG = ∇ₓ log p(xₜ) + w · ∇ₓ log p(c | xₜ)
```

This is equivalent to sampling from p(xₜ | c)^w · p(xₜ)^(1-w)—a sharpened version of the
conditional distribution. Higher w = more adherence to the prompt but less diversity.

**Why it matters**: CFG is used in virtually every modern diffusion/flow model. It requires
2× the compute per step (one conditional + one unconditional forward pass) but dramatically
improves sample quality and text alignment.

---

## Flow Matching — The Elegant Alternative

Flow matching emerged in 2022-2023 as a cleaner, simpler framework for training generative models
that addresses the fundamental inefficiencies of diffusion.

### Continuous Normalizing Flows: The Predecessor

**Continuous Normalizing Flows (CNFs)** (Chen et al., 2018) define a generative model through an
ODE. Given a simple base distribution p₀ (e.g., Gaussian noise), a vector field vθ(x, t)
transports samples along a continuous path:

```
dx/dt = vθ(x(t), t),    t ∈ [0, 1]
```

Starting from x(0) ~ p₀, integrating this ODE to t=1 yields a sample from the data distribution.

**The original problem**: training CNFs required simulating the ODE during training (expensive!)
and computing the Jacobian trace for the likelihood objective. This made them impractical at scale.

### Flow Matching: Training Without Simulation

**Flow Matching** (Lipman et al., 2022; Liu et al., 2022; Albergo & Vanden-Eijnden, 2022)
solved this by defining a **simulation-free** training objective. The core insight:

> Instead of learning the velocity field by simulating the entire flow, define **conditional
> probability paths** between individual noise-data pairs and regress the velocity field
> against these known paths.

#### The Mathematical Setup

We want to learn a velocity field vθ(x, t) for t ∈ [0, 1] that transports:
- p₀ = N(0, I) (noise at t=0)
- p₁ = p_data (data at t=1)

The probability density pₜ(x) evolves according to the **continuity equation**:

```
∂pₜ/∂t + ∇ · (pₜ · vₜ) = 0
```

This is mathematically beautiful: the density "flows" along the velocity field, like fluid dynamics.

#### Conditional Paths: The Key Innovation

For a single data point x₁ sampled from the data and noise x₀ ~ N(0, I), define the
**conditional** interpolation path:

```
xₜ = (1 - t) · x₀ + t · x₁
```

This is a straight line from noise to data! The conditional velocity along this path is simply:

```
uₜ(x | x₀, x₁) = x₁ - x₀
```

A constant vector pointing from the noise sample to the data sample.

#### The Flow Matching Loss

Train vθ by regressing against these conditional velocities:

```
L_FM = E_{t~U(0,1), x₀~N(0,I), x₁~p_data} [ ‖vθ(xₜ, t) - (x₁ - x₀)‖² ]
```

**That's it.** No ODE simulation during training. No Jacobian traces. Just:
1. Sample noise x₀ and data x₁
2. Pick a random time t
3. Compute the interpolant xₜ = (1-t)·x₀ + t·x₁
4. Predict the velocity vθ(xₜ, t) and regress against the target (x₁ - x₀)

#### Why Straight Paths Beat Diffusion Paths

**Diffusion models** follow **curved, stochastic** trajectories from noise to data. The paths
are governed by SDEs (stochastic differential equations) with both drift and diffusion terms.
When you convert to the probability flow ODE (as DDIM does), the paths are still curved because
the noise schedule imposes a non-linear relationship.

**Flow matching** directly learns **straight-line** trajectories in the simplest formulation.
Why does this matter?

1. **Fewer discretization steps**: Straight paths require fewer ODE solver steps to approximate
   accurately. A straight line can be traversed in one Euler step; a curved path needs many.

2. **Lower truncation error**: ODE solvers (Euler, Runge-Kutta) accumulate error proportional
   to path curvature. Straighter paths = less error per step.

3. **Faster convergence**: The simple velocity target (x₁ - x₀) is easier to learn than the
   complex score function ∇ₓ log pₜ(x) that diffusion models must estimate.

4. **Optimal transport connection**: The straight-line paths correspond to the **optimal
   transport** (Monge) map between the noise and data distributions—the shortest-distance
   transport plan.

#### General Conditional Flow Matching

The framework generalizes beyond linear interpolation. For conditioning on additional context c:

```
L_CFM = E_{c, t, x₀, x₁~p(·|c)} [ ‖vθ(xₜ, t, c) - (x₁ - x₀)‖² ]
```

You can also use different interpolation schemes:

```
xₜ = αₜ · x₁ + σₜ · x₀
```

where αₜ and σₜ define the path. Setting αₜ = t, σₜ = 1-t gives the linear case.
Setting them to match the DDPM noise schedule recovers diffusion training!

**Flow matching is strictly more general than diffusion**—diffusion is a special case of flow
matching with a particular (curved) path choice.

#### Stable Diffusion 3 and Flow Matching

Stability AI's **Stable Diffusion 3** (Esser et al., 2024) adopted flow matching as its training
paradigm, combined with a new **MMDiT (Multimodal Diffusion Transformer)** architecture.

Key SD3 innovations built on flow matching:
- **Rectified flow** formulation with linear interpolation paths
- **Logit-normal timestep sampling**: instead of uniform t ~ U(0,1), sample t from a
  logit-normal distribution that emphasizes intermediate timesteps (where learning is hardest)
- **Separate transformer streams** for text and image tokens that interact via attention
- This combination produced state-of-the-art text-to-image quality at the time of release

---

## Consistency Models

### The Problem: Even Flow Matching Needs Multiple Steps

Flow matching reduced the step count from 1000 to ~20-50, but each step still requires a
full network forward pass. For real-time applications (interactive editing, video games,
on-device generation), even 20 steps may be too many.

**Consistency Models** (Song et al., 2023) from OpenAI asked a radical question:
*Can we map ANY noise level directly to the final clean output in a single step?*

### The Self-Consistency Property

The defining property of consistency models is **self-consistency**: for any point on the
same trajectory of the diffusion ODE, the model maps to the same output.

Formally, let f(xₜ, t) be the consistency function. The **self-consistency property** requires:

```
f(xₜ, t) = f(xₜ', t')    for all t, t' on the same ODE trajectory
```

This means: if you take a noisy image xₜ at noise level t and a *differently-noised version*
xₜ' at noise level t' (both derived from the same clean image x₀ via the forward process),
the consistency model must map both to the **same output**.

**Boundary condition**: At t = 0 (clean data):

```
f(x₀, 0) = x₀
```

The model is the identity at the clean-data endpoint.

### Mathematical Formulation

Consider the probability flow ODE of a pre-trained diffusion model:

```
dx/dt = v(x, t)
```

where v(x, t) is the velocity field (from the diffusion model's score function).

Any point xₜ on this ODE trajectory eventually reaches x₀ at t = 0. The consistency
function is:

```
f(xₜ, t) = xₜ + ∫₀ᵗ v(xₛ, s) ds    (mapping xₜ back to x₀)
```

But we don't want to actually compute this integral (that would be multi-step sampling!).
Instead, we **train a neural network** fθ to satisfy self-consistency directly.

### Two Training Approaches

#### 1. Consistency Distillation (CD)

Start with a pre-trained diffusion model. For adjacent timesteps tₙ > tₙ₋₁:

```
L_CD = E [ d(fθ(xₜₙ, tₙ), fθ⁻(x̂ₜₙ₋₁, tₙ₋₁)) ]
```

where:
- xₜₙ is a noisy sample at time tₙ
- x̂ₜₙ₋₁ is obtained by running **one step** of the pre-trained diffusion ODE from tₙ to tₙ₋₁
- fθ⁻ is an **exponential moving average** (EMA) of the model parameters (the "teacher")
- d(·,·) is a distance metric (L2, LPIPS, etc.)

The intuition: adjacent points on the ODE trajectory should map to the same output.
The EMA teacher provides stable targets, similar to target networks in RL.

#### 2. Consistency Training (CT)

No pre-trained model needed! Instead of using a diffusion model to connect adjacent
timesteps, use the forward process directly:

```
L_CT = E_{x₀, t, ε} [ d(fθ(xₜₙ, tₙ), fθ⁻(xₜₙ₋₁, tₙ₋₁)) ]
```

where both xₜₙ and xₜₙ₋₁ are obtained by adding noise to the *same* x₀ at different levels.

This is more challenging but eliminates the need for a pre-trained diffusion model entirely.

### Architecture: Enforcing the Boundary Condition

To ensure f(x₀, 0) = x₀, consistency models use a **skip connection** parameterization:

```
fθ(x, t) = cₛₖᵢₚ(t) · x + cₒᵤₜ(t) · Fθ(x, t)
```

where cₛₖᵢₚ(0) = 1, cₒᵤₜ(0) = 0 (so at t=0, the output equals the input), and Fθ is
the neural network backbone. A common choice:

```
cₛₖᵢₚ(t) = σ_data² / (σ_data² + t²)
cₒᵤₜ(t) = t / √(σ_data² + t²)
```

### One-Step Generation

At inference:
1. Sample x_T ~ N(0, σ_max² · I)
2. Output = fθ(x_T, T)

**That's one forward pass.** The model directly maps noise to a clean image.

### Multi-Step Refinement

Consistency models also support optional multi-step refinement. After the initial prediction,
you can:
1. Re-noise the output to an intermediate level t'
2. Apply the consistency model again: fθ(x_t', t')
3. Repeat

Each additional step improves quality. This creates a smooth trade-off between speed (1 step)
and quality (multiple steps).

### Improved Consistency Training (iCT)

**Improved Consistency Training** (Song & Dhariwal, 2023) addressed several limitations:
- Better noise schedules adapted for consistency training
- Pseudo-Huber loss instead of L2/LPIPS
- Lossless training curriculum that progressively increases the number of discretization steps
- Achieved FID scores competitive with state-of-the-art diffusion models using just 2 steps

---

## Rectified Flow

### Straightening the Paths

**Rectified Flow** (Liu et al., 2022) provides a complementary perspective to flow matching,
focusing specifically on the problem of **path straightness** and a procedure to iteratively
improve it.

### The Core Observation

Consider a coupling (X₀, X₁) where X₀ ~ π₀ (noise) and X₁ ~ π₁ (data). The simplest
transport map defines the interpolation:

```
Xₜ = (1 - t) · X₀ + t · X₁
```

The velocity field that generates this interpolation is:

```
vₜ(x) = E[X₁ - X₀ | Xₜ = x]
```

This is a **conditional expectation**—the average direction from noise to data, given that
the trajectory passes through x at time t.

The trained model learns this conditional expectation, which is precisely the flow matching
objective:

```
L = E_{t, X₀, X₁} [ ‖vθ(Xₜ, t) - (X₁ - X₀)‖² ]
```

### The Problem: Crossing Paths

Even though individual (X₀, X₁) pairs define straight lines, the **learned** velocity field
vₜ(x) may represent *curved* trajectories. Why? Because many different (X₀, X₁) pairs have
trajectories that **cross each other** at intermediate times:

```
    X₁ᴬ ←——— crossing ———→ X₁ᴮ
     ↑            ×            ↑
    X₀ᴬ                      X₀ᴮ
```

When paths cross, the conditional expectation vₜ(x) at the crossing point must average
over multiple directions, creating a curved (and less efficient) flow.

### The Reflow Procedure

**Reflow** iteratively straightens these paths:

1. **Train** a rectified flow model v¹θ on the initial coupling (X₀, X₁)
2. **Generate new pairs**: for each noise sample X₀, solve the ODE dx/dt = v¹θ(x, t)
   from t=0 to t=1 to get X̂₁. This creates a new coupling (X₀, X̂₁).
3. **Retrain** a new model v²θ on the new coupling (X₀, X̂₁)
4. **Repeat**: Each iteration produces straighter paths because the new coupling has
   fewer crossing trajectories.

**Why it works**: After one pass of the learned ODE, each X₀ maps to a specific X̂₁.
The paths in this new coupling don't cross (they follow the deterministic ODE), so the
next model can learn straighter trajectories.

### Mathematical Guarantee

The **transport cost** (average squared path length) decreases monotonically with each
reflow iteration:

```
E[‖X̂₁⁽ᵏ⁺¹⁾ - X₀‖²] ≤ E[‖X̂₁⁽ᵏ⁾ - X₀‖²]
```

In the limit, reflow converges to straight-line transport (the optimal transport map).

### Connection to Flow Matching and Diffusion

- **Rectified Flow = Flow Matching** in the first iteration (same objective)
- **Reflow** is the novel contribution—a procedure to iteratively improve the coupling
- Diffusion models with DDIM sampling can be seen as a single (curved) flow;
  rectified flow straightens this
- **InstaFlow** (Liu et al., 2023) applied one step of reflow + distillation to achieve
  high-quality one-step generation

### Practical Impact

Rectified flow is the foundation for several production systems:
- **Stable Diffusion 3** uses a rectified flow formulation
- **FLUX** (Black Forest Labs) models use rectified flow
- The combination of rectified flow + distillation enables ~4-step high-quality generation

---

## Video Generation

### The Temporal Coherence Challenge

Video generation is *qualitatively harder* than image generation. A 10-second 30fps video
at 1080p contains:

```
300 frames × 1920 × 1080 × 3 channels = ~1.86 billion values
```

But the real challenge isn't just size—it's **temporal coherence**:
- Objects must maintain consistent appearance across frames
- Motion must be physically plausible
- Scene lighting and geometry must evolve smoothly
- Camera motion must be coherent

A model that generates beautiful individual frames but with flickering objects or teleporting
elements produces unwatchable video.

### How Video Diffusion Models Work

Video diffusion models extend image diffusion to the spatiotemporal domain.

#### Architecture: Inflating 2D to 3D

The standard approach starts with a pre-trained image diffusion model and "inflates" it
to handle video:

**Spatial layers** (pre-trained, often frozen or fine-tuned):
- 2D convolutions for spatial features
- Spatial self-attention within each frame

**Temporal layers** (newly added, trained from scratch):
- **Temporal attention**: each spatial position attends across all frames
- **Temporal convolutions**: 1D convolutions along the time axis
- **Cross-frame attention**: frames attend to key frames or reference frames

The interleaving looks like:

```
Input video tensor: (B, T, C, H, W)

For each block:
  1. Spatial Conv2D: process each frame independently
  2. Spatial Self-Attention: within each frame
  3. Temporal Attention: across frames at each spatial location
  4. Cross-Attention to text: inject text conditioning
  5. Feed-Forward Network
```

#### Temporal Attention Deep Dive

Temporal attention is the key mechanism. For a feature map of shape (T, H×W, C):

```
Reshape to: (H×W, T, C)    — each spatial position has T temporal tokens
Apply multi-head self-attention across the T dimension
Reshape back to: (T, H×W, C)
```

This allows frame 1 to attend to frame 50, learning long-range temporal dependencies
like "the ball thrown in frame 1 should land in frame 50."

#### Frame Conditioning Strategies

Several strategies maintain coherence:

1. **Autoregressive**: Generate frame-by-frame, conditioning each on previous frames.
   Coherent but slow and prone to drift.

2. **Hierarchical**: Generate keyframes first, then interpolate. Maintains long-range
   structure but may miss fine dynamics.

3. **Full 3D**: Process all frames jointly. Best quality but extreme compute requirements.

4. **Sliding window**: Process overlapping temporal windows with shared frames for
   continuity. Practical for long videos.

### Sora: Spacetime Patches

OpenAI's **Sora** (2024) represented a paradigm shift in video generation by treating video
as a collection of **spacetime patches**.

#### The Architecture

Sora combines:
1. A **video VAE** (variational autoencoder) that compresses video into a spatiotemporal
   latent space
2. A **Diffusion Transformer (DiT)** that operates on patches of this latent space
3. Text conditioning via cross-attention with text embeddings

#### Spacetime Patch Tokenization

Instead of operating on individual pixels or frames, Sora:

1. **Compresses** the video using a spatial-temporal VAE encoder:
   ```
   Raw video: (T, H, W, 3)  →  Latent: (T', H', W', C)
   ```
   where T' << T, H' << H, W' << W (e.g., 4× temporal, 8× spatial compression)

2. **Patchifies** the latent into non-overlapping 3D patches:
   ```
   Latent: (T', H', W', C)  →  Patches: (N, D)
   ```
   where N = (T'/pₜ) × (H'/pₕ) × (W'/p_w) is the number of patches and
   D = pₜ × pₕ × p_w × C is the patch embedding dimension

3. Each patch becomes a **token** processed by the transformer

This is analogous to how Vision Transformers (ViT) patchify images, extended to 3D.

#### Why Spacetime Patches Matter

- **Resolution agnostic**: Different video resolutions/durations produce different numbers
  of tokens, but the same architecture processes them all
- **Native aspect ratios**: No need to crop/pad to fixed sizes
- **Scalable**: Transformer compute scales with token count, enabling systematic
  quality-compute tradeoffs
- **Emergent capabilities**: Training at multiple resolutions lets the model learn
  cross-resolution representations

#### The Compute Challenge

Sora-class models require enormous compute:
- Training: estimated thousands of GPU-years
- Inference: minutes per video on high-end hardware
- The attention mechanism is O(N²) in the number of tokens, and a 1-minute video
  may have millions of latent tokens

This motivates all the efficiency work: flow matching (fewer steps), consistency models
(one step), and architectural innovations (efficient attention variants).

---

## DiT — Diffusion Transformers

### Why Replace U-Net?

The **U-Net** was the default backbone for diffusion models since DDPM. It features:
- Encoder-decoder structure with skip connections
- Downsampling/upsampling through the network
- Attention at lower resolutions
- Strong inductive biases for image structure

But U-Nets have limitations:
- **Scaling behavior**: Adding parameters doesn't consistently improve quality
- **Fixed resolution**: Architecture is tied to specific spatial dimensions
- **Limited attention**: Attention only at lower resolutions due to quadratic cost
- **Architecture complexity**: Many design choices (channel multipliers, attention
  resolutions, number of ResNet blocks)

### DiT: Scalable Diffusion Models with Transformers

**DiT** (Peebles & Xie, 2023) replaced U-Net with a **plain Vision Transformer (ViT)**
backbone, demonstrating that the scaling laws that made language models successful also
apply to diffusion.

#### Architecture

```
Input image → VAE encoder → Latent (H', W', C)
           → Patchify → Patch tokens (N, D)
           → + Positional encoding
           → DiT Blocks × L
           → Unpatchify
           → VAE decoder → Output image
```

Each **DiT Block** contains:
1. Layer Normalization (adaptive)
2. Multi-head Self-Attention
3. Layer Normalization (adaptive)
4. Feed-Forward Network (MLP)

The critical innovation is **how conditioning enters the network**.

### AdaLN-Zero: The Conditioning Mechanism

DiT explored several conditioning approaches and found **Adaptive Layer Normalization
with Zero initialization (AdaLN-Zero)** to be the best.

Standard Layer Normalization:
```
LayerNorm(h) = γ · (h - μ) / σ + β
```

**Adaptive** Layer Normalization makes γ and β functions of the conditioning:
```
AdaLN(h, c) = γ(c) · (h - μ) / σ + β(c)
```

where c = embed(timestep) + embed(class_label) and γ(c), β(c) are learned linear
projections.

**AdaLN-Zero** adds a crucial trick: it also learns a **gating parameter** α for the
residual connection, initialized to zero:

```
h ← h + α(c) · Attention(AdaLN(h, c))
h ← h + α'(c) · FFN(AdaLN(h, c))
```

**Why zero initialization?** At the start of training, each DiT block is an identity
function (because α = 0). This means:
- The initial model is well-behaved (outputs noise)
- Conditioning is gradually "learned in" during training
- Training is more stable compared to models that must immediately integrate conditioning

### Scaling Results

DiT demonstrated clear **scaling laws** for diffusion:

| Model     | Parameters | GFLOPs | FID-50K (ImageNet) |
|-----------|------------|--------|--------------------|
| DiT-S/2   | 33M       | 6      | 68.4              |
| DiT-B/2   | 130M      | 23     | 43.5              |
| DiT-L/2   | 458M      | 80     | 23.3              |
| DiT-XL/2  | 675M      | 119    | 9.62              |

**More parameters = better FID**, consistently. This mirrors the language model scaling
behavior and suggests that simply making diffusion transformers bigger will continue to
improve quality.

### The MMDiT Variant (Stable Diffusion 3)

SD3 extends DiT with the **MMDiT (Multimodal DiT)** architecture:

- **Two token streams**: one for image latents, one for text tokens
- Each stream has its **own** set of linear projections for Q, K, V in attention
- The streams are **concatenated** for joint attention, then separated
- This allows the model to learn modality-specific representations while still
  enabling cross-modal interaction

```
Image tokens  → Q_img, K_img, V_img ─┐
                                       ├─ Joint Attention ─→ Split ─→ Image FFN
Text tokens   → Q_txt, K_txt, V_txt ─┘                   └→ Text FFN
```

### Impact

DiT is now the **dominant architecture** for generative models:
- **Sora** uses a DiT backbone for video
- **FLUX** uses DiT for image generation
- **Stable Diffusion 3** uses MMDiT
- **DALL-E 3** uses a transformer-based diffusion architecture
- **Playground v3** uses DiT

The shift from U-Net to DiT is as significant as the shift from RNNs to Transformers
in NLP.

---

## 3D Generation

### The Challenge

3D generation is harder than 2D because:
- 3D data is scarce compared to 2D images
- 3D representations (meshes, point clouds, NeRFs) are diverse and complex
- Multi-view consistency is a strict geometric constraint
- Rendering is computationally expensive

### Score Distillation Sampling (SDS) — DreamFusion

**DreamFusion** (Poole et al., 2022) pioneered text-to-3D without 3D training data using
**Score Distillation Sampling (SDS)**.

The idea: use a pre-trained 2D diffusion model as a critic for 3D content.

1. Represent the 3D scene as a **NeRF** (Neural Radiance Field) with parameters φ
2. Render the NeRF from a random camera angle to get image x = render(φ, camera)
3. Add noise to get xₜ
4. Compute the diffusion model's predicted noise εθ(xₜ, t, text)
5. The SDS gradient pushes the NeRF rendering to look like a plausible image:

```
∇φ L_SDS = E_{t, ε, camera} [ w(t) · (εθ(xₜ, t, text) - ε) · ∂x/∂φ ]
```

**Intuition**: At each training step, we ask "does this 3D scene, rendered from this angle,
look like something the diffusion model would generate for this text prompt?" If not,
update the 3D scene accordingly.

**Limitations of SDS**:
- The Janus problem (multi-faced objects)
- Over-saturation and lack of diversity
- Slow optimization (per-object, not amortized)

### Multi-View Diffusion: Zero123 and Beyond

**Zero123** (Liu et al., 2023) takes a different approach: train a diffusion model to
directly generate novel views of an object given a single input image.

The model learns:
```
p(x_new_view | x_input, ΔR, Δt)
```

where ΔR is the relative rotation and Δt is the relative translation between views.

**Zero123++** improved this by generating **6 consistent views simultaneously** in a
tiled layout, dramatically improving 3D consistency.

**Pipeline**: Single image → Zero123++ (6 views) → 3D reconstruction (NeRF or mesh)

### Gaussian Splatting + Diffusion

**3D Gaussian Splatting** (Kerbl et al., 2023) provides a much faster 3D representation
than NeRFs. Recent work combines it with diffusion:

- **DreamGaussian**: SDS optimization with Gaussian Splatting (10× faster than NeRF-based)
- **LGM (Large Gaussian Model)**: Directly predict 3D Gaussians from images using a
  feed-forward transformer
- **GaussianDreamer**: Text-to-3D using Gaussian Splatting with guided diffusion

### Point Cloud and Mesh Generation

**Point-E** (OpenAI, 2022):
- Text → image (using DALL-E) → point cloud (using a point cloud diffusion model)
- Fast (~1 minute) but lower quality than optimization-based methods

**Shap-E** (OpenAI, 2023):
- Text → implicit 3D representation (NeRF + mesh simultaneously)
- Uses a diffusion model over the parameters of an implicit function

**MeshGPT** (2023):
- Treats mesh generation as a sequence prediction problem
- Uses VQ-VAE to tokenize mesh faces, then autoregressive transformer to generate sequences

---

## Autoregressive Image Models

### The Resurgence: Can Autoregressive Models Beat Diffusion?

While diffusion dominated image generation from 2020-2024, autoregressive approaches
made a strong comeback.

### Visual Autoregressive Modeling (VAR)

**VAR** (Tian et al., 2024) introduced **next-scale prediction** as an alternative to the
traditional next-token (raster-scan) prediction used in prior autoregressive image models.

#### The Problem with Next-Token Prediction for Images

Standard autoregressive image generation (à la PixelCNN, DALL-E) generates tokens in
raster order: left-to-right, top-to-bottom. This has issues:

1. **Unnatural ordering**: Images don't have a natural "reading order" like text
2. **Long sequences**: A 256×256 image with 16×16 patches = 256 tokens, but higher
   resolutions quickly become intractable
3. **Slow generation**: Each token requires a forward pass

#### Next-Scale Prediction: The VAR Insight

VAR proposes generating images **coarse-to-fine** across multiple resolution scales:

```
Scale 1: 1×1 token map   (global structure)
Scale 2: 2×2 token map   (coarse layout)
Scale 3: 4×4 token map   (regions)
Scale 4: 8×8 token map   (objects)
...
Scale K: H×W token map   (fine details)
```

At each scale, the model generates **all tokens in parallel** (not sequentially), conditioned
on all previous scales. This is a fundamentally different factorization:

**Next-token** (PixelCNN):
```
p(image) = ∏ᵢ p(tokenᵢ | token₁, ..., tokenᵢ₋₁)
```

**Next-scale** (VAR):
```
p(image) = ∏ₖ p(scaleₖ | scale₁, ..., scaleₖ₋₁)
```

#### Architecture

VAR uses:
1. **Multi-scale VQVAE**: An image tokenizer that produces discrete token maps at
   multiple resolutions simultaneously
2. **Autoregressive Transformer**: Takes token maps from scales 1..k-1 and predicts
   the token map at scale k
3. **Parallel decoding within each scale**: All tokens at scale k are generated
   simultaneously (like masked prediction)

#### Results

VAR achieves:
- **FID 1.73** on ImageNet 256×256 (competitive with best diffusion models)
- **20× faster** inference than comparable diffusion models
- **Clear scaling laws**: larger models = better quality, following power-law curves

#### Why This Matters

VAR demonstrates that the autoregressive paradigm—which powers all of language AI—can be
adapted to match diffusion for visual generation. The next-scale factorization is more
natural than raster-scan for images, and parallel decoding within scales eliminates the
speed disadvantage.

### Other Autoregressive Approaches

**MAGVIT-v2** (Yu et al., 2023):
- Lookup-free quantization for image tokenization
- Used in VideoPoet and other Google models

**LlamaGen** (Sun et al., 2024):
- Pure autoregressive transformer (vanilla Llama architecture) for image generation
- Competitive with diffusion using next-token prediction on image tokens
- Shows that large language model architectures transfer to image generation

**Chameleon** (Meta, 2024):
- Unified autoregressive model for interleaved text and images
- Single model handles both modalities with shared vocabulary

---

## The Unified Picture: How It All Connects

These breakthroughs aren't isolated—they form an interconnected web:

```
                    Diffusion Models (DDPM)
                         │
                ┌────────┼────────┐
                ▼        ▼        ▼
            DDIM    Score-SDE   Score Matching
           (ODE)    (SDE)       (Training)
                │        │
                ▼        ▼
            Probability Flow ODE
                │
        ┌───────┼───────┐
        ▼       ▼       ▼
  Flow Matching  Rectified   Consistency
  (Lipman '22)   Flow        Models
        │       (Liu '22)    (Song '23)
        │           │             │
        ▼           ▼             ▼
    Conditional  Reflow →    One-step
    FM + OT      Straighter  Generation
        │        paths
        │           │
        ▼           ▼
   SD3/FLUX    InstaFlow
        │
        ▼
  MMDiT / DiT ←── Transformers replace U-Net
        │
        ▼
  Sora / Video DiT
```

**Key insight**: The field is converging toward:
1. **Transformer architectures** (DiT) as the universal backbone
2. **Flow matching** as the training paradigm (subsuming diffusion)
3. **Rectified flow / consistency** for fast inference
4. **Scaling laws** that predict quality from compute

---

## Key Mathematical Concepts Summarized

### Flow Matching vs. Diffusion: A Side-by-Side

| Aspect              | Diffusion (DDPM)                       | Flow Matching                          |
|---------------------|----------------------------------------|----------------------------------------|
| Forward process     | Gradual Gaussian noising               | Linear interpolation                    |
| Reverse process     | Iterative denoising (SDE/ODE)          | ODE integration                        |
| Training target     | Noise ε or score ∇ log p              | Velocity v = x₁ - x₀                  |
| Path shape          | Curved (from noise schedule)           | Straight (optimal transport)           |
| Training loss       | ‖ε - εθ(xₜ, t)‖²                     | ‖vθ(xₜ, t) - (x₁ - x₀)‖²           |
| Steps needed (typ.) | 20-100 (DDIM)                          | 10-50                                  |
| Noise schedule      | Required, sensitive hyperparameter     | Not needed (implicit in interpolation) |
| Theoretical basis   | Score matching, SDE theory             | Optimal transport, continuity eq.      |

### The Speed Hierarchy

```
Method                    Steps    Quality (FID)    Speed
─────────────────────────────────────────────────────────
DDPM                      1000     ~3.0             1×
DDIM                      50       ~4.0             20×
Flow Matching             20       ~3.5             50×
Rectified Flow (1-reflow) 10       ~4.0             100×
Consistency Distillation  2        ~3.5             500×
Consistency Model         1        ~5.0             1000×
```

*(Approximate FID values on ImageNet 256×256; actual numbers vary by model size and configuration)*

---

## Key Papers & Sources

### Foundational Diffusion
1. **DDPM** — "Denoising Diffusion Probabilistic Models" (Ho, Jain, Abbeel, 2020)
   https://arxiv.org/abs/2006.11239
2. **DDIM** — "Denoising Diffusion Implicit Models" (Song, Meng, Ermon, 2020)
   https://arxiv.org/abs/2010.02502
3. **Score-Based SDE** — "Score-Based Generative Modeling through SDEs" (Song et al., 2021)
   https://arxiv.org/abs/2011.13456
4. **Classifier-Free Guidance** — (Ho & Salimans, 2022)
   https://arxiv.org/abs/2207.12598
5. **Diffusion Models Beat GANs** — (Dhariwal & Nichol, 2021)
   https://arxiv.org/abs/2105.05233

### Flow Matching
6. **Flow Matching for Generative Modeling** — (Lipman, Chen, Ben-Hamu, et al., 2022)
   https://arxiv.org/abs/2210.02747
7. **Flow Straight and Fast** — (Liu, Gong, Liu, 2022)
   https://arxiv.org/abs/2209.03003
8. **Conditional Flow Matching** — (Tong et al., 2023)
   https://arxiv.org/abs/2302.00482
9. **Stable Diffusion 3** — "Scaling Rectified Flow Transformers" (Esser et al., 2024)
   https://arxiv.org/abs/2403.03206

### Consistency Models
10. **Consistency Models** — (Song, Dhariwal, Chen, Sutskever, 2023)
    https://arxiv.org/abs/2303.01469
11. **Improved Consistency Training** — (Song & Dhariwal, 2023)
    https://arxiv.org/abs/2310.14189

### Rectified Flow
12. **Rectified Flow** — (Liu, Gong, Liu, 2022)
    https://arxiv.org/abs/2209.03003
13. **InstaFlow** — "One Step is Enough" (Liu et al., 2023)
    https://arxiv.org/abs/2309.06380

### Diffusion Transformers
14. **DiT** — "Scalable Diffusion Models with Transformers" (Peebles & Xie, 2023)
    https://arxiv.org/abs/2212.09748
15. **U-ViT** — "All are Worth Words" (Bao et al., 2023)
    https://arxiv.org/abs/2209.12152

### Video Generation
16. **Sora** — "Video Generation Models as World Simulators" (OpenAI, 2024)
    https://openai.com/index/video-generation-models-as-world-simulators/
17. **Video Diffusion Models** — (Ho et al., 2022)
    https://arxiv.org/abs/2204.03458
18. **Imagen Video** — (Ho et al., 2022)
    https://arxiv.org/abs/2210.02303
19. **Stable Video Diffusion** — (Blattmann et al., 2023)
    https://arxiv.org/abs/2311.15127

### 3D Generation
20. **DreamFusion** — (Poole et al., 2022)
    https://arxiv.org/abs/2209.14988
21. **Zero123** — "Zero-shot One Image to 3D" (Liu et al., 2023)
    https://arxiv.org/abs/2303.11328
22. **Point-E** — (Nichol et al., 2022)
    https://arxiv.org/abs/2212.08751
23. **3D Gaussian Splatting** — (Kerbl et al., 2023)
    https://arxiv.org/abs/2308.14737

### Autoregressive Image Models
24. **VAR** — "Visual Autoregressive Modeling" (Tian et al., 2024)
    https://arxiv.org/abs/2404.02905
25. **LlamaGen** — "Autoregressive Model Beats Diffusion" (Sun et al., 2024)
    https://arxiv.org/abs/2406.06525
26. **MAGVIT-v2** — (Yu et al., 2023)
    https://arxiv.org/abs/2310.05737

### Blog Posts & Tutorials
27. Lilian Weng — "What are Diffusion Models?"
    https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
28. Yang Song — "Generative Modeling by Estimating Gradients of the Data Distribution"
    https://yang-song.net/blog/2021/score/
29. Sander Dieleman — "Perspectives on Diffusion"
    https://sander.ai/2024/09/02/diffusion.html
30. Emilio Dorigatti — "Flow Matching Explained"
    https://e-dorigatti.github.io/math/2023/09/01/flow-matching.html

---

## Concepts for Knowledge Tree

1. **Diffusion Forward Process** — Adding Gaussian noise incrementally to destroy data structure
2. **Diffusion Reverse Process** — Learning to denoise step-by-step to generate data
3. **Score Function** — Gradient of the log probability density ∇ₓ log p(x)
4. **Score Matching** — Training to estimate the score function without knowing the normalizing constant
5. **Denoising Score Matching** — Score matching via noised data with known conditional score
6. **DDPM** — Denoising Diffusion Probabilistic Models; the foundational framework
7. **DDIM** — Non-Markovian deterministic sampler enabling fewer steps
8. **Probability Flow ODE** — Deterministic ODE whose marginals match the diffusion SDE
9. **Noise Schedule** — The variance schedule βₜ controlling noise addition rate
10. **Classifier-Free Guidance** — Amplifying conditional signal by interpolating between conditional and unconditional predictions
11. **Guidance Scale** — Hyperparameter controlling strength of classifier-free guidance
12. **Continuous Normalizing Flow** — ODE-based generative model mapping noise to data
13. **Flow Matching** — Simulation-free training of continuous normalizing flows
14. **Conditional Flow Matching** — Flow matching with conditioning on context
15. **Velocity Field** — The vector field v(x,t) governing the flow ODE dx/dt = v(x,t)
16. **Optimal Transport** — Finding the minimum-cost mapping between distributions
17. **Linear Interpolation Path** — The straight-line path xₜ = (1-t)x₀ + tx₁
18. **Continuity Equation** — PDE relating density evolution to the velocity field
19. **Consistency Models** — Models that map any noise level to the same clean output
20. **Self-Consistency Property** — f(xₜ, t) = f(xₜ', t') for points on the same trajectory
21. **Consistency Distillation** — Training consistency models from a pre-trained diffusion model
22. **Consistency Training** — Training consistency models from scratch without diffusion teacher
23. **Rectified Flow** — Flow matching with iterative path straightening (reflow)
24. **Reflow Procedure** — Iteratively straightening flow paths by regenerating couplings
25. **Path Crossing** — Intersecting trajectories that force the velocity field to average
26. **Diffusion Transformer (DiT)** — Replacing U-Net with a Transformer backbone in diffusion
27. **AdaLN-Zero** — Adaptive LayerNorm with zero-initialized gating for conditioning
28. **MMDiT** — Multimodal DiT with separate streams for text and image tokens
29. **Spacetime Patches** — 3D patches from video (time × height × width) used as tokens
30. **Temporal Attention** — Self-attention across the time dimension for video coherence
31. **Video Diffusion** — Extending diffusion models to generate temporally coherent video
32. **Score Distillation Sampling (SDS)** — Using 2D diffusion scores to optimize 3D representations
33. **Multi-View Diffusion** — Generating multiple consistent views for 3D reconstruction
34. **Neural Radiance Fields (NeRF)** — Implicit 3D representation for novel view synthesis
35. **3D Gaussian Splatting** — Explicit 3D representation using Gaussian primitives
36. **Visual Autoregressive Modeling (VAR)** — Next-scale prediction for image generation
37. **Next-Scale Prediction** — Generating images coarse-to-fine across resolution scales
38. **Logit-Normal Timestep Sampling** — Non-uniform timestep sampling emphasizing difficult steps
39. **EMA Target Network** — Exponential moving average of parameters for stable training targets
40. **Latent Diffusion** — Running diffusion in compressed VAE latent space rather than pixel space
