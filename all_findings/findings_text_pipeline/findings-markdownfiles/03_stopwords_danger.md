# Stopword Removal Dangers

## When it hurts
- Negation: "not" is a stopword but "not good" ≠ "good"
- Phrases: "to be or not to be" → meaningless after removal
- Short texts: in tweets, every word counts
- Modern models: BERT/GPT trained WITH stopwords — removing them degrades performance

## When it helps
- TF-IDF / BoW: reduces noise from high-frequency non-informative words
- Topic modeling: "the" dominates counts without adding topic info
- Search engines: index efficiency

## Practical fix
- Customize stopword lists: remove negations from the list
- Domain-specific stopwords: "court", "plaintiff" in legal corpus
