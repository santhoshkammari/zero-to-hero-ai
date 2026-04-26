# Deep Learning Foundations Interview Gotchas

1. **BatchNorm train vs eval** — running stats differ; small batch sizes cause instability; eval mode uses accumulated stats not batch stats
2. **Dropout left on at inference** — stochastic outputs, miscalibrated probabilities. Must call model.eval()
3. **"Why not just use a wider network?"** — Universal Approximation says you can, but depth gives exponentially better parameter efficiency and hierarchical features
4. **Dying ReLU** — neurons that output zero for all inputs, permanently dead. Caused by large learning rates pushing weights negative. LeakyReLU/ELU mitigate
5. **Xavier init with ReLU** — Xavier assumes linear activations. ReLU kills half the variance. Use He initialization instead
6. **Double descent** — test error can IMPROVE if you keep adding parameters past the interpolation threshold. Classical bias-variance is incomplete
7. **Grokking** — converged training loss doesn't mean learning is done. Generalization can appear much later
8. **Lottery ticket ≠ "just use small networks"** — you need the large network to FIND the winning ticket
9. **NTK regime vs feature learning** — infinite-width theory is clean but real networks learn features, which is the whole point
10. **Soft targets > hard labels** — knowledge distillation works because teacher mistakes carry information about class structure
11. **Attention IS associative memory** — modern Hopfield networks proved this mathematically (Ramsauer et al. 2020)
12. **Flat minima generalize, sharp don't** — but defining "flat" rigorously is still debated (reparameterization invariance)
13. **NAS found architectures ≈ hand-designed** — the search cost often outweighs marginal gains
14. **BPTT is just backprop through unrolled time** — a 200-step RNN = 200-layer network for gradient computation
15. **Focal loss γ=0 IS cross-entropy** — it's a generalization, not a replacement
