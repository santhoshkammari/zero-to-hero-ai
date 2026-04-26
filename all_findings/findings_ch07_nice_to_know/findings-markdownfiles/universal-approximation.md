# Universal Approximation Theorem

## Core Idea
- Cybenko (1989), Hornik (1991): a single hidden layer with enough neurons can approximate any continuous function on a compact set
- It's an existence theorem — says "can" not "will"
- Says nothing about: how many neurons needed, whether gradient descent finds the solution, sample efficiency, generalization

## Why It Matters
- Theoretical backbone for "neural nets are universal function approximators"
- But misleading if you stop there — it's like saying "a polynomial of high enough degree can fit any curve" (true, but not useful)
- In practice, depth >> width for parameter efficiency
- Deep nets build hierarchical representations; wide shallow nets waste parameters

## Interview Angle
- "True but misleading" — know why both halves matter
- Depth allows exponentially more compact representations than width (Telgarsky 2016)
- The theorem doesn't explain why deep learning works — it explains why it CAN work

## Key Gotcha
- People cite this to justify neural nets but it applies to ANY sufficiently flexible function class
- The real question is optimization + generalization, not expressiveness
