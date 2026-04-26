# Transfer Learning — Research Findings

## Core Concepts Gathered

### Why Transfer Learning Works (Theoretical)
1. **Feature Reuse Hypothesis**: Lower/mid layers learn universal features (edges, textures, shapes) transferable across tasks. Yosinski et al. (2014) empirically measured this layer-by-layer.
2. **Loss Landscape Theory**: Pretraining moves weights into a "basin of attraction" — a region of parameter space where fine-tuning finds flatter minima, leading to better generalization.
3. **Optimization Hypothesis**: Pretrained networks are better starting points, closer to optimal solutions for related tasks than random initialization.
4. **Inductive Bias**: Pretraining imbues implicit structural knowledge about data, improving learning on limited data.

### Yosinski et al. (2014) — Key Findings
- First 3 layers transfer almost perfectly between tasks
- Performance degrades as you transfer deeper, more task-specific layers
- Freezing transferred layers + training remaining from scratch works well for early/mid layers
- Fine-tuning transferred layers lessens negative impact at deeper layers
- Neurons in early layers resemble Gabor filters — universal edge detectors

### Evolution: ULMFiT to Foundation Models
1. **Pre-2017**: Training from scratch per task. Vision already used ImageNet pretrain-finetune.
2. **ULMFiT (2018)**: Howard & Ruder — 3-stage process: general pretraining → domain fine-tuning → task classifier. Introduced gradual unfreezing + discriminative LRs + slanted triangular LR.
3. **ELMo (2018)**: Deep contextual embeddings via bidirectional LSTMs.
4. **BERT (2018)**: Bidirectional transformers with masked LM. Popularized pretrain-then-fine-tune.
5. **GPT series (2018-2020)**: Scaling led to zero/few-shot capability.
6. **Foundation Models era**: Pretrain massive models → prompt/instruct rather than fine-tune. CLIP, SAM, GPT-4V for multimodal.
7. **PEFT methods (2021+)**: LoRA, adapters, prefix tuning — update <1% of params, near full fine-tune performance.

### Fine-Tuning Strategies
- **Feature Extraction (Frozen Backbone)**: Freeze all pretrained weights, train only new head. Best for tiny datasets, similar domains.
- **Full Fine-Tuning**: Unfreeze everything, low LR. Needs large dataset.
- **Gradual Unfreezing**: Unfreeze progressively from head to earlier layers. ULMFiT's key contribution.
- **Discriminative Learning Rates**: Different LR per layer group. Lower for early layers, higher for head. Exponential decay pattern.
- **Slanted Triangular LR**: Quick warmup then gradual decay — ULMFiT innovation.

### Domain Adaptation
- **DANN (Ganin et al., 2015)**: Gradient reversal layer forces domain-invariant features. Feature extractor tries to fool domain classifier.
- **CORAL**: Aligns second-order statistics (covariance matrices) between source/target.
- **Self-training with pseudo-labels**: Train on source → predict high-confidence labels on target → retrain on combined.
- **Modern**: Source-free adaptation (SHOT), contrastive learning-based UDA, test-time adaptation.

### Negative Transfer
- Occurs when source/target domains too different
- Signs: fine-tuning worse than scratch, early saturation, training loss fine but val loss stalls
- Solutions: partial transfer (use only early layers), domain-specific pretrained models, train from scratch with enough data

### Knowledge Distillation (Hinton et al., 2015)
- Teacher (large) → Student (small) via soft targets
- Temperature scaling: T>1 softens distribution, reveals "dark knowledge" — inter-class relationships
- Loss = α * KL_div(soft) + (1-α) * CE(hard)
- The soft probabilities encode which classes the teacher finds similar

### PEFT / LoRA
- LoRA: W' = W + BA where B∈R^(d×r), A∈R^(r×k), r << min(d,k)
- Only train A and B matrices — <1% of total params
- Advantages: modular (swap adapters per task), lower memory, minimal forgetting
- Near parity with full fine-tuning for most tasks

### Catastrophic Forgetting Prevention
- EWC (Elastic Weight Consolidation): Penalty on important weights changing
- Progressive Networks: New columns per task, keep old intact
- Replay/Rehearsal: Re-train on source data samples
- Learning Without Forgetting (LwF): Soft labels from old tasks as additional targets

### Paradigm Shift Summary
- **Era 1** (2012-2018): Pretrain on ImageNet → Fine-tune weights → Task-specific head
- **Era 2** (2018-2020): Large-scale pretrain (BERT/GPT) → Fine-tune for task
- **Era 3** (2020-2022): Foundation models → Prompt engineering → Zero/few-shot
- **Era 4** (2022+): Foundation models → PEFT/LoRA → In-context learning → No weight updates needed

### Practical Insights for Interview Depth
- BatchNorm freezing: Most common silent failure in fine-tuning
- The 1000x rule: need ~1000 examples per class for full fine-tuning
- Feature extraction can work with as few as 50 examples per class
- Domain gap is the critical variable, not just dataset size
- timm library: 700+ models, handles preprocessing automatically
- Always start with feature extraction as baseline, then escalate
