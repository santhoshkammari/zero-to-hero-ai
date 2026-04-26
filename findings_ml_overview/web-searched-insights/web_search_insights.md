# Web Search Insights — ML Overview & Workflow

## Search 1: End-to-End ML Pipeline (2024 Best Practices)
- 10-step pipeline from problem definition to iteration
- Key 2024 trends: MLOps adoption, data-centric ML, responsible AI, automated testing
- Data versioning (DVC, MLflow) now standard practice
- Model explainability (SHAP, LIME) is a required step, not optional

## Search 2: Inductive Bias
- Every algorithm must have bias to generalize — this is mathematically necessary
- Linear regression: linearity assumption. Decision trees: axis-aligned splits. NNs: compositionality
- CNNs bias toward spatial locality. Transformers bias toward attention patterns
- The "right" bias matches the structure of your problem

## Search 3: No Free Lunch Theorem
- Averaged over ALL possible problems, every algorithm performs equally
- Practical meaning: experimentation is mandatory, domain knowledge is your edge
- Connects to inductive bias — NFL is WHY bias matters
- Ensembles help because different models make different assumptions

## Search 4: Self-Supervised vs Semi-Supervised
- Self-supervised: creates own labels from data structure (GPT predicts next word, MAE masks image patches)
- Semi-supervised: uses small labeled set + large unlabeled set
- Both reduce reliance on expensive human annotation
- Self-supervised powers all modern foundation models

## Search 5: Data Leakage Real-World Examples
- Hospital ICU model included "time to ICU admission" — only known after admission
- Bank used "number of overdue payments in next year" for loan default prediction
- Kaggle competitions regularly surface leakage in public datasets
- Prevention: split before everything, use pipelines, audit feature importances

## Search 6: When NOT to Use ML
- If rules are clear and stable, use if/else
- If data is insufficient or noisy, rules work better
- Start simple → add ML when rules break down
- Hybrid approaches (rules as front-line filter, ML for ambiguous cases) very common

## Search 7: Generalization Theory
- PAC: "probably approximately correct" — enough data → high probability of good generalization
- VC dimension measures model capacity/flexibility
- Higher VC dimension → need more data to generalize
- Occam's Razor: prefer simpler models unless data justifies complexity

## Search 8: RL Fundamentals
- Agent-environment interaction loop with reward signals
- Policy = strategy, Value function = expected future reward
- Exploration vs exploitation tradeoff is central
- Practical applications: games, robotics, resource allocation with simulators
