# Interpretability & XAI Research Notes

## Key Concepts to Cover
1. **Intrinsic vs Post-hoc**: Decision trees, GAMs = intrinsic. SHAP, LIME = post-hoc. Rudin 2019 argues for intrinsic.
2. **SHAP**: Shapley values from cooperative game theory. φ_i = Σ |S|!(n-|S|-1)!/n! * [v(S∪{i}) - v(S)]. Properties: efficiency, symmetry, dummy, additivity. Variants: TreeSHAP, KernelSHAP, DeepSHAP, GradientSHAP.
3. **LIME**: Perturb → predict → fit local linear model. Fast but unstable (random perturbations).
4. **PDP/ICE**: PDP = average effect of feature. ICE = individual curves. If ICE parallel, PDP tells whole story. If divergent, PDP hides heterogeneity.
5. **Attention ≠ Explanation**: Jain & Wallace 2019, Wiegreffe & Pinter 2019.
6. **Gradient methods**: Integrated Gradients (Sundararajan 2017), Grad-CAM, SmoothGrad.
7. **Counterfactual explanations**: Wachter 2017. "What minimal change would flip the decision?" Closest possible world.
8. **TCAV**: Kim 2018. Concept Activation Vectors. Train linear classifier on concept examples in activation space. TCAV score = % of times gradient aligns with concept direction.
9. **Mechanistic interpretability**: Anthropic 2024. Sparse autoencoders, superposition, circuits, attribution graphs, transcoders.
10. **Fairness**: SHAP for bias detection, disparate impact, proxy features.
11. **Regulatory**: GDPR Article 22, EU AI Act 2024, US SR 11-7.
12. **Limitations**: Rudin 2019 critique, faithfulness problems, method disagreement, Adebayo sanity checks.

## Running Example: Loan approval model
- Concrete, relatable, threads through all sections
- Start with 3 features: income, credit_score, debt_ratio
- Grow as needed

## Analogies
1. **Courtroom analogy**: Model is the defendant, explanation methods are different witnesses testifying about what happened inside the model's "mind"
2. **Map analogy**: Explanations are maps of the model's decision landscape — different maps (SHAP, LIME) show different projections of the same terrain
