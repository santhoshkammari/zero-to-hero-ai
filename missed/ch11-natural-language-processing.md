# Missing Topics: Ch11 Natural Language Processing

Now I have enough information to compile the missing topics. Let me check what the chapter already covers vs. what's missing:

**Already covered in the chapter:**
- Text classification, sentiment analysis (including aspect-based, VADER, sarcasm mention)
- NER with BIO tagging, SpanBERT/span-based NER, CRFs
- POS tagging and dependency parsing
- Semantic similarity
- NLI/textual entailment
- QA (extractive, abstractive, open-domain, SQuAD)
- Summarization (extractive/TextRank, abstractive/BART/Pegasus, ROUGE, BERTScore)
- Coreference resolution (Lee et al. 2017 model)
- Relation extraction (supervised, distant supervision, neural approaches)
- GLUE, SuperGLUE, SQuAD benchmarks
- Embeddings: Word2Vec, GloVe, FastText, ELMo, BPE, WordPiece, SentencePiece
- Text generation: decoding strategies, beam search
- Machine translation: BLEU, METEOR, chrF, COMET, multilingual models
- Nice to Know: constituency/dependency parsing, cross-lingual transfer (mBERT, XLM-R), code-switching, multimodal NLP, document understanding, speech-text, prompt engineering, chain-of-thought, constitutional AI, tool use

Based on my analysis, here are the findings:

## Summary

The chapter already has surprisingly good coverage of many NLP fundamentals. However, several important topics are either completely absent or only mentioned in passing. The biggest gaps are: **dialogue systems/conversational AI**, **knowledge graphs from text**, **NLP evaluation metrics comprehensively**, **semantic role labeling**, **intent detection & slot filling**, **event extraction**, **emotion detection beyond sentiment**, **text-to-SQL/semantic parsing**, **few-shot/in-context learning for NLP tasks**, **entity linking/disambiguation**, **active learning for NLP**, and **NLP bias/fairness**. The chapter mentions some of these in passing (e.g., aspect-based sentiment gets one paragraph) but lacks the depth expected for interview preparation.

## Key Missing Topics

### 1. Dialogue Systems & Conversational AI (COMPLETELY MISSING)
- **Task-oriented dialogue**: Intent detection + slot filling (the ATIS/SNIPS paradigm) — this is a major interview topic
- **Dialogue state tracking (DST)**: Tracking user goals across multi-turn conversations
- **Open-domain chatbots**: Retrieval-based vs. generative approaches
- **Dialogue act classification**: Classifying utterance function (question, statement, request)
- Source: nlpprogress.com tracks this as a dedicated area with benchmarks (Switchboard, MRDA, MultiWOZ)
- Source: HuggingFace lists it implicitly under text generation tasks

### 2. Intent Detection & Slot Filling (COMPLETELY MISSING)
- Joint models for NLU in conversational systems
- BIO-based slot filling (the chapter covers BIO for NER but never connects to dialogue)
- Key benchmarks: ATIS (98.99% intent accuracy SOTA), SNIPS
- Models: Stack-Propagation, Capsule-NLU, Co-Interactive Transformer
- Source: nlpprogress.com/english/intent_detection_slot_filling.html

### 3. Semantic Role Labeling (COMPLETELY MISSING)
- "Who did what to whom" — predicate-argument structure
- Uses BIO notation similar to NER
- Key benchmark: OntoNotes (87.67 F1 SOTA), CoNLL-2005
- Critical for information extraction and QA systems
- Source: nlpprogress.com/english/semantic_role_labeling.html

### 4. Knowledge Graphs from Text (BARELY MENTIONED)
- The chapter mentions relation extraction produces triples but never covers:
  - Knowledge graph construction pipelines
  - Knowledge graph embeddings (TransE, RotatE, ComplEx)
  - Knowledge graph completion/link prediction
  - Open Information Extraction (OpenIE)
  - KB canonicalization (merging duplicate entities/relations)
- Source: nlpprogress.com/english/information_extraction.html covers Open KG Canonicalization

### 5. Event Extraction (COMPLETELY MISSING)
- Detecting events (triggers) and their arguments from text
- ACE2005 benchmark
- Temporal event ordering
- Difference from relation extraction: events have triggers, time, participants

### 6. Entity Linking / Entity Disambiguation (COMPLETELY MISSING)
- Mapping entity mentions to knowledge base entries (e.g., "Apple" → company vs. fruit)
- Key benchmarks and systems
- Zero-shot entity linking
- Source: nlpprogress.com lists it as a tracked task

### 7. Emotion Detection (MISSING — goes beyond sentiment)
- Multi-label emotion classification (joy, anger, fear, sadness, surprise, disgust)
- GoEmotions dataset (27 emotion categories)
- Emotion cause extraction
- Difference from sentiment: sentiment is polarity, emotion is categorical

### 8. Comprehensive NLP Evaluation Metrics Section (PARTIALLY COVERED, SCATTERED)
- The chapter mentions BLEU/METEOR/ROUGE/BERTScore across different sections but lacks a unified treatment:
  - **Perplexity** for language models (a common interview question per projectpro.io)
  - **BLEU** details (brevity penalty, n-gram precision)
  - **METEOR** (stem matching, synonyms, alignment)
  - **CIDEr** for captioning
  - **Human evaluation protocols**: inter-annotator agreement, Likert scales
  - **LLM-as-judge** evaluation paradigm
  - **Faithfulness metrics** for generation (factual consistency)

### 9. Text-to-SQL / Semantic Parsing (COMPLETELY MISSING)
- Converting natural language questions to structured queries
- Spider benchmark, WikiSQL
- Key interview topic for data engineering + NLP roles
- Source: nlpprogress.com lists semantic parsing as tracked task

### 10. Grammatical Error Correction (COMPLETELY MISSING)
- Sequence-to-sequence approach to fixing grammar
- BEA-2019 shared task
- Applications in writing assistants (Grammarly-type systems)
- Source: nlpprogress.com/english/grammatical_error_correction.html

### 11. Keyphrase Extraction & Generation (COMPLETELY MISSING)
- Extractive: TextRank, RAKE, YAKE
- Generative: seq2seq models that generate keyphrases not in document
- Applications: search, document indexing, topic modeling

### 12. Text Simplification (COMPLETELY MISSING)
- Making complex text accessible
- Lexical simplification, sentence splitting
- Applications: accessibility, education
- Source: nlpprogress.com tracks this

### 13. Stance Detection (COMPLETELY MISSING)
- Determining if text is FOR, AGAINST, or NEUTRAL toward a target
- Related to but distinct from sentiment analysis
- Applications: fake news detection, political analysis
- Source: nlpprogress.com/english/stance_detection.html

### 14. Few-Shot & In-Context Learning for NLP (MINIMAL)
- The chapter mentions zero-shot classification briefly but doesn't cover:
  - Few-shot NER approaches
  - In-context learning patterns for NLP tasks
  - Prompt tuning vs. fine-tuning tradeoffs
  - SetFit, Pattern-Exploiting Training (PET)

### 15. Data-to-Text Generation (COMPLETELY MISSING)
- Generating natural language from structured data (tables, databases, APIs)
- Sports reporting, weather reports, financial summaries
- Source: nlpprogress.com/english/data_to_text_generation.html

### 16. Lexical Normalization (MISSING AS DISTINCT TOPIC)
- Normalizing noisy text (social media, SMS)
- "u r gr8" → "you are great"
- The chapter mentions social media cleaning in passing but not as a formal task

### 17. Word Sense Disambiguation (COMPLETELY MISSING)
- Determining which meaning of a polysemous word is intended
- The chapter mentions polysemy in the embeddings section but never covers WSD as a task
- Key benchmark: SemEval WSD tasks
- Source: nlpprogress.com/english/word_sense_disambiguation.html

### 18. Domain Adaptation for NLP (COMPLETELY MISSING)
- Adapting models trained on one domain to another
- Techniques: continued pretraining, adapter layers, domain-adversarial training
- Source: nlpprogress.com lists it as tracked area

### 19. NLP Bias, Fairness & Ethics (COMPLETELY MISSING)
- Gender/racial bias in word embeddings and LLMs
- Debiasing techniques (counterfactual data augmentation, projection methods)
- Toxicity detection and content moderation
- Common interview topic for responsible AI positions

### 20. Active Learning for NLP (COMPLETELY MISSING)
- Strategies for selecting which examples to annotate
- Uncertainty sampling, query-by-committee
- Practical for building NLP systems with limited labeled data

### 21. Annotation & Labeling for NLP (COMPLETELY MISSING)
- Inter-annotator agreement (Cohen's kappa, Fleiss' kappa)
- Annotation guidelines design
- Crowdsourcing vs. expert annotation
- Common interview question: "How would you create a labeled dataset for X?"

### 22. Paraphrase Detection & Generation (BARELY MENTIONED)
- Mentioned in GLUE (MRPC, QQP) but not as standalone topic
- Paraphrase generation for data augmentation
- Source: nlpprogress.com/english/paraphrase-generation.html

### 23. Language Modeling Fundamentals (PARTIALLY COVERED)
- The chapter covers generation/decoding but doesn't explicitly cover:
  - Perplexity as evaluation metric
  - N-gram language models (bigram, trigram) — mathematical formulation
  - Smoothing techniques (Laplace, Kneser-Ney)
  - These are very common interview questions (confirmed by projectpro.io)

### 24. Topic Modeling (COMPLETELY MISSING)
- LDA (Latent Dirichlet Allocation)
- LSA/LSI (mentioned in interviews per projectpro.io)
- Neural topic models (BERTopic)
- Still relevant for unsupervised text exploration

### 25. Text Ranking / Information Retrieval (MISSING)
- BM25
- Neural re-ranking (cross-encoders vs. bi-encoders)
- ColBERT, late interaction models
- Dense passage retrieval (DPR)
- Critical for RAG systems (mentioned but not detailed)
- Source: HuggingFace lists "Text Ranking" as a task with 979 models

## Interview-Specific Gaps (from projectpro.io questions)

Common interview questions NOT adequately covered in the chapter:
1. **Perplexity** — definition, formula, interpretation
2. **N-gram models** — bigram probability, smoothing
3. **Latent Semantic Indexing/Analysis** — SVD-based approach
4. **Naive Bayes for text** — mathematical formulation for NLP
5. **HMM for sequence labeling** — forward-backward, Viterbi (mentioned briefly for CRF but no HMM detail)
6. **Regular expressions for NLP** — pattern matching fundamentals
7. **Attention mechanism details** — self-attention math (may be in transformer chapter)
8. **Difference between NLU, NLG, NLP** — terminology hierarchy

## Gaps Relative to nlpprogress.com Task List

Tasks tracked by nlpprogress.com that are MISSING from the chapter:
- Automatic speech recognition (only briefly in Nice to Know)
- Common sense reasoning
- Data-to-Text Generation
- Dialogue (entire area)
- Domain adaptation
- Entity linking
- Grammatical error correction
- Intent detection and slot filling
- Keyphrase extraction and generation
- Lexical normalization
- Multi-task learning for NLP
- Paraphrase generation
- Semantic parsing
- Semantic role labeling
- Simplification
- Stance detection
- Taxonomy learning
- Temporal processing
- Word sense disambiguation
