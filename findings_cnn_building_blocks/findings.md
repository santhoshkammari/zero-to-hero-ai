# CNN Building Blocks — Research Findings

## Convolution Operation
- CNNs use cross-correlation (no kernel flipping), not true mathematical convolution. Doesn't matter because weights are learned.
- Core idea: a small kernel (template) slides across the input, computing element-wise multiply-and-sum at each position. Output = feature map showing where/how strongly that pattern was detected.
- Multi-channel: kernel is 3D (K×K×C_in), sums over all input channels to produce one output value. Multiple filters → multiple output channels.
- Parameter sharing: same kernel used everywhere → massive parameter reduction vs FC layers. A 3×3 kernel on 64 channels = 576 weights per filter, not millions.

## Why Convolutions Beat FC Layers (Inductive Bias)
- **Local connectivity**: each neuron sees only a small patch. Natural images have local structure (edges, textures).
- **Weight sharing**: same filter everywhere. An edge detector works regardless of position.
- **Translation equivariance**: if input shifts, output shifts the same way. FC layers have no such property.
- Parameter explosion with FC: 224×224×3 = 150,528 inputs. One hidden layer of 1000 neurons = 150M weights. A 3×3 conv with 64 filters = ~1,800 weights.

## Stride, Padding, Dilation
- **Stride**: how far kernel moves per step. Stride 2 halves output dimensions. ResNet uses stride-2 convs instead of pooling — learnable downsampling.
- **Padding**: "valid" (no padding) shrinks output; "same" (pad to preserve size). Without padding, 20 layers loses 40 pixels of width.
- **Dilation (atrous)**: spaces out kernel elements with gaps. 3×3 with dilation=2 covers 5×5 area with 9 weights. Critical for DeepLab (segmentation), WaveNet (audio). Risk: gridding artifacts.
- **Output size formula**: (W - K + 2P) / S + 1. With dilation: effective kernel = K + (K-1)(d-1).

## Filters/Kernels — What They Learn
- Zeiler & Fergus (2013) visualization with deconvnet:
  - **Layer 1**: Gabor-like edge detectors, color blobs. Nearly universal across all CNNs.
  - **Layer 2-3**: Corners, texture motifs, edge combinations.
  - **Layer 4-5**: Object parts (wheels, eyes, dog faces), object-level patterns.
- This hierarchy emerges purely from backpropagation — nobody programs it.
- Foundation of transfer learning: early features are universal, deep features are task-specific.

## Pooling
- **Max pooling**: keeps maximum value per window. Provides translation invariance (small shifts don't change max). Used in mid-network. No learnable parameters.
- **Average pooling**: mean of window values. Smoother, less common in mid-network.
- **Global Average Pooling (GAP)**: collapses entire H×W to single value per channel. GoogLeNet (2014) popularized it. Replaced massive FC layers (VGG's FC1 = 102M params). Acts as regularizer. Enables input-size flexibility.
- **Strided convolutions as alternative**: learnable downsampling. "Striving for Simplicity" (Springenberg et al., 2014). Modern trend: strided convs for intermediate downsampling, GAP before classifier.

## Receptive Field
- **Theoretical RF**: region of input that CAN influence a neuron. RF = L×(K-1)+1 for L layers of K×K conv with stride 1.
- **Effective RF** (Luo et al., 2016): actual influence follows Gaussian — center pixels matter much more than borders. Effective RF ≈ √(theoretical RF) in some cases.
- Practical: if object spans 200×200 pixels, effective RF at detection layer must cover that. Theoretical RF may need to be 400×400+.
- Strategies to increase RF: dilated convolutions, aggressive downsampling, feature pyramid networks, skip connections.

## Depthwise Separable Convolutions
- Standard conv: K²×C_in×C_out parameters. Mixes spatial and channel at once.
- Depthwise separable splits into:
  1. **Depthwise**: separate K×K filter per channel. Params: K²×C_in.
  2. **Pointwise**: 1×1 conv to mix channels. Params: C_in×C_out.
- Total: K²×C_in + C_in×C_out vs K²×C_in×C_out. Ratio ≈ 1/K² for large C_out.
- For 3×3: ~9× fewer parameters.
- MobileNet V1 (2017): AlexNet-level accuracy with 1/30th parameters.
- MobileNet V2: inverted residuals with expansion (expand → depthwise → project back).
- EfficientNet: depthwise separable as fundamental building block.
- Trade-off: depthwise step limits cross-channel interaction. On server with abundant compute, standard convs can be slightly better.

## Transposed Convolution
- Insert zeros between input elements, then apply regular conv. Produces larger output.
- Used in U-Net, autoencoders, GANs, super-resolution.
- Checkerboard artifacts: uneven overlap when stride doesn't divide evenly into kernel size (Odena et al., distill.pub).
- Modern fix: bilinear upsampling + regular conv. Separates "make it bigger" from "learn features." Cleaner outputs.

## 1×1 Convolution
- Processes each spatial location independently across channels. Acts like per-pixel MLP.
- Purposes: channel reduction (bottleneck), channel expansion, cross-channel interaction.
- Network in Network (2013): introduced concept.
- GoogLeNet/Inception: 1×1 before expensive 3×3/5×5 to reduce channels.
- ResNet bottleneck: 1×1 reduce → 3×3 conv → 1×1 expand. Reduces computation dramatically.

## Conv-BN-ReLU Block
- Standard pattern in modern architectures. bias=False in conv when followed by BN (BN has its own bias).
- Design pattern: spatial dims go down, channel count goes up (224→112→56→28→1 spatially, 3→64→128→256 in channels).
- Trading spatial resolution for feature richness.

## Interview-Depth Insights
- Calculate output size in your head: (W-K+2P)/S + 1
- Parameter count: (K×K×C_in + 1) × C_out (the +1 is bias)
- Why two 3×3 layers > one 5×5: same RF (5×5), fewer params (18 vs 25 per channel pair), plus extra nonlinearity
- Effective vs theoretical RF: most people only know theoretical. Knowing about effective RF shows depth.
- 1×1 convolution as "channel-wise FC layer" — shows understanding of bottleneck design
- Depthwise separable: know the exact reduction ratio (1/N + 1/K²)
