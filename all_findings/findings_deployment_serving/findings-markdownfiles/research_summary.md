# Deployment & Serving Research Summary

## Key Insights from Research

### Model Serialization
- ONNX: universal interchange, opset 17-19 recommended, use onnx-simplifier post-export
- TorchScript: trace vs script tradeoffs, being superseded by torch.compile + torch.export
- SavedModel: TF ecosystem only, tight integration with TF Serving/TFLite/TF.js
- GGUF: llama.cpp format for CPU/laptop LLM inference

### Serving Frameworks
- Triton: multi-model multi-framework GPU sharing via CUDA streams, dynamic batching
- TorchServe: PyTorch native, .mar packaging, built-in batching
- TF Serving: mature, battle-tested, TF only
- BentoML: framework-agnostic, builds containers from Python service definitions
- vLLM: PagedAttention, continuous batching for LLMs specifically

### Edge Deployment
- TFLite: best on Android (NNAPI), INT8/FP16 quantization
- CoreML: fastest on iOS (Neural Engine), deep Apple HW integration
- ONNX Runtime Mobile: cross-platform, uses NNAPI/CoreML delegates

### Optimization
- Quantization: PTQ (easy, ~0-1% accuracy loss), QAT (harder, recovers accuracy)
- Pruning: unstructured (high compression, needs sparse HW) vs structured (works everywhere)
- Distillation: DistilBERT 40% smaller 60% faster 97% accuracy; TinyBERT 7.5x compression
- Compilation: TensorRT 2-6x, ONNX Runtime 2-3x, torch.compile 1.5-3x

### Scaling & Deployment Strategies
- HPA with custom GPU metrics (DCGM exporter + Prometheus adapter)
- KEDA for event-driven scaling
- Canary (safety), Blue-Green (instant rollback), Shadow (zero-risk testing), A/B (business impact)
- Circuit breakers, least-connections load balancing for ML
