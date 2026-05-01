# Writing Plan: Seq2Seq & the Birth of Attention

## Running Example
A tiny chatbot that translates cooking instructions from Spanish to English.
- Vocabulary: ~7-10 words
- Example sentence: "Corta las cebollas finamente" → "Chop the onions finely"
- Grows: short 3-word phrases → longer multi-clause recipes

## Recurring Analogies
1. **Telephone game / Whisper chain**: encoder compresses message into one whisper to pass forward. Short messages survive. Long messages get garbled. Attention = letting the decoder peek at written notes.
2. **Reading a recipe while cooking**: you don't memorize the whole recipe page then close the book. You glance back at the relevant line for each step.

## Concept Ladder (dependency order)
1. The translation problem (variable-length in → variable-length out)
2. Encoder-decoder architecture (two RNNs, context vector)
3. The bottleneck (fixed-size vector for any length input)
4. Teacher forcing & exposure bias (training mechanics)
5. Beam search & decoding strategies
6. REST STOP
7. Bahdanau attention (additive, score→softmax→weighted sum)
8. Luong attention (multiplicative, simpler scoring)
9. The QKV abstraction (naming the pattern)
10. Attention as alignment visualization
11. The bridge to self-attention and transformers

## Vulnerability Moments
1. Opening: I avoided attention for ages, kept using word2vec for everything
2. Bottleneck: "I'll be honest — when I first saw BLEU scores tanking on long sentences, I assumed it was a data problem"
3. Teacher forcing: "I still occasionally mix up which direction the scheduled sampling ratio goes"
4. Bahdanau scoring: "The first time I saw the scoring formula, it looked like three random operations stitched together"
5. Bridge to transformers: "I'm still developing my intuition for exactly why removing recurrence was so critical"

## Phase Structure
- Phase 1: Opening (confession, orientation, heads-up, invitation)
- Phase 2: Table of contents
- Phase 3: Build-up sections
- Phase 4: Rest stop after beam search (before attention)
- Phase 5: Wrap-up
- Phase 6: Resources
