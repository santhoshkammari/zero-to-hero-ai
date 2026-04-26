# GPU Landscape Research

## Key GPUs for ML (2024)
- **T4**: 16GB VRAM, 65 FP16 TFLOPS, $0.50-1/hr. Budget inference, small fine-tunes
- **L4**: 24GB VRAM, 121 FP16 TFLOPS, Ada Lovelace arch. Inference sweet spot
- **A100 80GB**: 80GB HBM2e, 312 TF32 TFLOPS, 2039 GB/s bandwidth. Training workhorse
- **H100 SXM**: 80GB HBM3, 989 TF32 TFLOPS, 3350 GB/s bandwidth, FP8 support. Frontier
- **B200**: 192GB HBM3e, ~2250 TFLOPS. Next-gen

## Key Insight
- H100 trains 12x faster and 86% cheaper per million tokens than A100
- Memory bandwidth often more important than raw TFLOPS for LLM inference
- NVLink: 900 GB/s (H100), InfiniBand: 50-100 GB/s, PCIe: 64 GB/s

## VRAM Math
- FP16: 2 bytes/param, FP32: 4 bytes, INT8: 1 byte, INT4: 0.5 byte
- Training overhead: weights + gradients + optimizer states (Adam: 2x FP32 copies)
- 7B model FP16 inference: ~14GB, Training: ~105GB

## Cloud vs On-prem break-even
- >40-50% GPU utilization over 3+ years: on-prem wins
- <40% or bursty: cloud wins
- H100 costs ~$30-40K, full server $50-100K
- Cloud H100: ~$4-12/hr depending on provider and commitment
