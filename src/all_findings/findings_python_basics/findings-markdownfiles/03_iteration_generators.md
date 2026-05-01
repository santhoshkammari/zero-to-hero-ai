# Iterators, Generators, and the Iteration Protocol

## Core Protocol
- Iterable: has __iter__() returning an iterator
- Iterator: has __next__() returning next value or raising StopIteration
- for loop calls iter() then next() repeatedly

## Generators
- Functions with yield - lazy evaluation
- Generator objects implement iterator protocol automatically
- Memory efficient: one item at a time vs full list
- Can only iterate once (exhaustion)
- send() enables two-way communication (coroutines)

## ML Pipeline Use
- Streaming large datasets that don't fit in memory
- Batch generators for training loops
- Data augmentation pipelines
- Prefetching and preprocessing chains
