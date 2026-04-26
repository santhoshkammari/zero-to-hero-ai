# Rewrite Plan for ch17/s03 - Reinforcement Learning

## Structure (Following Brandon's Style)

### Phase 1: Opening
- Personal confession: avoided RL, seemed like a different universe from supervised learning
- Orientation: what RL is, when it emerged (Bellman 1950s, modern deep RL 2013+)
- Heads-up: math notation, some probability, but built from scratch
- Journey invitation

### Phase 2: Table of Contents

### Phase 3: Build-Up (concept ladder)
1. The Loop (agent-environment interaction)
2. The Scoreboard (rewards and returns)
3. The Map (MDP framework)
4. The Bellman Shortcut (recursive value)
5. Solving with Full Knowledge (dynamic programming)
6. REST STOP
7. Learning from Episodes (Monte Carlo)
8. Learning Step by Step (TD learning)
9. Q-Learning (the off-policy trick)
10. SARSA (the on-policy alternative)
11. When Tables Fail (function approximation / DQN)
12. REST STOP
13. Learning Actions Directly (policy gradients / REINFORCE)
14. The Actor and the Critic (actor-critic / A2C)
15. PPO (the workhorse)
16. SAC (maximum entropy)
17. Imagining Before Acting (model-based RL)
18. Teaching Language Models Right from Wrong (RLHF)

### Phase 4: Rest Stops
- After dynamic programming (useful mental model of value functions)
- After DQN (can solve real problems now)

### Phase 5: Wrap-Up

### Phase 6: Resources

## Analogies (recurring)
1. "Training a dog" - rewards, delayed feedback, exploration
2. "GPS navigation" - value of states, shortest path, planning ahead
3. "Thermostat" - for control problems, feedback loops

## Vulnerability Moments
1. "I avoided RL for years..."
2. "The Bellman equation looked like hieroglyphics to me the first time"
3. "I'm still developing intuition for why PPO's simple clipping works so well"
4. "No one fully understands why DQN's combination of tricks prevents divergence so reliably"
5. "I still get confused about on-policy vs off-policy sometimes"
