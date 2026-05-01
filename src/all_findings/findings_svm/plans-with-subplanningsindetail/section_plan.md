# SVM Section Rewrite Plan

## Running Example: Email spam classifier
- Start with 6 emails (3 spam, 3 not) plotted in 2D (word frequency features)
- Build up from drawing a line to margin maximization to kernels
- Scale naturally: add non-linearly separable case, then high-dim text case

## Concept Ladder (dependency order)
1. The line-drawing problem → why many lines exist, which is best?
2. Margin and support vectors → the widest-road intuition
3. The math behind the margin → primal form, why minimize ||w||²
4. Soft margin and slack variables → real data isn't clean, C parameter
5. The hinge loss connection → SVM as loss + regularization (like logistic regression's cousin)
6. REST STOP — you now understand linear SVMs
7. The kernel trick — motivation: non-linear data
8. RBF kernel and infinite dimensions — Taylor expansion intuition
9. Gamma parameter — spotlight vs floodlight analogy
10. C and gamma interaction — grid search
11. The dual form — why data only appears as dot products (enables kernels)
12. REST STOP 2 — you now understand the full SVM
13. Practical matters: scaling, multi-class, Platt scaling
14. When SVMs still matter today
15. SVM in code
16. Wrap-up

## Analogies (recurring)
1. "Widest road" between two neighborhoods — margin
2. "Spotlight vs floodlight" — gamma parameter
3. "Passport control" — support vectors are the border guards

## Vulnerability Moments
1. "I avoided SVMs for years because the math looked intimidating"
2. "I still find the dual form derivation hard to hold in my head"
3. "The connection between margin width and generalization isn't intuitive until you see it fail"
4. "Nobody has great intuition for why the RBF kernel works so magically"
5. "I get tripped up by C being inverted from λ in ridge regression"
