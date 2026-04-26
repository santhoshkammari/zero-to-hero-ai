# Plan for Monitoring & Observability Rewrite

## Running Example
- A small e-commerce startup "ShopFlow" with a product recommendation model
- Starts tiny: 3 products, 50 users
- Grows throughout the piece as complexity demands

## Concept Ladder (dependency order)
1. Why ML fails silently (motivation) - the fundamental asymmetry
2. What drift actually is - start with covariate shift via toy example
3. Concept drift - same toy example, different failure
4. Label/prior probability shift - completing the trilogy
5. Measuring drift statistically - PSI from scratch, then KS test, then KL divergence
6. REST STOP
7. From detection to action - alerting strategies
8. Shadow mode and champion-challenger
9. A/B testing for ML (the traps)
10. Retraining triggers
11. The observability stack (logs, metrics, traces for ML)
12. Debugging production models - the playbook
13. Wrap-up

## Vulnerability Moments
1. Opening: "I shipped a model that was wrong for 3 weeks before anyone noticed"
2. After drift types: "I still mix up covariate and concept drift under pressure"
3. After PSI: "The formula looked like gibberish to me the first time"
4. After observability: "I'm still developing intuition for what to log vs what's noise"
5. In debugging: "No one fully knows why some models degrade in specific seasonal patterns"

## Recurring Analogies
1. Weather station analogy - instruments vs thermometer reading
2. Doctor's checkup analogy - vital signs, symptoms, diagnosis
