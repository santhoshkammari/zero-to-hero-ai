# SSM & Mamba Research Summary

## Key Concepts to Cover

### 1. Classical State Space Models
- Continuous-time ODE: x'(t) = Ax(t) + Bu(t), y(t) = Cx(t) + Du(t)
- From control theory (70+ years), satellite tracking, thermostats, autopilots
- x(t) = hidden state (system memory), u(t) = input, y(t) = output
- A governs dynamics, B maps input→state, C maps state→output, D skip connection

### 2. Discretization
- Zero-order hold (ZOH): assume input constant between samples
- A_d = exp(AΔt), B_d = (integral of exp(Aτ))B
- Bilinear transform alternative
- Result: x_k = Ā x_{k-1} + B̄ u_k — looks like an RNN!

### 3. Convolution-Recurrence Duality
- Unrolling the recurrence reveals a convolution kernel: K = (CB̄, CĀB̄, CĀ²B̄, ...)
- Training: use convolution → parallel, O(n log n) via FFT
- Inference: use recurrence → sequential, O(1) per step
- Best of both worlds vs RNN (sequential training) and Transformer (O(n²))

### 4. HiPPO Framework
- High-order Polynomial Projection Operator
- Projects input history onto orthogonal polynomials (Legendre)
- Optimal compression of entire history into fixed-size state
- Specific matrix A that provably remembers long history
- Each coefficient captures independent information

### 5. S4 (Structured State Spaces)
- Exploits HiPPO matrix structure (low-rank-plus-diagonal)
- Efficient computation via Cauchy kernel connection
- SOTA on Long Range Arena benchmark (1K-16K tokens)
- Limitation: A, B, C matrices are FIXED — no content-based selection

### 6. Mamba (Selective SSM)
- Key innovation: B, C, Δ become functions of input
- B_k = Linear(u_k), C_k = Linear(u_k), Δ_k = softplus(Linear(u_k))
- Large Δ → write strongly to state (remember), small Δ → barely update (forget)
- Content-based filtering like attention but O(n)
- Breaks convolution trick (kernel no longer fixed)
- Hardware-aware parallel scan: tiling for GPU SRAM, fused kernels

### 7. Mamba-2 (SSD)
- Structured State Space Duality
- Mathematical equivalence: linear attention ≈ SSM under specific parameterizations
- Faster, simpler implementation
- Unifies SSM and attention theory

### 8. Hybrid Architectures
- Jamba (AI21 Labs): Mamba + Transformer + MoE
- 52B params, ~12B active, 256K context
- ~1 attention layer per 7 Mamba layers
- Attention for precise retrieval, SSM for compression
- Griffin/Hawk (DeepMind), RWKV (linear attention)

### Running Example Idea
- Temperature monitoring system: sensor readings over time
- Simple: 4 sensors, predict next reading
- Scales: to thousands of sensors, long time horizons
- Natural for control theory origin story
