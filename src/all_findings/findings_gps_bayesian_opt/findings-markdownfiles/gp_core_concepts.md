# GP & Bayesian Optimization Core Concepts

## GP Intuition
- GP = distribution over functions, not single function
- Any finite subset of function values is jointly Gaussian
- Specified by mean function m(x) and kernel k(x,x')
- The kernel IS the model — it encodes smoothness, periodicity, scale

## Kernels
- RBF: infinitely smooth, default choice, can be unrealistically smooth
- Matern-3/2: once differentiable, more realistic for physical processes
- Matern-5/2: twice differentiable, practical default
- Periodic: repeating patterns, seasonal data
- Kernels can be composed: added, multiplied

## GP Regression
- Condition prior on data → posterior is also GP
- Predictive mean = weighted sum of training outputs
- Predictive variance = shrinks near data, grows in unexplored regions
- Key: matrix inversion of K + σ²I

## GP Classification
- Latent function through sigmoid/probit squashing
- Non-Gaussian likelihood → posterior intractable
- Approximate inference: Laplace, EP, VI

## Computational Challenges
- O(n³) time, O(n²) memory for exact inference
- Sparse GPs: M inducing points, O(nM²)
- Variational inference for learning inducing points
- GPyTorch: GPU-accelerated, 100K+ points

## Bayesian Optimization
- Expensive black-box function optimization
- Surrogate model (GP) + acquisition function
- Loop: fit surrogate → maximize acquisition → evaluate → update

## Acquisition Functions
- EI: expected improvement over current best, default choice
- UCB: μ + κσ, explicit exploration control
- PI: probability of improvement, too greedy in practice

## Multi-fidelity BO
- Use cheap approximations (fewer epochs, less data) 
- Successive halving, Hyperband, BOHB
- Balance fidelity levels for efficiency
