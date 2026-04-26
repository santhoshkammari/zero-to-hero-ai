# Rewrite Plan for ch05/s09.html — Nice to Know (Supervised Learning)

## Writing Style
- Brandon Rohrer style: practitioner voice, not teacher
- First person, vulnerable, honest about confusion
- Build from motivation → toy example → concept → limitation
- Running scenario: building a loan application decision system
- Analogies that recur

## Section Structure (rewritten)
1. Opening — personal confession about these "edge" topics
2. GLMs — why linear regression breaks on count data, link functions
3. Survival Analysis — censoring is the key insight, Cox model
4. Quantile Regression — when means lie, pinball loss
5. Bayesian Linear Regression — uncertainty as a feature
6. Probability Calibration — when "80% confident" means nothing
7. Multi-label Classification — sigmoid vs softmax, the real gotcha
8. Ordinal Regression — ordered categories aren't just numbers
9. Online Learning — when data never stops arriving
10. Interview landmines — the gotchas that trip people up
11. What you should now be able to do

## Running Example
- Loan application system: naturally hits GLMs (count of defaults), survival (time to default), 
  quantile (risk intervals), calibration (decision thresholds), multi-label (multiple risk flags),
  ordinal (credit ratings), online (streaming applications)
