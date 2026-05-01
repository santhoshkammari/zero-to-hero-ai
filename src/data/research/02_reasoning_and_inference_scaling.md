# The Reasoning Revolution: Test-Time Compute & Thinking Models

> *"The next frontier of AI isn't bigger models — it's models that think longer."*

For decades, the recipe for better AI was simple: **more parameters, more data, more training compute**. The Kaplan scaling laws (2020) and Chinchilla (2022) told us exactly how to spend our compute budget during training. But starting in 2024, a seismic shift occurred. OpenAI's o1, DeepSeek's R1, and a growing ecosystem of "reasoning models" demonstrated that you can dramatically improve performance by spending more compute **at inference time** — letting the model *think* before it answers.

This document traces the full arc of that revolution: from the first chain-of-thought prompts to the reinforcement-learning breakthroughs that taught models to reason, verify, and backtrack — all on their own.

---

## Table of Contents

1. [Why This Matters](#1-why-this-matters)
2. [Historical Evolution: From Prompting to Thinking](#2-historical-evolution-from-prompting-to-thinking)
3. [The Scaling Laws Shift](#3-the-scaling-laws-shift)
4. [How o1/o3 Work — Technical Deep Dive](#4-how-o1o3-work--technical-deep-dive)
5. [DeepSeek-R1 — The Open-Source Reasoning Breakthrough](#5-deepseek-r1--the-open-source-reasoning-breakthrough)
6. [The Math Behind It](#6-the-math-behind-it)
7. [The Broader Reasoning Ecosystem](#7-the-broader-reasoning-ecosystem)
8. [Practical Implications](#8-practical-implications)
9. [Open Problems and Future Directions](#9-open-problems-and-future-directions)
10. [Key Papers & Sources](#10-key-papers--sources)
11. [Concepts for the Knowledge Tree](#11-concepts-for-the-knowledge-tree)

---

## 1. Why This Matters

### The Old Paradigm: Train Bigger

From 2018 to 2023, the dominant strategy in AI was straightforward:

```
Better AI = More Parameters × More Data × More Training FLOPs
```

GPT-2 (1.5B) → GPT-3 (175B) → PaLM (540B) → GPT-4 (~1.8T estimated). Each generation was a bigger model trained on more data. The Kaplan scaling laws (OpenAI, 2020) showed that loss decreases as a smooth power law with model size, dataset size, and compute. Chinchilla (Hoffmann et al., 2022) refined this: for a fixed compute budget, you should scale model parameters and training tokens roughly equally.

But this approach has limits:
- **Training costs** grow quadratically or worse with model size
- **Data** is finite — we're approaching the limits of high-quality internet text
- A 10× bigger model gives you better average performance, but it **doesn't think harder on hard problems**

### The New Paradigm: Think Longer

The reasoning revolution inverts the equation:

```
Better AI = Good Base Model × More Inference Compute (on hard problems)
```

Instead of making the model bigger, you let it **generate a longer chain of reasoning** — exploring multiple solution paths, verifying its own work, backtracking from dead ends. A model that spends 10 seconds "thinking" about a hard math problem can dramatically outperform a model that produces an immediate answer.

**The key insight**: For many problems, it is more cost-effective to spend additional FLOPs at inference time than to have spent them during training.

This isn't just an engineering trick — it's a fundamental paradigm shift. It means:

1. **Smaller models can match larger ones** by thinking longer on hard problems
2. **Compute can be allocated adaptively** — easy questions get fast answers, hard questions get deep reasoning
3. **New capabilities emerge** — self-verification, backtracking, and strategic problem decomposition arise naturally from training models to reason

---

## 2. Historical Evolution: From Prompting to Thinking

The reasoning revolution didn't appear overnight. It was built on a series of insights spanning 2021–2024.

### 2.1 The Scratchpad Idea (Nye et al., 2021)

The earliest ancestor of modern reasoning models was the **scratchpad** concept. Nye et al. showed that if you train a model to write intermediate computation steps in a designated "scratchpad" area before producing a final answer, performance on multi-step tasks improves dramatically.

**Why it works**: Standard autoregressive LLMs produce output token by token, left to right. Without a scratchpad, the model must compute the answer in a single forward pass — effectively in "constant time." A scratchpad lets the model use its own generated text as working memory, turning it into a sequential computation device with **variable-length intermediate state**.

```
Without scratchpad:
  Input: "What is 347 × 28?" → Output: "9716"
  (Model must compute this in ~1 forward pass)

With scratchpad:
  Input: "What is 347 × 28?"
  Scratchpad: "347 × 8 = 2776. 347 × 20 = 6940. 2776 + 6940 = 9716."
  Output: "9716"
  (Model breaks computation into manageable steps)
```

This was the seed of a powerful idea: **the model's output IS its computation**.

### 2.2 Chain-of-Thought Prompting (Wei et al., 2022)

The landmark paper "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., NeurIPS 2022) showed that you don't even need to train for scratchpad behavior — you can simply **prompt** the model to show its work.

**The method**: Include a few-shot example where the answer includes intermediate reasoning steps. Or, most famously, just append "Let's think step by step" to the prompt.

**Key findings**:
- Chain-of-thought (CoT) improves performance on **arithmetic**, **commonsense reasoning**, and **symbolic reasoning** tasks
- The gains are **emergent with scale** — CoT helps large models (100B+) dramatically but barely helps small ones (<10B)
- On GSM8K (grade school math), CoT prompting with PaLM-540B achieved ~58% accuracy vs. ~18% with standard prompting — a **3.2× improvement** from prompting alone

**Why chain-of-thought works** (the deeper story):

1. **Decomposition**: Complex problems get broken into simpler sub-problems the model can handle
2. **Working memory**: Intermediate results are stored in the generated text, offloading computation from the model's fixed-width hidden state
3. **Error localization**: When the model makes a mistake, it's visible in the chain, making it possible to identify and correct
4. **Implicit verification**: Writing out steps creates a trace that is internally consistent — the model conditions each step on previous ones

### 2.3 Self-Consistency and Majority Voting (Wang et al., 2023)

Wang et al. introduced **self-consistency**: instead of generating one chain-of-thought, generate **many** different chains and take a **majority vote** on the final answer.

```
Problem: "Janet has 16 eggs. She eats 3 for breakfast..."

Chain 1: ... → Answer: 9
Chain 2: ... → Answer: 9  
Chain 3: ... → Answer: 7  (different reasoning path, wrong)
Chain 4: ... → Answer: 9
Chain 5: ... → Answer: 9

Majority vote: 9 ✓
```

**Key insight**: Different reasoning paths can reach the same correct answer. By sampling multiple paths, you can filter out errors through consensus. This was the first demonstration that **more inference compute → better answers** in a systematic, predictable way.

On GSM8K, self-consistency with 40 samples boosted PaLM-540B from ~58% (single CoT) to ~74%.

This laid the groundwork for the inference-time scaling paradigm: **you can literally buy accuracy by spending more compute at test time**.

### 2.4 Tree of Thoughts (Yao et al., 2023)

Self-consistency samples independent chains. **Tree of Thoughts** (ToT) goes further: it explores reasoning paths as a **tree**, where the model can **evaluate** intermediate states and **prune** unpromising branches.

The key components:
1. **Thought generation**: At each step, generate multiple candidate "thoughts" (reasoning steps)
2. **State evaluation**: Use the LLM itself (or a separate evaluator) to assess how promising each partial solution is
3. **Search algorithm**: Use BFS, DFS, or beam search to navigate the tree

```
                    Problem
                   /       \
              Thought A    Thought B
              /     \         |
          Thought C  Thought D  Thought E
             |          ✗          |
         Thought F              Thought G
             |                     |
          Answer 1              Answer 2
             ✓                     ✓
```

ToT showed dramatic improvements on tasks requiring **exploration and planning** — like the Game of 24, creative writing prompts, and crossword puzzles. It formalized the idea that LLM reasoning isn't just a linear chain — it's a **search problem**.

### 2.5 The Insight That Changed Everything

By mid-2023, the pattern was clear:

| Technique | Inference Cost | Performance Gain |
|-----------|---------------|------------------|
| Standard prompting | 1× | Baseline |
| Chain-of-thought | ~2-5× | Significant |
| Self-consistency (N=40) | ~40× | Large |
| Tree of Thoughts | ~100×+ | Very large on specific tasks |

**More compute at inference time buys better performance.** But all these techniques were applied externally — through prompting strategies. The model itself didn't know *how* to think, *when* to think harder, or *how to verify* its own reasoning.

The next breakthrough was training models to do this **internally**.

---

## 3. The Scaling Laws Shift

### 3.1 Training-Time Scaling Laws (Recap)

The original scaling laws describe how model performance improves with training resources:

**Kaplan et al. (2020) — OpenAI**:
```
L(N) ∝ N^(-α_N)     # Loss scales as a power law with parameters N
L(D) ∝ D^(-α_D)     # Loss scales as a power law with data D
L(C) ∝ C^(-α_C)     # Loss scales as a power law with compute C
```

Where α_N ≈ 0.076, α_D ≈ 0.095, α_C ≈ 0.050 for language modeling loss.

**Chinchilla / Hoffmann et al. (2022) — DeepMind**:

Revised the optimal allocation: for a compute budget C, the optimal model size N_opt and data size D_opt should scale roughly as:

```
N_opt ∝ C^(0.50)
D_opt ∝ C^(0.50)
```

This means parameters and training tokens should scale **equally** with compute. Chinchilla (70B parameters, 1.4T tokens) outperformed the much larger Gopher (280B parameters, 300B tokens) because Gopher was **undertrained** relative to its size.

### 3.2 Inference-Time Scaling Laws (The New Paradigm)

The groundbreaking paper "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" (Snell et al., August 2024) formalized what practitioners had observed:

**Core finding**: For a fixed total FLOPs budget, you can sometimes get better results by using a **smaller model** with **more inference compute** than a larger model with standard inference.

Specifically:
- A smaller model with **compute-optimal** test-time scaling can match a **14× larger model** on FLOPs-matched evaluations
- Efficient allocation of test-time compute can be **4× more effective** than naive best-of-N sampling
- The benefit depends on problem difficulty: **moderately hard** problems benefit most from extra inference compute

**The compute-optimal inference equation**:

Consider a problem of difficulty d. You have a budget of C total FLOPs. You can spend them as:

```
C = C_train + C_inference
C_train = f(N, D)        # Training a model of size N on D tokens
C_inference = g(N, K)     # Running model of size N with K inference steps
```

For easy problems: C_inference should be small (just answer immediately)
For moderately hard problems: Shift budget from C_train to C_inference
For extremely hard problems: You still need sufficient C_train (base capability matters)

This gives rise to an **inference-time scaling curve**:

```
Performance
    ↑
    │           ┌─────────── ceiling (base model capability)
    │         ╱
    │       ╱
    │     ╱
    │   ╱
    │  ╱
    │╱
    └──────────────────→ Inference Compute
```

Performance improves with inference compute, but with **diminishing returns** that eventually plateau at the model's capability ceiling. The key is that this ceiling is much higher than what standard (single-pass) inference achieves.

### 3.3 Two Mechanisms for Spending Inference Compute

Snell et al. identified two complementary mechanisms:

**1. Search against a Verifier (Process Reward Model)**

Generate multiple candidate solutions, score each with a verifier model, and select the best one. This is the "generate-then-verify" paradigm.

```
Prompt → Generate N solutions → Score each with PRM → Select highest-scoring
```

Effectiveness depends on:
- Quality of the verifier
- Diversity of generated solutions
- Number of candidates N

**2. Adaptive Revision (Iterative Refinement)**

Let the model revise its own answer iteratively, conditioned on the problem and its previous attempt.

```
Prompt → Initial answer → Self-critique → Revised answer → Self-critique → ...
```

Effectiveness depends on:
- Model's ability to identify its own errors
- Whether revisions actually improve the answer (risk of "revision collapse")

**The compute-optimal strategy** combines both: for easy problems, a single attempt suffices; for moderately hard problems, iterative refinement is most efficient; for hard problems, broad search with verification wins.

### 3.4 The Inference Scaling Laws Paper (Wu et al., ICLR 2025)

Wu et al. empirically studied the **Pareto frontier** of model size vs. inference compute:

**Key findings**:
- Advanced inference strategies (tree search, voting, backtracking) + smaller models can achieve **Pareto optimality** — sometimes beating much bigger models at the same total computation
- The optimal inference strategy **changes with the compute budget**: at low budgets, a single call to a big model wins; at higher budgets, search-augmented smaller models dominate
- There exist **inference scaling laws** analogous to training scaling laws: performance improves as a power law with inference compute, with problem-difficulty-dependent exponents

### 3.5 Why This Changes Everything

The implication is profound. In the old paradigm:

```
Deploy model → Every query gets the same compute → Done
```

In the new paradigm:

```
Deploy model → Easy query? Quick answer (cheap)
             → Hard query? Extended thinking (expensive, but worth it)
             → Adaptive compute allocation based on difficulty
```

This means AI systems can be **cost-efficient on average** while being **powerful on demand**. You don't need a 1-trillion-parameter model for every request — you need a good base model that knows how to think harder when required.

---

## 4. How o1/o3 Work — Technical Deep Dive

OpenAI's o1 (released September 2024) and o3 (released early 2025) represent the first large-scale commercial deployment of reasoning models. While OpenAI hasn't published full technical details, we can reconstruct the likely architecture from published research, patents, and empirical observations.

### 4.1 The High-Level Architecture

```
┌─────────────────────────────────────────────┐
│                  User Query                  │
└─────────────┬───────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────┐
│           Problem Analysis & Planning        │
│  (Assess difficulty, plan reasoning depth)   │
└─────────────┬───────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────┐
│         Internal Chain-of-Thought            │
│   ┌─────────────────────────────────────┐   │
│   │ Step 1: Decompose the problem       │   │
│   │ Step 2: Try approach A              │   │
│   │ Step 3: Verify... hmm, that's wrong │   │
│   │ Step 4: Backtrack, try approach B   │   │
│   │ Step 5: This looks right, verify... │   │
│   │ Step 6: Cross-check with edge cases │   │
│   │ Step 7: Confident in answer         │   │
│   └─────────────────────────────────────┘   │
│              ↕ (PRM scoring each step)       │
│   ┌─────────────────────────────────────┐   │
│   │     Process Reward Model (PRM)      │   │
│   │  Scores each reasoning step for     │   │
│   │  correctness and progress           │   │
│   └─────────────────────────────────────┘   │
└─────────────┬───────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────┐
│         Final Answer (visible to user)       │
│   (Internal reasoning chain is hidden)       │
└─────────────────────────────────────────────┘
```

### 4.2 Process Reward Models (PRMs) vs. Outcome Reward Models (ORMs)

This distinction, formalized in "Let's Verify Step by Step" (Lightman et al., 2023), is central to how reasoning models work.

**Outcome Reward Model (ORM)**:
- Receives: full solution (problem + complete reasoning chain + answer)
- Outputs: single scalar score (how likely the answer is correct)
- Trained on: (solution, correct/incorrect) pairs
- Limitation: Can't tell you **where** the reasoning went wrong

```
ORM(problem, full_solution) → score ∈ [0, 1]
```

**Process Reward Model (PRM)**:
- Receives: partial solution (problem + reasoning steps up to step k)
- Outputs: score for **each step** (is this step correct and productive?)
- Trained on: step-level annotations (each step labeled correct/incorrect/neutral)
- Advantage: Provides **dense supervision** — knows exactly where errors occur

```
PRM(problem, step_1, step_2, ..., step_k) → (score_1, score_2, ..., score_k)
```

**Why PRMs are critical for reasoning models**:

Consider this analogy. An ORM is like a teacher who only checks the final answer on an exam. A PRM is like a teacher who reads every line of your work, marking where you went wrong. The PRM provides:

1. **Better search guidance**: During tree search, the PRM can evaluate partial solutions, allowing early pruning of wrong branches
2. **Credit assignment**: When the final answer is wrong, the PRM identifies which step caused the error
3. **Training signal**: PRM scores can be used as reward signals during RL training

**The PRM800K dataset** (Lightman et al., 2023) was a pivotal contribution: 800,000 step-level human annotations on math solutions, showing that process supervision consistently outperforms outcome supervision for mathematical reasoning.

**Empirical results from Lightman et al.**:
- On MATH benchmark: PRM-guided best-of-N selection significantly outperformed ORM-guided selection
- The gap widens with more samples — PRMs scale better with inference compute
- PRMs also improve calibration: they're better at knowing when they're right

### 4.3 Tree Search over Reasoning Steps

The likely reasoning architecture in o1/o3 involves some form of **tree search** over reasoning steps, guided by a PRM:

```
                    Problem: "Prove that √2 is irrational"
                    /              |              \
          Approach A:          Approach B:      Approach C:
       Direct proof         Proof by            Assume rational,
       attempt              contradiction       derive contradiction
       PRM: 0.3             PRM: 0.8           PRM: 0.85
            ✗                    |                   |
                          /            \          ...
                  Assume √2=p/q     Assume √2=a/b
                  in lowest terms   where gcd(a,b)=1
                  PRM: 0.82         PRM: 0.88
                       |                 |
                      ...            Then 2b²=a²
                                    So a² is even
                                    So a is even...
                                    PRM: 0.95
                                         |
                                    (continues to
                                     valid proof)
```

The search algorithm is likely a variant of **beam search** or **Monte Carlo Tree Search (MCTS)**, adapted for language model reasoning.

### 4.4 MCTS for LLM Reasoning

Monte Carlo Tree Search, originally famous from AlphaGo, is a powerful framework for reasoning:

**The four phases of MCTS**:

```
1. SELECTION: Starting from root, traverse the tree using UCB
   (Upper Confidence Bound) to balance exploration vs exploitation

2. EXPANSION: At a leaf node, generate new child nodes
   (= generate candidate next reasoning steps)

3. SIMULATION (Rollout): From the new node, simulate to completion
   (= generate a complete solution from this point)

4. BACKPROPAGATION: Update node statistics based on the outcome
   (= was the final answer correct?)
```

**Adapted for LLM reasoning**:

```python
# Simplified MCTS for LLM reasoning
class ReasoningNode:
    state: str           # reasoning so far
    children: list       # possible next steps
    visits: int          # how many times explored
    value: float         # average PRM score or success rate

def select(node):
    """UCB1 selection: balance exploitation (high value) and 
    exploration (low visits)"""
    return argmax(
        child.value / child.visits 
        + c * sqrt(ln(node.visits) / child.visits)
        for child in node.children
    )

def expand(node, llm):
    """Generate candidate next reasoning steps"""
    next_steps = llm.generate_diverse(
        prompt=node.state, 
        n=num_candidates,
        temperature=0.7
    )
    for step in next_steps:
        node.children.append(ReasoningNode(
            state=node.state + step
        ))

def simulate(node, llm):
    """Complete the solution from this point"""
    full_solution = llm.generate(
        prompt=node.state, 
        max_tokens=max_remaining
    )
    return full_solution

def backpropagate(node, reward):
    """Update statistics up the tree"""
    while node is not None:
        node.visits += 1
        node.value += reward
        node = node.parent
```

**The PRM replaces random rollouts**: In classical MCTS (e.g., for Go), the simulation phase uses random playouts. For LLM reasoning, the PRM provides a much better value estimate — it can score a partial solution's quality without completing it.

### 4.5 Hidden Chain-of-Thought / Internal Deliberation

A distinctive feature of o1 is that its reasoning chain is **hidden from the user**. You see only a summary of the thinking process and the final answer. The internal chain of thought can be thousands of tokens long.

**Why hide the chain?**:
1. **Safety**: Internal deliberation may contain unfaithful or manipulative reasoning chains; hiding them reduces attack surface
2. **Competitive advantage**: The reasoning strategies represent significant IP
3. **User experience**: Most users want answers, not 5000-token reasoning traces
4. **Flexibility**: Hidden chains can use internal formats, abbreviations, or code that wouldn't make sense to users

**What we observe empirically about o1's reasoning**:
- On hard math problems, o1 generates **tens of thousands** of internal reasoning tokens
- The model exhibits clear **backtracking behavior**: "Wait, that approach doesn't work. Let me try..."
- It shows **self-verification**: "Let me check this by substituting back..."
- It demonstrates **strategic planning**: "This is a complex problem. I'll break it into three parts..."
- Reasoning length **correlates with problem difficulty** — harder problems elicit longer chains

### 4.6 How the Model Learns WHEN to Think More

A crucial aspect: o1 doesn't think for 30 seconds on "What's 2+2?" It adapts its reasoning depth to problem difficulty. This likely involves:

1. **Reinforcement learning with variable-length outputs**: During RL training, the model learns that longer reasoning chains are rewarded on hard problems but penalized (via cost) on easy ones
2. **Confidence calibration**: The model internally estimates its confidence and continues reasoning if confidence is below a threshold
3. **Trained stopping criteria**: The model has learned patterns like "I'm now confident" or "This checks out" as signals to stop reasoning

The result is **adaptive compute allocation** — the model spends its compute budget where it matters most.

### 4.7 Benchmark Results: The Proof Is in the Numbers

The impact of reasoning models on benchmarks has been staggering:

| Benchmark | GPT-4 (2023) | o1-preview | o1 | o3 |
|-----------|-------------|------------|-----|-----|
| AIME 2024 (math competition) | ~12% | ~44.6% | ~74.3% | ~96.7% |
| GPQA Diamond (grad-level science) | ~38% | ~73% | ~78% | ~87.7% |
| Codeforces (competitive programming) | ~11th percentile | ~62nd percentile | ~89th percentile | ~99th+ percentile |
| MATH benchmark | ~52% | ~85% | ~94.8% | ~96.7% |

These aren't incremental improvements — they represent **qualitative jumps** in capability. o3 on AIME 2024 performs at the level of top high-school math competitors. With tool access (Python interpreter), o3 achieves **98.7–99.5%** on AIME 2025.

---

## 5. DeepSeek-R1 — The Open-Source Reasoning Breakthrough

In January 2025, DeepSeek released R1, arguably the most important open-source AI model since Llama. The paper "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (arXiv: 2501.12948) revealed something remarkable: you can train a model to reason **purely through reinforcement learning**, without any human-labeled reasoning traces.

### 5.1 The Architecture: DeepSeek-V3 as Base

DeepSeek-R1 is built on DeepSeek-V3, a 671-billion parameter Mixture-of-Experts (MoE) model with 37 billion active parameters per token. The MoE architecture is crucial — it provides massive total capacity while keeping per-token compute manageable.

```
DeepSeek-V3 (671B total, 37B active)
         │
         │ Pure RL (no SFT on reasoning traces)
         ▼
DeepSeek-R1-Zero (emergent reasoning!)
         │
         │ + Cold-start SFT data + Multi-stage RL
         ▼
DeepSeek-R1 (production-quality reasoning)
         │
         │ Distillation
         ▼
R1-Distill-Qwen-{1.5B, 7B, 14B, 32B}
R1-Distill-Llama-{8B, 70B}
```

### 5.2 DeepSeek-R1-Zero: The Pure RL Experiment

The most scientifically remarkable contribution is **R1-Zero**: a model trained with RL directly on the base model, **without any supervised fine-tuning on reasoning traces**.

From the paper:

> *"DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step, demonstrates remarkable reasoning capabilities. Through RL, DeepSeek-R1-Zero naturally emerges with numerous powerful and intriguing reasoning behaviors."*

**The training setup**:
- **Base model**: DeepSeek-V3 (pre-trained on text, but never fine-tuned on reasoning data)
- **RL algorithm**: GRPO (Group Relative Policy Optimization)
- **Reward signals**: Rule-based, verifiable rewards (math answer correctness, code test-passing)
- **No human reasoning traces**: The model was never shown examples of step-by-step reasoning

**What emerged**:

The model spontaneously developed:

1. **Chain-of-thought reasoning**: Without being taught, R1-Zero began generating step-by-step solutions
2. **Self-verification**: The model learned to check its own work ("Let me verify this by plugging the answer back in...")
3. **Reflection**: "Wait, I think I made an error in step 3. Let me reconsider..."
4. **Backtracking**: The model learned to abandon unproductive approaches and try alternatives
5. **Problem decomposition**: Complex problems were spontaneously broken into sub-problems

### 5.3 The "Aha Moment"

The DeepSeek team described an "aha moment" during R1-Zero's training — a phase transition where the model suddenly discovered that **longer, more careful reasoning leads to higher rewards**:

Before the aha moment:
```
Q: What is the sum of the first 100 positive integers?
A: The sum is 5000.  [Wrong, and no reasoning shown]
```

After the aha moment:
```
Q: What is the sum of the first 100 positive integers?
A: I need to find 1 + 2 + 3 + ... + 100.
   I recall Gauss's formula: n(n+1)/2.
   So the sum = 100 × 101 / 2 = 10100 / 2 = 5050.
   Let me verify: pair up 1+100=101, 2+99=101, ..., 50+51=101.
   That's 50 pairs × 101 = 5050. ✓
   The answer is 5050.
```

This emergence is profound. The model wasn't *told* to reason step by step — it *discovered* that reasoning step by step leads to correct answers, which leads to higher rewards. **Reasoning emerged as an optimal strategy for reward maximization.**

The published training curves show this as a distinct phase transition: reasoning chain length suddenly increases, and simultaneously, accuracy on validation tasks jumps.

### 5.4 GRPO: Group Relative Policy Optimization

GRPO is DeepSeek's key algorithmic innovation — a variant of PPO (Proximal Policy Optimization) designed specifically for LLM reasoning.

**The problem with standard PPO for LLMs**:

PPO requires a **value network** (critic) that estimates the expected future reward from any given state. For LLMs:
- The "state" is the entire generated text so far — extremely high-dimensional
- Training an accurate value function is computationally expensive (essentially another LLM)
- Value function errors compound over long reasoning chains
- Memory cost is roughly **doubled** (policy + critic networks)

**GRPO's solution: eliminate the critic entirely**

Instead of learning a value function, GRPO estimates advantages **empirically** by generating a **group** of outputs for each prompt and comparing them to each other.

**The GRPO algorithm step by step**:

```
For each training prompt q:

1. SAMPLE: Generate G outputs {o_1, o_2, ..., o_G} from current policy π_θ
   
2. SCORE: Compute rewards {r_1, r_2, ..., r_G} using rule-based verifier
   (e.g., does the math answer match the ground truth?)

3. NORMALIZE: Compute advantages relative to the group:
   μ = mean(r_1, ..., r_G)
   σ = std(r_1, ..., r_G)
   A_i = (r_i - μ) / (σ + ε)     for each output i

4. UPDATE: Optimize the clipped surrogate objective with KL penalty:
   J_GRPO(θ) = (1/G) Σ_i [min(ρ_i · A_i, clip(ρ_i, 1-ε, 1+ε) · A_i)]
                         - β · D_KL(π_θ || π_ref)
   where ρ_i = π_θ(o_i|q) / π_old(o_i|q)
```

**Why this works for reasoning**:

- **No critic needed**: Saves ~40% memory and avoids compounding estimation errors
- **Group comparison is natural**: "This solution that got the right answer is better than those that didn't" — no learned value function needed
- **Handles variable-length output**: Long reasoning chains are compared as complete units
- **Works with binary rewards**: Even simple correct/incorrect signals are sufficient when you have group comparison

### 5.5 The Multi-Stage Training Pipeline

While R1-Zero demonstrated that reasoning emerges from pure RL, the production model (R1) used a more sophisticated pipeline to improve output quality:

**Stage 1: Cold-Start SFT**

A small amount of high-quality reasoning data (thousands of examples) is used for supervised fine-tuning. This provides:
- Consistent output formatting (proper `<think>...</think>` tags)
- Readable reasoning chains (R1-Zero's chains were functional but messy)
- Stability for subsequent RL training

**Stage 2: Reasoning-Focused RL**

Large-scale RL training on reasoning tasks (math, code, science) using GRPO with:
- Rule-based rewards for verifiable tasks
- Format compliance rewards
- Length penalties to prevent excessive verbosity

**Stage 3: Rejection Sampling + SFT**

Use the RL-trained model to generate many solutions for diverse prompts. Select the best solutions (via reward model or verifier) and fine-tune on these high-quality outputs. This:
- Improves performance on non-reasoning tasks (writing, summarization, etc.)
- Smooths out RL artifacts
- Produces more human-friendly output

**Stage 4: All-Scenario RL**

Final RL stage covering both reasoning and general helpfulness:
- Helpfulness and harmlessness rewards
- Reasoning accuracy rewards
- Format and style rewards

### 5.6 Distillation: Reasoning for Everyone

One of R1's most impactful contributions is **distillation** — transferring reasoning ability to much smaller models:

| Distilled Model | Parameters | AIME 2024 | MATH-500 | vs. OpenAI |
|----------------|-----------|-----------|----------|------------|
| R1-Distill-Qwen-1.5B | 1.5B | ~15% | ~83% | Competitive with GPT-4o on some tasks |
| R1-Distill-Qwen-7B | 7B | ~29% | ~92% | — |
| R1-Distill-Qwen-14B | 14B | ~47% | ~93% | — |
| R1-Distill-Qwen-32B | 32B | ~54% | ~94% | Outperforms o1-mini |
| R1-Distill-Llama-8B | 8B | ~32% | ~90% | — |
| R1-Distill-Llama-70B | 70B | ~62% | ~95% | Approaches o1 on some benchmarks |

**The distillation process**:
1. Use R1 to generate reasoning traces for a large dataset of problems
2. Fine-tune smaller base models (Qwen, Llama) on these (problem, reasoning_trace, answer) triples
3. The smaller model learns to **mimic the reasoning patterns** of the larger model

**A remarkable finding**: Distillation was more effective than RL for small models. Running RL directly on small models produced worse results than distilling reasoning from R1. This suggests that **the "discovery" of reasoning strategies requires a large model**, but once discovered, these strategies can be **compressed into smaller models** via supervised learning.

### 5.7 Key Differences: R1 vs. o1

| Aspect | OpenAI o1 | DeepSeek R1 |
|--------|----------|-------------|
| Architecture | Dense (GPT-based, ~200B est.) | MoE (671B total, 37B active) |
| Training | RL + proprietary methods | GRPO + multi-stage pipeline |
| Reasoning visibility | Hidden (summarized) | Open (full `<think>` traces) |
| Open weights | No | Yes (Apache 2.0) |
| Open paper | No full paper | Full paper with details |
| Critic/value network | Likely yes (PRM-based) | No (GRPO eliminates critic) |
| Distilled models | Not released | 6 models from 1.5B to 70B |

---

## 6. The Math Behind It

### 6.1 Reward Modeling for Reasoning

The fundamental challenge: **how do you reward "good reasoning"?**

**Rule-Based Rewards (DeepSeek approach)**:

For verifiable tasks, rewards are deterministic:

```
reward(output, ground_truth) = 
    1.0  if extract_answer(output) == ground_truth
    0.0  otherwise
```

For code:
```
reward(output, test_cases) = 
    fraction of test_cases that pass when executing extract_code(output)
```

Advantages: No reward model to train, no reward hacking, perfectly calibrated signals.
Limitation: Only works for tasks with verifiable answers.

**Learned Reward Models (OpenAI approach)**:

For tasks without ground-truth answers, train a reward model:

```
R(x, y) = f_φ(x, y)   where x = prompt, y = response
```

Trained via **Bradley-Terry model** on human preference data:

```
P(y_1 ≻ y_2 | x) = σ(R(x, y_1) - R(x, y_2))
```

Where σ is the sigmoid function and y_1 ≻ y_2 means "y_1 is preferred to y_2."

**Process Reward Models** extend this to step-level:

```
P(step_k is correct | x, step_1, ..., step_k) = σ(R_PRM(x, step_1, ..., step_k))
```

The overall solution score is typically the **product** (or minimum) of step scores:

```
Score(full_solution) = Π_k P(step_k is correct | prefix_k)
   or
Score(full_solution) = min_k P(step_k is correct | prefix_k)
```

The minimum formulation is more conservative: if any step is likely wrong, the whole solution is penalized.

### 6.2 The GRPO Objective in Detail

The full GRPO objective function:

```
J_GRPO(θ) = E_{q~D} [ (1/G) Σ_{i=1}^{G} L_clip(θ, o_i, q) - β · D_KL(π_θ(·|q) || π_ref(·|q)) ]
```

Where:

**Clipped surrogate loss** (same idea as PPO):
```
L_clip(θ, o_i, q) = min(
    ρ_i(θ) · Â_i,
    clip(ρ_i(θ), 1-ε, 1+ε) · Â_i
)

ρ_i(θ) = π_θ(o_i | q) / π_θ_old(o_i | q)    # probability ratio
```

**Group-normalized advantage**:
```
Â_i = (r_i - μ_G) / (σ_G + δ)

μ_G = (1/G) Σ_{j=1}^{G} r_j    # group mean reward
σ_G = std(r_1, ..., r_G)        # group standard deviation
δ = 1e-8                         # numerical stability
```

**KL divergence penalty**:
```
D_KL(π_θ || π_ref) = E_{o~π_θ} [ log(π_θ(o|q) / π_ref(o|q)) ]
```

In practice, this is estimated per-token:
```
D_KL ≈ (1/T) Σ_{t=1}^{T} [ log π_θ(o_t | o_{<t}, q) - log π_ref(o_t | o_{<t}, q) ]
```

### 6.3 Why the KL Penalty Matters

The KL divergence term `β · D_KL(π_θ || π_ref)` is critical and serves multiple purposes:

**1. Prevents mode collapse**: Without KL, the model collapses to always producing the single output with highest reward. The KL penalty keeps the output distribution diverse.

**2. Preserves language quality**: The reference policy π_ref is typically the base model (DeepSeek-V3). The KL penalty ensures the RL-trained model doesn't forget how to write coherent text.

**3. Controls exploration**: Higher β → more conservative updates → slower but more stable learning. Lower β → more aggressive exploration → faster learning but risk of instability.

**4. Prevents reward hacking**: Without KL, the model might find degenerate solutions that technically maximize reward but produce gibberish. The KL term anchors it to natural language.

**The β hyperparameter**:
- Too high: Model barely changes from the base; learning is too slow
- Too low: Model rapidly diverges, producing high-reward but nonsensical output
- Sweet spot: Model learns new reasoning behaviors while maintaining language quality

Typical values: β ∈ [0.001, 0.1], often annealed during training.

### 6.4 Why RL Produces Different Reasoning Than SFT

A profound question: why does RL training produce fundamentally different reasoning patterns than supervised fine-tuning (SFT) on human-written reasoning traces?

**SFT**: Model learns to **imitate** the distribution of training data.
```
θ_SFT = argmin_θ E_{(x,y)~D_human} [ -log π_θ(y|x) ]
```
This minimizes cross-entropy with human demonstrations. The model learns to produce outputs that look like the training data.

**RL (GRPO)**: Model learns to **maximize expected reward** while staying close to a reference.
```
θ_RL = argmax_θ E_{q~D, o~π_θ(·|q)} [ R(o, q) ] - β · D_KL(π_θ || π_ref)
```

**The key difference**: SFT copies human strategies. RL discovers optimal strategies.

This explains several empirical observations:

1. **RL models develop novel strategies**: R1-Zero discovered reasoning patterns not present in any training data
2. **RL models are better at self-correction**: Because correction is rewarded, not just imitated
3. **SFT has a ceiling**: You can't surpass the quality of your training demonstrations via imitation alone
4. **RL can surpass human performance**: By optimizing for outcomes, not mimicking human process

However, RL alone (R1-Zero) produces messy, hard-to-read reasoning. The practical solution is:
```
SFT (formatting + cold-start) → RL (capability improvement) → SFT (polishing)
```

### 6.5 Verification as a Natural Byproduct

One of the most elegant aspects of RL-trained reasoning is that **verification emerges naturally**.

**Why verification emerges**:
- The reward function is binary (correct/incorrect for the final answer)
- Wrong answers get zero reward regardless of how "close" they were
- A model that verifies its answer before committing catches errors that would waste the entire output's reward
- Therefore: **verification is incentivized because it improves expected reward**

In R1-Zero's outputs, researchers observed three types of emergent verification:

**1. Substitution checking**:
```
"I got x = 3. Let me verify: 2(3) + 1 = 7. Yes, that matches the equation. ✓"
```

**2. Alternative method verification**:
```
"I solved this algebraically and got 42. Let me verify numerically...
 Computing directly: 42. The answers match. ✓"
```

**3. Sanity checking**:
```
"I got the probability is 1.3. Wait, probabilities must be between 0 and 1.
 I must have made an error. Let me redo this..."
```

None of these behaviors were explicitly taught. They emerged because they increase the probability of correct final answers, which the RL reward signal reinforces.

---

## 7. The Broader Reasoning Ecosystem

The reasoning revolution extends far beyond o1 and R1. By mid-2025, reasoning capabilities have become a standard feature across leading AI systems.

### 7.1 The Reasoning Model Landscape

**Commercial**:
- **OpenAI o1/o3/o4-mini**: Pioneered commercial reasoning models; o3 achieves 96.7% on AIME 2024
- **Google Gemini 2.0 Flash Thinking**: Google's reasoning model with explicit thinking tokens
- **Anthropic Claude 3.5 Sonnet (extended thinking)**: Anthropic's approach to deliberative reasoning; the model can request more thinking time on hard problems
- **xAI Grok**: Incorporated reasoning capabilities in later versions

**Open-Source**:
- **DeepSeek R1/R1-Zero**: The gold standard for open reasoning; full paper, code, and weights
- **Qwen QwQ-32B**: Alibaba's reasoning model, competitive with o1-mini
- **R1-Distill family**: 6 distilled models from 1.5B to 70B parameters
- **Sky-T1**: Open reasoning model from Sky Computing Lab (UC Berkeley)
- **Open-R1 / Open-Reasoner community**: Community efforts to reproduce R1's training pipeline

### 7.2 The Convergence Pattern

Despite different approaches, all reasoning models converge on similar emergent behaviors:

1. **Long internal monologues**: All spend more tokens "thinking" on harder problems
2. **Self-correction**: All develop the ability to catch and fix their own errors
3. **Strategic exploration**: All learn to try multiple approaches when stuck
4. **Confidence-based stopping**: All learn to stop reasoning when confident

This convergence suggests these behaviors are **optimal strategies** for any system that:
- Has sufficient base capabilities (language understanding, knowledge)
- Is trained to maximize accuracy on verifiable tasks
- Is allowed variable-length output

### 7.3 The Verification Paradigm

A subtle but important shift: reasoning models have transformed AI from a **generation** paradigm to a **generation + verification** paradigm.

```
Old paradigm:  prompt → generate answer → done
New paradigm:  prompt → generate candidate → verify → (revise if wrong) → done
```

This is significant because **verification is often easier than generation**:
- It's hard to write a correct proof, but relatively easy to check if a proof is valid
- It's hard to write bug-free code, but relatively easy to run tests
- It's hard to solve a math problem, but easy to check an answer by substitution

Reasoning models exploit this **asymmetry** by generating candidates and verifying them, effectively turning difficult generation problems into easier verification problems.

---

## 8. Practical Implications

### 8.1 When to Use Reasoning Models vs. Standard Models

Not every task benefits from reasoning. Here's a practical guide:

| Task Type | Best Model Type | Why |
|-----------|----------------|-----|
| Simple Q&A, summarization | Standard (GPT-4o, Claude) | Fast, cheap, reasoning unnecessary |
| Creative writing | Standard | Reasoning doesn't help creativity much |
| Multi-step math | Reasoning (o1, R1) | Dramatic accuracy improvement |
| Complex coding | Reasoning | Better at debugging, edge cases |
| Scientific reasoning | Reasoning | Handles multi-step logical chains |
| Translation | Standard | Well-solved without explicit reasoning |
| Data extraction | Standard | Pattern matching, not reasoning |
| Strategic planning | Reasoning | Benefits from exploration and verification |

**Rule of thumb**: Use reasoning models when the task has a **verifiable correct answer** and requires **multiple logical steps** to reach it.

### 8.2 Cost-Accuracy Tradeoffs

Reasoning tokens are expensive. o1's hidden reasoning chain can generate **10,000+ tokens** of internal deliberation for a single problem. At ~$15/million output tokens (o1 pricing), a single hard problem might cost $0.15 — compared to $0.01 for a standard GPT-4o response.

**The cost structure of reasoning**:

```
Standard model:  ~100-500 output tokens  → $0.001-0.01 per query
Reasoning model: ~1000-50000 reasoning tokens + ~100-500 answer tokens
                                         → $0.02-1.00 per query
```

This creates a natural **tiering strategy**:

```
User query arrives
    │
    ├─ Easy? → Standard model (fast, cheap)
    │
    ├─ Medium? → Reasoning model, limited thinking budget
    │
    └─ Hard? → Reasoning model, extended thinking budget
```

Several approaches to managing cost:
1. **Difficulty classification**: Use a cheap model to estimate query difficulty, then route
2. **Thinking budgets**: Set maximum reasoning token limits
3. **Distilled models**: Use R1-Distill-32B instead of full R1 for most reasoning tasks
4. **Cached reasoning**: For repeated similar queries, cache reasoning patterns

### 8.3 Adaptive Compute Allocation

The most sophisticated deployment strategy is **adaptive compute allocation**:

```
Performance
    ↑
    │
    │  ████████████████████████ Full reasoning (expensive)
    │  ████████████████████     Medium reasoning
    │  ████████████████         Light reasoning  
    │  ██████████               Standard model
    │  ████                     Cached / trivial
    └──────────────────────────→ Query difficulty
```

This mirrors how human experts work: a mathematician doesn't show all their work for 2+2, but will fill pages of scratch work for a research problem.

### 8.4 Impact on Benchmarks: Before and After

The reasoning revolution has transformed AI benchmark performance:

**Math (AIME 2024)**:
- Pre-reasoning best (GPT-4, 2023): ~12%
- o1 (Sep 2024): ~74%
- o3 (Jan 2025): ~97%
- Human competition median: ~40%

**Graduate-Level Science (GPQA Diamond)**:
- Pre-reasoning best: ~38%
- o1: ~78%
- Expert humans: ~65%

**Competitive Programming (Codeforces)**:
- Pre-reasoning: ~11th percentile
- o1: ~89th percentile
- o3: ~99th+ percentile

**The pattern**: On tasks requiring deep reasoning, the improvement from standard to reasoning models exceeds the improvement from GPT-3 to GPT-4. Test-time compute scaling is **at least as powerful** as the training-time scaling that dominated the previous era.

---

## 9. Open Problems and Future Directions

### 9.1 Unsolved Challenges

**1. Faithfulness of reasoning chains**: Do models actually *use* their written reasoning, or is it a post-hoc rationalization? Research is mixed — there's evidence both that reasoning chains influence the answer AND that models sometimes produce correct reasoning followed by wrong answers (or wrong reasoning followed by right answers).

**2. Scaling limits**: Do inference-time scaling laws continue to hold as problems get harder? Early evidence suggests diminishing returns on extremely hard problems (e.g., open research problems in math). The model's base capability sets a ceiling that no amount of test-time compute can overcome.

**3. Beyond verifiable tasks**: Current reasoning models excel on tasks with clear correct answers (math, code). Extending reasoning to subjective tasks (ethics, creative work, nuanced judgment) remains challenging because verification is harder.

**4. Computational efficiency**: Generating 50,000 tokens of reasoning for one answer is expensive. Can we achieve similar performance with more efficient search algorithms? Can we compress reasoning chains?

**5. Safety of reasoning models**: Hidden reasoning chains create new safety challenges. A model might internally reason about how to manipulate a user while producing a seemingly innocent explanation. Monitoring and aligning hidden deliberation is an open research area.

### 9.2 Promising Directions

**1. Learned search policies**: Instead of using fixed search algorithms (MCTS, beam search), train models to learn their own search strategies end-to-end.

**2. Reasoning distillation at scale**: Can we distill reasoning into models small enough to run on phones? Early results with R1-Distill-Qwen-1.5B are encouraging.

**3. Multi-modal reasoning**: Extending chain-of-thought to vision, audio, and video — reasoning about what you see, hear, and perceive over time.

**4. Collaborative reasoning**: Multiple specialized reasoning agents working together, each bringing different expertise.

**5. Continuous self-improvement**: Models that generate their own training data through reasoning, creating a flywheel of improving capability — the "self-play" approach that worked so well in games.

**6. Reasoning with tools**: Combining chain-of-thought reasoning with tool use (code execution, web search, calculators) for even more powerful problem-solving. o3 with Python access achieves near-perfect scores on math competitions.

### 9.3 The Bigger Picture

The reasoning revolution represents a fundamental shift in how we think about AI capabilities:

```
Era 1 (2018-2022): Scale the model → Better average performance
Era 2 (2023-2025): Scale inference compute → Better worst-case performance  
Era 3 (2025+):     Scale both adaptively → Efficient, powerful reasoning on demand
```

We're moving from AI systems that are "smart on average" to AI systems that can "think hard when it matters." This mirrors the difference between human intuition (fast, cheap, usually right) and human deliberation (slow, expensive, handles hard cases) — Kahneman's System 1 and System 2 thinking.

The reasoning revolution may be the closest we've come to giving AI a System 2.

---

## 10. Key Papers & Sources

### Foundational Papers

| Paper | Authors | Year | Key Contribution |
|-------|---------|------|------------------|
| "Scaling Laws for Neural Language Models" | Kaplan et al. (OpenAI) | 2020 | Original training scaling laws |
| "Training Compute-Optimal Large Language Models" (Chinchilla) | Hoffmann et al. (DeepMind) | 2022 | Revised scaling: balance params and data |
| "Show Your Work: Scratchpads for Intermediate Computation" | Nye et al. | 2021 | Scratchpad concept for LLM reasoning |
| "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" | Wei et al. (Google) | 2022 | Chain-of-thought prompting |
| "Self-Consistency Improves Chain of Thought Reasoning in Language Models" | Wang et al. (Google) | 2023 | Majority voting over reasoning chains |
| "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" | Yao et al. | 2023 | Tree-structured reasoning search |
| "Let's Verify Step by Step" | Lightman et al. (OpenAI) | 2023 | Process reward models + PRM800K dataset |

### Inference-Time Scaling

| Paper | Authors | Year | Key Contribution |
|-------|---------|------|------------------|
| "Scaling LLM Test-Time Compute Optimally" | Snell et al. | 2024 | Inference-time scaling laws; small model + more inference > big model |
| "Inference Scaling Laws: An Empirical Analysis" | Wu et al. | 2025 (ICLR) | Pareto frontier of model size vs. inference compute |

### Reasoning Models

| Paper | Authors | Year | Key Contribution |
|-------|---------|------|------------------|
| "Learning to Reason with LLMs" (o1 blog post) | OpenAI | Sep 2024 | First commercial reasoning model |
| "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL" | DeepSeek | Jan 2025 | Open-source reasoning model; GRPO; emergent reasoning from RL |
| "DeepSeek-R1 incentivizes reasoning in LLMs through RL" | DeepSeek | 2025 (Nature) | Peer-reviewed publication in Nature |

### Key URLs

- Chain-of-Thought paper: https://arxiv.org/abs/2201.11903
- Self-Consistency paper: https://arxiv.org/abs/2203.11171
- Tree of Thoughts paper: https://arxiv.org/abs/2305.10601
- Let's Verify Step by Step: https://arxiv.org/abs/2305.20050
- Scaling LLM Test-Time Compute: https://arxiv.org/abs/2408.03314
- Chinchilla paper: https://arxiv.org/abs/2203.15556
- Kaplan Scaling Laws: https://arxiv.org/abs/2001.08361
- DeepSeek-R1 paper: https://arxiv.org/abs/2501.12948
- OpenAI o1 blog: https://openai.com/index/learning-to-reason-with-llms/
- OpenAI o3 announcement: https://openai.com/index/introducing-o3-and-o4-mini/
- Inference Scaling Laws (ICLR 2025): https://openreview.net/forum?id=HkcSKi4yTs
- Scratchpad paper (Nye et al.): https://arxiv.org/abs/2112.00114
- GRPO vs PPO explanation: https://tildalice.io/grpo-vs-ppo-llm-reasoning/
- DeepSeek R1 GRPO deep dive: https://blog.piax.org/deepseek-r1-theory-tutorial-architecture-grpo-kl-divergence/
- GRPO mathematical walkthrough: https://ai.gopubby.com/how-deepseek-r1-pushes-the-limits-of-language-models-a-mathematical-dive-into-group-relative-79dba9906f94

---

## 11. Concepts for the Knowledge Tree

### Core Concepts (Reasoning & Inference)
1. **Test-Time Compute** — Spending additional FLOPs during inference rather than training
2. **Inference-Time Scaling Laws** — Power-law relationship between inference compute and performance
3. **Chain-of-Thought (CoT) Prompting** — Eliciting step-by-step reasoning through prompting
4. **Self-Consistency** — Majority voting over multiple sampled reasoning chains
5. **Tree of Thoughts (ToT)** — Tree-structured exploration of reasoning paths
6. **Scratchpad Reasoning** — Using generated text as intermediate computation memory
7. **Process Reward Model (PRM)** — Step-level verification and scoring of reasoning
8. **Outcome Reward Model (ORM)** — Final-answer-only verification and scoring
9. **Reasoning Tokens / Thinking Tokens** — Hidden internal deliberation tokens in reasoning models
10. **Adaptive Compute Allocation** — Spending more compute on harder problems

### Reinforcement Learning for Reasoning
11. **GRPO (Group Relative Policy Optimization)** — Critic-free RL algorithm using group-based advantages
12. **PPO (Proximal Policy Optimization)** — Standard RL algorithm with clipped surrogate objective
13. **KL Divergence Penalty** — Regularization to keep RL policy close to reference model
14. **Reward Hacking** — Models exploiting reward function loopholes
15. **Emergent Reasoning** — Reasoning behaviors arising from RL without explicit supervision
16. **Rule-Based Rewards** — Deterministic verification signals (math answer match, code test pass)

### Search & Verification
17. **Monte Carlo Tree Search (MCTS)** — Tree search algorithm using random sampling for node evaluation
18. **Beam Search over Reasoning Steps** — Maintaining top-k reasoning paths at each step
19. **Self-Verification** — Model checking its own answers for correctness
20. **Backtracking** — Abandoning wrong reasoning paths and trying alternatives
21. **Best-of-N Sampling** — Generating N candidates and selecting the best via a verifier

### Models & Systems
22. **OpenAI o1/o3** — Commercial reasoning models with hidden chain-of-thought
23. **DeepSeek-R1** — Open-source reasoning model trained with GRPO
24. **DeepSeek-R1-Zero** — Pure RL reasoning model (no SFT on reasoning traces)
25. **R1-Distill** — Smaller models distilled from R1's reasoning capabilities
26. **Reasoning Distillation** — Transferring reasoning ability from large to small models via SFT on generated traces
27. **Mixture-of-Experts (MoE)** — Architecture with many parameters but sparse activation (used by R1)

### Meta-Concepts
28. **System 1 vs System 2 Thinking** — Fast intuition vs. slow deliberation (Kahneman), analogous to standard vs. reasoning models
29. **Generation-Verification Asymmetry** — It's easier to verify a solution than to generate one; reasoning models exploit this
30. **Training-Inference Compute Tradeoff** — You can trade training FLOPs for inference FLOPs and sometimes come out ahead
31. **The Aha Moment** — Phase transition during RL training when a model discovers that reasoning leads to higher rewards
32. **Chinchilla Scaling Laws** — Compute-optimal training allocation (params ∝ data); the predecessor paradigm to inference scaling

---

## Appendix A: Timeline of the Reasoning Revolution

```
2020  ─── Kaplan et al.: Training scaling laws (bigger = better)
  │
2021  ─── Nye et al.: Scratchpad — models can use their output as working memory
  │
2022  ─── Hoffmann et al. (Chinchilla): Revised scaling (balance size and data)
  │   ─── Wei et al.: Chain-of-thought prompting (just say "think step by step")
  │
2023  ─── Wang et al.: Self-consistency (sample many chains, vote on answer)
  │   ─── Yao et al.: Tree of Thoughts (explore reasoning as a tree)
  │   ─── Lightman et al.: Let's Verify Step by Step (PRMs >> ORMs)
  │   ─── PRM800K dataset released
  │
2024  ─── Snell et al.: Inference-time scaling laws formalized
  │   ─── OpenAI releases o1-preview (Sep) — first commercial reasoning model
  │   ─── OpenAI releases o1 (Dec) — full reasoning model
  │   ─── Community explores MCTS + LLM combinations
  │
2025  ─── DeepSeek releases R1 (Jan) — open-source reasoning breakthrough
  │   ─── R1-Zero shows reasoning emerges from pure RL
  │   ─── R1-Distill models democratize reasoning (1.5B to 70B)
  │   ─── Wu et al.: Inference scaling laws (ICLR 2025)
  │   ─── OpenAI releases o3 — 96.7% on AIME 2024
  │   ─── Reasoning capabilities spread across all major AI labs
  │   ─── Nature publishes DeepSeek-R1's results
  │   ─── Industry shifts to adaptive compute allocation
```

---

## Appendix B: Comparing the Two Paradigms

```
┌─────────────────────────────────────────────────────────────────┐
│              TRAINING-TIME SCALING (2018-2023)                  │
│                                                                 │
│  Strategy: Make the model bigger and train on more data         │
│  Cost: Paid once at training time (millions of $$$)             │
│  Benefit: Better AVERAGE performance across all tasks           │
│  Limitation: Same compute for easy and hard queries             │
│  Metaphor: Building a bigger brain                              │
│                                                                 │
│  GPT-2 (1.5B) → GPT-3 (175B) → PaLM (540B) → GPT-4 (~1.8T)  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│              INFERENCE-TIME SCALING (2024+)                     │
│                                                                 │
│  Strategy: Let the model think longer on hard problems          │
│  Cost: Paid per-query, proportional to difficulty               │
│  Benefit: Better WORST-CASE performance on hard problems        │
│  Limitation: Expensive for reasoning-heavy queries              │
│  Metaphor: Thinking harder with the brain you have              │
│                                                                 │
│  o1 → o3 → R1 → adaptive systems → ???                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix C: A Minimal Reasoning System (Conceptual)

For those who want to build intuition, here's how you could construct a minimal reasoning system from scratch:

```python
# Conceptual pseudocode for a minimal reasoning system

def reasoning_system(problem, base_model, verifier, budget):
    """
    A minimal reasoning system that trades inference compute for accuracy.
    
    Args:
        problem: The input question/problem
        base_model: An LLM that generates reasoning chains
        verifier: A PRM that scores reasoning quality  
        budget: Maximum number of candidate solutions to generate
    """
    
    candidates = []
    
    for i in range(budget):
        # Generate a candidate reasoning chain + answer
        chain = base_model.generate(
            prompt=f"Think step by step to solve:\n{problem}",
            temperature=0.7,  # diversity for exploration
            max_tokens=2048
        )
        
        # Score each step in the chain with the PRM
        steps = split_into_steps(chain)
        step_scores = [verifier.score(problem, steps[:k+1]) 
                       for k in range(len(steps))]
        
        # Overall score = minimum step score (conservative)
        overall_score = min(step_scores)
        
        candidates.append({
            'chain': chain,
            'answer': extract_answer(chain),
            'score': overall_score,
            'step_scores': step_scores
        })
    
    # Select best candidate by verifier score
    best = max(candidates, key=lambda c: c['score'])
    
    # Optional: majority voting as tiebreaker
    answers = [c['answer'] for c in candidates]
    most_common = majority_vote(answers)
    
    # Return best-scored answer, with majority vote as backup
    if best['score'] > confidence_threshold:
        return best['answer'], best['chain']
    else:
        return most_common, "Low confidence — used majority voting"


def adaptive_reasoning(problem, base_model, verifier):
    """
    Adaptive compute: spend more on harder problems.
    """
    # Quick attempt with small budget
    answer, chain = reasoning_system(problem, base_model, verifier, budget=1)
    score = verifier.score_full(problem, chain)
    
    if score > 0.95:
        return answer  # Easy problem, done
    
    # Medium difficulty: try harder
    answer, chain = reasoning_system(problem, base_model, verifier, budget=8)
    score = verifier.score_full(problem, chain)
    
    if score > 0.85:
        return answer  # Got it with moderate effort
    
    # Hard problem: maximum effort
    answer, chain = reasoning_system(problem, base_model, verifier, budget=64)
    return answer
```

This captures the essence of the reasoning revolution: **generate, verify, and spend compute adaptively based on difficulty**. Production systems like o1 and R1 are vastly more sophisticated (learned search policies, internal deliberation, RL-trained reasoning strategies), but the core principle is the same.

---

*Last updated: July 2025*
*This document synthesizes research from 15+ papers and technical sources to provide a comprehensive overview of the test-time compute and reasoning revolution in AI. For corrections or additions, refer to the original papers linked in Section 10.*
