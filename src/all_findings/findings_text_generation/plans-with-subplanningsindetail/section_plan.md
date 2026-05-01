# Section Plan: Text Generation and Translation

## Running Example
Building a story-writing assistant chatbot. Start with a tiny vocabulary of 5 words and trace through each decoding strategy manually.

## Concept Ladder (each motivated by limitation of previous)
1. The generation loop (autoregressive) - why it's sequential
2. Greedy decoding → limitation: repetitive, can't backtrack
3. Temperature → limitation: still samples from full vocabulary including garbage
4. Top-k → limitation: fixed k doesn't adapt
5. Top-p/nucleus → limitation: still can repeat, and what about multiple hypotheses?
6. Repetition penalties → limitation: sampling is stochastic, what if we need THE best?
7. Beam search → limitation: conservative, good for constrained tasks
8. REST STOP: You now understand all the knobs
9. Machine translation as the original seq2seq — parallel corpora
10. BLEU and its problems → chrF → METEOR → COMET
11. Multilingual models (mBART, NLLB)
12. Constrained generation & structured output
13. Watermarking
14. Evaluation challenges for open-ended generation
15. Wrap-up

## Vulnerability Moments
1. Opening: "I avoided understanding decoding for embarrassingly long"
2. Temperature: "I used to think temperature was some magical creativity dial"
3. Beam search: "I still find beam search counterintuitive"
4. BLEU: "I'll be honest — when I first computed BLEU..."
5. Watermarking: "I'm still developing my intuition for why this is robust"

## Recurring Analogies
1. Restaurant menu analogy: model gives you a menu, decoding strategy is how you order
2. Hiking paths: greedy takes the steepest trail, beam search scouts multiple trails
