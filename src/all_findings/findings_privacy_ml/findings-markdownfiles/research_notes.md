# Privacy-Preserving ML Research Notes

## Key Topics Covered
1. Privacy Attacks: Membership inference, model inversion, data extraction from LLMs
2. Differential Privacy: ε-δ definition, Gaussian mechanism, composition theorems
3. DP-SGD: Clipping + noise, moments accountant
4. Federated Learning: FedAvg, communication efficiency, non-IID heterogeneity
5. Secure Multi-Party Computation: Secret sharing
6. Homomorphic Encryption for ML
7. Privacy Regulations: GDPR, CCPA
8. Synthetic Data for Privacy
9. Privacy-Utility Tradeoffs

## Running Example Idea
A health startup building a disease prediction model across 3 hospitals.
Each hospital has patient data they can't share. We build from "why can't we just collect all data" to the full privacy stack.

## Key Numbers
- Netflix deanonymization: 500K users, 6-8 ratings enough to identify
- DP-SGD accuracy cost: 2-10% typically
- CIFAR-10 DP at ε=8: ~96% vs ~99% without
- Apple local DP: ε≈2-8
- US Census 2020: ε≈19.6
- FHE overhead: 1,000-1,000,000x slower
- Synthetic data DP-GAN: 5-20% utility loss at ε=2-5

## Concept Ladder (dependency order)
1. Why anonymization fails (Netflix example) → motivation
2. What privacy even means mathematically → ε-δ definition
3. How to add noise properly → Gaussian/Laplace mechanisms
4. How privacy degrades → composition theorems
5. How to train models privately → DP-SGD
6. REST STOP
7. What if data can't leave? → Federated Learning / FedAvg
8. FL isn't automatically private → gradient attacks
9. Securing FL → Secure aggregation, SMPC
10. Computing on encrypted data → Homomorphic encryption
11. Legal requirements → GDPR, CCPA, machine unlearning
12. Generating fake data → Synthetic data
13. The fundamental tradeoff → Privacy vs utility

## Analogies
1. Soundproof rooms: Privacy = building walls between data. DP = making walls thick enough. The thicker the wall (lower ε), the less signal leaks, but also less useful sound gets through.
2. Locked mailbox analogy: FL = each hospital has a locked mailbox. They send model updates out but raw patient records never leave. SMPC = the mailboxes have combination locks where multiple keys needed.
3. Whispering in a crowd: Adding noise to data = whispering your answer in a loud crowd. The crowd noise (Gaussian/Laplace) covers your specific whisper.
