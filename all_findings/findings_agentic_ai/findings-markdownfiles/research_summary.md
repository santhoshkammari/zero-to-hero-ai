# Agentic AI Research Summary

## Key Concepts
1. **Agent = LLM + Tools + Loop** - The perceive-reason-act cycle
2. **Function Calling** - LLM outputs structured JSON to invoke tools; pioneered by OpenAI, adopted by Anthropic/Google
3. **ReAct Pattern** (Yao et al. 2023) - Interleaved Thought-Action-Observation traces
4. **Planning**: ReAct (step-at-a-time), Plan-and-Execute (upfront plan), Reflexion (self-correcting with verbal reinforcement)
5. **Memory**: Short-term (context window), Working (scratchpad), Long-term (vector DB), Episodic (timestamped events)
6. **Multi-Agent**: Supervisor/hierarchy, debate, assembly line, role specialization
7. **Frameworks**: LangGraph (graph-based state machine), CrewAI (role-based crews), AutoGen (multi-agent conversations)
8. **Code Agents**: SWE-agent (Princeton), Devin (Cognition), Codex/Copilot - plan/code/test/iterate loop
9. **Reflexion** (Shinn 2023) - verbal reinforcement learning, self-reflection after failures
10. **Safety**: Sandboxing, human-in-the-loop, token budgets, trace logging
11. **Benchmarks**: SWE-bench Verified (~80% top), GAIA (~92% top with multi-model), SWE-bench Pro (~23%)
12. **Compounding errors**: 95% per-step reliability → 77% after 5 steps → reliability is THE production problem

## Running Example Idea
Build a "vacation planning agent" - starts tiny (one tool: weather lookup), grows to multi-tool (flights, hotels, weather), then multi-agent (researcher, booker, budget-checker). Relatable, scales naturally.
