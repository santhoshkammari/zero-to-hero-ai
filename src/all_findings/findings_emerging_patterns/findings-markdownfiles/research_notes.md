# Emerging Patterns Research Notes

## Multimodal
- GPT-4V: vision encoder → projection → LLM (late fusion)
- Gemini: natively multimodal, all modalities tokenized into shared space (early fusion)
- Key distinction: modular (encoder+projection+LLM) vs unified (single transformer, shared tokens)

## Small Language Models
- Phi-2 (2.7B) matched models 10-25x size
- Phi-3 Mini (3.8B) competitive with GPT-3.5
- Gemma family (2B, 7B) by Google
- Key insight: data quality >> parameter count ("textbook-quality" synthetic data, curriculum learning)

## Model Merging
- Model Soups (2022): average weights from multiple checkpoints
- TIES-Merging: resolves sign conflicts in task vectors, trims redundant deltas, averages remaining
- DARE: randomly drops delta parameters (sets to zero) and rescales remaining, then merges
- Task vectors: θ_merged = θ_base + λ(θ_finetuned - θ_base) for each model
- No retraining needed - combine capabilities post-hoc

## Synthetic Data & Distillation
- Teacher-student: large model generates training data for small model
- Self-play / self-consistency for quality
- Model collapse: recursive self-training degrades diversity
- Mitigation: periodic real data injection, diversity enforcement

## World Models
- Yann LeCun's JEPA: predict future latent representations, not pixels
- Planning via internal simulation
- Sora (OpenAI) as world simulator through video generation

## Continual Learning / Catastrophic Forgetting
- EWC, SI: regularization-based (constrain important weights)
- Replay buffers: store/generate old data
- Parameter isolation: adapters per task
- LoRA/adapters naturally isolate task knowledge

## Federated Learning for LLMs
- Train across distributed devices, data never leaves device
- FedAvg + regularization
- Challenges: heterogeneous data, communication cost
- Privacy-preserving fine-tuning with LoRA

## On-Device AI
- Models like Phi-3 Mini run on phones/laptops
- Quantization (4-bit) critical for fitting in device RAM
- NPU/TPU hardware acceleration
- Hybrid: on-device for speed/privacy, cloud for capability

## Open Source Ecosystem
- Llama 3, Mistral/Mixtral, Qwen, DeepSeek
- Community: Hugging Face hub, vLLM, GGUF, llama.cpp
- Open eval: LMSYS Chatbot Arena, Open LLM Leaderboard
- Closing gap with closed models rapidly
