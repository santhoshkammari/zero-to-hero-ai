# Regression, MCC, and Production Metrics — Deep Findings

## Regression
- MAE: treats all errors equally, robust to outliers, easy to explain
- RMSE: squares errors → 100K miss contributes 100x more than 10K miss
- R²: proportion of variance explained, can be negative (worse than mean)
- Adjusted R² penalizes adding useless features
- MAPE: business-friendly "off by X%" but explodes near zero

## MCC
- Uses ALL FOUR confusion matrix cells (F1 ignores TN)
- Range: -1 to +1, 0 = random
- Treats both classes symmetrically
- A model predicting all negatives gets MCC=0 (correctly signals useless)
- Same model might get deceptive accuracy of 99%
- Hard to game — must perform well on BOTH classes

## Production / Goodhart's Law
- "When a measure becomes a target, it ceases to be a good measure"
- Optimizing CTR → clickbait, not value
- Offline metrics are first filter, online A/B tests give real answer
- Offline and online metrics WILL disagree — trust online
- Need guardrail metrics alongside primary metrics
