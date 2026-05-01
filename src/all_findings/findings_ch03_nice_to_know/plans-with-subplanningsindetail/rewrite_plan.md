# Rewrite Plan for ch03/s10.html — Nice to Know (Data Fundamentals)

## Style
- Brandon Rohrer voice: practitioner, not professor
- Narrative prose, not listicles
- Each topic gets a "why you'll care" framing, not just description
- Focus on when these matter in practice, not textbook definitions
- Vulnerability moments: honest about what's confusing, what doesn't work as advertised

## Topics to Cover (rewritten with depth)
1. **DVC** — version control for data, the "which data trained model v2.3?" problem
2. **Feature Stores** — the train/serve skew problem at feature level
3. **Imbalanced Datasets** — class weights vs SMOTE, production reality
4. **Synthetic Data Generation** — when real data is scarce/sensitive, fundamental limitation
5. **Data Augmentation for Tabular** — why it's harder than images, mixup, noise
6. **Delta Lake / Lakehouse** — ACID + time travel on data lakes
7. **Privacy Regulations (GDPR/CCPA/HIPAA)** — what ML engineers actually need to know
8. **Differential Privacy** — the privacy/utility tradeoff, DP-SGD
9. **Data Contracts & Catalogs** — organizational scaling
10. **Data Leakage** — the silent killer, interview gotcha

## HTML Structure
- Preserve exact HTML skeleton (head, sidebar, nav, topbar, page-nav, scripts)
- Rewrite only the content div inner content
- Keep callout box style at end
