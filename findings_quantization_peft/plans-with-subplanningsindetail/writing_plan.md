# Writing Plan: Efficient LLMs — Quantization & PEFT

## Opening (Phase 1)
- Personal confession: avoided quantization, treated models as sacred, finally GPU OOM forced the issue
- Orientation: what quantization and PEFT are, when they emerged
- Heads-up: we'll touch on linear algebra and some training concepts, but build from scratch
- Journey invitation

## Running Example
- A sentiment classifier startup scenario: you've fine-tuned a 7B model but need to deploy it on a single 24GB GPU, then a laptop, then customize it for 50 different clients
- Start with a tiny weight matrix (4×4) to show quantization mechanics
- Thread this through every section

## Concept Ladder (dependency order)
1. Why numbers have sizes (FP32 → FP16 → INT8 → INT4) — the memory math
2. The rounding problem — what quantization actually does to a number
3. Symmetric vs asymmetric quantization (toy example with 8 values)
4. Granularity: per-tensor → per-channel → per-group
5. Post-training quantization: GPTQ, AWQ, GGUF
6. SmoothQuant: taming activation outliers
7. Quantization-aware training
8. **REST STOP** — you can now shrink models, but what about customizing them?
9. The fine-tuning memory wall
10. LoRA: the low-rank insight (toy matrix example)
11. LoRA math, initialization, scaling, rank selection
12. QLoRA: NF4 + LoRA = magic
13. Other PEFT methods: adapters, prefix tuning, prompt tuning, IA3
14. When to use which method — decision guide
15. Wrap-up

## Analogies (recurring)
1. **Packing for a trip** — FP32 is bringing your entire wardrobe, INT4 is a carry-on with carefully chosen outfits. Recurs when discussing quality tradeoffs.
2. **Renovating a house** — Full fine-tuning = tear down and rebuild. LoRA = new paint and fixtures on solid structure. Recurs with QLoRA and adapters.

## Vulnerability Moments
1. Opening: avoided quantization, felt like mutilating a model
2. Quantization section: "I still don't have perfect intuition for why group-128 works so well"
3. LoRA section: "When I first saw the rank decomposition, I didn't believe it could work"
4. QLoRA section: "The fact that 4-bit base weights give good enough gradients still surprises me"
5. Decision guide: "I've gotten this wrong more times than I'd like to admit"

## Rest Stop Placement
- After quantization methods (before PEFT) — reader now knows how to shrink models
