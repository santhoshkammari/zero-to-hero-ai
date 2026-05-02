# Chapter 14 — Probabilistic & Bayesian ML: Cleanup Report

Total chapter size: **~339 KB** across 5 content files + index.

| File | Size |
|------|------|
| bayesian-fundamentals.html | 55 KB |
| probabilistic-models-inference.html | 68 KB |
| sequential-models-ppl.html | 71 KB (largest) |
| gaussian-processes-bayesian-optimization.html | 60 KB |
| nice-to-know.html | 60 KB |

---

## Summary

Chapter 14 is well-structured and pedagogically strong. The main sources of bloat are:

1. **Wrap-Up sections** in 4 of 5 files that mechanically re-list every heading covered — pure recap with zero synthesis or new insight.
2. **"I'll be honest" / personal admission pattern** — appears **13+ times** across the chapter, creating a repetitive stylistic tic.
3. **Cross-file redundancy** — Bayesian Neural Networks (MC Dropout, Bayes by Backprop, etc.) are taught in *both* `sequential-models-ppl.html` AND `nice-to-know.html`.
4. **Verbose arithmetic walkthroughs** — step-by-step arithmetic narration where a summary + code would suffice.
5. **Repeated metaphors** — same metaphor used 2-3 times within a file (breathing, mountain/hiker, ice cream shop recycled 5+ times in sequential-models-ppl.html).

---

## Redundant Content

### CROSS-FILE: BNN / MC Dropout content duplicated (HIGH priority)

**`sequential-models-ppl.html`** section "Bayesian neural networks" teaches:
- BNN concept (distributions over weights)
- MC Dropout as cheap approximation
- Variational inference via Pyro/NumPyro
- Deep ensembles
- Ice cream shop example for BNN

**`nice-to-know.html`** section "Bayesian Deep Learning" teaches:
- MC Dropout (dedicated H3 subsection with clinic example)
- Bayes by Backprop (dedicated H3 subsection)
- Laplace Approximation (dedicated H3 subsection)

**Overlap:** MC Dropout is explained in both files. The `nice-to-know.html` version is deeper and better structured (with H3 subsections). The `sequential-models-ppl.html` version is briefer but redundant. **Recommendation:** Remove or drastically shorten the BNN section in `sequential-models-ppl.html` and cross-reference `nice-to-know.html`.

### WITHIN-FILE: "The Beta-Binomial, Step by Step" ↔ "Sequential Updating" (bayesian-fundamentals.html)

Both sections walk through the **identical** three-day example:
- Day 1: 10 visitors, 3 click → α=5, β=9
- Day 2: 20 visitors, 6 click → α=11, β=23
- Day 3: 50 visitors, 14 click → α=25, β=59

Section 6 does it with prose arithmetic. Section 7 repeats it with Python code using the same batches: `(3,7), (6,14), (14,36)`. **Recommendation:** Consolidate into one section. Either do the arithmetic inline with the code, or drop the manual walkthrough and let the code carry the example.

### WITHIN-FILE: Conditional independence explained twice (probabilistic-models-inference.html)

- "Drawing the Story: Bayesian Networks" introduces conditional independence (line ~365)
- "D-Separation: Reading Independence Off the Graph" re-explains it from scratch (line ~416)

The D-Separation section deepens the concept but re-covers ground already laid. **Recommendation:** In the Bayesian Networks section, briefly mention conditional independence and defer the full treatment to D-Separation rather than explaining it twice.

### WITHIN-FILE: Mountain/hiker metaphor repeated (probabilistic-models-inference.html)

The MCMC-vs-VI mountain metaphor appears in:
- "When Exact Answers Are Too Expensive" (line ~467): hikers with altimeters vs satellite images
- "The Optimization Path: Variational Inference" (line ~580): repeats the same satellite metaphor

**Recommendation:** Use the metaphor once in section 7, then reference it briefly in section 12 without restating it.

### WITHIN-FILE: Exploitation-exploration repeated per acquisition function (gaussian-processes-bayesian-optimization.html)

The exploitation-exploration tradeoff is stated in the general "Acquisition Functions" intro, then restated in each of the three subsections (EI, UCB, PI). The final recommendation at line ~525 also echoes an earlier recommendation already embedded in the EI subsection. **Recommendation:** State the tradeoff once in the intro, then each subsection only needs to say how it handles the tradeoff.

---

## Overly Verbose

### 1. Arithmetic narration in "The Beta-Binomial, Step by Step" (bayesian-fundamentals.html)

> "Day one: 10 visitors, 3 click. We update. α becomes 2 + 3 = 5. β becomes 2 + 7 = 9. Our posterior is Beta(5, 9), with mean 5/14 ≈ 0.357. The raw data said 30% clicked, our prior said 50%, and the posterior landed at about 36% — a compromise that leans toward the data because we saw 10 real observations against our 4 imaginary ones."

Three days of this level of arithmetic narration is excessive. A table or the code example alone would suffice.

### 2. Forward/Viterbi algorithm day-by-day walkthroughs (sequential-models-ppl.html)

Both "The forward algorithm" and "The Viterbi algorithm" trace through Day 1, Day 2, Day 3 with six-significant-figure arithmetic:

> "Day 2: We observe Medium. For each state today, we consider every state from yesterday, multiply the forward probability by the transition probability, sum them up, and multiply by today's emission probability. For Sunny today: (0.30 × 0.7 + 0.05 × 0.4) × 0.3 = 0.069..."

Each walkthrough is ~150 words of arithmetic. **Recommendation:** Keep Day 1 as illustration, summarize Days 2-3 in a compact table, or let the code carry the computation.

### 3. "MAP vs. MLE" introspective paragraph (bayesian-fundamentals.html)

> "I'm still building my intuition for when full Bayesian inference — integrating over the entire posterior rather than taking the mode — is worth the computational cost over MAP. The honest answer: it matters most when data is scarce..."

This is ~80 words of the author thinking out loud rather than teaching. The useful content ("matters most when data is scarce, MAP and full Bayes agree with large data") could be stated in 1-2 sentences.

### 4. "Choosing Your Path: When to Use Which" (probabilistic-models-inference.html)

Lines ~657-665 contain lengthy decision heuristics that could be condensed from ~180 words to ~90 without loss. The validation pattern (try VI → check with MCMC) is explained twice.

### 5. "Distribution Over Functions" buildup (gaussian-processes-bayesian-optimization.html)

The progression from single Gaussian → multivariate → GP takes 6 paragraphs where 3 would suffice:

> "Now take two random variables together — say, the temperature at Station A and Station B. A multivariate Gaussian distribution gives you a two-dimensional bell shape, and crucially, it encodes how the two temperatures correlate. If Station A is warm, Station B is probably warm too (they're in the same valley), and the multivariate Gaussian captures that."

Could be: "A multivariate Gaussian over stations A and B encodes their correlation — warm at A predicts warm at B."

### 6. Cat-in-warehouse analogy for particle filters (sequential-models-ppl.html)

~90 words (5 sentences) to explain a 4-step loop (sample, weight, resample, propagate). Evocative but oversized for the concept.

### 7. Bayesian Decision Theory dual presentation (bayesian-fundamentals.html)

The A/B test example is fully explained in prose (~100 words covering green/blue buttons, $5000 switching cost, 3pp lift threshold), then **the same example is repeated as Python code**. Either the prose walkthrough or the code is sufficient — having both is redundant.

---

## Content to REMOVE

### 1. All four Wrap-Up sections → REMOVE or replace with 1-2 sentence forward pointers

Every wrap-up mechanically re-lists all headings covered. None synthesize or add insight.

**bayesian-fundamentals.html — "Wrap-Up":**
> "We started with a philosophical question — what does probability mean? — and built up a complete machinery for updating beliefs with evidence. We traced through Bayes' theorem by counting, met the four characters (prior, likelihood, evidence, posterior), worked through the Beta-Binomial step by step..."

**probabilistic-models-inference.html — "Wrap-Up":**
> "We started with a simple observation: joint probability tables are exponentially large, and graphical models compress them by encoding which variables directly influence which others. We learned two flavors — Bayesian networks for causal stories, Markov random fields for undirected correlations..."

**gaussian-processes-bayesian-optimization.html — "Wrap-Up":**
> "We started with three weather stations in a valley and the question 'what's the temperature at the farmer's field?' To answer it, we built up from a single Gaussian to a multivariate Gaussian to a Gaussian Process..."

**nice-to-know.html — "Wrap-Up":**
> "We started with neural networks that admit uncertainty — MC Dropout as the quick retrofit, Bayes by Backprop as the principled approach, and Laplace approximation as the post-hoc solution..."

**Each is 100% redundant with the content that precedes it.** Replace each with a 1-sentence bridge to the next file/topic, or remove entirely.

### 2. BNN section in sequential-models-ppl.html → REMOVE (covered better in nice-to-know.html)

The "Bayesian neural networks" section (~15 lines) in `sequential-models-ppl.html` duplicates what `nice-to-know.html` covers in greater depth with proper H3 subsections. Replace with a 1-line cross-reference.

### 3. Duplicate BO insight (gaussian-processes-bayesian-optimization.html)

> "Each of those 50 trials is informed by all previous trials... Fifty intelligent trials often outperform 500 random ones. That's the power of Bayesian Optimization — not faster individual evaluations, but far fewer wasted evaluations."

Sentences 3 and 4 say the same thing. Remove sentence 4.

---

## Filler & Padding

### "I'll be honest" / personal admission pattern (chapter-wide)

This phrase and its variants appear **13+ times** across the chapter:

| File | Count | Examples |
|------|-------|---------|
| bayesian-fundamentals.html | 3 | "I'll be honest — the first time I read...", "I'll be honest: this term confused me for months", "I'm still building my intuition..." |
| probabilistic-models-inference.html | 4 | "I'll be honest — when I first saw this factoring trick...", "I still occasionally get tripped up by colliders", "I'll be honest — the physics connection took me a while", "I'm still developing my intuition for why the physics simulation..." |
| sequential-models-ppl.html | 3 | "I'll be honest — the first time I saw this, it felt like a magic trick", "I'm still developing my intuition for exactly when EKF fails", "I'll be honest — this idea was a genuine revelation" |
| gaussian-processes-bayesian-optimization.html | 3 | "I'll be honest — the first time I read this...", "I'm still developing my intuition for when each approximation...", "I'll be honest: the first time I saw a sparse GP..." |
| nice-to-know.html | 3 | "I'll be honest — I underestimated EP for years", "I won't pretend I have deep intuition...", "I'll be honest — the math can feel impenetrable" |

**Recommendation:** Keep 3-4 of the most impactful ones (e.g., the EP realization, the evidence term confusion). Cut or rephrase the rest. 13 occurrences makes it a verbal tic rather than an authentic voice.

### Breathing metaphor repeated 3x (sequential-models-ppl.html, "The predict-update cycle")

- "think of them as breathing. Inhale: predict. Exhale: update."
- "your uncertainty *grows* during prediction"
- "your uncertainty *shrinks*"
- "That rhythm — that breathing"

Used once it's evocative. Repeated 3 times it's padding. **Keep the first mention, cut the callbacks.**

### Ice cream shop scenario overuse (sequential-models-ppl.html)

The same ice cream shop is reintroduced for: HMMs (section 2), Kalman filters (section 8), PyMC (section 13), BNNs (section 17), and uncertainty quantification (section 18). By the BNN section the re-framing feels like padding rather than pedagogy. If the BNN section is removed (per above), this reduces to 4 uses, which is acceptable.

### Car engine analogy (sequential-models-ppl.html, "Probabilistic programming languages")

> "Building an HMM from scratch is like building a custom engine for a specific car. Using a PPL is like having a factory that can build any engine from a blueprint."

~30 words for a point that could be stated directly. Minor, but part of a pattern.

### Mystery novel analogy (sequential-models-ppl.html, "The backward algorithm and smoothing")

> "Another way to think about it: the forward pass is like reading a mystery novel from the beginning, and the backward pass is like reading from the end. Combining them gives you the full picture that neither direction alone can provide."

Nice imagery but follows right after another metaphor ("Information from the past meets information from the future"). Two metaphors for one concept is one too many.

---

## Estimated Impact

| Category | Estimated savings | Files affected |
|----------|------------------|----------------|
| Remove 4 Wrap-Up sections | ~1,500 words | All 4 main files |
| Remove duplicate BNN section | ~400 words | sequential-models-ppl.html |
| Consolidate Beta-Binomial + Sequential Updating | ~300 words | bayesian-fundamentals.html |
| Trim arithmetic walkthroughs (Forward, Viterbi) | ~200 words | sequential-models-ppl.html |
| Reduce "I'll be honest" occurrences (13 → 4) | ~400 words | All files |
| Trim verbose paragraphs (MAP introspection, Distribution Over Functions, etc.) | ~300 words | Multiple files |
| Remove duplicate metaphors & analogies | ~200 words | Multiple files |
| Trim Bayesian Decision Theory dual presentation | ~100 words | bayesian-fundamentals.html |
| Deduplicate exploitation-exploration in acquisition functions | ~100 words | gaussian-processes-bayesian-optimization.html |
| Trim conditional independence double-explanation | ~100 words | probabilistic-models-inference.html |
| **Total estimated reduction** | **~3,600 words (~10-12%)** | **All 5 files** |

The chapter's teaching content, topical coverage, and code examples remain fully intact. All cuts target presentation bloat — not subject matter.
