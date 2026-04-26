# Optimization Section Rewrite Plan

## Running Example
A hiker navigating mountainous terrain blindfolded, feeling the slope underfoot.
- Starts with a simple 1D valley (convex)
- Grows to a mountain range with deceptive valleys (non-convex)
- Introduces fog, wind (noise/stochasticity)
- The terrain analogy recurs throughout

## Concept Ladder (dependency order)
1. What optimization IS — finding the lowest point
2. Gradient descent from scratch — the slope-feeling hiker
3. Convex vs non-convex — one valley vs many
4. The learning rate dilemma — step size matters
5. Momentum — the rolling ball that coasts through flats
6. SGD and mini-batches — noise as a feature
7. Adaptive methods — Adam, RMSprop, per-parameter adaptation
8. The SGD vs Adam debate — sharp vs flat minima
9. Learning rate schedules — changing pace through the journey
10. Saddle points — the real enemy, not local minima
11. Loss landscapes — what the terrain actually looks like
12. Constrained optimization — guardrails on the hike
13. Second-order methods — why we don't use the map

## Rest Stop
After section on SGD + momentum — reader has a useful mental model for training.

## Vulnerability Moments
1. Opening: avoided optimization, thought it was "the boring math part"
2. Learning rate: "I still sometimes pick a learning rate that's off by 10x"
3. Adam vs SGD: "I'm still developing my intuition for when to use which"
4. Saddle points: "no one is completely certain" about loss landscape geometry
5. Second-order methods: "I haven't figured out a great way to visualize the Hessian"

## Analogies (recurring)
1. Blindfolded hiker on mountains — gradient descent, terrain = loss landscape
2. Ball rolling downhill — momentum, velocity, coasting through flats
3. Fog/weather — noise in SGD, learning rate schedules

## Structure
- Opening: personal confession, orientation, heads-up, journey invitation
- TOC
- Build-up sections with motivation → toy example → step-through → name → limitation
- Rest stop after momentum/SGD
- Advanced: Adam, schedules, saddle points, landscapes, constraints
- Wrap-up with gratitude, recap, future hope
- Resources
