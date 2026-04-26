# Knowledge Distillation

## Core Idea (Hinton et al., 2015)
- Train a small "student" network to mimic a large "teacher" network
- The student learns from teacher's soft probability outputs, not just hard labels
- Soft targets contain "dark knowledge" — relationships between classes
- E.g., teacher saying "80% cat, 15% tiger, 5% dog" teaches more than just "cat"

## Temperature Scaling
- Soften teacher outputs with temperature T: softmax(logits/T)
- Higher T → softer distribution → more information about class relationships
- T=1 is standard softmax; T=3-20 common for distillation
- Student trained on weighted combination of: soft targets (from teacher) + hard labels

## Why It Works
- Teacher's mistakes are informative — "this 3 looks like an 8" is useful signal
- Soft targets provide richer gradient signal than one-hot labels
- Student can achieve near-teacher accuracy with fraction of parameters

## Practical Impact
- Model compression for deployment (BERT → DistilBERT: 40% smaller, 60% faster, 97% performance)
- Ensembles → single model distillation
- Used extensively in production (mobile models, edge deployment)

## Interview Angle
- Know temperature scaling mechanism
- Know why soft targets beat hard labels
- Know DistilBERT as canonical example
