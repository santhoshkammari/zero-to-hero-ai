# Rewrite Plan for ch02/s07.html — Numerical Computing

## Running Example
A tiny neural network predicting house prices — we follow a single training step through
forward pass, loss computation, backward pass, weight update. Each numerical trap appears
naturally in this journey.

## Concept Ladder (dependency order)
1. Why computers lie about numbers (0.1 + 0.2 story) → IEEE 754 basics
2. The number line has holes (machine epsilon, precision limits)
3. When small errors become big ones (catastrophic cancellation, variance formula)
4. The log-sum-exp trick (softmax, log-probabilities)
5. REST STOP — you now know how to avoid 90% of NaN bugs
6. Solving equations without inverting matrices (condition number, ridge connection)
7. When matrices are too big (iterative methods, sparse computation)
8. GPU memory: the real bottleneck (hierarchy, tensor cores)
9. Mixed precision: training with half the bits (fp16, bf16, fp8, loss scaling)
10. Wrap-up

## Vulnerability Moments
1. "I spent two days debugging a NaN that turned out to be an unprotected log(0)"
2. "I still catch myself reaching for matrix inversion"
3. "Condition numbers still intimidate me a bit"
4. "The first time I saw 0.1 + 0.2 != 0.3, I genuinely questioned Python"

## Recurring Analogies
1. Ruler analogy: floating point is like a ruler with tick marks that get farther apart
2. Kitchen scale: precision vs range tradeoff (fine scale can't weigh a truck)
3. Assembly line: GPU as massively parallel assembly line vs CPU artisan workshop

## Style Notes
- Brandon Rohrer voice: practitioner, not professor
- Personal confessions, dry humor
- Every concept motivated by pain
- Toy examples before names
- Define every term inline
