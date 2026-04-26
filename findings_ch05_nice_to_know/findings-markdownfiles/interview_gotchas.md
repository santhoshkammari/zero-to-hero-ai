# Supervised Learning Interview Gotchas

## GLMs
- Link function confusion: it maps linear predictor → mean of response, not the other way
- Logistic regression IS a GLM (binomial family, logit link)
- Feature scaling matters for numerical stability and regularization fairness

## Quantile Regression
- Uses asymmetric "pinball" loss, not squared error
- Median regression (τ=0.5) is more robust to outliers than mean regression
- Different quantiles can cross if fit independently — quantile crossing problem

## Online Learning
- Standard k-fold CV doesn't work — use progressive/prequential validation
- "Regret" measures cumulative loss vs best fixed policy in hindsight
- Concept drift: distribution changes over time, model must adapt
- partial_fit() in scikit-learn for incremental updates

## Survival Analysis
- Can't drop censored observations — introduces survivorship bias
- Informative vs non-informative censoring changes everything

## Calibration
- Random Forests tend to push probabilities toward 0.5
- Neural networks tend toward overconfidence
- Always calibrate on held-out data, never training data

## Multi-label
- softmax ≠ sigmoid: using softmax for multi-label forces mutual exclusivity
- Hamming loss, not accuracy, is the right metric
