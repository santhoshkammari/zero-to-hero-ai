# Prompt Engineering Core Concepts

## Zero-Shot Prompting
- No examples, instruction only
- Works for tasks heavily seen in pretraining
- Key: specificity, role assignment, format constraints

## Few-Shot Prompting (In-Context Learning)
- Examples activate latent capabilities via induction heads
- Mechanistically: attention heads detect/copy patterns, simulate gradient descent in forward pass
- 3-5 examples sweet spot, diversity > quantity
- Order effects (recency bias) matter

## Chain-of-Thought (CoT)
- Wei et al. 2022, Google
- Force step-by-step reasoning, model shows work
- Reduces shallow pattern matching, enables self-correction
- Zero-shot CoT: "Let's think step by step"
- Few-shot CoT: provide reasoning examples

## Self-Consistency
- Wang et al. 2022
- Sample N diverse CoT paths (temperature > 0)
- Extract final answers, majority vote
- Filters out reasoning errors statistically
- Significant improvement over single CoT

## Tree of Thought (ToT)
- Yao et al. 2023
- Branching reasoning instead of linear
- Explore multiple paths, evaluate, prune, backtrack
- Good for complex/creative tasks (puzzles, planning)
- More compute, higher accuracy

## ReAct (Reasoning + Acting)
- Yao et al. 2022
- Alternates Thought/Action/Observation loops
- Integrates tool use with reasoning
- Foundation of LLM agent architectures

## DSPy
- Stanford, programmatic prompt optimization
- Treats prompts as tunable parameters
- Automated search (Bayesian, evolutionary) over prompt space
- Replaces manual trial-and-error with systematic optimization

## Prompt Injection
- Direct: malicious instructions in input
- Indirect: hidden instructions in external content
- Defenses: input sanitization, prompt segregation, output filtering, sandwich defense
- OWASP LLM Top 10 relevance

## System/User/Assistant Roles
- System: behavioral constraints, persona, persistent instructions
- User: human input
- Assistant: model responses
- System prompt has highest priority in well-designed APIs
