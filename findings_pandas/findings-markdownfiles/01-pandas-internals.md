# Pandas Internals Research

## BlockManager Architecture
- DataFrame uses BlockManager internally to organize data
- Groups columns of same dtype into contiguous NumPy arrays (blocks)
- Accessing `df._data` or `df._mgr` reveals block structure
- Each Block wraps a 2D NumPy array where first axis = rows
- Object dtype columns stored separately, less efficient
- Operations across same-dtype columns are fast (vectorized C-level)
- Cross-dtype operations slower due to multiple blocks

## Copy-on-Write (CoW) - Pandas 3.0
- Default in pandas 3.0+
- `b = a` shares data until write, then copies
- Eliminates SettingWithCopyWarning class of bugs
- Chained assignment now safer and predictable
- Read-only operations improved memory usage
- First write to shared object triggers copy

## Index Alignment - Silent Bug Factory
- Pandas aligns on index by default, NOT position
- Arithmetic on mismatched indices → silent NaN
- Most dangerous in production: results look plausible but wrong
- Always `.reset_index()` when positional logic needed
- Assert `s1.index.equals(s2.index)` before operations

## PyArrow Backend
- `dtype="string[pyarrow]"` for Arrow-backed strings
- 2-5x memory reduction over object dtype
- 2-10x faster string operations
- Zero-copy interchange with Spark, Dask, Polars
- Native parquet/feather I/O without serialization overhead

## Merge Internals
- Hash join: O(N), used for unsorted keys, memory-heavy
- Sort-merge join: O(N log N), used for sorted keys, less memory
- Many-to-many: Cartesian explosion M*N rows per key match
- `validate=` parameter catches unexpected join types at runtime
