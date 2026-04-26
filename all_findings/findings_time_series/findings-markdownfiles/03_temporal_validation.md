# Temporal Cross-Validation

## Walk-Forward Validation
- Train on past, test on immediate future — mirrors production
- Expanding window: uses all available history
- Sliding window: fixed-size window, drops old data
- Use sliding when old data is no longer relevant

## Purged Cross-Validation (Lopez de Prado)
- For financial data where features have lookback periods
- Purge: remove training samples whose features overlap with test window
- Embargo: gap after test set, don't use N bars after test for training
- Prevents subtle leakage from rolling features

## Key Principle
- At every point in time, ask: "Would I have this information when making this prediction in production?"
