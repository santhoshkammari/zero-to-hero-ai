# Rewrite Plan: Python Under the Hood

## Running Example: Building a log ingestion pipeline
- Start small: process 3 log files
- Scale up: 10,000 files, API calls, CPU-bound parsing
- Thread through every section

## Concept Ladder (dependency order)
1. What happens when you type `python script.py` (execution pipeline)
2. Everything is a PyObject (memory model foundation)
3. Reference counting (how memory is freed)
4. Garbage collector (when refcounting fails)
5. The GIL (why threads don't run in parallel)
6. Threading vs Multiprocessing (practical concurrency)
7. Asyncio (cooperative multitasking for I/O)
8. The future: free-threaded Python

## Rest Stop
After GIL section - reader now understands memory + GIL, can diagnose most issues

## Recurring Analogies
1. Kitchen analogy: one chef (GIL), multiple prep stations (threads), separate kitchens (processes)
2. Post office mailroom: sorting (CPU-bound) vs waiting for delivery (I/O-bound)

## Vulnerability Moments
1. "I avoided looking at CPython source for years"
2. "I still get tripped up by views vs copies in NumPy"
3. "I'm still developing intuition for when async beats threading"
4. "I once spent a day debugging a memory leak that was just dangling references"
