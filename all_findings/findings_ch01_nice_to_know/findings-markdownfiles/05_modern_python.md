# Modern Python Features - Findings

## Walrus Operator (:=) - 3.8
- Assign and use in one expression
- Shines in while loops with input, comprehension filters

## Structural Pattern Matching - 3.10
- match/case with destructuring
- Works on sequences, mappings, classes
- __match_args__ in dataclasses

## Exception Groups - 3.11
- except* for handling multiple simultaneous exceptions
- Critical for asyncio.TaskGroup

## Type Parameter Syntax - 3.12
- def first[T](items: list[T]) -> T
- No more TypeVar boilerplate

## Protocol - 3.8+
- Structural subtyping / compile-time duck typing
- If it has the methods, it satisfies the protocol

## ParamSpec - 3.10
- Type decorators that preserve function signatures

## Dataclasses Advanced
- slots=True (3.10): memory efficient, faster attr access
- frozen=True: immutable instances
- kw_only=True (3.10): keyword-only fields
- field(default_factory=...) for mutable defaults
- __post_init__ for validation
