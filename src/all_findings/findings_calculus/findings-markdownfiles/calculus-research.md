# Calculus for ML — Research Findings

## Key Insights from Web Research

### Chain Rule & Backpropagation
- Backpropagation IS the chain rule applied systematically — nothing mystical
- Neural nets are compositions of functions: layer after layer
- Each layer computes a local derivative; the chain rule multiplies them together
- The Rube Goldberg machine analogy: changing something at the start ripples through mechanisms
- Cost: roughly 2x forward pass (one forward, one backward)

### Gradients & Loss Landscapes  
- Loss landscape = mountainous terrain where height = loss, coordinates = parameters
- Gradient points uphill; we walk opposite direction (downhill)
- In high dimensions, saddle points vastly outnumber local minima
- SGD noise helps escape saddle points — a feature, not a bug
- Gradient is O(n) to compute — the only thing you can afford at scale

### Jacobian Matrix
- Extends gradients to vector-valued functions (m outputs, n inputs → m×n matrix)
- Backprop through layers = multiplying by Jacobians (or their transposes)
- In practice, never explicitly constructed — frameworks compute vector-Jacobian products (VJPs)
- Critical for softmax layer, multi-output networks

### Hessian Matrix
- Second-order partial derivatives — captures curvature of loss surface
- Eigenvalues reveal: all positive = local min, mixed = saddle point
- Newton's method: delta = -H^(-1) * gradient — accounts for curvature
- O(n²) storage, O(n³) inversion — impossible for large nets
- Approximations: L-BFGS, KFAC, diagonal Hessian

### Automatic Differentiation
- Three approaches: symbolic (expression manipulation), numerical (finite differences), automatic (chain rule on elementary ops)
- Forward mode: propagates derivatives input→output, needs n passes for n inputs
- Reverse mode: propagates output→input, ONE backward pass for all gradients
- ML has many inputs (parameters), one output (loss) → reverse mode wins spectacularly
- PyTorch builds dynamic computational graph during forward pass, traverses in reverse
- Each op stores its backward function during forward pass

### Vanishing/Exploding Gradients
- Gradient = product of many local derivatives through layers
- Sigmoid max derivative = 0.25 → 0.25^20 ≈ 10^(-12) = vanishing
- Solutions: ReLU (derivative 1 for positive), residual connections (gradient shortcuts), careful init (He/Xavier)
- Exploding: gradient norm clipping before update step
- BPTT in RNNs: sequence length T = T layers deep → particularly severe

### Softmax + Cross-Entropy
- The elegant result: gradient = ŷ - y (predicted minus true)
- Derivation cancels beautifully through Jacobian of softmax
- Numerically: always use combined log_softmax + NLL, never separate softmax + log
- Log-sum-exp trick prevents overflow

### Taylor Expansion → Gradient Descent
- First-order Taylor: L(w + δ) ≈ L(w) + ∇L·δ
- Minimize by choosing δ opposite to gradient: δ = -α∇L
- Learning rate α controls how far we trust this linear approximation
- Too large α → approximation breaks, overshoot; too small → slow
- Second-order (Newton): uses Hessian, converges quadratically but O(n³) cost
