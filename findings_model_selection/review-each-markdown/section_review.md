# Review of Rewritten ch04/s06.html — Model Selection

## Checklist (from SYSTEM_PROMPT.md)

- [x] Opening has personal confession, orientation, heads-up, and journey invitation
- [x] Table of contents is present (inline TOC div)
- [x] Every concept section has: motivation → toy example → step-through → name → limitation
- [x] Rest stop with explicit permission to stop
- [x] Running example threads from first section through wrap-up (5,000 houses dataset)
- [x] Vulnerability/honesty moments distributed throughout:
  1. "I spent an embarrassing amount of time skipping to fanciest model"
  2. "one particularly humbling incident where linear regression beat my 500-tree ensemble"
  3. "I'm still developing my intuition for when AutoML is worth reaching for"
  4. "I still get tripped up by this temptation"
  5. "I wish someone had told me this five years ago"
  6. "I keep having to relearn this lesson"
- [x] Every term defined inline on first use (hyperparameters, SHAP, Shapley values, AIC, BIC, TPE, etc.)
- [x] No unexplained jargon
- [x] Analogies used more than once (building floors, restaurant analogy, rocket launcher/jar)
- [x] No bullet-point listicles for explanations
- [x] Wrap-up has gratitude, journey recap, and future hope
- [x] Resources section with personality
- [x] No "simply," "just," "obviously," "clearly," "of course"
- [x] Organic transitions (no "In this section we will")
- [x] Paragraphs 2-5 sentences
- [x] Short punchy sentences follow longer ones

## Topics Covered
- No Free Lunch Theorem
- Baselines (DummyClassifier)
- Model complexity vs data size
- Hyperparameter tuning (grid, random, Bayesian/TPE)
- Optuna with pruning
- AIC and BIC
- Learning curves
- Nested cross-validation
- SHAP and permutation importance
- AutoML (Auto-sklearn, FLAML)
- When simpler models win
- Complete workflow

## Interview Depth
- AIC/BIC math traced through example
- TPE internals explained (l(x)/g(x))
- Nested CV data leakage prevention
- Statistical model comparison (paired t-test, Wilcoxon)
- Feature-to-sample ratio
- Deployment constraints
