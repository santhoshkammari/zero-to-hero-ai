# AI for Science: When Neural Networks Do Real Science

> *In 2024, AI won both the Nobel Prize in Physics and the Nobel Prize in Chemistry. This is no longer "just tech" — artificial intelligence is now a first-class instrument of scientific discovery, standing alongside the microscope, the telescope, and the particle accelerator.*

---

## Why This Matters

In October 2024, the Nobel Committee made history — twice:

- **Nobel Prize in Physics** → Geoffrey Hinton and John Hopfield, for "foundational discoveries and inventions that enable machine learning with artificial neural networks." Hinton's Boltzmann machines and backpropagation insights laid the groundwork for every deep learning system in existence.

- **Nobel Prize in Chemistry** → Demis Hassabis, John Jumper, and David Baker, for "protein structure prediction" (AlphaFold) and "computational protein design" (Baker's Rosetta/RFdiffusion work).

This wasn't a "tech award." These prizes went to the *physics* and *chemistry* committees because the AI systems produced genuine scientific breakthroughs — solving problems that had resisted decades of traditional approaches.

The message is unmistakable: **AI is no longer just a tool that helps scientists. In critical domains, AI is doing the science itself** — predicting protein structures, forecasting weather, proving theorems, discovering materials, and designing drugs.

This document maps the landscape of AI-for-science as of early 2025: what works, how it works, and why it matters.

---

## 1. Protein Structure Prediction

### The 50-Year Problem

Proteins are the molecular machines of life. Their function is determined by their 3D shape, but predicting shape from amino acid sequence — the "protein folding problem" — was an unsolved grand challenge for over 50 years. Experimental methods (X-ray crystallography, cryo-EM) cost months to years per structure. By 2020, humanity had solved ~170,000 structures total.

### AlphaFold 2: The Breakthrough (2020)

At CASP14 (Critical Assessment of protein Structure Prediction), AlphaFold 2 achieved a median GDT score of 92.4 — essentially experimental accuracy. No other method came close.

**How AlphaFold 2 Works:**

```
Input Sequence → MSA Construction → Evoformer (48 blocks) → Structure Module → 3D Coordinates
```

The architecture has three key innovations:

1. **Multiple Sequence Alignment (MSA) Processing**: The model searches protein databases for evolutionarily related sequences. Co-evolution patterns reveal which residues are spatially close — if position 23 and position 157 always mutate together across species, they're probably in contact in the 3D structure.

2. **Evoformer Module**: This is the core innovation — a novel Transformer architecture that jointly processes two representations:
   - **MSA representation**: Rows = different homologous sequences; columns = positions in the alignment
   - **Pair representation**: A matrix encoding the relationship between every pair of residues
   
   The Evoformer uses several specialized attention mechanisms:
   - **Row-wise attention**: "What do other species tell us about this position?"
   - **Column-wise attention**: "What is the consensus at this position across evolution?"
   - **Triangle multiplicative updates**: If residue i is close to residue k, and residue k is close to residue j, then i and j are constrained — this enforces geometric consistency (triangle inequality on distances)
   - **Triangle attention**: Attention weighted by the pair representation, allowing the model to reason about spatial relationships

3. **Structure Module with Invariant Point Attention (IPA)**: Takes Evoformer features and directly predicts 3D coordinates. IPA is equivariant to rotations and translations — the model predicts the same structure regardless of coordinate frame. It builds the backbone as a series of rigid-body frames (one per residue), then refines side-chain positions.

4. **Recycling**: The output is fed back as input for 3 iterations, progressively refining the prediction.

**Training**: Supervised on ~170,000 experimentally determined structures from the Protein Data Bank (PDB). Loss function combines Frame Aligned Point Error (FAPE) on atom positions with auxiliary losses on distograms and predicted LDDT confidence scores.

**Impact**: DeepMind subsequently predicted structures for all ~200 million known protein sequences and released them in the AlphaFold Protein Structure Database — essentially solving structural biology's data problem overnight.

### AlphaFold 3: Beyond Proteins (2024)

AlphaFold 3, published in Nature in May 2024, represents a fundamental architectural shift:

**What Changed:**

| Feature | AlphaFold 2 | AlphaFold 3 |
|---------|-------------|-------------|
| Inputs | Protein sequences only | Proteins + DNA + RNA + ligands + ions + modifications |
| Architecture | Evoformer → Structure Module | Pairformer → Diffusion Module |
| Output | Single best structure | Distribution of plausible structures |
| Complex prediction | Limited multimer support | Full biomolecular complexes |
| Drug binding | No | Yes — predicts protein-ligand interactions |

**The Diffusion Architecture:**

AlphaFold 3 replaced the deterministic Structure Module with a **diffusion-based generative model** — the same family of models behind Stable Diffusion and DALL-E, but operating in 3D molecular space instead of pixel space.

```
Step 1: Place all atoms (protein + DNA + RNA + ligand + ions) at random positions
Step 2: Add noise to create a "cloud" of atoms  
Step 3: Iteratively denoise — the model learns to progressively refine
        random atom clouds into physically realistic molecular structures
Step 4: Output: all-atom 3D coordinates of the entire complex
```

The diffusion approach has a crucial advantage: it naturally handles **uncertainty**. Instead of predicting one structure, it can sample multiple conformations, capturing the inherent flexibility of biomolecular complexes.

**Pairformer** replaces the Evoformer — it's a simplified trunk that focuses on pair representations and processes them more efficiently, since the heavy lifting of structure generation moves to the diffusion module.

**Why This Matters for Drug Discovery:**
- AF3 can predict how a drug molecule binds to a protein target — the core question of rational drug design
- It handles CRISPR-Cas complexes (protein + guide RNA + target DNA) — critical for gene therapy
- It models post-translational modifications, metal ion coordination, and water-mediated interactions
- Accuracy on protein-ligand binding exceeds previous best methods by a significant margin

**Limitations**: AF3 can sometimes generate physically implausible ("hallucinated") structures, especially for novel complexes far from training data. Experimental validation remains essential.

### ESMFold: The Language Model Approach (Meta AI, 2022)

While AlphaFold uses MSAs (slow — requires database search), Meta AI's ESMFold takes a radically different approach:

**Core Idea**: Train a massive protein language model (ESM-2, 15 billion parameters) on protein sequences using masked language modeling (like BERT), then add a folding head that predicts 3D structure from the language model's internal representations.

```
Single sequence → ESM-2 (protein LM) → Folding trunk → 3D coordinates
```

**Key Advantages:**
- **Speed**: ~14 seconds per protein on a V100 GPU (vs. minutes to hours for AlphaFold 2)
- **No MSA required**: Works from a single sequence — no database search needed
- **Scalable**: Can process millions of proteins rapidly for large-scale metagenomic analysis

**Key Trade-off**: Lower accuracy than AlphaFold 2 for well-characterized protein families, but remarkably good given it uses zero evolutionary information. For poorly characterized or orphan proteins (no known homologs), ESMFold can still make useful predictions where AlphaFold may struggle.

**The Language Model Insight**: ESM-2's attention patterns, learned purely from sequence statistics, spontaneously encode protein contact maps — the model "discovers" 3D structure information from sequence patterns alone.

### Impact on Drug Discovery

The practical impact is already measurable:

- **Insilico Medicine**: AI-designed drug candidate for idiopathic pulmonary fibrosis reached Phase II clinical trials in 2024
- **Antibiotic Discovery**: AI tools leveraging AlphaFold predictions identified new antibiotics (abaucin, halicin) active against multi-drug resistant pathogens
- **AlphaFold Database**: Over 200 million structures freely available — used by 2+ million researchers in 190 countries
- **Speed**: Structure determination went from months/years → seconds
- **AlphaFold 3 open-sourced** in 2024 (code + weights for academic research), further accelerating adoption

But a critical caveat: **knowing a protein's structure is necessary but not sufficient for drug design**. The pipeline from predicted structure → validated drug target → clinical candidate → approved drug still takes years and billions of dollars. AI accelerates the early stages enormously but hasn't yet produced an FDA-approved drug end-to-end.

---

## 2. Weather & Climate Prediction

### The Revolution

Weather prediction has been one of the most stunning success stories for AI in science. In 2023-2024, multiple ML-based weather models surpassed physics-based numerical weather prediction (NWP) systems that had been refined for 50+ years — and they did it running 1,000-10,000x faster.

### GraphCast (DeepMind, 2023)

Published in Science (November 2023), GraphCast demonstrated that a graph neural network trained on historical weather data could outperform ECMWF's HRES (the gold standard operational forecast system) on the majority of evaluation metrics.

**Architecture:**

```
Current weather state (t) + Previous state (t-6h)
        ↓
    Encoder: Grid → Multi-mesh graph  
        ↓
    Processor: 16 rounds of message passing on icosahedral mesh
        ↓
    Decoder: Multi-mesh graph → Grid
        ↓
    Predicted weather state (t+6h)
```

**The Graph Neural Network Approach:**

1. **Representation**: Earth's atmosphere is mapped onto a hierarchical icosahedral mesh (not a regular latitude-longitude grid). This avoids the pole-singularity problem and provides roughly uniform spatial resolution globally.

2. **Multi-mesh Structure**: 
   - Fine mesh: ~40,000 nodes (0.25° resolution)
   - Coarse mesh: ~2,500 nodes (for long-range interactions)
   - Edges connect neighboring nodes at each resolution level plus cross-resolution connections

3. **Message Passing**: Each node's state is updated by aggregating information from its neighbors through learned edge functions. 16 rounds of message passing allow information to propagate across the entire globe — critical for capturing teleconnections (how weather in the Pacific affects Europe).

4. **Variables**: Predicts 5 surface variables and 6 atmospheric variables at 37 pressure levels = 227 variables total, at 0.25° resolution (~1 million grid points).

5. **Autoregressive Rollout**: For multi-day forecasts, the model's 6-hour prediction is fed back as input, iterating to produce 10-day forecasts.

**Training**: 39 years of ERA5 reanalysis data (1979-2017). Trained to minimize the 6-hour forecast error, with noise injection during training to prevent error accumulation during rollout.

**Results**: Outperformed HRES on 90.3% of 2,760 evaluation targets (combinations of variables, pressure levels, and lead times). Particularly strong for medium-range forecasts (3-10 days).

**Speed**: A 10-day global forecast in under 1 minute on a single TPU v4, vs. hours on a supercomputer for HRES.

### Pangu-Weather (Huawei, 2023)

Published in Nature (July 2023), Pangu-Weather was the first AI model to demonstrably outperform operational NWP systems.

**Architecture: 3D Earth-Specific Transformer (3DEST)**

Unlike GraphCast's GNN approach, Pangu-Weather uses a Transformer with a critical innovation: it processes the atmosphere as a true 3D volume, not a stack of 2D layers.

```
3D atmospheric state → Patch embedding (3D) → Earth-Specific Transformer blocks → Predicted state
```

**Key Innovations:**
- **3D patch embedding**: Treats the atmosphere as a 3D tensor (latitude × longitude × pressure level), not separate 2D slices
- **Earth-specific positional encoding**: Accounts for the geometry of a sphere — grid cells near the poles represent smaller physical areas than equatorial cells
- **Hierarchical temporal aggregation**: Trains separate models for 1h, 3h, 6h, and 24h prediction intervals, then chains them for multi-day forecasts. This reduces cumulative error accumulation.

**Results:**
- Outperformed ECMWF IFS (operational) for forecast lead times from 1 hour to 7 days
- Superior tropical cyclone tracking — critical for disaster preparedness
- 10,000x faster than physics-based NWP
- Forecasts available free via ECMWF

### GenCast (DeepMind, 2024)

Published in Nature (December 2024), GenCast represents the next evolution: **probabilistic weather forecasting with diffusion models**.

**The Problem with Deterministic Forecasts:**
GraphCast and Pangu-Weather produce a single "best guess." But weather is inherently chaotic — small uncertainties grow exponentially. Operational weather centers run 50+ slightly perturbed simulations (ensemble forecasts) to quantify uncertainty. GenCast brings this to ML weather models.

**Architecture:**

```
Current weather state → Inject calibrated noise → Iterative denoising (diffusion)
                                                          ↓
                                            Ensemble of 50+ plausible futures
```

GenCast is a **conditional diffusion model** adapted for Earth's spherical geometry:

1. **Spherical Diffusion**: Standard diffusion models work on flat grids. GenCast adapts the noise schedule and denoising network for spherical geometry, ensuring physically consistent predictions across the globe.

2. **Ensemble Generation**: By starting from different noise realizations, GenCast samples 50+ diverse but physically plausible future weather states — each representing a possible evolution of the atmosphere.

3. **Probabilistic Calibration**: The ensemble spread is trained to match observed forecast uncertainty — when the model says "30% chance of rain," it should rain roughly 30% of the time.

**Specifications:**
- 0.25° global resolution (~22×22 km grids)
- 80+ weather variables
- 15-day forecasts in 12-hour increments
- 50+ ensemble members generated in ~8 minutes on TPUs

**Results:**
- Outperformed ECMWF's ENS (the operational ensemble system) on 97%+ of evaluation targets
- Superior extreme weather prediction (heatwaves, cold spells)
- Better tropical cyclone track forecasts up to 5-7 days ahead
- Improved wind power output predictions — critical for renewable energy grid management

**Open-sourced**: Code, model weights, and example data released for non-commercial research.

### Why ML Weather Models Beat Physics-Based NWP

This seems counterintuitive — how can a learned model outperform equations derived from first principles? Several factors:

1. **Implicit bias correction**: NWP models have systematic biases from approximations in their physics schemes. ML models learn to avoid these biases from data.

2. **Sub-grid parameterization**: Physics models must approximate processes smaller than their grid resolution (convection, turbulence). ML models can learn more accurate representations from data.

3. **Computational budget**: Physics models must spend compute on explicitly integrating equations. ML models concentrate compute on inference, having already "learned" the dynamics during training.

4. **Optimal information extraction**: ML models may find patterns in observational data that physics-based models miss — subtle correlations across variables and regions.

5. **BUT**: ML models don't generalize to unseen climate regimes. A model trained on 1979-2017 data may fail if future climates are outside its training distribution. Physics-based models, derived from fundamental equations, are more robust to climate change. **The future is hybrid: ML + physics.**

### Impact on Disaster Prediction

- **Tropical cyclone tracking**: ML models now provide competitive or superior track forecasts, buying critical hours for evacuation planning
- **Extreme weather events**: Probabilistic ML forecasts better quantify the risk of rare, high-impact events
- **Renewable energy**: More accurate wind/solar forecasts improve grid management and reduce reliance on backup fossil fuel generation
- **Developing nations**: ML models run on modest hardware, democratizing access to high-quality forecasts previously available only to well-funded national weather services

---

## 3. Mathematics

### AI as Mathematician

The dream of automated mathematical reasoning is as old as AI itself — Newell, Shaw, and Simon's Logic Theorist (1956) proved theorems in Principia Mathematica. But modern systems have leaped from proving textbook exercises to solving Olympiad-level problems and making genuine mathematical discoveries.

### AlphaProof: IMO-Level Theorem Proving (2024)

At the 2024 International Mathematical Olympiad (IMO), DeepMind's AlphaProof solved 3 out of 5 non-geometry problems — achieving the equivalent of a **silver medal**. This was the first time any AI system reached medal-level performance at IMO using formally verified proofs.

**How AlphaProof Works:**

```
Natural language problem → Formalization in Lean 4 → Neural proof search → Verified proof
```

1. **Problem Translation**: The IMO problem (natural language) is translated into the formal language of **Lean 4** — a proof assistant where every logical step must be machine-verified. This translation step uses a fine-tuned LLM trained on pairs of informal/formal mathematical statements.

2. **Neural Proof Search**: The core is a neural network that predicts which proof tactics to apply at each step:
   - It represents the current "proof state" (goals, hypotheses, context)
   - Predicts the most promising next tactic (induction, contradiction, algebraic manipulation, etc.)
   - Explores a proof search tree, balancing exploration (trying new approaches) and exploitation (deepening promising paths)

3. **Reinforcement Learning via Self-Play**: 
   - AlphaProof generates millions of candidate problems and attempted proofs
   - Successful proofs provide positive reward; failures provide negative signal
   - The model progressively improves its proof strategies — analogous to AlphaZero's self-play in chess
   - Critically, it can learn to invent useful sublemmas — auxiliary results not in the training data

4. **Formal Verification**: Every completed proof is checked by Lean's type checker — guaranteeing correctness. No hallucinations, no hand-waving. If Lean accepts it, the proof is valid.

**Key Insight**: The combination is crucial. LLMs alone hallucinate proofs. Lean alone can't generate creative strategies. Together, the LLM provides mathematical intuition while Lean provides absolute rigor.

### AlphaGeometry: Solving Geometry (2024)

Published in Nature (January 2024), AlphaGeometry solved 25 out of 30 IMO-level geometry problems — matching the average performance of human gold medalists.

**Neuro-Symbolic Architecture:**

```
Geometry problem → Symbolic deduction engine ←→ Neural language model → Proof
                         ↕                           ↕
                  Algebraic/geometric           Suggests auxiliary
                  deduction rules               constructions
```

The system combines two complementary components:

1. **Symbolic Deduction Engine (DD+AR)**: An algebraic deduction engine that can derive conclusions from known geometric facts using rules like angle chasing, congruence, similarity, and cyclic quadrilateral properties. It's fast and exact, but can only derive what follows logically from given information — it can't "be creative."

2. **Neural Language Model**: Trained on 100 million synthetic geometry proofs, this model suggests **auxiliary constructions** — the "creative leaps" in geometry (e.g., "draw line through A parallel to BC," "construct the circumcircle of triangle XYZ"). These are the moves that make geometry hard: knowing *what to add* to a diagram to unlock a proof.

**The Synthesis:**
- The symbolic engine tries all deductions from current facts
- When stuck, it asks the neural model: "What construction might help?"
- The neural model proposes a construction (e.g., "let P be the midpoint of AB")
- The symbolic engine incorporates this new element and tries deduction again
- This loop repeats until a proof is found (or time runs out)

**Training Data**: Since few formal geometry proofs exist, DeepMind generated 100 million synthetic proofs by:
1. Randomly sampling geometric constructions
2. Computing all derivable facts using the symbolic engine
3. Selecting non-trivial facts as "theorems" with their derivation as "proofs"
4. Training the neural model on the relationship between problem states and useful constructions

**Previous best (symbolic-only)**: 10/30. **AlphaGeometry**: 25/30. **Human gold medalists**: 25.9/30.

### FunSearch: Discovering New Mathematics (2023)

Published in Nature (December 2023), FunSearch was the first demonstration of an LLM making a **verifiable new discovery** in open mathematics.

**The Setup:**

FunSearch doesn't solve pre-existing problems — it discovers new mathematical objects and functions. Its first target was the **cap set problem**, a famous open problem in combinatorics:

> What is the largest subset of vectors in F₃ⁿ (n-dimensional space over the field with 3 elements) such that no three distinct vectors sum to zero?

This is a problem where solutions are "easy to check but hard to find" — perfect for AI assistance.

**How FunSearch Works:**

```
Seed programs → LLM generates variations → Evaluator scores them → 
Best programs retained → LLM sees best programs → Generates better variations → ...
                     (evolutionary loop)
```

1. **Program Search, Not Answer Search**: FunSearch doesn't search for cap sets directly. It searches for *programs that construct cap sets*. This is crucial — programs are more generalizable than specific solutions.

2. **LLM as Variation Generator**: A code-specialized LLM (Codey, based on PaLM 2) takes existing high-scoring programs and generates variations — modifying the logic, adding heuristics, combining strategies.

3. **Automated Evaluator**: Each candidate program is executed, and the resulting cap set is evaluated for size and validity. This provides an exact, unambiguous fitness signal — no human judgment needed.

4. **Evolutionary Selection**: The population of programs evolves over millions of iterations. Programs that produce larger valid cap sets survive; others are discarded.

**Results:**
- Discovered the largest known cap sets for dimension n=8, breaking records held by humans and computers
- The solutions were genuinely new — not in any existing database
- Produced interpretable programs (not just the answer, but the *method*)

**Also Applied To:**
- **Bin packing**: Found new heuristics outperforming classical approaches
- **Online bin packing**: Discovered scheduling strategies

**Significance**: This is the first time an LLM contributed a novel, verifiable result to an open problem in mathematics. It represents a new paradigm: **LLMs as creative engines within a rigorous evaluation loop**.

### LLMs as Mathematical Reasoning Engines

Beyond specialized systems, general-purpose LLMs are increasingly capable mathematicians:

**DeepSeek-Prover (2024)**: Achieved 50% pass rate on the MiniF2F Lean benchmark by training on 8+ million synthetic formal proofs — a massive leap from previous SOTA.

**TheoremLlama (2024)**: An end-to-end framework for converting general-purpose LLMs into Lean 4 experts, surpassing GPT-4 on formal theorem-proving benchmarks.

**Key Challenge — Autoformalization**: Converting informal mathematics ("Let n be a positive integer such that...") into formal Lean code is itself a major research problem. Process-driven approaches using Lean's feedback as training signal show promise.

**The Feedback Loop**:
```
LLM proposes proof step → Lean checks it → 
    If valid: continue
    If invalid: backtrack, try different approach
    Outcome: used as RL training signal for the LLM
```

This creates a neuro-symbolic feedback loop analogous to AlphaZero's self-play — but for mathematics instead of chess.

### Formal Verification and Proof Assistants

The rise of AI-for-math has supercharged interest in formal proof assistants:

- **Lean 4**: Developed at Microsoft Research, now the dominant proof assistant for AI-math integration. Its mathlib library contains ~110,000 formalized theorems.
- **Coq**: Historically dominant, used for verified software (CompCert compiler).
- **Isabelle**: Strong in mathematical logic and automated reasoning.

The key insight is that proof assistants provide a **perfect reward signal** for RL — a proof either type-checks or it doesn't. This makes mathematics uniquely amenable to AI approaches that struggle in domains with ambiguous evaluation (like natural language generation).

---

## 4. Materials Science & Chemistry

### GNoME: 2.2 Million New Materials (2023)

Published in Nature (November 2023), Google DeepMind's GNoME (Graph Networks for Materials Exploration) discovered **2.2 million new stable crystal structures** — increasing known stable materials by a factor of 45x.

**Context**: Before GNoME, humanity had experimentally verified ~48,000 stable inorganic crystals (accumulated over centuries of chemistry). Computational methods (DFT — Density Functional Theory) could predict stability but were expensive: each structure required hours of supercomputer time.

**How GNoME Works:**

```
Candidate crystal structure → Graph representation → GNN predicts formation energy
                                                          ↓
                                              Stable if energy below threshold
```

1. **Graph Representation**: Each crystal structure is encoded as a graph:
   - Nodes = atoms (with features: element type, oxidation state)
   - Edges = bonds/interactions (with features: distance, angle)
   - The graph captures both local chemical environment and long-range periodicity

2. **GNN Architecture**: A specialized graph neural network processes the crystal graph through multiple rounds of message passing. Atoms aggregate information from their neighbors, building up a representation of the local and global chemical environment.

3. **Stability Prediction**: The GNN predicts the **formation energy** — the energy difference between the crystal and its constituent elements. Negative formation energy → thermodynamically stable → potentially synthesizable.

4. **Active Learning Pipeline**:
   ```
   GNN predicts candidates → DFT validates top predictions → 
   Validated structures added to training set → GNN retrained → 
   Better predictions → ...
   ```
   
   This iterative loop progressively improved the model while generating the massive dataset.

**Scale of Discovery:**
- 2.2 million predicted stable structures (381,000 on the convex hull — the most thermodynamically favorable)
- Includes 52,000 new layered materials (potential 2D materials like graphene analogs)
- 528 potential lithium-ion conductors (for next-gen batteries)

**Validation**: Before publication, 736 of GNoME's predicted materials had been independently synthesized by experimental labs worldwide — confirming the predictions are real.

**Open Data**: All 2.2 million structures released publicly on GitHub, massively accelerating materials research globally.

### Crystal Structure Prediction

GNoME is part of a broader revolution in computational materials science:

- **MACE (Multi-ACE)**: Machine-learned interatomic potentials that achieve near-DFT accuracy at a fraction of the cost. Used for molecular dynamics simulations of large systems.
- **M3GNet / CHGNet**: Universal potential models from Materials Project, enabling rapid property prediction for arbitrary compositions.
- **Diffusion models for crystals**: Analogous to AlphaFold 3's approach for proteins — generative models that produce plausible crystal structures by denoising random atom arrangements.

### Molecular Property Prediction

Predicting molecular properties (solubility, toxicity, binding affinity, reactivity) is critical for drug discovery and chemical engineering:

- **Chemprop v2 (MIT, 2024)**: Modular, multi-fidelity ML for molecular property prediction. Uses message-passing neural networks on molecular graphs.
- **Uni-Mol**: Pretraining on 3D molecular conformations, analogous to how protein language models pretrain on sequences.
- **Foundation models for chemistry**: Following the protein language model playbook, researchers are training large models on millions of molecules to learn transferable chemical representations.

### Retrosynthesis Planning

Given a target molecule, **retrosynthesis** asks: "What sequence of reactions can build this from available starting materials?"

**AI approaches (2024 state-of-the-art):**

1. **Template-based**: Learn to select reaction templates (known reaction patterns) from a library. Fast but limited to known chemistry.
2. **Template-free**: Directly predict reactants from product using sequence-to-sequence models (SMILES → SMILES). More flexible but sometimes generates invalid chemistry.
3. **UAlign (2024)**: Graph-to-sequence model with unsupervised SMILES alignment — outperforms both template-based and template-free methods.
4. **BatGPT-Chem**: 15-billion-parameter foundation model unifying retrosynthesis with natural language, showing strong zero-shot capabilities.
5. **Chimera (Microsoft + Novartis, 2024)**: Ensemble framework combining GNNs and Transformers with learned ranking — handles rare and complex reactions.

**Search Algorithms**: MCTS-enhanced A* search (MEEA*) achieves near-perfect success rates on standard benchmarks, finding novel synthetic routes even for complex natural products.

---

## 5. Code & Software Engineering

### AlphaCode / AlphaCode 2

**AlphaCode (2022)**: DeepMind's first competitive programming system. Generated millions of candidate programs per problem, then filtered and clustered them. Achieved approximately 50th percentile on Codeforces — "average human competitor" level.

**AlphaCode 2 (2023)**: Built on Gemini Pro, representing a major leap:
- **85th percentile** on Codeforces (rating ~2337 — Candidate Master level)
- Outperformed 85% of human competitive programmers
- Uses a fundamentally different approach: instead of brute-force generation + filtering, it reasons about the problem using Gemini's capabilities, then generates targeted solutions

**Key Insight**: The jump from AlphaCode → AlphaCode 2 came primarily from the foundation model's improved reasoning, not from algorithmic innovations in the competitive programming pipeline itself. This suggests that general reasoning capability is the bottleneck.

### AI-Assisted Coding Evolution

The trajectory of AI coding assistance:

```
2021: Copilot launches — autocomplete on steroids (single-line / few-line completions)
2022: ChatGPT — conversational coding, explain/debug/refactor
2023: GPT-4 / Claude — multi-file reasoning, architectural understanding
2024: Claude 3.5 Sonnet / GPT-4o — near-human code generation for well-specified tasks
2025: Agentic coding — autonomous multi-step software engineering
```

The fundamental shift: from **autocomplete** (predict the next token) to **autonomous agents** (understand the task, plan the approach, write the code, test it, debug it, iterate).

### SWE-bench: Real-World Software Engineering

SWE-bench is the definitive benchmark for measuring AI's ability to solve real software engineering tasks — specifically, resolving actual GitHub issues from popular open-source Python repositories.

**Dataset:**
- **Full**: 2,294 issues from 12 Python repos (Django, Flask, scikit-learn, etc.)
- **Lite**: 300 curated simpler instances
- **Verified** (August 2024): 500 human-validated, engineer-solvable issues — the gold standard

**Progress (2024):**

| Timeline | Best Performance (Verified) | Model/Agent |
|----------|---------------------------|-------------|
| Early 2024 | ~10-20% | Various LLMs |
| Mid 2024 | ~33% | Claude 3.5 Sonnet + tools |
| Late 2024 | ~55% | Amazon Q Developer Agent, devlo, OpenHands |

**What This Means**: The best AI agents can now resolve about half of real-world software engineering tasks that a human engineer could solve. But the remaining 45% includes the hard cases — complex multi-file changes, subtle architectural decisions, and deep domain knowledge.

**The Architecture of a SWE-bench Agent:**
```
Issue description + Repository code → 
    Agent reads codebase (grep, view files) →
    Understands the bug / feature request →
    Plans the fix →
    Writes code changes →
    Runs tests →
    Iterates until tests pass →
    Submits patch
```

### The Path from Autocomplete to Autonomous Coding

**Level 0 — Autocomplete** (Copilot 2021): Predict the next line. Useful but limited — the programmer drives.

**Level 1 — Conversational** (ChatGPT 2022): Ask questions, get code. Human must integrate, test, and debug.

**Level 2 — Multi-step with tools** (2023-2024): AI reads files, runs commands, iterates. Human reviews output.

**Level 3 — Autonomous agents** (2024-2025): Given an issue, the agent autonomously navigates the codebase, writes code, runs tests, and produces a working patch. Human approves or rejects.

**Level 4 — Software engineer** (future): End-to-end feature development, including design decisions, testing strategy, documentation, and deployment. Not yet achieved.

We're currently in the Level 2-3 transition. The limiting factors are:
- Long-horizon planning and reasoning
- Understanding complex codebases holistically
- Handling ambiguous requirements
- Knowing when to ask for clarification vs. making assumptions

---

## 6. Robotics & Embodied AI

### RT-2: From Language to Robot Action (2023)

DeepMind's RT-2 (Robotic Transformer 2) demonstrated that **vision-language models can directly control robots** — bridging the gap between internet-scale knowledge and physical action.

**Architecture — Vision-Language-Action (VLA) Model:**

```
Camera image + Natural language instruction → Vision-Language Model → Robot action tokens
```

RT-2 takes a pretrained vision-language model (like PaLI-X or PaLM-E) and fine-tunes it on robot demonstration data, where actions are tokenized as text strings:

```
Input:  [Image of table with objects] + "Pick up the green apple"
Output: "1 128 91 241 1 0 0"  (x, y, z, rotation, gripper_open, terminate, ...)
```

**The Breakthrough — Zero-Shot Generalization:**
Because RT-2 inherits the VLM's world knowledge from web-scale pretraining, it can:
- Understand objects it was never shown during robot training ("pick up the Taylor Swift album")
- Follow abstract instructions ("move the object to the country on the left" — requires geographic knowledge)
- Reason about object properties ("pick up the extinct animal" → selects the dinosaur toy)
- Perform rudimentary chain-of-thought reasoning about physical actions

**Scale**: Trained on robot demonstrations from a fleet of 13 robots performing ~130,000 episodes across 700+ tasks, combined with web-scale vision-language data.

**Limitation**: RT-2 operates on relatively simple tabletop manipulation tasks. It cannot yet handle complex multi-step tasks, dynamic environments, or high-dexterity manipulation.

### Foundation Models for Robotics

The robotics community is converging on the foundation model paradigm:

**π₀ (pi-zero) — Physical Intelligence (2024):**
- General-purpose foundation model for robots
- Handles diverse tasks: folding laundry, bussing tables, complex manipulation
- Accepts natural language commands
- Decomposes high-level instructions into primitive actions
- Trained on data from multiple robot platforms — aimed at being a "GPT for robots"

**Octo (2024):**
- Open-source generalist robot policy
- Trained on 800K+ robot trajectories from the Open X-Embodiment dataset
- Provides a pretrained backbone that can be fine-tuned for specific robots

**Key Challenge**: Unlike language (where vast text corpora exist) or vision (ImageNet, LAION), robot data is scarce and expensive to collect. Every demonstration requires a physical robot in a physical environment. This data bottleneck is the primary constraint on robotics foundation models.

### Sim-to-Real Transfer

Training robots in simulation and transferring to the real world addresses the data scarcity problem:

**DrEureka (RSS 2024):**
- Uses LLMs to automatically design reward functions and domain randomization parameters for sim-to-real transfer
- Demonstrated on quadruped locomotion and novel manipulation tasks
- Reduces human engineering effort dramatically

**Ai2 Zero-Shot Transfer (2024):**
- Allen Institute for AI demonstrated training entirely in simulation and deploying in the real world with zero real-world fine-tuning
- Challenges the assumption that real-world data is always necessary

**RialTo (MIT, 2024):**
- Real-to-sim-to-real pipeline: scan your home with a smartphone → create digital twin → train robot in simulation → deploy at home
- Bridges general simulation with personalized environments

**The Reality Gap**: Simulations never perfectly match reality — different friction, lighting, dynamics. The field has developed several strategies:
- **Domain randomization**: Vary simulation parameters widely so the robot learns a policy robust to any setting
- **Domain adaptation**: Learn to transform simulated observations to look like real ones
- **System identification**: Estimate real-world physical parameters and calibrate the simulation
- **Residual learning**: Learn a correction term that compensates for sim-to-real mismatch

### Physical Intelligence and Manipulation

Dexterous manipulation — the ability to handle objects with human-like skill — remains one of robotics' hardest problems:

**Current capabilities (2024-2025):**
- Pick-and-place of diverse objects: largely solved for simple scenarios
- In-hand manipulation (rotating, flipping objects with fingers): emerging but fragile
- Deformable object manipulation (folding clothes, tying knots): early demonstrations (π₀)
- Tool use: rudimentary capabilities demonstrated

**What's missing:**
- Tactile sensing integration (most systems rely on vision alone)
- Long-horizon task planning in unstructured environments
- Robust failure recovery
- Human-level dexterity and speed

**The Vision**: A general-purpose robot that can navigate your home, manipulate any object, follow arbitrary instructions, and recover from errors. We're perhaps 5-10 years away from commercially viable versions — but the foundation model approach is rapidly closing the gap.

---

## 7. Cross-Cutting Themes

### The Foundation Model Pattern

Across all these domains, the same pattern repeats:

```
1. Collect massive domain-specific dataset
2. Train large neural network on self-supervised or supervised objective
3. Fine-tune or adapt for specific downstream tasks
4. Optionally: add search/verification loop for reliability
```

| Domain | Dataset | Model | Verification |
|--------|---------|-------|-------------|
| Proteins | PDB + UniProt | AlphaFold / ESM | Experimental validation |
| Weather | ERA5 reanalysis | GraphCast / GenCast | Operational forecasts |
| Math | mathlib + synthetic proofs | AlphaProof | Lean type checker |
| Materials | Materials Project + DFT | GNoME | DFT calculation |
| Code | GitHub + competitive programming | AlphaCode 2 | Test suites |
| Robotics | Open X-Embodiment | RT-2 / π₀ | Physical execution |

### The Verification Advantage

Domains where AI excels fastest share a common property: **solutions are easy to verify**. 

- In math: Lean checks proofs automatically
- In materials: DFT calculations validate stability predictions
- In code: tests verify correctness
- In weather: forecasts can be compared to observations
- In proteins: experimental structures provide ground truth

This enables the "generate many candidates, verify the best" paradigm that FunSearch, AlphaProof, and AlphaCode all exploit.

### Remaining Challenges

1. **Generalization beyond training distribution**: ML weather models may fail under novel climate conditions. AlphaFold struggles with proteins unlike anything in the PDB.

2. **Interpretability**: These systems produce answers, not understanding. A physicist can explain *why* a weather pattern develops; GraphCast just predicts it.

3. **Data hunger**: Robotics is bottlenecked by data scarcity. Materials science needs expensive DFT calculations for training labels.

4. **Integration with human science**: The most impactful systems augment human scientists rather than replacing them. AlphaGeometry's proofs are human-readable. FunSearch's programs are interpretable.

5. **Hallucination in high-stakes domains**: AlphaFold 3 can generate physically implausible structures. An incorrect weather forecast could lead to lives lost. Rigorous uncertainty quantification is essential.

---

## Key Papers & Sources

### Protein Structure Prediction
1. Jumper, J. et al. "Highly accurate protein structure prediction with AlphaFold." Nature 596, 583–589 (2021). https://www.nature.com/articles/s41586-021-03819-2
2. Abramson, J. et al. "Accurate structure prediction of biomolecular interactions with AlphaFold 3." Nature 630, 493–500 (2024). https://www.nature.com/articles/s41586-024-07487-w
3. Lin, Z. et al. "Evolutionary-scale prediction of atomic-level protein structure with a language model." Science 379, 1123–1130 (2023). https://www.science.org/doi/10.1126/science.ade2574
4. AlphaFold Protein Structure Database: https://alphafold.ebi.ac.uk/

### Weather & Climate
5. Lam, R. et al. "Learning skillful medium-range global weather forecasting." Science 382, 1416–1421 (2023). https://www.science.org/doi/10.1126/science.adi2336
6. Bi, K. et al. "Accurate medium-range global weather forecasting with 3D neural networks." Nature 619, 533–538 (2023). https://www.nature.com/articles/s41586-023-06185-3
7. Price, I. et al. "Probabilistic weather forecasting with machine learning." Nature (2024). https://www.nature.com/articles/s41586-024-08252-9
8. GraphCast code: https://github.com/google-deepmind/graphcast

### Mathematics
9. Trinh, T.H. et al. "Solving olympiad geometry without human demonstrations." Nature 625, 476–482 (2024). https://www.nature.com/articles/s41586-023-06747-5
10. AlphaProof & AlphaGeometry 2 blog: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
11. Romera-Paredes, B. et al. "Mathematical discoveries from program search with large language models." Nature 625, 468–475 (2024). https://www.nature.com/articles/s41586-023-06924-6
12. FunSearch code: https://github.com/google-deepmind/funsearch

### Materials Science
13. Merchant, A. et al. "Scaling deep learning for materials discovery." Nature 624, 80–85 (2023). https://www.nature.com/articles/s41586-023-06735-9
14. GNoME data: https://github.com/google-deepmind/materials_discovery

### Code & Software Engineering
15. Li, Y. et al. "AlphaCode 2 Technical Report." DeepMind (2023). https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf
16. Jimenez, C.E. et al. "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" arXiv:2310.06770 (2023). https://arxiv.org/abs/2310.06770
17. SWE-bench leaderboard: https://www.swebench.com/

### Robotics
18. Brohan, A. et al. "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control." arXiv:2307.15818 (2023). https://arxiv.org/abs/2307.15818
19. Physical Intelligence π₀: https://www.physicalintelligence.company/blog/pi0
20. Open X-Embodiment: https://robotics-transformer-x.github.io/

### Nobel Prizes & General
21. Nobel Prize 2024 — Physics: https://www.nobelprize.org/prizes/physics/2024/summary/
22. Nobel Prize 2024 — Chemistry: https://www.nobelprize.org/prizes/chemistry/2024/summary/
23. DeepMind blog: https://deepmind.google/blog/
24. Nature — AI for Science collection: https://www.nature.com/collections/ai-for-science

---

## Concepts for Knowledge Tree

1. **Protein folding problem** — the 50-year grand challenge of predicting 3D structure from amino acid sequence
2. **Multiple Sequence Alignment (MSA)** — alignment of homologous protein sequences revealing co-evolutionary constraints
3. **Evoformer** — AlphaFold 2's novel Transformer that jointly processes MSA and pair representations
4. **Invariant Point Attention (IPA)** — attention mechanism equivariant to 3D rotations and translations
5. **Diffusion models for molecular structure** — generative models that denoise random atom clouds into 3D structures (AlphaFold 3, GenCast)
6. **Protein language models** — Transformer models (ESM-2) trained on protein sequences that learn structural information implicitly
7. **Graph Neural Networks (GNNs)** — neural networks operating on graph-structured data (GraphCast, GNoME)
8. **Numerical Weather Prediction (NWP)** — physics-based weather forecasting by integrating atmospheric equations
9. **Ensemble forecasting** — running multiple simulations with perturbed initial conditions to quantify uncertainty
10. **Icosahedral mesh** — sphere-covering grid used by GraphCast for uniform global resolution
11. **Message passing** — GNN operation where nodes aggregate information from neighbors
12. **3D Earth-Specific Transformer** — Pangu-Weather's architecture treating atmosphere as a 3D volume
13. **Probabilistic weather forecasting** — predicting distributions of outcomes rather than single deterministic forecasts
14. **Formal verification / proof assistants** — software (Lean, Coq) that machine-checks mathematical proofs
15. **Neuro-symbolic AI** — combining neural networks (intuition) with symbolic reasoning (rigor) — AlphaGeometry
16. **Reinforcement learning for theorem proving** — training proof search via self-play and verification feedback (AlphaProof)
17. **Autoformalization** — translating informal mathematics to formal proof assistant code
18. **Evolutionary program search** — FunSearch's approach of evolving programs via LLM-guided mutation
19. **Formation energy** — thermodynamic quantity predicting crystal stability (GNoME)
20. **Active learning** — iteratively selecting the most informative data points for labeling (GNoME's DFT pipeline)
21. **Retrosynthesis** — working backward from target molecule to find synthetic routes
22. **Vision-Language-Action (VLA) models** — models that map visual observations and language instructions to robot actions (RT-2)
23. **Sim-to-real transfer** — training in simulation, deploying in reality, with domain randomization to bridge the gap
24. **Domain randomization** — varying simulation parameters during training to produce robust policies
25. **Zero-shot generalization** — performing tasks never seen during training by leveraging broad pretraining knowledge
26. **SWE-bench** — benchmark measuring AI ability to resolve real GitHub issues autonomously
27. **CASP (Critical Assessment of protein Structure Prediction)** — biennial competition that benchmarks protein structure prediction methods
28. **Triangle multiplicative updates** — AlphaFold's mechanism for enforcing geometric consistency in residue pair predictions
29. **Autoregressive weather rollout** — chaining short-term ML predictions to produce multi-day forecasts
30. **Foundation models for science** — large pretrained models adapted across scientific domains, following the NLP/vision paradigm

---

---

## 8. The Bigger Picture: What This All Means

### The Three Eras of Scientific Computing

**Era 1 — Simulation (1950s-2010s)**: Encode physical laws as equations, solve numerically on supercomputers. Weather models, molecular dynamics, finite element analysis. Strengths: interpretable, generalizable. Weaknesses: expensive, limited by approximations.

**Era 2 — Data-Driven Discovery (2015-2023)**: Train neural networks on scientific data. AlphaFold, GraphCast, GNoME. Strengths: faster, often more accurate. Weaknesses: opaque, limited to training distribution, requires massive data.

**Era 3 — AI-Augmented Science (2024+)**: Hybrid systems combining neural networks with formal reasoning, physical constraints, and human insight. AlphaProof (neural + formal logic), GenCast (ML + uncertainty quantification), FunSearch (LLM + rigorous evaluation). This is where the field is headed.

### What Makes AI-for-Science Different from AI-for-Tech

| Dimension | AI in Tech | AI in Science |
|-----------|-----------|---------------|
| Evaluation | User satisfaction, revenue | Ground truth, reproducibility |
| Failure cost | Bad recommendation | Wrong drug, missed tornado |
| Data | Abundant (internet) | Scarce (experiments are expensive) |
| Interpretability | Nice to have | Essential for trust |
| Verification | A/B testing | Formal proofs, experiments |
| Timeline | Quarterly releases | Multi-year research programs |

### The Next 5 Years

The most likely near-term breakthroughs:

1. **AI-designed drugs reaching Phase III trials** — validating the end-to-end pipeline from AlphaFold prediction to clinical candidate
2. **ML weather models becoming operational** — national weather services adopting ML ensembles for official forecasts (already beginning at ECMWF)
3. **Automated mathematical discovery at scale** — FunSearch-like systems contributing to multiple open problems
4. **New materials reaching production** — GNoME-predicted materials being manufactured for batteries, semiconductors, and superconductors
5. **General-purpose robot foundation models** — robots that can learn new tasks from a few demonstrations, deployed in warehouses and eventually homes
6. **AI-assisted scientific paper writing and review** — not replacing scientists, but accelerating the communication of results

The throughline is clear: **AI is becoming a general-purpose instrument of science**, as fundamental as the computer itself. The systems described in this document are the first generation. The next generation will be more accurate, more interpretable, more integrated with human scientific practice, and more widely accessible.

The Nobel Prizes of 2024 weren't an anomaly. They were a signal flare.

---

*Last updated: 2025. This document covers AI-for-science breakthroughs from 2022-2025. The field moves fast — by the time you read this, new records will have been set.*
