# Key Concepts for Causal Inference Section

## Potential Outcomes (Rubin)
- Y_i(1) = outcome if treated, Y_i(0) = outcome if not treated
- Fundamental problem: only observe ONE of these per person
- Individual Treatment Effect: τ_i = Y_i(1) - Y_i(0) — never directly observable
- ATE = E[Y(1) - Y(0)] — population average
- ATT = E[Y(1) - Y(0) | T=1] — effect on those actually treated
- CATE(x) = E[Y(1) - Y(0) | X=x] — effect for subgroup with characteristics x

## Simpson's Paradox
- Berkeley admissions 1973: aggregate showed men admitted more (44% vs 35%)
- But department-level showed slight bias TOWARD women
- Women applied to more competitive departments
- Resolution requires causal reasoning, not just statistics

## Key Estimation Methods
- **Propensity Score Matching**: e(X) = P(T=1|X), match treated/control on this score
- **IPW**: weight by 1/e(X) for treated, 1/(1-e(X)) for control
- **DiD**: compare changes over time between treatment and control groups
  - Parallel trends assumption is critical
- **IV**: find instrument Z that affects treatment but not outcome directly
  - Two-stage least squares
- **RDD**: exploit sharp cutoff in assignment variable
  - Sharp: deterministic at cutoff
  - Fuzzy: probability jumps at cutoff

## Pearl's Framework
- DAGs encode causal assumptions
- Three structures: fork (confounder), chain (mediator), collider
- do-calculus: surgery on graph — cut incoming edges to treated variable
- Backdoor criterion: which variables to control for
- Frontdoor criterion: for when you can't block all backdoor paths

## Modern ML + Causality
- Double ML (Chernozhukov 2018): use ML for nuisance parameters, cross-fitting
- Causal Forests (Wager & Athey 2018): random forests for CATE estimation
- Meta-learners: S-learner, T-learner, X-learner for CATE

## Tech Applications
- Uplift modeling: target users whose behavior CHANGES due to treatment
- Personalization: CATE-based targeting
- Feature rollouts: estimate causal impact without full A/B test
