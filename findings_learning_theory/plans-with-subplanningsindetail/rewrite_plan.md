# Rewrite Plan: Learning Theory Foundations

## Running Example
A startup building a spam classifier. Start with 3 emails, grow naturally. Thread it throughout.

## Concept Ladder (dependency order)
1. The bet we make (generalization problem) - OPENING
2. No Free Lunch - motivation for why theory matters
3. PAC Learning - the first formal framework
4. VC Dimension - extending PAC to infinite classes (shattering via toy example)
5. Generalization bounds - connecting VC to practice
6. Rademacher complexity - data-dependent alternative  
7. Bias-Complexity tradeoff formalized
8. REST STOP
9. Double Descent - breaks classical picture
10. Benign Overfitting - why interpolation doesn't always hurt
11. Neural Tangent Kernel - infinite width lens
12. Implicit Regularization - SGD's hidden bias
13. Grokking - delayed generalization mystery
14. Why deep learning works despite overparameterization - synthesis

## Recurring Analogies
1. Courtroom analogy: training error = evidence, generalization = verdict, model complexity = number of witnesses (too many can confuse jury)
2. Map analogy: hypothesis class = set of possible maps, VC dim = most landmarks map can locate, overfitting = map that memorizes every tree but misses the roads

## Vulnerability Moments
1. Opening: avoided learning theory for years
2. VC dimension: confess the shattering concept took multiple tries
3. Double descent: "I didn't believe it when I first saw it"
4. NTK: "I'm still developing my intuition for this"
5. Grokking: "no one fully knows why"

## Style Notes
- Brandon Rohrer style: personal, journey, toy examples, step-by-step
- No bullet lists for explanations
- Define every term inline
- Motivate each section with frustration from previous
- Short paragraphs (2-5 sentences)
