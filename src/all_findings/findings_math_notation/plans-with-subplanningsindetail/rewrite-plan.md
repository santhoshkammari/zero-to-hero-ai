# Rewrite Plan: Mathematical Notation (ch02/s01)

## Approach: Brandon Rohrer Style
- Personal confession opening about avoiding math notation
- Running example: reading a real ML paper (the attention formula from "Attention Is All You Need")
- Build up from absolute zero — what does each symbol mean?
- Rest stop after basic symbols before diving into advanced notation
- Vulnerability moments throughout

## Concept Ladder (dependency order)
1. Why notation exists (compression) — the "foreign language" feeling
2. The Alphabet: scalars, vectors, matrices — how papers signal what's what
3. Greek Letters — the 10 you'll see 90% of the time
4. Subscripts & Superscripts — the triple overloading problem
5. Decorators: hat, tilde, bar, star — what sits on top of variables
6. Summation (Σ) and Product (Π) — loops in disguise
7. **REST STOP** — you can now read basic formulas
8. Functions, Mappings, argmin/argmax — optimization notation
9. Norms — measuring size with double bars
10. Probability Notation — the p(x|y) family
11. Calculus Notation — ∂, ∇, Jacobian, Hessian
12. Einstein Summation — the modern shorthand
13. Blackboard Bold & Calligraphic — the fancy fonts
14. Putting it all together — reading the attention formula

## Running Example
Start with the self-attention formula: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V
By the end, the reader can decode every symbol in this formula.

## Vulnerability Moments
1. "I skipped every paper with more than two Greek letters for years"
2. "The numerator vs denominator layout debate still trips me up"
3. "I still have to look up whether ξ is 'xi' or 'psi' every single time"
4. "No one tells you that the same symbol means different things in different papers"
5. "I'm still not 100% sure I always read Einstein notation correctly on first pass"

## Analogies
1. Musical notation analogy — musicians read sheet music fluently, we need to read math notation fluently
2. Foreign language analogy — notation is just another language, and immersion is the only way to learn
