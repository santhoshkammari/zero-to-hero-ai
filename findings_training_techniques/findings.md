# Findings: Training Techniques — Normalization, Regularization & Gradients

## Normalization Deep Dive

### BatchNorm (Ioffe & Szegedy, 2015)
- Original claim: reduces "internal covariate shift" — each layer's input distribution shifts as weights update
- Santurkar et al. (2018) "How Does Batch Normalization Help Optimization?" debunked this: BN works because it **smooths the loss landscape**, making gradients more predictive and allowing higher learning rates
- Computes mean/var across batch dimension per channel: shape (B, H, W) → per-channel stats
- Learnable γ (scale) and β (shift) let the network undo normalization if needed
- Train/eval split: uses batch stats during training, exponential moving average during inference
- **Critical bug vector**: forgetting model.eval() → batch-dependent inference outputs
- Breaks down with small batches (2-4): noisy statistics → unstable training
- SyncBatchNorm aggregates stats across GPUs for larger effective batch

### LayerNorm (Ba et al., 2016)
- Normalizes across features per sample — no batch dependency
- Works with batch size 1, identical train/eval behavior, no running stats
- **The normalization for Transformers**: GPT, LLaMA, BERT, T5 all use it
- Reason: variable-length sequences, often batch size 1 at inference

### Pre-LN vs Post-LN (Xiong et al., 2020)
- Original Transformer (Vaswani 2017): Post-LN = LayerNorm(x + Sublayer(x))
- Pre-LN = x + Sublayer(LayerNorm(x)) — gradient flows directly through residual path
- Pre-LN is dramatically more stable for deep models, allows skipping LR warmup
- Post-LN can achieve marginally better final performance but needs careful warmup
- Modern LLMs (GPT-2/3, LLaMA, Mistral) all use Pre-LN

### GroupNorm (Wu & He, 2018)
- Splits channels into groups, normalizes within each group per sample
- Sweet spot: no batch dependency + respects channel structure
- num_groups=num_channels → InstanceNorm; num_groups=1 → LayerNorm
- Default in Detectron2 for detection/segmentation (small batch sizes)

### RMSNorm (Zhang & Sennrich, 2019)
- Key insight: mean subtraction in LayerNorm may not be necessary
- Only divides by RMS (root mean square) — no mean centering
- Only scale parameter γ, no shift β — fewer parameters
- ~7-10% faster than LayerNorm at scale
- LLaMA paper: "We replace LayerNorm with RMSNorm. We did not observe any degradation in performance."
- Used by: LLaMA 1/2/3, Mistral, Gemma — becoming the default for LLMs
- Formula: y = x / RMS(x) * γ, where RMS(x) = sqrt(mean(x²) + ε)

### InstanceNorm (Ulyanov et al., 2016)
- Per-channel, per-sample normalization
- Strips style information (mean contrast, brightness)
- Go-to for style transfer, rarely used elsewhere

## Regularization Deep Dive

### Dropout (Srivastava et al., 2014)
- Randomly zeros activations with probability p during training
- **Ensemble interpretation**: each mask = different sub-network; training = training exponential number of weight-sharing sub-networks; inference with all neurons ≈ ensemble average
- **Bayesian interpretation** (Gal & Ghahramani, 2016): dropout ≈ approximate variational inference; Monte Carlo Dropout = keep dropout on at test time, run multiple passes → uncertainty estimates
- Inverted dropout: scale by 1/(1-p) during training so no adjustment at inference
- Typical rates: 0.1 for Transformers, 0.2-0.5 for MLPs
- **Trend**: Large models (GPT-3+, LLaMA) train with zero dropout when data is large enough — overfitting less of a concern, dropout noise hurts optimization speed

### DropPath / Stochastic Depth (Huang et al., 2016)
- Drops entire residual blocks instead of individual neurons
- Each block bypassed with some probability → identity shortcut only
- Drop probability often increases with depth (deeper layers more likely skipped)
- Widely used in Vision Transformers (ViT, Swin), modern ResNets
- More appropriate than standard dropout for residual architectures

### Weight Decay / L2 Regularization
- L2 adds λ||w||² to loss → gradient gets λw added → pushes weights toward zero
- In SGD: L2 ≡ weight decay
- In Adam: they DIVERGE — L2 penalty goes through adaptive moment scaling, distorting regularization
- **AdamW** (Loshchilov & Hutter, 2019): decouples weight decay from gradient computation
  - Normal Adam step first, then separate weight shrinkage
  - Consistent regularization regardless of gradient magnitude
- Typical values: 0.01 to 0.1
- **The most important regularizer** — used in virtually every modern recipe
- Don't apply to bias terms or LayerNorm parameters (convention)

### Label Smoothing (Szegedy et al., 2016)
- Soft targets: correct class gets (1 - ε), others get ε/(K-1)
- Prevents model from pushing logits to infinity (overconfidence)
- Improves calibration: predicted probabilities better match true probabilities
- Connection to knowledge distillation (Müller et al., 2019): label smoothing ≈ distillation from uniform prior
- Standard ε = 0.1; used in most image classification and machine translation
- Müller et al. showed it hurts knowledge distillation when teacher uses it (clusters penultimate representations)

### Mixup (Zhang et al., 2018) & CutMix (Yun et al., 2019)
- Mixup: linear interpolation of inputs AND labels: x̃ = λx_i + (1-λ)x_j, ỹ = λy_i + (1-λ)y_j
- λ ~ Beta(α, α), typically α=0.2-0.4
- Encourages linear behavior between training examples → smoother decision boundaries
- CutMix: cut patch from one image, paste on another, mix labels by area proportion
- Both improve robustness and calibration; standard in competitive vision pipelines

### Early Stopping
- Monitor validation loss, stop when it degrades
- Patience: 5-20 epochs typical
- Always save best checkpoint, not final epoch

## Gradient Management Deep Dive

### Gradient Clipping
- **By value**: clamp each element to [-v, v] — changes gradient direction, not preferred
- **By global norm** (preferred): if ||g|| > max_norm, scale g ← g * max_norm/||g||
  - Preserves gradient direction, only reduces magnitude
- Essential for RNNs and Transformers (long sequences = deep compute graphs)
- Default max_norm: 1.0 for most models, 0.5 sometimes for very deep
- Order: loss.backward() → clip → optimizer.step()

### Gradient Accumulation
- Simulate large batches: accumulate gradients over N micro-batches before optimizer step
- Must divide loss by N to maintain correct gradient magnitude
- Used universally in LLM training (GPT-3: effective batch of 3.2M tokens)
- Works with gradient clipping: clip after accumulation, before step

### Mixed Precision & Loss Scaling
- FP16 training: faster compute, less memory, but limited dynamic range
- Loss scaling: multiply loss by large factor before backward → prevents gradient underflow in FP16
- Dynamic loss scaling (GradScaler): auto-adjusts scale, skips steps on overflow
- BF16: larger dynamic range, usually no loss scaling needed
- Keep BN, softmax, loss computation in FP32

### Vanishing/Exploding Gradients — Full Solution Stack
1. Proper initialization (He/Xavier) — sets initial gradient magnitudes
2. Normalization (BN/LN/RMSNorm) — keeps activations in stable range
3. Residual connections — gradient highway bypassing transformations
4. Gradient clipping — safety net for explosions
5. Activation functions (ReLU, GELU) — avoid saturating regions
6. All used together in modern architectures — no single silver bullet

## Interview-Depth Insights

- "Why does BatchNorm work?" → Loss landscape smoothing (Santurkar 2018), NOT internal covariate shift
- "BN vs LN?" → BN for CNNs with large batches, LN for Transformers, GN for small-batch vision
- "Why RMSNorm in LLaMA?" → Same performance, fewer ops (no mean subtraction), faster at scale
- "Dropout as Bayesian inference?" → Gal & Ghahramani 2016, MC Dropout for uncertainty
- "Why AdamW not Adam?" → L2 in Adam gets distorted by adaptive scaling; decoupled decay is correct
- "Label smoothing hurts distillation?" → Müller et al. 2019, clusters representations
- "Pre-LN vs Post-LN?" → Pre-LN more stable gradient flow, Post-LN slightly better final perf
