# Double Descent

## Core Idea
- Test error doesn't always follow classic U-shaped bias-variance curve
- Three regimes: underfitting → classical overfitting peak → second descent in overparameterized regime
- The interpolation threshold (model barely fits training data) is the WORST place to be
- Beyond it, SGD's implicit regularization finds simpler solutions among many that fit

## Key Insight
- Classical statistics says: more parameters → more overfitting
- Double descent says: keep going past that, and error drops again
- Explains why "just make it bigger" works for deep learning

## Where It Shows Up
- Model-wise: wider/deeper networks past interpolation threshold
- Epoch-wise: training longer can show same pattern (train more → worse → better)
- Sample-wise: more data can temporarily HURT near the threshold (Belkin et al. 2019)

## Why Interviewers Love It
- Tests whether you understand modern generalization beyond textbook bias-variance
- The interpolation threshold is the key concept
- Connects to: implicit regularization of SGD, overparameterization benefits, scaling laws

## Gotcha
- Double descent doesn't mean "always make models bigger" — it means the bias-variance tradeoff is incomplete
- Regularization can smooth out the peak, making it less dramatic
