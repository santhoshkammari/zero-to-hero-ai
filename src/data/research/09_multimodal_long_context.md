# Multimodal AI & Long Context: Unifying Vision, Language, Audio, and Memory

> AI that sees, reads, hears, and remembers — the convergence toward general intelligence

---

## Why This Matters

For most of the deep learning era, models were specialists. A language model processed text.
A vision model processed images. A speech model processed audio. Each lived in its own
embedding space, its own training pipeline, its own deployment stack.

That era is ending.

The most capable AI systems of 2024 are **multimodal**: they ingest images, text, audio, and
video through a single architecture, reason across modalities simultaneously, and generate
outputs in any combination of them. Alongside this, the **long context revolution** has
expanded what these models can hold in working memory from a few thousand tokens to over
a million — enabling them to process entire books, hours of audio, or hundreds of document
pages in a single forward pass.

These two trends — multimodality and long context — are deeply coupled. A model that can
see an image produces hundreds of visual tokens. A model that processes an hour of audio
generates tens of thousands of audio tokens. Without the ability to handle long sequences
efficiently, multimodal models would be crippled. Together, they represent the most
significant architectural shift in AI since the original Transformer.

**Why you should care:**
- **Multimodal understanding** is the foundation for AI assistants that can look at your
  screen, read your documents, listen to your voice, and respond coherently
- **Long context** eliminates the need for complex chunking, retrieval, and summarization
  pipelines — the model just reads everything
- **The combination** enables use cases that were impossible two years ago: analyzing a
  100-page PDF with charts and tables, having a real-time voice conversation about a
  video feed, or coding from a screenshot of a design mockup

This chapter traces both revolutions — from the foundational ideas in contrastive learning
and position encodings, through the architectural innovations that made them practical,
to the systems-level optimizations that make them fast.

---

## Vision-Language Models

### CLIP's Legacy: Where It All Began

Before multimodal LLMs existed, there was **CLIP** (Contrastive Language-Image Pre-training,
OpenAI, 2021). CLIP didn't generate text or answer questions — it learned to **align** images
and text in a shared embedding space. But its impact on everything that followed cannot be
overstated.

**The contrastive learning idea:**

```
Given a batch of N (image, text) pairs:

1. Encode each image through a vision encoder  → image_embeddings [N, d]
2. Encode each text through a text encoder     → text_embeddings  [N, d]
3. Compute similarity matrix                   → S = image_emb @ text_emb.T  [N, N]
4. The diagonal entries are positive pairs (matching image-text)
5. Off-diagonal entries are negative pairs (non-matching)
6. Train with symmetric cross-entropy loss to maximize diagonal, minimize off-diagonal
```

The loss function (InfoNCE) for a single image i:

```
L_image(i) = -log( exp(sim(I_i, T_i) / τ) / Σ_j exp(sim(I_i, T_j) / τ) )

where:
  sim(a, b) = cosine_similarity(a, b)
  τ = learnable temperature parameter
```

**Why CLIP mattered:**

1. **Zero-shot transfer**: CLIP could classify images it had never seen during training by
   comparing image embeddings against text embeddings of class descriptions ("a photo of a
   dog", "a photo of a cat"). No task-specific fine-tuning needed.

2. **Web-scale training**: Trained on 400 million image-text pairs scraped from the internet.
   This demonstrated that noisy, large-scale data could produce powerful representations —
   a lesson that shaped every multimodal model afterward.

3. **The visual encoder everyone uses**: CLIP's ViT (Vision Transformer) became the default
   visual backbone for nearly every subsequent vision-language model — LLaVA, BLIP-2,
   Flamingo, and dozens of others simply took CLIP's pre-trained vision encoder and built
   on top of it.

4. **Shared embedding space**: The idea that images and text should live in the same vector
   space — where "a golden retriever playing fetch" and a photo of that scene are nearby
   vectors — became the foundational assumption of the field.

### Vision Transformers (ViT) as Visual Encoders

The Vision Transformer (ViT), introduced by Google in 2020 ("An Image is Worth 16x16 Words"),
is the architecture that made transformer-based vision practical. It takes the self-attention
mechanism from NLP and applies it directly to images.

**How ViT processes an image:**

```
Input: Image of size H × W × C (e.g., 224 × 224 × 3)

Step 1: Patchify
  Split image into P × P patches (typically P = 14 or 16)
  Number of patches = (H/P) × (W/P)
  For 224×224 with P=16: 14 × 14 = 196 patches

Step 2: Flatten and Project
  Each patch (P × P × C) is flattened to a vector of dimension P²·C
  For P=16, C=3: 16 × 16 × 3 = 768 dimensions
  A learned linear projection maps this to the model dimension d:
    patch_embed = Linear(P²·C, d)

Step 3: Add Position Embeddings
  Learnable position embeddings are added to each patch embedding
  pos_embed ∈ R^(N_patches × d)
  This tells the model where each patch came from spatially

Step 4: Prepend [CLS] Token
  A special classification token is prepended to the sequence
  Total sequence: [CLS, patch_1, patch_2, ..., patch_196]
  Length: 197 tokens

Step 5: Transformer Encoder
  Standard transformer encoder blocks (self-attention + FFN)
  Each patch attends to every other patch (global receptive field)
  Output: 197 contextualized embeddings

Step 6: Output
  [CLS] token embedding → global image representation
  All patch embeddings → local, spatially-aware representations
```

**Key insight**: After passing through the transformer, each patch embedding has been
contextualized by attending to every other patch. The model understands both local
features (edges, textures in a single patch) and global structure (the relationship
between a person's face and their hand gesture, even if they're in different patches).

**Scale variants commonly used in multimodal models:**

| Model         | Patches | Dim  | Layers | Heads | Params |
|---------------|---------|------|--------|-------|--------|
| ViT-B/16      | 16×16   | 768  | 12     | 12    | 86M    |
| ViT-L/14      | 14×14   | 1024 | 24     | 16    | 304M   |
| ViT-H/14      | 14×14   | 1280 | 32     | 16    | 632M   |
| ViT-G/14      | 14×14   | 1664 | 48     | 16    | 1.8B   |

Most state-of-the-art multimodal models in 2024 use ViT-L/14 or larger as their visual
backbone, often initialized from CLIP or SigLIP pre-trained weights.

### How Images Get Tokenized for LLMs

The central challenge of vision-language models is bridging two fundamentally different
representations: the continuous, spatial features from a vision encoder and the discrete
token sequences that language models expect. Several strategies have emerged:

**Strategy 1: Direct Projection (LLaVA approach)**

```
Visual tokens = Linear_projection( ViT_output_patches )

ViT output: [N_patches, d_vision]  →  Projection: [N_patches, d_llm]

The projected visual tokens are simply concatenated with text tokens:
Input to LLM: [visual_1, visual_2, ..., visual_N, <text_tokens>]
```

This is the simplest approach. Each image patch becomes one token in the LLM's input
sequence. A 224×224 image with 14×14 patches produces 196 visual tokens. A 336×336
image produces 576 tokens. Higher resolution means more tokens.

**Strategy 2: Resampling (Flamingo approach)**

```
Perceiver Resampler:
  Input: Variable-length ViT features [N_patches, d]
  Learnable queries: [M, d]  where M << N_patches (e.g., M = 64)

  For each cross-attention layer:
    queries attend to ViT features (cross-attention)
    queries self-attend (self-attention)

  Output: Fixed M visual tokens regardless of image resolution
```

This compresses visual information into a fixed number of tokens, making the approach
more token-efficient but potentially losing fine-grained spatial detail.

**Strategy 3: Q-Former (BLIP-2 approach)**

```
Q-Former (Query Transformer):
  32 learnable query tokens attend to frozen ViT features
  Trained with three objectives simultaneously:
    1. Image-text contrastive learning
    2. Image-grounded text generation
    3. Image-text matching

  Output: 32 visual tokens that capture image semantics
  These 32 tokens are then projected and fed to a frozen LLM
```

The Q-Former approach is extremely parameter-efficient — only the Q-Former (~188M params)
is trained, while both the ViT encoder and the LLM remain frozen.

**Token count comparison:**

| Method         | Tokens per Image | Trainable Params | Resolution Flexible |
|----------------|-----------------|------------------|---------------------|
| Direct (LLaVA) | 196-576+       | Projection layer | Yes (more res = more tokens) |
| Resampler      | 64 (fixed)     | Resampler module | Yes (compressed)    |
| Q-Former       | 32 (fixed)     | Q-Former         | Yes (compressed)    |
| Dynamic (InternVL) | 256-1024+  | Projection + adapter | Yes (adaptive) |

### LLaVA: Visual Instruction Tuning

**LLaVA** (Large Language-and-Vision Assistant, 2023) demonstrated that a surprisingly simple
architecture could achieve strong multimodal performance. Its significance lies not in
architectural novelty but in the **training methodology**: visual instruction tuning.

**Architecture (LLaVA 1.5):**

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  CLIP ViT-L/14  │────▶│  MLP Bridge  │────▶│    Vicuna-7B    │
│  (frozen or     │     │  (2-layer    │     │  or 13B LLM     │
│   fine-tuned)   │     │   projection)│     │  (fine-tuned)   │
└─────────────────┘     └──────────────┘     └─────────────────┘
     336×336 image          576 visual           Autoregressive
     → 576 patches          tokens in            text generation
                            LLM space
```

**Two-stage training:**

```
Stage 1: Feature Alignment (Pre-training)
  - Freeze: ViT encoder + LLM
  - Train: Only the MLP projection layer
  - Data: 558K image-caption pairs
  - Goal: Align visual features to LLM's embedding space
  - Duration: ~5 hours on 8× A100 GPUs

Stage 2: Visual Instruction Tuning (Fine-tuning)
  - Freeze: ViT encoder
  - Train: MLP projection + full LLM
  - Data: 665K multimodal instruction-following examples
  - Types: Conversations, detailed descriptions, complex reasoning
  - Duration: ~20 hours on 8× A100 GPUs
```

**The instruction-tuning data was the key innovation.** The team used GPT-4 to generate
high-quality instruction-following data from existing image-caption datasets:

```
Example instruction-tuning sample:

Image: [photo of a busy kitchen]
Human: What safety hazards can you identify in this image?
Assistant: I can identify several potential safety hazards in this kitchen:
1. The knife is placed near the edge of the counter, where it could fall
2. There appears to be water on the floor near the stove, creating a slip risk
3. The pot handle is facing outward over the stove edge...
```

This approach — using a powerful model to generate training data for a more efficient
model — became a widely adopted pattern. LLaVA showed that with the right data,
even a simple linear projection could bridge vision and language effectively.

### Flamingo, BLIP-2, and InternVL: Alternative Approaches

**Flamingo (DeepMind, 2022)** pioneered efficient multimodal integration:

```
Key innovations:
1. Perceiver Resampler: Compresses variable visual features to fixed-size
2. Gated cross-attention: Interleaved between frozen LLM layers
   - Cross-attention layers let text attend to visual features
   - Gating mechanism (initialized at zero) allows graceful integration
   - tanh(α) * cross_attention_output  (α starts at 0, learned)
3. Few-shot in-context learning: Process multiple interleaved images and text
```

**BLIP-2 (Salesforce, 2023)** focused on parameter efficiency:

```
Architecture: Frozen ViT → Q-Former → Frozen LLM

Q-Former training (two stages):
  Stage 1: Vision-language representation learning
    - Q-Former learns to extract visual features via 3 losses
    - ITC (Image-Text Contrastive), ITG (Image-grounded Text Generation),
      ITM (Image-Text Matching)
  Stage 2: Vision-to-language generative learning
    - Q-Former output connected to frozen LLM via projection
    - LLM learns to generate text from Q-Former's visual tokens

Total trainable params: ~188M (vs billions in the full pipeline)
```

**InternVL (Shanghai AI Lab, 2023-2024)** scaled up aggressively:

```
Key differences:
1. Custom ViT backbone: InternViT-6B (6 billion parameters!)
   - Much larger than typical CLIP ViT-L (304M)
   - Trained from scratch on massive image-text data
2. Dynamic resolution: Adaptive token count based on image complexity
3. Progressive training: Contrastive → generative → instruction tuning
4. Open-source focus: Competitive with proprietary models
```

**Architectural comparison:**

```
Flamingo:  ViT ──▶ Perceiver ──▶ Cross-Attention (interleaved in LLM)
                   Resampler      ↕ LLM layers ↕

BLIP-2:   ViT ──▶ Q-Former ──▶ Linear ──▶ LLM (frozen)

LLaVA:    ViT ──▶ MLP ──▶ [visual tokens + text tokens] ──▶ LLM

InternVL: InternViT-6B ──▶ Projection ──▶ LLM (with adapters)
```

---

## Native Multimodal Models

### Early Fusion vs. Late Fusion vs. Cross-Attention

The fundamental architectural question in multimodal AI is **when** and **how** to combine
information from different modalities. Three paradigms have emerged:

**Late Fusion (Separate Encoders, Combined Later)**

```
┌──────────┐     ┌──────────┐
│  Vision   │     │ Language  │
│  Encoder  │     │ Encoder   │
│  (ViT)    │     │ (BERT)    │
└─────┬─────┘     └─────┬─────┘
      │                 │
      ▼                 ▼
   [v_emb]           [t_emb]
      │                 │
      └────────┬────────┘
               ▼
        Fusion Layer
        (concat, add,
         attention)
               │
               ▼
           Output

Examples: CLIP, basic dual-encoder models
Pros: Modular, can pre-train separately, efficient retrieval
Cons: Limited cross-modal interaction, misses fine-grained alignment
```

**Cross-Attention Fusion (Bridged Encoders)**

```
┌──────────┐
│  Vision   │
│  Encoder  │──────────────┐
└──────────┘               │
                    Cross-Attention
┌──────────┐        Layers          ┌──────────┐
│ Language  │──────▶ (vision        │  Output   │
│  Model    │        attends to     │  Decoder  │
│           │◀────── language and   │           │
└──────────┘        vice versa)     └──────────┘

Examples: Flamingo, CoCa
Pros: Rich cross-modal interaction, keeps modality-specific features
Cons: More complex, cross-attention adds latency
```

**Early Fusion (Native Multimodal — Single Backbone)**

```
┌─────────────────────────────────────┐
│         Shared Transformer          │
│                                     │
│  Input: [img_tok_1, img_tok_2, ..., │
│          txt_tok_1, txt_tok_2, ..., │
│          aud_tok_1, aud_tok_2, ...] │
│                                     │
│  Every token attends to every other │
│  token regardless of modality.      │
│  No separate encoders.              │
│                                     │
│  Output: unified representation     │
└─────────────────────────────────────┘

Examples: GPT-4o, Gemini
Pros: Deepest cross-modal understanding, lowest latency
Cons: Enormous training cost, requires all modalities from start
```

### GPT-4V/4o: The Omni Approach

GPT-4V (Vision) was OpenAI's first production multimodal model, adding image understanding
to GPT-4. But it was architecturally a **bolted-on** system — images went through a
separate encoder and were projected into GPT-4's input space.

**GPT-4o** ("omni", May 2024) represented a fundamental shift:

```
GPT-4V (2023):                    GPT-4o (2024):
Audio → Whisper → Text ─┐         Audio ─────┐
                        │                     │
Image → ViT → Proj ────▶│ GPT-4   All ──────▶│ Single    ──▶ Any
                        │                     │ Transformer    modality
Text ──────────────────▶│         Image ─────┤              output
                                              │
                        Text ──────────────────┘

Pipeline latency:                 End-to-end latency:
Audio: ~300ms (Whisper)           Audio: ~200ms total
+ LLM: ~500ms                    (no intermediate text)
+ TTS: ~300ms
= ~1.1 seconds                   Preserves tone, emotion,
                                  emphasis — no information
Loses emotion, tone,             loss from transcription
emphasis in transcription
```

**What "native multimodal" means technically:**

1. **Single tokenizer** handles all modalities — images are patchified, audio is converted
   to spectral tokens, text is BPE-tokenized. All token types share the same embedding space.

2. **Joint pre-training** — the model is trained on interleaved multimodal data from the
   start, not fine-tuned to accept images after text pre-training.

3. **Cross-modal attention from layer 1** — image tokens can attend to audio tokens can
   attend to text tokens, all within the same self-attention mechanism, from the very first
   transformer layer.

4. **Any-to-any generation** — the model can output text, audio, or (in principle) images
   from any combination of inputs, without routing through intermediate text.

### Gemini: Natively Multimodal from Pre-training

Google's Gemini (December 2023) was designed as a natively multimodal model from its
inception — images, text, audio, and video were all part of the pre-training data mixture.

**Key architectural properties:**

```
Gemini's approach:
1. Multimodal tokenization from the start:
   - Text: SentencePiece tokenizer
   - Images: ViT-based patch tokenization
   - Audio: Universal Speech Model (USM) features
   - Video: Frame-by-frame ViT encoding + temporal tokens

2. Interleaved multimodal pre-training:
   - Training data mixes text, image-text, video-text, audio-text
   - The model never encounters a "text-only phase" followed by
     a "multimodal phase" — it's mixed from day one

3. Context window: Up to 1M tokens (Gemini 1.5 Pro)
   - This means: ~1 hour of video, or ~11 hours of audio,
     or ~700,000 words of text, or combinations thereof
```

**Why native multimodal outperforms bolted-on approaches:**

```
Bolted-on (e.g., LLaVA):
  ViT features → projection → LLM
  Problem: The LLM was pre-trained on text only.
  Visual tokens are "foreign" — the LLM must learn to interpret
  them during fine-tuning, with limited multimodal data.
  The deeper layers of the LLM have text-specific inductive biases.

Native (e.g., Gemini):
  All modalities → shared tokenizer → single transformer
  Advantage: Every layer, every attention head, every FFN weight
  has been shaped by multimodal data from the start.
  The model develops modality-agnostic representations in deeper
  layers — it represents "concepts" rather than "text about concepts"
  or "images of concepts" separately.

Result: Native models show superior performance on tasks requiring
deep cross-modal reasoning, such as:
  - Describing what's happening in a video while understanding
    the dialogue audio
  - Reading a chart, understanding the axes, and answering
    mathematical questions about the data
  - Following a recipe shown in an image while understanding
    spoken modifications
```

---

## Audio & Speech Integration

### Whisper and Speech-to-Text

**Whisper** (OpenAI, 2022) brought the "scale solves everything" philosophy to speech
recognition. Trained on 680,000 hours of labeled audio data from the web, it demonstrated
that a simple encoder-decoder Transformer, given enough data, could match or exceed
specialized ASR systems.

**Architecture:**

```
Audio Input
    │
    ▼
Log-Mel Spectrogram
(80 frequency bins × time frames)
    │
    ▼
┌─────────────────────────────┐
│    Convolutional Frontend    │
│  2 Conv1D layers:            │
│    Conv(80→d, kernel=3)      │
│    Conv(d→d, kernel=3, s=2)  │
│  Downsamples by factor of 2  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│    Transformer Encoder       │
│  Sinusoidal position embs    │
│  N layers of self-attention  │
│  + FFN                       │
│  Output: audio features      │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│    Transformer Decoder       │
│  Learned position embs       │
│  Cross-attention to encoder  │
│  Autoregressive generation   │
│  Output: text tokens         │
└─────────────────────────────┘

Special tokens control behavior:
  <|startoftranscript|>
  <|en|>  (language)
  <|transcribe|> or <|translate|>
  <|notimestamps|> or timestamps
```

**Whisper's key insight**: By training on diverse, noisy web data across 96 languages,
the model learned to handle accents, background noise, overlapping speech, and
domain-specific vocabulary without explicit noise-handling pipelines.

**Model sizes:**

| Model     | Params | Layers | d_model | Heads | English WER |
|-----------|--------|--------|---------|-------|-------------|
| tiny      | 39M    | 4      | 384     | 6     | ~7.6%       |
| base      | 74M    | 6      | 512     | 8     | ~5.0%       |
| small     | 244M   | 12     | 768     | 12    | ~3.4%       |
| medium    | 769M   | 24     | 1024    | 16    | ~2.9%       |
| large-v3  | 1.55B  | 32     | 1280    | 20    | ~2.1%       |

### Audio Tokens and Audio Understanding

Moving beyond speech-to-text, modern multimodal systems need to **understand** audio
as a first-class modality — not just transcribe it. This requires representing audio
as discrete tokens that can be processed alongside text and image tokens.

**Neural audio codecs (the key technology):**

```
SoundStream / EnCodec architecture:

Raw Audio Waveform (24kHz)
    │
    ▼
┌─────────────────────────────┐
│    Encoder CNN               │
│    Downsamples to latent     │
│    representation            │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  Residual Vector Quantizer   │
│  (RVQ)                       │
│                              │
│  Multiple codebooks:         │
│    Level 1: Coarse structure │
│             (speech content) │
│    Level 2: Finer detail     │
│             (speaker identity│
│    Level 3+: Fine texture    │
│             (ambient, noise) │
│                              │
│  Each level: 1024 codes      │
│  8-16 levels typical         │
└─────────────┬───────────────┘
              │
              ▼
    Discrete Audio Tokens
    (e.g., 75 tokens/sec at
     8 codebook levels)
```

**Why this matters for multimodal LLMs:**

These discrete audio tokens can be treated exactly like text tokens — embedded, processed
through transformer layers, and predicted autoregressively. This enables:

1. **Audio understanding**: The model attends to audio tokens the same way it attends to
   text, learning to extract meaning (what's being said, who's speaking, what emotions
   are present, what background sounds exist)

2. **Audio generation**: The model can predict audio tokens autoregressively, then decode
   them back to waveforms through the neural codec's decoder

3. **Cross-modal reasoning**: Audio tokens and text tokens in the same sequence allow the
   model to reason about connections (e.g., "the speaker sounds anxious when discussing
   deadlines")

### Voice Mode: Real-Time Audio-In, Audio-Out

The "voice mode" capability (as seen in GPT-4o and Gemini Live) represents a paradigm
shift from the traditional pipeline:

**Traditional pipeline:**

```
User Speech → ASR (Whisper) → Text → LLM → Text → TTS → Audio Response
              ~300ms          ~50ms  ~500ms  ~50ms  ~300ms
              Total: ~1.2 seconds minimum latency
              Problem: Emotion, tone, emphasis lost in ASR step
```

**Native voice mode:**

```
User Speech → Audio Tokens → Multimodal Transformer → Audio Tokens → Audio
              ~50ms          ~200ms                    ~50ms
              Total: ~300ms latency
              Advantage: Preserves paralinguistic features throughout
```

**Technical requirements for real-time voice:**

1. **Streaming inference**: The model must begin generating output before the user finishes
   speaking (full-duplex), requiring interleaved input/output token generation
2. **Low-latency audio codec**: Encoding/decoding audio must add minimal delay (~20ms)
3. **Speculative decoding**: Pre-generating likely continuations to reduce perceived latency
4. **Turn-taking**: The model must learn when the user has finished speaking vs. pausing,
   which requires understanding prosodic cues in the audio tokens

### Music and Audio Generation (AudioLM)

**AudioLM** (Google, 2022) demonstrated that language modeling techniques could generate
coherent, long-form audio — including speech and music — by operating on discrete audio
tokens.

**The hierarchical generation approach:**

```
Stage 1: Semantic Token Generation
  - Generate high-level "semantic" tokens that capture content
  - These represent what is being said or the musical structure
  - Model: Transformer trained on semantic tokens (from w2v-BERT)

Stage 2: Coarse Acoustic Token Generation
  - Conditioned on semantic tokens, generate coarse acoustic tokens
  - These capture speaker identity, timbre, recording conditions
  - Model: Transformer conditioned on Stage 1 output

Stage 3: Fine Acoustic Token Generation
  - Conditioned on coarse tokens, generate fine-grained tokens
  - These capture subtle acoustic details for natural sound
  - Model: Transformer conditioned on Stage 2 output

Stage 4: Neural Codec Decoding
  - All acoustic tokens decoded to waveform via SoundStream decoder
```

This hierarchical approach ensures coherent long-range structure (you can't get a
melody that makes sense by just predicting fine-grained audio samples — you need
the high-level structure first).

**Subsequent models built on this foundation:**
- **MusicLM**: Music generation conditioned on text descriptions
- **SoundStorm**: Parallel decoding for much faster audio generation
- **VALL-E / VALL-E X**: Voice cloning from 3-second audio samples
- **Bark**: Open-source text-to-audio with speaker control

---

## Long Context Revolution

### From 2K to 1M+ Tokens

The context window — how many tokens a model can process in a single forward pass —
has undergone exponential growth:

```
Timeline of context length expansion:

2018  GPT-1          512 tokens     (~400 words)
2019  GPT-2          1,024 tokens   (~800 words)
2020  GPT-3          2,048 tokens   (~1,500 words)
2022  GPT-3.5        4,096 tokens   (~3,000 words)
2023  GPT-4          8,192 tokens   (~6,000 words)
      GPT-4-32k      32,768 tokens  (~24,000 words)
      Claude 2       100,000 tokens (~75,000 words)
      Claude 2.1     200,000 tokens
2024  GPT-4 Turbo    128,000 tokens (~96,000 words)
      Gemini 1.5 Pro 1,000,000 tokens (~750,000 words)
      Claude 3       200,000 tokens
      Gemini 1.5     2,000,000 tokens (10M experimental)
      Llama 3.1      128,000 tokens

Growth: ~2000× in 6 years
```

**What 1M tokens means in practice:**

```
1,000,000 tokens ≈
  - 750,000 words of text (about 10 novels)
  - An entire codebase (medium-sized project)
  - ~1 hour of video (with frame descriptions)
  - ~11 hours of audio (transcribed)
  - ~1,500 pages of documents
  - A complete legal case file
```

**Why this matters beyond raw numbers:**

The practical impact isn't just "more text." Long context enables fundamentally
different interaction patterns:

```
Before (4K context):
  User: "Summarize this chapter" (must chunk document)
  System: Splits into 4K chunks, summarizes each, combines
  Problem: Loses cross-chunk relationships, redundancy, inconsistency

After (1M context):
  User: "Summarize this book" (entire book fits)
  System: Reads entire book at once, generates coherent summary
  Advantage: Understands narrative arcs, character development,
             thematic connections across the full text
```

### RoPE (Rotary Position Embeddings)

**RoPE** (Rotary Position Embedding), introduced in the RoFormer paper (Su et al., 2021),
has become the dominant position encoding method in modern LLMs. Llama, Mistral, Qwen,
Gemma, and most open-source models use RoPE.

**The core idea:**

Instead of adding position information to token embeddings (additive, like sinusoidal
embeddings) or learning absolute position embeddings, RoPE **rotates** the query and
key vectors in attention by an angle proportional to their position.

```
Mathematical formulation:

Given position m and dimension pair (2i, 2i+1):

θ_i = 10000^(-2i/d)    (frequency for dimension pair i)

The rotation applied to query q at position m:

┌ q_{2i}^(m)  ┐     ┌ cos(mθ_i)  -sin(mθ_i) ┐   ┌ q_{2i}  ┐
│              │  =  │                         │ × │         │
└ q_{2i+1}^(m)┘     └ sin(mθ_i)   cos(mθ_i)  ┘   └ q_{2i+1}┘

Same rotation applied to keys.

When computing attention: q_m^T · k_n, the relative position (m-n)
naturally emerges from the rotation mathematics:

  (R_m · q)^T · (R_n · k) = q^T · R_{m-n} · k

The attention score depends only on the relative distance (m-n),
not absolute positions — this is key for length generalization.
```

**Why RoPE works well:**

1. **Relative position encoding**: Attention naturally depends on distance between tokens
2. **No learned parameters**: The rotation angles are deterministic (no training needed)
3. **Compatible with linear attention**: Rotation is a unitary operation
4. **Extrapolation potential**: The mathematical structure allows extension techniques

**The problem: RoPE doesn't extrapolate naturally**

When a model trained with max position 4096 encounters position 8192, the rotation
angles are outside the training distribution. The model hasn't seen these rotation
frequencies during training, and performance degrades sharply.

### Extension Techniques: YaRN, NTK-Aware Scaling, ALiBi

Several techniques have been developed to extend RoPE beyond its training length:

**1. Position Interpolation (PI)**

```
Simple idea: Instead of extrapolating to new positions,
interpolate existing positions to fit more tokens.

Original: positions [0, 1, 2, ..., L-1] for training length L
Extended: positions [0, 0.5, 1, 1.5, ..., (L-1)] for 2× length

Formula: position(i) = i × (L_train / L_target)

Problem: Compresses position information — nearby tokens become
harder to distinguish, hurting short-range performance.
```

**2. NTK-Aware Scaling**

```
Insight: Not all frequency dimensions should be scaled equally.

High-frequency dimensions (small θ_i):
  - Encode fine-grained, short-range position differences
  - Scaling these hurts local attention
  - Should be left mostly unchanged

Low-frequency dimensions (large θ_i):
  - Encode coarse, long-range position differences
  - These are the ones that need extending
  - Can be scaled aggressively

NTK-aware approach:
  θ_i' = θ_i × α^(d/(d-2i))

  where α = L_target / L_train

  This scales low-frequency dimensions more than high-frequency,
  preserving short-range resolution while extending long-range capacity.
```

**3. YaRN (Yet another RoPE extensioN)**

```
YaRN combines NTK-aware scaling with attention temperature scaling:

1. Frequency categorization:
   - High-frequency: no modification (preserve local)
   - Medium-frequency: interpolated (blend original and scaled)
   - Low-frequency: NTK-scaled (extend range)

2. Attention scaling factor:
   - √(1/s) applied to attention logits
   - where s = scale factor
   - Corrects for the reduced entropy in attention distributions
     that scaling causes

3. Fine-tuning:
   - Only ~400 training steps needed on extended-length data
   - 0.1% of original pre-training compute

Result: Models extended from 4K to 128K context with minimal
quality degradation and negligible compute cost.
```

**4. ALiBi (Attention with Linear Biases)**

ALiBi takes a completely different approach — no explicit position embeddings at all:

```
Instead of encoding positions in embeddings,
ALiBi adds a linear bias directly to attention scores:

attention_score(i, j) = q_i^T · k_j - m · |i - j|

where m is a head-specific slope (different for each attention head)

Slopes: m_h = 2^(-8h/H) for head h out of H total heads

Effect:
  - Nearby tokens: small penalty → strong attention
  - Distant tokens: large penalty → weak attention
  - Each head has different decay rate → different "attention ranges"

Advantages:
  - No positional embeddings to learn or extend
  - Naturally extrapolates to any length
  - Trained on 1K tokens? Works at 100K with no modification

Disadvantage:
  - Linear decay may be too simple for some position-dependent tasks
  - Less commonly adopted than RoPE (used in MPT, BLOOM)
```

### Ring Attention for Infinite Context

Even with efficient position encodings, standard attention is limited by **memory**:
the key-value cache for N tokens requires O(N × d × L) memory, where d is the
dimension and L is the number of layers. For 1M tokens, this can exceed single-GPU
memory.

**Ring Attention** (2023) solves this by distributing attention computation across
multiple devices in a ring topology:

```
Device layout (logical ring):

  GPU 0 ──▶ GPU 1 ──▶ GPU 2 ──▶ GPU 3
    ▲                                │
    └────────────────────────────────┘

Each GPU holds a block of the sequence:
  GPU 0: tokens [0, N/4)
  GPU 1: tokens [N/4, N/2)
  GPU 2: tokens [N/2, 3N/4)
  GPU 3: tokens [3N/4, N)

Algorithm:
  For each round r = 0, 1, ..., num_devices - 1:
    1. Each GPU computes attention of its Q block against
       the current KV block it holds
    2. Each GPU sends its KV block to the next GPU in the ring
    3. Each GPU receives a KV block from the previous GPU
    4. Accumulate partial attention results (online softmax)

  After num_devices rounds, every GPU has attended to the
  full sequence, but only ever held 1/num_devices of the
  KV cache at a time.

Memory per device: O(N/D × d × L) instead of O(N × d × L)
Communication: O(N × d) per round (overlapped with compute)
```

**The critical insight**: Attention computation can be decomposed into blocks and
accumulated using the online softmax trick (the same trick used in Flash Attention).
Each device computes partial attention scores against a KV block, tracks the running
maximum and sum, and merges results from successive rounds.

```
Online softmax accumulation:

Initialize: max_score = -inf, sum_exp = 0, output = 0

For each KV block b:
  scores_b = Q_local @ K_b.T / sqrt(d)
  new_max = max(max_score, max(scores_b))

  # Rescale previous accumulation
  correction = exp(max_score - new_max)
  sum_exp = sum_exp * correction + sum(exp(scores_b - new_max))
  output = output * correction + exp(scores_b - new_max) @ V_b

  max_score = new_max

Final: output = output / sum_exp
```

This allows attention over sequences that no single device could hold, with context
length scaling linearly with the number of devices.

### The "Lost in the Middle" Problem

A critical finding from Liu et al. (2023): even when models have long context windows,
they don't use all positions equally.

**The experiment:**

```
Setup:
  - Place a key fact ("needle") at various positions in a long document
  - Surround with irrelevant text ("haystack")
  - Ask the model to retrieve/use the key fact

Results (accuracy by position):
  Position     | GPT-3.5 | GPT-4  | Claude 2
  Beginning    | ~95%    | ~98%   | ~96%
  25% in       | ~80%    | ~90%   | ~82%
  Middle       | ~55%    | ~75%   | ~62%
  75% in       | ~70%    | ~88%   | ~75%
  End          | ~92%    | ~97%   | ~94%

Pattern: U-shaped curve — high accuracy at start and end,
significant degradation in the middle.
```

**Why this happens:**

```
1. Attention distribution bias:
   Self-attention naturally develops strong patterns at sequence
   boundaries. The first few tokens receive disproportionate
   attention ("attention sink"), and recent tokens benefit from
   recency bias.

2. Training data distribution:
   Most training examples are short. The model has much more
   practice extracting information from the beginning and end
   of inputs than from arbitrary middle positions.

3. Positional encoding artifacts:
   Position embeddings may provide stronger signals at sequence
   edges, where the model has more training signal.
```

**Mitigation strategies:**

```
1. Training on long sequences with randomly placed targets
2. Explicit "retrieval heads" — attention heads specialized
   for long-range information retrieval
3. Instruction tuning with middle-placement examples
4. Multi-pass approaches: re-order context to place likely
   relevant information at sequence boundaries
5. Better position encodings with uniform attention distribution
```

### Needle-in-a-Haystack Evaluation

The "needle-in-a-haystack" test has become the standard benchmark for evaluating
effective context window utilization:

```
Evaluation protocol:

1. Generate haystack text of length L (using essays, documents, etc.)
2. Insert a distinctive fact (needle) at position p within the haystack:
   "The best thing to do in San Francisco is eat a sandwich and
    sit in Dolores Park on a sunny day."
3. After the haystack, ask: "What is the best thing to do in
   San Francisco?"
4. Vary L from 1K to max context length
5. Vary p from 0% to 100% of L
6. Create a 2D heatmap: (context_length × needle_position) → accuracy

Ideal result: Green (100% accuracy) everywhere
Typical result: Green at edges, yellow/red in the middle for
                certain lengths

This has become the standard "proof" that a model can actually
use its full context window, not just accept tokens without
benefiting from them.
```

**Gemini 1.5 Pro's performance on this benchmark** at 1M tokens showed near-perfect
retrieval at almost all positions — a significant milestone that demonstrated long
context can actually work at scale. However, retrieval is the easy case; reasoning
over information scattered across a long context remains a harder challenge.

---

## Efficient Attention Mechanisms

### Flash Attention 1, 2, 3 — IO-Aware Exact Attention

**Flash Attention** (Tri Dao, Stanford, 2022) is arguably the single most impactful
systems-level innovation in the transformer era. It made long-context training and
inference practical by solving the memory bottleneck of attention.

**The core problem:**

```
Standard Attention computation:

S = Q @ K^T          # [N, N] matrix — O(N²) memory!
P = softmax(S)       # [N, N] matrix — O(N²) memory!
O = P @ V            # [N, d] output

For N = 32,768 tokens in fp16:
  S matrix: 32768² × 2 bytes = 2 GB  (just for one head!)
  P matrix: another 2 GB
  Total for intermediate storage: 4 GB per attention head

This matrix must be written to GPU DRAM, then read back —
GPU DRAM bandwidth is the bottleneck, not compute.
```

**The GPU memory hierarchy insight:**

```
GPU Memory Hierarchy:
┌─────────────────────────────┐
│  Registers     ~100KB       │  Speed: ~100 TB/s
│  Per-thread, fastest        │
├─────────────────────────────┤
│  Shared Memory (SRAM)       │  Speed: ~20 TB/s
│  ~200KB per SM              │  (on-chip)
│  Shared across thread block │
├─────────────────────────────┤
│  L2 Cache     ~40MB         │  Speed: ~5 TB/s
│  Shared across all SMs      │
├─────────────────────────────┤
│  Global Memory (HBM/DRAM)   │  Speed: ~2 TB/s
│  40-80 GB (A100)            │  (off-chip — 10-50× slower!)
│  Where the N² matrix lives  │
└─────────────────────────────┘

Flash Attention's insight: Never materialize the N² matrix in HBM.
Compute everything in SRAM tiles, write only the final [N, d] output.
```

**How Flash Attention works (tiling + online softmax):**

```
Algorithm (simplified):

Divide Q into blocks of size B_r
Divide K, V into blocks of size B_c
Choose B_r, B_c so blocks fit in SRAM

For each Q block (row block i):
    Initialize: O_i = 0, l_i = 0, m_i = -∞

    For each KV block (column block j):
        # Load from HBM to SRAM
        Load Q_i, K_j, V_j into SRAM

        # Compute local attention in SRAM
        S_ij = Q_i @ K_j^T / √d      # [B_r, B_c] — fits in SRAM!

        # Online softmax update
        m_ij = rowmax(S_ij)
        m_new = max(m_i, m_ij)

        # Rescale previous results
        P_ij = exp(S_ij - m_new)
        l_new = exp(m_i - m_new) * l_i + rowsum(P_ij)
        O_i = exp(m_i - m_new) * O_i + P_ij @ V_j

        m_i = m_new
        l_i = l_new

    # Normalize
    O_i = O_i / l_i

    # Write final output to HBM
    Store O_i to output

Total HBM reads:  O(N²d / M)  where M = SRAM size
Total HBM writes: O(N × d)  — just the output!
vs. Standard: O(N² + N × d) reads AND writes
```

**Memory savings:**

```
                Standard       Flash Attention
Memory:         O(N²)          O(N)
HBM accesses:   O(N²)          O(N²d/M)  (M = SRAM)
Speed (A100):   baseline       2-4× faster
Max seq length:  ~8K (80GB)    ~64K (80GB)
```

### Why Flash Attention Was a Game-Changer

Flash Attention's impact went far beyond theoretical speedups:

1. **Enabled long context**: Before Flash Attention, 32K+ context was impractical on
   standard hardware. After, 128K became routine.

2. **Exact, not approximate**: Unlike Linformer, Performer, or other efficient attention
   variants, Flash Attention computes mathematically identical results to standard
   attention. No approximation trade-offs. Drop-in replacement.

3. **Training speedup**: 2-4× wall-clock speedup for attention, which is 30-50% of total
   training time → 15-25% overall training speedup for free.

4. **Backward pass too**: Flash Attention also optimizes the backward pass (gradient
   computation), recomputing attention on-the-fly instead of storing the O(N²) matrix
   for backpropagation.

**Flash Attention 2 improvements (2023):**

```
Key optimizations over Flash Attention 1:
1. Better parallelism: Parallelize over sequence length dimension
   (not just batch × heads), improving GPU occupancy
2. Reduced non-matmul FLOPs: Minimize overhead operations
3. Better warp scheduling: Reduce shared memory read/write conflicts
4. Support for variable-length sequences in a batch (no padding waste)

Result: 2× faster than Flash Attention 1 on A100
        Reaches 50-73% of theoretical max FLOPS (vs 25-40% for FA1)
```

**Flash Attention 3 improvements (2024):**

```
Targets Hopper architecture (H100 GPUs):
1. Exploits asynchronous execution: Overlaps data movement with
   computation using hardware-level async capabilities
2. FP8 quantized attention: Supports lower-precision computation
   for further speedup with minimal quality loss
3. Block quantization: Dynamic per-block scaling for numerical stability
4. Warp-specialized kernels: Different warps handle different tasks
   (data loading vs computation) simultaneously

Result: 1.5-2× faster than Flash Attention 2 on H100
        Approaching hardware theoretical limits
```

### Sparse Attention Patterns

Before Flash Attention proved that exact attention could be made efficient, the primary
approach to handling long sequences was **sparse attention** — limiting which tokens can
attend to which other tokens.

**Common sparse patterns:**

```
1. Local (Sliding Window) Attention:
   Each token attends only to its W nearest neighbors
   Complexity: O(N × W) instead of O(N²)

   Token i attends to: [max(0, i-W/2), min(N, i+W/2)]

   Used in: Mistral (window=4096), Longformer

2. Dilated Attention:
   Like local attention but with gaps
   Token i attends to: i-W, i-2W, i-3W, ... (every Wth token)
   Captures longer-range dependencies without full attention

3. Global + Local:
   Certain tokens (e.g., [CLS], first token) attend to everything
   All other tokens use local attention
   Provides an information highway through the sequence

   Longformer pattern:
   [Global]───────────────────────── (attends everywhere)
   [Local ]─────╮                     (attends to window)
   [Local ]─────┤
   [Local ]─────╯
   [Global]───────────────────────── (another global token)

4. Strided (Block) Attention:
   Divide sequence into blocks of size B
   Within-block: full attention
   Between-blocks: attend to summary tokens or stride patterns

5. BigBird Pattern:
   Combines local + global + random attention
   Random attention: each token attends to r random positions
   This ensures any two tokens are connected within O(1) attention
   hops, preserving theoretical expressiveness
```

**Why sparse attention lost to Flash Attention:**

```
Sparse attention advantages:
  - Truly reduces FLOPs (less computation)
  - O(N) or O(N√N) complexity

Sparse attention disadvantages:
  - Loses information: some token pairs never directly interact
  - Pattern design is task-dependent (one pattern doesn't fit all)
  - Implementation complexity (irregular memory access)
  - For moderate N (≤64K), Flash Attention's constant-factor speedup
    on exact attention is competitive with sparse attention's
    asymptotic advantages

Result: For N ≤ 128K, Flash Attention (exact) dominates.
        For N > 128K, hybrid approaches emerge:
          - Sliding window attention + sparse global attention
          - Flash Attention applied to each window/block
```

### Linear Attention Alternatives

A separate line of work attempts to replace softmax attention entirely with operations
that scale linearly in sequence length:

**The linearization idea:**

```
Standard attention:
  Attn(Q, K, V) = softmax(QK^T / √d) V

If we decompose softmax(QK^T) ≈ φ(Q) · φ(K)^T for some feature map φ:

  Attn(Q, K, V) ≈ φ(Q) · (φ(K)^T · V)

By associativity:
  Instead of: [N×N] @ [N×d] = O(N²d) operations
  Compute:    [d×d] matrix S = φ(K)^T @ V first  (O(Nd²))
  Then:       Output = φ(Q) @ S                   (O(Nd²))
  Total: O(Nd²) — linear in N!
```

**Key approaches:**

```
1. Performer (2020):
   φ(x) = exp(x) ≈ random_features(x)
   Uses FAVOR+ (Fast Attention Via Orthogonal Random features)
   Problem: Approximation quality degrades for sharp attention

2. Linear Transformers (2020):
   φ(x) = elu(x) + 1  (simple element-wise nonlinearity)
   Fast but often underperforms softmax attention

3. RetNet (2023):
   Combines linear attention with explicit exponential decay:
     y_n = Σ_{m≤n} γ^{n-m} · (Q_n · K_m^T) · V_m
   Supports three computation modes:
     - Parallel (like attention, for training)
     - Recurrent (like RNN, O(1) per step for inference)
     - Chunkwise (hybrid for long sequences)

4. Mamba / S4 (State Space Models):
   Not attention at all — uses structured state space equations:
     h_t = A·h_{t-1} + B·x_t    (state update, like an RNN)
     y_t = C·h_t + D·x_t        (output)

   Key innovation: A is structured (diagonal + low-rank) so the
   recurrence can be computed efficiently both sequentially AND
   in parallel (via a scan/prefix-sum).

   Complexity: O(N) for both training and inference
   Result: Competitive with Transformers on many tasks, especially
           for very long sequences where quadratic attention is
           prohibitive.
```

**The 2024 landscape:**

```
Architecture        | Quality  | Training | Inference | Long Context
--------------------|----------|----------|-----------|-------------
Softmax Attention   | Best     | O(N²)   | O(N²)    | Limited
+ Flash Attention   | Best     | O(N²)*  | O(N²)*   | Good (128K)
Sparse Attention    | Good     | O(N√N)  | O(N√N)   | Good
Linear Attention    | Fair     | O(N)    | O(N)     | Excellent
Mamba/SSM           | Good     | O(N)    | O(1)/step| Excellent
Hybrid (Attn+Mamba) | Very Good| Mixed   | Mixed    | Very Good

* Flash Attention: O(N²) FLOPs but optimized IO, so much faster
  wall-clock than standard O(N²)

Trend: Hybrid architectures combining a few full-attention layers
(for complex reasoning) with many linear/SSM layers (for efficiency)
are emerging as the best compromise.
```

---

## Document and Visual Understanding

### OCR-Free Document Understanding

Traditional document processing pipelines rely on OCR (Optical Character Recognition)
to extract text, then process the text with language models. This approach has fundamental
limitations:

```
Traditional Pipeline:
  Document Image → OCR Engine → Raw Text → NLP Model → Answer

Problems:
  1. OCR errors propagate: Misread characters corrupt downstream reasoning
  2. Layout lost: Tables, columns, headers, footers become flat text
  3. Visual elements ignored: Charts, logos, handwriting, stamps
  4. Language/script dependency: OCR needs per-language models
  5. Pipeline complexity: Multiple systems to maintain
```

**OCR-free models** process document images directly through vision encoders:

```
OCR-Free Pipeline:
  Document Image → Vision Encoder → Language Model → Answer

Advantages:
  1. No OCR error propagation
  2. Layout understanding is visual (columns, tables preserved)
  3. Charts, figures, handwriting handled naturally
  4. Language-agnostic (the vision encoder doesn't care about script)
  5. Single end-to-end model
```

**Key architectures for OCR-free document understanding:**

```
1. Donut (Document Understanding Transformer):
   - Swin Transformer encoder → BART text decoder
   - No OCR, no text detection — just image in, text out
   - Pre-trained on synthetic document rendering
   - Can read text, understand layout, extract key-value pairs

2. Pix2Struct:
   - ViT encoder with variable-resolution patching
   - Pre-trained by learning to parse web page screenshots → HTML
   - Effective for charts, tables, infographics, UI screenshots

3. Nougat (Neural Optical Understanding for Academic Documents):
   - Specialized for scientific documents
   - Converts PDF pages directly to LaTeX/markdown
   - Handles equations, tables, figures, references
   - Swin Transformer → mBART decoder

4. Modern VLMs (GPT-4V, Gemini, Claude 3):
   - General-purpose multimodal models that happen to be
     excellent at document understanding
   - Can process document images, understand layout, read text,
     reason about content — all in one model
   - Handle mixed-content pages (text + charts + tables + images)
```

### ColPali: Using Vision Models for Document Retrieval

**ColPali** (2024) represents a paradigm shift in document retrieval. Instead of the
traditional approach (OCR → text indexing → text retrieval), ColPali treats document
pages as images and uses vision-language models for retrieval.

**The traditional document retrieval pipeline:**

```
Indexing:
  PDF → OCR → Text chunks → Embedding model → Vector store

Querying:
  Query text → Embedding model → Nearest neighbor search → Results

Problems:
  - OCR errors corrupt the index
  - Layout information lost
  - Tables become garbled text
  - Charts and figures aren't indexed at all
  - Complex multi-column layouts break chunking
```

**ColPali's approach:**

```
Architecture: Vision Language Model + ColBERT-style late interaction

Indexing:
  Document page (image) → PaliGemma (ViT + LLM)
  → Per-patch embeddings stored (not a single vector!)

  Each page produces ~1024 patch embeddings
  These capture BOTH visual layout AND textual content

Querying:
  Query text → Same model → Per-token embeddings

  Late interaction scoring:
  score = Σ_i max_j (query_token_i · doc_patch_j)

  For each query token, find the most similar document patch,
  sum across all query tokens → final relevance score
```

**Why late interaction matters:**

```
Single-vector retrieval (bi-encoder):
  Document → one vector
  Query → one vector
  Score = dot_product(doc_vec, query_vec)

  Problem: One vector can't capture everything about a document
  A table, a paragraph, and a chart get merged into one embedding

Late interaction (ColPali):
  Document → many vectors (one per patch)
  Query → many vectors (one per token)
  Score = sum of best token-patch matches

  Advantage: Fine-grained matching
  Query "revenue in Q3" matches the specific table cell
  showing Q3 revenue, not just the overall page embedding
```

**Performance on document retrieval benchmarks:**

ColPali achieves state-of-the-art results while being simpler to deploy than traditional
pipelines. It eliminates the need for OCR, text extraction, layout analysis, and chunking
entirely. A single vision-language model handles everything.

### Table Understanding and Structured Extraction

Tables are one of the hardest challenges in document understanding. They combine spatial
layout (rows, columns, merged cells) with textual content and often numerical data that
requires precise extraction.

**Approaches to table understanding:**

```
1. Vision-based (OCR-free):
   - Treat table as an image region
   - Vision encoder captures row/column structure visually
   - Language model generates structured output (JSON, CSV, HTML)

   Example prompt: "Extract this table as JSON"
   Model sees the table image, outputs:
   {
     "headers": ["Quarter", "Revenue", "Growth"],
     "rows": [
       ["Q1 2024", "$12.3B", "15%"],
       ["Q2 2024", "$14.1B", "18%"],
       ...
     ]
   }

2. Layout-aware models:
   - LayoutLM family (Microsoft)
   - Input: text tokens + their 2D bounding box coordinates
   - The model learns position-aware representations
   - Can identify cell boundaries, headers, row/column associations

3. HTML reconstruction:
   - Models like Pix2Struct learn to generate HTML <table> markup
   - Preserves structure (colspan, rowspan, headers)
   - Output can be rendered or parsed programmatically

4. Hybrid approaches:
   - Use vision model for structure detection (row/col boundaries)
   - Use text model for content extraction within detected cells
   - Combine for accurate structured output
```

**The state of the art (2024):**

Modern vision-language models (GPT-4V, Gemini, Claude 3) can understand most tables
through their general multimodal capabilities. However, for high-precision extraction
at scale (e.g., processing millions of financial documents), specialized models like
Table Transformer, DETR-based table detectors, or fine-tuned document-specific VLMs
still outperform general-purpose models.

---

## Putting It All Together: The Multimodal Long-Context Stack

The full picture of a modern multimodal system combines all the components discussed:

```
Input Processing:
┌─────────────────────────────────────────────────┐
│  Text:  BPE Tokenizer    → [text tokens]        │
│  Image: ViT Patchifier   → [visual tokens]      │
│  Audio: Neural Codec     → [audio tokens]       │
│  Video: Frame × ViT      → [video tokens]       │
└─────────────┬───────────────────────────────────┘
              │
              ▼
Position Encoding:
┌─────────────────────────────────────────────────┐
│  RoPE (with YaRN/NTK extension for long context)│
│  Modality-specific position tokens               │
│  2D position encoding for images                 │
└─────────────┬───────────────────────────────────┘
              │
              ▼
Attention Computation:
┌─────────────────────────────────────────────────┐
│  Flash Attention (IO-aware, tiled, exact)        │
│  + Sliding window for very long sequences        │
│  + Ring Attention for multi-device               │
│  + KV cache for efficient autoregressive decode  │
└─────────────┬───────────────────────────────────┘
              │
              ▼
Transformer Backbone:
┌─────────────────────────────────────────────────┐
│  N layers of:                                    │
│    Multi-head self-attention                     │
│    (all modality tokens attend to each other)    │
│    Feed-forward network (SwiGLU)                 │
│    RMSNorm                                       │
│                                                  │
│  Every layer has been trained on mixed-modality  │
│  data from the start (native multimodal)         │
└─────────────┬───────────────────────────────────┘
              │
              ▼
Output Generation:
┌─────────────────────────────────────────────────┐
│  Text:  Next-token prediction → text             │
│  Audio: Audio token prediction → neural codec    │
│         decoder → waveform                       │
│  Image: (Some models) Image token prediction     │
│         → decoder → pixels                       │
└─────────────────────────────────────────────────┘
```

---

## Key Papers & Sources

### Foundational Vision-Language Papers
- **CLIP**: "Learning Transferable Visual Models From Natural Language Supervision" — Radford et al., OpenAI, 2021 — https://arxiv.org/abs/2103.00020
- **ViT**: "An Image is Worth 16x16 Words" — Dosovitskiy et al., Google, 2020 — https://arxiv.org/abs/2010.11929
- **LLaVA**: "Visual Instruction Tuning" — Liu et al., 2023 — https://arxiv.org/abs/2304.08485
- **LLaVA-1.5**: "Improved Baselines with Visual Instruction Tuning" — Liu et al., 2023 — https://arxiv.org/abs/2310.03744
- **Flamingo**: "A Visual Language Model for Few-Shot Learning" — Alayrac et al., DeepMind, 2022 — https://arxiv.org/abs/2204.14198
- **BLIP-2**: "Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models" — Li et al., Salesforce, 2023 — https://arxiv.org/abs/2301.12597
- **InternVL**: "Scaling Up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks" — Chen et al., 2023 — https://arxiv.org/abs/2312.14238
- **SigLIP**: "Sigmoid Loss for Language Image Pre-Training" — Zhai et al., Google, 2023 — https://arxiv.org/abs/2303.15343

### Native Multimodal Models
- **GPT-4 Technical Report** — OpenAI, 2023 — https://arxiv.org/abs/2303.08774
- **GPT-4o Announcement** — OpenAI, 2024 — https://openai.com/index/hello-gpt-4o/
- **Gemini Technical Report**: "Gemini: A Family of Highly Capable Multimodal Models" — Gemini Team, Google, 2023 — https://arxiv.org/abs/2312.11805
- **Gemini 1.5 Technical Report** — Gemini Team, Google, 2024 — https://arxiv.org/abs/2403.05530
- **CoCa**: "Contrastive Captioners are Image-Text Foundation Models" — Yu et al., Google, 2022 — https://arxiv.org/abs/2205.01917

### Audio and Speech
- **Whisper**: "Robust Speech Recognition via Large-Scale Weak Supervision" — Radford et al., OpenAI, 2022 — https://arxiv.org/abs/2212.04356
- **AudioLM**: "A Language Modeling Approach to Audio Generation" — Borsos et al., Google, 2022 — https://arxiv.org/abs/2209.03143
- **SoundStream**: "An End-to-End Neural Audio Codec" — Zeghidour et al., Google, 2021 — https://arxiv.org/abs/2107.03312
- **EnCodec**: "High Fidelity Neural Audio Compression" — Défossez et al., Meta, 2022 — https://arxiv.org/abs/2210.13438
- **VALL-E**: "Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers" — Wang et al., Microsoft, 2023 — https://arxiv.org/abs/2301.02111
- **MusicLM**: "Generating Music From Text" — Agostinelli et al., Google, 2023 — https://arxiv.org/abs/2301.11325

### Long Context and Position Encodings
- **RoPE / RoFormer**: "Enhanced Transformer with Rotary Position Embedding" — Su et al., 2021 — https://arxiv.org/abs/2104.09864
- **ALiBi**: "Train Short, Test Long: Attention with Linear Biases" — Press et al., 2021 — https://arxiv.org/abs/2108.12409
- **YaRN**: "YaRN: Efficient Context Window Extension of Large Language Models" — Peng et al., 2023 — https://arxiv.org/abs/2309.00071
- **Position Interpolation**: "Extending Context Window of Large Language Models via Positional Interpolation" — Chen et al., Meta, 2023 — https://arxiv.org/abs/2306.15595
- **Lost in the Middle**: "How Language Models Use Long Contexts" — Liu et al., Stanford, 2023 — https://arxiv.org/abs/2307.03172
- **Ring Attention**: "Ring Attention with Blockwise Transformers for Near-Infinite Context" — Liu et al., Berkeley, 2023 — https://arxiv.org/abs/2310.01889

### Efficient Attention
- **Flash Attention**: "Fast and Memory-Efficient Exact Attention with IO-Awareness" — Dao et al., Stanford, 2022 — https://arxiv.org/abs/2205.14135
- **Flash Attention 2**: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning" — Dao, 2023 — https://arxiv.org/abs/2307.08691
- **Flash Attention 3**: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision" — Shah et al., 2024 — https://arxiv.org/abs/2407.08691
- **Longformer**: "The Long-Document Transformer" — Beltagy et al., AI2, 2020 — https://arxiv.org/abs/2004.05150
- **BigBird**: "Transformers for Longer Sequences" — Zaheer et al., Google, 2020 — https://arxiv.org/abs/2007.14062
- **Mamba**: "Linear-Time Sequence Modeling with Selective State Spaces" — Gu & Dao, 2023 — https://arxiv.org/abs/2312.00752

### Document Understanding
- **ColPali**: "Efficient Document Retrieval with Vision Language Models" — Faysse et al., 2024 — https://arxiv.org/abs/2407.01449
- **Donut**: "OCR-free Document Understanding Transformer" — Kim et al., Naver, 2022 — https://arxiv.org/abs/2111.15664
- **Pix2Struct**: "Screenshot Parsing as Pretraining for Visual Language Understanding" — Lee et al., Google, 2023 — https://arxiv.org/abs/2210.03347
- **Nougat**: "Neural Optical Understanding for Academic Documents" — Blecher et al., Meta, 2023 — https://arxiv.org/abs/2308.13418
- **LayoutLM**: "Pre-training of Text and Layout for Document AI" — Xu et al., Microsoft, 2020 — https://arxiv.org/abs/1912.13318

---

## Concepts for Knowledge Tree

1. **Contrastive Learning** — Training by pushing matching pairs together and non-matching pairs apart in embedding space
2. **CLIP (Contrastive Language-Image Pre-training)** — Foundational model aligning images and text via contrastive loss
3. **InfoNCE Loss** — Contrastive loss function using softmax over positive/negative similarity scores
4. **Vision Transformer (ViT)** — Transformer architecture applied to image patches instead of text tokens
5. **Patch Embeddings** — Technique of splitting images into fixed patches and projecting to embedding vectors
6. **Visual Tokens** — Image patch representations treated as tokens in a language model's input sequence
7. **Visual Instruction Tuning** — Fine-tuning multimodal models on instruction-following data with images
8. **Perceiver Resampler** — Module that compresses variable-length visual features to fixed-size using learned queries
9. **Q-Former (Query Transformer)** — Learned query mechanism for bridging frozen vision encoders and frozen LLMs
10. **Early Fusion** — Combining modalities at input level, processing jointly through shared layers
11. **Late Fusion** — Processing modalities separately then combining at output or intermediate stages
12. **Cross-Attention Fusion** — Using attention mechanisms to let one modality attend to another's representations
13. **Native Multimodal** — Models pre-trained on all modalities simultaneously from the start
14. **Neural Audio Codec** — Neural network that compresses audio into discrete tokens (SoundStream, EnCodec)
15. **Residual Vector Quantization (RVQ)** — Hierarchical quantization producing multi-level discrete audio tokens
16. **AudioLM** — Language-modeling approach to audio generation using hierarchical token prediction
17. **RoPE (Rotary Position Embeddings)** — Position encoding via rotation of query/key vectors by position-dependent angles
18. **Position Interpolation** — Extending context by compressing position indices to fit within training range
19. **NTK-Aware Scaling** — Frequency-selective RoPE extension that scales low frequencies more than high frequencies
20. **YaRN** — Advanced RoPE extension combining NTK scaling with attention temperature correction
21. **ALiBi (Attention with Linear Biases)** — Position-free approach adding linear distance penalties to attention scores
22. **Ring Attention** — Distributed attention algorithm passing KV blocks around a ring of devices
23. **Online Softmax** — Technique for computing exact softmax incrementally over blocks without full materialization
24. **Lost in the Middle** — Empirical finding that LLMs poorly utilize information in the middle of long contexts
25. **Needle-in-a-Haystack** — Evaluation benchmark testing retrieval of specific facts from varying positions in long text
26. **Flash Attention** — IO-aware tiled attention algorithm computing exact attention without materializing N² matrices
27. **GPU Memory Hierarchy** — The SRAM/HBM speed gap that Flash Attention exploits for efficiency
28. **Sparse Attention** — Attention patterns restricting which token pairs interact (local, global, random)
29. **Sliding Window Attention** — Each token attends only to a fixed-size local window of neighboring tokens
30. **Linear Attention** — Approximation replacing softmax with kernel features for O(N) complexity
31. **State Space Models (SSMs / Mamba)** — Recurrence-based sequence models achieving linear complexity
32. **KV Cache** — Storing computed key-value pairs for efficient autoregressive generation
33. **OCR-Free Document Understanding** — Processing document images directly without text extraction
34. **ColPali** — Vision-based document retrieval using late interaction between patch and token embeddings
35. **Late Interaction Retrieval** — Scoring documents via fine-grained token-to-patch matching (MaxSim)
36. **Attention Sink** — Phenomenon where initial tokens receive disproportionate attention regardless of content
37. **Multimodal Tokenization** — Unified approach to converting text, images, and audio into a shared token space
38. **Full-Duplex Voice** — Real-time simultaneous audio input and output without turn-taking pipeline delays
