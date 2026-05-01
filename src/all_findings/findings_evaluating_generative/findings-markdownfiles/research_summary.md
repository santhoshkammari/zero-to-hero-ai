# Research Summary: Evaluating Generative Models

## Key Topics Covered
1. FID - Fréchet Inception Distance (Heusel et al 2017): Wasserstein-2 between Gaussians in Inception feature space
2. IS - Inception Score (Salimans et al 2016): KL(p(y|x) || p(y)), higher better, ImageNet biased
3. CLIP Score: cosine similarity in CLIP embedding space for text-image alignment
4. LPIPS (Zhang et al 2018): Learned perceptual metric using deep features, per-pair distance
5. Precision/Recall (Kynkäänniemi 2019): Precision=realism, Recall=coverage. Density/Coverage (Naeem 2020) improve on these
6. Mode collapse detection: visual inspection, latent interpolation, unique sample counts, FID/recall metrics
7. Likelihood evaluation (Theis 2016): bits/dim doesn't equal sample quality; good likelihood ≠ good samples
8. Goodhart's Law: when FID becomes target, models game it (mode collapse, overfitting stats, distribution matching tricks)
9. Human eval: MOS (1-5 scale), 2AFC (pairwise), Elo ratings (chess-style from pairwise comparisons)
10. Benchmark datasets: CIFAR-10, ImageNet 256x256, LSUN, COCO (text-to-image)

## Key Insights for Writing
- The fundamental tension: quality vs diversity vs faithfulness
- No single metric captures everything - need multi-metric approach
- FID's Gaussian assumption is key strength AND weakness
- Theis 2016 is crucial: likelihood and sample quality are not the same thing
- Precision/recall decompose what FID conflates
- Goodhart's law is the meta-lesson of this entire section
