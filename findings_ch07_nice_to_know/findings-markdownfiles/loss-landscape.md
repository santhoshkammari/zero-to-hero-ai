# Loss Landscape & Mode Connectivity

## Loss Landscape Topology
- Neural network loss functions create complex high-dimensional surfaces
- Multiple minima exist — but are they equally good?
- Flat minima tend to generalize better than sharp minima (Hochreiter & Schmidhuber 1997, Keskar et al. 2017)
- Large batch training → sharp minima → worse generalization

## Mode Connectivity (Draxler et al. 2018, Garipov et al. 2018)
- Different trained networks (different local minima) are connected by paths of low loss
- Not straight-line paths, but curved paths through parameter space
- Implies the loss landscape is more connected than previously thought
- Different "good" solutions aren't isolated islands — they're connected valleys

## Flat vs Sharp Minima
- Flat minimum: small perturbation of weights → small change in loss → robust
- Sharp minimum: small perturbation → large loss change → fragile, poor generalization
- SAM (Sharpness-Aware Minimization) explicitly seeks flat minima
- Stochastic weight averaging (SWA) also finds flatter regions

## Practical Implications
- Learning rate schedules affect which minima SGD finds
- Warmup → explore broadly; decay → settle into flat minimum
- Batch size affects sharpness (small batch → flat, large batch → sharp)
- Model soups: average weights of models along low-loss path

## Interview Angle
- Know flat vs sharp minima and generalization connection
- Know why learning rate warmup + decay matters geometrically
- Mode connectivity explains why ensemble methods and weight averaging work
