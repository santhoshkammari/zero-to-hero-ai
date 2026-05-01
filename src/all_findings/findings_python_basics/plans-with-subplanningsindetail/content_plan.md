# Python Basics Section - Content Plan

## Running Example: Building a tiny ML experiment tracker
- Start with tracking 3 experiment results
- Grows naturally to need dicts, generators, decorators, error handling
- Relatable: every ML engineer needs to track experiments

## Concept Ladder (dependency order):
1. Variables as name bindings (not boxes) - the mental model shift
2. Mutable vs immutable - why this distinction exists
3. Data structures - list, dict, set, tuple - when to use which
4. Iteration protocol - for loops, iterators, generators
5. Functions as objects - first-class functions
6. Closures and decorators - the power tools
7. Context managers - resource safety
8. Exception handling - EAFP philosophy
9. Comprehensions and Pythonic patterns
10. Type hints - why they matter at scale

## Rest Stop: After data structures + iteration
- Reader has enough to write real Python for ML
- Can process data, loop through it, choose right containers
- But missing the power tools: decorators, generators, context managers

## Vulnerability Moments:
1. "I avoided understanding the memory model for years" (opening)
2. "The mutable default argument bug hit me in production" 
3. "I still sometimes forget generators can only be iterated once"
4. "I'm still developing intuition for when Protocol beats ABC"

## Analogies:
1. Variables as post-it notes on objects (not boxes containing values)
2. Iterator as a bookmark in a book (can only move forward)
3. Decorator as a gift wrapper (the gift stays the same, wrapping adds behavior)
