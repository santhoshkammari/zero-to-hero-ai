# PAC Learning

## Core Framework
- "Probably Approximately Correct" — Leslie Valiant, 1984
- Formalizes: how much data do you need to learn "well enough" with confidence?
- Two knobs: ε (error tolerance) and δ (failure probability)
- Sample complexity: n ≥ (1/ε)(log|H| + log(1/δ)) for finite hypothesis spaces

## VC Dimension Connection
- For infinite hypothesis spaces, VC dimension replaces log|H|
- VC dimension = max number of points a model can shatter (classify in all 2^n ways)
- Linear classifier in 2D has VC dim 3 (can shatter any 3 points, not 4)

## Why Practitioners Should Care
- Gives mathematical grounding to "more complex model needs more data"
- Connects model capacity → data requirements → generalization
- Structural Risk Minimization: minimize empirical risk + complexity penalty
- This is the THEORY behind regularization, early stopping, model selection

## Limitations
- PAC bounds are often extremely loose in practice
- Modern deep learning violates classical PAC predictions (double descent)
- Still valuable as conceptual framework even when bounds aren't tight
