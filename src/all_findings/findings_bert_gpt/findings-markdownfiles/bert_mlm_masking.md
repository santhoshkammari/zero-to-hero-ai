# BERT MLM 80/10/10 Masking Strategy

- 15% of tokens selected for prediction
- 80% replaced with [MASK], 10% random token, 10% unchanged
- Addresses pre-train/fine-tune discrepancy (no [MASK] at inference)
- Random replacements force robust contextual representations
- Unchanged tokens prevent model from only activating on [MASK]
- Key insight: forces deep encoding of context, not shortcut learning from [MASK] artifact
