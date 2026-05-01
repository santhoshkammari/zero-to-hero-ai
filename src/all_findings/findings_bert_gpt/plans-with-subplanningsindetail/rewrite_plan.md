# Rewrite Plan: BERT & GPT Two Paradigms

## Running Example
A movie review classifier - thread it from start to finish.
"The movie was dark but the ending was bright" - ambiguous word "dark" and "bright" need context.

## Concept Ladder
1. The fork in the road: which tokens see which? (motivation from transformer)
2. BERT: seeing everything at once (fill-in-the-blank intuition)
3. MLM masking strategy (80/10/10 with toy example)
4. NSP and why it failed
5. Input representation: [CLS], [SEP], embeddings
6. Fine-tuning BERT (the head swap)
7. REST STOP
8. GPT: left-to-right generation (writing a story analogy)
9. Next-token prediction objective
10. GPT scaling story (1→2→3→4)
11. In-context learning and few-shot
12. Emergent abilities debate
13. Chinchilla scaling laws
14. REST STOP 2
15. BERT vs GPT paradigm comparison
16. BERT family: RoBERTa, ALBERT, DeBERTa
17. The hybrid workflow
18. Wrap-up

## Analogies (recurring)
1. Fill-in-the-blank test vs writing a story (BERT vs GPT) - used throughout
2. Chef reading whole recipe vs writing recipe one line at a time
3. Detective with full evidence vs detective getting clues one at a time

## Vulnerability Moments
1. Opening: avoided understanding the BERT/GPT split
2. NSP: "I spent a week implementing NSP before learning it was dropped"
3. Emergent abilities: "I'm still developing my intuition for why scale unlocks new behaviors"
4. DeBERTa: "I haven't figured out a great way to visualize disentangled attention"
5. Paradigm choice: "I still occasionally pick the wrong paradigm for a task"
