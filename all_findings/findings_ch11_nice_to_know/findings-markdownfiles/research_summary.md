# Ch11 Nice to Know - Research Summary

## Topics to Cover
1. Linguistic Structure (syntax trees, constituency vs dependency parsing)
2. Cross-lingual Transfer (mBERT, XLM-R, zero-shot transfer)
3. Code-switching (multilingual mid-sentence switching)
4. Multimodal NLP (CLIP text side, Flamingo)
5. Document Understanding (LayoutLM - spatial + text)
6. Speech-Text Integration (Whisper encoder-decoder)
7. Prompt Engineering Taxonomy (zero-shot, few-shot, CoT, ToT, role-based, self-consistency)
8. Chain-of-Thought Reasoning (Wei et al 2022, step-by-step decomposition)
9. Constitutional AI (Anthropic, RLAIF, self-critique, principles)
10. Tool Use / Function Calling (JSON schema, structured output, execution loop)

## Running Example Idea
Build a multilingual customer support bot that starts with basic text and grows to handle:
- Parsing customer messages (linguistic structure)
- Supporting multiple languages (cross-lingual, code-switching)
- Understanding uploaded receipts/documents (LayoutLM)
- Voice input (Whisper)
- Seeing product images (CLIP)
- Reasoning about refund policies (CoT)
- Following safety guidelines (Constitutional AI)
- Looking up order status via API (tool use)

## Key Insights
- Constituency parsing = phrase grouping hierarchy (NP, VP, PP)
- Dependency parsing = word-to-word relationships (subject, object, modifier)
- mBERT learns cross-lingual alignment without explicit parallel data - shared subword vocab is key
- Code-switching breaks tokenizers, lacks training data, mixes grammars
- CLIP: 12-layer transformer text encoder, BPE tokenizer, contrastive InfoNCE loss, shared embedding space
- LayoutLM: BERT + 2D bounding box spatial embeddings for each token
- Whisper: encoder-decoder transformer, log-mel spectrogram input, autoregressive text output
- CoT: explicit intermediate reasoning steps, works best on large models, "let's think step by step"
- Constitutional AI: constitution (principles) + self-critique + RLAIF = reduces human labeler dependency
- Tool use: LLM outputs structured JSON function calls, platform executes, result fed back
