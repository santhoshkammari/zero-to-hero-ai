# Gradient Boosting

## Core Insight: Gradient Descent in Function Space
- Not adjusting parameters, building up a function step by step
- Each tree fits pseudo-residuals = negative gradient of loss w.r.t. predictions
- For MSE: residuals = y - F(x), which IS the negative gradient
- For other losses: compute actual gradient → pseudo-residuals
- Framework generalizes to ANY differentiable loss

## Hiking Analogy
- Hiking down a valley in function space
- Each iteration: find direction (tree shape) that best reduces loss
- Take a step (add tree with learning rate)

## Key Differences from Bagging
- Bagging: parallel, reduces variance
- Boosting: sequential, reduces bias
- Boosting can overfit (unlike RF where more trees never hurts)
- Early stopping is non-negotiable
