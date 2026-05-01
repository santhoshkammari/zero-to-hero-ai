# Mixed Precision Training

## Core Idea
- Forward/backward in fp16/bf16 (fast, less memory)
- Weight master copy + accumulation in fp32 (accurate)
- ~2x memory savings, 1.5-3x speedup on tensor cores

## Loss Scaling
- float16 smallest normal: ~6e-5
- Small gradients underflow to 0 → model stops learning
- Solution: multiply loss by large constant before backward
- All gradients scale up into representable range
- Divide by same constant before weight update
- Dynamic scaling: increase on clean steps, decrease on overflow

## bfloat16 vs float16
- float16: 5 exp bits, 10 mantissa — good precision, limited range
- bfloat16: 8 exp bits, 7 mantissa — less precision, same range as fp32
- bfloat16 rarely overflows/underflows → loss scaling often unnecessary
- Google TPUs, NVIDIA A100+ all support bfloat16 natively

## FP8 (2024)
- E4M3 and E5M2 formats
- NVIDIA Hopper (H100) native support
- Up to 4x throughput vs fp16
- Minimal accuracy loss with proper scaling

## Tensor Cores
- Specialized hardware for small matrix multiplies (4x4, 8x8)
- Mixed precision: multiply in fp16, accumulate in fp32
- 2-8x throughput vs standard CUDA cores
- Shapes must be multiples of 8/16 for best performance
