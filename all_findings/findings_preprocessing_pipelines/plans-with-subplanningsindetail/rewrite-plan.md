# Rewrite Plan for ch03/s06 - Preprocessing Pipelines

## Running Example
A loan approval system that starts with 3 columns (age, income, occupation) and grows as complexity demands.

## Concept Ladder (dependency order)
1. The Gap Problem — motivation via the "loose code" nightmare
2. What a Pipeline Actually Is — the assembly line analogy
3. Building Your First Pipeline — toy example with 3 steps
4. How fit/transform Chains Under the Hood — the internal mechanics
5. ColumnTransformer — the routing problem (mixed types)
6. Custom Transformers — when sklearn doesn't have what you need
7. REST STOP — you can build real pipelines now
8. The Leakage Trap — why pipelines + cross-validation matter
9. Pipeline + GridSearchCV — tuning across the entire chain
10. Production — serialization, feature stores, train-serve skew
11. Wrap-up

## Analogies (recurring)
1. Assembly line / factory floor — pipeline as sequential stations
2. Recipe card — fitted pipeline as a frozen set of instructions

## Vulnerability Moments
1. Opening confession about scattered preprocessing code
2. "I still forget remainder='drop' is the default" 
3. "I'm still developing my intuition for when FunctionTransformer isn't enough"
4. Admit the ColumnTransformer column ordering confused me initially
5. Data leakage: "I once shipped a model with leaked features"
