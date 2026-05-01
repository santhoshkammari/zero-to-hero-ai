# Rewrite Plan for ch01/s07.html (Pandas)

## Writing Style: Brandon Rohrer
- Personal confession opening (avoided Pandas depth)
- Running example: building a small employee analytics dashboard
- Build-up from absolute zero: what IS a DataFrame under the hood
- Toy examples with 3-5 rows, walk through step by step
- Vulnerability moments throughout
- Rest stop after core patterns
- No bullet-point explanations, all narrative
- Every concept motivated by frustration/limitation of previous

## Concept Ladder (dependency order)
1. What Pandas actually is (the BlockManager, why it exists)
2. The DataFrame as a labeled 2D NumPy array (tiny example)
3. Selection: loc vs iloc (the index trap)
4. Index alignment: the silent bug factory
5. Method chaining: the readable pipeline
6. GroupBy: split-apply-combine from scratch
7. transform vs agg: the KEY distinction
8. Merge: hash joins, sort-merge, and the row explosion
9. REST STOP
10. Memory: dtype optimization, categoricals, Arrow backend
11. Performance: why apply() is slow, vectorization
12. Copy-on-Write: the future of Pandas
13. When Pandas isn't enough: Polars and the lazy evaluation model
14. Wrap-up

## Running Example
- Small company: 5 employees, 3 departments
- Grows naturally to illustrate each concept
- Referenced in wrap-up

## Vulnerability Moments
1. "I used Pandas for two years before understanding what a BlockManager was"
2. "Index alignment cost me an entire day of debugging once"
3. "I still reach for apply() as my first instinct, then catch myself"
4. "Nobody fully understands when Pandas returns a view vs a copy"

## Recurring Analogies
1. Filing cabinet (BlockManager groups same-type documents together)
2. Assembly line (method chaining as manufacturing steps)
