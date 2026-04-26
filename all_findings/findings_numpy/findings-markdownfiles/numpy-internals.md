# NumPy Internals Research

## ndarray Structure
- An ndarray is a thin Python object wrapping: data pointer, shape tuple, strides tuple, dtype, flags
- The C struct (PyArrayObject) contains: char *data, int nd, npy_intp *dimensions, npy_intp *strides, PyObject *base, PyArray_Descr *descr, int flags
- The "base" pointer is what enables views - it points to the original array's data

## Memory Layout
- C-order (row-major): last axis contiguous in memory. Default.
- F-order (column-major): first axis contiguous. Used by Fortran/MATLAB.
- Strides = bytes to jump per axis. For (3,4) float64 C-order: strides=(32, 8)
- address = base + i0*stride0 + i1*stride1 + ...

## Why NumPy is Fast
1. Compiled C code - avoids Python interpreter overhead per element
2. Contiguous memory - cache-friendly access patterns
3. BLAS/LAPACK - highly optimized linear algebra (OpenBLAS, MKL, ATLAS)
4. SIMD vectorization - process multiple elements per CPU instruction
5. Type homogeneity - no per-element type checking
6. UFuncs - universal functions that operate elementwise in C

## Broadcasting Internals
- Broadcasting manipulates strides/shape metadata, NOT data
- A stride of 0 means "repeat this element" - that's the trick
- np.broadcast_to() creates read-only view with zero strides

## Views vs Copies
- Views: basic slicing, reshape (usually), transpose, ravel (sometimes)
- Copies: fancy indexing, boolean masking, .copy(), astype(), np.concatenate
- np.shares_memory(a, b) or np.may_share_memory(a, b) to check

## Performance Gotchas
- np.append/concatenate in loop = O(n²) - preallocate or use lists
- float64 default wastes memory for ML (use float32)
- Non-contiguous arrays slower for BLAS operations
- In-place ops (+=) save memory vs creating new arrays (a = a + b)
