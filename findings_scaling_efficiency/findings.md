# Scaling & Efficiency — Research Findings

## 1. GPU Fundamentals & VRAM Budget
- GPUs: thousands of simple cores vs CPU's few powerful cores. DL = matrix multiply = embarrassingly parallel.
- VRAM holds: parameters, gradients, optimizer states (Adam = 2× params), activations, temp buffers.
- VRAM formula for mixed-precision Adam training: ~16-20 bytes per parameter (before activations).
- 1B model in FP16+Adam: ~18-24 GB. 7B model: ~130-140 GB minimum.
- OOM fixes priority: reduce batch size → mixed precision → gradient accumulation → gradient checkpointing.

## 2. Data Parallelism: DP vs DDP
- DataParallel (DP): single process, GIL bottleneck, asymmetric GPU 0 memory, never use.
- DistributedDataParallel (DDP): one process per GPU, ring all-reduce via NCCL, gradient bucketing (25MB default), communication overlaps backward pass.
- Ring all-reduce: N workers in ring, each sends 2*(N-1)/N of tensor size total. Bandwidth-optimal.
- Gradient bucketing: groups small gradients into buckets, triggers all-reduce per bucket as backward completes layers. Overlaps comm with compute.
- Near-linear scaling: 4 GPUs ≈ 3.6-3.9× throughput.
- Key gotchas: DistributedSampler, sampler.set_epoch(), log/save only on rank 0, SyncBatchNorm, torchrun launcher.

## 3. FSDP & DeepSpeed ZeRO
- ZeRO Stage 1: shard optimizer states → per-GPU = P + G + O/N
- ZeRO Stage 2: + shard gradients → per-GPU = P + G/N + O/N
- ZeRO Stage 3 / FSDP: + shard parameters → per-GPU = P/N + G/N + O/N
- ZeRO-Infinity: offload to CPU/NVMe, theoretically unlimited model size.
- FSDP: native PyTorch, simpler setup, great for ≤32 GPUs. DeepSpeed ZeRO-3: better at massive scale (64+ GPUs), more config.
- Tradeoff: more sharding = more communication overhead. Use lowest stage that fits.

## 4. Model Parallelism: Tensor & Pipeline
- Tensor Parallelism: split individual layer computation across GPUs. E.g., split large matmul so each GPU computes portion. Needs high-bandwidth interconnect (NVLink).
- Pipeline Parallelism: assign layer groups to different GPUs. Data flows through pipeline. Challenge: pipeline bubbles (GPU idle time). Micro-batching reduces but doesn't eliminate bubbles.
- 3D Parallelism (Megatron-LM style): data × tensor × pipeline. E.g., 64 GPUs = 4 data × 4 pipeline × 4 tensor.

## 5. Scaling Laws (Kaplan & Chinchilla)
- Kaplan (2020): L(N,D) ≈ L∞ + k_N·N^(-α) + k_D·D^(-β). Loss decreases as power law with model size and data.
- Chinchilla (2022): For fixed compute C, optimal tokens D* ≈ 20N. C = 6ND. Most models were undertrained.
- Practical: don't make model bigger without proportionally more data. Compute-optimal = balanced N and D.

## 6. Memory Optimization Techniques
- Mixed Precision: FP16/BF16 forward+backward, FP32 master weights. ~2× speedup, ~40% less memory.
- BF16 vs FP16: BF16 has same exponent range as FP32 (no loss scaling needed). FP16 needs GradScaler. Use BF16 on A100+.
- Gradient Accumulation: simulate larger batch by accumulating gradients over K micro-batches before optimizer step. Memory of small batch, effective batch of K× larger.
- Gradient Checkpointing: don't store all activations; recompute during backward. Memory O(√N) for N layers. ~30% compute overhead.
- Flash Attention: IO-aware tiling. Keeps computation in fast SRAM, avoids materializing N×N attention matrix in HBM. Exact (not approximate). O(Nd) memory vs O(N²).

## 7. Compute Efficiency & Tooling
- torch.compile: JIT compilation with operator fusion, kernel optimization. Can give 20-50% speedup.
- FP8 training (H100 Transformer Engine): next frontier, 2× over BF16 for supported ops.
- Experiment tracking: W&B, MLflow, TensorBoard. Track from day 1.
- Cloud GPU landscape: AWS (p5/H100), GCP (A3/H100, TPUs), Azure, Lambda Labs, RunPod.

## 8. Interview-Depth Topics
- "Why not DataParallel?" → GIL, asymmetric memory, poor scaling.
- "Estimate VRAM for 7B model" → 7B × ~18 bytes = ~126 GB + activations.
- "When FSDP vs DDP?" → Model fits one GPU? DDP. Doesn't fit? FSDP. Massive scale? DeepSpeed ZeRO-3.
- "What are scaling laws?" → Power law loss decay. Chinchilla: 20 tokens per parameter is compute-optimal.
- "How does gradient checkpointing work?" → Trade compute for memory by recomputing activations.
- "Flash Attention vs standard attention?" → IO-aware tiling in SRAM, no N×N materialization, exact same output.
