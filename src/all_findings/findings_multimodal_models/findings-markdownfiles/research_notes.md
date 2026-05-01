# Multimodal Models Research Notes

## Key Concepts to Cover (Build-up Order)
1. Why multimodal? The limitation of single-modality models
2. The fusion problem - how to combine information from different senses
3. Late fusion (simplest) - CLIP as the canonical example
4. Contrastive learning mechanics - the N×N similarity matrix
5. Zero-shot transfer from shared embedding spaces
6. Cross-attention fusion - letting modalities talk to each other
7. Flamingo's Perceiver Resampler + gated cross-attention
8. LLaVA's simplicity - MLP projection that worked
9. Early fusion - tokenize everything, process together (Gemini, GPT-4o)
10. Document understanding - LayoutLM spatial position encoding
11. ImageBind - anchoring all modalities through images
12. The modality gap problem - cone effect, contrastive gap
13. Unified architectures - GPT-4o, Gemini

## Running Example
Building a "smart museum guide" that takes photos of artwork and answers questions about them. Starts simple (matching images to descriptions), grows to answering complex questions, understanding audio tours, reading plaques.

## Vulnerability Moments
- "I avoided multimodal for a while - it felt like gluing different systems together"
- "The modality gap genuinely surprised me - embeddings don't actually overlap"
- "I'm still developing intuition for when early vs late fusion matters in practice"
- "No one fully understands why the simple LLaVA approach works as well as it does"
- "I still get tripped up by which fusion strategy to pick"

## Key Analogies
1. Translation desk at UN (interpreters converting between languages = encoders mapping to shared space)
2. Orchestra conductor (fusion strategies = how the conductor coordinates instruments)
