# Writing Plan for Prompt Engineering Section

## Running Example
Building an AI-powered customer support bot for a small online bookstore.
- Starts tiny: 3 types of customer messages
- Grows: multi-step reasoning, tool use, structured output
- Returns in every section

## Concept Ladder (dependency order)
1. The raw problem: talking to a model that doesn't know what you want
2. Zero-shot: the first attempt, specificity matters
3. Few-shot: showing examples, in-context learning mechanism
4. Chain-of-thought: making the model think out loud
5. Self-consistency: voting across multiple reasoning paths
6. Tree of thought: branching exploration
7. REST STOP
8. System/user/assistant roles: the control hierarchy
9. Structured output: getting JSON, not prose
10. ReAct: reasoning + acting with tools
11. Prompt injection: the dark side
12. DSPy & prompt optimization: beyond manual tweaking
13. Evaluation: measuring prompt quality

## Vulnerability Moments
1. Opening: avoided prompt engineering as "not real engineering"
2. Few-shot: confused by why example ORDER changed results
3. CoT: "I still don't fully understand WHY making a model talk to itself works"
4. Injection: "the first time someone showed me a prompt injection, I felt embarrassed"
5. Evaluation: "measuring prompt quality is still the hardest part"

## Recurring Analogies
1. Cooking analogy: prompt = recipe, model = kitchen/chef
   - Zero-shot = "make me something Italian"
   - Few-shot = showing photos of dishes you liked
   - CoT = asking chef to explain their plan before cooking
   - Returns when discussing structured output (specifying exact plating)
2. GPS/navigation analogy:
   - Different prompting strategies = different levels of directions
   - Returns in ToT (exploring multiple routes)
   - Returns in ReAct (recalculating when you hit a dead end)

## Rest Stop Placement
After self-consistency/ToT section - reader has solid mental model of
prompting strategies. Can stop here for most use cases.
