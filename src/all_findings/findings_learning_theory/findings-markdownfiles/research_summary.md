# Learning Theory Foundations - Research Summary

## Key Topics & Insights

### PAC Learning
- Valiant 1984, "Probably Approximately Correct"
- Two knobs: epsilon (accuracy), delta (confidence)
- Sample complexity: m >= (1/ε) ln(|H|/δ) for finite H
- Log dependence on |H| is the key insight - learning feasible even with huge classes
- Realizable vs Agnostic: realizable assumes truth in H, agnostic doesn't (1/ε² instead of 1/ε)

### VC Dimension
- Measures capacity of infinite hypothesis classes
- Shattering: H shatters m points if it can realize every possible labeling
- VC dim = largest m that can be shattered
- Linear classifiers in d dims: VC dim = d+1
- Replaces |H| in sample complexity bounds
- Key: infinite class can be learned with finite samples if VC dim is finite

### Rademacher Complexity
- Data-dependent alternative to VC dimension
- Measures how well H can fit random noise on actual data
- Tighter bounds because they incorporate data geometry
- Bound: L_true ≤ L_train + 2·R̂_m(H) + sqrt(ln(1/δ)/(2m))

### No Free Lunch Theorem
- Wolpert 1996
- No single algorithm best for all problems
- Averaged over all possible distributions, all algorithms equal
- Domain knowledge is crucial - success comes from matching methods to problems

### Bias-Complexity Tradeoff
- True Error ≤ Approximation Error + Estimation Error
- Approximation error (bias): best possible in H
- Estimation error (variance): gap from best to what you find with finite data
- SRM: nested sequence of increasingly complex classes, minimize train error + penalty

### Double Descent
- Belkin et al 2019
- Error curve is not U-shaped but double-descent shaped
- Three regimes: under-parameterized, interpolation threshold (worst), over-parameterized
- Past interpolation, more params → better generalization
- Observed in random features, trees, deep nets, epoch-wise

### Neural Tangent Kernel (NTK)
- Jacot et al 2018
- Infinite-width networks behave like kernel methods (linear regression in feature space)
- Training dynamics become linear - weights barely move from init
- No feature learning in NTK regime
- Explains convergence but not why finite-width nets learn representations

### Grokking
- Power et al 2022
- Delayed generalization: model memorizes first, then suddenly generalizes
- Phase transition after extended training
- Weight decay/regularization speeds it up
- Competing solutions: memorization (fast) vs algorithmic solution (slow)

### Benign Overfitting
- Bartlett et al 2020
- Overparameterized model fits data exactly (including noise) yet generalizes
- Noise gets spread across many irrelevant dimensions
- Minimum-norm solution key mechanism

### Implicit Regularization
- GD without explicit regularization still finds "simple" solutions
- Linear models: converges to minimum norm
- Deep nets: more complex, active research
- SGD acts as if regularized
