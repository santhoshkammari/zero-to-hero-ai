# Focal Loss, Contrastive Loss, Triplet Loss

## Focal Loss
- Downweights easy examples via (1-pt)^γ modulating factor
- γ=0 → standard CE; γ=2 (typical) → strong focus on hard examples
- α balancing handles class frequency; γ handles prediction difficulty
- Key insight: weighted CE adjusts for class frequency, focal loss adjusts for prediction confidence
- RetinaNet: simple one-stage detector beat all two-stage architectures — bottleneck was loss, not model

## Contrastive Loss
- Pairs: pull similar together, push dissimilar apart
- L = (1-y)·½D² + y·½max(0, m-D)²
- Margin m: minimum desired separation for dissimilar pairs
- Used in Siamese networks (face verification, signature verification)

## Triplet Loss
- Triplets: anchor, positive, negative
- L = max(0, D(a,p) - D(a,n) + m)
- Hard negative mining essential — random negatives too easy, don't teach anything
- FaceNet: landmark paper using triplet loss

## InfoNCE
- Many negatives at once (batch-based)
- L = -log(exp(sim(z,z+)/τ) / Σexp(sim(z,zi-)/τ))
- Temperature τ controls softness
- Used in SimCLR, MoCo, CLIP

## Quantile/Pinball Loss
- Asymmetric: penalize over/under-prediction differently
- q=0.5 → MAE; q≠0.5 → asymmetric
- Enables prediction intervals (e.g., 10th and 90th percentiles)
- Applications: demand forecasting, risk assessment, Value at Risk
