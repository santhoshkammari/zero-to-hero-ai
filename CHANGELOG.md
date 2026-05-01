# Changelog

All notable changes to the **Zero to Hero AI** curriculum are documented here.

## [2025-05-02] — Curriculum Restructure: Zero-to-Hero Alignment

A comprehensive audit of the 18-chapter curriculum identified 9 structural
problems — topics introduced before prerequisites, duplicated content across
chapters, and misordered parts. All 9 have been resolved.

### Moved

- **Scikit-learn** (Ch 1 → Ch 4) — Moved after ML Optimization so learners
  meet ML theory before the toolkit. ([`6ffda95`])
- **Algorithms & Data Structures for ML** (Ch 1 → Ch 17) — Hash maps, HNSW,
  autograd graphs, and beam search assume deep-learning knowledge; relocated
  to Learning Theory & Advanced ML. ([`6ffda95`])
- **Reinforcement Learning** (Ch 17 nav → Ch 10 nav) — RL concepts
  (MDPs, policy gradient, PPO, RLHF) now appear before the LLM chapters that
  rely on them. ([`31deeca`], [`6d09755`])

### Removed (archived)

- **Self-Supervised & Representation Learning** from Ch 6 — Duplicate of
  Ch 16 (Advanced Deep Learning) which covers contrastive learning, BYOL, and
  MAE in full depth. Archived as `_removed-*`. ([`c617222`])
- **Retrieval-Augmented Generation** from Ch 11 — Duplicate of Ch 12 (LLMs)
  which owns the complete RAG pipeline. Archived as `_removed-*`.
  ([`c617222`], [`adfecee`])

### Narrowed

- **Ch 2 Optimization** — Removed ~300 lines of ML optimizer content
  (SGD, Adam, momentum, learning-rate schedules) that duplicated Ch 4.
  Chapter now focuses on pure mathematical optimization: convexity,
  constrained optimization (Lagrangians, KKT, duality), and second-order
  methods (Newton, L-BFGS). Cross-references Ch 4 for practical ML
  optimizers. ([`6ffda95`])
- **Ch 5 Time-Series Forecasting** — Replaced deep-learning forecasting
  section (LSTM, Transformers) with a forward-reference callout to
  Ch 7–10. Chapter now covers classical methods only: ARIMA, Prophet,
  walk-forward validation, feature engineering. ([`6ffda95`])
- **Ch 9 Interpretability & Visualization** — Removed LIME, SHAP, and
  Mechanistic Interpretability sections (covered in Ch 16). Chapter now
  focuses on vision-specific methods: Grad-CAM, saliency maps, occlusion
  sensitivity, feature visualization, TCAV, attention maps.
  ([`4b045dc`], [`7eeac71`])

### Reordered

- **Probabilistic & Bayesian ML (Ch 14) and Generative Models (Ch 15)**
  now appear before **ML Systems & Production (Ch 13)** in navigation.
  Learners cover the theory before seeing production deployment.
  ([`b0f5985`], [`b7ec81d`])

### Fixed (during verification)

- Stale prev/next links for RL section after nav move ([`6d09755`])
- Leftover "· RAG" text in Ch 11 chapter overview ([`adfecee`])
- Standalone SHAP paragraph in Ch 9 toolbox replaced with Ch 16
  cross-reference ([`7eeac71`])
- Wrong nav order in `ch01/async-io.html` for Ch 14-15/Ch 13 swap
  ([`b7ec81d`])
- Breadcrumb, card numbering, and prev-link class for Algorithms page
  in Ch 17 ([`6d09755`])

### How it was verified

Every change was verified by parallel sub-agents checking:
sidebar nav consistency across all 148 HTML files, prev/next link chains,
chapter index card numbering, and content correctness. A final browser
walkthrough (agent-browser) confirmed all clicks and navigation work
end-to-end.

---

*No chapter numbers were changed. Only navigation order and section
placement were modified.*
