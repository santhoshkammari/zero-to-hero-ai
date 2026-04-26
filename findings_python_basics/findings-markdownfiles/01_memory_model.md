# Python Memory Model & Object System

## Key Insights
- Variables are name bindings (labels/post-it notes), NOT containers
- Everything is an object on the heap; variables hold pointers
- Assignment never copies - it binds another name to same object
- id() returns memory address in CPython
- `is` checks identity (same object), `==` checks equality (same value)
- Integer interning: -5 to 256 are cached singletons
- String interning for identifiers
- Reference counting + cyclic GC (generational: gen 0, 1, 2)
- PyObject struct: refcount + type pointer

## Production Gotchas
- Mutable default arguments: evaluated ONCE at function definition
- Late binding closures: capture variable, not value
- Shallow vs deep copy for nested mutables
- `b = a` for lists copies reference, not data
- `[[0]*3]*3` creates 3 refs to SAME inner list
