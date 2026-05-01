# ROC-AUC vs PR-AUC — Deep Findings

## ROC-AUC Intuition
- Probabilistic interpretation: probability that random positive scores higher than random negative
- AUC=0.5 is random, AUC=1.0 is perfect
- Invariant to class imbalance ratio (which is both strength AND weakness)

## Why ROC Misleads on Imbalanced Data
- FPR = FP/(FP+TN) — when TN is enormous, FPR stays tiny even with many false positives
- 500 false positives out of 99,000 negatives = 0.5% FPR but 500 false alarms
- ROC "rewards" getting countless negatives right
- The curve looks great even when positive class performance is mediocre

## PR-AUC Advantage
- Precision ignores TN — focuses entirely on positive class performance
- Baseline is class prevalence (1% for fraud), not 50% — makes differences visible
- A model predicting all negatives gets PR-AUC ≈ class prevalence (terrible)
- Same model gets ROC-AUC that can look decent

## Key Paper
- Saito & Rehmsmeier (2015): "The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets"
