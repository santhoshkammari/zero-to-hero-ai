# Online Learning & Bandits - Key Concepts

## Core Concept Ladder
1. The batch learning limitation → why online learning exists
2. Online learning protocol (predict, observe, update)
3. Regret as the scorecard (not accuracy)
4. Mistake bounds (Perceptron convergence)
5. Online Gradient Descent
6. Partial information → bandits
7. Explore vs exploit tradeoff
8. Epsilon-greedy (simplest approach)
9. UCB (principled approach)
10. Thompson Sampling (Bayesian approach)
11. Adversarial bandits (EXP3)
12. Contextual bandits (LinUCB)
13. Online Convex Optimization (FTRL)
14. Real-world applications

## Running Example: Coffee shop owner choosing which daily special to offer
- 5 specials, unknown customer preferences
- Learns one day at a time
- Can only see sales for today's special (bandit feedback)
- Context: weather, day of week (contextual bandit)

## Key Insights
- Perceptron mistake bound: (R/γ)² — bigger margin = fewer mistakes
- UCB: optimism in the face of uncertainty
- Thompson: posterior naturally balances explore/exploit
- EXP3: importance weighting for adversarial settings
- LinUCB: ridge regression + confidence ellipsoid
- FTRL unifies OGD, multiplicative weights, etc.
