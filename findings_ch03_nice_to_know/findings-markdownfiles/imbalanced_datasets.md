# Imbalanced Datasets

## SMOTE vs Class Weights
- **Class weights**: preferred first approach in production — simple config, no data modification, lower overfitting risk
- **SMOTE**: creates synthetic minority samples by interpolation — risk of overfitting, synthetic points may not be realistic
- SMOTE must ONLY be applied to training data, NEVER validation/test
- Extreme class weights can cause training instability

## Key Insight
- Production teams almost always start with class weights because it's a model parameter, not a data transformation
- SMOTE adds pipeline complexity and can introduce artifacts
- Evaluation must use precision/recall/F1/AUC-ROC, never accuracy alone
- Regular retraining needed because imbalanced problems are usually non-stationary
