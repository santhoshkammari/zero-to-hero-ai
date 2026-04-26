# Key Web-Searched Insights

1. Normal equation uses O(p³) for matrix inversion — infeasible above ~10k features
2. Never invert XᵀX directly; use QR/SVD decomposition for numerical stability
3. Ridge's λI makes matrix always invertible — regularization serves double duty
4. L1 sparsity from diamond geometry: subdifferential at corners allows zero solutions
5. Bayesian view: Ridge = Gaussian prior, Lasso = Laplace prior, both are MAP estimation
6. ElasticNet's grouping effect: correlated features stay together, solving Lasso instability
7. IRLS for logistic regression: Newton-Raphson = iterative weighted least squares
8. Fisher scoring and Newton-Raphson coincide for logistic regression specifically
9. Perfect separation: MLE diverges, coefficients → ±∞, regularization fixes it
10. GLM framework unifies all linear models: same engine, different link functions
11. "Linear" means linear in parameters — polynomial regression IS linear regression
12. Logistic regression calibration is free from optimizing log-loss (proper scoring rule)
