# Neural Architecture Search (NAS)

## Core Idea
- Automate the design of neural network architectures instead of hand-crafting them
- Search space: what operations, connections, layer types to consider
- Search strategy: RL, evolutionary algorithms, gradient-based (DARTS)
- Performance estimation: how to evaluate candidate architectures cheaply

## Key Methods
- **Zoph & Le (2017)**: RL-based NAS, found NASNet — required 1800 GPU days
- **ENAS (2018)**: shared weights across architectures, much cheaper
- **DARTS (2019)**: differentiable relaxation, continuous search space, gradient-based — few GPU days
- **ProxylessNAS**: search directly on target task/hardware

## DARTS Innovation
- Relaxes discrete architecture choices to continuous weights
- Train architecture parameters and network weights jointly via bilevel optimization
- After search, discretize by keeping highest-weight operations
- Reduced search from thousands of GPU days to single GPU days

## Practical Reality
- NAS-found architectures often only marginally better than hand-designed ones
- The search cost can be enormous (original NAS: $100K+ in compute)
- Modern efficient NAS makes it more accessible
- Most impactful contribution: inspiring EfficientNet, MobileNet families

## Interview Gotcha
- Know DARTS and why it was a breakthrough (differentiable search)
- Know the compute cost criticism of early NAS
- Understand search space design matters more than search algorithm
