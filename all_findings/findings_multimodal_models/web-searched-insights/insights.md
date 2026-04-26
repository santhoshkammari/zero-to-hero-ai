# Web Search Insights

## CLIP
- Symmetric cross-entropy loss, learned temperature parameter
- Batch size of 32,768 critical - each sample is negative for all others
- L2 normalized embeddings on unit hypersphere
- Zero-shot via cosine similarity between image and text prompt embeddings

## Modality Gap (2024 Research)
- Cone effect: neural network inductive biases cause embeddings for each modality to cluster in distinct cones
- Contrastive loss itself creates and preserves the gap
- Anisotropic separation, not random noise
- Mitigation: parameter sharing, intra-modality separation, uniformity loss, AlignCLIP
- Some researchers argue: "accept the gap" - forcing overlap can destroy semantic structure

## Flamingo
- Frozen vision encoder → Perceiver Resampler (learned queries cross-attend to visual features) → 64 fixed tokens
- Gated cross-attention: gate initialized near zero, preserves LLM abilities
- Interleaved image-text sequences

## LLaVA
- CLIP ViT → MLP projection → concatenate with text tokens → LLM
- Stage 1: train MLP only (LLM frozen), image-caption alignment
- Stage 2: fine-tune everything on visual instruction data
- GPT-4 generated 150K instruction-following examples

## LayoutLM
- BERT + 2D position embeddings from OCR bounding boxes
- Each token gets text + segment + 1D position + 2D spatial (x0,y0,x1,y1) embeddings
- Enables understanding of forms, invoices, receipts

## ImageBind
- Images as the anchor/hub modality
- Six modalities: image, text, audio, depth, thermal, IMU
- Emergent cross-modal alignment without explicit paired data for all combinations
- Audio-text retrieval works despite never seeing audio-text pairs

## GPT-4o / Gemini
- Natively multimodal from scratch - single model handles all modalities
- GPT-4o: text, image, audio in single architecture, real-time audio I/O
- Gemini: designed from ground up for text, images, audio, video
- Contrast with adapter approach (Flamingo, LLaVA): bolt vision onto existing LLM
