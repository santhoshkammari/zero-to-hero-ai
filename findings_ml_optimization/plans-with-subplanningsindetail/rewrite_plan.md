# Plan for ch04/s07.html Rewrite — ML Optimization

## Running Example
A house price prediction model. We start with a single-parameter model (predict price from square footage) and build up.
This is tangible, relatable, and scales naturally.

## Concept Ladder (dependency order)
1. What optimization even means (finding the best knob settings)
2. The loss landscape — a terrain metaphor that recurs
3. Gradient descent: feel slope, step downhill
4. Learning rate: why step size is everything
5. Batch vs SGD vs mini-batch
6. **REST STOP** — you now have a working mental model
7. Momentum: the heavy ball analogy
8. Adaptive methods: AdaGrad → RMSprop → Adam → AdamW
9. Learning rate schedules
10. Convergence challenges: saddle points, sharp vs flat minima
11. Gradient clipping
12. Backprop vs gradient descent distinction
13. Second-order methods (brief)
14. Practical recipe

## Recurring Analogies
1. **Foggy landscape** — the loss surface, recurs when discussing saddle points, sharp/flat minima
2. **Heavy ball rolling** — momentum, recurs for Nesterov and Adam

## Vulnerability Moments
1. Opening confession: avoided optimization math
2. Acknowledging that no one fully knows why Adam works so well universally
3. Admitting the sharp vs flat minima theory is still debated
4. Confessing SGD vs Adam debate has no clean answer
5. Still developing intuition for why warmup helps

## Style Notes
- Brandon Rohrer style: build from zero, personal voice, toy examples
- No "simply," "just," "obviously"
- Narrative prose, not listicles
- Every concept motivated by frustration/limitation of previous
- Define every term inline on first use
