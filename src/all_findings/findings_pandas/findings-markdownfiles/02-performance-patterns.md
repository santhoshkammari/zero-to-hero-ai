# Pandas Performance Patterns

## Categorical dtype
- String column with 10 unique values across 1M rows: 90%+ memory savings
- groupby/merge on categoricals significantly faster
- `observed=True` in groupby skips unused categories

## Numeric downcasting
- `pd.to_numeric(col, downcast="integer")` picks int8 over int64
- 87% less memory per column for small-range integers

## apply() is the enemy
- Runs Python function per row/group → GIL, no vectorization
- Replace with vectorized ops: .str accessor, .dt accessor, numpy ops
- itertuples() 5-10x faster than iterrows() when iteration unavoidable

## eval() and query() with numexpr
- numexpr engine: 2-10x faster than Python eval for large numeric data
- Multi-threaded, vectorized chunk processing
- Only works for numeric/boolean operations
- query() more readable than boolean indexing for complex filters

## SettingWithCopyWarning
- Chained indexing creates ambiguous copy/view
- df[mask]['col'] = val may not update original
- Always use .loc for compound selection+assignment
- CoW in pandas 3.0 largely eliminates this class of bugs
