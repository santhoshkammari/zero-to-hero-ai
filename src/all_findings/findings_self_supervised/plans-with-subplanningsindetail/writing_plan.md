# Writing Plan for Self-Supervised & Contrastive Learning

## Running Example
Building a wildlife camera trap classifier. Start with 3 animals (deer, fox, owl). 
We have 50,000 unlabeled trail cam photos but only 47 labeled ones (a volunteer labeled them one weekend).
This motivates: why can't we use all 50K photos to learn something useful?

## Concept Ladder (dependency order)
1. The labeling bottleneck (motivation)
2. Pretext tasks - teaching by hiding (rotation, jigsaw, colorization as toy examples)
3. Why pretext tasks feel unsatisfying → leads to contrastive
4. Contrastive learning core idea (positive/negative pairs)
5. InfoNCE loss (the math behind "pick the right one")
6. SimCLR as the clean reference implementation
7. The batch size problem → MoCo's solution
8. REST STOP
9. Can we drop negatives? BYOL's surprising answer
10. DINO and emergent attention maps
11. Masked image modeling (MAE) - the vision equivalent of BERT
12. Text vs vision: why approaches differ
13. CLIP as multimodal contrastive
14. Evaluation: linear probing vs fine-tuning
15. When to use SSL in practice
16. Wrap-up

## Vulnerability Moments
1. Opening: "I kept hearing 'self-supervised' and mentally filing it as 'unsupervised with extra steps'"
2. After pretext tasks: "I'll be honest - I thought jigsaw puzzles were a gimmick"
3. After InfoNCE: "The temperature parameter still trips me up"
4. After BYOL: "Nobody fully understands why BYOL works" 
5. After MAE: "I'm still developing intuition for why 75% masking is the sweet spot"

## Analogies
1. **Photo lineup analogy**: InfoNCE as police lineup - pick the suspect from lineup of look-alikes
2. **Jigsaw puzzle / detective analogy**: Pretext tasks as training exercises for detectives
3. **Apprentice watching master**: BYOL/DINO teacher-student as apprenticeship

## Rest Stop Placement
After MoCo - reader now understands contrastive learning fully (SimCLR + MoCo). 
Can stop here with "similar things close, different things far" mental model.
