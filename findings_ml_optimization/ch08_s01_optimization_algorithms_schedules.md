# Findings: Optimization Algorithms & Schedules (ch08/s01)

## Key Research Findings

### Optimizer Evolution Timeline
- SGD (pre-2010) → Momentum (Polyak 1964, Rumelhart 1986) → Adagrad (Duchi 2011) → RMSprop (Hinton 2012, unpublished Coursera lecture) → Adadelta (Zeiler 2012) → Adam (Kingma & Ba 2014) → AdamW (Loshchilov & Hutter 2017/2019)
- Each solved the previous one's limitation: SGD oscillates → momentum smooths → Adagrad adapts per-param but decays too aggressively → RMSprop uses EMA instead of sum → Adam combines momentum + RMSprop + bias correction → AdamW fixes broken weight decay

### Adam Deep Dive
- Tracks two running averages per parameter: first moment (mean of gradients = direction) and second moment (mean of squared gradients = magnitude/noise)
- Divides by √v: frequent large gradients → smaller effective LR (cautious); rare/small gradients → larger effective LR (bolder)
- Bias correction matters only at startup: at t=1 with β₁=0.9, correction multiplies by 10×; by t=20 it's negligible
- Default hyperparams (β₁=0.9, β₂=0.999, ε=1e-8, lr=0.001) are still standard

### AdamW vs Adam+L2
- In Adam, L2 regularization gradient (2λθ) gets processed through adaptive term → regularization weakened for params with large gradients
- AdamW applies weight decay directly to weights AFTER the gradient update → consistent shrinkage force
- Practically better generalization, more predictable regularization behavior
- Paper: Loshchilov & Hutter, "Decoupled Weight Decay Regularization" (arxiv 1711.05101)

### SGD vs Adam Generalization Gap
- Wilson et al. (2017): Adam often doesn't generalize as well as SGD+momentum despite faster training
- SGD noise from stochastic batches helps escape sharp minima, favors flat ones
- Adam tends to converge to sharper minima → larger generalization gap
- Keskar et al. (2017): batch size and optimizer choice affect flatness
- Practical: some teams use Adam for initial training, switch to SGD for final fine-tuning

### LARS and LAMB (Large Batch Optimizers)
- LARS (Layer-wise Adaptive Rate Scaling): per-layer LR scaling based on ratio ||weights|| / ||gradients|| — enables batch sizes of 8K-32K
- LAMB (Layer-wise Adaptive Moments for Batch training): combines Adam with LARS-style layer scaling — used for BERT pretraining at 32K-64K batch sizes
- Key insight: different layers have different weight/gradient norms, so a global LR is suboptimal at very large batch sizes
- Neither is needed for typical training; they're for distributed training at scale

### Cosine Annealing
- Smooth decay following cosine curve: η_t = η_min + ½(η_max - η_min)(1 + cos(T_cur/T_max · π))
- Better than step decay because: no abrupt shocks, more time at moderate LRs (where learning is productive), very gentle tail lets model settle into flat regions
- Cosine with warm restarts (SGDR, Loshchilov & Hutter 2016): LR snaps back after each cycle, helps escape local minima
- T_mult parameter makes subsequent cycles longer

### Learning Rate Warmup
- Essential for transformers and large batch training
- Why: early gradients are unreliable (random init), Adam moments haven't converged, large steps on garbage gradients cause instability
- Transformers simply don't train without warmup — attention mechanism is particularly sensitive
- Typical: 5-10% of total training steps; linear ramp from ~0 to target LR

### One-Cycle Policy (Leslie Smith 2018)
- Ramp LR up to peak, then anneal down to near zero in a single cycle
- Key insight: high LR in middle acts as regularization, prevents settling into sharp minima too early
- Momentum is often cycled inversely: decreases when LR rises, increases when LR falls
- "Super-convergence": can achieve same accuracy in 5-10× fewer epochs
- Critical gotcha: steps per batch, not per epoch

### SWA (Stochastic Weight Averaging)
- Average weights from multiple points late in training
- Tends to land in flat, wide minima (intersection of many local minima basins)
- Simple to implement: just maintain a running average of weights
- Izmailov et al. 2018: "Averaging Weights Leads to Wider Optima and Better Generalization"
- PyTorch has built-in SWA support

### Interview-Critical Knowledge
- Why Adam converges faster (per-param adaptive LR)
- Adam vs AdamW (decoupled weight decay — most important distinction)
- When SGD beats Adam (vision tasks, when you can tune LR schedule → flatter minima)
- Warmup + cosine = modern default recipe
- LAMB/LARS for distributed large-batch (shows systems-level understanding)
- SWA as a simple generalization booster
- LR finder technique (Leslie Smith 2017)
- Checkpoint resumption must include optimizer + scheduler state
