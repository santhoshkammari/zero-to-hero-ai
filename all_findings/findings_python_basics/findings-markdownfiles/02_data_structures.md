# Data Structures Internals

## dict
- Hash table with open addressing
- Keys must be hashable (immutable)
- O(1) average lookup/insert/delete
- Preserves insertion order since 3.7 (compact dict)
- Raymond Hettinger's key insight: separate indices array from entries array

## list vs tuple
- Both are contiguous arrays of pointers
- Tuple: immutable, less memory, slightly faster creation
- List: over-allocates for amortized O(1) append
- Tuple can be dict key, list cannot

## set
- Hash table like dict but keys only
- O(1) membership test vs O(n) for list
- frozenset is immutable/hashable variant

## Why this matters for ML
- dict for config, hyperparams, feature mappings
- set for deduplication, vocabulary building
- list for ordered sequences, batches
- tuple for immutable records, function returns
