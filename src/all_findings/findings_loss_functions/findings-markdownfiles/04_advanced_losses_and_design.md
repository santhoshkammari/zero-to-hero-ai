# Advanced Loss Functions and Custom Design

## Huber Loss / Smooth L1
- Quadratic for |error| ≤ δ (MSE-like), linear for |error| > δ (MAE-like)
- Smooth L1 in PyTorch ≈ Huber loss
- δ = 1.0 good default when targets standardized
- Used in DQN (reinforcement learning) for stability with noisy TD targets
- Heuristic: set δ to median absolute deviation of residuals

## Hinge Loss
- max(0, 1 - y·f(x)) — SVM's loss function
- Creates max-margin classifier
- Penalizes not just misclassified but also within-margin correct predictions

## Knowledge Distillation Loss
- Weighted combination: CE(student, labels) + KL(student, teacher_soft_outputs)
- Temperature parameter softens teacher outputs to reveal "dark knowledge"

## Label Smoothing
- Replace hard labels [0,0,1,0] with [ε/K, ε/K, 1-ε+ε/K, ε/K]
- Prevents overconfidence, improves calibration
- Regularization effect

## Perceptual Loss
- Compare feature activations (e.g., VGG features) instead of pixels
- L_perceptual = ||φ(x) - φ(x̂)||² where φ is pretrained network
- Used in super-resolution, style transfer

## Loss Surface Landscape
- Loss function shapes the optimization landscape
- Different losses → different landscapes (valleys, saddle points, plateaus)
- MSE on linear model → single convex bowl
- CE on deep network → complex non-convex landscape with many saddle points
- Saddle points more common than local minima in high dimensions
