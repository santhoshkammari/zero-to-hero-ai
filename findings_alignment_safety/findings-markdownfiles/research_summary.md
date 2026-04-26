# Alignment & Safety Research Summary

## Key Topics to Cover
1. RLHF - reward model training, PPO loop, KL penalty, Goodhart's law / reward hacking
2. DPO - direct preference optimization, eliminates reward model, Bradley-Terry derivation
3. GRPO - group relative policy optimization (DeepSeek), batch ranking, verifiable rewards
4. Constitutional AI - RLAIF, self-critique, principles-based, Anthropic approach
5. Red teaming - systematic probing, adversarial testing, automated red teaming
6. Jailbreaking & defenses - roleplay attacks, encoding tricks, multi-turn, prompt injection (direct/indirect)
7. Toxicity/bias mitigation - data curation, Safe RLHF, output filtering, Llama Guard
8. Hallucination reduction - RAG grounding, self-consistency, chain-of-verification, claim decomposition
9. Safety benchmarks - TruthfulQA, ToxiGen, RealToxicityPrompts, HHH, AdvBench
10. Responsible AI frameworks - EU AI Act, NIST RMF, Anthropic ASLs
11. Alignment tax - capability cost vs safety benefit tradeoff
12. Scalable oversight - debate, recursive reward modeling, oversight games
13. Production safety stack - input filters, guardrails, output classifiers, monitoring

## Running Example: Content moderation chatbot for a children's education platform
- Start with a base model that produces harmful content
- Progressively align it through SFT, RLHF/DPO
- Show how each safety layer addresses a specific failure mode
- Scale from 3 example prompts to production concerns

## Key Analogies
1. Dog training analogy - reward shaping, the dog learns to fake sitting for treats (reward hacking)
2. Constitution/law analogy - rules that govern behavior even when no human is watching (Constitutional AI)
3. Security guard layers - multiple checkpoints at a concert venue (defense in depth)
