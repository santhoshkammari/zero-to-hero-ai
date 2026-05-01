# Rewrite Plan for ch18/s01 - Fairness & Bias Detection

## Running Example: Loan Approval System
A small bank with 3 branches building a loan approval model. Start with 20 applicants, grow from there.

## Concept Ladder (dependency order):
1. What bias even is — the loan approval scenario
2. Sources of bias (historical, representation, measurement, aggregation, label, sampling)
3. Why removing protected attributes doesn't work (proxy variables)
4. Fairness definitions — demographic parity first (simplest)
5. Equalized odds and equal opportunity (motivated by limitations of demographic parity)
6. Calibration and predictive parity
7. Individual and counterfactual fairness
8. The impossibility theorem (the gut punch)
9. REST STOP
10. Detecting bias — tools and code (Fairlearn, AIF360)
11. Disparate impact / four-fifths rule
12. Mitigation: pre/in/post-processing
13. Intersectional fairness (Gender Shades, Buolamwini)
14. Fairness in LLMs
15. Real-world case studies thread throughout

## Recurring Analogies:
1. "Courtroom" analogy — fairness definitions as different judges with different priorities
2. "Scale/balance" analogy — calibrating a kitchen scale that reads differently depending on who's standing on it

## Vulnerability moments:
1. Opening: avoided this topic because it felt more political than technical
2. Impossibility theorem: genuinely unsettling when first encountered
3. Proxy variables: embarrassing realization that removing columns is theater
4. Intersectionality: still developing intuition for how to audit small subgroups
5. LLM fairness: nobody fully knows how to measure this yet

## Rest stop placement:
After impossibility theorem — reader has mental model of what fairness means and why it's hard
