# Findings: Architecture Evolution (LeNet → ConvNeXt)

## Research Summary

### LeNet-5 (1998) — Yann LeCun et al.
- **Purpose**: Handwritten digit recognition (MNIST, postal checks)
- **Architecture**: 2 conv layers (5×5), 2 avg pooling layers, 3 FC layers; ~60K params
- **Key innovations**: Local receptive fields, weight sharing, learnable pooling, end-to-end backprop training
- **Template established**: Conv → Pool → Conv → Pool → FC → Output (still the skeleton)
- **Limitation**: Couldn't scale — no GPUs, small datasets, no ReLU/dropout/BatchNorm
- **14 year gap** before CNNs came back (2012)

### AlexNet (2012) — Krizhevsky, Sutskever, Hinton
- **Context**: ILSVRC ImageNet challenge, 1.2M images, 1000 classes. Previous best ~26% top-5 error
- **Result**: 15.3% top-5 error — 10+ percentage point improvement overnight
- **Key innovations**:
  - ReLU activation (no saturation for positive values, 6× faster training vs tanh)
  - GPU training (2× GTX 580, 3GB each, model split across GPUs)
  - Dropout (p=0.5 in FC layers, new technique at the time)
  - Data augmentation (random crops, flips, PCA color jittering)
- **Architecture**: 5 conv + 3 FC, ~60M params, large 11×11 and 5×5 kernels
- **Not elegant** — the GPU split was an engineering hack — but proved deep learning works

### VGGNet (2014) — Simonyan & Zisserman, Oxford Visual Geometry Group
- **Key insight**: Stack 3×3 convolutions instead of large kernels
  - Two 3×3 layers = same receptive field as one 5×5, fewer params (18 vs 25), extra ReLU
  - Three 3×3 layers = same as one 7×7
- **Architecture**: VGG-16 (16 layers), VGG-19 (19 layers), only 3×3 conv + 2×2 max pool
- **Beautiful simplicity** but massive: 138M parameters (mostly in FC layers)
- **Lesson**: Deeper is better, but you need smarter ways to go deep

### GoogLeNet / Inception v1 (2014) — Szegedy et al.
- **Philosophy**: Don't choose filter size — use 1×1, 3×3, 5×5 in parallel, let network decide
- **1×1 convolution bottleneck**: Reduce channels before expensive ops (e.g., 256→64 before 3×3)
  - This pattern appears everywhere in modern architectures
- **Only 6.8M params** — 20× fewer than VGG, won 2014 ImageNet
- **Auxiliary classifiers** at intermediate layers (later shown not strictly necessary)
- **Limitation**: Complex multi-branch design, hard to modify/extend

### ResNet (2015) — Kaiming He et al.
- **THE most important architecture innovation in deep learning**
- **Degradation problem**: Networks >20 layers performed WORSE (training error increased)
  - Not overfitting — training accuracy itself decreased
  - Identity mapping is hard to learn with stacked nonlinear layers
- **Residual learning**: Learn F(x) = H(x) - x, output = F(x) + x
  - If optimal is identity, F(x) just needs to be ~zero (easy — weight decay does it naturally)
  - Skip connection = "highway" for gradients
- **Two block types**:
  - Basic block (ResNet-18/34): Two 3×3 convs
  - Bottleneck block (ResNet-50/101/152): 1×1 → 3×3 → 1×1 (8× param reduction)
- **Pre-activation ResNet v2**: BN → ReLU → Conv ordering, true identity shortcut
- **Skip connections now everywhere**: U-Net, DenseNet, Transformers, diffusion models

### DenseNet (2017) — Huang et al.
- **Every layer connected to every other layer** (within a block)
- **Concatenation** instead of addition (unlike ResNet)
- **Growth rate k**: Each layer produces k feature maps, channels grow linearly
- **Advantages**: Extreme feature reuse, strong gradient flow, parameter efficient
- **Disadvantage**: Memory hungry (all concatenated features in memory simultaneously)

### EfficientNet (2019) — Tan & Le
- **Problem**: Scaling one dimension (depth/width/resolution) hits diminishing returns
- **Compound scaling**: Scale all three together with fixed ratio using coefficient φ
  - depth = α^φ, width = β^φ, resolution = γ^φ, where α·β²·γ² ≈ 2
- **Baseline from NAS**: EfficientNet-B0 found via neural architecture search
- **B0→B7 family**: 5.3M→66M params, 77.1%→84.3% top-1
- **8.4× fewer params** than previous SOTA at same accuracy

### Vision Transformer — ViT (2020) — Dosovitskiy et al.
- **Radical idea**: Standard Transformer on image patches, no convolutions
- **Image = sequence of patches**: Split 224×224 into 16×16 patches → 196 tokens
- **Data hunger**: Worse than ResNet on ImageNet alone (weak inductive bias)
  - CNNs have built-in local connectivity, translation equivariance
  - ViT needs JFT-300M or ImageNet-21k to surpass CNNs
- **DeiT (2021)**: Right training recipe (augmentation, distillation) fixes data hunger
- **Significance**: Same architecture for vision AND language → multimodal AI unlock

### Swin Transformer (2021) — Liu et al.
- **Shifted window attention**: Local windows (7×7) instead of global attention
- **Hierarchical features**: Multi-scale pyramid like CNNs (4×, 8×, 16×, 32×)
- **Default backbone** for detection/segmentation tasks
- **O(n) complexity** vs ViT's O(n²)

### ConvNeXt (2022) — Liu et al.
- **Provocative question**: What if Transformer success wasn't about attention?
- **Systematic modernization** of ResNet-50 with Transformer-era choices:
  - 7×7 depthwise conv, GELU, LayerNorm, inverted bottleneck, patchify stem
- **Pure CNN matches/beats Swin Transformer** at every scale
- **Meta-lesson**: Ideas matter more than attention vs convolution

## Key Interview Insights
1. Why did networks degrade beyond 20 layers before ResNet? (Identity mapping is hard)
2. ResNet: residual vs full mapping — what changes in optimization landscape?
3. Why 3×3 > 5×5? (VGG insight: fewer params + more nonlinearity)
4. 1×1 convolution purpose (GoogLeNet bottleneck, channel mixing)
5. Compound scaling intuition (depth needs width needs resolution)
6. ViT data hunger vs CNN inductive bias tradeoff
7. ConvNeXt lesson: training recipe often matters more than architecture family
8. Skip connections are universal: ResNet → Transformers → Diffusion → everything
