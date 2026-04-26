# Web Search Summary

## MLOps Maturity Levels (Google)
- Level 0: Manual processes, notebooks, email model files
- Level 1: Pipeline automation (Kubeflow, TFX), scheduled retraining
- Level 2: Full CI/CD automation, auto-triggered retraining, drift detection, rollback

## CI/CD for ML
- CML (Continuous Machine Learning) by Iterative.ai
- GitHub Actions integration with DVC for data versioning
- Self-hosted runners for GPU workloads
- CML reports as PR comments with metrics/visualizations

## Pipeline Orchestration
- Kubeflow: Open source, K8s-native, max flexibility, steep learning curve
- Vertex AI: Managed, GCP-native, built on KFP, easy setup
- SageMaker: AWS-native, managed spot training, JumpStart

## Feature Stores
- Feast: Open source, offline+online stores, point-in-time joins
- Tecton: Commercial, declarative pipelines, monitoring
- Key: unified feature definitions prevent training/serving skew

## Model Governance
- EU AI Act requires audit trails, risk management, documentation
- Model cards for transparency
- Article 12: automatic logging requirements

## Cost Management
- Spot instances: 70-90% cheaper
- Checkpointing essential for spot usage
- Right-sizing GPU instances
- Kubecost for K8s cost monitoring
- Run:ai for GPU scheduling optimization
