# Findings: PyTorch Training (ch08/s03)

## Research Summary

### 1. Autograd Internals
- Tape-based reverse-mode autodiff: operations recorded as they execute (define-by-run)
- Every Tensor has a `grad_fn` pointing to the Function that created it
- Function objects store context via `ctx.save_for_backward()` — only what's needed for backward
- Graph is ephemeral: built during forward, consumed/freed during `.backward()` (unless retain_graph=True)
- Leaf tensors (user-created with requires_grad=True) accumulate gradients in `.grad`
- Non-leaf tensors: gradients computed but NOT stored by default (use `.retain_grad()` or hooks)
- `create_graph=True` enables higher-order gradients (graph of the backward pass itself)
- In-place operations can corrupt autograd: "modified by an inplace operation" RuntimeError

### 2. DataLoader Deep Dive
- Multiprocessing: workers use shared memory queues, each calls `__getitem__` independently
- `prefetch_factor` (default 2): each worker prefetches this many batches ahead
- `persistent_workers=True`: avoids re-spawning workers each epoch (saves 5-15s per epoch)
- `pin_memory=True`: allocates page-locked memory for faster CPU→GPU async transfer via `cuda.Stream`
- Collation: `collate_fn` controls how samples become a batch — default stacks tensors
- IterableDataset vs map-style Dataset: former for streaming data, latter for random access
- `worker_init_fn`: critical for setting different random seeds per worker (otherwise identical augmentations)
- On Windows: num_workers>0 requires `if __name__ == '__main__'` guard

### 3. torch.compile (PyTorch 2.0+)
- TorchDynamo: Python-level JIT tracer, hooks into CPython bytecode frames
- Captures FX graph of PyTorch operations, falls back to eager for unsupported Python constructs
- TorchInductor: compiler backend that generates optimized Triton kernels (GPU) or C++ (CPU)
- Key optimizations: operator fusion, kernel generation, memory planning
- Modes: "default" (safe), "reduce-overhead" (CUDA graphs), "max-autotune" (benchmarks multiple kernels)
- Graph breaks: when Dynamo can't trace through Python code, splits into subgraphs
- Typical speedup: 15-40% on standard models, more on memory-bound workloads

### 4. Distributed Training (DDP & FSDP)
- DDP: full model replica per GPU, gradient all-reduce via NCCL ring algorithm
- Bucketization: gradients grouped into buckets, all-reduce overlaps with backward computation
- FSDP: shards parameters, gradients, AND optimizer states across GPUs
- FSDP enables training models that don't fit in single GPU memory
- DDP: simpler, use when model fits in GPU memory
- FSDP: complex but memory-efficient, use for billion+ parameter models
- torch.distributed.launch → torchrun (elastic launch, fault tolerance)

### 5. Mixed Precision (AMP)
- autocast: dispatcher-level hook that routes ops to float16/bfloat16 when safe
- Safe ops (matmul, conv) → lower precision; risky ops (softmax, loss) → float32
- GradScaler: dynamic loss scaling to prevent float16 gradient underflow
- Scale up loss → larger gradients → scale down before optimizer step
- If inf/nan detected: skip optimizer step, reduce scale factor
- bfloat16 vs float16: bfloat16 has same exponent range as float32, less mantissa precision
- bfloat16 often doesn't need GradScaler (wider dynamic range)
- On Ampere+ GPUs, bfloat16 is preferred for training stability

### 6. nn.Module Internals
- `__setattr__` overridden: detects nn.Parameter and nn.Module assignments, registers them
- `_parameters`, `_buffers`, `_modules`: internal OrderedDicts
- `register_buffer`: non-trainable state (e.g., BatchNorm running_mean) — saved in state_dict, moves with .to()
- `register_parameter`: explicit parameter registration (rare, usually just assign nn.Parameter)
- Hooks: forward_hook, forward_pre_hook, full_backward_hook — for debugging, feature extraction, gradient modification
- `state_dict()`: recursively gathers all parameters + buffers as OrderedDict
- `load_state_dict(strict=False)`: allows partial loading (useful for transfer learning)

### 7. Gradient Checkpointing
- Trade compute for memory: don't store intermediate activations, recompute during backward
- `torch.utils.checkpoint.checkpoint(fn, *args)`: wraps a function for checkpointing
- Typically applied per transformer block or per residual block
- Reduces activation memory from O(N) to O(sqrt(N)) for N layers
- Must ensure checkpointed function is deterministic (no dropout with different seeds on recompute)

### 8. Interview-Depth Topics
- Why zero_grad before forward (not after backward)? Convention, but both work
- retain_graph=True: when you need multiple backward passes from same graph (e.g., GAN training)
- create_graph=True: for computing gradients of gradients (e.g., MAML, penalty terms)
- In-place operations and autograd: can corrupt saved tensors needed for backward
- Difference between .detach() and .data: .detach() is safe, .data bypasses autograd (dangerous)
- Why CrossEntropyLoss takes logits not probabilities: numerical stability (LogSumExp trick)
- model.train() vs model.eval(): only affects Dropout and BatchNorm, NOT gradient computation

### 9. Lightning & Higher-Level Abstractions
- Lightning: structured wrapper, separates research code from engineering boilerplate
- Key benefit: multi-GPU/TPU with single flag change
- Key drawback: abstraction makes debugging harder, lag behind cutting-edge PyTorch features
- Fabric (Lightning Lite): lighter wrapper, more control than full Lightning
- Modern trend: many teams use raw PyTorch + custom utilities rather than full Lightning
