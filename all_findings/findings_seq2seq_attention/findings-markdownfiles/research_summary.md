# Seq2Seq & Attention Research Summary

## Key Historical Facts
- Sutskever et al. (2014): Original seq2seq with encoder-decoder LSTMs
  - Trick: reversing input sequence reduced effective dependency distance
- Cho et al. (2014): Similar encoder-decoder approach with GRU
- Bahdanau et al. (2015): Additive attention - "Neural Machine Translation by Jointly Learning to Align and Translate"
  - Bidirectional encoder, small feedforward network for scoring
  - Computes attention BEFORE decoder RNN step (uses s_{t-1})
- Luong et al. (2015): Multiplicative attention - "Effective Approaches to Attention-based Neural Machine Translation"
  - Three variants: dot, general, concat
  - Computes attention AFTER decoder RNN step (uses s_t)
  - Dot product = no extra parameters, fast
- Vaswani et al. (2017): "Attention Is All You Need" - self-attention, Transformer

## Key Concepts
1. Information bottleneck: fixed-size context vector can't represent variable-length sequences
2. BLEU scores collapsed beyond ~20 tokens with vanilla seq2seq
3. Attention = score, softmax, weighted sum (QKV pattern)
4. Teacher forcing: use ground truth as decoder input during training
5. Exposure bias: train/inference mismatch from teacher forcing
6. Scheduled sampling: gradually shift from teacher forcing to own predictions
7. Beam search: keep top-k hypotheses at each step, prune back
8. Scaled dot product: divide by sqrt(d_k) to prevent softmax saturation
9. Attention weights form interpretable alignment matrices
