# SciPy Research Findings

## Origin Story
- Created early 2000s because Python lacked robust scientific computing tools
- Wraps battle-tested FORTRAN libraries: BLAS, LAPACK, ARPACK via F2PY
- Built on top of NumPy - NumPy gives arrays, SciPy gives algorithms
- Key insight: decades of FORTRAN numerical code, now accessible through Python

## Core Modules & Production Relevance

### scipy.optimize
- BFGS: quasi-Newton, approximates Hessian inverse (dense n×n matrix)
- L-BFGS-B: limited-memory BFGS, keeps only m past vectors (3-20), handles bounds
- Used in sklearn's LogisticRegression (solver='lbfgs')
- curve_fit: Platt scaling for probability calibration
- Key interview: local vs global optimization, convergence debugging, when NOT to use (use SGD/Adam for neural nets)

### scipy.sparse
- CSR: compressed sparse row - fast row slicing, matrix-vector products (ML standard)
- CSC: compressed sparse column - fast column slicing
- COO: coordinate list - construction format, convert to CSR/CSC for math
- Memory: stores 3 arrays (data, indices, indptr) vs full dense matrix
- Production: TF-IDF matrices, graph adjacency, recommendation user-item matrices
- Interview: format trade-offs, when to convert, integration with sklearn

### scipy.sparse.linalg
- svds: truncated SVD via ARPACK - top k singular values only
- Used for LSA (latent semantic analysis) and recommendation systems
- eigsh: sparse eigenvalue decomposition
- Key: only compute what you need from massive matrices

### scipy.stats
- Production: A/B testing (ttest_ind, mannwhitneyu)
- Data drift detection: ks_2samp (Kolmogorov-Smirnov) comparing training vs live distributions
- gaussian_kde: kernel density estimation
- Interview: p-value interpretation, effect size vs significance

### scipy.spatial
- KDTree: works well up to ~20 dimensions, degrades after
- BallTree: slightly better, up to ~40 dimensions
- Curse of dimensionality: high-dim makes tree structures useless
- Production: use FAISS/Annoy for >40 dims (BERT embeddings = 768 dims)

### scipy.signal
- FFT convolution: convolution theorem - multiply in frequency domain
- fftconvolve: orders of magnitude faster for long signals
- Audio ML: STFT, mel spectrograms, filtering
- Production: real-time audio processing, sensor data

### scipy.interpolate
- Spline interpolation for short gaps in time series
- Good for smooth signals (sensors, medical devices)
- Bad for large gaps or noisy data
- Production: preprocessing for models needing regular spacing

### scipy.integrate
- quad: adaptive quadrature for probability density integration
- Used for custom loss functions, anomaly detection scoring
- Computing probabilities from KDE estimates

## Key Interview Themes
1. When to use SciPy vs PyTorch/specialized tools
2. Sparse matrix format trade-offs
3. Optimization algorithm selection
4. Statistical testing interpretation
5. Curse of dimensionality in spatial search
6. Understanding that SciPy wraps FORTRAN (LAPACK, BLAS, ARPACK)
