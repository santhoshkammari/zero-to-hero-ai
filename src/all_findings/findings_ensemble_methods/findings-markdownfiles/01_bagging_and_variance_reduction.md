# Bagging & Variance Reduction

## Core Insight
- Var(ensemble) = (1/B) * σ² + [(B-1)/B] * ρ * σ²
- If ρ = 1 (fully correlated), no reduction. If ρ = 0, variance reduces by factor B.
- Key: bagging only helps high-variance, low-bias models (deep trees). Pointless on linear models.
- ~63.2% unique samples per bootstrap (1 - 1/e), rest are duplicates.
- OOB: ~36.8% left out per tree → free validation.

## Why It Works
- Each tree overfits differently because it saw different data subset
- Averaging cancels uncorrelated errors
- Bias unchanged (each tree is high-capacity), variance drops
