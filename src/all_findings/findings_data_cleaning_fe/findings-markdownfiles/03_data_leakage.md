# Data Leakage Findings

## Three Types of Leakage

### 1. Target Leakage
- Feature uses information not available at prediction time
- Often derived from target variable directly/indirectly
- Example: using "future sales" to predict "current sales"

### 2. Train-Test Contamination
- Test set info leaks into training
- Scaling/normalizing on full dataset before splitting
- Feature encoding using entire dataset before split
- THE most common leakage in practice

### 3. Temporal Leakage
- Model accesses future data during training
- Shuffling time-series before split mixes temporal info
- Rolling statistics that peek into future values

## Prevention Checklist
1. Split data FIRST, then apply all preprocessing
2. Fit transformers on training data ONLY, transform both
3. For time series: ALWAYS split chronologically
4. Review each feature's origin—no label info should bleed in
5. Use sklearn Pipeline to encapsulate preprocessing

## The Sneaky One
- Target encoding without CV folds = leakage
- Aggregation features computed on full dataset = leakage
- Even imputation on full dataset before split = leakage
