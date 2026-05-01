# Synthetic Data Generation & Tabular Augmentation

## Synthetic Data (SDV/CTGAN)
- SDV library with CTGAN, GaussianCopula, TVAE models for tabular data
- CTGAN handles mixed types (numeric + categorical) well
- Fundamental limitation: synthetic data only captures known patterns, can't surprise with real-world edge cases
- Use cases: privacy-sensitive data, scarce training data, testing pipelines

## Tabular Data Augmentation
- **Mixup**: interpolate between two samples (features and labels) — promotes smoother decision boundaries
  - Caution: don't mix categorical features arithmetically
- **Feature noise (jittering)**: add small Gaussian noise to continuous features
  - Keep noise proportional to feature's natural variance
- **Row dropout**: randomly mask features to simulate missing data
- **Random swap**: swap values within same class for categorical features

## Key Insight
- Unlike images (flip, rotate, crop), tabular augmentation is harder because feature semantics matter
- Mixup works but requires care with categoricals
- Always validate augmented data doesn't hurt performance on real test data
