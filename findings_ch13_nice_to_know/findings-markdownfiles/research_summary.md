# Ch13 Nice to Know - Research Summary

## Topics to Cover
1. ML Technical Debt (Sculley et al., 2015) - glue code, pipeline jungles, hidden feedback loops, configuration debt
2. Data Cascades (Sambasivan et al., 2021) - compounding errors, "everyone wants to do model work not data work"
3. Feedback Loops Gone Wrong - predictive policing, recommendation filter bubbles, runaway feedback
4. AI Incident Database (AIID) - Partnership on AI, documenting failures, COMPAS, Amazon recruiting
5. Chaos Engineering for ML - Netflix approach, fault injection for models, graceful degradation
6. ML Carbon Footprint - Strubell 2019, training costs, CodeCarbon, carbon-aware scheduling
7. Regulatory Landscape - EU AI Act risk tiers, FDA SaMD, algorithm change protocols
8. ML Team Anti-patterns - all scientists no engineers, premature specialization, no MLOps
9. Build vs Buy - vendor lock-in, decision framework, hybrid approaches

## Key Insights
- Sculley's paper found only ~5% of ML system code is actual model code; rest is infrastructure
- Data cascades are invisible until deployment; 92% of practitioners in Sambasivan study experienced them
- Predictive policing creates self-fulfilling prophecies through observation bias
- EU AI Act: 4 risk tiers (unacceptable, high, limited, minimal)
- FDA SaMD: Class I/II/III, 510(k), De Novo, PMA pathways
- Netflix pioneered chaos engineering for ML with ChAP and FIT tools
