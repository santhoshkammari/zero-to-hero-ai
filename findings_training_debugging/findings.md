# Training Debugging & Stability — Research Findings

## Sources Consulted
- Andrej Karpathy, "A Recipe for Training Neural Networks" (2019)
- Leslie N. Smith, "Cyclical Learning Rates for Training Neural Networks" (2017, arXiv:1506.01186)
- Hao Li et al., "Visualizing the Loss Landscape of Neural Nets" (2018, arXiv:1712.09913)
- Foret et al., "Sharpness-Aware Minimization" (2021, arXiv:2010.01412)
- Garipov et al., "Loss Surfaces, Mode Connectivity, and Fast Ensembling" (2018, arXiv:1802.10026)
- PyTorch docs: Reproducibility, AMP, detect_anomaly
- NVIDIA Mixed Precision Training docs
- Power et al., "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets" (2022)

## Key Findings

### Loss Landscape Geometry
- Non-convex surface with n+1 dimensions for n parameters
- In high dimensions, most critical points are saddle points, not local minima (Dauphin et al. 2014)
- Probability all Hessian eigenvalues are positive → vanishingly small in high-D
- Sharp minima generalize poorly; flat minima generalize well (Keskar et al. 2017)
- Li et al. (2018) showed skip connections dramatically smooth the loss landscape — ResNets have much smoother landscapes than VGGs
- Mode connectivity: independently trained models can be connected via low-loss paths (Garipov et al. 2018)
- SAM (Foret et al. 2021) explicitly optimizes for flat minima by minimizing worst-case loss in a neighborhood

### Batch Size & Landscape Navigation
- Small batch SGD noise acts as implicit regularizer, pushes toward flat minima
- Large batch training tends to sharp minima, worse generalization
- Linear scaling rule: scale LR linearly with batch size (Goyal et al. 2017)
- LR warmup critical for large batch training — prevents early catapulting into bad basins

### NaN Loss — Root Causes
1. Exploding gradients → weights overflow to inf → NaN propagation
2. Numerical instability: log(0), sqrt(0), x/0, exp(large)
3. float16 overflow (max ~65,504) — particularly softmax, squared terms
4. Bad data: NaN/Inf values in input data
5. Learning rate too high — overshooting to infinity
6. Missing epsilon guards in custom loss functions

### Learning Rate Finder (Smith 2017)
- Start at very low LR (1e-7), increase exponentially per batch (not epoch)
- Plot loss vs LR on log scale
- Optimal LR: ~one order of magnitude below where loss starts exploding
- Formula: lr = lr_start * (lr_end/lr_start)^(batch_num/total_batches)
- Usually run for less than 1 epoch
- Stop early if loss diverges (>4x initial loss)

### Loss Curve Patterns
1. Good fit: both train/val decrease, converge close together
2. Overfitting: train decreases, val decreases then increases
3. Underfitting: both remain high, minimal decrease
4. Double descent: val loss decreases, increases, then decreases again with more capacity/epochs
5. Grokking: train loss drops early, val loss stays high for thousands of steps, then suddenly drops

### Reproducibility
- Sources of nondeterminism: CUDA atomics, cuDNN algo selection, DataLoader workers, random seeds
- Need to seed: torch, cuda, numpy, python random, cuda.manual_seed_all
- torch.backends.cudnn.deterministic = True (slower)
- torch.backends.cudnn.benchmark = False
- DataLoader worker_init_fn for per-worker seeding
- Even with all seeds set, cross-machine/cross-version reproducibility not guaranteed
- torch.use_deterministic_algorithms(True) — strictest mode, raises error on non-deterministic ops

### Common Silent Training Bugs
1. Forgetting model.eval() during validation — dropout/batchnorm in wrong mode
2. Double softmax: model's softmax + CrossEntropyLoss's internal LogSoftmax
3. loss.append(loss) instead of loss.append(loss.item()) — stores computation graph, OOM
4. Not calling optimizer.zero_grad() — gradient accumulation bug
5. Wrong dtype: int tensors where float expected, kills gradients silently
6. Applying augmentation to validation set
7. Preprocessing stats computed on full dataset instead of train-only (data leakage)
8. Scheduler stepped per batch instead of per optimizer step with gradient accumulation
9. Frozen parameters from .detach() or requires_grad=False
10. Missing model.train() after model.eval()

### Gradient Clipping in Practice
- Standard default: max_norm=1.0 (BERT, HuggingFace Transformers default)
- Range 0.1-5.0 typical
- Very unstable training: lower to 0.5
- Stable/shallow models: up to 5.0
- Always clip BEFORE optimizer.step()

### Weight Initialization
- Xavier/Glorot: for sigmoid/tanh activations
- Kaiming/He: for ReLU and variants (modern default)
- PyTorch nn.Linear uses Kaiming Uniform by default
- Less critical when using BatchNorm (normalizes activations anyway)

### Grokking & Delayed Generalization
- Model memorizes (low train loss) long before generalizing (low val loss)
- Weight decay can both delay and promote grokking
- Connected to phase transitions in training dynamics
- Practical implication: sometimes training longer helps even when it looks stuck

### Karpathy's Key Debugging Wisdom
- "Failing to overfit a tiny batch is the equivalent of a segmentation fault in deep learning"
- Start simple, verify, scale up
- Most failures are "dumb bugs," not theoretical issues
- Debug visually: look at data, losses, gradients
- Zero out inputs as a test — model output should reflect this
- Quick feedback loops over long training runs
