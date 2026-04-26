# Text Preprocessing Pipeline Key Findings

## Order matters
1. Unicode normalization (NFKC/NFC) FIRST
2. Lowercasing
3. Tokenization
4. Stop word removal (optional)
5. Stemming/Lemmatization (optional)
6. Vectorization

## Unicode gotchas
- é can be single codepoint or e + combining accent — visually identical, string compare fails
- Fullwidth characters (ａ vs a) — common in CJK text
- Ligatures (ﬀ → ff) only under NFKC/NFKD

## Domain-specific cleaning
- Social media: URLs, @mentions, hashtags, emojis, slang
- Medical: abbreviations (q.d., b.i.d.), dosage patterns, HIPAA considerations
- Legal: section references (§), citations, Latin terms

## Key insight
- Over-cleaning strips signal. Under-cleaning adds noise. The right amount depends on task.
