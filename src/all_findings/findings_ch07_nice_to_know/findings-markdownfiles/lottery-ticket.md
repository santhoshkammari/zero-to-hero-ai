# Lottery Ticket Hypothesis

## Core Idea (Frankle & Carlin, 2019)
- Inside a randomly initialized dense network, there exist sparse subnetworks ("winning tickets")
- These subnetworks can match full network performance when trained from their ORIGINAL initialization
- Key: it's not just the structure, it's the specific initial weights that matter
- Found via iterative magnitude pruning: train → prune smallest weights → rewind to original init → repeat

## Why It's Wild
- Can remove 90%+ of parameters without meaningful accuracy loss
- Large networks succeed not because they need all parameters, but because they contain at least one winning ticket
- The lottery analogy: buying more tickets (parameters) increases chance of winning

## Practical Impact
- Model compression for edge/mobile deployment
- Explains why overparameterization helps training (more tickets → higher chance of a winner)
- Led to research on finding winning tickets cheaply (without full training cycle)

## Limitations
- Finding winning tickets requires training the full network first (expensive)
- Scaling to very large models (transformers) is still active research
- "Late rewinding" variant: rewind to early training (not init) works better for larger models

## Interview Gotcha
- "If small networks can match large ones, why train large?" → because we can't identify the winning ticket without training the large one first
