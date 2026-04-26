# Self-Supervised Learning Core Concepts

## Pretext Tasks (Pre-Contrastive Era)
- **Rotation Prediction** (Gidaris 2018): Rotate image by 0/90/180/270°, classify angle. Forces understanding of object orientation.
- **Jigsaw Puzzle** (Noroozi & Favaro 2016): Split image into 3x3 grid, shuffle, predict permutation. Learns spatial relationships.
- **Colorization** (Zhang, Isola, Efros 2016): Given grayscale, predict color. Learns semantics since color correlates with object identity.
- These were superseded by contrastive methods which don't need hand-designed tasks.

## Contrastive Learning Core
- Positive pairs: two augmented views of same image
- Negative pairs: views from different images
- Goal: pull positives close in embedding space, push negatives apart
- Key insight: augmentation strategy IS the supervision signal

## InfoNCE Loss
- Essentially softmax classification: "which of N candidates is the real match?"
- Temperature τ controls sharpness (0.05-0.2 typical)
- Low τ → sharp distinctions, high τ → soft

## Representation Collapse
- Central failure mode: map everything to same vector → zero loss trivially
- Contrastive methods prevent via negatives
- Non-contrastive methods need: asymmetry, stop-gradient, EMA, BatchNorm

## Key Methods Timeline
1. SimCLR (Google Brain, 2020) - clean baseline, needs huge batches (4096+)
2. MoCo (Facebook AI, 2019/2020) - momentum encoder + queue, works with batch 256
3. BYOL (DeepMind, 2020) - no negatives, predictor + EMA target
4. DINO (Meta, 2021) - self-distillation with ViTs, emergent attention maps
5. MAE (Meta, 2021) - mask 75% patches, reconstruct pixels
6. DINOv2 (Meta, 2023) - universal visual feature extractor
7. I-JEPA (Meta, 2023) - predict representations not pixels

## CLIP as Contrastive
- Image encoder + text encoder → shared embedding space
- InfoNCE across image-text pairs in batch
- Enables zero-shot classification via text prompts

## Evaluation Protocols
- Linear probing: freeze backbone, train linear classifier on top → measures feature quality
- Fine-tuning: unfreeze all, train end-to-end → measures initialization quality
- Both typically reported

## When SSL Beats Supervised
- Large domain shift from ImageNet
- Few labeled examples in target domain
- Abundant unlabeled target domain data
- Multiple downstream tasks from one backbone
