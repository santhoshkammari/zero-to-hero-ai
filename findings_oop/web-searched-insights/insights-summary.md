# Web Search Insights Summary

## Key Takeaways for OOP Section Rewrite

1. **The WHY**: OOP in ML is not about textbook definitions. It's about building systems that multiple engineers can extend without breaking things. Google, Meta, OpenAI all use OOP to enforce contracts across teams.

2. **Real Patterns That Matter**:
   - Template Method (PyTorch __call__ → forward)
   - Strategy (swap optimizers, loss functions, activations at runtime)
   - Observer (hooks for gradient clipping, logging, feature extraction)
   - Registry/Factory (HuggingFace AutoModel, OpenAI resource classes)
   - Composition over inheritance (sklearn Pipeline, LangChain chains)

3. **Production Focus**: Senior engineers care about WHY a pattern exists, not HOW to write a class. The question is: "When you're building an ML system that 10 people will work on, how do you structure it?"

4. **Anti-Patterns to Cover**: God class, deep inheritance, global state — these are what interviewers test for.

5. **Modern Python**: Protocol classes (PEP 544) for structural subtyping, dataclasses for config, ABC for enforcing contracts.
