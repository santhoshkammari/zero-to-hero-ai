# Model Calibration — Deep Findings

## What Calibration Means
- A calibrated model's "80% confident" predictions are correct ~80% of the time
- AUC only measures ranking — doesn't care if 92% confidence maps to 40% truth
- Calibration matters when probabilities are USED (not just rankings)

## When It Matters
- Insurance pricing, medical test ordering, bid amounts, risk scoring
- Any downstream decision that uses the probability VALUE
- NOT needed when you only care about ranking (search, recommendations)

## Reliability Diagrams
- Bin predictions, plot mean predicted vs observed fraction positive
- Perfect calibration = points on diagonal
- Above diagonal = underconfident, below = overconfident

## Fixes
- Platt scaling: fit logistic regression to raw scores (good for sigmoid-like miscalibration)
- Isotonic regression: piecewise monotonic — more flexible but can overfit with small data
- Need held-out calibration set

## Log Loss Connection
- Log loss is a proper scoring rule — incentivizes honest probability reporting
- -log(0.99) ≈ 0.01 (right and confident = tiny penalty)
- -log(0.01) ≈ 4.6 (wrong and confident = devastating penalty)
- This is "surprisal" from information theory
