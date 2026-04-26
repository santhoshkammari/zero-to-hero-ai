# Model Development Research Summary

## Key Topics to Cover
1. **Experiment Tracking** - MLflow, W&B, what to log, comparison
2. **Reproducibility** - Seeds, env pinning, Docker, DVC
3. **Hyperparameter Optimization** - Optuna (TPE internals), Ray Tune (ASHA), grid/random/Bayesian
4. **Model Registry** - Versioning, lifecycle stages (None→Staging→Production→Archived), governance
5. **Model Versioning** - Semantic versioning for models, artifact immutability
6. **A/B Testing** - Shadow deployment, canary, statistical significance, peeking problem
7. **Offline Evaluation** - Temporal splits, backtesting, stratified, hold-out
8. **Baseline Models** - Why start simple, heuristic-first, minimum viable model
9. **Model Cards** - Mitchell et al. 2019, documentation structure, responsible AI
10. **Documentation Best Practices** - README for models, decision logs
11. **Model Development Lifecycle** - End to end flow

## Running Example Idea
A churn prediction model for a subscription service. Start with a rule-based heuristic, evolve through tracking, tuning, registry, A/B testing.

## Key Insights from Research
- TPE works by splitting trials into good/bad, fitting Parzen estimators, maximizing l(x)/g(x)
- ASHA starts many trials cheap, halves worst performers asynchronously 
- Model cards: model details, intended use, factors, metrics, ethical considerations
- Shadow deployment → canary → full rollout pipeline
- Reproducibility: even with seeds, CUDA atomicAdd is non-deterministic
