# Python Gotchas - Findings

## Mutable Default Arguments
- Defaults evaluated ONCE at function definition, not per call
- Shared mutable default = bugs across calls
- Fix: use None sentinel, create inside function body

## Late Binding Closures
- Closures capture variables by REFERENCE not value
- Loop + lambda = all lambdas share last loop value
- Fix: default argument trick `lambda i=i: i`

## is vs ==
- is: identity (same object in memory)
- ==: equality (same value)
- CPython caches small integers (-5 to 256) and interned strings
- `a = 256; b = 256; a is b` → True (cached)
- `a = 257; b = 257; a is b` → False (not cached, usually)

## Shallow vs Deep Copy
- copy.copy: new outer container, same inner objects
- copy.deepcopy: recursively copies everything
- Nested mutables + shallow copy = shared mutation bugs

## The GIL
- Only one thread executes Python bytecode at a time (CPython)
- Threading helps I/O-bound, NOT CPU-bound
- multiprocessing for CPU parallelism
- asyncio for I/O concurrency without threads
