# Linear Regression Foundations

## Core Insight: "Linear" means linear in PARAMETERS, not features
- y = w₀ + w₁x² + w₂sin(x) is still "linear regression" because w's appear linearly
- Polynomial regression is a linear model. This trips up everyone.
- The geometry: you're always fitting a hyperplane in the (possibly transformed) feature space

## Normal Equation vs Gradient Descent
- Normal equation: w = (XᵀX)⁻¹Xᵀy — exact, one-shot, O(p³) for inversion
- Fails when: XᵀX is singular (multicollinearity, p > n), ill-conditioned (nearly collinear)
- Numerical stability: never invert directly; use QR decomposition or SVD in practice
- Ridge's λI trick: makes XᵀX + λI always invertible — regularization as numerical rescue
- GD: O(npk) for k iterations, scales to millions of features, needs feature scaling

## Why Squared Error?
- Convex → single global minimum
- Differentiable everywhere → smooth optimization
- MLE connection: if errors are Gaussian, minimizing MSE = maximizing likelihood
- Gauss-Markov: under LINE assumptions, OLS is BLUE (Best Linear Unbiased Estimator)

## Assumptions (LINE) — Why they matter in production
- Linearity: residuals-vs-fitted shows curves → model is structurally wrong
- Independence: time series residuals correlated → standard errors are lies
- Normality: least important for prediction, matters for confidence intervals
- Equal variance (homoscedasticity): funnel in residuals → use WLS or robust SE
