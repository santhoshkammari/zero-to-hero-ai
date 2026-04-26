# XGBoost vs LightGBM vs CatBoost

## XGBoost
- Regularization in objective (L1/L2 on leaf weights)
- Histogram-based splitting
- Native missing value handling (learns direction)
- Column subsampling
- GPU + distributed training

## LightGBM
- Leaf-wise growth (always split leaf with max loss reduction)
- GOSS: keep all large-gradient samples, subsample small-gradient ones
- Native categorical support
- Fastest training on CPU
- Risk: overfitting on small datasets (deeper asymmetric trees)

## CatBoost
- Ordered target encoding (no target leakage by construction)
- Ordered boosting (computes residuals on different subsets → no prediction shift)
- Symmetric trees by default
- Best defaults out of box
- Slowest to train

## 2024 Benchmarks (10M rows)
- LightGBM: 20s, AUC 0.792
- XGBoost: 40s, AUC 0.757
- CatBoost: 70s, AUC 0.735

## Why GBMs Beat Neural Nets on Tabular
- Axis-aligned splits match tabular data structure
- Native categorical/missing handling
- Sample efficient (most tabular datasets are moderate size)
- Faster, easier to tune
- TabNet, FT-Transformer still rarely beat tuned GBMs
