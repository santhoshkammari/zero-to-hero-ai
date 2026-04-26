# ARIMA & Classical Approaches

## ARIMA Components
- AR(p): linear combo of past values. "Yesterday's temperature × 0.8 + day before × 0.1"
- I(d): differencing to achieve stationarity. Model changes, not levels.
- MA(q): linear combo of past forecast errors. "I overshot by 3, so adjust down."
- SARIMA adds seasonal (P,D,Q,m) components
- auto_arima from pmdarima finds parameters automatically

## When ARIMA Beats ML
- Short, clean, univariate series (hundreds of points)
- Linear relationships
- No external features needed
- Interpretability required

## Exponential Smoothing
- Simple: weighted average, recent obs get exponentially more weight
- Holt's: adds trend
- Holt-Winters: adds seasonality
- ETS framework (Error, Trend, Seasonal) generalizes all variants
