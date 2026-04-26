# Training Stability — Research Findings

## Vanishing Gradients
- Chain rule multiplies local gradients across layers; sigmoid derivative max is 0.25, so 0.25^50 ≈ 10^-31
- Tanh peaks at 1.0 derivative but in practice neurons rarely sit at zero input — typical range 0.2–0.8
- Symptoms: loss plateaus early, early layers barely update, last layers train fine — "penthouse on sand"
- ReLU fixes this: derivative is exactly 1 for positive inputs, so 1^50 = 1 (no vanishing for active neurons)
- Dead ReLU tradeoff: if neuron goes negative, gradient is permanently 0 — neuron never recovers

## Exploding Gradients
- Same chain rule, opposite: per-layer multiplier >1 means exponential growth (1.5^50 ≈ 6.4×10^8)
- Symptoms: loss suddenly spikes to NaN/inf, weights jump to astronomical values
- Especially brutal in RNNs: same weight matrix multiplied at every timestep = literal matrix exponentiation
- Detection: monitor gradient norms per layer, watch for sudden spikes

## Gradient Clipping
- Norm-based (most common): if total gradient norm > max_norm, scale all gradients down proportionally. Preserves direction.
- Value-based: clamp each element individually — loses direction info, rarely recommended
- Practical max_norm values: 0.5–5.0, commonly 1.0 for RNNs/transformers
- Adaptive Gradient Clipping (AGC): clip per-layer based on ratio of gradient norm to parameter norm. λ=0.01–0.05. Used in NF-Nets (batch-norm-free architectures)
- Rule of thumb: if clipping activates every step, threshold too low

## Weight Initialization
- Zero init → symmetry problem: all neurons identical forever, N neurons = 1 neuron
- Random with wrong scale: too large → exploding activations; too small → collapsing to zero
- Xavier/Glorot (2010): Var(W) = 2/(fan_in + fan_out). For sigmoid/tanh (approx linear near zero)
- He/Kaiming (2015): Var(W) = 2/fan_in. Doubles variance to compensate for ReLU killing ~50% of activations
- PyTorch defaults: nn.Linear uses Kaiming uniform (correct for ReLU). Biases initialized to zero (no symmetry issue)
- BatchNorm reduces initialization sensitivity but doesn't eliminate it — bad init still means slower convergence

## Batch Normalization
- Forward: compute per-feature mean & variance across mini-batch, normalize, then scale (γ) and shift (β) — learnable
- Training mode: uses batch stats, updates running averages (exponential moving average)
- Inference mode: uses saved running averages — no batch dependency
- Original claim: reduces "internal covariate shift" (layer input distributions shifting during training)
- Modern debate: likely helps more via smoothing loss landscape, making optimization better-conditioned
- Limitations: breaks with small batches, variable-length sequences, batch size 1 at inference

## Layer Normalization
- Normalizes across features within each individual sample (not across batch)
- No batch dependency → works with batch size 1, variable sequence lengths
- Why transformers use it: variable-length sequences, distributed training, inference with single samples
- Pre-LayerNorm (before attention/MLP block) much more stable than Post-LayerNorm (after residual)
  - Post-LN: original transformer (2017), GPT-2, early BERT — unstable at scale
  - Pre-LN: GPT-3, Llama, PaLM — strongly recommended for deep models
- RMSNorm: drops mean subtraction, only uses root mean square. Cheaper, similar stability. Used in Llama 2, modern LLMs

## Residual Connections
- y = F(x) + x instead of y = F(x)
- Gradient through skip path is always 1 (∂x/∂x = 1) — gradient highway
- Solves degradation problem: deeper plain networks perform WORSE than shallower ones (not overfitting, optimization failure)
- With residual connections, network only needs to learn the residual F(x) = desired_output - x
- If identity mapping is optimal, F(x)=0 is easy to learn (push weights toward zero)
- ResNets: 152+ layers trainable where plain networks collapse at ~20 layers

## Dead ReLU / Dying Neurons
- Causes: large negative biases/weights from init, high learning rate pushing weights permanently negative
- Detection: activation histograms showing large fraction of zeros, very low mean activations
- Solutions: Leaky ReLU (small slope for x<0), PReLU (learned slope), GELU (smooth, never fully zero), He init, batch norm

## Learning Rate Warmup
- Prevents unstable early training with large gradients
- Especially important with large batch sizes, transformers, pre-trained models
- Linear warmup for several hundred/thousand steps, then decay schedule

## Mixed Precision & NaN Issues
- FP16 training speeds things up but introduces numerical instability
- Dynamic loss scaling: automatically lower scale if NaN detected
- Some operations (softmax, layernorm) kept in FP32 for stability
- BF16 (bfloat16): same exponent range as FP32, better for training stability than FP16
