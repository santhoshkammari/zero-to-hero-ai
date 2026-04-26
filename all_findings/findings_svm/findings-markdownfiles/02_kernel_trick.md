# The Kernel Trick

## Core Insight
- SVM dual form only needs dot products between data points
- Kernel K(x_i, x_j) = φ(x_i) · φ(x_j) — computes dot product in high-dim space without mapping
- Never need to compute φ(x) explicitly

## Mercer's Theorem
- Any continuous, symmetric, positive semi-definite function K can be decomposed as inner product in some Hilbert space
- Guarantees that a valid kernel implicitly corresponds to some feature space
- Foundation for why the kernel trick is mathematically sound

## RBF Kernel and Infinite Dimensions
- K(x,y) = exp(-γ||x-y||²)
- Taylor expansion of the exponential produces infinite series
- Each term corresponds to a basis function in the feature space
- The implied feature space is literally infinite-dimensional
- Yet computing K(x,y) takes O(d) time where d = original dimensions

## Common Kernels
- Linear: K(x,y) = x·y — no mapping, good for sparse high-dim data
- Polynomial: K(x,y) = (γx·y + r)^d — all polynomial interactions up to degree d
- RBF/Gaussian: K(x,y) = exp(-γ||x-y||²) — infinite-dim, the default choice
- Sigmoid: K(x,y) = tanh(γx·y + r) — rarely used, not always valid Mercer kernel

## Gamma Parameter (RBF)
- γ = 1/(2σ²) where σ is Gaussian bandwidth
- High γ: narrow Gaussian, each point influences only nearby points → complex boundary
- Low γ: wide Gaussian, each point has broad influence → smooth boundary
- Default sklearn: γ = 1/(n_features * var(X)) when gamma='scale'
