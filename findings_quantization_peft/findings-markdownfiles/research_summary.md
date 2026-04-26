# Research Summary: Quantization & PEFT

## Key Insights from Research

### LoRA
- Weight updates during fine-tuning have very low intrinsic rank (Aghajanyan et al., "Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning")
- Intrinsic dimensionality of fine-tuning is often just a few hundred to a few thousand, vs millions of parameters
- Ship/rudder analogy: you don't redesign the whole ship, you turn the rudder
- Rank 16 is the practical sweet spot for most tasks
- LoRA alpha/r = effective scaling factor; alpha = 2*r is common
- A initialized Gaussian, B initialized to zero → BA = 0 at start (no perturbation)
- Can merge BA back into W for zero inference overhead

### Quantization Methods
- GPTQ: Hessian-based, +0.2-0.5 perplexity vs FP16, GPU-first
- AWQ: Activation-aware, +0.1-0.4 perplexity, slightly better quality
- GGUF: Container format for llama.cpp, CPU-first, Q4_K_M is sweet spot
- SmoothQuant: Migrates quantization difficulty from activations to weights, enables W8A8

### QLoRA
- NF4: Non-uniform 4-bit levels matching Gaussian distribution of weights
- Double quantization: Quantize the scale factors themselves to 8-bit
- Paged optimizers: CUDA unified memory for optimizer state overflow
- Matches full 16-bit fine-tuning quality (surprising result)

### Other PEFT Methods
- Adapters: Bottleneck layers between transformer layers, add inference latency
- Prefix tuning: Virtual KV pairs prepended to each attention layer
- Prompt tuning: Soft prompt embeddings at input only
- IA3: Learned scaling vectors for K, V, FFN activations

### Latest Developments (2024)
- EfficientQAT: 2-bit Llama2-70B on single A100
- BitNet: 1-bit LLMs feasible with specialized training
- LLM-QAT: Data-free QAT using self-generated data
- INT4 QAT recovering 96% of PTQ-induced accuracy loss
