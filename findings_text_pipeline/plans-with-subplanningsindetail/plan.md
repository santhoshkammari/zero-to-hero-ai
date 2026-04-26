# Rewrite Plan for ch11/s01.html

## Running Example
A spam filter for a small email inbox — 5 emails. Grows throughout.
Relatable, concrete, threads from start to finish.

## Concept Ladder
1. Why text is hard for computers (the bedrock)
2. Text normalization (lowercasing, unicode, stripping)
3. Tokenization (whitespace → regex → spaCy)
4. Stop words (when to remove, when to keep)
5. Stemming vs Lemmatization
6. REST STOP — you now have clean tokens
7. Bag of Words — counting
8. TF-IDF — the math and the why
9. N-grams — partial fix for word order
10. Domain-specific pipelines (social media, medical, legal)
11. Putting it together with sklearn/spaCy

## Vulnerability Moments
1. Opening confession: avoided NLP preprocessing, thought it was boring
2. Unicode: "I once spent two hours debugging why string equality failed..."
3. Stop words: "I removed stop words everywhere for years before learning it destroyed negation"
4. TF-IDF log: "I'm still not fully satisfied by the log explanation"
5. Domain cleaning: "Every new domain humbles you"

## Analogies
1. Kitchen analogy: raw text is raw ingredients, pipeline is mise en place
2. Library card catalog: vocabulary index, lookup by position
Both recur throughout.

## Rest Stop
After stemming/lemmatization — reader has clean text toolkit.
Before jumping to numerical representations (BoW, TF-IDF).
