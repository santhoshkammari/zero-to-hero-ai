# Missing Topics: Ch07 Deep Learning Foundations

Now I have everything I need. Here is my comprehensive analysis:

---

## Summary

Chapter 7 "Deep Learning Foundations" already has solid coverage of many core topics. The **neural-network-basics.html** covers activation functions (ReLU, Leaky ReLU, PReLU, GELU, Swish, Sigmoid, Tanh, Softmax), Xavier/He initialization, and the Universal Approximation Theorem. The **training-stability.html** covers vanishing/exploding gradients, Xavier/Glorot and He/Kaiming initialization, batch/layer normalization, residual connections, gradient clipping, and dead neurons. The **nice-to-know.html** covers UAT, Lottery Ticket Hypothesis, Double Descent, Grokking, Knowledge Distillation, Loss Landscape, Hopfield Networks, Neural Tangent Kernel, NAS, BPTT, and Focal Loss. The **emerging-methods.html** covers scaling laws, test-time training, meta-learning, continual learning, neurosymbolic AI, geometric deep learning, TDA, and quantum ML.

Additionally, **Chapter 8** (training-techniques section) covers Dropout theory, weight decay, label smoothing, Mixup/CutMix, early stopping, DropPath/stochastic depth, gradient management. **Chapter 9** covers DenseNet, ResNet, Squeeze-and-Excitation blocks, and architecture evolution.

### What IS covered (cross-chapter):
- ✅ Activation functions: ReLU, Leaky ReLU, PReLU (mentioned), ELU (mentioned), GELU, Swish — in `ch07/neural-network-basics.html`
- ✅ Weight initialization: Xavier/Glorot, He/Kaiming — in `ch07/neural-network-basics.html` + `ch07/training-stability.html`
- ✅ Universal Approximation Theorem — in `ch07/neural-network-basics.html` + `ch07/nice-to-know.html`
- ✅ Vanishing/Exploding gradients — in `ch07/backpropagation.html` + `ch07/training-stability.html`
- ✅ Skip connections / ResNet theory — in `ch07/training-stability.html` + `ch09/architecture-evolution.html`
- ✅ DenseNet — in `ch09/architecture-evolution.html`
- ✅ Squeeze-and-Excitation — in `ch09/nice-to-know.html`
- ✅ Dropout theory — in `ch08/training-techniques.html` (3 interpretations)
- ✅ Stochastic depth / DropPath — in `ch08/training-techniques.html`
- ✅ Mixup, CutMix — in `ch08/training-techniques.html`
- ✅ Lottery Ticket Hypothesis — in `ch07/nice-to-know.html`
- ✅ Double Descent — in `ch07/nice-to-know.html`
- ✅ Neural Tangent Kernel — in `ch07/nice-to-know.html`
- ✅ Knowledge Distillation — in `ch07/nice-to-know.html` + `ch08/nice-to-know.html`
- ✅ Hopfield Networks (and mention of Boltzmann machines) — in `ch07/nice-to-know.html`
- ✅ Loss Landscape — in `ch07/nice-to-know.html`
- ✅ NAS — in `ch07/nice-to-know.html`
- ✅ Batch/Layer/Group Norm — in `ch07/training-stability.html` + `ch08/training-techniques.html`

### What is MISSING (not found anywhere in the book):

**Genuinely Missing from the Entire Book:**

1. **Mish activation function** — zero mentions across all chapters
2. **DropConnect** — zero mentions
3. **DropBlock** — zero mentions
4. **Cutout** (data augmentation) — zero mentions
5. **Orthogonal initialization** — zero mentions
6. **LSUV (Layer-Sequential Unit-Variance)** — zero mentions
7. **Fixup initialization** — zero mentions
8. **Capsule Networks (CapsNet)** — zero mentions anywhere in the book
9. **Spiking Neural Networks / Neuromorphic computing** — zero mentions anywhere
10. **Neural ODEs / Continuous-depth networks** — only tangential mentions in calculus chapters
11. **Hypernetworks** — zero mentions anywhere
12. **Energy-Based Models (deep treatment)** — only a passing mention in ch07 nice-to-know (one sentence referencing "energy-based models" in the Hopfield context)
13. **Boltzmann Machines (proper section)** — only a passing mention in ch07 nice-to-know alongside Hopfield
14. **Restricted Boltzmann Machines / Deep Belief Networks** — one mention only (`ch14/classic-generative-models.html`)
15. **Network pruning & compression** (structured vs unstructured) — only mentioned in `ch15/deployment-serving.html`, not in the deep learning foundations chapter
16. **Spectral Normalization** — zero mentions
17. **Instance Normalization** — zero mentions

**Missing from Ch07 specifically but partly covered elsewhere:**
18. Architecture building blocks theory (DenseNet, SE) — covered in ch09 but not from a "foundations" theory perspective in ch07
19. Pruning basics — covered in ch15 deployment but missing from foundations

Here is the complete findings file content:

---

# Ch 07 — Deep Learning Foundations: Missing Topics

## Overview

Chapter 7 currently has **7 sections**: Neural Network Basics, Loss Functions, Backpropagation, Training Stability, Nice to Know, Graph Neural Networks, and Emerging Methods. The coverage is strong on core mechanics (activations, initialization, gradients, backprop) and has good "Nice to Know" theoretical topics (UAT, lottery ticket, double descent, NTK, Hopfield). However, several categories of important deep learning foundations topics are **entirely absent** — both from this chapter and the entire book.

---

## 1. Activation Functions Deep Dive — Mish Missing

### What's Already Covered
- ReLU, dying ReLU problem, Leaky ReLU, PReLU (mentioned), ELU (mentioned), GELU, Swish — `ch07/neural-network-basics.html`
- Dead neurons and prevention with Leaky ReLU/GELU — `ch07/training-stability.html`

### What's Missing

#### Mish Activation Function
**Priority: LOW-MEDIUM** · *Interview relevance: occasionally asked*

Mish (Misra, 2019) is defined as `f(x) = x · tanh(softplus(x))` where `softplus(x) = ln(1 + eˣ)`. It's a self-regularizing non-monotonic activation that was the default in YOLOv4 and YOLOv5. Key properties:
- Smooth, non-monotonic (small dip for negative inputs before approaching zero)
- Unbounded above, bounded below (≈ −0.31)
- No hard zero region — avoids dead neurons like GELU/Swish
- Empirically outperformed ReLU and Swish on several vision benchmarks

**Why it matters**: Mish represents the "smooth activation" trend alongside GELU and Swish. In interviews, candidates are sometimes asked to compare modern activations. The chapter covers GELU and Swish well but Mish is a notable omission given its YOLO adoption.

**Suggested addition**: A brief mention in the "Smooth Gates — GELU and Swish" section of `neural-network-basics.html`, or a comparison table of modern activations:

| Activation | Formula | Key Use Case | Zero Region? |
|-----------|---------|-------------|-------------|
| ReLU | max(0, x) | Default baseline | Yes (dead neurons) |
| Leaky ReLU | max(αx, x) | When dead neurons are a problem | No |
| GELU | x · Φ(x) | Transformers (BERT, GPT) | No (smooth) |
| Swish/SiLU | x · σ(x) | EfficientNet, general | No (smooth) |
| Mish | x · tanh(softplus(x)) | YOLOv4/v5, vision | No (smooth) |

---

## 2. Weight Initialization — Orthogonal & Advanced Methods Missing

### What's Already Covered
- Symmetry breaking problem — `ch07/training-stability.html`
- Xavier/Glorot initialization (2010) with derivation — `ch07/training-stability.html`
- He/Kaiming initialization (2015) with derivation — `ch07/training-stability.html`
- PyTorch implementation patterns — `ch07/training-stability.html`

### What's Missing

#### Orthogonal Initialization
**Priority: MEDIUM** · *Interview relevance: moderate, especially for RNN/LSTM questions*

Orthogonal initialization (Saxe et al., 2014) initializes weight matrices as random orthogonal matrices (via QR decomposition of a random Gaussian matrix). Key properties:
- Preserves gradient norms during backprop — orthogonal matrices have all singular values = 1
- Critical for RNNs where the same weight matrix is applied repeatedly across time steps
- Prevents both vanishing and exploding gradients in recurrent architectures
- Used as default initialization for recurrent weights in many frameworks

**Why it matters**: The chapter covers Xavier (for sigmoid/tanh) and He (for ReLU) but doesn't address what initialization to use for recurrent weights. Since the Nice-to-Know section covers BPTT, orthogonal initialization is a natural companion topic.

#### LSUV (Layer-Sequential Unit-Variance) Initialization
**Priority: LOW** · *Niche but elegant*

LSUV (Mishkin & Matas, 2016) is a data-driven initialization: initialize with orthogonal matrices, then pass a mini-batch through the network and rescale each layer's weights so the output variance is 1. This adapts to the actual data distribution rather than relying on theoretical assumptions.

#### Fixup Initialization
**Priority: LOW** · *Relevant for understanding ResNet training without normalization*

Fixup (Zhang et al., 2019) enables training deep residual networks without any normalization layers by carefully scaling residual branch weights by L^(-1/(2m-2)) where L is the number of residual blocks and m is the number of layers per block. Demonstrates that batch norm is not strictly necessary if initialization is done correctly.

**Suggested addition**: A brief "Beyond Xavier and He" subsection in `training-stability.html`:

```
Orthogonal init: W = QR(random_gaussian) — preserves gradient norms, essential for RNNs
LSUV: Orthogonal + data-driven variance calibration per layer
Fixup: Enables training deep ResNets without normalization layers
```

---

## 3. Advanced Regularization — DropConnect, DropBlock, Cutout Missing

### What's Already Covered (in Ch08)
- Dropout theory (3 interpretations: ensemble, Bayesian, noise injection) — `ch08/training-techniques.html`
- DropPath / Stochastic depth — `ch08/training-techniques.html`
- Weight decay / AdamW — `ch08/training-techniques.html`
- Label smoothing — `ch08/training-techniques.html`
- Mixup and CutMix — `ch08/training-techniques.html`
- Early stopping — `ch08/training-techniques.html`

### What's Missing

#### DropConnect
**Priority: LOW-MEDIUM** · *Interview relevance: sometimes asked as dropout variant*

DropConnect (Wan et al., 2013) randomly zeros individual weights (connections) rather than entire neurons. While dropout sets activations to zero, DropConnect sets weight matrix entries to zero. This is a more fine-grained form of regularization:
- Dropout: `h = f(W · (m ⊙ x))` where m is a mask on activations
- DropConnect: `h = f((M ⊙ W) · x)` where M is a mask on weights

In practice, DropConnect has largely been superseded by dropout variants, but understanding the conceptual difference is valuable for interviews.

#### DropBlock
**Priority: LOW-MEDIUM** · *Important for CNN regularization*

DropBlock (Ghiasi et al., 2018) drops contiguous rectangular regions of feature maps rather than individual units. Motivation: in CNNs, adjacent activations are highly correlated, so dropping individual neurons (standard dropout) is ineffective since neighbors carry the same information. DropBlock forces the network to learn from non-adjacent features.

- Used in ResNet, EfficientNet, and other CNN architectures
- The block size and drop probability are key hyperparameters
- Equivalent to Cutout when applied to the input layer

#### Cutout
**Priority: LOW** · *Data augmentation regularization*

Cutout (DeVries & Taylor, 2017) randomly masks out square regions of training images. It's a simple but effective regularization/augmentation technique for image classification. CutMix (already covered) subsumes Cutout by also mixing labels, but Cutout is historically important and sometimes asked about separately.

**Suggested addition**: These fit naturally as brief mentions in Ch08's regularization section rather than Ch07, but could be referenced in Ch07's "Nice to Know" if the goal is comprehensive coverage within the chapter.

---

## 4. Network Pruning & Compression Foundations — MISSING

### What's Already Covered
- Lottery Ticket Hypothesis (iterative magnitude pruning concept) — `ch07/nice-to-know.html`
- Knowledge Distillation — `ch07/nice-to-know.html` + `ch08/nice-to-know.html`
- Brief mention of pruning in deployment context — `ch15/deployment-serving.html`

### What's Missing

#### Structured vs. Unstructured Pruning
**Priority: MEDIUM-HIGH** · *Very common interview topic, practical relevance*

This is a significant gap. The Lottery Ticket Hypothesis section mentions iterative magnitude pruning but doesn't cover the fundamental taxonomy:

**Unstructured pruning**: Remove individual weights (set to zero). Creates sparse weight matrices.
- Pros: Can achieve very high sparsity (90-99%) with minimal accuracy loss
- Cons: Sparse matrices don't map well to GPU hardware — no actual speedup without specialized sparse kernels
- Methods: Magnitude pruning, gradient-based importance, Optimal Brain Damage (LeCun 1989), Optimal Brain Surgeon

**Structured pruning**: Remove entire neurons, filters, channels, or attention heads. Changes the architecture shape.
- Pros: Results in standard dense networks that run faster on any hardware
- Cons: More aggressive — harder to prune as aggressively without accuracy loss
- Methods: L1-norm filter pruning, Taylor expansion importance, geometric median pruning

**When to use which**:
- Unstructured for maximum compression ratio (edge/mobile with sparse hardware support)
- Structured for real-world GPU deployment speedup
- The distinction is critical for understanding why "90% sparse" doesn't mean "10× faster"

#### Quantization Basics
**Priority: MEDIUM** · *Covered in ch12/ch15 for LLMs but not as a foundation concept*

Post-training quantization (PTQ) and quantization-aware training (QAT) as foundational concepts:
- Float32 → Float16 → Int8 → Int4 progression
- The precision-accuracy tradeoff
- Why quantization works (neural network weight distributions are approximately Gaussian)

**Suggested addition**: A dedicated subsection in Nice-to-Know titled "Network Compression: Pruning, Quantization, and Distillation" that provides the foundational theory (distinct from the LLM-specific treatment in ch12).

---

## 5. Capsule Networks — COMPLETELY MISSING

**Priority: MEDIUM** · *Interview relevance: commonly asked, historically important*

Zero mentions of capsule networks anywhere in the entire book.

### What Should Be Covered

**Core Concept**: Geoffrey Hinton's capsule networks (2017) challenge the fundamental CNN assumption that spatial pooling is sufficient. Instead of scalar activations, capsules output activity vectors encoding both the probability of an entity's existence and its pose (position, orientation, scale).

**Key Ideas**:
- **Equivariance vs. invariance**: CNNs with max-pooling achieve translation invariance (discard position info). Capsules achieve equivariance (position info is preserved and transformed predictably)
- **Routing by agreement**: Lower-level capsules send predictions to higher-level capsules. When multiple lower-level predictions agree, the higher-level capsule activates. This replaces max-pooling with a dynamic routing mechanism
- **The "Picasso problem"**: Standard CNNs can classify a face even when the eyes and mouth are scrambled. Capsules model part-whole spatial relationships, catching such errors
- **Dynamic routing algorithm**: Iterative process where coupling coefficients between capsule layers are adjusted based on agreement between prediction vectors

**Why It Matters for Interviews**:
- Tests understanding of CNN limitations (pooling discards spatial relationships)
- Tests knowledge of equivariance vs invariance
- Shows awareness of alternative architectural paradigms beyond standard CNNs/Transformers
- Hinton (Turing Award winner) championed this idea — interviewers love asking about it

**Current Status**: Capsule networks haven't achieved practical success at scale. They struggle with complexity on large images and haven't outperformed modern CNNs or ViTs on standard benchmarks. But the *ideas* (equivariance, part-whole reasoning, routing by agreement) remain influential.

**Suggested placement**: Emerging Methods section or Nice-to-Know section.

---

## 6. Spiking Neural Networks / Neuromorphic Computing — COMPLETELY MISSING

**Priority: LOW-MEDIUM** · *Growing importance, niche but increasingly relevant*

Zero mentions anywhere in the book.

### What Should Be Covered

**Core Concept**: SNNs are "third generation" neural networks that mimic biological neurons more closely. Neurons don't fire on every forward pass — they accumulate membrane potential over time and fire only when a threshold is reached, emitting discrete spikes.

**Key Ideas**:
- **Leaky Integrate-and-Fire (LIF) model**: The standard spiking neuron model. Membrane potential decays over time (leaks), spikes when threshold is reached, then resets
- **Temporal coding**: Information is encoded not in firing rates but in precise spike timing. A single spiking neuron can theoretically replace hundreds of conventional neurons
- **Energy efficiency**: SNNs are event-driven — computation only happens when spikes occur. This makes them orders of magnitude more energy-efficient for sparse, temporal data
- **Hardware**: Intel's Loihi, IBM's TrueNorth, BrainScaleS — neuromorphic chips designed specifically for SNNs
- **Training challenge**: Spikes are non-differentiable events, so standard backprop doesn't directly apply. Solutions include surrogate gradient methods, spike-timing-dependent plasticity (STDP), and conversion from trained ANNs

**Why It Matters**:
- Edge computing / IoT where power consumption is critical
- Processing temporal/event data (event cameras, audio)
- Represents a fundamentally different computing paradigm from GPU-based deep learning
- Active research area with growing industry investment

**Suggested placement**: Emerging Methods section (2-3 paragraphs).

---

## 7. Neural ODEs / Continuous-Depth Networks — EFFECTIVELY MISSING

**Priority: MEDIUM** · *Elegant theory, strong interview topic*

The book mentions "neural ODE" in passing in calculus chapters but never explains the concept.

### What Should Be Covered

**Core Concept** (Chen et al., NeurIPS 2018 Best Paper): Instead of discrete layers h_{l+1} = f(h_l), define network dynamics as a continuous ODE: dh/dt = f_θ(h(t), t). The output is obtained by solving this ODE from t=0 to t=T using a numerical solver.

**Key Insight**: ResNets are Euler discretizations of Neural ODEs. The residual connection h_{l+1} = h_l + f(h_l) is just h(t+Δt) = h(t) + f(h(t))·Δt with Δt=1.

**Why It's Interesting**:
- **Constant memory**: The adjoint method computes gradients without storing intermediate activations — O(1) memory regardless of "depth"
- **Adaptive computation**: The ODE solver automatically adjusts step size — more computation for complex inputs, less for simple ones
- **Continuous normalizing flows**: Enable tractable density estimation for generative modeling
- **Time series modeling**: Natural framework for irregularly-sampled time series

**Why It Matters for Interviews**:
- Connects deep learning to dynamical systems theory
- Tests understanding of the ResNet-ODE connection
- Shows mathematical maturity

**Suggested placement**: Emerging Methods section or Nice-to-Know.

---

## 8. Energy-Based Models — INADEQUATELY COVERED

### What's Already Covered
- One sentence mentioning "energy-based models (Boltzmann machines, restricted Boltzmann machines, deep belief networks)" in the Hopfield Networks section of `ch07/nice-to-know.html`
- Brief treatment in `ch14/classic-generative-models.html`

### What's Missing

**Priority: LOW-MEDIUM** · *Historical importance, theoretical elegance*

The EBM framework deserves at least a paragraph-level treatment as a foundational concept:

**Core Concept**: Instead of directly outputting probabilities, EBMs learn an energy function E_θ(x) that assigns low energy to correct/likely configurations and high energy to incorrect/unlikely ones. The probability is then P(x) = exp(-E(x)) / Z.

**Key Framework**:
- **Boltzmann Machines** (Hinton & Sejnowski, 1985): Stochastic recurrent networks with symmetric connections. Energy is E = -Σ w_ij s_i s_j. Learning is intractable for general connectivity
- **Restricted Boltzmann Machines (RBMs)**: Bipartite graph restriction — no intra-layer connections. This makes inference tractable via blocked Gibbs sampling. Were the building blocks of Deep Belief Networks
- **Deep Belief Networks** (Hinton, 2006): Stacks of RBMs trained greedily layer by layer. Historically important as the method that reignited interest in deep learning before end-to-end backprop took over
- **Modern EBMs**: Use Langevin dynamics or score matching for training. Connect to diffusion models (which are essentially learning the score function ∇_x log p(x))

**Why It Matters**: The EBM → Diffusion model connection is the theoretical backbone of modern image generation (Stable Diffusion, DALL-E). Understanding EBMs provides deep insight into why diffusion models work.

**Suggested placement**: Expand the Hopfield Networks section in Nice-to-Know with a "The Energy-Based Model Framework" subsection.

---

## 9. Hypernetworks — COMPLETELY MISSING

**Priority: LOW-MEDIUM** · *Niche but increasingly relevant*

Zero mentions anywhere in the book.

### What Should Be Covered

**Core Concept**: A hypernetwork is a neural network that generates the weights for another neural network (the "main" or "target" network). Instead of learning weights directly via backprop, a smaller network learns to produce them.

**Key Formulation**: Given context c, the hypernetwork H_φ(c) produces weights θ = H_φ(c), which are then used by the main network f_θ(x) to make predictions.

**Key Applications**:
- **Continual learning**: Generate task-specific weights without catastrophic forgetting
- **Neural architecture search**: Generate weights for candidate architectures without training each from scratch
- **Model personalization**: Condition weight generation on user/context features
- **LoRA and adapter methods**: Modern parameter-efficient fine-tuning can be viewed through a hypernetwork lens — small networks that modulate the behavior of a frozen large model
- **Weight generation for implicit neural representations** (NeRF, neural fields)

**Why It Matters**: The hypernetwork concept appears in modern contexts like LoRA adapters, model merging, and conditional computation. Understanding the basic idea helps make sense of these practical techniques.

**Suggested placement**: Emerging Methods section (1-2 paragraphs).

---

## 10. Spectral Normalization & Instance Normalization — MISSING

### What's Already Covered (Normalization)
- Batch Normalization — `ch07/training-stability.html` + `ch08/training-techniques.html`
- Layer Normalization — `ch07/training-stability.html` + `ch08/training-techniques.html`
- RMSNorm — `ch08/training-techniques.html`
- Group Normalization — `ch08/training-techniques.html`

### What's Missing

#### Instance Normalization
**Priority: LOW-MEDIUM** · *Critical for style transfer and image generation*

Instance normalization (Ulyanov et al., 2016) normalizes each channel of each sample independently. It's essentially batch norm with batch size = 1. Critical for:
- Style transfer (the original motivation)
- Image generation (many GANs use it)
- Any task where batch statistics are inappropriate

#### Spectral Normalization
**Priority: LOW-MEDIUM** · *Key for GAN training stability*

Spectral normalization (Miyato et al., 2018) constrains the Lipschitz constant of each layer by dividing weights by their largest singular value. This stabilizes GAN discriminator training by preventing the discriminator from becoming too powerful.

**Suggested placement**: These belong more in Ch08 or Ch14 (generative models) than Ch07, but are worth noting as gaps.

---

## 11. Additional Interview-Critical Topics — MISSING

### Mode Connectivity
**Priority: LOW** · *Advanced theory*

The discovery that different local minima found by SGD are connected by simple paths (curves) of near-constant loss (Draxler et al., 2018; Garipov et al., 2018). This challenges the intuition that the loss landscape has isolated minima.

### Lottery Ticket at Scale / Linear Mode Connectivity
**Priority: LOW** · *Extension of already-covered topic*

The original Lottery Ticket Hypothesis (covered) doesn't scale to large networks. Later work showed that rewinding to early training (not initialization) is necessary for larger models. This "rewinding" variant is more practically relevant.

### Feature Visualization / Network Interpretability Basics
**Priority: LOW-MEDIUM** · *Interview topic*

What do neurons learn? Maximizing activation to visualize features, gradient-based saliency maps (Grad-CAM), and the general question of what representations different layers learn (edges → textures → parts → objects). This bridges deep learning foundations with interpretability.

---

## Summary Table: Missing Topics by Priority

| Topic | Priority | In Ch07? | In Book? | Interview Freq |
|-------|----------|----------|----------|----------------|
| Structured vs. Unstructured Pruning | HIGH | ❌ | Barely (ch15) | Very Common |
| Capsule Networks | MEDIUM | ❌ | ❌ | Common |
| Neural ODEs | MEDIUM | ❌ | ❌ | Moderate |
| Orthogonal Initialization | MEDIUM | ❌ | ❌ | Moderate |
| Mish Activation | LOW-MED | ❌ | ❌ | Occasional |
| DropConnect / DropBlock | LOW-MED | ❌ | ❌ | Occasional |
| Hypernetworks | LOW-MED | ❌ | ❌ | Occasional |
| Energy-Based Models (proper) | LOW-MED | Bare mention | Bare mention | Moderate |
| Spiking Neural Networks | LOW-MED | ❌ | ❌ | Growing |
| Instance Normalization | LOW-MED | ❌ | ❌ | Context-dep. |
| Spectral Normalization | LOW-MED | ❌ | ❌ | GAN interviews |
| Cutout | LOW | ❌ | ❌ | Rare |
| LSUV / Fixup Init | LOW | ❌ | ❌ | Rare |
| Mode Connectivity | LOW | ❌ | ❌ | Rare |

---

## Recommendations

### Must-Add to Ch07 (High-value, clearly missing from foundations chapter)
1. **Network Pruning & Compression subsection** in Nice-to-Know — structured vs unstructured pruning taxonomy, connecting to the already-covered Lottery Ticket Hypothesis
2. **Capsule Networks** brief treatment in Emerging Methods — Hinton's routing-by-agreement, equivariance vs invariance
3. **Neural ODEs** brief treatment in Emerging Methods — the ResNet-ODE connection, continuous depth
4. **Orthogonal Initialization** addition to Training Stability — one paragraph after He initialization

### Should-Add (Medium value)
5. **Mish activation** brief mention alongside GELU/Swish in Neural Network Basics
6. **Spiking Neural Networks** brief mention in Emerging Methods
7. **Hypernetworks** brief mention in Emerging Methods
8. **Energy-Based Models** expansion of existing Hopfield mention in Nice-to-Know

### Could-Add (Low value, for completeness)
9. DropConnect/DropBlock mention (could go in Ch08 instead)
10. Instance/Spectral normalization (better suited for Ch08 or Ch14)
11. Cutout (already partially subsumed by CutMix coverage in Ch08)
