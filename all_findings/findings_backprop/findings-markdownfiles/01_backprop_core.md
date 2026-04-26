# Backpropagation — Core Research Findings

## What Backprop Actually Is
- An efficient algorithm for computing gradients of loss w.r.t. all parameters
- It IS the chain rule applied in reverse through a computational graph — nothing more
- NOT a learning algorithm itself — it only computes gradients; the optimizer does the updating
- Cost: roughly 2× one forward pass, regardless of parameter count
- Without it, you'd need n forward passes for n parameters (numerical differentiation)

## History (Credit Where Due)
- 1970: Seppo Linnainmaa — reverse mode automatic differentiation (the mathematical core)
- 1974: Paul Werbos — first to apply it to neural networks (PhD thesis)
- 1986: Rumelhart, Hinton, Williams — popularized it, showed it works empirically
- The algorithm itself predates its fame by 16 years

## Three Types of Differentiation
1. **Symbolic**: manipulates expressions (Wolfram Alpha). Produces exact formulas but suffers "expression swell" — formulas grow exponentially for deep compositions
2. **Numerical**: finite differences f'(x) ≈ (f(x+h) - f(x))/h. Easy but inaccurate and O(n) forward passes per gradient
3. **Automatic (AD)**: tracks operations, applies chain rule to actual numbers. No expression swell, exact to machine precision. This is what frameworks use.

## Forward vs Reverse Mode AD
- Forward mode: computes J·v (Jacobian-vector product). Cost = n passes for n inputs
- Reverse mode: computes v^T·J (vector-Jacobian product). Cost = m passes for m outputs
- Neural nets have 1 scalar loss and millions of params → reverse mode wins by factor of millions
- Reverse mode AD IS backpropagation

## The Computational Graph
- DAG of operations recorded during forward pass
- Each node knows how to compute its local derivative
- backward() traverses in reverse topological order
- PyTorch: dynamic graph (tape-based, built on-the-fly)
- TensorFlow 1.x: static graph (defined then run) — mostly historical now

## Vanishing/Exploding Gradients
- Chain rule = multiplying local derivatives together
- If derivatives consistently < 1: gradient vanishes (exponential decay)
- If derivatives consistently > 1: gradient explodes (exponential growth)
- Sigmoid max derivative = 0.25 — guaranteed vanishing after ~10 layers
- Solutions: ReLU (2011), residual connections (2015), batch norm (2015), proper initialization (Xavier 2010, He 2015), gradient clipping

## Common Misconceptions
1. Backprop "learns" → No, it only computes gradients
2. Backprop finds global minimum → No, it gives local gradient direction
3. Backprop is computationally expensive → No, ~2× forward pass
4. Backprop is biologically plausible → No, brains don't do it this way
5. You need separate passes per parameter → No, one backward pass covers all

## Interview Depth
- Must be able to derive it from scratch on whiteboard
- Understand the pattern: gradient for weight = upstream_signal × local_input
- Know dead ReLU problem and why it happens (chain rule multiplies by 0)
- Gradient accumulation: PyTorch accumulates by default (feature, not bug)
- .detach() vs torch.no_grad() — when and why
- Gradient checkpointing: O(√n) memory trade for ~30% more compute
