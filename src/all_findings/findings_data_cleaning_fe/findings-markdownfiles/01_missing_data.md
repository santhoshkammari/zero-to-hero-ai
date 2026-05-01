# Missing Data Findings

## Key Insights

### The Three Missingness Mechanisms (Rubin's Framework)
- **MCAR**: Pure randomness. Sensor glitch, page failed to load. Safe to drop—you lose power but no bias.
- **MAR**: Missingness depends on OTHER observed variables. Young people skip income question. Must condition imputation on those variables.
- **MNAR**: The dangerous one. The value itself determines missingness (high earners refuse to report). No statistical trick fully fixes this.

### Diagnostic Steps
- Visualize missingness patterns (heatmaps, bar plots)
- Little's MCAR test for statistical validation
- Domain knowledge is often the ONLY way to distinguish MAR from MNAR

### MICE (Multiple Imputation by Chained Equations) - How It Actually Works
1. Fill all missing values with simple guesses (mean/median)
2. For each column with missing values: treat it as target, use all other columns as predictors, fit a regression, predict the missing values
3. Cycle through all columns = one iteration
4. Repeat 5-10 iterations until convergence
5. Do the whole thing multiple times with different random seeds to capture uncertainty

### When MICE is overkill
- Few missing values (<5% of data)
- Single variable with missingness
- Quick EDA (computational cost not justified)

### Production Considerations
- Imputation logic MUST be identical in training and inference
- Wrap imputation in pipeline (sklearn.Pipeline)
- Monitor for data drift - missingness patterns change in production
- Document assumptions about missingness mechanism
