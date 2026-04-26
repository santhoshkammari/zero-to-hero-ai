# Rewrite Plan for ch12/s04 - Reasoning & Inference-Time Scaling

## Running Example
A math tutoring bot that needs to solve word problems for students.
Start with a simple 2-step problem, scale up to multi-step, then competition-level.

## Concept Ladder (dependency order)
1. The autoregressive bottleneck (why single-pass fails for reasoning)
2. Chain-of-thought as scratchpad (intermediate tokens expand computation)
3. Zero-shot vs few-shot CoT
4. Self-consistency (sampling + voting)
5. REST STOP
6. Tree of Thoughts (branching search)
7. Thinking tokens / o1 paradigm (trained internal reasoning)
8. Inference-time scaling laws (the fourth axis)
9. Process Reward Models vs Outcome Reward Models
10. MCTS for reasoning
11. STaR and GRPO (self-improving reasoning)
12. Benchmarks (GSM8K, MATH, AIME)
13. Wrap-up

## Recurring Analogies
1. Chess player analogy: System 1 = blitz chess (instant moves), System 2 = classical chess (think for minutes). Bring back for thinking tokens and MCTS.
2. Draft-and-revise analogy: writing an essay with rough drafts vs final submission. Bring back for self-consistency and PRM.

## Vulnerability Moments
1. Opening: avoided understanding why CoT works
2. Self-consistency: "I still find it counterintuitive that asking the same model the same question gets different answers"
3. PRM: "I'm still building my intuition for how step-level rewards propagate"
4. Inference scaling: "no one is completely certain where the ceiling is"
5. MCTS: admit it's hard to visualize how tree search applies to text generation
