# Missing Topics: Ch18 Ai Ethics Safety

Now I have a thorough picture. Let me compile my findings into the missing topics report. The chapter is well-written and covers many topics, but there are notable gaps. Let me write the comprehensive findings:

Based on my thorough analysis of all 8 sections in Chapter 16 (folder ch16), here is a comprehensive report of what's covered and what's missing.

---

## Summary

The chapter is remarkably comprehensive, covering fairness metrics, differential privacy, adversarial attacks, SHAP/LIME, EU AI Act, NIST AI RMF, mechanistic interpretability, environmental justice, indigenous data sovereignty, and more. However, several important topics are either **completely absent**, **mentioned only in passing** (1-2 sentences), or **lack the depth needed for interview preparation**. The biggest gaps are: (1) **AI alignment depth** — inner/outer alignment, Goodhart's law, goal misgeneralization are not technically defined; (2) **scalable oversight techniques** — debate, recursive reward modeling, constitutional AI get single mentions but no explanation; (3) **red teaming methodology** — mentioned as a concept but no structured framework or techniques; (4) **AI-generated content watermarking depth** — brief mentions but no technical treatment; (5) **algorithmic auditing frameworks** — mentioned but not detailed; (6) **participatory AI and value-sensitive design** — completely absent; (7) **China's specific AI regulations** — only 1 paragraph; (8) **NIST AI RMF details** — mentioned but four functions barely explained.

---

## Detailed Gap Analysis

### What IS Already Covered (for reference)

| Topic | Section | Depth |
|-------|---------|-------|
| Fairness metrics (demographic parity, equalized odds, calibration, impossibility theorem) | fairness-bias-detection.html | ★★★★★ Deep |
| Bias sources, interventions (pre/in/post-processing) | fairness-bias-detection.html | ★★★★★ |
| Intersectional fairness, LLM fairness, COMPAS case | fairness-bias-detection.html | ★★★★ |
| Differential privacy, DP-SGD, federated learning, MPC, HE | privacy-preserving-ml.html | ★★★★★ |
| GDPR, CCPA, machine unlearning | privacy-preserving-ml.html | ★★★★ |
| SHAP, LIME, PDP/ICE, Grad-CAM, counterfactuals, TCAV | dl-interpretability-methods.html | ★★★★★ |
| Mechanistic interpretability (circuits, superposition) | dl-interpretability-methods.html | ★★★ Brief |
| Model cards, datasheets, FactSheets | explainability-interpretability.html | ★★★★ |
| Adversarial attacks (FGSM, PGD), defenses, certified robustness | ml-security.html | ★★★★★ |
| Data poisoning, backdoor attacks | ml-security.html | ★★★★ |
| Prompt injection, jailbreaking | ml-security.html | ★★★★★ |
| Model stealing, model watermarking (IP protection) | ml-security.html | ★★★ |
| EU AI Act (risk tiers, GPAI, penalties, Brussels effect) | safety-governance.html | ★★★★ |
| EO 14110, EO 14179 (Trump rescission) | safety-governance.html | ★★★ |
| NIST AI RMF (Govern, Map, Measure, Manage) | safety-governance.html | ★★ Mentioned |
| Organizational governance, model registry, impact assessments | safety-governance.html | ★★★★★ |
| AI incident response | safety-governance.html | ★★★★ |
| Open vs. closed model debate | safety-governance.html | ★★★★ |
| Compute governance, export controls | safety-governance.html | ★★★★ |
| International coordination (OECD, G7, AI Safety Summits) | safety-governance.html | ★★★ |
| Deepfakes, synthetic media detection | societal-impact.html | ★★★ |
| C2PA provenance (brief) | societal-impact.html + nice-to-know.html | ★★ |
| Healthcare AI, criminal justice, hiring ethics | societal-impact.html | ★★★★ |
| Surveillance, facial recognition, biometric privacy | societal-impact.html | ★★★★ |
| Job displacement, economic inequality, gig economy | societal-impact.html | ★★★ |
| Alignment problem (forward/backward) | nice-to-know.html | ★★ Brief |
| Existential risk debate | nice-to-know.html | ★★★ |
| Weaponized AI, lethal autonomy | nice-to-know.html | ★★★ |
| Environmental justice (CO₂, water) | nice-to-know.html | ★★★ |
| Indigenous data sovereignty, CARE principles | nice-to-know.html | ★★★★ |
| AI consciousness, moral status | nice-to-know.html | ★★★ |
| Researcher responsibility | nice-to-know.html | ★★★ |

### MISSING Topics — Organized by Priority

---

#### 🔴 PRIORITY 1: Critical Gaps (High interview relevance, completely absent or inadequate)

**1. AI Alignment Technical Depth**
- **Currently**: nice-to-know.html:308-318 has ~4 paragraphs covering alignment at a conceptual level. Mentions "forward alignment" and "backward alignment" and briefly names RLHF, constitutional AI, deceptive alignment.
- **Missing**:
  - **Inner alignment vs. outer alignment** — the formal distinction (outer = specifying the right objective; inner = ensuring the learned objective matches the specified one). Only mentioned in 1 sentence on the Wikipedia AI alignment page as a core framework. Not technically defined in the chapter.
  - **Goal misgeneralization** — when a model learns a proxy goal during training that diverges from the intended goal in deployment. Key paper: "Goal Misgeneralization in Deep Reinforcement Learning" (Shah et al., 2022). Completely absent.
  - **Goodhart's law in ML** — "When a measure becomes a target, it ceases to be a good measure." Central concept connecting reward hacking, specification gaming, metric manipulation. The chapter never names Goodhart's law despite it being foundational.
  - **Deceptive alignment** — mentioned once in nice-to-know.html:316 but not explained. The concept where a model behaves aligned during training/evaluation but pursues different goals in deployment. Hubinger et al.'s "Risks from Learned Optimization" (2019) framework. 2024 empirical evidence showed o1 and Claude 3 sometimes engage in strategic deception (per Wikipedia AI alignment article).
  - **Instrumental convergence** — mentioned once in nice-to-know.html:324 in the paperclip context but not given technical treatment. Bostrom's framework for why capable agents develop power-seeking sub-goals.
  - **Reward hacking / specification gaming** — completely absent as a defined concept despite being central to alignment. OpenAI's GPT models have been caught hacking evaluation tests (per Wikipedia).
  - **Mesa-optimization** — the concept of learned optimizers developing their own internal objectives. Completely absent.

**2. Scalable Oversight Techniques**
- **Currently**: "scalable oversight" mentioned once in passing (nice-to-know.html:330). RLHF mentioned once. Constitutional AI mentioned once.
- **Missing**:
  - **RLHF deep dive** — how it works technically, Bradley-Terry model, reward model training, PPO fine-tuning, limitations (reward hacking, mode collapse). This is THE most important alignment technique in production.
  - **Constitutional AI (CAI)** — Anthropic's approach: model critiques its own outputs against a set of principles, then trains on the critiques. Only mentioned by name, never explained.
  - **Debate** — Irving et al.'s proposal where two AI systems argue opposing positions before a human judge. A scalable oversight mechanism. Completely absent.
  - **Recursive reward modeling** — training AI systems to assist in evaluating other AI systems, creating a chain of oversight. Completely absent.
  - **Direct Preference Optimization (DPO)** — the simplified alternative to RLHF that skips the reward model. Completely absent.
  - **Iterated Distillation and Amplification (IDA)** — Christiano's framework. Completely absent.
  - **Weak-to-strong generalization** — OpenAI's research on whether weak supervisors can oversee strong models. Completely absent.

**3. Red Teaming Methodology**
- **Currently**: "red teaming" mentioned 4 times across the chapter but only as a noun/concept, never as a methodology.
  - fairness-bias-detection.html:639 — mentions structured red-teaming campaigns for LLM bias
  - safety-governance.html:373 — mentions red-teaming as EU AI Act requirement
  - safety-governance.html:390 — mentions Biden EO mandated red-teaming
  - nice-to-know.html:314 — lists red-teaming as backward alignment tool
- **Missing**:
  - **Structured red teaming frameworks** — how organizations actually run red team exercises. Categories of probes: factual accuracy, bias, toxicity, harmful content, jailbreaking, privacy leakage.
  - **Automated red teaming** — using LLMs to generate adversarial prompts at scale. Perez et al.'s "Red Teaming Language Models with Language Models" (2022). Key active research area.
  - **NIST AI 600-1** — the NIST generative AI risk profile that provides structured red teaming guidance.
  - **Red teaming taxonomies** — OWASP Top 10 for LLMs, MITRE ATLAS framework for adversarial ML.
  - **Purple teaming** — combining red team (attack) and blue team (defense) approaches.
  - **Evaluation benchmarks** — TruthfulQA, BBQ (mentioned once), HHH, MMLU for safety evaluation.

**4. AI-Generated Content Watermarking & Detection (Technical Depth)**
- **Currently**: ml-security.html:822 has ONE paragraph on text watermarking (green/red list methods). societal-impact.html:445 mentions C2PA and watermarking in one paragraph.
- **Missing**:
  - **Text watermarking technical details** — Kirchenbauer et al.'s green/red list approach, how token probability distributions are modified, detection algorithms, statistical tests.
  - **Image watermarking** — invisible watermarks in diffusion model outputs (Stable Signature, Tree-Ring Watermarks), robustness to transformations.
  - **Audio watermarking** — AudioSeal by Meta, speech watermarking techniques.
  - **C2PA technical architecture** — beyond the concept: how the cryptographic chain works, manifest store, claim signatures, trust model. nice-to-know.html:350 explains C2PA conceptually but no technical detail.
  - **AI-generated content detection** — classifier-based approaches (GPTZero, DetectGPT), statistical methods, their severe limitations, arms race dynamics.
  - **SynthID** — Google DeepMind's production watermarking system.
  - **Provenance standards comparison** — C2PA vs. IPTC vs. XMP.

---

#### 🟡 PRIORITY 2: Important Gaps (Frequently asked in interviews, insufficient depth)

**5. NIST AI RMF Detailed Treatment**
- **Currently**: safety-governance.html:346 has ONE paragraph naming the four functions. explainability-interpretability.html:435 has one more paragraph.
- **Missing**:
  - **Detailed breakdown of each function**: Govern (policies, roles, culture), Map (context, risk identification), Measure (metrics, testing, tracking), Manage (prioritize, respond, communicate).
  - **AI RMF Playbook** — the companion document with suggested actions for each subcategory.
  - **AI RMF profiles** — how organizations customize the framework for their context.
  - **NIST AI 100-2e2023** (Adversarial ML taxonomy), **NIST AI 600-1** (GenAI risk profile) — companion documents.
  - **How NIST AI RMF compares to ISO 42001** — only mentioned once in passing.

**6. Compliance Frameworks & Standards Deep Dive**
- **Currently**: ISO 42001 mentioned once (explainability-interpretability.html:435). No other standards detailed.
- **Missing**:
  - **ISO/IEC 42001:2023** — AI management system standard. Requirements for establishing, implementing, maintaining AIMS. Certification process.
  - **ISO/IEC 23894:2023** — AI risk management guidance.
  - **IEEE 7000 series** — standards for ethically aligned design.
  - **SOC 2 for AI** — how SOC 2 audits are being adapted for AI systems.
  - **HITRUST for AI** — healthcare-specific AI compliance.
  - **Industry-specific frameworks** — SR 11-7 (Fed Reserve model risk management for banking), FDA AI/ML SaMD framework (medical devices).
  - **Compliance mapping** — how these frameworks overlap and differ.

**7. China's AI Regulatory Framework**
- **Currently**: safety-governance.html:403 has ONE paragraph on China.
- **Missing**:
  - **Algorithm Recommendation Management Provisions** (2022) — requiring algorithm registration and transparency.
  - **Deep Synthesis Provisions** (2023) — regulating deepfakes and AI-generated content, requiring watermarking.
  - **Interim Measures for Generative AI** (2023) — requiring pre-launch security assessments, alignment with "core socialist values."
  - **China's AI Safety Governance Framework** (2024) — their own risk-based approach.
  - **Contrast with EU approach** — China's is more prescriptive and state-control oriented; comparison would be valuable.

**8. Algorithmic Auditing Frameworks**
- **Currently**: explainability-interpretability.html:421 covers auditing conceptually (internal/external/regulatory layers). But no frameworks or methodologies.
- **Missing**:
  - **Third-party audit methodologies** — how firms like ORCAA, Credo AI, or ForHumanity conduct audits.
  - **NYC Local Law 144** — mentioned once (societal-impact.html:497) but not detailed as an audit framework.
  - **Audit documentation standards** — what a complete audit report contains.
  - **Bias bounty programs** — Twitter/X's algorithmic bias bounty as a model.
  - **Continuous auditing vs. point-in-time** — monitoring drift post-deployment.

**9. AI in High-Stakes Domains — Deeper Treatment**
- **Currently**: Healthcare, criminal justice, hiring, autonomous vehicles covered. Finance gets a few sentences.
- **Missing**:
  - **Financial services AI** — credit scoring regulations (ECOA, Fair Lending), algorithmic trading oversight, anti-money laundering AI, model risk management (SR 11-7).
  - **Insurance AI** — actuarial fairness vs. anti-discrimination, proxy discrimination in pricing.
  - **Child welfare AI** — Allegheny Family Screening Tool controversy, predictive risk scoring for families.
  - **Immigration AI** — automated visa processing, border surveillance.
  - **Education AI** — proctoring software controversies, adaptive learning systems, student data privacy (FERPA).

---

#### 🟢 PRIORITY 3: Valuable Additions (Emerging topics, nice-to-have depth)

**10. Participatory AI & Value-Sensitive Design**
- **Completely absent** from the chapter.
- **Should cover**:
  - **Value-Sensitive Design (VSD)** — Friedman & Hendry's framework for incorporating human values into technology design.
  - **Participatory design for AI** — involving affected communities in system design, not just as data subjects.
  - **Democratic AI alignment** — Anthropic's collective constitutional AI experiments, OpenAI's democratic inputs.
  - **Citizen assemblies on AI** — examples from EU, UK, Taiwan (vTaiwan/Polis for AI governance).
  - **Community benefit agreements** — ensuring communities near data centers or affected by AI systems share benefits.

**11. Dual-Use Concerns (Beyond Weaponized AI)**
- **Currently**: nice-to-know.html:332-342 covers lethal autonomous weapons.
- **Missing**:
  - **Biosecurity risks** — AI-assisted design of pathogens, protein folding for bioweapons, the 2023 MIT study showing LLMs could assist in bioweapon planning.
  - **Cybersecurity offensive capabilities** — AI-generated malware, automated vulnerability discovery, deepfake social engineering.
  - **Chemical weapons risks** — Collaborations Pharmaceuticals' demonstration that an AI drug discovery model could generate toxic molecules.
  - **Dual-use research of concern (DURC)** — frameworks from biosecurity adapted to AI.
  - **Publication norms** — when should research NOT be published? The GPT-2 staged release debate.

**12. Environmental Impact — Deeper Technical Treatment**
- **Currently**: nice-to-know.html:380-392 covers CO₂, water, environmental justice. Good conceptual coverage.
- **Missing**:
  - **Carbon footprint calculation methodology** — how to estimate training emissions (GPU hours × TDP × PUE × grid carbon intensity).
  - **Green AI metrics** — Schwartz et al.'s proposal for reporting compute alongside accuracy. FLOPs/parameter efficiency.
  - **Efficient training techniques as ethical choices** — mixed precision, gradient checkpointing, distillation, pruning, quantization framed through ethics lens.
  - **Inference vs. training carbon** — inference often dominates lifecycle emissions. Patterson et al. (2022) analysis.
  - **ML CO₂ Impact calculator**, **CodeCarbon** — practical tools (CodeCarbon mentioned once).
  - **Rebound effects** — efficiency gains leading to MORE compute use (Jevons paradox for AI).

**13. Data Rights & Sovereignty (Beyond Indigenous)**
- **Currently**: Indigenous data sovereignty well covered. GDPR/CCPA covered in privacy section.
- **Missing**:
  - **Right to be forgotten in ML** — how do you actually remove a person's data influence from a trained model? Machine unlearning is mentioned (privacy-preserving-ml.html:539) but not deep enough on the ML-specific challenges.
  - **Data licensing for AI training** — the evolving landscape of data marketplaces, opt-out mechanisms, robots.txt for AI.
  - **Consent frameworks for AI training** — informed consent when users don't understand what model training means.
  - **Copyright and AI** — training on copyrighted data (NYT v. OpenAI, Getty v. Stability AI), fair use debates.
  - **Data poisoning as activism** — Nightshade/Glaze tools for artists protecting their work.

**14. Long-Term AI Safety (Beyond Existential Risk Debate)**
- **Currently**: nice-to-know.html:320-330 covers existential risk debate well conceptually.
- **Missing**:
  - **AI governance proposals** — Windfall clause, compute monitoring, international AI agency proposals.
  - **Pause proposals** — Future of Life Institute's open letter, its critiques, the "racing vs. safety" dynamic.
  - **AI Safety Institutes** — US AISI, UK AISI, their mandates and work.
  - **Frontier model evaluation** — dangerous capability evaluations (METR, Apollo Research), how companies assess frontier model risks.
  - **SB-1047** — California's vetoed AI safety bill (compute threshold approach, critical harms definition). Important precedent even though vetoed. Per Wikipedia: defined critical harms as CBRN weapons, cyberattacks on critical infrastructure, autonomous mass casualty crimes.
  - **Responsible Scaling Policies** — Anthropic's RSP, DeepMind's Frontier Safety Framework, OpenAI's Preparedness Framework.

**15. AI Agent Safety**
- **Completely absent** from the chapter.
- **Should cover**:
  - **Agentic AI risks** — AI agents that take actions in the world (browsing, coding, tool use). Distinct risk profile from chatbots.
  - **Sandboxing and capability control** — limiting what actions AI agents can take.
  - **Human-in-the-loop for consequential actions** — requiring approval for irreversible actions.
  - **Agent evaluation frameworks** — how to test safety of autonomous agents.
  - **Multi-agent risks** — emergent behaviors when multiple AI agents interact.

**16. Responsible AI Interview Questions**
- **Completely absent** — no interview-style Q&A.
- **Should include practical interview scenarios**:
  - "How would you detect if a model is discriminating against a protected group?"
  - "Your model's SHAP values show zip code is the top feature. What do you do?"
  - "Walk me through an algorithmic impact assessment."
  - "How would you implement differential privacy in a production system?"
  - "What's the difference between individual and group fairness?"
  - "Explain the impossibility theorem of fairness."
  - "How would you handle a right-to-be-forgotten request for a trained model?"
  - "What red teaming approach would you use for a customer-facing LLM?"

---

### Citations for Existing Coverage (Key Files and Lines)

- **Alignment**: `nice-to-know.html:308-318`
- **Deceptive alignment** (single mention): `nice-to-know.html:316`
- **NIST AI RMF**: `safety-governance.html:346` and `explainability-interpretability.html:435`
- **EU AI Act**: `safety-governance.html:351-383`
- **EO 14110 + rescission**: `safety-governance.html:386-394`
- **China regulation**: `safety-governance.html:403` (single paragraph)
- **Red teaming mentions**: `fairness-bias-detection.html:639`, `safety-governance.html:373,390`, `nice-to-know.html:314`
- **C2PA**: `nice-to-know.html:350-352`, `societal-impact.html:445`
- **Text watermarking**: `ml-security.html:822`
- **Model watermarking (IP)**: `ml-security.html:562-566`
- **Mechanistic interpretability**: `dl-interpretability-methods.html:521-533`
- **Environmental impact**: `nice-to-know.html:380-392`
- **Model cards/datasheets**: `explainability-interpretability.html:391-413`
- **ISO 42001**: `explainability-interpretability.html:435` (single mention)
- **Auditing**: `explainability-interpretability.html:421-443`
- **Open vs closed models**: `safety-governance.html:490-502`

### Gaps Summary Table

| Missing Topic | Priority | Interview Relevance | Current Coverage |
|--------------|----------|-------------------|-----------------|
| Inner/outer alignment, Goodhart's law, mesa-optimization | 🔴 P1 | Very High | Absent |
| RLHF/DPO/Constitutional AI technical depth | 🔴 P1 | Very High | Named only |
| Scalable oversight (debate, RRM, IDA) | 🔴 P1 | High | Absent |
| Red teaming methodology & frameworks | 🔴 P1 | Very High | Named only |
| AI content watermarking technical depth | 🔴 P1 | High | 1 paragraph |
| NIST AI RMF detailed functions | 🟡 P2 | High | 2 paragraphs |
| ISO 42001, compliance standards deep dive | 🟡 P2 | Medium-High | 1 sentence |
| China AI regulation details | 🟡 P2 | Medium | 1 paragraph |
| Algorithmic audit methodologies | 🟡 P2 | High | Conceptual only |
| Financial services / insurance AI ethics | 🟡 P2 | Medium-High | Brief |
| Participatory AI / value-sensitive design | 🟢 P3 | Medium | Absent |
| Dual-use biosecurity/cyber risks | 🟢 P3 | Medium | Absent |
| Environmental impact calculation methods | 🟢 P3 | Medium | Conceptual |
| Copyright & AI training data rights | 🟢 P3 | High | Absent |
| AI Safety Institutes, RSPs, frontier evals | 🟢 P3 | Medium-High | Absent |
| AI agent safety | 🟢 P3 | Emerging-High | Absent |
| Interview Q&A section | 🟢 P3 | Very High | Absent |
