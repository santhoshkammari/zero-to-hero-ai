# Rewrite Plan for ch01/s03.html

## Approach: Brandon Rohrer Style
- Personal confession opening about avoiding OOP
- Running example: building a mini ML training framework from scratch
- Build from "why" not "what"
- Each section motivated by a limitation of the previous approach

## Section Flow:
1. Opening (confession, orientation, heads-up, invitation)
2. Table of Contents
3. The Spaghetti Script (start with no OOP — show the pain)
4. The First Class (encapsulation — group related things)
5. The Contract (why interfaces matter — ABC, Protocol)
6. Inheritance: When the Framework Says So (nn.Module, BaseEstimator)
7. Composition: When You're Building Your Own Thing (has-a beats is-a)
8. Rest Stop
9. The Patterns You'll Actually See (Template Method, Strategy, Observer, Registry)
10. The Dunder Methods That Earn Their Keep (__call__, __len__, __getitem__, __enter__)
11. The Modern Toolkit (dataclasses, Protocol, frozen configs)
12. The Anti-Patterns That Kill Codebases (God class, deep inheritance, global state)
13. Wrap-Up
14. Resources

## Running Example: Building "minitrainer" — a tiny training framework
- Start: messy script with functions everywhere
- Evolve into classes, then composition, then real patterns
- Thread through every section

## Vulnerability Moments:
- "I avoided OOP for years — functions were fine"
- "I still get tripped up by MRO in diamond hierarchies"  
- "I'm still developing my intuition for when ABC vs Protocol is the right call"
- "I once spent a day debugging a mutable class attribute"
- "No one fully agrees on the right level of abstraction"
