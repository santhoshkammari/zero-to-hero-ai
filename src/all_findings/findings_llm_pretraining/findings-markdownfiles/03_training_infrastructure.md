# Training Infrastructure

## GPU Clusters
- H100: NVLink 4.0, 900 GB/s bidirectional per GPU
- DGX H100: 8 GPUs connected via NVLink mesh + NVSwitch
- Inter-node: InfiniBand 400 Gbps (HDR/NDR), ~1-2μs latency, RDMA
- Fat-tree or Dragonfly topologies

## 3D Parallelism
- TP (Tensor Parallelism): within node, NVLink — splits weight matrices
- PP (Pipeline Parallelism): across few nodes — splits layers
- DP/FSDP: across many nodes — data parallel replicas
- Example: LLaMA-70B on 256 GPUs: TP=8 × PP=4 × DP=8

## Training Stability
- Loss spikes: bad data batches, LR too high, numerical instability
- PaLM approach: rollback to checkpoint ~100 steps before spike, skip bad batches
- Checkpoint averaging: average weights from last 5-20 checkpoints
- Gradient clipping (global norm 1.0)
- QK-Norm, z-loss, BF16 over FP16

## Tokenizer Training at Scale
- BPE via SentencePiece or tiktoken
- Typical vocab: 32k-128k tokens
- LLaMA-2: 32k SentencePiece BPE
- GPT-4: 100k tiktoken
- Larger vocab → fewer tokens per sequence but larger embedding layer
