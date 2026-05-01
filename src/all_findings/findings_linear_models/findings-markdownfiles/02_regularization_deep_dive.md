# Regularization Deep Dive

## The Geometry That Explains Everything
- L1 constraint region: diamond with sharp corners on axes → loss contours hit corners → sparsity
- L2 constraint region: smooth circle → contours touch anywhere → no exact zeros
- At L1 corners: subdifferential is large, multiple subgradients support the minimum, coefficients "snap" to zero

## Bayesian Interpretation
- Ridge = MAP estimation with Gaussian prior N(0, τ²) on weights → "I believe weights are probably small"
- Lasso = MAP estimation with Laplace prior on weights → "I believe most weights are exactly zero"
- The penalty term IS the negative log of the prior
- λ controls prior strength: large λ = strong prior belief that weights are small

## ElasticNet: The Grouping Effect
- Lasso with correlated features: arbitrarily picks one, zeros others. Unstable across data splits.
- ElasticNet's L2 component forces correlated features to share coefficients (grouping effect)
- Practical l1_ratio: start at 0.5, tune with CV. Low correlation → higher l1_ratio, high correlation → lower
- Zou & Hastie (2005): "ElasticNet encourages a grouping effect where strongly correlated predictors tend to be in or out of the model together"

## Regularization Path
- Plot coefficients vs λ: visualize when features enter/leave the model
- Lasso path shows sharp transitions to zero
- Ridge path shows gradual shrinkage, never reaching zero
- Critical for feature importance storytelling
