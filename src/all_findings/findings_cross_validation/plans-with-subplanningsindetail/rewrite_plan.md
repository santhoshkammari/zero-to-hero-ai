# Cross-Validation Section Rewrite Plan

## Running Example
- Building a spam classifier for a small company with 2,000 emails
- Grows naturally: start with 10 emails, scale to 2000, add time dimension, add user groups

## Concept Ladder
1. The trust problem — why a single split is unreliable (motivate with shuffled results)
2. K-Fold from scratch — build the mechanic with 10 emails
3. The choice of k — bias-variance of the estimator itself
4. Stratified K-Fold — motivated by imbalanced spam ratio
5. REST STOP
6. Time Series Split — motivated by "what if emails arrive over time?"
7. Group K-Fold — motivated by "what if same sender appears in train+test?"
8. Nested CV — motivated by "we tuned hyperparameters, now our score is lying"
9. The preprocessing trap — leakage through fit_transform before split
10. Comparing models fairly — same folds, paired differences

## Analogies (recurring)
1. **Taste-testing analogy** — judging a chef by one dish vs. having them cook 5 different meals
2. **Exam analogy** — studying with the answer key vs. studying independently and taking the test blind

## Vulnerability Moments
1. Confession about trusting a single split early in career
2. "I still occasionally mess up the preprocessing pipeline"
3. "The LOOCV result surprised me when I first saw it"
4. "No one talks about how uncomfortable it is to watch your score drop when you fix leakage"

## Style
- Brandon Rohrer voice: practitioner who went down the rabbit hole
- First person for experience, first person plural for the journey
- Toy examples first, name concepts after
- Every section: motivation → example → walkthrough → name → limitation
