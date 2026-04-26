# Chart Selection & Visualization Principles

## Chart Decision Framework
- Distribution (1 variable): histogram, KDE
- Relationship (2 numeric): scatter plot
- Comparison across categories: bar chart
- Distribution across categories: box plot, violin plot
- Correlation matrix: heatmap
- Time series / trends: line plot
- All pairwise relationships: pair plot
- Part-to-whole: bar chart (NOT pie chart — humans are bad at comparing angles)

## Tufte's Principles
- Data-ink ratio: maximize ink used for actual data
- Chartjunk: remove unnecessary decoration (3D effects, heavy gridlines, ornate fonts)
- Every pixel should convey information

## Common Mistakes
- Truncated Y-axis exaggerates small differences
- Cherry-picked scales hide context
- No baseline comparison makes results meaningless
- Rainbow colormap (jet) distorts data and fails colorblind users
- Dual Y-axes mislead about relationships
- Overplotting hides structure — use transparency, jitter, or aggregation

## Colormap Best Practices
- Use perceptually uniform: viridis, plasma, inferno, magma, cividis
- All are colorblind-safe
- Never use jet/rainbow for quantitative data
- 8% of men have color vision deficiency

## Production Monitoring
- wandb.log(), mlflow.log_figure(), TensorBoard SummaryWriter
- Log training curves, confusion matrices, feature importance automatically
- Manual screenshots don't scale
