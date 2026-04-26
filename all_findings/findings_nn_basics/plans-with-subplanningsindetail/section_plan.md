# Section Plan: Neural Network Basics (ch07/s01)

## Running Example: Building a spam detector
- Start tiny: 2 features (word count, has-link) → spam/not-spam
- Scale up naturally as we add layers and activations
- Returns throughout the section

## Concept Ladder (dependency order)
1. The Artificial Neuron — weighted sum + bias + activation (bedrock)
2. The Perceptron — a neuron that learns from mistakes
3. The XOR Wall — where a single neuron fails (motivates layers)
4. Stacking Layers: The MLP — hidden layers transform space
5. Why Nonlinearity Matters — without it, depth is an illusion
6. Activation Functions: ReLU and Its Descendants
7. The Smooth Gates: GELU and Swish
8. Sigmoid, Tanh, and Softmax — output activations
9. Weight Initialization — Xavier vs He
10. Universal Approximation — what depth really buys you

## Rest Stop Placement
- After MLP section (reader has: neuron → perceptron → MLP mental model)

## Vulnerability Moments
1. "I avoided neural networks for longer than I'd like to admit" (opening)
2. "I'll be honest — the XOR thing confused me for years" (XOR section)
3. "No one is completely certain why depth works so much better" (UAT section)
4. "I still occasionally mess up initialization" (init section)
5. Admit oversimplification about neurons being like brain cells

## Recurring Analogies
1. Assembly line / factory — each layer adds a step of processing
2. Space-bending / origami — hidden layers fold the input space
