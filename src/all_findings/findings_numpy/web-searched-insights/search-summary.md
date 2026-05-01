# Web Search Insights Summary

## Key Insights Gathered

### 1. Strides are the secret sauce
- Strides enable views, broadcasting, transpose - all without copying data
- as_strided can create sliding windows, but dangerous (use sliding_window_view)
- Broadcasting works by setting stride=0 for stretched dimensions

### 2. The PyArrayObject C struct
- data pointer, nd, dimensions, strides, base, descr, flags
- This thin metadata layer over raw memory is what makes NumPy powerful
- "base" attribute links views back to original data owner

### 3. BLAS/LAPACK are the real speed
- np.dot, np.matmul, np.linalg.* all delegate to BLAS/LAPACK
- OpenBLAS/MKL use hand-tuned assembly, multi-threading, cache blocking
- This is why matrix multiply is so much faster than element-wise in loops

### 4. einsum for ML
- 'bid,bjd->bij' for attention scores
- 'bij,bjk->bik' for weighted sum (attention output)  
- Can express any tensor contraction compactly

### 5. Modern RNG
- default_rng(seed) is local, uses PCG64, no global state pollution
- Legacy np.random.seed() is global and fragile
- Always pass rng objects for reproducibility in ML

### 6. Interview depth topics
- Memory layout C vs F order and cache implications
- When reshape copies vs views (non-contiguous requires copy)
- Pairwise distance: naive broadcasting O(n²d) memory vs algebraic trick
- UFuncs and how they enable vectorization
