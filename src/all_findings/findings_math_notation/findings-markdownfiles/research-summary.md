# Mathematical Notation Research Summary

## Key Insights from Web Research

### 1. The Core Problem for ML Engineers
- Math notation is a compressed language — programmers struggle because code is explicit, math omits "obvious" details
- Same symbols get overloaded across papers (x can be scalar, vector, matrix depending on context)
- Subscripts/superscripts carry 3+ different meanings: indexing, time steps, exponents, transposes
- Papers abuse notation constantly — even experts get confused

### 2. The Symbol Categories That Matter Most
1. **Scalar/Vector/Matrix conventions** — lowercase, bold lowercase, bold uppercase (but not all papers follow this)
2. **Greek letters** — θ (params), α (learning rate), λ (regularization), σ (std dev + sigmoid), ∇ (gradient)
3. **Blackboard bold** — ℝ (reals), 𝔼 (expectation), ℙ (probability)
4. **Calligraphic** — 𝒩 (normal dist), 𝒟 (dataset), ℒ (loss), 𝒳/𝒴 (spaces)
5. **Hat/tilde/bar decorators** — ŷ (predicted), x̄ (mean), x̃ (noisy/augmented)
6. **Operators** — argmin/argmax, ∑/∏, ∂/∇, ‖·‖ (norms)

### 3. Einstein Summation (einsum)
- Repeated indices = implicit summation
- Core to modern deep learning — attention mechanisms, tensor contractions
- np.einsum / torch.einsum are the code equivalents
- 'ij,jk->ik' = matrix multiplication — j appears in both inputs but not output, so summed over

### 4. Matrix Calculus for Backprop
- Gradient: ∇f is column vector of partial derivatives
- Jacobian: matrix of all partial derivatives for vector-to-vector functions
- Hessian: matrix of second derivatives
- Numerator vs denominator layout — huge source of confusion
- Chain rule in matrix form is what backpropagation actually computes

### 5. Norm Notation
- ‖x‖₁ = L1 (Manhattan), ‖x‖₂ = L2 (Euclidean), ‖A‖_F = Frobenius
- Double bars always mean some kind of "size" measurement
- L1 regularization → sparsity, L2 regularization → small weights

### 6. Probability Notation
- p(x|y) = conditional probability/density
- X ~ 𝒩(μ, σ²) = "X is distributed as Normal with mean μ, variance σ²"
- 𝔼[X] = expectation, Var(X) = variance
- The ∝ symbol means "proportional to" — used constantly in Bayesian ML

### 7. Common Pitfalls in Interviews
- Not being able to read argmin/argmax fluently
- Confusing subscript conventions across papers
- Not knowing that hat (^) means "estimated" not "exponent"
- Mixing up p(x) as probability vs p times x
- Not recognizing einsum patterns
