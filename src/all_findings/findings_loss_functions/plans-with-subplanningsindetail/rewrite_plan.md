# Rewrite Plan: Loss Functions Section

## Running Example: House Price Predictor
A tiny model predicting house prices. Start with 3 houses. Use this throughout to show how different losses react to the same errors.

## Concept Ladder (dependency order):
1. What "wrong" means — the loss function as your model's value system
2. The landscape metaphor — loss as terrain the optimizer walks
3. MSE — via toy example, then Gaussian MLE derivation
4. MAE — same toy example, different philosophy, Laplace connection
5. Huber — bridging the two, δ parameter
6. REST STOP — regression losses complete
7. Binary Cross-Entropy — from gambling/betting perspective
8. Why log? — information theory surprise
9. Categorical Cross-Entropy — extension to K classes
10. KL Divergence connection
11. Numerical stability — the _with_logits imperative
12. Focal Loss — when easy examples drown signal
13. REST STOP 2 — classification losses complete
14. Beyond standard: contrastive, triplet, quantile
15. Hinge loss, ranking losses, knowledge distillation
16. The decision rule
17. PyTorch patterns
18. Wrap-up

## Analogies (recurring):
1. Loss as landscape/terrain — optimizer hiking downhill
2. Loss as a judge's scoring rubric — different judges, different winners
3. The gambling/betting metaphor for probability losses

## Vulnerability moments:
1. Opening: avoided thinking deeply about loss functions
2. MSE section: "I used MSE everywhere for years without thinking"
3. Cross-entropy: "the log confused me for a long time"
4. Focal loss: "I still need to look up whether gamma should be 2 or 5"
5. Custom losses: "I'm still developing intuition for when standard losses aren't enough"
