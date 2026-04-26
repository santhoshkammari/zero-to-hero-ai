# Findings: Frameworks — TensorFlow, Keras & JAX

## Key Research Insights

### TensorFlow vs PyTorch (2024-2025)
- PyTorch dominates research: most NeurIPS/ICML/CVPR papers since 2020 are PyTorch
- TF still huge in production/enterprise: TF Serving, TFLite, TF.js are battle-tested
- PyTorch 2.0 introduced torch.compile (Dynamo + Inductor) — closing the compilation gap
- TF2 added eager execution by default, but core identity remains graph-mode compilation
- HuggingFace ecosystem is PyTorch-first
- Companies like Meta, Tesla, Microsoft are PyTorch end-to-end now

### TensorFlow Graph Mode vs Eager Mode
- Eager: line-by-line like Python, great for debugging, slower
- Graph: @tf.function compiles computation graph, optimizes, fuses ops — production speed
- AutoGraph converts Python control flow (if/for) to graph ops — can surprise you
- The tension: debug in eager, deploy in graph. This dual-mode design caused years of confusion
- SavedModel format enables serialization for serving

### Keras 3 Multi-Backend (Major 2024 Development)
- Keras 3 is now truly backend-agnostic: runs on TF, PyTorch, OR JAX
- Set via KERAS_BACKEND environment variable
- Write once, run anywhere — but not all features equally supported across backends
- Separate pip package `keras` (not `tf.keras`)
- This is a big philosophical shift: Keras as universal high-level API

### JAX Core Concepts
- Built around pure functions: no hidden state, no mutation
- Four key transforms: grad, jit, vmap, pmap — composable
- jit: traces function → builds XLA computation graph → compiles to optimized code
- vmap: write for single example, auto-vectorize to batches
- pmap: parallelize across multiple devices (GPUs/TPUs)
- grad: returns a NEW function that computes gradients (not .backward())
- Transforms are composable: vmap(grad(jit(f))) works

### JAX Gotchas & Limitations
- Arrays are IMMUTABLE — no in-place mutation (x[0] = 5 doesn't work)
- No global PRNG state — must manually split and thread random keys
- Python control flow inside jit: must use jax.lax.cond, jax.lax.scan for data-dependent flow
- Tracing happens at first call per unique input signature; recompiles on new shapes
- Side effects (print, logging) inside jit'd functions don't work as expected
- Steep learning curve if coming from imperative/OOP background

### PyTrees in JAX
- Nested containers (dicts, lists, tuples) of arrays
- JAX transforms operate on entire pytrees — crucial for parameter management
- tree_util.tree_flatten / tree_unflatten for manipulation
- Model params are pytrees, gradients are pytrees with same structure

### Flax vs Equinox (JAX NN Libraries)
- Flax (Google): explicit Module class, params dict separated from model, production-ready
- Equinox (community): models are dataclasses/pytrees, native JAX patterns, minimal abstraction
- Flax: larger ecosystem, more docs, used in Google projects
- Equinox: preferred by researchers who want "pure JAX", used in cutting-edge work (Mamba, Neural ODEs)
- Optax: composable optimizer library for JAX (works with both)

### PyTorch 2.0 torch.compile
- TorchDynamo: frontend tracer, intercepts Python ops, builds IR graph
- TorchInductor: backend compiler, uses Triton for GPU codegen
- "Graph breaks" allow fallback to eager mode for unsupported Python
- Much more forgiving than JAX jit — handles dynamic shapes, complex Python
- Closing the performance gap with JAX/XLA

### Framework Selection Mental Model
- PyTorch: default choice, research + increasingly production
- TF/Keras: existing production systems, mobile/edge (TFLite), quick prototyping
- JAX: Google/DeepMind ecosystem, TPU workloads, custom differentiation, research needing composable transforms
- The underlying ML concepts are identical — switching is syntax, not fundamentals

### Interview-Depth Insights
- "Why does JAX require pure functions?" — enables safe composition of transforms
- "What's the difference between eager and graph execution?" — debugging vs performance tradeoff
- "When would you choose TF over PyTorch?" — existing infra, TFLite mobile, TF Serving
- "What problem does torch.compile solve?" — bridges eager debugging with compiled performance
- "What are pytrees?" — JAX's way of handling nested parameter structures
- "How does Keras 3 differ from tf.keras?" — multi-backend, framework-agnostic
