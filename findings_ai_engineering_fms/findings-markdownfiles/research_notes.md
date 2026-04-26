# AI Engineering with Foundation Models - Research Notes

## Key Concepts to Cover

### 1. The Paradigm Shift: Training → Integration
- Old world: collect data → clean → train → deploy. Each project starts from scratch.
- New world: start with a model that already understands. Your job is integration, not creation.
- The "AI engineer" role is distinct from "ML engineer" — less PyTorch, more API design + system design.

### 2. API-First Development
- 90%+ of LLM apps are API calls. OpenAI, Anthropic, Google expose frontier models via REST.
- The simplicity is the point — idea to prototype in an afternoon.
- But production needs: retry logic, fallbacks, timeouts, rate limit handling.

### 3. LLM Application Architecture Patterns
- Single LLM call (simplest)
- Chain/pipeline (output of one feeds into next)
- RAG (retrieve → augment → generate)
- Tool-use / function calling
- Agent loops (model decides what to do)
- Multi-agent systems
- Compound AI systems (Zaharia et al., BAIR 2024)

### 4. Prompt Management
- Prompts in production are code, not experiments.
- Version control, testing, monitoring, rollback.
- Regression suites for prompt changes.

### 5. Evaluation-Driven Development
- Hardest part of AI engineering — free-form text outputs.
- Three approaches: human eval, LLM-as-judge, automated benchmarks.
- Golden datasets, CI integration, production monitoring signals.

### 6. LLM Caching
- Exact-match cache (hash the prompt)
- Provider-level prompt prefix caching (Anthropic, OpenAI cache KV state)
- Semantic cache (embed queries, cosine similarity threshold)

### 7. Gateway/Router Patterns
- Single entry point for all LLM consumers
- Provider abstraction layer (adapter pattern)
- Routing: cost-based, capability-based, latency-based, failover
- Circuit breakers, health checks

### 8. Fine-Tuning vs Prompting Decision Framework
- Always start with prompting
- Add RAG when knowledge is needed
- Fine-tune when prompting hits quality ceiling or need specific style/format
- They're not mutually exclusive — layer all three

### 9. Compound AI Systems
- Zaharia et al. (BAIR, Feb 2024): "a system that tackles AI tasks using multiple interacting components"
- Components: LLMs + retrievers + tools/APIs + smaller specialized models + orchestration logic + verification
- >60% of LLM workflows use RAG, 30% use multi-step chains
- The question shifts from "which model?" to "how do I compose?"

### 10. LLMOps vs MLOps
- MLOps: data → train → deploy → monitor → retrain cycle
- LLMOps: prompt engineering → evaluation → deploy → monitor → prompt iteration
- Key differences: no training loop (usually), prompt versioning replaces model versioning, eval is harder (free-form text), cost scales per-token not per-GPU

## Running Example Idea
- Building an internal knowledge assistant for a company ("AskAcme")
- Starts as a single API call, evolves through each pattern
- Very relatable — everyone has built or wants to build this
