# Calculus Section Rewrite Plan

## Running Example: Training a tiny house price predictor
- Start with one weight, one input, one output
- Build up to multi-weight, then layers, then full network
- Concrete: predicting house price from square footage, then adding bedrooms, etc.

## Concept Ladder (build-up order)
1. **What is a derivative?** — The wiggle test. Nudge input, watch output change.
2. **Why ML cares** — Loss function depends on weights. Derivative tells you which way to nudge.
3. **Differentiation rules** — Power rule, product rule. Brief, practical.
4. **The Chain Rule** — THE calculus concept for ML. Compositions of functions = neural networks.
5. **Partial derivatives & gradients** — Multiple parameters. Gradient = vector of all partial derivatives.
6. **Jacobian & Hessian** — Vector outputs, curvature. Why first-order methods dominate.
7. **Key ML functions & derivatives** — Sigmoid, ReLU, tanh, softmax. Why each matters, derivatives.
8. **Integrals** — Accumulation, probability, expectations. Brief but grounded.
9. **Taylor series → Gradient descent** — First-order approximation directly produces the algorithm.
10. **Backpropagation** — Chain rule applied systematically. Computational graphs.
11. **Vanishing/Exploding gradients** — The product-of-derivatives problem. Solutions.
12. **Automatic Differentiation** — Three approaches. Why reverse mode wins for ML.
13. **Softmax + Cross-Entropy** — The elegant ŷ - y result.
14. **Advanced: Neural ODEs, Variational Calculus, Information Geometry**

## Rest Stop
After gradient descent derivation from Taylor (section 9). Reader now has: derivatives, chain rule, gradients, and the core algorithm.

## Recurring Analogies
1. **The hiking trail** — Loss landscape as terrain, gradient as slope, you're hiking downhill
2. **The nudge test** — Wiggle a knob, see what happens to the output

## Vulnerability Moments
1. Opening: avoided calculus, relied on frameworks blindly
2. Chain rule: "I used to think backprop was some separate algorithm"
3. Hessian: "I still find second-order methods intimidating"
4. Vanishing gradients: "The first time I saw my loss flatline..."
5. Autodiff: "I assumed PyTorch was doing symbolic math under the hood"

## Style Notes (Brandon Rohrer)
- First person, journey-based
- Build from tiny example up
- Every concept motivated by frustration with what came before
- Show limitation at end of each section
- Define every term inline on first use
- No "simply", "just", "obviously"
- Narrative prose, not bullet listicles for explanations
