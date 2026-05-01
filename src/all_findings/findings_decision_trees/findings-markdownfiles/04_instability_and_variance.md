# Instability & The Variance Problem

## Why Trees Are Unstable
- Greedy splits compound: change first split → entire tree changes
- Near-ties between features flip easily with small data changes
- Smaller datasets amplify instability
- High variance, low bias model

## The Cascade Effect
- Top split has huge downstream impact
- Feature A: 0.51 gain vs Feature B: 0.49 gain — one data point can flip
- Every subsequent split in those branches becomes different

## Why This Matters
- This instability is the RAW MATERIAL for ensemble methods
- Bagging (Random Forests): average many diverse trees → reduces variance
- Boosting (Gradient Boosting): each tree corrects previous errors
- Without variance, there's nothing to average out

## Oblique Trees
- Standard trees: axis-aligned splits only (staircase boundaries)
- Oblique trees: linear combinations of features (diagonal cuts)
- More compact but harder to interpret, more expensive to train
- Rarely used in practice — ensembles of axis-aligned trees work better
