# MLOps Research Notes

## Key Topics to Cover
1. CI/CD for ML (CML, GitHub Actions) - Three pipelines: code CI, data CI, model CI
2. ML Pipelines (Kubeflow, Vertex AI, SageMaker Pipelines) - Orchestration comparison
3. Infrastructure as Code for ML (Terraform, Pulumi)
4. Continuous Training (CT) - Triggers, automation
5. Feature Stores in Production (Feast, Tecton) - Training/serving skew
6. Model Governance & Compliance - EU AI Act, audit trails, model cards
7. MLOps Maturity Levels (Google 0-2)
8. Platform Engineering for ML
9. Cost Management - FinOps, spot instances, GPU optimization
10. Team Structures - ML platform vs product ML

## Running Example
A fraud detection system at a small fintech startup growing from 1 model to 20+.

## Key Insights
- MLOps differs from DevOps: 3 moving axes (code, data, model) vs 1 (code)
- Silent degradation is the killer problem
- Feature stores solve training/serving skew via unified feature definitions
- Google's maturity levels: 0=manual, 1=pipeline automation, 2=CI/CD automation
- IaC enables reproducible ML infrastructure
- Cost: spot instances 70-90% cheaper, but need checkpointing
- Team structure: platform team builds tools, product team builds models
