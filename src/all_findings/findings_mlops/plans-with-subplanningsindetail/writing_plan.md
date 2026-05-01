# Writing Plan for MLOps Section

## Running Example
FraudShield - a tiny fraud detection system at a 3-person ML startup.
Start: one notebook, one model, one data scientist.
End: 20+ models, automated pipelines, full governance.

## Concept Ladder (dependency order)
1. The Three Moving Parts (code, data, model) - why MLOps exists
2. The Notebook to Pipeline Journey - motivate automation
3. CI/CD for ML - three pipelines
4. Continuous Training - when and why to retrain
5. Feature Stores - training/serving skew problem
6. ML Pipelines & Orchestration - Kubeflow, Vertex, SageMaker
7. Infrastructure as Code - reproducible ML infra
8. Model Governance & Compliance - audit trails, model cards
9. Cost Management - FinOps for ML
10. MLOps Maturity Levels - Google 0-2
11. Team Structures - platform vs product ML
12. Platform Engineering - building the internal ML platform

## Rest Stops
- After CI/CD + CT (useful mental model of automated ML)
- After governance (before cost/team structure)

## Vulnerability Moments
1. Opening: avoided MLOps, thought it was buzzword soup
2. Feature stores: didn't understand why needed until hit skew bug
3. IaC: still get the Terraform state wrong sometimes
4. Maturity levels: honest that most teams are Level 0 and that's OK
5. Cost: share a $40K GPU bill story

## Recurring Analogies
1. Restaurant kitchen: from home cooking to restaurant chain
2. Assembly line: Henry Ford's standardization
