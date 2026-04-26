# ML Interview Gotchas & Edge Cases

## Data Leakage
- Including future information in training features
- Preprocessing (scaling, imputing) before train/test split
- Target leakage: features that are proxies for the label

## Simpson's Paradox
- Aggregated trend reverses when data is stratified
- Classic: treatment appears better overall but worse in every subgroup
- Always check subgroup behavior, not just aggregate metrics

## Goodhart's Law
- "When a measure becomes a target, it ceases to be a good measure"
- Optimizing click-through rate → clickbait
- Optimizing accuracy on imbalanced data → always predicting majority class
- Your model will find shortcuts you didn't anticipate

## Label Noise
- Deep networks memorize noisy labels → hurts generalization
- Different annotators disagree → inter-annotator agreement matters
- Noise-robust losses exist (symmetric cross-entropy, etc.)

## Double Descent
- Classical: more parameters → eventually overfits
- Modern reality: past interpolation threshold, test error decreases again
- Challenges the classical bias-variance U-curve
- Happens in linear models, trees, and neural networks
