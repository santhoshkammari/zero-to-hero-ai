# ML Security Research Summary

## Key Topics Covered
1. Adversarial attacks: FGSM (one-step gradient), PGD (iterative), C&W (optimization-based minimum perturbation)
2. Adversarial training: Madry et al. min-max formulation, accuracy-robustness tradeoff
3. Certified robustness: Randomized smoothing, certified radii, 2024 advances (ARS, PPRS, DRF)
4. Data poisoning: Label flipping, backdoor/trojan attacks, clean-label attacks, dynamic triggers
5. Model stealing: Query-based extraction, knowledge distillation from API outputs
6. Prompt injection: Direct (user input), indirect (external content), defense layers
7. Supply chain: Pickle deserialization RCE, safetensors format, model hub poisoning
8. Watermarking: White-box (weights), black-box (trigger inputs), adversarial watermarking
9. Red teaming: Attack surface mapping, diverse team, continuous iteration
10. MITRE ATLAS: Threat modeling framework for ML, analogous to ATT&CK
11. Defense-in-depth: Layered approach across data, training, deployment, inference

## Running Example Idea
A spam classifier for an email service - starts simple, gets attacked in various ways throughout.
This is relatable, concrete, and allows us to demonstrate every attack type naturally.
