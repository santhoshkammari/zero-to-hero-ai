# Section Plan: Feature Selection & Data Splitting

## Running Example
Building a credit card fraud detection system - starts tiny (6 customers, 4 features), grows naturally.

## Concept Ladder
1. Why not use all features? (curse of dimensionality intuition)
2. Filter methods - variance, correlation, mutual information
3. The MI vs correlation distinction (nonlinear relationships)
4. Wrapper methods - RFE (and why it's expensive)
5. Embedded methods - L1/Lasso geometry, tree importance
6. REST STOP - you now know how to select features
7. Why splitting matters - the sealed envelope analogy
8. Train/val/test - three distinct jobs
9. Data leakage - the silent killer
10. Stratified splits - preserving distributions
11. Time-based splits - never peek at the future
12. Group-based splits - entity-level isolation
13. Cross-validation - when one split isn't enough

## Recurring Analogies
1. **Sealed envelope** - test set is a sealed envelope, open once
2. **Kitchen pantry** - features are ingredients, too many spoils the dish
3. **Crime scene** - leakage contaminates evidence

## Vulnerability Moments
1. Admit: spent weeks debugging a model that had leakage
2. Confess: MI feels like magic, still building intuition
3. Acknowledge: L1 geometry is hard to visualize beyond 2D
4. Share: time-based splits feel wasteful but are non-negotiable
