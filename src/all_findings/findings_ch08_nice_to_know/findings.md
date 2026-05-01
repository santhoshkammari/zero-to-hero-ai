# Ch08 Nice to Know — Training Deep Networks: Research Findings

## Weight Averaging & EMA

### Stochastic Weight Averaging (SWA)
- Average weights from last several epochs instead of using final weights
- Lands in flatter minima → better generalization (free 1-2% accuracy boost)
- PyTorch built-in: `torch.optim.swa_utils.AveragedModel`
- Key insight: flat minima = small weight changes → small loss changes → robust to perturbations
- Must update batch norm stats after averaging (`update_bn`)
- Paper: Izmailov et al. 2018 "Averaging Weights Leads to Wider Optima and Better Generalization"

### Exponential Moving Average (EMA)
- Shadow copy of weights: EMA_{t+1} = α × EMA_t + (1 - α) × W_{t+1}, α ≈ 0.999
- Use shadow weights at inference, train with regular weights
- Smooths noisy SGD updates → acts like lightweight model ensembling (Polyak averaging)
- Standard in diffusion models, GANs, self-supervised learning, production setups
- Doesn't change training dynamics, only affects inference weights

## Training Strategies

### Knowledge Distillation
- Student (small) mimics teacher (large) soft probability outputs
- Soft labels carry richer info: cat=0.7/tiger=0.2/lynx=0.1 teaches inter-class relationships
- Temperature scaling: softmax(z_i / T) with T > 1 → softer distributions → amplifies dark knowledge
- Student loss = α × KL(soft_student, soft_teacher) + (1-α) × CE(hard_student, hard_label)
- Hinton et al. 2015 "Distilling the Knowledge in a Neural Network" — coined "dark knowledge"
- This is how you compress 10B params into something running on a phone

### Curriculum Learning
- Feed model easy examples first, gradually introduce harder ones
- Bengio et al. 2009
- Helps with: noisy/complex data, tasks with natural difficulty progression, avoiding bad local minima
- Doesn't help much with clean/balanced datasets without clear difficulty gradient
- Self-paced learning (automated curriculum) is gaining traction in 2024
- Used in LLMs, multi-modal tasks, RL

### Progressive Resizing
- Start training on small images (64×64), increase resolution over time (128, 224, etc.)
- Early epochs fast (small images cheap), later epochs fine-tune at full resolution
- Acts as regularization: small images force model to learn global features first
- Popular in fast.ai workflows, Kaggle competitions
- Essentially curriculum learning applied to input resolution
- Bonus: smaller images = larger batch sizes = more stable gradients on limited VRAM

## Memory & Compute Tricks

### Gradient Checkpointing
- Normal: forward pass stores ALL intermediate activations for backward pass
- Checkpointing: store activations only at certain checkpoints, recompute the rest during backprop
- Memory: O(L) → O(√L) when checkpointing every √L layers
- ~60% GPU memory savings at ~20% speed cost
- Essential for fine-tuning 7B+ LLMs on single GPU
- PyTorch: `torch.utils.checkpoint`

### torch.compile (PyTorch 2.0+)
- One-line API: `model = torch.compile(model)`
- TorchDynamo: intercepts Python bytecode, extracts pure PyTorch ops
- TorchInductor: compiles sub-graphs to optimized CUDA/Triton/C++ kernels
- Speedup: 1.5x–3x via kernel fusion, reduced Python overhead, backend specialization
- 2024 status: stable for standard models (CNNs, transformers), some edge cases still problematic
- Default backend for GPU/CPU since PyTorch 2.x

## Exotic Optimizers

### Lookahead Optimizer
- Wraps any base optimizer (usually Adam)
- Maintains "slow weights" that periodically sync with "fast weights"
- Optimizer occasionally steps back to verify fast exploration direction
- Can improve training stability, not widely adopted

### LAMB / LARS
- Layer-wise adaptive learning rate for large batch training (32K+ batch size)
- LARS: for vision (ResNet), LAMB: for language (BERT)
- Scales learning rate per-layer because what works for one layer can be wrong for another
- Only needed for serious distributed training at massive scale

### Sharpness-Aware Minimization (SAM)
- Minimizes loss AND sharpness of loss landscape simultaneously
- Seeks parameters robust to small perturbations → flat minima → better generalization
- Catch: requires TWO forward-backward passes per step → doubles compute
- Consistently improves generalization in benchmarks
- Foret et al. 2021 (NeurIPS)

## Large-Scale Training Frameworks

### DeepSpeed (Microsoft)
- ZeRO optimizer: shards model states across GPUs
  - Stage 1: Shard optimizer states only
  - Stage 2: + Shard gradients
  - Stage 3: + Shard parameters (everything sharded, train 100B+ models)
- Higher stages = more memory savings but more communication overhead
- Can train models that don't fit on any single device

### Megatron-LM (NVIDIA)
- Tensor parallelism, pipeline parallelism, sequence parallelism
- Focus on compute efficiency (vs DeepSpeed's memory efficiency focus)
- Many large-scale setups combine both DeepSpeed + Megatron-LM

## Experiment Tracking

### Weights & Biases (W&B)
- De facto standard in research and industry (2024)
- Real-time interactive dashboards, hyperparameter sweeps, artifact versioning
- Two lines: `wandb.init()` and `wandb.log()`
- Free for personal use
- Alternatives: MLflow (open-source, enterprise/on-prem), Neptune, TensorBoard
- Many teams: W&B for R&D, MLflow for production governance

## Interview Gotchas & Key Insights
- EMA vs SWA: EMA is online (every step), SWA is offline (average last N checkpoints)
- Knowledge distillation temperature: T=1 is standard softmax, T>1 softens → more dark knowledge
- Gradient checkpointing: √L checkpoints is the sweet spot (memory vs compute)
- torch.compile: first compilation is slow (graph capture), subsequent runs are fast
- SAM's 2x cost is why it's competitions-only in practice
- DeepSpeed ZeRO Stage 3 vs FSDP: PyTorch's FSDP is the native alternative to ZeRO Stage 3
- Curriculum learning: defining "difficulty" is the hard part — loss-based scoring, model confidence, or hand-crafted heuristics
