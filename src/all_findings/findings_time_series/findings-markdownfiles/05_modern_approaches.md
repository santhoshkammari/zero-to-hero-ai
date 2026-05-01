# Modern & Deep Learning Approaches

## Prophet
- Additive model: y(t) = g(t) + s(t) + h(t) + ε
- g(t): piecewise linear trend with automatic changepoint detection
- s(t): Fourier series for seasonality
- h(t): holiday/event effects
- Fitted via Stan (MAP or MCMC)
- Great for business time series with daily data and strong seasonality
- Struggles with high-frequency, multivariate, or complex datasets

## N-BEATS
- Pure feedforward NN (no RNN/CNN needed)
- Stacked blocks: each block produces backcast (reconstructed input) and forecast
- Residual learning: each block models what previous blocks couldn't explain
- Interpretable variant: explicit trend and seasonality blocks
- Won M4 competition

## Temporal Fusion Transformer (TFT)
- Variable selection networks: learns which features matter
- Handles static covariates, known future inputs, observed past inputs
- Multi-head attention over time steps
- Interpretable: attention weights show which time steps/features matter
- SOTA for complex multivariate forecasting

## Foundation Models (2024)
- TimesFM (Google): zero-shot forecasting, 100B+ training points
- Chronos (Amazon): open-source, handles univariate and multivariate
- Lag-Llama: transformer-based, community-driven
- Trend: plug-and-play forecasting without retraining
