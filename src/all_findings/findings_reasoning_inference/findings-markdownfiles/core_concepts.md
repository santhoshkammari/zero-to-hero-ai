# Reasoning & Inference-Time Scaling - Core Concepts

## Chain-of-Thought (CoT) Prompting
- Wei et al. 2022 - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Key mechanic: each intermediate token conditions the next, narrowing probability space
- Zero-shot CoT: append "Let's think step by step" - Kojima et al. 2022
- Few-shot CoT: provide worked examples with reasoning traces
- Works best on >100B parameter models; effect magnified with scale
- Biggest gains: GSM8K math, symbolic reasoning, multi-hop QA

## Self-Consistency (Wang et al. 2022)
- Sample N reasoning chains at high temperature
- Extract final answers, majority vote
- Correct paths converge; errors scatter randomly
- 60% single-attempt → ~83% with 10 samples via binomial statistics
- Key: samples are NOT truly independent (share model biases)

## Tree of Thoughts (Yao et al. 2023)
- Treats reasoning as tree search (BFS/DFS)
- Each node = partial reasoning state
- LLM generates branches, evaluates promising paths
- Game of 24 as canonical example
- Enables backtracking from dead ends

## Inference-Time Scaling (Snell et al. 2024)
- arXiv:2408.03314
- Fourth axis: inference-time compute (beyond params, data, train compute)
- Smaller model + more inference budget can beat 14x larger model
- Adaptive compute allocation: easy queries→fast, hard queries→deep reasoning
- >4x improvement over naive best-of-N with adaptive strategies

## Process Reward Models (Lightman et al. 2023)
- PRM evaluates each reasoning step, not just final answer
- Enables pruning bad paths early (compute efficient)
- ORM only checks final answer - can't locate errors
- PRM training requires step-level labels (expensive)
- Monte Carlo estimation can reduce labeling cost

## STaR (Zelikman et al. 2022)
- Self-Taught Reasoner: bootstrapping reasoning with reasoning
- Generate traces → keep correct ones → fine-tune → repeat
- "Rationalization": give correct answer as hint for failed problems
- Self-improvement flywheel

## GRPO (DeepSeek-R1)
- Group Relative Policy Optimization
- No separate reward model needed
- Sample N solutions, compute group-relative advantages
- Update policy: increase prob of above-average, decrease below-average
- Needs only correctness signal (right/wrong)

## MCTS for Reasoning
- AlphaProof-style: MCTS + LLM for mathematical proof search
- Node = partial solution, Action = next reasoning step
- UCB1/PUCT for exploration vs exploitation
- Rollouts to estimate path quality

## Benchmarks
- GSM8K: grade school math, near-saturated (~96-97% top models)
- MATH: competition-level, harder (~70-72% for best models)
- AIME: o1 scored 83% vs GPT-4o at 13%
- GSM1k: new benchmark to avoid data contamination
