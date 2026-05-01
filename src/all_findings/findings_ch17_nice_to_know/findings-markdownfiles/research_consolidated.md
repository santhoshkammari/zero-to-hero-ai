# Ch17 Nice to Know - Research Consolidated

## Topics to Cover
1. Optimal Transport (Wasserstein distance, Sinkhorn)
2. Information Bottleneck Method
3. Minimum Description Length & Algorithmic Information Theory
4. Computational Complexity of Learning
5. Lottery Ticket Hypothesis (revisited with theory)
6. Neural Collapse
7. Feature Learning Theory
8. Scaling Law Theory
9. Universality in Deep Learning (Double Descent, Grokking, Emergent Abilities)

## Key Insights
- Optimal Transport: Earth Mover's Distance = minimum cost of reshaping one distribution into another. Sinkhorn adds entropy for speed.
- Information Bottleneck: Compress input while preserving prediction-relevant info. Two phases: fitting then compression.
- MDL: Occam's Razor formalized. Shortest total description = best model. Connected to Kolmogorov complexity.
- Computational Complexity: Proper PAC learning of NP-hard concept classes is intractable. Improper learning can sometimes help.
- Lottery Ticket: Sparse subnetworks exist at initialization that can match full network performance. Strong LTH = no training needed.
- Neural Collapse: In terminal training phase, features collapse to simplex ETF structure. Maximally symmetric class separation.
- Feature Learning: Lazy/NTK regime (features frozen) vs rich/mean-field regime (features evolve). Real networks do feature learning.
- Scaling Laws: Loss follows power law in compute/params/data. Chinchilla: balance model size and data.
- Universality: Double descent, grokking, emergent abilities - deep learning defies classical statistics.
