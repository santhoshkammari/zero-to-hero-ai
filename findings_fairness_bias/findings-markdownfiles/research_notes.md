# Fairness & Bias Detection - Research Notes

## Key Case Studies
1. **COMPAS** - ProPublica 2016: Black defendants 2x likely to be falsely labeled high risk. Northpointe said calibrated. Both right — impossibility theorem.
2. **Amazon Hiring** - 2014-2017: Trained on 10 years of male-dominated resumes. Penalized "women's" in resumes. Scrapped in 2017.
3. **Healthcare Algorithm (Obermeyer 2019)**: Used cost as proxy for health need. Black patients have lower costs due to structural barriers. Only 17.7% Black patients selected vs 46.5% who should have qualified.
4. **Gender Shades (Buolamwini & Gebru 2018)**: Facial recognition error rates: light-skinned men 0-0.8%, dark-skinned women 20.8-34.7%. Up to 44x disparity.

## Impossibility Theorem
- Chouldechova 2017, Kleinberg et al. 2016
- When base rates differ between groups, CANNOT simultaneously have: calibration + equal FPR + equal FNR
- Proof: via Bayes' rule — if TPR and FPR equal across groups, but base rates differ, PPV must differ

## Fairness in LLMs
- BBQ Benchmark (Parrish et al. 2022): 58K+ questions across 9 social categories
- Ambiguous vs disambiguated contexts
- Bias score measures stereotype reliance
- Red teaming, prompt-based evaluation

## Mitigation
- Pre-processing: Reweighing (adjust sample weights)
- In-processing: Adversarial debiasing, constrained optimization (ExponentiatedGradient)
- Post-processing: Threshold optimizer (different thresholds per group)
