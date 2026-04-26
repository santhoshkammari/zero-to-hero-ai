# Rewrite Plan for ch01/s12.html - Scikit-learn

## Running Example
Building a house price predictor - starts tiny (3 houses, 2 features), grows organically

## Concept Ladder
1. The Problem: ML code without consistency (motivate why sklearn exists)
2. The Contract: fit/predict/transform - the three verbs
3. Why this works - underscore convention, get_params, clone
4. Pipelines - chaining steps, preventing leakage
5. ColumnTransformer - different columns, different treatments
6. Custom Transformers - building your own pipeline-compatible pieces
7. Model Selection - cross-validation, grid search internals
8. REST STOP
9. Production Patterns - serialization, schema validation, set_output
10. Where Scikit-learn Ends - limitations, when to move on

## Analogies
1. LEGO bricks - all same connector system (the API), different functions
   - Reuse: custom transformers are custom LEGO bricks
2. Assembly line / factory - Pipeline as conveyor belt
   - Reuse: ColumnTransformer as parallel assembly lines merging

## Vulnerability Moments
1. Opening: "I used sklearn for years before understanding WHY fit and transform are separate"
2. "I'll be honest - I caused data leakage for months before pipelines clicked"
3. "The underscore convention seemed like a quirk until I saw what clone() does with it"
4. "I still get tripped up by when to use FunctionTransformer vs a custom class"
