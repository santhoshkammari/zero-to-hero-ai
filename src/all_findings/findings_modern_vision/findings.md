# Modern Vision — Research Findings

## Vision Transformer (ViT) — "An Image is Worth 16x16 Words" (Dosovitskiy et al., 2020)
- Core insight: treat an image as a sequence of patches, apply standard transformer encoder
- Patch embedding: split image into non-overlapping patches (e.g., 16×16), flatten each, linear projection → embedding
- 224×224 image with 16×16 patches → 196 tokens (14×14 grid)
- Learned positional embeddings added (not sinusoidal — learned works better for images)
- Prepend a learnable [CLS] token — aggregates global info via self-attention, used for classification
- Standard transformer encoder: multi-head self-attention + MLP + LayerNorm + residual connections
- Key limitation: quadratic attention complexity O(N²) where N = number of patches — limits resolution
- ViT needs massive data (JFT-300M, ImageNet-21k) to beat CNNs. On ImageNet-1k alone, CNNs win
- Why: ViT has minimal inductive bias — no locality, no translation equivariance baked in. Must learn everything from data
- This is both weakness (data hungry) and strength (no assumptions limit what it can learn)

## DeiT — Data-efficient Image Transformer (Touvron et al., 2021)
- Showed ViT can be trained effectively on ImageNet-1k alone using knowledge distillation
- Introduces distillation token alongside [CLS] token — learns from a CNN teacher (RegNet)
- Dual loss: cross-entropy with true labels + KL divergence with teacher soft labels
- Key message: strong data augmentation + knowledge distillation bridges the data gap
- Made ViT practical for teams without JFT-300M access

## Swin Transformer (Liu et al., 2021)
- Hierarchical vision transformer with shifted window attention
- Solves ViT's two big problems: (1) quadratic complexity (2) no multi-scale features
- Window attention: compute self-attention within local windows (e.g., 7×7) — linear complexity
- Shifted windows: alternate between regular and shifted window partitions — enables cross-window information flow
- Patch merging between stages: reduces spatial resolution, increases channels (like CNN pooling)
- 4 stages: 56×56 → 28×28 → 14×14 → 7×7 (for 224×224 input with 4×4 initial patches)
- Produces multi-scale feature maps — compatible with FPN, works for detection/segmentation
- Became the go-to backbone for dense prediction tasks
- Swin v2: improved training stability, scaled to 3B parameters, 1536×1536 resolution

## CLIP — Contrastive Language-Image Pre-training (Radford et al., 2021)
- Two encoders: image (ViT or ResNet) + text (Transformer)
- Trained on 400M image-text pairs from internet (WIT dataset)
- Contrastive loss: batch of N pairs → N×N similarity matrix → maximize diagonal (matching pairs)
- Symmetric cross-entropy loss on rows and columns
- Zero-shot classification: encode class descriptions as text, encode image, cosine similarity → prediction
- Zero-shot ImageNet accuracy competitive with supervised ResNet-50
- Prompt engineering matters: "a photo of a {class}" >> "{class}" alone
- CLIP is foundational: text encoder powers Stable Diffusion, image encoder backs multimodal LLMs
- SigLIP (Google): replaces softmax loss with sigmoid — scales better, no need for full N×N matrix
- EVA-CLIP: stronger ViT backbones, state-of-art zero-shot performance

## DINOv2 (Oquab et al., 2023)
- Self-supervised vision foundation model from Meta — no labels, no text, images only
- Self-distillation: teacher-student setup, teacher = EMA of student weights
- Student sees augmented/cropped views, must match teacher's representations
- Combines self-distillation (DINO) with masked image modeling ideas
- Produces rich features: classification, segmentation, depth estimation, retrieval — all with frozen backbone + linear head
- Best spatial features available — especially for dense prediction tasks
- Trained on curated 142M image dataset (LVD-142M)
- Available in ViT-S/B/L/g variants

## Hybrid Architectures
- CoAtNet: CNN early stages (local features) → Transformer later stages (global context)
- ConvNeXt (Liu et al., 2022): pure CNN modernized with transformer design choices — large kernels (7×7), LayerNorm, inverted bottlenecks, GELU. Matches Swin performance
- Key insight: the gap between CNNs and transformers was largely about training recipes and design details, not fundamentally about attention vs convolution
- EfficientViT: lightweight hybrid for mobile/edge deployment

## SAM — Segment Anything Model (Kirillov et al., 2023)
- Foundation model for segmentation — promptable (points, boxes, masks)
- Architecture: ViT image encoder (frozen) + prompt encoder + lightweight mask decoder
- Image encoder runs once, prompt decoder is fast → interactive segmentation
- Trained on SA-1B dataset: 11M images, 1.1B masks
- Zero-shot segmentation across domains

## Key Themes for Interview Depth
- ViT's lack of inductive bias: weakness (data hungry) and strength (no ceiling)
- Attention complexity: quadratic (ViT) vs linear (Swin's windowed attention)
- Foundation model paradigm: pre-train once broadly, adapt cheaply for specific tasks
- CLIP unlocked zero-shot vision and became the bridge between vision and language
- Self-supervised (DINOv2) vs contrastive vision-language (CLIP): different strengths, complementary
- The "CNN vs Transformer" debate resolved: it's about scale, data, and training recipe more than architecture
