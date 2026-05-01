# Rewrite Plan for ch04/s01.html — ML Overview & Workflow

## Running Example
A spam filter for a small email startup — starts with 3 emails, scales up naturally.
Threads from taxonomy through workflow through leakage.

## Concept Ladder (dependency order)
1. What ML actually is (pattern recognition from data, not programming rules)
2. The taxonomy (supervised → unsupervised → RL → semi/self-supervised)
3. Inductive bias (why algorithms disagree — each has built-in assumptions)
4. No Free Lunch (why no algorithm wins everywhere)
5. Key terminology (features, target, loss, parameters, hyperparameters, generalization)
6. When NOT to use ML
7. REST STOP
8. End-to-end workflow (problem → data → features → model → evaluation → deploy)
9. Data leakage deep dive
10. Wrap-up

## Recurring Analogies
1. **The detective analogy** — ML is like a detective building a theory from evidence. 
   Inductive bias = detective's prior experience. NFL = different detectives excel at different cases.
2. **The recipe analogy** — workflow steps as cooking stages. 
   Problem definition = choosing what to cook. Features = ingredients. Model = the recipe. Evaluation = taste test.

## Vulnerability Moments
1. "I avoided thinking about what ML actually IS for an embarrassingly long time"
2. "I still sometimes pick the wrong problem framing on the first try"
3. "I'll be honest — inductive bias confused me for years"
4. "No one fully agrees on where the line between semi-supervised and self-supervised sits"
5. "I once shipped a model with preprocessing leakage and didn't catch it for weeks"

## Brandon Style Checklist
- Personal confession opening ✓
- Toy examples for every concept ✓
- Limitations shown for each section ✓
- Organic transitions ✓
- Terms defined inline ✓
- No "simply", "just", "obviously" ✓
