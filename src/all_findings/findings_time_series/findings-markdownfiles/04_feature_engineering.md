# Feature Engineering for Time Series

## Lag Features
- Most fundamental: y(t-1), y(t-2), ... y(t-k)
- Use ACF/PACF plots to determine significant lags
- Include domain-appropriate lags (7 for weekly, 365 for yearly)

## Rolling Statistics
- Rolling mean, std, min, max over backward-looking windows
- CRITICAL: always .shift(1) to avoid including current value
- Multiple window sizes capture different temporal scales

## Calendar Features
- Day of week, month, quarter, is_weekend, is_holiday
- Cyclical encoding with sin/cos for continuous features

## Fourier Features
- sin(2πkt/P) and cos(2πkt/P) for period P
- K harmonics control complexity
- Places December next to January in feature space (unlike raw month integers)
- Prophet uses this internally for seasonality

## Trend Handling
- Trees CANNOT extrapolate (piecewise constant regressors)
- Solutions: detrend first, predict differences, or hybrid model (linear for trend + trees for residuals)
