# Self-Supervised & Representation Learning - Core Research Findings

## The Labeled Data Problem
- ImageNet: years, millions of dollars, 14M images labeled
- Medical imaging: $400/hr board-certified radiologists
- Internet produces ~2.5 quintillion bytes of unlabeled data daily
- Self-supervised learning: design tasks where data labels itself

## Pretext Tasks
- Corrupt/hide part of input, train model to recover it
- NLP: Masked LM (BERT), Next Token Prediction (GPT)
- Vision: Rotation prediction, Jigsaw puzzles, Colorization, MAE
- The task is the excuse; the representation is the prize
- Got eclipsed in vision by contrastive methods (hand-designed, features don't always transfer)

## Contrastive Learning Core
- Learn representations by knowing what's similar vs different
- Positive pairs: augmented views of same image
- Negative pairs: different images in batch
- InfoNCE loss: softmax over cosine similarities
- Temperature τ controls concentration on hard negatives

### SimCLR (Chen et al., 2020)
- augment → encode → project → contrast
- Key findings: strong augmentations matter most, projection head critical, large batch sizes (4096+) needed
- Achilles' heel: needs 128 TPU cores for proper training
- Paper: "A Simple Framework for Contrastive Learning of Visual Representations"

### MoCo (He et al., 2020)
- Queue of 65,536 negatives (decoupled from batch size)
- Momentum encoder: EMA update (τ=0.999) for consistency
- First to match supervised ImageNet features on single 8-GPU machine
- MoCo v2: borrowed SimCLR augmentations + projection head

## Non-Contrastive Methods

### BYOL (Grill et al., 2020)
- No negatives needed, outperformed SimCLR and MoCo
- Online network (encoder + projector + predictor) and Target network (encoder + projector, EMA updated)
- Why no collapse: architectural asymmetry (predictor + stop-gradient + EMA)
- Collapse becomes unstable equilibrium rather than attractive one

### Barlow Twins (Zbontar et al., 2021)
- Inspired by neuroscientist Horace Barlow's redundancy reduction hypothesis
- Push cross-correlation matrix toward identity
- Diagonal=1: each feature captures same content across views
- Off-diagonal=0: different features capture different information
- No negatives, no momentum, no asymmetry

### VICReg
- Variance-Invariance-Covariance Regularization
- Invariance: similar views → similar representations
- Variance: ensure sufficient variance per dimension (explicit collapse prevention)
- Covariance: penalize correlation between dimensions

## DINO & DINOv2
- Self-distillation with No Labels (2021, Caron et al.)
- Student-teacher framework, teacher is EMA of student
- Emergent segmentation: attention maps automatically highlight objects
- DINOv2 (2023): larger scale, better architectures, universal visual features

## MAE (He et al., 2022)
- Mask 75% of image patches, reconstruct them
- Only encode visible 25% patches (very efficient)
- Lightweight decoder reconstructs masked patches
- Loss: MSE on masked patches only
- Heavy masking forces global representation learning

## Representation Learning Theory (Bengio 2013)
- Manifold hypothesis: real data lies on low-dimensional manifolds
- Good representations: invariant to irrelevant, sensitive to relevant
- Properties: disentanglement, informativeness, compactness, sparsity, hierarchical
- Wang & Isola (2020): alignment (positives close) + uniformity (spread out on hypersphere)

## Evaluation
- Linear probe: freeze encoder, train linear classifier on top (gold standard for representation quality)
- Fine-tuning: unfreeze encoder, train end-to-end with small LR
- Gap between linear probe and fine-tuning = task-specific adaptation needed
