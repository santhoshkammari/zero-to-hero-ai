# Rewrite Plan: Self-Supervised & Representation Learning

## Running Example
Photo sorting app - building an app that can organize photos by content without manually tagging each one.
Start tiny: 3 photos (dog, cat, bird). Scale up as concepts demand.

## Concept Ladder (dependency order)
1. The label problem - why we need self-supervised learning (motivation)
2. The core insight: make the data supervise itself (pretext tasks concept)
3. What "representation" even means - the map analogy
4. Contrastive learning - the similarity game (positive/negative pairs)
5. SimCLR - the elegant but expensive approach
6. MoCo - solving SimCLR's cost problem with a queue
7. REST STOP
8. Beyond negatives - BYOL and the collapse problem
9. Barlow Twins - redundancy reduction
10. DINO - self-distillation and emergent segmentation
11. MAE - the BERT of vision
12. How to use representations: linear probes and fine-tuning
13. Wrap-up

## Analogies (recurring)
1. Map/cartography analogy - representations as maps of data landscape
2. Apprentice/mentor analogy - for self-distillation (BYOL, DINO)

## Vulnerability moments
1. Opening confession about avoiding the topic
2. "I still don't fully understand why BYOL doesn't collapse" 
3. Acknowledging that no one fully knows why 75% masking works so well in MAE
4. Admitting the progression of methods feels obvious in hindsight but wasn't at all
5. "I still get confused about which methods need negatives and which don't"
