# Density Estimation & KDE

## What it is
- Non-parametric estimation of the probability density function
- Place a smooth kernel (often Gaussian) on each data point, sum them up
- Bandwidth parameter controls smoothness — too small = noisy, too large = oversmoothed

## Where it connects to unsupervised learning
- Foundation of Mean-Shift clustering (find density peaks)
- Anomaly detection: low-density regions = anomalies
- Generative modeling: sample from the estimated density

## Practical gotchas
- Curse of dimensionality: KDE degrades badly above ~5 dimensions
- Bandwidth selection is critical — use cross-validation or Scott's/Silverman's rule
- Slow for large datasets (O(n) per query point) — approximations exist (KD-trees, ball trees)

## When to use
- Continuous, low-dimensional data
- EDA visualization (seaborn kdeplot)
- Likelihood estimation without parametric assumptions
- Building block for other algorithms (Mean-Shift, DBSCAN intuition)
