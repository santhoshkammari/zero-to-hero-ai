# Tokenization Algorithms Notes

## BPE
- Start with characters, merge most frequent pair, repeat
- Deterministic: same merges every time
- At inference: replay merges in learned order
- GPT-2/3/4, LLaMA, most modern LLMs

## WordPiece
- Like BPE but merge criterion = maximize corpus likelihood
- Similar to pointwise mutual information
- ## prefix for continuation tokens
- BERT, DistilBERT, Electra

## Unigram
- Start large, prune least useful tokens
- Probabilistic: multiple valid segmentations, pick highest probability
- Subword regularization: sample different segmentations during training (data augmentation)
- SentencePiece implements both Unigram and BPE
- T5, ALBERT, XLNet

## Byte-level BPE
- Start with 256 raw bytes instead of Unicode characters
- No UNK tokens ever - any byte sequence representable
- Non-Latin scripts may use 1.3-1.5x more tokens
- GPT-2, GPT-3, GPT-4

## Vocabulary size tradeoffs
- Too small (4k): long sequences, reduced context window
- Too large (500k): huge embedding table, undertrained rare tokens
- Sweet spot: 30k-50k for English, 100k-256k for multilingual
- Trend toward larger vocabs as models grow (relative cost shrinks)
