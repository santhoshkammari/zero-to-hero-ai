# Seaborn, Plotly, Altair

## Seaborn
- High-level wrapper on matplotlib
- Understands DataFrames natively
- Statistical visualization: auto-computes KDEs, regressions, confidence intervals
- FacetGrid: small multiples by splitting data by categories
- Three key calls: pairplot, heatmap, set_theme
- Returns matplotlib axes — you can always drop down to matplotlib for fine control

## Plotly
- Interactive visualization (zoom, hover, filter)
- Outputs HTML/JSON — lives in browser
- plotly.express: high-level API similar to seaborn
- Dash: full web app framework for dashboards
- Right tool when: non-technical stakeholders need to explore data
- Not needed for personal EDA

## Altair (Vega-Lite)
- Declarative (grammar of graphics) vs matplotlib's imperative
- You describe WHAT you want, not HOW to draw it
- Based on Vega-Lite JSON spec
- Great for reproducibility and concise code
- Less control than matplotlib for custom plots

## When to use what
- Matplotlib: fine-grained control, publications, batch generation
- Seaborn: 80% of EDA, statistical plots, fast exploration
- Plotly: interactive dashboards, stakeholder-facing
- Altair: declarative exploration, reproducible specs
