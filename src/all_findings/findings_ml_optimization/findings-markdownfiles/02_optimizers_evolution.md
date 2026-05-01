# Optimizer Evolution

## Momentum
- Keeps running average of past gradients (velocity)
- Dampens oscillations across steep directions, accelerates along consistent direction
- β=0.9 typical (EMA of last ~10 gradients)
- Nesterov: evaluate gradient at lookahead position, catches overshooting sooner

## Adaptive Methods
- Core insight: different parameters need different learning rates
- Sparse features (rare words) vs frequent features (common words) example

### AdaGrad
- Sum of squared gradients per parameter
- Great for sparse problems but fatal flaw: cache only grows, LR decays to zero

### RMSprop
- Hinton's fix: EMA of squared gradients instead of sum
- Never formally published (Coursera lecture!)
- Direct ancestor of Adam

### Adam
- Momentum + RMSprop + bias correction
- First moment m (momentum), second moment v (RMSprop)
- Bias correction: divides by (1-β^t) to fix zero-initialization bias early on
- Default β1=0.9, β2=0.999, ε=1e-8

### AdamW (Loshchilov & Hutter 2019)
- Decoupled weight decay from gradient update
- In Adam+L2: the L2 penalty gets scaled by adaptive learning rates → inconsistent regularization
- In AdamW: weight decay applied directly to weights, independent of moment estimates
- Better generalization, easier to tune
- This is what you should actually use

## When to Use What
- Adam/AdamW: default for everything, especially NLP/transformers
- SGD+momentum: vision tasks when you have time to tune LR schedule, sometimes better generalization
- Hybrid: pretrain with Adam, fine-tune with SGD
