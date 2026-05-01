# Survival Analysis Findings

## Core Concept
- Models **time-to-event** data with **censored observations** (event hasn't happened yet)
- Right-censoring most common: customer hasn't churned yet, patient still alive at study end
- Kaplan-Meier curves: non-parametric survival probability estimates
- Cox Proportional Hazards: semi-parametric, models hazard rate h(t|X) = h0(t) * exp(βX)
  - No assumption about baseline hazard shape (huge advantage)
  - Coefficients interpretable as hazard ratios

## ML Extensions
- Random Survival Forests, DeepSurv, XGBoost with Cox loss
- lifelines library in Python for classical approaches

## Key Applications
- Healthcare: patient survival, disease recurrence
- SaaS: churn prediction with subscription start dates
- Manufacturing: equipment failure / predictive maintenance
- Finance: time to loan default

## Interview Gotcha
- You can't just drop censored observations or treat them as "no event" — both approaches introduce bias
- Censoring is informative vs non-informative: if people drop out because they're sicker, that's informative censoring and violates assumptions
