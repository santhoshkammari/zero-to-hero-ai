# Plan: Ensemble Methods Section Rewrite

## Running Example: Predicting House Prices
- Start with 5 houses, grow to realistic dataset
- Single tree → bagging → random forest → boosting → gradient boosting → modern libs

## Concept Ladder
1. The problem with single trees (unstable, high variance)
2. The committee idea (many opinions > one)
3. Bootstrap sampling (creating diverse training sets)
4. Bagging (train independently, average)
5. Random Forest (add feature subsampling for decorrelation)
6. OOB score, feature importance
7. REST STOP
8. Boosting philosophy (sequential, fix mistakes)
9. AdaBoost (reweight samples)
10. Gradient boosting (fit residuals = gradient descent in function space)
11. Learning rate / shrinkage
12. XGBoost (regularized, production-grade)
13. LightGBM (leaf-wise, GOSS, fastest)
14. CatBoost (ordered boosting, categorical specialist)
15. Comparison
16. Stacking
17. Production considerations
18. The standard pattern (LightGBM + early stopping + CV)

## Recurring Analogies
1. Committee of experts (each with different expertise/perspective) - used throughout
2. Hiking down a valley (gradient boosting as gradient descent in function space)

## Vulnerability Moments
1. Opening: avoided ensemble methods, used single models for too long
2. Feature importance trap: got burned by MDI in production
3. Gradient boosting: "gradient descent in function space" took a while to click
4. Stacking: the diminishing returns surprise
5. Still developing intuition for when CatBoost vs LightGBM

## Style: Brandon Rohrer
- Personal confession opening
- Build from scratch with toy examples
- Name concepts AFTER showing them work
- Show limitations that motivate next section
- Rest stop with permission to leave
- Wrap-up with gratitude and future hope
