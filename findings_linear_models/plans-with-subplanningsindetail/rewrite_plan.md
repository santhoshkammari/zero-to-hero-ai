# Rewrite Plan: Linear Models (ch05/s01)

## Approach: Brandon Rohrer style — build from scratch, running example, vulnerability

## Running Example: Predicting whether a coffee shop will survive its first year
- Start with one feature (foot traffic), grow to many
- Naturally transitions from regression (predicted revenue) to classification (survive/fail)
- Relatable, concrete, scales naturally

## Concept Ladder (dependency order):
1. Opening: personal confession about avoiding linear models thinking they're "too basic"
2. What "linear" actually means — linear in parameters, not features
3. One feature: fitting a line (the house price intuition → coffee shop revenue)
4. The loss: why squared errors, connection to Gaussian MLE
5. Normal equation: the closed-form magic and when it breaks
6. Gradient descent: when the matrix is too big
7. **REST STOP** — you now have a working regression model
8. Regularization: the geometry of L1/L2/ElasticNet
9. Bayesian interpretation of regularization
10. From regression to classification: the sigmoid from log-odds
11. Log-loss: why MSE fails for classification
12. Decision boundaries and odds ratios
13. **REST STOP** — you can now build and interpret both models
14. The GLM framework: the unifying view
15. Perfect separation, calibration, multiclass
16. Production gotchas
17. Wrap-up

## Vulnerability Moments:
- "I dismissed linear models for years as too basic"
- "The L1 sparsity geometry took me embarrassingly long to internalize"
- "I still get confused by sklearn's C vs alpha parameterization"
- "I'm still building intuition for when ElasticNet actually beats pure Lasso"
- "Perfect separation bit me in production before I understood what was happening"

## Analogies:
- Loss landscape as a physical terrain (bowl, valley, canyon)
- Regularization as a budget constraint on a shopping trip
- Sigmoid as a dimmer switch (not binary on/off)
