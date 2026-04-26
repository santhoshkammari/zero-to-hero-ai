# Cloud ML Platforms Research

## AWS SageMaker
- Kitchen sink approach, most instance types
- Spot training built-in
- 20-40% premium over raw EC2
- Best for: teams deep in AWS ecosystem
- Bedrock for GenAI

## GCP Vertex AI
- Clean API, TPU access unique differentiator
- Model Garden: one-click fine-tune/deploy
- Kubeflow Pipelines under the hood
- BigQuery Feature Store
- Best for: JAX/TPU users, data-centric teams

## Azure ML
- Enterprise governance standout
- Responsible AI Dashboard
- Azure OpenAI Service (GPT-4o, o1)
- Best for: regulated industries, Microsoft shops

## Key Decision
- Pick based on where data lives (data gravity)
- Cross-cloud ML adds complexity rarely worth it
- Data transfer: $0.09/GB between clouds
