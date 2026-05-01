# Grokking

## Core Idea (Power et al., 2022)
- Model memorizes training data quickly (near-perfect train accuracy, chance test accuracy)
- Then MUCH later, suddenly generalizes — test accuracy jumps sharply
- Happens thousands of epochs after training loss has converged
- First observed on small algorithmic tasks (modular arithmetic, permutations)

## Why It's Fascinating
- Contradicts the idea that once training loss converges, learning is done
- Network transitions from a "memorization circuit" to a "generalizing circuit"
- The generalizing solution was always reachable, but took much longer to find
- Mechanistic interpretability studies show actual structural changes in the network during grokking

## Practical Implications
- Converged training loss ≠ done learning (especially on small datasets)
- Weight decay and regularization can speed up grokking dramatically
- Connects to: mechanistic interpretability, circuit-level understanding of networks

## Limitations
- Mostly observed on small, structured, algorithmic datasets
- Whether it occurs meaningfully in large-scale practical training is debated
- But the insight about delayed generalization is broadly important

## Interview Angle
- Know the phenomenon, know it challenges "early stopping" intuitions
- Connection to weight decay accelerating generalization
