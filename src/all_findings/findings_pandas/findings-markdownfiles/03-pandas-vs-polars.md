# Pandas vs Polars

## When Polars wins
- Datasets >1GB, especially 10GB+
- Multi-core parallelism (Rust-based, uses all cores)
- Long chains of transformations (lazy evaluation optimizes query plan)
- 1.5-20x faster depending on workload
- Significantly lower memory footprint

## When Pandas wins
- Datasets <1GB where execution time isn't critical
- Deep ecosystem integration (scikit-learn, statsmodels, etc.)
- Specific pandas features not in Polars (advanced time series, custom index)
- Team familiarity and existing codebases
- Battle-tested stability in production

## Lazy Evaluation (Polars)
- Constructs query plan, optimizes before execution
- Eliminates intermediate memory allocations
- Fuses operations for efficiency
- Pandas is eager: each step executes immediately, stores intermediates

## Practical advice
- Prototype in Pandas
- Migrate to Polars when hitting performance/memory limits
- Syntax is similar enough for easy migration
