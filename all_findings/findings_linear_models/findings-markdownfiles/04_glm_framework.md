# Generalized Linear Models — The Unified View

## Three Components
1. Random component: response distribution from exponential family
2. Systematic component: linear predictor η = Xβ
3. Link function: g(E[y]) = η, connecting mean to linear predictor

## How Linear and Logistic Regression Unify
| Model | Distribution | Link | Mean |
|-------|-------------|------|------|
| Linear regression | Normal | Identity: g(μ) = μ | μ = Xβ |
| Logistic regression | Binomial | Logit: g(μ) = log(μ/(1-μ)) | μ = sigmoid(Xβ) |
| Poisson regression | Poisson | Log: g(μ) = log(μ) | μ = exp(Xβ) |

## Why This Matters
- Linear regression and logistic regression aren't separate models — they're the same framework with different distribution assumptions
- Understanding GLMs means you can handle count data (Poisson), duration data (Gamma), any exponential family
- The "canonical link" is the natural parameterization of the exponential family — it gives the nicest math
