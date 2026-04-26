# Text Generation & Translation Research Summary

## Key Topics Covered

### Autoregressive Generation
- Next-token prediction loop: feed tokens → get distribution → pick token → append → repeat
- Sequential dependency: token N depends on tokens 1..N-1
- KV-cache optimization: store key/value tensors, O(n²) → O(n) per token

### Decoding Strategies (Concept Ladder)
1. **Greedy**: argmax at each step. Fast, deterministic, repetitive, can't backtrack
2. **Temperature**: divide logits by T before softmax. T<1 sharpens, T>1 flattens. T→0 = greedy, T→∞ = uniform
3. **Top-k**: keep k highest prob tokens, zero rest, renormalize. Problem: fixed k regardless of model confidence
4. **Top-p (Nucleus)**: keep smallest set with cumsum >= p. Adapts dynamically to model confidence
5. **Beam search**: maintain b hypotheses. Length normalization (score/len^α). Diversity penalty (group beams)
6. **Repetition penalty**: divide/multiply logits of seen tokens by factor. 1.1-1.3 range. Frequency penalty vs presence penalty

### Machine Translation
- Rule-based (1950s-80s): handcrafted grammar rules, couldn't scale
- Statistical MT: noisy channel model P(e|f) = P(f|e)·P(e), phrase-based SMT, IBM models 1-5
- Neural MT: encoder-decoder (Sutskever 2014), fixed-vector bottleneck
- Attention (Bahdanau 2015): decoder attends to all encoder states, solved bottleneck
- Transformer (Vaswani 2017): replaced RNNs entirely

### Multilingual Models
- mBART: denoising pretraining in 25 languages, encoder-decoder, language tags
- NLLB-200: 200+ languages, sparse MoE, low-resource breakthrough, 44% BLEU improvement
- Zero-shot translation: translate between unseen pairs via shared representation
- Off-target translation: model outputs wrong language

### Evaluation Metrics
- BLEU: modified n-gram precision + brevity penalty, 0-100, surface-level
- METEOR: precision+recall, stems/synonyms/paraphrases, better segment-level
- chrF: character n-gram F-score, good for morphologically rich languages
- COMET: neural learned metric, best correlation with human judgment, needs GPU

### Constrained Generation
- Grammar-based decoding: CFG/PEG restricts tokens at each step
- Libraries: Outlines, Guidance, LMQL, jsonformer
- OpenAI function calling, structured outputs API

### Watermarking
- Kirchenbauer et al. 2023: green/red list tokens
- PRNG splits vocabulary per position, bias toward green tokens
- Detection: statistical overrepresentation of green tokens
- Robust to minor edits, vulnerable to heavy paraphrasing

### Evaluation Challenges (Open-ended)
- Perplexity: doesn't measure quality/coherence/factuality
- MAUVE: distributional similarity metric
- Human evaluation: gold standard but expensive/slow
- No single automatic metric captures everything
- Distinct-n, self-BLEU for diversity

### Speculative Decoding
- Draft model proposes N tokens, target model verifies in batch
- Maintains quality of target model, speeds up 2-3x
