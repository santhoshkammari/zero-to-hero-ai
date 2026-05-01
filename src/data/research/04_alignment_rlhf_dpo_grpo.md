# Post-Training Alignment: RLHF → DPO → GRPO

## The Evolution of Making Models Helpful, Harmless, and Honest

---

## Why This Matters

A raw pretrained language model is like a brilliant savant with no social skills. It has absorbed
the entire internet — the good, the bad, the toxic, the brilliant — and it will happily regurgitate
any of it without judgment. Ask it to help you write a poem? It might. Ask it to help you do
something dangerous? It might do that too. It has no concept of "should."

**Alignment is the bridge between capability and usefulness.**

The pretrained model *can* do almost anything with language. Alignment teaches it what it
*should* do. This is the difference between GPT-3 (powerful but erratic) and ChatGPT (powerful
and helpful). Same base architecture. Same parameters. The difference? Post-training alignment.

And here's the kicker: alignment isn't just about safety. **Aligned models are often more capable
than their unaligned counterparts on downstream tasks.** This is the "alignment bonus" — by
teaching a model to be helpful, you often make it better at everything. InstructGPT (1.3B
parameters, aligned) was preferred by humans over GPT-3 (175B parameters, unaligned). Let
that sink in: a model 100x smaller was *preferred* because it was aligned.

The evolution from RLHF to DPO to GRPO represents one of the most important threads in
modern AI — the quest to make powerful models reliably beneficial. Each step simplifies the
process, reduces cost, and often improves results. Understanding this evolution is essential for
anyone building, deploying, or thinking critically about AI systems.

---

## The Post-Training Pipeline

### The Three Stages of Building a Useful LLM

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   PRETRAINING    │────▶│       SFT        │────▶│    ALIGNMENT     │
│                  │     │                  │     │                  │
│ Learn language   │     │ Learn to follow  │     │ Learn what       │
│ and knowledge    │     │ instructions     │     │ humans prefer    │
│                  │     │                  │     │                  │
│ Objective:       │     │ Objective:       │     │ Objective:       │
│ Next-token       │     │ Cross-entropy on │     │ Maximize human   │
│ prediction       │     │ demonstration    │     │ preference       │
│                  │     │ data             │     │ scores           │
│ Data: Trillions  │     │ Data: ~100K      │     │ Data: ~50K       │
│ of tokens from   │     │ high-quality     │     │ comparison       │
│ the web          │     │ (prompt,response)│     │ pairs            │
│                  │     │ pairs            │     │                  │
│ Cost: $$$$$      │     │ Cost: $$         │     │ Cost: $-$$$      │
│                  │     │                  │     │ (method-dependent)│
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

### Stage 1: Pretraining — The Foundation

Pretraining creates a model that understands language deeply. The objective is simple:

```
L_pretrain = -∑ log P(x_t | x_1, x_2, ..., x_{t-1})
```

Predict the next token, given all previous tokens. Do this over trillions of tokens. The result is a
model with vast knowledge of language, facts, reasoning patterns, code, math — everything it saw
in training data.

**But the model has no notion of "helpful."** It's trained to predict what text *comes next*, not
what text *should* come next. If the training data includes toxic forum posts, it'll complete
prompts in that style. If it includes scientific papers, it'll do that too. It mirrors whatever
distribution it was trained on.

### Stage 2: Supervised Fine-Tuning (SFT) — Learning to Follow Instructions

SFT takes the pretrained model and teaches it to follow instructions by training on curated
(prompt, response) pairs written by human demonstrators:

```
L_SFT = -∑ log P_θ(y_t | x, y_1, ..., y_{t-1})
```

Where `x` is the prompt and `y` is the desired response. This is just standard cross-entropy loss,
but on carefully curated data.

**SFT transforms the model from a text completer into an instruction follower.** After SFT, the
model can answer questions, write code, summarize text — it "gets" the format of helpful
interaction.

### Why SFT Alone Isn't Enough

SFT has fundamental limitations:

1. **Imitation ≠ Understanding**: SFT teaches the model to mimic the *form* of good responses,
   not to understand *why* a response is good. It learns surface patterns, not deep preferences.

2. **Bounded by demonstrator quality**: The model can never be better than its training data. If
   demonstrators make subtle errors or have inconsistent styles, the model inherits those flaws.

3. **No notion of relative quality**: SFT treats all training examples as equally good. It can't
   learn that response A is *better than* response B — only that response A exists.

4. **Distribution mismatch**: During training, the model sees only gold-standard responses. At
   inference time, it generates its own (often imperfect) responses. This train-test mismatch
   (called **exposure bias**) means errors can compound.

5. **Cannot optimize for nuanced preferences**: Humans don't just want "correct" — they want
   concise, well-structured, appropriately cautious, and contextually sensitive responses. These
   preferences are hard to capture in demonstration data alone.

**This is why we need alignment: to teach the model not just what good responses look like, but
what makes one response better than another.**

---

## RLHF — The Original Alignment Method

### The Core Idea

RLHF (Reinforcement Learning from Human Feedback) was the breakthrough that turned GPT-3
into ChatGPT. The key insight: **instead of telling the model what to say, let humans judge what
it says, then optimize for those judgments.**

This is a fundamentally different learning signal. SFT says "this is a good response." RLHF says
"this response is better than that one." The difference is profound — comparison is easier than
generation, and humans are much better at judging quality than producing optimal text.

### The RLHF Pipeline

```
Step 1: Collect Comparisons
┌─────────────────────────────────────────────────────┐
│ Prompt: "Explain quantum computing simply"          │
│                                                     │
│ Response A: [Model-generated response 1]            │
│ Response B: [Model-generated response 2]            │
│                                                     │
│ Human annotator: "A is better than B" ✓             │
└─────────────────────────────────────────────────────┘

Step 2: Train Reward Model
┌─────────────────────────────────────────────────────┐
│ Input: (prompt, response) → Scalar reward score     │
│                                                     │
│ Trained to predict: P(y_w ≻ y_l | x)               │
│ using Bradley-Terry model                           │
└─────────────────────────────────────────────────────┘

Step 3: Optimize Policy with PPO
┌─────────────────────────────────────────────────────┐
│ Generate responses → Score with reward model        │
│ → Update policy to maximize reward                  │
│ → Constrain with KL penalty to stay near SFT model  │
└─────────────────────────────────────────────────────┘
```

### Step 1: The Reward Model and Bradley-Terry

The reward model is trained on human comparison data using the **Bradley-Terry model** of
pairwise preferences. Given a prompt `x` and two responses `y_w` (preferred) and `y_l`
(dispreferred), the probability of the human preference is modeled as:

```
P(y_w ≻ y_l | x) = σ(r_θ(x, y_w) - r_θ(x, y_l))
```

Where:
- `r_θ(x, y)` is the scalar reward assigned by the reward model
- `σ` is the sigmoid function: `σ(z) = 1/(1 + exp(-z))`

This is equivalent to:

```
P(y_w ≻ y_l | x) = exp(r_θ(x, y_w)) / (exp(r_θ(x, y_w)) + exp(r_θ(x, y_l)))
```

The reward model is trained by minimizing the negative log-likelihood over the comparison dataset:

```
L_RM(θ) = -E_{(x, y_w, y_l) ~ D} [log σ(r_θ(x, y_w) - r_θ(x, y_l))]
```

**Why Bradley-Terry?** It's the simplest model that converts pairwise comparisons into a scalar
score. Each response gets a "strength" parameter, and the probability of one beating another
depends on the difference in strengths. It's the same model used in chess ratings (Elo), sports
rankings, and tournament seedings.

The reward model is typically initialized from the SFT model itself — you take the language model,
remove the language modeling head, and add a scalar output head. This gives the reward model a
deep understanding of language that helps it judge response quality.

### Step 2: PPO — Proximal Policy Optimization

With a trained reward model, we can now optimize the language model (the "policy" π_θ) to
generate responses that score highly. This is a reinforcement learning problem:

- **State**: The prompt `x` plus tokens generated so far
- **Action**: The next token to generate
- **Reward**: The reward model's score for the complete response

The RLHF objective that PPO optimizes:

```
max_θ  E_{x ~ D, y ~ π_θ(·|x)} [r_RM(x, y) - β · KL(π_θ(·|x) ‖ π_ref(·|x))]
```

Where:
- `r_RM(x, y)` is the reward model score
- `β` is the KL penalty coefficient
- `π_ref` is the reference policy (the SFT model, frozen)
- `KL(π_θ ‖ π_ref)` is the KL divergence between current and reference policy

**PPO's surrogate objective** (the actual optimization target at each step):

```
L^PPO(θ) = E_t [min(ρ_t(θ) · Â_t, clip(ρ_t(θ), 1-ε, 1+ε) · Â_t)]
```

Where:
- `ρ_t(θ) = π_θ(a_t|s_t) / π_old(a_t|s_t)` is the probability ratio
- `Â_t` is the estimated advantage (how much better this action is than average)
- `ε` is the clipping hyperparameter (typically 0.1-0.2)
- The `min` and `clip` ensure the policy doesn't change too drastically in one step

**The clipping is crucial.** Without it, RL training of language models is incredibly unstable. The
policy can collapse, generating the same response for every prompt, or it can exploit the reward
model's weaknesses. PPO's conservative updates are what make RLHF feasible at all.

### The KL Penalty — Why It's Essential

The KL penalty `β · KL(π_θ ‖ π_ref)` is perhaps the most important component of RLHF. Without
it, the model would **reward hack** — finding degenerate outputs that score highly on the reward
model but are nonsensical or useless to humans.

```
KL(π_θ(·|x) ‖ π_ref(·|x)) = E_{y ~ π_θ} [log(π_θ(y|x) / π_ref(y|x))]
```

The KL penalty says: "Maximize reward, but don't stray too far from the SFT model." This serves
multiple purposes:

1. **Prevents reward hacking**: The reward model is imperfect. Without the KL constraint, the
   policy would find adversarial inputs that exploit the reward model's blind spots — responses
   that score highly but are actually terrible.

2. **Preserves language quality**: The SFT model already produces fluent, coherent text. The KL
   constraint ensures the aligned model maintains that fluency.

3. **Regularization**: It prevents the policy from collapsing to a single high-reward response
   for each prompt, maintaining diversity in generations.

4. **Goodhart's Law defense**: "When a measure becomes a target, it ceases to be a good
   measure." The reward model is a proxy for human judgment. Optimizing it too hard inevitably
   degrades the thing it's supposed to measure.

### InstructGPT and ChatGPT's Secret Sauce

**InstructGPT** (Ouyang et al., 2022) was the paper that demonstrated RLHF at scale. Key findings:

- InstructGPT 1.3B (RLHF-aligned) was **preferred over GPT-3 175B** (unaligned) by human raters
- The alignment process improved truthfulness, reduced toxic outputs, and improved instruction-following
- A team of ~40 human labelers produced comparison data
- The SFT dataset contained ~13K demonstrations
- The comparison dataset contained ~33K comparisons
- Training used PPO with a KL penalty coefficient β ≈ 0.02

**ChatGPT** built on this foundation, applying RLHF to GPT-3.5 with:
- Larger and more diverse comparison datasets
- More sophisticated reward modeling
- Iterative RLHF — multiple rounds of data collection and training
- Careful human labeler guidelines emphasizing helpfulness, harmlessness, and honesty

### Problems with RLHF

Despite its success, RLHF has significant challenges:

**1. Reward Hacking (Goodhart's Law)**
The model finds ways to game the reward model rather than genuinely improving:
- Generating overly verbose responses (longer ≈ higher reward in many reward models)
- Using sycophantic language ("What a great question!")
- Avoiding answering to appear "safe" (excessive refusals)
- Inserting reward-model-pleasing phrases regardless of context

**2. Training Instability**
- PPO is notoriously difficult to tune for language models
- Training can diverge, producing gibberish or repetitive outputs
- Reward model scores can become miscalibrated as the policy drifts
- Hyperparameter sensitivity is extreme — small changes in β, learning rate, or batch size
  can dramatically change outcomes

**3. Computational Cost**
RLHF requires running **four models simultaneously**:
- The policy model (being trained)
- The reference model (frozen SFT model for KL computation)
- The reward model (for scoring)
- The value model/critic (for advantage estimation in PPO)

For a 70B parameter model, this means loading ~280B parameters into GPU memory. This is
extraordinarily expensive.

**4. Reward Model Bottleneck**
- Training a good reward model requires extensive, expensive human annotation
- The reward model has a fixed capacity — it can't perfectly represent all human preferences
- As the policy improves, the reward model may become less informative (ceiling effect)
- Different annotators have different preferences, introducing noise

**5. Complexity**
The multi-stage pipeline (SFT → Reward Model → PPO) has many moving parts, each with its own
hyperparameters, data requirements, and failure modes. Debugging is extremely difficult.

These problems motivated the search for simpler alignment methods — leading to DPO.

---

## DPO — Direct Preference Optimization

### The Key Insight: You Don't NEED a Separate Reward Model

In May 2023, Rafailov et al. published one of the most influential papers in alignment research:
"Direct Preference Optimization: Your Language Model is Secretly a Reward Model."

The insight is elegant and mathematical. Recall the RLHF objective:

```
max_θ  E_{x ~ D, y ~ π_θ(·|x)} [r(x, y) - β · KL(π_θ(·|x) ‖ π_ref(·|x))]
```

This is a KL-constrained reward maximization problem. It turns out this problem has a **closed-form
solution**. The optimal policy π* for a given reward function r is:

```
π*(y|x) = (1/Z(x)) · π_ref(y|x) · exp(r(x, y) / β)
```

Where `Z(x)` is a normalization constant (partition function).

**Now here's the magic.** If we rearrange this equation and solve for the reward:

```
r(x, y) = β · log(π*(y|x) / π_ref(y|x)) + β · log Z(x)
```

This means: **the reward function is implicitly defined by the policy itself.** The reward for any
response is proportional to how much more likely the optimal policy makes it compared to the
reference policy.

### The DPO Derivation

Since the reward is defined by the policy, we can substitute it back into the Bradley-Terry
preference model. Recall:

```
P(y_w ≻ y_l | x) = σ(r(x, y_w) - r(x, y_l))
```

Substituting the implicit reward:

```
r(x, y_w) - r(x, y_l) = β · [log(π_θ(y_w|x)/π_ref(y_w|x)) - log(π_θ(y_l|x)/π_ref(y_l|x))]
```

Note that `β · log Z(x)` cancels out because it doesn't depend on `y`!

This gives us the **DPO loss function**:

```
L_DPO(θ) = -E_{(x, y_w, y_l) ~ D} [log σ(β · (log(π_θ(y_w|x)/π_ref(y_w|x))
                                              - log(π_θ(y_l|x)/π_ref(y_l|x))))]
```

Let's define the **implicit reward** for notational clarity:

```
r̂(x, y) = β · log(π_θ(y|x) / π_ref(y|x))
```

Then:

```
L_DPO(θ) = -E_{(x, y_w, y_l) ~ D} [log σ(r̂(x, y_w) - r̂(x, y_l))]
```

### What This Means in Practice

The DPO loss is saying: **increase the relative probability of preferred responses (compared to
the reference model) and decrease the relative probability of dispreferred responses.**

For each training example (x, y_w, y_l):
- Compute log π_θ(y_w|x) and log π_θ(y_l|x) — forward pass on both responses
- Compute log π_ref(y_w|x) and log π_ref(y_l|x) — forward pass on reference model (cached)
- Take the difference of log-ratios
- Apply sigmoid and log — this is the loss

**No reward model. No RL. No PPO. No value network. Just supervised learning on preference
pairs.**

```
RLHF Pipeline:                          DPO Pipeline:
┌───────────┐                           ┌───────────┐
│ SFT Model │                           │ SFT Model │
└─────┬─────┘                           └─────┬─────┘
      │                                       │
      ▼                                       │
┌───────────┐                                 │
│  Reward   │                                 │
│  Model    │                                 │
└─────┬─────┘                                 │
      │                                       │
      ▼                                       ▼
┌───────────┐                           ┌───────────┐
│PPO + Value│                           │ DPO Loss  │
│  Network  │                           │ (direct)  │
└─────┬─────┘                           └─────┬─────┘
      │                                       │
      ▼                                       ▼
┌───────────┐                           ┌───────────┐
│  Aligned  │                           │  Aligned  │
│  Model    │                           │  Model    │
└───────────┘                           └───────────┘
 4 models loaded                         2 models loaded
 Complex RL loop                         Simple supervised training
 Unstable                                Stable
```

### The Gradient of DPO

The gradient of the DPO loss reveals its behavior:

```
∇_θ L_DPO = -β · E [σ(-r̂_w + r̂_l) · (∇_θ log π_θ(y_w|x) - ∇_θ log π_θ(y_l|x))]
```

Where `σ(-r̂_w + r̂_l)` acts as a **weighting factor**:
- When the model already correctly ranks y_w above y_l (high implicit reward gap), this weight
  is small — the model doesn't need much updating
- When the model incorrectly ranks them (low or negative gap), the weight is large — focus
  learning on the mistakes

This is elegant: **DPO automatically focuses learning on the examples where the model most
disagrees with human preferences.** This is impossible in standard SFT, which treats all examples
equally.

### Why DPO is Simpler, Cheaper, and Often as Good

**Simpler:**
- No reward model training stage
- No RL loop with its many hyperparameters
- No value network / critic
- Standard supervised training — any framework that can do fine-tuning can do DPO

**Cheaper:**
- Only 2 models in memory (policy + reference) vs 4 for RLHF
- No online generation during training (RLHF requires generating responses at each step)
- Fewer hyperparameters to tune
- Faster convergence in practice

**Effective:**
- Matches or exceeds RLHF on many benchmarks
- More stable training — no RL divergence issues
- The implicit KL constraint (via the reference model in the log-ratio) provides natural
  regularization

**But DPO has limitations too:**
- Requires paired preference data (y_w and y_l for the same prompt)
- Can overfit to the preference dataset
- The fixed reference model means the KL constraint is static
- May not capture complex, multi-dimensional preferences as well as a learned reward model
- Less effective for online/iterative improvement compared to RLHF

### DPO Variants: The Alignment Method Zoo

The success of DPO spawned a wave of variants, each addressing specific limitations:

#### IPO — Identity Preference Optimization (Azar et al., 2023)

**Problem with DPO:** DPO can overfit to preference data because the Bradley-Terry model
assumption may not hold exactly. When the model becomes very confident, the sigmoid saturates,
and gradients vanish.

**IPO's fix:** Replace the log-sigmoid loss with a squared loss that explicitly regularizes:

```
L_IPO(θ) = E [(log(π_θ(y_w|x)/π_ref(y_w|x)) - log(π_θ(y_l|x)/π_ref(y_l|x)) - 1/(2β))²]
```

IPO separates the preference optimization from KL regularization, making each tunable
independently. It directly targets a specific margin between preferred and dispreferred responses
rather than driving the gap to infinity.

#### KTO — Kahneman-Tversky Optimization (Ethayarajh et al., 2024)

**Problem:** DPO requires *paired* preferences (y_w, y_l for each prompt). In practice, it's much
easier to collect *pointwise* feedback — just "this response is good" or "this response is bad."

**KTO's insight:** Humans evaluate outcomes relative to a reference point, with **loss aversion**
(losses loom larger than gains). This is **prospect theory** from behavioral economics.

```
Value function (Kahneman-Tversky):

v(z) = { (z - z_ref)^α           if z ≥ z_ref     (gains: concave)
        { -λ(z_ref - z)^α         if z < z_ref     (losses: convex, steeper)

Where λ > 1 encodes loss aversion, α ∈ (0,1] controls diminishing sensitivity
```

KTO applies this to alignment:
- Good outputs are "gains" — the model should increase their probability
- Bad outputs are "losses" — the model should decrease their probability more aggressively (loss aversion)
- The reference point is the expected reward under the reference model

**Key advantage:** KTO works with **unpaired binary feedback** — just thumbs up/thumbs down.
No need to compare two responses to the same prompt. This dramatically reduces data collection
cost and makes real-world deployment much easier.

#### ORPO — Odds Ratio Preference Optimization (Hong et al., 2024)

**Problem:** DPO requires a separate SFT stage, then a preference optimization stage, and
needs a reference model in memory.

**ORPO's fix:** Combine SFT and preference optimization in a single training stage, and eliminate
the need for a reference model entirely:

```
L_ORPO = L_SFT + λ · L_odds_ratio

Where L_odds_ratio encourages higher odds for preferred responses:
odds(y|x) = P_θ(y|x) / (1 - P_θ(y|x))

L_odds_ratio = -log σ(log(odds(y_w|x) / odds(y_l|x)))
```

| Feature           | DPO | ORPO |
|-------------------|-----|------|
| Separate SFT      | Yes | No   |
| Reference model   | Yes | No   |
| Training stages   | 2   | 1    |
| Memory overhead   | 2x  | 1x   |

#### SimPO — Simple Preference Optimization (2024)

**Problem:** DPO's implicit reward (log-ratio with reference model) doesn't account for response
length. Longer responses get unfairly high implicit rewards because they have more tokens
contributing to the log-probability.

**SimPO's fix:** Use length-normalized average log-probability as the implicit reward, plus an
explicit target reward margin:

```
SimPO implicit reward:
r̂(x, y) = (1/|y|) · ∑_t log π_θ(y_t | x, y_<t)

L_SimPO = -log σ(β · (r̂(x, y_w) - r̂(x, y_l) - γ))
```

Where:
- `|y|` is the response length (number of tokens)
- `γ` is the target reward margin (hyperparameter)
- No reference model needed! The reward is based purely on the policy's own log-probabilities

SimPO is perhaps the simplest of all — it doesn't even need a reference model, yet achieves
competitive performance.

### Summary: The DPO Family

```
Method  | Paired Data? | Reference Model? | Separate SFT? | Key Innovation
--------|-------------|-----------------|---------------|---------------------------
DPO     | Yes         | Yes             | Yes           | Eliminate reward model + RL
IPO     | Yes         | Yes             | Yes           | Better regularization
KTO     | No          | Yes             | Yes           | Unpaired binary feedback
ORPO    | Yes         | No              | No            | Single-stage, no reference
SimPO   | Yes         | No              | Yes           | Length-normalized reward
```

---

## GRPO — Group Relative Policy Optimization

### DeepSeek's Breakthrough for Reasoning

In early 2025, DeepSeek released R1, a model that matched or exceeded frontier models on
reasoning benchmarks — at a fraction of the training cost. The secret? **GRPO (Group Relative
Policy Optimization)**, an elegantly simple alternative to both RLHF and DPO that proved
particularly effective at eliciting *emergent reasoning* capabilities.

GRPO was introduced in the DeepSeek-Math paper and then scaled to train DeepSeek-R1. It
represents a fundamentally different philosophy: instead of learning from human preference
comparisons, **learn from the model's own outputs by comparing them against each other.**

### The Core Idea

For each prompt, generate a **group** of responses. Some will be better, some worse. Score them
all. Then optimize the policy to make the good ones more likely and the bad ones less likely,
with the advantage computed **relative to the group**.

```
GRPO Pipeline:
┌──────────────────────────────────────────────────────────────────┐
│ For each prompt x:                                              │
│                                                                  │
│ 1. Sample G responses: {y_1, y_2, ..., y_G} ~ π_old(·|x)      │
│                                                                  │
│ 2. Score each: r_1, r_2, ..., r_G  (reward model or verifier)  │
│                                                                  │
│ 3. Compute group-relative advantages:                           │
│    Â_i = (r_i - mean(r)) / std(r)                               │
│                                                                  │
│ 4. Update policy using PPO-style clipped objective              │
│    with group-relative advantages                               │
└──────────────────────────────────────────────────────────────────┘
```

### How GRPO Works in Detail

**Step 1: Group Sampling**

For each prompt `x`, sample `G` complete responses from the current policy (or a slightly older
version of it):

```
{y_1, y_2, ..., y_G} ~ π_old(·|x)
```

Typical group sizes: G = 16 to 64. This is the "group" in Group Relative Policy Optimization.

**Step 2: Reward Scoring**

Each response is scored. For reasoning tasks, this can be:
- A reward model (like in RLHF)
- A **rule-based verifier** (check if the final answer is correct)
- A combination

For math problems, the verifier just checks if the answer is right:
`r_i = 1` if correct, `r_i = 0` if incorrect. Simple, cheap, and noise-free.

**Step 3: Group-Relative Advantage Estimation**

This is the key innovation. Instead of using a learned value function (critic network) to estimate
advantages, GRPO computes advantages **relative to the group**:

```
Â_i = (r_i - μ_G) / σ_G
```

Where:
- `μ_G = (1/G) · ∑_j r_j` is the group mean reward
- `σ_G = sqrt((1/G) · ∑_j (r_j - μ_G)²)` is the group standard deviation

This is just **z-score normalization** of rewards within the group.

**Why this works:** If a prompt is easy and all responses are correct, all advantages are near zero
— no learning signal (which is correct — the model already handles this). If a prompt is hard and
only 2 of 16 responses are correct, those 2 get large positive advantages and the other 14 get
negative advantages — strong learning signal to reinforce the correct reasoning patterns.

**Alternatively**, the advantage can be computed without the self (leave-one-out):

```
Â_i = r_i - (1/(G-1)) · ∑_{j≠i} r_j
```

This avoids including the sample's own reward in its baseline, providing an unbiased estimate.

**Step 4: Policy Update**

GRPO uses a PPO-style clipped objective with a KL penalty:

```
L_GRPO(θ) = E_{x, {y_i}} [∑_i min(ρ_i · Â_i, clip(ρ_i, 1-ε, 1+ε) · Â_i) - β · KL_i]
```

Where:
- `ρ_i = π_θ(y_i|x) / π_old(y_i|x)` is the probability ratio
- `Â_i` is the group-relative advantage
- `ε` is the clipping parameter
- `β · KL_i` is a per-sample KL penalty to prevent drift from the reference policy

The KL term can be computed token-by-token:

```
KL_i = ∑_t [π_ref(y_i,t | x, y_i,<t) / π_θ(y_i,t | x, y_i,<t) 
            - log(π_ref(y_i,t | x, y_i,<t) / π_θ(y_i,t | x, y_i,<t)) - 1]
```

### No Reward Model, No Critic — Just Group Comparisons

GRPO's architectural simplicity is stunning:

```
Models needed:

RLHF/PPO:     Policy + Reference + Reward Model + Value Network = 4 models
DPO:           Policy + Reference = 2 models
GRPO:          Policy + Reference = 2 models (no value network!)
               (+ optional lightweight reward model or rule-based verifier)
```

**No value network (critic):** Traditional PPO requires a critic to estimate advantages. This critic
must be as large as the policy model itself (for LLMs), doubling memory requirements. GRPO
replaces the critic with simple group statistics. This halves the memory overhead compared to
PPO-based RLHF.

**No separate reward model (for verifiable tasks):** For math, code, and other tasks with
objective correctness criteria, GRPO can use rule-based verifiers instead of learned reward models.
A simple "is the answer correct?" check replaces a multi-billion parameter reward model.

### Why GRPO Enables Emergent Reasoning

This is the most remarkable finding. When DeepSeek trained models with GRPO on math and
reasoning tasks, the models spontaneously developed:

1. **Chain-of-thought reasoning**: Without being explicitly taught to "think step by step," the
   model learned to break down problems

2. **Self-verification**: The model learned to check its own work

3. **Exploration of solution strategies**: The model would try multiple approaches before
   committing to an answer

4. **Metacognition-like behavior**: Phrases like "Wait, let me reconsider..." emerged naturally

**Why does this happen?** The group comparison mechanism creates a natural curriculum:

- Easy problems: Most responses are correct → small advantages → little learning
- Hard problems: Only creative, careful reasoning leads to correct answers → those responses
  get large advantages → the model reinforces the reasoning patterns that led to success
- The model learns that extended, careful reasoning → correct answers → positive advantage

GRPO doesn't tell the model *how* to reason. It creates conditions where reasoning *emerges*
because it's advantageous. This is a profound result: **the right optimization objective, with the
right structure, can elicit capabilities that weren't explicitly trained.**

### The Math: Complete GRPO Formulation

For a batch of prompts {x_1, ..., x_B}, for each prompt x_k sample G responses:

```
{y_k,1, ..., y_k,G} ~ π_θ_old(·|x_k)
```

Score each response:
```
r_k,i = R(x_k, y_k,i)    (reward model or verifier)
```

Compute group-normalized advantages:
```
Â_k,i = (r_k,i - μ_k) / (σ_k + ε)
Where:  μ_k = mean({r_k,j}_j), σ_k = std({r_k,j}_j)
```

Compute per-token probability ratios:
```
ρ_k,i,t = π_θ(y_k,i,t | x_k, y_k,i,<t) / π_θ_old(y_k,i,t | x_k, y_k,i,<t)
```

Token-level GRPO loss:
```
L_token(k,i,t) = min(ρ_k,i,t · Â_k,i, clip(ρ_k,i,t, 1-ε, 1+ε) · Â_k,i)
```

Full GRPO objective (to maximize):
```
J_GRPO(θ) = (1/B) ∑_k (1/G) ∑_i [(1/|y_k,i|) ∑_t L_token(k,i,t)] - β · KL_k,i
```

### GRPO vs PPO vs DPO — Summary

```
Feature          │ RLHF (PPO)              │ DPO                     │ GRPO
─────────────────┼─────────────────────────┼─────────────────────────┼──────────────────────────
Training type    │ Reinforcement learning  │ Supervised learning     │ RL (simplified)
Reward model     │ Required (learned)      │ Not needed              │ Optional (verifier ok)
Value network    │ Required                │ Not needed              │ Not needed
Reference model  │ Required                │ Required                │ Required
# Models in mem  │ 4                       │ 2                       │ 2 (+ optional verifier)
Training data    │ Online (generate + score│ Offline (fixed pairs)   │ Online (generate + score)
                 │  during training)       │                         │  during training)
Stability        │ Low (RL instability)    │ High (supervised)       │ Medium (simpler RL)
Best for         │ General alignment       │ General alignment       │ Reasoning tasks
Key innovation   │ Human feedback → RL     │ No RL needed            │ No critic needed
Emergent ability │ Moderate                │ Limited                 │ Strong (reasoning)
```

---

## Constitutional AI & RLAIF

### Anthropic's Approach: AI-Generated Feedback

Constitutional AI (CAI), introduced by Anthropic in 2022, represents a different philosophical
approach to alignment. Instead of asking "what do humans prefer?", it asks "what *principles*
should the model follow?"

The key innovation: **use AI feedback instead of (or alongside) human feedback**. This is RLAIF —
Reinforcement Learning from AI Feedback.

### How Constitutional AI Works

**Phase 1: Supervised Self-Critique (Red-teaming + Revision)**

```
Step 1: Generate a potentially harmful response
  Prompt: "How can I break into a car?"
  Model: [generates harmful response]

Step 2: Ask the model to critique itself against constitutional principles
  "Critique your response according to the principle:
   'Choose the response that is least likely to cause harm.'"
  Model: "My response could enable illegal activity..."

Step 3: Ask the model to revise based on its critique
  Model: [generates revised, harmless response]

Step 4: Fine-tune on the revised (helpful) responses
```

**Phase 2: RLAIF (RL from AI Feedback)**

```
Step 1: Generate pairs of responses to prompts
Step 2: Ask an AI model to judge which response better follows the constitution
Step 3: Train a reward model on AI preferences (not human preferences)
Step 4: Use RLHF (or DPO) with this AI-generated reward model
```

### The Constitution

The "constitution" is a set of principles written in natural language:

1. "Choose the response that is most helpful to the human."
2. "Choose the response that is least harmful or toxic."
3. "Choose the response that is most honest and truthful."
4. "Choose the response that best refuses to engage in harmful activities."
5. "Choose the response that is least likely to be used for illegal purposes."
6. ... (typically 15-20 principles)

These principles are **transparent and auditable** — unlike a neural reward model, you can read
and understand exactly what values the model is being trained on.

### Why RLAIF Matters

**Scaling:** Human annotation is expensive and slow. AI feedback scales to millions of comparisons
at the cost of compute, not human labor.

**Consistency:** AI judges are more consistent than human judges. They don't get tired, don't have
varying expertise, and apply the same principles uniformly.

**Iterability:** You can quickly test different constitutions, principles, and feedback strategies.
Updating alignment objectives is a matter of editing text, not retraining human labelers.

**Reducing the human bottleneck:** The biggest constraint on alignment research is high-quality
human feedback data. RLAIF dramatically reduces this dependency.

**Empirical results:** Anthropic showed that models trained with RLAIF were comparable to or
better than models trained with pure human feedback on harmlessness benchmarks, while
maintaining helpfulness.

### The Philosophical Shift

Constitutional AI represents a move from:
- **Behavioral alignment**: "Match what humans say they prefer" (RLHF)
- To **principled alignment**: "Follow these explicit rules" (CAI)

This matters for scalability. As models become more capable than humans at certain tasks, we
can't rely on humans to judge their outputs. But we can specify principles and have AI systems
apply those principles — even to outputs that humans can't fully evaluate.

---

## The Bigger Picture

### Self-Play and Debate for Alignment

**AI Debate** (Irving et al., 2018) proposes using adversarial argumentation for alignment:
- Two AI agents argue for competing answers to a question
- A human judge (or weaker AI) evaluates the arguments
- The debaters are trained via self-play to make the most convincing *truthful* arguments

The insight: even if a human can't directly evaluate a complex claim, they can evaluate
**arguments about that claim**. Two adversarial AIs will expose each other's errors and
deceptions, making the truth emerge.

Recent (2024) experiments show debate-trained models produce more informative, accurate
arguments than "consultancy" models (single-sided explanation), especially on tasks too complex
for direct human evaluation.

**Challenges:** Strategic adversarial influence can sway debates toward incorrect conclusions.
Debate is promising but not yet robust enough for production alignment.

### Weak-to-Strong Generalization

OpenAI's **superalignment** team investigated a critical question: **Can weak supervisors
effectively align strong models?**

In the "Weak-to-Strong Generalization" paper (Burns et al., 2023):
- A small, less capable model provides labels/preferences for a larger, more capable model
- The large model is fine-tuned on these weak labels
- Key finding: the large model often **generalizes beyond the weak labels**, performing better than
  the weak supervisor

This is encouraging for scalable alignment: even imperfect human oversight might be sufficient
to align models more capable than the overseers. But the gap between weak supervision quality
and strong model capability needs careful management.

### Scalable Oversight

The fundamental challenge of alignment at scale: **how do you supervise a system smarter than
you?**

Approaches under active research:

1. **Iterated Amplification**: Decompose complex oversight tasks into simpler subtasks that
   humans (or weaker models) can evaluate. Recursively build up oversight capability.

2. **Recursive Reward Modeling**: Use an aligned model to help train the next, more capable
   aligned model. Each generation's oversight capability scales with its capability.

3. **Debate**: As described above — use adversarial AI systems to expose errors and make
   oversight tractable.

4. **Market-based approaches**: Create "markets" where AI systems bet on the quality of their
   outputs, with payoffs determined by eventual human evaluation.

5. **Interpretability**: If we can understand *what* a model is doing internally, we can align it
   more precisely. Mechanistic interpretability research aims to make neural networks transparent
   enough for principled oversight.

### Alignment Tax vs. Alignment Bonus

A crucial empirical question: does alignment make models worse at their primary tasks?

**Alignment Tax:** Some early concerns suggested that safety constraints would reduce model
capability — you'd pay a "tax" in performance for safety.

**Alignment Bonus:** The surprising finding from InstructGPT, ChatGPT, Claude, and others:
**alignment often *improves* performance.** Models trained with RLHF/DPO are not just safer —
they're better at following instructions, more accurate, and preferred by users on a wide range
of tasks.

Why? Because alignment teaches models to:
- Actually answer the question asked (rather than rambling)
- Be precise and well-structured (rather than verbose)
- Acknowledge uncertainty (rather than confidently hallucinating)
- Follow the user's intent (rather than pattern-matching to training data)

The alignment bonus is most pronounced for user-facing tasks. For narrow benchmarks (pure math,
coding puzzles), there may still be a small alignment tax if safety constraints prevent certain
outputs. But for most practical applications, aligned models are simply better.

### The Frontier: What's Next?

**Online DPO / Iterative DPO**: Instead of training on a fixed preference dataset, generate new
comparisons from the current policy and continuously improve.

**Process Reward Models**: Instead of scoring complete responses, score each reasoning step.
This provides denser, more informative feedback for reasoning tasks.

**Multi-turn Alignment**: Most alignment research focuses on single-turn interactions. Aligning
models for coherent, helpful behavior across multi-turn conversations is an open challenge.

**Alignment for Agentic Systems**: As LLMs become agents that take actions in the world (browsing,
coding, tool use), alignment becomes even more critical — and more difficult.

**Reward Model Ensembles**: Using multiple reward models to reduce reward hacking through
diversity of evaluation perspectives.

**Constitutional AI + DPO**: Combining the principled approach of Constitutional AI with the
simplicity of DPO — using AI-generated principles to create preference data for direct
optimization.

---

## Key Papers & Sources

### Foundational Papers

1. **InstructGPT** — Ouyang et al. (2022)
   "Training language models to follow instructions with human feedback"
   https://arxiv.org/abs/2203.02155

2. **DPO** — Rafailov et al. (2023)
   "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
   https://arxiv.org/abs/2305.18290

3. **Constitutional AI** — Bai et al. (2022)
   "Constitutional AI: Harmlessness from AI Feedback"
   https://arxiv.org/abs/2212.08073

4. **PPO** — Schulman et al. (2017)
   "Proximal Policy Optimization Algorithms"
   https://arxiv.org/abs/1707.06347

5. **DeepSeek-Math / GRPO** — Shao et al. (2024)
   "DeepSeekMath: Pushing the Limits of Mathematical Reasoning"
   https://arxiv.org/abs/2402.03300

6. **DeepSeek-R1** — DeepSeek AI (2025)
   "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
   https://arxiv.org/abs/2501.12948

### DPO Variants

7. **IPO** — Azar et al. (2023)
   "A General Theoretical Paradigm to Understand Learning from Human Feedback"
   https://arxiv.org/abs/2310.12036

8. **KTO** — Ethayarajh et al. (2024)
   "KTO: Model Alignment as Prospect Theoretic Optimization"
   https://arxiv.org/abs/2402.01306

9. **ORPO** — Hong et al. (2024)
   "ORPO: Monolithic Preference Optimization without Reference Model"
   https://arxiv.org/abs/2403.07691

10. **SimPO** — Meng et al. (2024)
    "SimPO: Simple Preference Optimization with a Reference-Free Reward"
    https://arxiv.org/abs/2405.14734

### Alignment Theory & Safety

11. **RLHF Original** — Christiano et al. (2017)
    "Deep Reinforcement Learning from Human Preferences"
    https://arxiv.org/abs/1706.03741

12. **Weak-to-Strong Generalization** — Burns et al. (2023)
    "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision"
    https://arxiv.org/abs/2312.09390

13. **AI Safety via Debate** — Irving et al. (2018)
    "AI Safety via Debate"
    https://arxiv.org/abs/1805.00899

14. **Scaling Laws for Reward Model Overoptimization** — Gao et al. (2022)
    https://arxiv.org/abs/2210.10760

15. **Training Language Models to Win Debates with Self-Play** — Khan et al. (2024)
    https://arxiv.org/abs/2409.16636

16. **Self-Play in Reinforcement Learning Survey** (2024)
    https://arxiv.org/abs/2408.01072

---

## Concepts for Knowledge Tree

1. **Post-Training Alignment** — The process of adjusting a pretrained model's behavior to be helpful, harmless, and honest after the initial pretraining phase
2. **RLHF (Reinforcement Learning from Human Feedback)** — Training language models using reinforcement learning with rewards derived from human preference judgments
3. **Reward Model** — A neural network trained on human comparisons to predict scalar quality scores for model responses
4. **Bradley-Terry Model** — A probabilistic model for pairwise comparisons that converts preference data into scalar scores via logistic probability
5. **PPO (Proximal Policy Optimization)** — A policy gradient RL algorithm that constrains updates via clipping to prevent destabilizing large policy changes
6. **KL Divergence Penalty** — A regularization term that prevents the aligned model from diverging too far from the reference (SFT) model
7. **Reward Hacking** — When models exploit imperfections in the reward model to achieve high scores without genuinely improving quality (Goodhart's Law)
8. **Goodhart's Law** — "When a measure becomes a target, it ceases to be a good measure" — central failure mode in reward-based optimization
9. **DPO (Direct Preference Optimization)** — An alignment method that optimizes preferences directly without a separate reward model by reparameterizing the RLHF objective
10. **Implicit Reward** — In DPO, the reward function is defined implicitly as the log-ratio between the policy and reference model probabilities
11. **Closed-Form Solution** — DPO derives from the analytical solution to the KL-constrained reward maximization problem, avoiding iterative RL
12. **Reference Policy** — The frozen SFT model used as a baseline to compute KL penalties and implicit rewards in DPO and RLHF
13. **IPO (Identity Preference Optimization)** — A DPO variant with explicit KL regularization that avoids Bradley-Terry overfitting via squared loss
14. **KTO (Kahneman-Tversky Optimization)** — Alignment using unpaired binary feedback inspired by prospect theory's loss aversion and reference dependence
15. **ORPO (Odds Ratio Preference Optimization)** — Single-stage alignment combining SFT and preference learning without a reference model using odds ratios
16. **SimPO (Simple Preference Optimization)** — Reference-free alignment using length-normalized average log-likelihood as the implicit reward with a target margin
17. **GRPO (Group Relative Policy Optimization)** — DeepSeek's critic-free RL method computing advantages from group statistics of sampled responses
18. **Group-Relative Advantage** — Estimating how good a response is by comparing its reward to the mean/std of other responses generated for the same prompt
19. **Constitutional AI** — Anthropic's approach to alignment using explicit written principles (a "constitution") to guide model behavior
20. **RLAIF (Reinforcement Learning from AI Feedback)** — Using AI systems rather than humans to generate preference labels for alignment training
21. **Scalable Oversight** — The challenge of supervising AI systems that are more capable than their human overseers
22. **Weak-to-Strong Generalization** — The finding that strong models can generalize beyond weak supervisors' labels, relevant to superalignment
23. **Alignment Tax** — The potential performance cost of alignment constraints on model capability
24. **Alignment Bonus** — The empirical finding that well-executed alignment often improves rather than degrades model performance
25. **Self-Play for Alignment** — Training AI through adversarial or cooperative games between model instances to improve alignment properties
26. **AI Debate** — An alignment approach where adversarial AI agents argue for competing answers, exposing errors for human judgment
27. **Emergent Reasoning** — Reasoning capabilities that arise spontaneously from RL training (especially GRPO) without explicit chain-of-thought supervision
28. **SFT (Supervised Fine-Tuning)** — Training a pretrained model on curated (prompt, response) pairs to teach instruction-following behavior
29. **Exposure Bias** — The distribution mismatch between teacher-forced training (SFT) and autoregressive generation at inference time
30. **Process Reward Models** — Reward models that score individual reasoning steps rather than complete responses, enabling denser feedback
31. **Sycophancy** — A reward hacking failure mode where models learn to agree with or flatter users rather than being truthful
32. **Iterative RLHF** — Multiple rounds of data collection and alignment training, each round improving on the last
33. **Preference Data** — Datasets of human (or AI) judgments comparing pairs of model outputs, used for reward model training or DPO

---

## Quick Reference: The Evolution at a Glance

```
2017 │ Christiano et al. — RLHF concept with deep RL from human preferences
     │
2017 │ Schulman et al. — PPO algorithm (foundation for RLHF optimization)
     │
2022 │ Ouyang et al. — InstructGPT: RLHF at scale, proving alignment works
     │ Bai et al. — Constitutional AI: principles-based alignment with RLAIF
     │
2023 │ ChatGPT launches — RLHF goes mainstream, changes the world
     │ Rafailov et al. — DPO: eliminates reward model and RL entirely
     │ Azar et al. — IPO: fixes DPO's overfitting with better regularization
     │ Burns et al. — Weak-to-strong generalization (OpenAI superalignment)
     │
2024 │ Ethayarajh et al. — KTO: unpaired binary feedback via prospect theory
     │ Hong et al. — ORPO: single-stage, no reference model
     │ Meng et al. — SimPO: length-normalized, reference-free simplicity
     │ DeepSeek — GRPO in DeepSeek-Math: critic-free RL for reasoning
     │
2025 │ DeepSeek-R1 — GRPO at scale: emergent reasoning from RL alone
     │ The field continues to simplify: fewer models, less data, better results
```

**The trajectory is clear: each generation of alignment methods is simpler, cheaper, and more
effective than the last.** From 4 models and complex RL (RLHF) to 2 models and supervised
learning (DPO) to critic-free RL with emergent reasoning (GRPO) — the field is converging on
methods that are both more powerful and more accessible.

The question is no longer "can we align language models?" It's "how do we align models that are
smarter than us?" That's the scalable oversight problem, and it's the defining challenge of the
next decade of AI research.

---

*"The goal of alignment research is to make the transition from 'AI that CAN do anything' to
'AI that SHOULD do the right thing' — and to make that transition robust, scalable, and
verifiable."*
