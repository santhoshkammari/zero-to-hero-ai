# Stationarity & Time Series Foundations

## Key Insights
- Stationarity = statistical properties (mean, variance, autocorrelation) don't change over time
- Most classical models (ARIMA, exponential smoothing) REQUIRE stationarity
- Two complementary tests: ADF (null=non-stationary) and KPSS (null=stationary)
- Use both together: if ADF rejects but KPSS doesn't → strong evidence of stationarity
- Differencing: y'(t) = y(t) - y(t-1) to remove trend
- Log transform first if variance grows with level
- Unit root = shocks have permanent effect (random walk)

## Why It Matters
- Non-stationary data produces spurious correlations
- A model trained on non-stationary data learns relationships that don't hold
- Even ML models benefit from stationary inputs (more stable feature distributions)
