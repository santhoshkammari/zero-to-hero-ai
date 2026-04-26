# Probability Calibration Findings

## The Problem
- Many classifiers output "confidence scores" that aren't true probabilities
- A model saying "80% confident" might only be right 60% of the time
- This matters enormously in healthcare, lending, any decision with thresholds

## Two Main Techniques

### Platt Scaling
- Fits logistic regression on top of classifier scores: P(y=1|f(x)) = 1/(1+exp(Af(x)+B))
- Originally for SVMs
- Assumes sigmoid relationship between scores and probabilities
- Works well with limited data, fewer parameters to fit

### Isotonic Regression
- Non-parametric: fits piecewise-constant non-decreasing function
- More flexible — no functional form assumption
- Needs more data to avoid overfitting
- scikit-learn's CalibratedClassifierCV uses this

## Which Classifiers Need It?
- SVMs: definitely (outputs aren't probabilities at all)
- Random Forests: tend to push predictions toward 0.5
- Gradient Boosting: often over-confident
- Logistic Regression: usually well-calibrated already
- Neural Networks: often over-confident after training

## Reliability Diagrams
- Plot predicted probability vs actual frequency in bins
- Perfect calibration = diagonal line
- Most useful diagnostic tool

## Key Insight
- Calibration is a post-processing step — train model first, calibrate second
- Always use held-out data for calibration (never training set)
