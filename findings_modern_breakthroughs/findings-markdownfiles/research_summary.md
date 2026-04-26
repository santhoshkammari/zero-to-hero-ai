# Modern Breakthroughs in Generative AI - Research Summary

## Text-to-Image Evolution
- DALL-E 3: LLM-in-the-loop for prompt understanding, UnCLIP mechanism, cascade generation
- Midjourney v6: Proprietary, focused on aesthetic quality, closed source
- Stable Diffusion: 1.5 (U-Net) → SDXL (larger U-Net) → SD3 (MMDiT, flow matching) → FLUX (Black Forest Labs, flow matching + DiT)
- Key shift: U-Net → Diffusion Transformer (DiT) backbone

## Image Editing
- Inpainting: Keep unmasked pixels fixed during denoising, only denoise masked region
- Outpainting: Place image on larger canvas, mask new areas, use inpainting process
- Img2img: Encode source image → add noise (strength param) → denoise with new prompt
- ControlNet: Clone encoder, inject control signals via zero convolutions
- IP-Adapter: Image prompting via decoupled cross-attention

## Video Generation
- Sora: Spacetime DiT, processes video as 3D spacetime patches, variable length/resolution
- Runway Gen-3/4: Best cinematic quality, 10-16 sec clips, camera control
- Kling: Longest clips (1-2 min), best temporal coherence
- Pika: Quick creative effects, short clips, accessible
- Stable Video Diffusion: Open model, temporal attention layers

## 3D Generation
- NeRF: Neural Radiance Fields, slow rendering (seconds/frame), high quality
- 3D Gaussian Splatting: Real-time rendering (60+ fps), explicit representation, nearly matching NeRF quality
- Score Distillation Sampling (DreamFusion): Use 2D diffusion model as critic for 3D optimization
- Zero-1-to-3: Fine-tune diffusion for novel view synthesis from single image
- Point-E, Shap-E: Direct 3D generation models

## Audio/Music Generation
- Neural audio codecs (EnCodec, SoundStream): Compress audio to discrete tokens
- AudioLM (Google): Predict audio token sequences with transformer
- MusicGen (Meta): Text-conditioned transformer over EnCodec tokens
- Bark: Text-to-speech with prosody, multilingual
- Pipeline: Raw audio → codec → tokens → transformer prediction → decode back to audio

## Ethical Implications
- Deepfakes and misinformation
- Copyright gray areas (training data, ownership of outputs)
- Creative industry disruption
- Detection vs generation arms race
- Regulatory frameworks (EU AI Act)
