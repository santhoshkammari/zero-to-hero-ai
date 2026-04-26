# LLM Serving & Inference Research Summary

## KV Cache
- Per token: L × H × D × 2 × bytes_per_element
- Llama-2 70B: 80 layers × 64 heads × 128 dim × 2 × 2 bytes = ~2.6MB per token
- For 4096 seq len: ~10GB KV cache alone
- Prefill = compute-bound (process all prompt tokens), Decode = memory-bandwidth-bound

## Continuous Batching
- Orca paper introduced iteration-level scheduling
- Static batching: must wait for longest sequence in batch
- Continuous: requests join/leave mid-batch, 10-23x throughput improvement

## PagedAttention (vLLM)
- Maps OS virtual memory concepts to KV cache
- Fixed-size blocks (pages), non-contiguous allocation
- Near-zero memory waste, enables prefix caching
- Sequence maps to list of physical pages

## Speculative Decoding
- Small draft model generates K candidate tokens fast
- Large target model verifies all K tokens in single forward pass
- Accept tokens matching target distribution, reject and resample on mismatch
- 2-3x speedup, output distribution identical to target model

## Tensor Parallelism
- Column parallel: split weight columns across GPUs, concat outputs
- Row parallel: split weight rows, all-reduce sum outputs
- Q/K/V projections: column parallel (each GPU gets subset of heads)
- FFN: combination of column and row parallel

## Serving Frameworks
- vLLM: PagedAttention, continuous batching, OpenAI-compatible API, Python
- TensorRT-LLM: NVIDIA optimized C++/CUDA, fastest on NVIDIA hardware, complex setup
- TGI: HuggingFace, Rust, easy deployment, broad model support
- SGLang: structured generation, JSON schema enforcement, programmable
- Ollama: local deployment, llama.cpp backend, GGUF format, consumer hardware

## Cost Economics
- API: ~$0.01-0.03/1K tokens (GPT-4 class)
- Self-hosted A100: ~$0.015-0.02/1K tokens
- Tipping point: high sustained volume favors self-hosted
- Model cascading: route easy queries to small model, hard to large

## Streaming & API Design
- SSE (Server-Sent Events) for token-by-token delivery
- OpenAI-compatible API format is de facto standard
- Guardrails: rate limiting, input validation, output filtering, timeouts

## Key Metrics
- TTFT: Time to First Token (prefill latency)
- TPOT: Time Per Output Token (decode latency)
- Throughput: tokens/second across all concurrent requests
