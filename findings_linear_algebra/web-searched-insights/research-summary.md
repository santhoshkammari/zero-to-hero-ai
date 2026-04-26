# Web Research Summary

## Search 1: Eigenvalues in PCA
- Eigenvectors of covariance matrix = principal directions of data spread
- Eigenvalues = amount of variance captured per direction
- Ellipse analogy: eigenvectors are axes, sqrt(eigenvalue) = axis length
- Real symmetric matrices always have real eigenvalues and orthogonal eigenvectors

## Search 2: SVD in Recommender Systems
- User-item ratings matrix factorized into U Σ Vᵀ
- Latent factors emerge mathematically (not labeled)
- Truncated SVD for denoising and compression
- Simon Funk's blog post popularized this for Netflix Prize
- FunkSVD and ALS for large-scale systems

## Search 3: Matrix Decomposition Comparison
- LU: square matrices, linear solves
- QR: least squares, more stable than normal equation
- Cholesky: symmetric positive definite, 2x faster than LU
- SVD: any matrix, most robust, PCA/compression
- Eigendecomposition: square (often symmetric), PCA theory

## Search 4: Geometric Intuition
- Matrices transform space: stretch, rotate, project, reflect, shear
- Neural net layers = matrix transformations
- PCA = finding the rotation that diagonalizes covariance
- Linear regression = projection onto column space

## Search 5: Interview Depth Questions
- Why can't symmetric matrices have complex eigenvalues?
- How outliers affect PCA
- SVD vs eigendecomposition differences
- Condition number diagnosis and remediation
- Rank deficiency implications for model expressivity

## Search 6: Deep Learning Connections
- Weight matrices determine connectivity and expressiveness
- Gradient flow via backprop = chain of Jacobian multiplications
- Singular values of weights control vanishing/exploding gradients
- Orthogonal initialization preserves gradient flow

## Search 7: Netflix Prize Story
- 2006 $1M challenge
- Simon Funk's SVD approach became legendary
- Latent factors = hidden taste dimensions
- Prediction = dot product of user and item factor vectors

## Search 8: Word Embeddings & Cosine Similarity
- Word2Vec: similar contexts → similar vector directions
- king - man + woman ≈ queen works because relationships create consistent offsets
- Cosine similarity normalizes out magnitude, measures directional agreement

## Search 9: Condition Number & NaN Prevention
- High condition number = numerical instability
- Feature scaling reduces condition number
- Normal equation squares κ → QR/SVD preferred
- Batch normalization also helps conditioning
