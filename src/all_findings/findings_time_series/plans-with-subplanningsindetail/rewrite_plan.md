# Rewrite Plan for Time Series Forecasting Section

## Running Example
A small coffee shop forecasting daily cup sales. Starts tiny (3 days of data), grows naturally.

## Concept Ladder
1. Why time series is different (temporal dependence breaks i.i.d.)
2. Autocorrelation — the fundamental property
3. Stationarity — why it matters, how to test, how to fix
4. Classical baselines: ARIMA from scratch, exponential smoothing
5. The ML reframe: turning forecasting into supervised learning
6. Feature engineering: lags, rolling stats, calendar, Fourier
7. Walk-forward validation (why random CV is wrong)
8. The tree extrapolation trap
9. REST STOP
10. Prophet — how it actually works inside
11. Deep learning: N-BEATS, TFT
12. Foundation models: the new frontier
13. Production concerns: concept drift, leakage, horizon degradation
14. Full LightGBM pattern

## Recurring Analogies
1. Weather forecasting / looking out the window
2. The coffee shop owner's intuition

## Vulnerability Moments
1. "I avoided time series for years because the notation looked like alphabet soup"
2. "I still get tripped up by which direction to shift"
3. "No one fully agrees on the best way to handle trend with trees"
4. "Foundation models feel like magic — I'm still building intuition for when they fail"
