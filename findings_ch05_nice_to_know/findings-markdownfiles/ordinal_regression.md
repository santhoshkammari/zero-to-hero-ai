# Ordinal Regression Findings

## Core Problem
- Categories have natural order (star ratings 1-5, pain low/med/high) but gaps between categories aren't equal
- Standard classification: treats "predict 1 when truth is 5" same as "predict 4 when truth is 5" — absurd
- Standard regression: assumes equal spacing between categories — also wrong

## Threshold (Proportional Odds) Model
- Assumes latent continuous variable divided by K-1 thresholds
- P(Y ≤ k) = sigmoid(θ_k - w^T x) — learns both weights and thresholds
- Does NOT assume equal distance between categories
- Output: ordered probabilities

## Alternative Approaches
- Multiple binary classifiers: train K-1 classifiers for P(Y > k)
- Ordinal loss functions: penalize larger errors more (MAE-style)
- CORAL: Consistent Rank Logits — deep learning approach

## Libraries
- mord (Python), statsmodels, R's polr/ordinal
- scikit-learn lacks native ordinal regression

## Key Insight
- The threshold model is elegant: it says "there's a hidden continuous score, and the categories are just bins along that score"
