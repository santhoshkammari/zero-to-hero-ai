# Writing Plan for Ch10 Nice to Know

## Running Example
A small "document summarizer" that processes paragraphs of text. Start with a 5-word vocabulary.
This threads through: context windows (Transformer-XL), permutation training (XLNet), 
efficient attention (Reformer), external memory (NTM), routing to experts (MoE), 
and streaming inference (RWKV/RetNet).

## Concept Ladder (dependency order)
1. The Context Window Problem → Transformer-XL
2. The Masking Problem → XLNet
3. The Quadratic Cost Problem → Reformer & LSH
4. Rest Stop
5. The Memory Problem → Neural Turing Machines & DNC
6. The Differentiability Insight → Differentiable Programming
7. The Efficiency Problem → Mixture of Experts (Switch, GShard)
8. The Speed Problem → RetNet & RWKV
9. Wrap-up

## Vulnerability Moments
1. Opening: Confession about feeling lost in the zoo of transformer variants
2. XLNet: Admitting permutation LM took multiple reads to click
3. NTM: "I still find the addressing mechanism hard to visualize"
4. MoE: "No one fully understands why sparse routing works as well as it does"
5. RWKV: "I'm still developing intuition for when these alternatives beat transformers"

## Recurring Analogies
1. Library analogy: librarian searching shelves (attention), card catalog (memory), 
   specialist librarians (MoE)
2. Conveyor belt: tokens moving through processing, with different speeds/windows
