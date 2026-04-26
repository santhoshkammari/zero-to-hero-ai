# Asyncio Internals

## Coroutines are Enhanced Generators
- async def creates coroutine objects with __await__
- await is essentially yield from - drives coroutine until it yields
- Coroutines are state machines, pausing/resuming at await points

## Event Loop
- Single thread running a loop: select/poll/epoll (Linux), kqueue (Mac), IOCP (Windows)
- selector.select(timeout) blocks until an event or timeout
- When event fires, corresponding coroutine is resumed

## Key Insight
- Not parallelism, it's cooperative multitasking
- One thread juggles thousands of tasks by switching at await points
- Ideal for I/O-bound work with many concurrent connections
- Does NOT help CPU-bound work at all
