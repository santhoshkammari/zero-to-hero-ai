# NLP Task Landscape Research Summary

## Key Architecture Mapping
- **Sequence Classification**: One label per input (sentiment, topic, intent, NLI). Uses [CLS] token + classification head.
- **Token Classification**: One label per token (NER, POS tagging). Uses per-token hidden states + linear layer.
- **Seq2Seq**: Input sequence → output sequence (summarization, abstractive QA, translation). Encoder-decoder (T5, BART).
- **Span Classification**: Classify spans (extractive QA start/end positions, span-based NER).

## Tasks covered
1. Text Classification (sentiment, topic, intent)
2. NER (BIO tagging, SpanBERT, nested entities)
3. POS Tagging (Universal POS, Penn Treebank)
4. Dependency Parsing (head-modifier, UD framework)
5. Semantic Similarity (STS, SBERT, Siamese networks)
6. Textual Entailment / NLI (premise-hypothesis, 3-way classification)
7. Question Answering (extractive vs abstractive, SQuAD)
8. Summarization (extractive TextRank, abstractive BART/T5)
9. Coreference Resolution (mention detection + clustering)
10. Relation Extraction (triples, distant supervision, marker tokens)

## Benchmarks
- GLUE: CoLA, SST-2, MRPC, QQP, STS-B, MNLI, RTE, WNLI
- SuperGLUE: BoolQ, WiC, CB, COPA, MultiRC, ReCoRD, WSC, RTE
- SQuAD: Extractive QA benchmark (v1.1 and v2.0 with unanswerable)

## Running Example Idea
Build a customer support system for a fictional e-commerce company "ShopBot" that needs to handle customer messages end-to-end. Each NLP task maps naturally to a real need in this system.
