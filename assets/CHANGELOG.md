# Changelog

All notable changes to the **Zero to Hero AI** book will be documented in this file.

Format: Each entry includes the date, what changed, and which chapter/section was affected.

---

## [Unreleased]

### 2026-04-25 — Full Book v3 Rewrite (ch02-ch18)

- **Rewrote all 17 remaining chapters** (ch02-ch18) using v3 philosophy: variable depth, conversational tone, production-focused
- **Total consolidation**: 209 sections → 150 sections (28% reduction)
- **Global sidebar sync**: Updated sidebar nav in all 169 HTML files (168 chapter files + root index.html) to reflect new section structure

#### Chapter-by-chapter summary:
| Ch | Topic | Before → After | Deep Sections |
|----|-------|----------------|---------------|
| 02 | Math Foundations | 8→8 | Linear Algebra, Probability & Statistics (merged) |
| 03 | Data Fundamentals | 13→10 | EDA, Cleaning & Feature Engineering (merged) |
| 04 | ML Fundamentals | 8→8 | ML Workflow, Bias-Variance+Overfitting (merged), Metrics |
| 05 | Supervised Learning | 11→9 | Linear/Logistic Regression, Trees, Ensembles |
| 06 | Unsupervised Learning | 7→6 | Clustering, Dimensionality Reduction |
| 07 | DL Foundations | 8→7 | Loss Functions, Backpropagation |
| 08 | Training Deep Nets | 16→8 | Optimization, Normalization/Reg, PyTorch |
| 09 | CNNs & Vision | 14→9 | CNN Blocks, Architecture Evolution, Transfer Learning |
| 10 | Sequence & Attention | 12→7 | Transformer Self-Attention, BERT vs GPT |
| 11 | NLP | 9→7 | Word Embeddings, Tokenization |
| 12 | LLMs | 22→12 | Pretraining/Scaling, Prompting, RAG, Alignment, PEFT, Production |
| 13 | ML Systems | 15→9 | System Design, Deployment/Serving, MLOps |
| 14 | Bayesian ML | 14→8 | Bayesian Inference, VI & MCMC |
| 15 | Generative Models | 8→6 | Diffusion Models |
| 16 | Advanced DL | 12→7 | Multimodal Models (CLIP/VLMs) |
| 17 | Learning Theory | 13→7 | Reinforcement Learning |
| 18 | AI Ethics & Safety | 9→7 | Fairness, Privacy, Security, Guardrails |

- **Created**: `chapter-wise-folder/ch02.md` through `ch18.md` — per-chapter tracking files
- **Moved**: Tangential sections to `dont-know-where-to-keep/` per chapter as needed

---

### 2026-04-25 — Chapter 01 v3 Rewrite
- **Added**: `assets/instructions.md` — Book writing philosophy and instructions
- **Added**: `assets/CHANGELOG.md` — This changelog file
- **Updated**: `assets/instructions.md` — Added "Why First" principle, Two Lanes rule, Training for Reality mindset, Nice to Know chapter-end section requirement
- **Moved**: `ch01/s22.html` (Modern Python Features) → `dont-know-where-to-keep/ch01/` (content used in Nice to Know)
- **Moved**: `ch01/s24.html` (Testing, Debugging, Profiling) → `dont-know-where-to-keep/ch01/`
- **Moved**: `ch01/s25.html` (ML Implementation Patterns) → `dont-know-where-to-keep/ch01/`
- **Reorganized**: Chapter 01 — 25 sections → 15 sections:
  - s01: Python Essentials *(merged from old s01-s05)*
  - s02: Pythonic Patterns *(merged from old s06+s08+s09)*
  - s03: Object-Oriented Programming *(deep revision)*
  - s04: File I/O *(deep revision)*
  - s05: Modules and Packages *(deep revision)*
  - s06: NumPy *(deep revision)*
  - s07: Pandas *(deep revision)*
  - s08: SciPy *(concise revision)*
  - s09: Data Visualization *(deep revision)*
  - s10: Jupyter Notebooks *(concise revision)*
  - s11: Version Control with Git *(concise revision)*
  - s12: Scikit-learn *(concise revision)*
  - s13: Python Under the Hood *(merged from old s19-s21)*
  - s14: Algorithms and Data Structures for ML *(intro/reality revision)*
  - s15: Nice to Know *(new section)*
- **Updated**: Sidebar navigation across all 232 HTML files to reflect new ch01 structure
- **Verified**: HTML structure validity and content quality via automated review agents

### v2 Table-Driven Rewrite
- **Rewrote**: All 15 ch01 sections from verbose prose → table-driven expert notes
  - Total: ~13k lines → ~3.3k lines (~75% reduction)
  - Every section now tables-first, 1-2 sentence glue, ML/production context
  - s01 (5 tables), s02 (4), s03 (6), s04 (3), s05 (4), s06 (14), s07 (8), s08 (2), s09 (4), s10 (2), s11 (3), s12 (3), s13 (6), s14 (2), s15 (1)
- **Verified**: Structure (HTML validity, nav, table presence) + Content quality (style compliance, line counts)
- **Fixed** post-verification:
  - s12: Trimmed h1 subtitle ("— The Universal ML API" removed)
  - s06: Removed verbose broadcasting intro paragraph
  - s13: Collapsed verbose TL;DR + motivational preamble to single sentence
  - s15: Added missing checklist section
- **Updated**: `assets/instructions.md` — Added table-driven writing style rules, content budgets
- **Created**: `chapter-wise-folder/general-approach.md` — Standardized approach for all chapters
- **Created**: `chapter-wise-folder/ch01.md` — Chapter 1 specific intent and v2 targets

### v3 Variable-Depth Rewrite (Concept-Driven, Conversational Tone)
- **Complete rewrite**: All 15 ch01 sections — variable depth per concept, conversational Brandon Rohrer-inspired tone
  - v2 had 67 uniform tables → v3 uses tables ONLY for comparisons/decisions (~13 total)
  - Power tools (collections, itertools, broadcasting, groupby, method chaining) get deep treatment with real code
  - Common knowledge (types, basic OOP, imports) reduced to 1-2 lines
  - Format matches concept: tables for decisions, prose for "why", code for leverage tools
- **Updated**: `assets/instructions.md` — Complete rewrite with v3 philosophy, tone guide, depth rules
- **Updated**: `chapter-wise-folder/general-approach.md` — Added tone section, updated format matching
- **Updated**: `chapter-wise-folder/ch01.md` — Status v3, added intents #11-#16
- **Verified**: Structure (all checks pass) + Content quality (variable depth correct, tone good)
- **Fixed** post-verification:
  - s15: Removed walrus operator and match/case (duplicated from s01)
  - s15: Renamed itertools/functools sections to "The Rest You'll See in the Wild"
  - s13: Added GIL "why it exists" paragraph (reference counting thread safety)
