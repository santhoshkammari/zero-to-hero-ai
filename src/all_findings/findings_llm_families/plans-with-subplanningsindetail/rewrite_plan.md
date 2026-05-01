# Rewrite Plan: LLM Families & Architecture

## Running Example
A small team building "TinyChat" — a chatbot for a local restaurant chain.
Start with picking GPT-1 era simplicity, evolve through needing better/cheaper/faster models.

## Concept Ladder
1. The decoder-only bet (why one architecture won)
2. GPT lineage (scaling story)
3. The open-source revolution (LLaMA moment)
4. LLaMA's architectural toolkit (RoPE, RMSNorm, SwiGLU, GQA)
5. REST STOP
6. Mistral's clever tricks (sliding window, MoE)
7. The broader landscape (Claude, Gemini, DeepSeek, Phi)
8. Architectural decision table (what actually matters)
9. Open vs closed models
10. Model cards and responsible release

## Vulnerability Moments
1. Opening confession about avoiding model zoo
2. "I still mix up which model uses which trick"
3. "No one fully knows why SwiGLU works better"
4. "I oversimplified when I said architecture doesn't matter"
5. "The open vs closed debate has no clean answer"

## Analogies
1. Car engine analogy: Same engine block (decoder-only), different tuning (turbo=MoE, fuel injection=SwiGLU)
2. Restaurant kitchen: Head chef (router) assigns dishes to sous chefs (experts)
3. Telescope/binoculars: sliding window = binoculars (limited view but layers stack)
