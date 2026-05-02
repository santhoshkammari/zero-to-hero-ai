# Missing Topics: Ch15 Generative Models

Now I have a comprehensive understanding of what's in the chapter and what's missing. Let me compile the findings into a thorough analysis.

Here is my complete analysis of what's covered and what's missing from Chapter 14 (Generative Models):

---

## Summary

The chapter is **remarkably comprehensive** for its core sections — diffusion models are covered with excellent mathematical depth (DDPM, DDIM, classifier-free guidance, latent diffusion, ControlNet, consistency models, flow matching), classic generative models cover VAEs, GANs, normalizing flows (RealNVP, Glow, coupling layers), and energy-based models well, and the "Nice to Know" section adds score matching, PixelCNN→VQGAN, neural ODEs, discrete diffusion, and Poisson flows. However, there are **significant gaps** in GAN architecture variants, personalization/fine-tuning of diffusion models, scientific applications of generative models, audio/speech depth (WaveNet is missing), voice cloning details, and several interview-critical topics.

---

## Current Chapter Coverage (Verified)

**Section 1: Classic Generative Models** (`chapters/ch14/classic-generative-models.html`)
- Autoencoders (vanilla, denoising, sparse) → VAEs (reparameterization trick, ELBO)
- GANs (minimax objective, training loop, non-saturating loss)
- Mode collapse + WGAN/Wasserstein distance/WGAN-GP (gradient penalty mentioned `:499-503`)
- Conditional GANs + CVAEs (Pix2Pix, CycleGAN mentioned in one paragraph `:522`)
- Normalizing flows (coupling layers, RealNVP, Glow, invertible 1×1 convolutions) `:527-555`
- Energy-based models (score function, Langevin dynamics, partition function) `:558-586`
- Comparison table of model families `:589+`

**Section 2: Diffusion Models** (`chapters/ch14/diffusion-models.html`)
- Forward process, noise schedule, closed-form shortcut `:317-378`
- Reverse process, noise prediction vs score prediction `:381-434`
- Training loop (5-line PyTorch) `:435-478`
- DDPM sampling, DDIM `:479-528`
- Classifier-free guidance `:529-551`
- Latent diffusion / Stable Diffusion architecture `:552-596`
- ControlNet `:597-610`
- Consistency models `:611-624`
- Flow matching / rectified flows `:625+`

**Section 3: Modern Breakthroughs** (`chapters/ch14/modern-breakthroughs.html`)
- Text-to-image: DALL·E 1→2→3, Midjourney, SD 1.5→SDXL→SD3→FLUX, MMDiT `:313-335`
- Image editing: inpainting, outpainting, img2img `:345-370`
- ControlNet (spatial control) `:373-381`
- Video generation: temporal attention, spacetime patches, Sora, Runway, Kling `:391-421`
- 3D: NeRF, Gaussian Splatting, DreamFusion/SDS, Zero-1-to-3, Point-E/Shap-E `:428-466`
- Audio: neural codecs (EnCodec/SoundStream), AudioLM, MusicGen, Bark, Stable Audio `:472-504`
- Multimodal generation `:510-518`
- Ethics: copyright, deepfakes, creative disruption `:524-544`

**Section 4: Evaluating Generative Models** (`chapters/ch14/evaluating-generative-models.html`)
- FID, IS, CLIP Score, LPIPS, Precision/Recall, likelihood trap, mode collapse detection
- Diversity-quality tradeoff, truncation trick, human evaluation (MOS, 2AFC, Elo)
- Goodhart's Law

**Section 5: Nice to Know** (`chapters/ch14/nice-to-know.html`)
- Neural style transfer, deepfakes+detection, adversarial examples for generative models
- Score matching + Langevin dynamics (deeper), Poisson Flow, Neural ODEs/CNFs
- Discrete diffusion for text, Autoregressive image models (PixelCNN→VQ-VAE→VQGAN)
- Creative AI tools ecosystem

---

## MISSING TOPICS — Detailed Gap Analysis

### 🔴 HIGH PRIORITY (Commonly asked in interviews, core knowledge gaps)

#### 1. **GAN Architecture Variants (StyleGAN, DCGAN, Progressive GAN)**
**Currently**: StyleGAN mentioned only twice in passing (deepfakes context, truncation trick). DCGAN not mentioned at all. Progressive GAN not mentioned.
**What's missing**:
- **DCGAN** (Radford et al., 2016): The first stable convolutional GAN architecture — batch norm, strided convolutions replacing pooling, architectural guidelines. This is foundational and commonly asked in interviews.
- **Progressive GAN / ProGAN** (Karras et al., 2018): Growing resolution during training (4×4 → 8×8 → ... → 1024×1024). Key innovation: progressive training stabilizes high-res generation.
- **StyleGAN / StyleGAN2 / StyleGAN3** architecture: Mapping network (z→w), AdaIN-based style injection, style mixing, progressive growing, perceptual path length regularization. StyleGAN's latent space (W space vs Z space) is a **top interview question**.
- **Self-Attention GAN (SAGAN)**: Spectral normalization + self-attention layers in GAN discriminator/generator.
- **BigGAN**: Class-conditional generation at scale, truncation trick origin.
- **Source**: Stanford CS236 dedicates full lectures to GAN variants (weeks 5-6). Interview question lists consistently include "Explain StyleGAN architecture" and "What is the mapping network in StyleGAN?"

#### 2. **Diffusion Model Personalization & Fine-Tuning (DreamBooth, Textual Inversion, LoRA for Diffusion)**
**Currently**: LoRA mentioned once in passing in the tools ecosystem paragraph. DreamBooth and Textual Inversion not mentioned at all.
**What's missing**:
- **Textual Inversion** (Gal et al., 2022): Learning new "words" (embeddings) for the text encoder to represent a concept from 3-5 images.
- **DreamBooth** (Ruiz et al., 2023): Fine-tuning the entire diffusion model on a few images with a unique identifier token + prior preservation loss.
- **LoRA for Diffusion Models**: Low-rank adaptation applied to U-Net/DiT cross-attention layers — the dominant community method for model customization.
- **IP-Adapter** (Ye et al., 2023): Image prompt adapter that uses a decoupled cross-attention mechanism for image-conditioned generation without fine-tuning.
- This is **critical practical knowledge** — the entire open-source SD ecosystem (Civitai, ComfyUI) revolves around these techniques.

#### 3. **Classifier Guidance (vs. Classifier-Free Guidance)**
**Currently**: Classifier-free guidance is well-covered. But **classifier guidance** (Dhariwal & Nichol, 2021) — the predecessor that requires training a separate classifier on noisy images — is not explained, making the "why classifier-free?" motivation incomplete.
**What's missing**:
- Classifier guidance: using gradients from a classifier p(y|x_t) to steer the denoising process
- Why it was replaced: requires training an extra classifier, doesn't work with text conditioning easily
- This is a common interview question: "What's the difference between classifier guidance and classifier-free guidance?"

#### 4. **WaveNet and Foundational Audio Generation**
**Currently**: Audio section jumps straight to neural codecs (EnCodec/SoundStream). WaveNet not mentioned at all.
**What's missing**:
- **WaveNet** (van den Oord et al., 2016): Autoregressive model for raw audio waveforms — dilated causal convolutions, sample-by-sample generation. Revolutionary for TTS quality. The "PixelCNN for audio."
- **Tacotron / Tacotron 2**: Text-to-spectrogram + WaveNet vocoder pipeline — the classic TTS architecture.
- **HiFi-GAN**: GAN-based neural vocoder that replaced WaveNet for real-time synthesis.
- These are foundational and the chapter covers PixelCNN for images but misses the audio analog entirely.

#### 5. **Voice Cloning & Modern TTS**
**Currently**: ElevenLabs mentioned once in the tools ecosystem. No technical depth on voice cloning or TTS.
**What's missing**:
- **Zero-shot voice cloning**: Systems like VALL-E (Microsoft), Tortoise TTS, XTTS that clone voices from seconds of audio
- **VALL-E**: Treats TTS as a language modeling problem over neural codec tokens — same framework as AudioLM but for speech synthesis
- **Speaker embedding**: How voice identity is captured and conditioned on
- Voice cloning raises major ethical issues and is a **hot interview topic**

#### 6. **Generative AI for Science (Drug Discovery, Protein Design, Materials)**
**Currently**: Zero coverage. No mention of drug discovery, protein design, molecular generation, or materials science.
**What's missing**:
- **Molecular generation**: Using VAEs, GANs, and diffusion models to generate novel drug candidates (SMILES strings, molecular graphs)
- **Protein structure generation**: RFdiffusion (Baker lab), FrameDiff — diffusion models for protein backbone generation
- **AlphaFold connection**: While not generative per se, the generative extensions (AlphaFold-based design) are important context
- **Materials science**: Crystal structure generation, property-conditioned material design
- Berkeley CS294-158 has a dedicated guest lecture on "AI for Science" (L13a). This is one of the most impactful real-world application areas.

#### 7. **GAN Training Tricks & Stabilization Techniques**
**Currently**: WGAN/gradient penalty mentioned. Label smoothing and multi-step D training briefly mentioned (`:486`). But no systematic coverage.
**What's missing**:
- **Spectral normalization** (Miyato et al., 2018): Constraining Lipschitz constant of D by normalizing weight matrices by their spectral norm — now standard.
- **Two-timescale update rule (TTUR)**: Different learning rates for G and D.
- **Feature matching loss**: Training G to match statistics of intermediate D layers.
- **Minibatch discrimination**: Detecting mode collapse by examining diversity across batch.
- **R1 regularization**: Gradient penalty on real data only (used in StyleGAN2).
- **Exponential moving average (EMA) of generator weights**: Stabilizes output quality.
- These are consistently asked in ML interviews: "What techniques stabilize GAN training?"

### 🟡 MEDIUM PRIORITY (Important for completeness, sometimes asked)

#### 8. **Restricted Boltzmann Machines (RBMs) & Deep Belief Networks**
**Currently**: Boltzmann machines mentioned once in a parenthetical (`:classic-generative-models.html`).
**What's missing**: RBMs as the historical predecessor to modern generative models — contrastive divergence training, Gibbs sampling, and how deep belief networks (Hinton, 2006) kicked off the deep learning revolution. Stanford CS236 covers this historical context.

#### 9. **Super-Resolution Models**
**Currently**: "upscal" appears once in evaluation context. No dedicated coverage.
**What's missing**:
- **SRGAN** / **ESRGAN**: GAN-based super-resolution
- **Diffusion-based super-resolution**: Used in DALL·E 2's cascaded pipeline, Imagen's cascaded approach
- Cascaded generation (generate at low-res, upscale) as an architectural pattern

#### 10. **Imagen Architecture**
**Currently**: Imagen mentioned once in the diffusion intro (`:305`). No architectural detail.
**What's missing**:
- Imagen's architecture: T5-XXL text encoder + cascaded diffusion (64×64 → 256×256 → 1024×1024)
- Key finding that scaling the language model (T5) mattered more than scaling the image model
- Comparison with DALL·E 2's CLIP-based approach

#### 11. **Noise Schedule Design**
**Currently**: Linear schedule from DDPM mentioned. No discussion of alternatives.
**What's missing**:
- **Cosine schedule** (Nichol & Dhariwal, 2021): Improved sample quality by avoiding too-rapid noise at early steps
- **Learned schedules**: Models that learn optimal noise schedules
- **v-prediction** parameterization as alternative to ε-prediction
- These schedule choices significantly affect generation quality and are interview-relevant

#### 12. **Distillation & Acceleration Methods (Beyond Consistency Models)**
**Currently**: Consistency models covered. DDIM covered as faster sampling.
**What's missing**:
- **Progressive distillation** (Salimans & Ho, 2022): Halving sampling steps iteratively by training student to match 2 teacher steps in 1
- **Latent consistency models (LCM)**: Consistency distillation in latent space — enables 4-step generation
- **Adversarial diffusion distillation**: SDXL Turbo approach
- **Rectified flow distillation**: InstaFlow
- These are cutting-edge and increasingly important for deployment

#### 13. **Compositional & Controlled Generation**
**Currently**: Classifier-free guidance and ControlNet covered. But compositional generation is missing.
**What's missing**:
- **Composable Diffusion Models**: Combining multiple conditions via score composition
- **Attend-and-Excite**: Attention manipulation for better prompt following
- **Layout-to-image generation**: GLIGEN, spatial conditioning beyond ControlNet
- **Negative prompting**: How it works mathematically (CFG with negative conditioning)

#### 14. **Generative Model Taxonomy — Unified Mathematical Framework**
**Currently**: Each model family explained separately with a comparison table.
**What's missing**: The unified view from Song et al. (2021) — the SDE/ODE framework that shows diffusion, score matching, and flow matching as special cases of the same framework. The chapter's Nice to Know section touches this but doesn't provide the full unifying picture:
- Forward SDE → reverse SDE → probability flow ODE
- How different choices of SDE coefficients give DDPM vs SMLD vs others
- This is the "big picture" that Stanford CS236 and Berkeley CS294-158 both emphasize

#### 15. **Watermarking & Content Provenance (Technical Details)**
**Currently**: C2PA mentioned once (`:538`), watermarking mentioned vaguely.
**What's missing**:
- **Invisible watermarking techniques**: Stable Signature, Tree-Ring watermarks for diffusion models
- **How watermarks survive image transformations**: Robustness to crops, compression, screenshots
- **Detection APIs**: Google SynthID, Content Credentials
- Technical details of embedding watermarks in the diffusion process itself

### 🟢 LOWER PRIORITY (Nice to have, advanced topics)

#### 16. **Mixture of Experts in Generative Models**
**What's missing**: How MoE architectures are being used in large-scale DiT models for efficiency

#### 17. **Discrete Tokenization for Images (More Depth on VQ-VAE-2, MAGVIT, LlamaGen)**
**Currently**: VQ-VAE → VQGAN covered in Nice to Know.
**What's missing**: 
- **MAGVIT-2**: State-of-art visual tokenizer enabling autoregressive image generation competitive with diffusion
- **LlamaGen**: Pure autoregressive (next-token) image generation matching diffusion quality
- The **resurgence of autoregressive models** for image generation in 2024

#### 18. **Diffusion Transformers (DiT) Architecture Details**
**Currently**: MMDiT mentioned for SD3. Sora's spacetime DiT mentioned.
**What's missing**: The original DiT paper (Peebles & Xie, 2023) — replacing U-Net with transformer, AdaLN-Zero conditioning, scalability analysis. This is now the dominant architecture.

#### 19. **Adversarial Training Formulations (f-GAN, Least Squares GAN)**
**What's missing**:
- **f-GAN**: Generalizing GANs to arbitrary f-divergences
- **LSGAN**: Least-squares loss instead of log loss for more stable training
- **Hinge loss GAN**: Used in SAGAN, BigGAN

#### 20. **Generative Models for Data Augmentation**
**What's missing**: Using generative models (GANs, diffusion) to augment training data for classifiers — a common practical application and interview question.

---

## Interview Questions Analysis

Based on the `awesome-generative-ai-guide` 60-question interview list and other sources, the chapter **covers well**:
- ✅ GAN vs discriminative models
- ✅ GAN architecture + training
- ✅ VAE architecture + latent variables  
- ✅ Mode collapse + mitigation
- ✅ Conditional generation
- ✅ ELBO / reparameterization trick
- ✅ Diffusion forward/reverse process
- ✅ FID, IS, evaluation metrics
- ✅ WGAN / Wasserstein distance

But **commonly asked topics NOT adequately covered**:
- ❌ StyleGAN architecture (mapping network, W-space, style mixing)
- ❌ DCGAN architectural guidelines
- ❌ Classifier guidance vs classifier-free guidance comparison
- ❌ GAN training stabilization techniques (spectral norm, feature matching)
- ❌ DreamBooth / LoRA / Textual Inversion for personalization
- ❌ Super-resolution with generative models
- ❌ Generative models for data augmentation
- ❌ Imagen architecture details
- ❌ WaveNet / foundational audio models
- ❌ Voice cloning technical approach
- ❌ Scientific applications (drug discovery, protein design)
- ❌ Noise schedule variants (cosine, learned)
- ❌ Progressive distillation / acceleration methods
- ❌ RBMs / historical context
