# Perceptron to MLP — Key Findings

## McCulloch-Pitts Neuron (1943)
- Binary threshold unit: sum weighted binary inputs, fire if >= threshold
- No learning — weights and threshold are fixed
- Could implement AND, OR, NOT logic gates

## Rosenblatt's Perceptron (1958)
- Added learning rule: w_i ← w_i + η(t - y)x_i
- Perceptron Convergence Theorem: if data is linearly separable, converges in finite steps
- Geometrically: finds a separating hyperplane

## XOR Crisis (1969)
- Minsky & Papert proved single perceptron can't solve non-linearly-separable problems
- XOR: no single line separates the classes in 2D
- Led to first AI winter — funding dried up

## MLP Solution
- Hidden layer transforms input space via nonlinear activations
- "Bends" the space so XOR becomes linearly separable in the new representation
- Minimum: 2 hidden neurons can solve XOR
- Backpropagation (1986, Rumelhart/Hinton/Williams) made training practical

## Universal Approximation Theorem
- Single hidden layer with enough neurons can approximate any continuous function
- BUT: "enough neurons" can mean exponentially many
- Deep networks achieve same expressiveness with far fewer parameters
- Depth enables hierarchical feature composition
- The theorem is existence proof, not construction guide — doesn't tell you HOW to find weights
