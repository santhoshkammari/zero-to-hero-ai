# Rewrite Plan for ch03/s07.html — Data Quality & Preparation

## Brandon Rohrer Style Approach
- Personal confession opening: avoided thinking about data quality, focused on models
- Running example: building a spam classifier for an email startup
- Build from absolute zero: what IS a label? → why labels matter → how labels go wrong → how to fix them
- Rest stop after labeling + augmentation basics
- Vulnerability moments throughout

## Section Structure (Concept Ladder)

### Phase 1: Opening
- Confession: I spent months tuning models when the data was the problem all along
- Orientation: Data quality is the ceiling your model can never exceed
- Heads-up: We'll touch on statistics and Python code, building as we go
- Journey invitation

### Phase 2: Table of Contents

### Phase 3: Build-Up Sections
1. **The Labeling Problem** — Running example: spam classifier. Why supervised learning needs labels. What makes a label "good."
2. **Annotation Guidelines & Agreement** — Writing clear rules. Cohen's Kappa. When disagreement reveals task ambiguity.
3. **When Manual Labels Are Too Expensive** — Weak supervision with Snorkel. Labeling functions. LabelModel.
4. **Active Learning** — Label smarter. Uncertainty sampling. The train/score/label loop. Real savings.
5. **Finding Bad Labels After the Fact** — Cleanlab / Confident Learning. Using model predictions to audit labels.
6. **Data Augmentation** — Creating training examples from transformations. Image (torchvision, CutMix, MixUp). Text. The one rule: preserve the label.
7. **Test-Time Augmentation** — Cheap accuracy boost at inference.

### REST STOP — You now understand labeling, augmentation, and label quality. That's 70% of the battle.

8. **Data Validation** — Great Expectations, Pandera. Schema enforcement. Treating data tests like code tests.
9. **Drift Detection** — KS test, PSI, Chi-square. Evidently AI. When your production data stops looking like training data.
10. **Data Contracts** — Formal agreements between producers and consumers. The future of data quality.

### Phase 4: Wrap-Up
- Gratitude, journey recap, future hope
- Resources

## Vulnerability Moments
1. Opening: spent months tuning hyperparameters when 3 mislabeled examples were the real problem
2. Annotation guidelines: I used to think labeling was trivial until I saw annotators disagree
3. Weak supervision: the first time I saw Snorkel's noisy labels outperform my careful ones
4. Drift: I still get a knot in my stomach when I think about the time we deployed without drift checks
5. Data contracts: still developing my intuition for where the boundary sits

## Recurring Analogies
1. Kitchen/restaurant: Data quality is the ingredient quality. Best chef can't save rotten ingredients.
2. Building foundation: You can't add floors to a cracked foundation without the whole thing tilting.
