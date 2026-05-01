# SVM Mathematical Foundations

## Primal Form
- Minimize (1/2)||w||² subject to y_i(w·x_i + b) >= 1
- The constraint forces each point to be on the correct side of the margin
- Minimizing ||w||² is equivalent to maximizing margin = 2/||w||

## Geometric vs Functional Margin
- Functional margin: y_i(w·x_i + b) — raw score, scale-dependent
- Geometric margin: y_i(w·x_i + b) / ||w|| — actual distance, scale-invariant
- Support vectors sit at geometric margin = 1/||w||

## Dual Formulation
- Lagrangian: L = (1/2)||w||² - Σ α_i[y_i(w·x_i + b) - 1]
- Dual form: maximize Σα_i - (1/2)ΣΣ α_i α_j y_i y_j (x_i · x_j)
- Subject to: α_i >= 0 and Σ α_i y_i = 0
- KEY: Data only appears as dot products x_i · x_j — enables kernel trick

## KKT Conditions
- Complementary slackness: α_i[y_i(w·x_i + b) - 1] = 0
- If α_i > 0 → point is ON the margin → it IS a support vector
- If α_i = 0 → point is beyond margin → NOT a support vector
- w = Σ α_i y_i x_i (weight vector is linear combination of support vectors only)

## Why Dual is Preferred
1. Enables kernel trick (only needs dot products)
2. Sparse solution (most α_i = 0)
3. Number of variables = number of training points (can be smaller problem)

## Soft Margin and Hinge Loss
- Soft margin: minimize (1/2)||w||² + C Σ max(0, 1 - y_i(w·x_i + b))
- max(0, 1 - y_i f(x_i)) IS the hinge loss
- Equivalent to: L2 regularization + hinge loss minimization
- C = inverse regularization strength (high C = low regularization)

## Connection to Structural Risk Minimization
- SVM implements Vapnik's SRM principle
- Balances empirical risk (training error) with model complexity (VC dimension)
- Wider margin → lower effective VC dimension → better generalization bound
