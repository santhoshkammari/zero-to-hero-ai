# Explainability & Interpretability for Responsible AI - Research Summary

## Key Topics to Cover (Ethics/Governance Angle)

### 1. Right to Explanation (GDPR Article 22)
- Article 22(1): Data subjects have right NOT to be subject to solely automated decisions with legal/significant effects
- Exceptions: contract necessity, explicit consent, law authorization
- Safeguards: human intervention, express point of view, contest decision
- "Right to explanation" not explicitly named but supported by Recitals 71, 63 and Article 15
- Must explain: existence of automated decision-making, underlying logic, significance and consequences
- EU AI Act (2024) supplements with stricter transparency for high-risk AI

### 2. Stakeholder-Specific Explanations
- User: Simple, clear reasons in everyday language ("recommended because...")
- Developer: Technical detail, logs, metrics, SHAP/LIME, feature importance
- Regulator: Compliance reports, risk assessments, audit trails, model documentation
- Affected Individual: Personalized actionable feedback, appeal process, recourse

### 3. Fidelity vs Comprehensibility Tradeoff
- High fidelity = accurately reflects model's actual decision logic (but complex)
- High comprehensibility = simple, human-friendly (but potentially unfaithful)
- 2024 focus: hybrid explanations, user-adaptive explanations, fidelity metrics

### 4. Model Documentation
- Model Cards (Mitchell et al., 2019): model details, intended use, factors, metrics, ethical considerations, caveats
- Datasheets for Datasets (Gebru et al., 2021): motivation, composition, collection process, preprocessing
- FactSheets (IBM): holistic AI service documentation
- Data Statements (NLP): speaker, dialect, demographics

### 5. Algorithmic Auditing
- NIST AI RMF: risk identification, measurement, mitigation, documentation
- Algorithmic Impact Assessments (AIA): before and after deployment
- External third-party auditors (ForHumanity, BSI, TüV SÜD)
- ISO/IEC 42001:2023 for AI management systems

### 6. Contestability
- Right to contest = recognized right to challenge automated decisions
- Requires: notification, explanation, human review, accessible appeals, accountability
- GDPR Article 22 + Australian AHRC + OECD/UNESCO guidelines

### 7. EU AI Act 2024
- High-risk AI: biometric ID, critical infra, education, employment, law enforcement
- Article 13: systems must be transparent enough for deployers to "reasonably understand"
- Must provide clear instructions for use, disclose limitations and risks
- Penalties: up to €35M or 7% of global turnover
- Compliance deadlines: most high-risk obligations by August 2026

### 8. High-Stakes Domains
- Healthcare: diagnosis/treatment decisions need explainability
- Criminal Justice: COMPAS - biased against Black defendants, opaque, no recourse
- Finance: credit scoring, loan approval - unexplained rejections cause harm

### 9. Rashomon Effect
- Multiple models can achieve same accuracy with different explanations
- Explanations are model-dependent, not unique
- Implication: we should seek robust, consensus-based interpretations

### Running Example: Loan Application Decision System
- Concrete, relatable, threads through all concepts
- Applicant denied, wants to know why
- Different stakeholders need different explanations
- Contestability, audit, documentation all apply
