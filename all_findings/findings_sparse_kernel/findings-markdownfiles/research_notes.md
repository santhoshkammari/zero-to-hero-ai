# Sparse & Kernel Methods - Research Notes

## Key Concepts to Cover

### Sparsity in ML
- L1 motivation: geometric intuition (diamond vs circle), why exact zeros
- LASSO path: how coefficients shrink as lambda increases, regularization path visualization
- Elastic net: best of both worlds, handles correlated features
- Compressed sensing: Nyquist vs sparse recovery, RIP, MRI application

### Sparse Coding & Dictionary Learning
- Represent data as sparse combination of learned atoms
- Dictionary learning: learn the atoms from data (K-SVD)
- Applications: image denoising, feature extraction
- Connection to neuroscience (sparse neural coding)

### Kernel Methods Beyond SVM
- Kernel PCA: nonlinear dimensionality reduction via kernel matrix eigendecomp
- Kernel regression: weighted sum of kernel evaluations
- Multiple kernel learning: combine kernels, learn weights

### RKHS Intuition
- Functions as vectors in a space
- Kernel reproduces function values via inner products
- Representer theorem: optimal solution is linear combo of kernel evals at training points

### Scalability Solutions
- Nyström approximation: subsample m landmark points, approximate n×n matrix as C W+ C^T
- Random Fourier Features (Rahimi & Recht 2007): Bochner's theorem, sample frequencies, explicit finite mapping
- Complexity drops from O(n²) to O(nm) or O(nD)

### Connections to Attention
- Softmax attention = kernel evaluation between Q and K
- Performers: use RFF to approximate softmax kernel
- Associativity trick: φ(Q)(φ(K)^T V) gives O(N) instead of O(N²)
- Kernelized attention is linear attention

## Running Example Idea
- A tiny spam filter / document classifier with 5 features
- Show sparsity (only 2 features matter)
- Show kernel trick (nonlinear boundary)
- Scale up to motivate approximations
