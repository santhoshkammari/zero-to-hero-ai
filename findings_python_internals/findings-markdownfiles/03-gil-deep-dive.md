# GIL Deep Dive

## Implementation
- Mutex in ceval.c, condition variable for thread switching
- gil_locked boolean, gil_last_holder for priority
- Threads yield every ~5ms (sys.setswitchinterval())
- C extensions release with Py_BEGIN_ALLOW_THREADS / Py_END_ALLOW_THREADS

## Why It Exists
- Reference counting is not thread-safe
- Two threads doing Py_DECREF simultaneously = memory corruption
- Fine-grained per-object locks would slow single-threaded code (the common case)

## Where It Doesn't Matter
- NumPy/PyTorch release GIL during C computation
- I/O operations release the GIL
- sklearn n_jobs uses multiprocessing internally

## Free-Threaded Python (PEP 703)
- Python 3.13: experimental --free-threading build
- ~10% single-threaded slowdown due to biased reference counting
- Dramatic multi-threaded speedups possible
- Ecosystem still catching up (NumPy, pandas being updated)
- Production readiness: late 2025+ realistically
