# Reinforcement Learning Research Summary

## Key Concepts to Cover (Build-Up Order)
1. The RL problem framing - agent/env loop, why it's different from supervised learning
2. Running example: training a virtual dog to navigate a park
3. MDP framework - states, actions, transitions, rewards, discount factor
4. Bellman equations - recursive value decomposition
5. Dynamic programming - value iteration, policy iteration (when you know the model)
6. Monte Carlo methods - learning from complete episodes
7. TD Learning - the brilliant middle ground, bootstrapping
8. Q-learning and SARSA - tabular control methods
9. Deep RL / DQN - function approximation, experience replay, target networks
10. Policy gradients - REINFORCE, variance reduction, baselines
11. Actor-critic - A2C, A3C, combining value and policy
12. PPO - the workhorse, clipped surrogate objective
13. SAC - maximum entropy, off-policy actor-critic
14. Model-based RL - Dyna, World Models, MuZero
15. RLHF / DPO / GRPO - alignment connection
16. Applications and challenges

## Key Insights from Research
- Bellman equation: "value of a state = immediate reward + discounted value of next state"
- TD vs MC tradeoff: TD has bias but lower variance, MC has no bias but high variance
- DQN breakthrough: experience replay breaks correlations, target network stabilizes targets
- PPO: trust region via clipping, not Hessians - embarrassingly simple yet effective
- RLHF pipeline: SFT → Reward Model → PPO with KL penalty
- DPO: skips reward model, direct preference optimization - rising in popularity
- GRPO: newer method from DeepSeek, group-relative policy optimization
- Model-based RL: MuZero learns abstract model, Dreamer learns in latent space

## Running Example Idea
A grid world / maze scenario - training a virtual mouse to find cheese
- Start simple: 3x3 grid, mouse at top-left, cheese at bottom-right
- Scale up as concepts demand more complexity
- Naturally motivates: value functions, exploration, bootstrapping
