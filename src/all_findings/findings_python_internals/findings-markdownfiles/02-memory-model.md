# Python Memory Model

## PyObject - The Foundation
- Every Python object is a C struct starting with PyObject: ob_refcnt + ob_type
- Everything is heap-allocated, variables are pointers
- ob_type points to PyTypeObject with function pointers for behavior

## Reference Counting
- ob_refcnt tracks references, immediate deallocation at zero
- Py_INCREF/Py_DECREF at C level
- sys.getrefcount() adds 1 for the argument itself

## Generational GC
- 3 generations: Gen 0 (new), Gen 1 (survived once), Gen 2 (long-lived)
- Only handles reference cycles, not general cleanup
- gc.disable() pattern in training loops, gc.collect() between epochs

## pymalloc Arena Allocator
- Custom allocator for objects ≤ 512 bytes
- Arenas (256KB) → Pools (4KB) → Blocks (size classes)
- Faster than system malloc for frequent small allocations

## Optimization Tricks
- Small integer cache: -5 to 256 pre-allocated at startup
- String interning: identifiers stored once, reused
- None, True, False are singletons
- Empty tuple is cached
