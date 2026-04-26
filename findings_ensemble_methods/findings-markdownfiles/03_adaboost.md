# AdaBoost

## Core Mechanism
- Minimizes exponential loss: L = e^{-y·f(x)}
- Wrong predictions → exponentially huge loss → weights go up
- Each weak learner gets vote weight α proportional to its accuracy
- α_t = 0.5 * ln((1 - error_t) / error_t)

## Classroom Analogy
- Each new tutor spends more time on students previous tutors couldn't help

## Weakness
- Very sensitive to outliers/noise (keeps upweighting hard examples which may be mislabeled)
- Superseded by gradient boosting in practice
- Historically important, theoretically elegant
