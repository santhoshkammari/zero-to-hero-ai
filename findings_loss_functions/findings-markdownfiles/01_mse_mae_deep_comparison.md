# MSE vs MAE Deep Comparison

## Statistical Foundations
- MSE = MLE under Gaussian noise assumption. Minimizing MSE ≡ maximizing likelihood when errors ~ N(0,σ²)
- MAE = MLE under Laplacian noise. Minimizing MAE ≡ maximizing likelihood when errors ~ Laplace(0,b)
- MSE estimates the **mean** of conditional distribution; MAE estimates the **median**
- For symmetric distributions, mean = median. For skewed/heavy-tailed, median is more robust

## Gradient Behavior
- MSE gradient: 2(ŷ - y) — linear in error, smooth, differentiable everywhere
- MAE gradient: sign(ŷ - y) — constant magnitude ±1, undefined at zero
- MSE: large errors → large gradients → big updates (fast but dangerous with outliers)
- MAE: constant gradient regardless of error magnitude → oscillates near optimum

## Key Insight: The "Value System" Metaphor
- MSE thinks error of 10 is 100× worse than error of 1
- MAE thinks error of 10 is 10× worse than error of 1
- These are fundamentally different philosophies about what "wrong" means
- The model faithfully optimizes whichever philosophy you hand it

## Practical Decision
- Clean data, Gaussian-ish errors → MSE
- Outliers, heavy tails, corrupted labels → MAE or Huber
- Need median prediction → MAE
- Need mean prediction → MSE
