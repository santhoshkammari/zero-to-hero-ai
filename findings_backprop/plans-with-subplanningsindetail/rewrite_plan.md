# Rewrite Plan — ch07/s04 Backpropagation

## Running Example
A temperature prediction network: given yesterday's high temp and humidity, predict today's high.
Start with 2 inputs, 2 hidden neurons, 1 output — small enough to trace by hand.

## Concept Ladder (dependency order)
1. Why we need backprop (motivation: can't check each weight individually)
2. The chain rule as amplification — signal passing through stages
3. Forward pass traced step by step (concrete numbers)
4. Backward pass traced step by step (concrete numbers)
5. The pattern: gradient = upstream_signal × local_input
6. **REST STOP** — you now understand backprop for a small network
7. Computational graphs — what frameworks actually build
8. Three flavors of differentiation (symbolic, numerical, automatic)
9. Forward vs reverse mode AD — why reverse wins
10. Vanishing and exploding gradients — the product-of-many-numbers problem
11. PyTorch autograd in practice
12. Practical details: gradient accumulation, detach, checkpointing
13. What backprop does NOT do
14. Wrap-up

## Analogies (recurring)
1. **Assembly line / factory defect trace** — tracing blame backwards through stations
2. **Telephone game** — signal degrading through layers (vanishing gradients)

## Vulnerability Moments
1. "I avoided deriving backprop for years..."
2. "I'm still developing my intuition for why the sigmoid+BCE derivative simplifies so cleanly"
3. "No one fully understands the loss landscape geometry..."
4. "I still occasionally mix up when to use detach vs no_grad"

## Style Notes
- Brandon Rohrer voice: practitioner sharing discovery, not professor lecturing
- No "simply", "just", "obviously"
- Every formula explained inline in prose
- Toy example traced completely — no skipped steps
- Preserve HTML structure of current file (sidebar, nav, css links, etc.)
