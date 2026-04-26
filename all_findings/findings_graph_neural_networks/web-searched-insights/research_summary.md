# GNN Research Summary

## Key Insights from Research

### Message Passing
- Universal framework: message, aggregate, update
- Must be permutation-invariant (sum, mean, max)
- k layers = k-hop neighborhood

### GCN (Kipf & Welling 2017)
- Spectral origin simplified to spatial
- Chebyshev polynomial approx, K=1 first-order
- H^(l+1) = σ(D̃^(-½) Ã D̃^(-½) H^(l) W^(l))
- Ã = A + I (self-loops), D̃ = degree matrix of Ã
- Symmetric normalization prevents high-degree domination

### GAT (Veličković et al. 2018)
- Attention scores between node pairs
- Only attends to neighbors (sparse), unlike Transformer (dense/global)
- e_ij = LeakyReLU(a^T[Wh_i || Wh_j])
- Multi-head stabilizes training
- GATv2 (Brody 2021) fixes static ranking issue

### GraphSAGE (Hamilton et al. 2017)
- Inductive: learns aggregation function, not fixed embeddings
- Neighborhood sampling: fixed # of neighbors per layer
- Enables mini-batch training on billion-edge graphs
- Aggregators: mean, LSTM (shuffle), max-pool

### Over-smoothing
- Repeated averaging → all nodes converge to same representation
- Like Gaussian blur repeated
- 2-3 layers sweet spot
- Solutions: skip connections, DropEdge, JK networks, PairNorm

### WL Test & Expressiveness
- 1-WL: iterative color refinement
- MP-GNNs ≤ 1-WL in power
- GIN = 1-WL (maximally powerful MP-GNN)
- Highly symmetric graphs fool both WL and GNNs
- Higher-order WL tests more powerful but costly

### Graph Pooling
- Global: mean, sum, max (simple, no params)
- DiffPool: learned soft cluster assignments
- SAGPool: attention-based node selection (top-k)

### Applications
- Molecules: atoms=nodes, bonds=edges, property prediction
- Social: fraud, community detection, influence
- Recommendations: user-item bipartite graphs (Pinterest, Twitter)
- Knowledge graphs: entity/relation completion

### Frameworks
- PyG: PyTorch-native, research-friendly, great model zoo
- DGL: better for large-scale/heterogeneous, industry (AWS)
