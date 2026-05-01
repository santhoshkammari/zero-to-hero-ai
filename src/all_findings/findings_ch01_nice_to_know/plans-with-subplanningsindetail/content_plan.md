# Content Plan: Ch01 S15 - Nice to Know

## Overall Approach
Brandon Rohrer style - narrative journey, not a listicle. Running example: building a small ML experiment tracker CLI tool. Each topic introduced because the tool needs it, not because "it's next on the list."

## Structure

### Opening
- Personal confession: kept hitting weird Python in other people's code
- The "what the heck is this" moment when reading framework source

### Running Example
A small experiment tracker - we encounter each "nice to know" feature naturally as we build/debug it.

### Topics (in narrative order, motivated by need):

1. **The Gotchas That Bite First** - mutable defaults, late binding closures, is vs ==
   - Motivated by: debugging our tracker and finding shared state bugs
   - Toy example: the mutable default list that accumulates across calls

2. **Decorators Under the Hood** - the machinery, functools.wraps, factories, stacking
   - Motivated by: wanting to add timing/logging to our tracker functions
   - Show how stacking order matters, how wraps preserves identity

3. **Context Managers** - __enter__/__exit__, contextlib, ExitStack
   - Motivated by: managing file handles and DB connections in tracker
   - The generator-based approach with @contextmanager

4. **Descriptors & The Machinery Behind @property**
   - Motivated by: reading framework code and seeing __get__/__set__
   - How property, classmethod, staticmethod are all descriptors

5. **Metaclasses: The Nuclear Option**
   - Motivated by: reading Django/SQLAlchemy source
   - __init_subclass__ as the 80% solution
   - When you actually need a metaclass vs not

6. **Modern Python Worth Knowing**
   - Walrus operator, pattern matching, f-string debug mode
   - Dataclasses advanced (slots, frozen, kw_only)
   - Type hints beyond basics (Protocol, ParamSpec)

### Rest Stop
After gotchas + decorators + context managers - "you're already ahead of most"

### Wrap-up
- These aren't daily tools, they're recognition tools
- Next time you see __get__ in source code, you won't flinch

## Vulnerability Moments
1. Admit getting burned by mutable default in production
2. Confess still double-checking decorator stacking order
3. Acknowledge metaclasses are genuinely confusing
4. Admit the descriptor lookup order is hard to memorize

## Recurring Analogies
1. Toolbox analogy: daily drivers vs specialty tools you pull out twice a year
2. X-ray vision: these features let you see through framework "magic"
