# Missing Topics: Ch13 Ml Systems Production

Now I have a thorough understanding of what's already in the chapter and what's missing. Based on my research across multiple authoritative sources (Chip Huyen's DMLS book, Khang Pham's ML interview guide, TryExponent's ML system design framework, the awesome-mlops list, Google's Rules of ML, and the Databricks MLOps guide), here is my comprehensive analysis of missing topics:

## Summary

The chapter (ch15) is **impressively comprehensive** — it already covers feature stores (Feast/Tecton), edge deployment (TFLite/CoreML/ONNX Runtime), A/B testing pitfalls, cost management (FinOps, spot instances), platform engineering, ML technical debt, regulatory landscape, canary/rollback strategies, and real system designs (recommendation, search, fraud, content moderation). However, there are significant gaps in **ML system design interview patterns** (ad click prediction, ETA estimation, notification systems, feed ranking), **deep experimentation methodology** (multi-armed bandits for traffic allocation, interleaving), **data mesh architecture**, **ML testing taxonomy**, **detailed LLMOps operations**, and **several practical production patterns**.

## Key Findings: Topics That Are MISSING or Insufficiently Covered

### 1. Additional ML System Design Patterns (Interview-Critical)
**Status: PARTIALLY MISSING** — The chapter covers recommendation, search, fraud, content moderation. But per the `khangich/machine-learning-interview` repo and Exponent's guide, FAANG interviews commonly ask:
- **Ad Click Prediction / CTR systems** (Facebook's practical lessons paper, Google's ad click prediction paper) — cited in `khangich/machine-learning-interview` lines 244-249
- **Feed Ranking** (LinkedIn, Facebook News Feed, Twitter/X timeline) — cited in `khangich/machine-learning-interview` line 38
- **ETA/Delivery Time Estimation** (Uber, DoorDash) — cited in `khangich/machine-learning-interview` lines 44, 224-227
- **Notification/Push systems** — when to send, what to send, volume optimization
- **Harmful Content Detection** at scale (different from moderation — includes deepfake detection, misinformation)
- **Entity Resolution / Duplicate Detection** systems
- **Pricing/Dynamic Pricing** systems (ride-sharing surge, e-commerce)

### 2. Deep & Wide Models, Embedding-Based Architectures for Production
**Status: MISSING** — No mention of:
- Wide & Deep (Google, 2016) architecture pattern
- DeepFM, DCN (Deep & Cross Network) for CTR prediction
- Embedding table management at scale (billions of sparse features)
- Feature hashing for categorical features in production
- These are standard interview topics per Khang Pham's guide and Google's research papers

### 3. Multi-Armed Bandits for Production Traffic Allocation
**Status: MISSING** — A/B testing is covered well with network effects and peeking, but:
- **Epsilon-greedy, UCB, Thompson Sampling** for model selection in production
- **Contextual bandits** for personalization (LinUCB, etc.)
- **Interleaving experiments** (Team Draft, Probabilistic) — used at Netflix, Spotify for ranking
- Bandits vs. A/B tests trade-offs (exploration-exploitation in production)
- The chapter mentions "Online Learning & Bandits" in Ch5 but doesn't connect it to production system design

### 4. Data Mesh & Data Contracts
**Status: MISSING** — Zero mentions in the chapter:
- **Data Mesh** architecture (Zhamak Dehghani's 4 principles): domain-oriented ownership, data as a product, self-serve platform, federated governance
- **Data Contracts** between producer and consumer teams
- Schema registries (Confluent Schema Registry, AWS Glue)
- Schema evolution strategies for ML pipelines
- Decentralized vs. centralized data architectures

### 5. Comprehensive ML Testing Taxonomy
**Status: PARTIALLY COVERED** — CI/CD mentions unit/integration tests, but missing a dedicated treatment of:
- **Data validation tests** (schema tests, distribution tests, freshness tests)
- **Model validation tests** (invariance tests, directional tests, minimum functionality tests — from "Beyond Accuracy" paper)
- **ML-specific test types**: behavioral testing (CheckList paper, Ribeiro et al. 2020), metamorphic testing, slice-based testing
- **Infrastructure tests** for model serving (load testing, chaos testing for ML — briefly mentioned in nice-to-know but not developed)
- **Pre-train/post-train validation gates** as a formal concept
- Production model smoke tests, shadow comparison tests

### 6. Detailed LLMOps Beyond the Existing Section
**Status: PARTIALLY COVERED** — The AI Engineering section covers prompt management, caching, gateways, and LLMOps vs MLOps distinction. Missing:
- **Prompt versioning and A/B testing prompts** as a formal process
- **LLM output parsing & structured generation** (function calling, JSON mode, constrained decoding)
- **Guardrails frameworks** in detail (NeMo Guardrails, Guardrails AI, constitutional AI in production)
- **LLM fine-tuning operations** (LoRA/QLoRA deployment, adapter management, serving multiple adapters)
- **Token budget management** at organizational scale
- **LLM evaluation pipelines** (MT-Bench, Arena, automated red-teaming)
- **Multi-model orchestration** operational challenges (retry logic, fallback chains between providers)

### 7. Real-Time ML Architecture Patterns (Deeper)
**Status: PARTIALLY COVERED** — Kafka, Flink, streaming inference are mentioned. Missing deeper treatment of:
- **Lambda vs. Kappa architecture** comparison for ML
- **Stream-table duality** and its implications for feature stores
- **Windowed aggregations** patterns (tumbling, sliding, session windows) for features
- **Backfill strategies** when streaming features break
- **Exactly-once semantics** challenges for ML predictions
- **Event sourcing** for ML audit trails

### 8. ML System Reliability & Incident Management
**Status: PARTIALLY COVERED** — Rollback, alerting tiers, and chaos engineering mentioned. Missing:
- **Formal ML incident runbooks** structure (detection → triage → diagnosis → mitigation → postmortem)
- **Blast radius estimation** for ML failures
- **Graceful degradation patterns**: fallback to simpler model, rule-based fallback, cache-based serving
- **SLOs/SLIs/SLAs for ML** (not just latency — prediction quality SLOs)
- **On-call for ML** — how it differs from traditional software on-call
- **Game days** for ML systems (simulating model degradation, data pipeline failures)

### 9. Feature Engineering at Scale (Production Patterns)
**Status: PARTIALLY COVERED** — Feature stores covered well. Missing:
- **Feature computation patterns**: point-in-time correct joins (implementation depth), time-travel queries
- **Feature freshness tiers** (real-time < 1s, near-real-time < 5min, batch < hours)
- **Feature sharing and discovery** across teams at scale
- **Feature monitoring** (feature drift vs. model drift, feature attribution)
- **Embedding features** management in production (embedding versioning, stale embeddings)

### 10. ML Platform Engineering (Deeper Treatment)
**Status: PARTIALLY COVERED** — Section exists in MLOps. Missing deeper treatment of:
- **Platform abstraction layers** (how Uber's Michelangelo, Spotify's Hendrix, Airbnb's Bighead are structured)
- **Self-service model deployment templates**
- **Multi-tenancy** in ML platforms (resource isolation, fair scheduling)
- **Developer experience** metrics for ML platforms (time-to-first-prediction, onboarding time)
- **Internal ML marketplace** (model catalog, feature catalog, dataset catalog)

### 11. Distributed Training Operations
**Status: PARTIALLY COVERED** — Multi-GPU strategies in Infrastructure section. Missing:
- **Training job management** at scale (priority queues, preemption policies, gang scheduling)
- **Distributed training debugging** (stragglers, gradient synchronization issues, OOM debugging)
- **Training efficiency metrics** (MFU — Model FLOPs Utilization, GPU utilization)
- **Large-scale hyperparameter search** operations (population-based training, ASHA)

### 12. Model Compression & Optimization Pipeline (Deeper)
**Status: PARTIALLY COVERED** — Quantization, pruning, distillation mentioned. Missing:
- **Neural Architecture Search (NAS)** for production constraints
- **Structured vs. unstructured pruning** trade-offs
- **Post-training quantization vs. quantization-aware training** decision framework
- **Speculative decoding** for LLM serving
- **KV-cache optimization** (PagedAttention/vLLM internals)
- **Continuous batching** (vs. static batching) for LLM serving

### 13. Data Flywheel & Feedback Collection Systems
**Status: PARTIALLY COVERED** — Feedback loops section exists. Missing:
- **Implicit vs. explicit feedback collection** system design
- **Delayed feedback handling** (attribution windows, label correction)
- **Human-in-the-loop production systems** (active learning triggers, confidence-based routing to humans)
- **Data labeling pipelines** at scale (Snorkel-style programmatic labeling in production)
- **Logging infrastructure** for ML — what to log, how to sample, storage considerations

### 14. Compliance, Governance & Audit (Deeper)
**Status: PARTIALLY COVERED** — EU AI Act, model cards, governance section exist. Missing:
- **GDPR right-to-erasure** impact on trained models (machine unlearning)
- **Model lineage tracking** (from data to prediction — full provenance)
- **Audit trails** for predictions (regulatory requirement in finance, healthcare)
- **Fairness monitoring in production** (not just pre-deployment fairness checks)
- **Model risk management** frameworks (SR 11-7 for banking)
- **Explainability requirements** per domain (credit decisions, insurance, hiring)

### 15. Cost Optimization Patterns (Deeper)
**Status: PARTIALLY COVERED** — FinOps section and spot instances well covered. Missing:
- **Inference cost optimization** beyond model compression: request batching, caching strategies, early exit
- **Model cascade cost** analysis (cheap model → expensive model routing economics)
- **GPU sharing** patterns (MIG — Multi-Instance GPU, time-slicing, MPS)
- **Reserved capacity vs. on-demand vs. spot** decision framework
- **Cost-per-prediction** benchmarking and optimization
- **Right-sizing** GPU instances (when T4 is enough vs. when you need A100)

## Cross-References

The following sources were the primary basis for identifying gaps:
- **chiphuyen/dmls-book** (O'Reilly 2022) — Chapter structure covering data engineering fundamentals, training data, feature engineering, model deployment, data distribution shifts, continual learning, infrastructure
- **khangich/machine-learning-interview** — ML system design interview topics: YouTube recommendation, LinkedIn feed ranking, ad click prediction, delivery time estimation, Airbnb search ranking, fraud detection
- **TryExponent ML System Design Guide** — 6-step framework emphasizing problem definition, data pipeline, model architecture, training/evaluation, deployment, wrap-up
- **Google's "Hidden Technical Debt in ML Systems" (NeurIPS 2015)** — Boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies
- **Databricks MLOps Guide** — LLMOps differences from traditional MLOps (computational resources, transfer learning, human feedback, hyperparameter tuning, performance metrics)
- **visenger/awesome-mlops** — Categories: workflow management, feature stores, data engineering, model deployment/serving, testing/monitoring/maintenance, infrastructure/tooling, model governance/ethics

## Gaps and Uncertainties

- I could not access `educative.io`'s ML system design course content (404 error) or Neptune.ai's experiment tracking guide (403 error) for additional cross-referencing
- Medium articles on ML system design interview questions were inaccessible (403 paywall)
- The chapter's coverage of many topics (A/B testing, feature stores, edge deployment, cost management) is already quite good — the "missing" items above are about **depth and additional patterns** rather than completely absent topics
- Some topics (data mesh, ML testing taxonomy, interleaving experiments) are **completely absent** and represent clear gaps for interview preparation
