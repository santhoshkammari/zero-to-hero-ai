# Rewrite Plan: ch17/s05 - Sparse & Kernel Methods

## Structure (Brandon style)

### Phase 1: Opening
- Personal confession about avoiding sparsity/kernels
- Orientation: what these methods are
- Heads-up: math prereqs dismissed
- Journey invitation

### Phase 2: Table of Contents

### Phase 3: Build-Up Sections
1. **Why most features don't matter** - motivate sparsity with tiny example (5 features, 2 matter)
2. **L1 vs L2: The geometry of zero** - diamond vs circle, why L1 gives exact zeros
3. **The LASSO path** - walking lambda from 0 to infinity, watching features drop out
4. **Elastic net** - when LASSO picks one from correlated group, elastic net groups them
5. **Compressed sensing** - fewer measurements than dimensions, L1 recovery, MRI
6. **Sparse coding & dictionary learning** - learn the basis, represent sparsely
7. **REST STOP** - you now understand sparsity half
8. **The kernel trick revisited** - from feature maps to kernel functions
9. **RKHS: why kernels aren't a hack** - functions as vectors, representer theorem
10. **Kernels beyond SVM** - kernel PCA, kernel regression, MKL
11. **The scaling wall** - O(n²) kernel matrix problem
12. **Nyström approximation** - subsample to approximate
13. **Random Fourier features** - explicit finite maps via Bochner's theorem
14. **Attention IS a kernel** - softmax attention, Performers, linear attention
15. **REST STOP 2** - full picture

### Phase 4: Wrap-up
- Gratitude, journey recap, future hope

### Phase 5: Resources

## Running Example
- Building a house price predictor with 50 features
- Most features are noise (sparsity)
- Nonlinear relationships (kernels)
- Scale to citywide data (approximations)

## Vulnerability Moments
1. "I avoided kernel papers for years because RKHS sounded terrifying"
2. "I still find it surprising that L1 gives exact zeros"
3. "I'm not sure anyone has a perfect intuition for why RFF works so well in practice"
4. "I oversimplified when I said kernels can't scale"
5. "The connection between attention and kernels still makes me pause every time"

## Recurring Analogies
1. Sculpture analogy: sparsity is chiseling away marble to find the statue
2. Telescope analogy: kernels let you see in higher dimensions without going there
