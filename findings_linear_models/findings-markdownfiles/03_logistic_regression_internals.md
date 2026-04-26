# Logistic Regression Internals

## Why Sigmoid? It's not arbitrary.
- Start from: log-odds are linear in features → log(p/(1-p)) = wᵀx + b
- Solve for p → you get the sigmoid. The math chose the function, not us.
- σ'(z) = σ(z)(1-σ(z)) — derivative from the function value itself, computationally free

## MLE and No Closed Form
- Log-likelihood: ℓ(β) = Σ[yᵢ log σ(zᵢ) + (1-yᵢ) log(1-σ(zᵢ))]
- Negative of this = cross-entropy loss. Same math, two names.
- Non-linear in β because of sigmoid → can't set derivatives to zero and solve
- Must iterate: GD, Newton-Raphson (IRLS), or L-BFGS

## IRLS: The Elegant Connection
- Newton-Raphson for logistic regression = repeatedly solving weighted least squares
- At each step: form working response z, solve WLS with weights W = diag(μᵢ(1-μᵢ))
- Fisher scoring and Newton-Raphson coincide for logistic regression
- This is why it's called "iteratively reweighted least squares"

## Perfect Separation
- When a linear combination of features perfectly predicts the outcome
- MLE diverges → coefficients go to ±∞
- Log-likelihood keeps increasing, never reaches maximum
- Fix: regularization (L2 penalty), or Firth's penalized likelihood
- sklearn symptom: "LBFGS failed to converge" + absurdly large coefficients

## Calibration: The Hidden Superpower
- Logistic regression is naturally calibrated because it directly optimizes log-loss (a proper scoring rule)
- "70% probability" means ~70% of those cases are actually positive
- RF, SVM, NB all need post-hoc calibration (Platt scaling, isotonic regression)
- Critical in production: insurance pricing, medical triage, fraud thresholds
