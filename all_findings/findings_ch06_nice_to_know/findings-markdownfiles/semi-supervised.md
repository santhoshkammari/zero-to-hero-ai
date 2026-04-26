# Semi-Supervised Learning

## Why it matters
- Labeled data expensive, unlabeled data abundant
- Bridge between supervised and unsupervised

## Key approaches
1. **Self-training**: Train on labeled data → predict on unlabeled → add high-confidence predictions → retrain. Simple but can compound errors
2. **Label propagation**: Build similarity graph → spread labels through edges. Assumes nearby points share labels. In scikit-learn
3. **Pseudo-labels**: Same idea as self-training but specifically in neural network training — add pseudo-labeled data to training batches
4. **Co-training**: Two models with different "views" of data teach each other
5. **MixMatch/FixMatch**: Modern deep semi-supervised — combine consistency regularization + pseudo-labeling + data augmentation

## The danger: confirmation bias
- Model's mistakes become training signal → errors compound
- Mitigation: confidence thresholds, curriculum learning, temperature sharpening

## Production reality
- Medical imaging (expensive labels), NLP with limited annotations
- Often the practical answer when you can't label everything
- Interview angle: "what would you do with 100 labeled and 100,000 unlabeled examples?"
