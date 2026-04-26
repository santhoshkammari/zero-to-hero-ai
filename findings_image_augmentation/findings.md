# Findings: Image Augmentation (Ch09 S04)

## Core Concept
- Augmentation teaches models **invariances** — things that shouldn't change the label
- Invariance vs equivariance distinction: classification wants invariance (f(T(x)) = f(x)), detection/segmentation wants equivariance (output transforms predictably with input)
- Augmentation = inductive bias — encoding prior knowledge about a problem's symmetries
- Acts as implicit regularization: reduces capacity to memorize inconsequential details
- Expands support of training distribution to better cover real-world deployment distribution

## Geometric Transforms
- Horizontal flip: doubles effective dataset, almost universal for natural images
- DANGER: don't flip digits 6/9, text, medical L/R anatomy, compass-oriented satellite imagery
- Vertical flip: useful for aerial/microscopy/satellite where "up" is arbitrary
- RandomResizedCrop: arguably single most important augmentation for classification (8%–100% area, 3/4 to 4/3 aspect ratio)
- Rotation: ±15° for natural images, up to 360° for aerial/pathology
- Affine/perspective: combine rotation, scaling, translation, shearing — use small magnitudes
- Border handling matters for rotations especially on small images

## Color & Intensity Transforms
- ColorJitter: brightness, contrast, saturation, hue — the color equivalent of flipping
- Keep hue shifts small (≤0.1) to avoid unnatural colors
- Random grayscale (p=0.1-0.2): forces reliance on shape over color, combats spurious color correlations
- Channel shuffle/dropout: similarly reduces color dependence
- Must apply BEFORE normalization (spatial → color → ToTensor → Normalize)
- Match to deployment: security cameras → brightness reduction + blur; scanned docs → contrast + slight rotation

## Advanced Augmentations (2017-2020 era)

### Cutout / Random Erasing (2017)
- Randomly mask square region with zeros or random values
- Dropout applied to input image
- Forces redundant feature learning — model can't rely on single most discriminative region
- Labels remain UNCHANGED (key difference from MixUp/CutMix)

### MixUp (Zhang et al., 2018)
- Blend two images: x_new = λ*x_a + (1-λ)*x_b, same for labels
- λ ~ Beta(α, α), typically α = 0.2 to 0.4
- Forces linear behavior between training samples → smoother decision boundaries
- Improves calibration and adversarial robustness
- α=0.2: mostly one image with ghost of other; α=1.0: uniform blends
- Weakness: produces unnatural "ghostly" images

### CutMix (Yun et al., 2019)
- Cut patch from one image, paste onto another; labels mixed by area proportion
- Strictly better than Cutout: masked region filled with useful content instead of zeros
- Better than MixUp: locally coherent patches rather than ghostly blends
- Consistently +1-2% on ImageNet, standard in modern training recipes (DeiT, ConvNeXt)
- Combines spatial regularization (from Cutout) with label smoothing (from MixUp)

### Mosaic (YOLOv4/v5)
- Combines 4 images in quadrants
- Particularly powerful for object detection: multiple scales, more context diversity per batch
- Reduces need for separate multi-scale training

## Comparison: CutOut vs MixUp vs CutMix
| Method  | Spatial Mixing | Label Mixing | Regularization Type    |
|---------|---------------|-------------|----------------------|
| CutOut  | Yes (masking) | No          | Local (occlusion)    |
| MixUp   | No (blending) | Yes         | Global (interpolation)|
| CutMix  | Yes (patches) | Yes         | Local + Label-aware  |

## Automated Augmentation Policies

### AutoAugment (Cubuk et al., 2019, Google)
- RL to search over augmentation policy space
- Found surprising combinations no human would try
- Cost: ~15,000 GPU hours on P100s (~$50,000) — impractical for most teams
- Policies transfer somewhat across datasets

### RandAugment (Cubuk et al., 2020)
- Pick N random augmentations at magnitude M from fixed set
- Only 2 hyperparameters instead of dozens
- Default: N=2, M=9 — matches or beats AutoAugment
- Total search cost: few training runs vs thousands
- The practical choice for most teams

### TrivialAugment (Müller & Hutter, 2021)
- Single random augmentation with random magnitude
- Zero hyperparameters
- Matches RandAugment on most benchmarks
- Sometimes the simplest approach wins

### AugMix
- Combines multiple augmentations in parallel, mixes results
- Excellent for robustness to distribution shift and corruption
- Moderate compute cost

## Newer Techniques (2020-2024)
- GridMask: grid of rectangular masks, distributes occlusion evenly
- FMix: Fourier-transform-based binary masks for mixing
- PuzzleMix: optimal transport + saliency for semantically meaningful mixing
- SnapMix/AttentiveMix: attention-based mixing
- SaliencyMix: preserves important regions during mixing
- KeepAugment: saliency-based, preserves informative regions
- TokenMix: adapted for Vision Transformers, works in token/patch domain
- AugMax: adversarial composition of augmentations for robustness

## GPU-Accelerated Augmentation
- Albumentations: OpenCV-based, 2-10x faster than torchvision for heavy augmentations
- Kornia: PyTorch-native, pure tensor ops, GPU-accelerated
- NVIDIA DALI: end-to-end GPU pipeline including decode, augment, batch
- torchvision.transforms: PIL-based, slower but tight PyTorch integration
- On-the-fly augmentation: augment during batch loading, saves disk space, infinite variety

## Task-Specific Considerations
- Classification: augment image only, label unchanged
- Detection: MUST adjust bounding box coordinates after spatial transforms
- Segmentation: MUST apply identical spatial transforms to image AND mask
- Common pitfall: forgetting to transform annotations alongside images

## Test-Time Augmentation (TTA)
- Create multiple augmented versions at inference, average predictions
- Typically +0.5-2% accuracy boost
- Works because errors on different views are partially uncorrelated — averaging reduces variance
- Essentially an ensemble where "different models" = same model seeing different views
- Standard in Kaggle top solutions
- Diminishing returns after 4-8 augmentations
- Trade-off: more augmentations = more accuracy = more inference time
- Competition: 10-20 TTA passes; Production: 2-5

## Critical Best Practices
1. "Does the label survive this transform?" — the cardinal rule
2. Don't augment validation/test data (except TTA)
3. Stronger augmentation → need more training epochs
4. Start gentle on small datasets, add augmentations one at a time
5. Turn off augmentation first when debugging
6. Different tasks need different augmentations
7. Augmentation order: spatial → color → normalize
8. Match augmentations to deployment domain

## Interview-Depth Insights
- Augmentation as group theory: transforms correspond to symmetry groups
- Connection to Vicinal Risk Minimization (VRM) — MixUp explicitly minimizes vicinal risk
- Label smoothing effect of MixUp/CutMix
- Why augmentation works differently for self-supervised learning (SimCLR uses very aggressive augmentations because the pretext task itself is about invariances)
- Augmentation schedule: can increase augmentation strength during training (similar to curriculum learning)
- Over-augmentation can hurt: model spends capacity handling distortions instead of learning the task
