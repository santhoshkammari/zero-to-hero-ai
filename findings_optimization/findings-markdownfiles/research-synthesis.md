# Optimization Research Synthesis

## Key Insights from Web Research

### Gradient Descent Variants
- Batch: all data per step, smooth but slow
- Stochastic: one sample, fast but noisy
- Mini-batch: sweet spot — hardware efficient, noise helps generalization
- Mini-batch noise helps escape sharp minima toward flatter, more generalizable regions

### Convex vs Non-Convex
- Convex: every local min = global min (linear reg, logistic reg, SVMs)
- Non-convex: neural nets — multiple layers + nonlinear activations = non-convex
- High-dimensional blessing: most local minima are "good enough"
- Saddle points dominate over bad local minima (Dauphin et al., 2014)
- Overparameterization makes many good solutions accessible

### Saddle Points (Dauphin et al., 2014)
- Critical points where gradient=0 but curvature is mixed (positive in some dirs, negative in others)
- In N dimensions, for a local min ALL N directions must have positive curvature — astronomically unlikely
- Local minima exponentially rare vs saddle points as dimensionality increases
- SGD noise + momentum help escape saddles
- This explains why deep nets work despite non-convexity

### Momentum
- Polyak heavy ball: accumulates velocity from past gradients, coasts through flat regions
- Nesterov: "looks ahead" then corrects — more responsive, less overshoot
- Both critical for escaping saddle points where gradient ≈ 0

### Adam Optimizer
- Combines momentum (first moment — direction) + RMSprop (second moment — step size adaptation)
- Per-parameter adaptive learning rates
- Fast convergence, less tuning required
- BUT: tends to find sharper minima → sometimes worse generalization than SGD
- AdamW (Loshchilov & Hutter, 2019): decouples weight decay, closes generalization gap

### SGD vs Adam Debate
- SGD often generalizes better (especially vision tasks) — finds flatter minima
- Adam converges faster but can find sharper minima
- SGD noise acts as implicit regularizer
- AdamW preferred over vanilla Adam when weight decay matters
- Practical: Adam for fast experiments, SGD+momentum for final training on vision

### Learning Rate Schedules
- Step decay: traditional, abrupt drops at milestones
- Cosine annealing: smooth decrease, "soft landing"
- Cyclical LR: oscillate between bounds, helps escape local minima
- One-cycle policy: up then down in one cycle, fast and effective
- Warmup: critical for transformers and large batch training

### Loss Landscape Visualization
- Li et al. (2018): filter-normalized 2D projections
- Skip connections (ResNets) produce smoother landscapes
- Mode connectivity (Garipov et al., 2018): independently found minima connected by low-loss paths
- Challenges notion of isolated local minima

### Second-Order Methods
- Newton's method: uses Hessian (n×n matrix) — too expensive for deep nets
- L-BFGS: approximate inverse Hessian — works for small/medium problems
- Natural gradient: Fisher information matrix — reparameterization invariant
- K-FAC: Kronecker-factored Fisher approximation — scalable but complex
- First-order methods dominate because: cheap, parallelizable, work well enough
