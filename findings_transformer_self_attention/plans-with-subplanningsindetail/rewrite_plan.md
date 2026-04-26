# Rewrite Plan: Self-Attention & the Transformer

## Running Example
Building a tiny translation system: "I love cats" → Spanish
Start with 3 words, grow organically through the section

## Concept Ladder (dependency order)
1. Why attention to self? (motivation from seq2seq limitation)
2. The lookup intuition — what if every word could search the whole sentence?
3. Q, K, V from first principles (build from the lookup metaphor)
4. Scaled dot-product attention (walk through with numbers)
5. Why sqrt(d_k) — derive from variance argument with toy numbers
6. Multi-head attention (one head can only look one direction)
7. Positional encoding (attention is order-blind — disaster!)
8. REST STOP — you now understand the core attention mechanism
9. The Transformer block: residual connections + layer norm + FFN
10. Pre-LN vs Post-LN 
11. FFN: where knowledge lives
12. Encoder-decoder architecture
13. Causal masking for decoders
14. Full architecture wiring
15. Wrap-up

## Vulnerability Moments
1. Opening: avoided transformers for years, felt like gatekeeping
2. sqrt(d_k): "I'll be honest — I glossed over this for months"
3. Multi-head: "I still can't always predict which patterns different heads will learn"
4. RoPE: "I'm still building intuition for why rotation specifically works so well"
5. FFN knowledge storage: "no one is completely certain why factual knowledge concentrates here"

## Recurring Analogies
1. Library/filing cabinet — Q/K/V as search/label/content (evolves through section)
2. Residual stream as a river — each layer adds tributaries, water flows through
3. Orchestra — multi-head as different sections playing simultaneously

## Rest Stop Placement
After multi-head attention + positional encoding — reader has working mental model of the core mechanism
