# Cross-Validation Core Findings

## Why CV Exists
- Single train/test split is unreliable — score depends on which examples land where
- CV provides a distribution of scores, not one lucky number
- Every data point gets used for both training and testing

## K-Fold Bias-Variance of the Estimator
- k=5: 80% training data per fold, slightly higher bias, lower variance
- k=10: 90% training data per fold, lower bias, moderate variance
- Kohavi (1995) empirically showed 10-fold is slightly more accurate and stable
- k=5 is the practical default; k=10 for final reporting

## LOOCV Paradox
- Low bias (trains on n-1 samples) but HIGH variance as an estimator
- Why? Training sets overlap almost entirely, making fold scores highly correlated
- A single influential point can dramatically swing the estimate
- Practical: 5-fold or 10-fold beats LOOCV for most use cases

## Stratified K-Fold
- Preserves class distribution in each fold
- Critical for imbalanced datasets (fraud detection, cancer diagnosis, churn)
- sklearn silently uses stratified when you pass cv=5 for classifiers

## Time Series Split / Walk-Forward
- Must respect temporal ordering — no shuffling
- Expanding window: train on past, test on future
- Purged CV (López de Prado): removes observations whose label windows overlap test set
- Embargo: excludes additional samples after test set for delayed leakage

## Nested CV
- Outer loop: unbiased evaluation
- Inner loop: hyperparameter tuning
- Prevents the subtle bias of reporting the "best CV score" as expected performance
- Gold standard when tuning + reporting in same experiment

## Preprocessing Leakage
- The #1 practical mistake: fit scaler/encoder on full data before splitting
- Correct: use Pipeline so fit happens inside each fold
- Real-world horror stories: healthcare sepsis model, Kaggle competition disqualifications

## Group K-Fold
- For data with natural groups (patients, users, devices)
- Prevents model from "recognizing" the source instead of the pattern
