# Writing Plan - AI Engineering with Foundation Models

## Running Example
"AskAcme" — an internal knowledge assistant for a fictional company. 
- Starts: single API call answering employee questions
- Grows: adds retrieval, caching, routing, evaluation, guardrails
- Threads through every section

## Recurring Analogies
1. **Restaurant kitchen analogy** — the chef (LLM) vs the restaurant manager (AI engineer). You don't train the chef, you design the menu, manage the kitchen flow, handle complaints.
2. **Plumbing analogy** — pipes, valves, pressure regulators. The LLM is the water supply; you're the plumber connecting it to every faucet in the building.

## Section Structure
1. Opening (personal confession, orientation, heads-up, journey invitation)
2. Table of Contents
3. The shift — from training to integration (motivate with the old pain)
4. The first API call (toy example — AskAcme v0)
5. When one call isn't enough — architecture patterns
6. Prompt management as software engineering
7. REST STOP
8. The evaluation problem
9. Caching — because every token costs money
10. The gateway and router
11. Fine-tune vs prompt vs RAG decision framework
12. Compound AI systems
13. LLMOps vs MLOps
14. Wrap-up
15. Resources

## Vulnerability Moments
1. Opening: "I avoided this topic because I thought it was beneath me"
2. Architecture patterns: "I built my first LLM app as one giant prompt. It was embarrassing."
3. Evaluation: "I'm still not confident we've solved LLM evaluation. Nobody is."
4. Fine-tuning decision: "I've watched teams burn months fine-tuning when a better prompt would have worked."
5. Compound systems: "The term 'compound AI system' made me roll my eyes at first."
