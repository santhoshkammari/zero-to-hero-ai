# Learning Rate Schedules and Convergence Challenges

## Schedules
- **Step decay**: multiply LR by factor at fixed epochs (older, manual)
- **Cosine annealing**: smooth cosine curve decay, no jumps, modern default
- **Warmup**: start tiny, linearly increase for first 5-10% of training — stabilizes early when params are random
- **One-cycle (Leslie Smith)**: ramp up to max then anneal below start — matches tuned schedules with zero decisions
- Modern recipe: warmup + cosine decay (used by GPT, BERT, ViT)

## Saddle Points vs Local Minima
- In high dimensions, true local minima are astronomically rare
- For a critical point to be a local minimum, loss must curve upward in ALL directions — virtually impossible in millions of dims
- Almost every critical point is a saddle point
- SGD noise provides enough perturbation to escape saddle points

## Sharp vs Flat Minima
- Sharp: narrow steep valley, small param changes → large loss changes, poor generalization
- Flat: broad basin, robust to perturbation, better generalization
- Large batch → sharp minima (bad), small batch → flat minima (good)
- SAM (Sharpness-Aware Minimization): explicitly seeks flat minima by considering worst-case loss in neighborhood

## Gradient Clipping
- Prevents exploding gradients (especially in RNNs, early transformer training)
- Global norm clipping: if gradient norm > threshold, scale down proportionally
- Default: max_norm=1.0, essentially free insurance
- Always clip AFTER backward(), BEFORE optimizer.step()

## Backpropagation ≠ Gradient Descent
- Gradient descent: WHAT to do with gradients (optimization algorithm)
- Backpropagation: HOW to compute gradients efficiently (chain rule applied backward)
- Without backprop: finite differences — N forward passes for N parameters
- With backprop: one backward pass for all gradients — O(1) vs O(N)

## Second-Order Methods
- Newton's method: uses Hessian (curvature), quadratic convergence near minimum
- Problem: Hessian is n×n matrix — 100 trillion entries for 10M params
- L-BFGS: approximates inverse Hessian with last k gradient updates
- Good for <100K params with full-batch; scikit-learn's default for logistic regression
- Impractical for deep learning (doesn't work with stochastic mini-batches)
