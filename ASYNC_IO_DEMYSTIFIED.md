
Async IO Demystified
From Scratch

I avoided asyncio for longer than I'd like to admit. Every time I saw `async def` and `await` in someone's code, I'd nod politely and move on. Finally the discomfort of not knowing what's really happening under the hood grew too great for me. Here is that dive.

Asyncio is Python's built-in machinery for writing concurrent code that doesn't waste time waiting around. It was formalized in Python 3.4 and has been refined ever since. It's now the backbone of modern Python web frameworks, scrapers, bots, and anything that talks to the outside world.

Before we start, just a heads-up. We're going to be writing a lot of small Python programs and touching on some operating system concepts, but you don't need to know any of it beforehand. We'll add what we need, one piece at a time.

This isn't a short journey, but I hope you'll be glad you came.

    The waiting problem
    Blocking code
    Doing things while you wait
    Concurrency is not parallelism
    Callbacks: the first attempt
    The event loop
    Rest stop and an off ramp
    Generators: a detour worth taking
    Coroutines
    async and await
    Running the loop
    awaitables
    Tasks: fire and forget (almost)
    gather: running things together
    Real example: checking multiple websites
    asyncio.Queue and producer-consumer
    Common pitfalls
    When NOT to use asyncio
    Wrap up

The waiting problem

Programs spend a shocking amount of time doing nothing.

When your code asks the operating system to read a file, fetch a web page, or query a database, the CPU fires off that request and then just... sits there. It's waiting for a hard drive to spin, or for packets to travel across the ocean, or for a database server to think. These waits are called I/O operations, and they are slow. Not slow like "this loop has too many iterations" slow. Slow like "the speed of light through fiber optic cable across the Atlantic" slow.

To put some rough numbers on it, if a single CPU cycle took one second, then reading from RAM would take about 4 minutes. Reading from an SSD would take 1-3 days. And a network round trip to a server across the world? About 4 years.

Your CPU is extraordinarily fast. The world outside it is extraordinarily slow. The gap between the two is what asyncio exists to exploit.

Blocking code

Here's the simplest possible example of the problem. Imagine we're building a little tool that checks whether three websites are up.

```python
import time

def check_site(url):
    print(f"Checking {url}...")
    # Simulating a network request that takes 2 seconds
    time.sleep(2)
    print(f"{url} is up!")

start = time.time()
check_site("site-a.com")
check_site("site-b.com")
check_site("site-c.com")
print(f"Done in {time.time() - start:.1f} seconds")
```

```
Checking site-a.com...
site-a.com is up!
Checking site-b.com...
site-b.com is up!
Checking site-c.com...
site-c.com is up!
Done in 6.0 seconds
```

Six seconds. Each `check_site` call blocks — it seizes control and doesn't give it back until it's finished waiting. The second site can't start checking until the first one is done, even though the CPU is doing absolutely nothing during those two-second waits.

This is called blocking I/O. The word "blocking" is doing a lot of work here. It doesn't mean the function is computing something difficult. It means the function is sitting idle, refusing to let anything else happen until its wait is over.

Three sites, two seconds each, six seconds total. If we had a hundred sites, that's two hundred seconds. The tragedy is that all of those waits could overlap. We could start all three checks at once and be done in two seconds flat. That's what we're going to work toward.

Doing things while you wait

This is the core insight behind asyncio, and it's not a technical one. It's something you already do every day.

When you put bread in the toaster, you don't stand there staring at it. You go pour coffee. When the coffee is brewing, you check your phone. You're one person, but you're juggling several tasks by switching between them whenever one is waiting.

You are not doing three things simultaneously. You are doing one thing at a time, but you're smart about what you do while something else is blocked.

That's concurrency. One worker, many tasks, smart switching.

Concurrency is not parallelism

This is worth being very explicit about because the two get tangled up constantly.

**Parallelism** is having multiple workers doing things at the same time. Two cooks in a kitchen, each working on a different dish. In Python, this is what `multiprocessing` gives you — separate processes, each with its own CPU core.

**Concurrency** is one worker juggling multiple tasks by switching between them during wait times. One cook, but while the pasta is boiling, they're chopping vegetables. In Python, this is what `asyncio` gives you — one thread, but it switches tasks whenever one is waiting on I/O.

**Threading** is somewhere in between. It gives you multiple workers (threads), but in Python they're constrained by the GIL to take turns on the CPU anyway. The GIL — Global Interpreter Lock — is a rule baked into Python's most common implementation that says only one thread can execute Python code at a time, even if you have 16 CPU cores sitting idle. It's a famously controversial design choice. For I/O-bound work, it doesn't matter much because threads spend most of their time waiting, not computing. But it means that threading doesn't give you true parallelism for Python code.

For I/O-bound work, threading and asyncio solve similar problems. Asyncio does it with less overhead and more predictable behavior, which is why it's taken over.

If your work is I/O-bound (lots of waiting), asyncio is your tool. If your work is CPU-bound (lots of computing), you want multiprocessing. If you try to use asyncio for CPU-bound work, you'll be disappointed. It's not magic. It's just smart scheduling of wait times.

Callbacks: the first attempt

Before asyncio existed in its current form, the standard way to handle concurrent I/O was callbacks. The idea: instead of waiting for a result, you hand off a function to be called when the result is ready, and you move on.

```python
def on_site_checked(url):
    print(f"{url} is up!")

def check_site(url, callback):
    print(f"Checking {url}...")
    # imagine this registers the check and moves on immediately
    # when the response arrives later, callback gets called
    register_network_request(url, callback=lambda: callback(url))
```

This works. You can fire off all three checks without waiting, and when each one finishes, its callback runs. The problem is what happens when things get more complex.

```python
def step1(callback):
    fetch_user(user_id, lambda user:
        fetch_orders(user.id, lambda orders:
            fetch_details(orders[0].id, lambda details:
                callback(details))))
```

This is callback hell. Each step depends on the previous one, so they nest deeper and deeper. The code reads inside-out and bottom-up. Error handling becomes a nightmare. Debugging is miserable.

Callbacks are powerful but ergonomically brutal. They turn sequential logic into a tangled web of nested functions. People tolerated this for years, but everyone knew there had to be a better way.

The event loop

At the center of asyncio is a thing called the event loop. It's less mysterious than it sounds.

The event loop is a `while True` loop. That's it. I'll be honest — when I first read that, I didn't believe it. It felt like there had to be more. There is more plumbing, but the core concept really is that simple, and it took me a while to trust that. The loop runs forever (or until you tell it to stop), and on each iteration it checks: "Are any of my tasks ready to make progress?" If yes, it runs that task until the task says "I'm waiting on something." Then it moves to the next ready task.

Here's a cartoon version:

```
while there are tasks:
    for each task:
        if task is ready:
            run task until it says "I'm waiting"
            note what it's waiting for
    check if any waited-on things are now ready
```

That's the whole idea. The event loop is the cook in the kitchen, the single worker juggling tasks. It doesn't do any of the actual I/O. It orchestrates. It decides who runs when.

The beauty is that the switching happens at well-defined points — only when a task explicitly says "I'm waiting." This is cooperative multitasking. Tasks cooperate by voluntarily yielding control when they have nothing to do.

This is in contrast to threads, where the operating system can yank control away at any moment — even mid-sentence, even between two lines of your code. That's called preemptive multitasking, and it's the source of all those exciting race conditions that make multithreaded programming feel like defusing a bomb.

Rest stop and an off ramp

Congratulations on making it this far. You can stop if you want. The mental model of "one worker juggling tasks during wait times, coordinated by an event loop" is a genuinely useful way to think about asyncio. It captures the important concepts.

The next sections cover the mechanics of how Python actually implements this. If you just want to use asyncio and don't care about the guts, the short version is: write `async def` instead of `def`, write `await` before anything that waits, and use `asyncio.run()` to kick it off. There. You're 80% of the way there.

But if the discomfort of not knowing what's underneath is nagging at you, read on.

Generators: a detour worth taking

To understand coroutines, we first need to understand generators. They're the mechanical foundation on which asyncio was originally built.

A normal function runs from top to bottom and returns once.

```python
def count_up():
    return [1, 2, 3]
```

A generator function can pause partway through and resume later.

```python
def count_up():
    yield 1
    yield 2
    yield 3
```

The `yield` keyword is the magic word. When a generator hits `yield`, it hands a value back to whoever called it and freezes in place. All its local variables, its position in the code, everything is preserved. When you ask for the next value, it wakes up exactly where it left off and continues until it hits the next `yield`.

```python
gen = count_up()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

Between those `next()` calls, you can do anything you want. The generator is suspended, patiently holding its state, waiting to be resumed. I still find it slightly magical that a function can freeze in place and resume later, all its local variables intact. If that feels weird, sit with it — it felt weird to me too.

This ability — to pause a function, do something else, and come back later — is exactly what we need for concurrent I/O. Generators gave Python the machinery for cooperative multitasking.

To see the connection, let's build a tiny scheduler. Two generators, each pretending to do some work with waits in between, and a `while` loop that manually interleaves them:

```python
def task_a():
    print("A: start")
    yield  # "I'm waiting"
    print("A: middle")
    yield  # "I'm waiting again"
    print("A: done")

def task_b():
    print("B: start")
    yield
    print("B: done")

tasks = [task_a(), task_b()]
while tasks:
    task = tasks.pop(0)
    try:
        next(task)
        tasks.append(task)
    except StopIteration:
        pass
```

```
A: start
B: start
A: middle
B: done
A: done
```

Look at that. Two functions, interleaved, with a `while` loop driving them. The `yield` is each function raising its hand and saying "I've got nothing to do right now, go help someone else." The `while` loop is the event loop. This is asyncio in 12 lines. Everything else is refinement.

The insight that made asyncio possible: what if, instead of yielding nothing, a function could yield a description of what it's waiting for? "I'm waiting on a network response. Here, take this token. Wake me up when it's ready."

Coroutines

A coroutine is a generator that yields control instead of values. That's the conceptual leap.

In the early days of asyncio (Python 3.4), coroutines literally were generators with a decorator slapped on:

```python
import asyncio

@asyncio.coroutine
def check_site(url):
    print(f"Checking {url}...")
    yield from asyncio.sleep(2)
    print(f"{url} is up!")
```

The `yield from asyncio.sleep(2)` says "I need to wait 2 seconds. I'm yielding control back to the event loop. Wake me up when the time is up." The event loop notes the wake-up time, goes to run other tasks, and comes back when the 2 seconds are up.

This worked, but `yield from` was confusing. It looked like generators but meant something completely different. People kept mixing up generators (which produce values) with coroutines (which yield control). I'll admit I spent an embarrassing amount of time staring at `yield from asyncio.sleep(2)` trying to figure out what "value" `sleep` was yielding. The answer is: it doesn't matter. It's yielding control, not data. The confusion is real and it's not your fault. Python 3.5 fixed this by introducing dedicated syntax.

async and await

`async def` and `await` are syntactic sugar over coroutines. They don't add new capability. They add clarity.

```python
import asyncio

async def check_site(url):
    print(f"Checking {url}...")
    await asyncio.sleep(2)
    print(f"{url} is up!")
```

`async def` declares a coroutine function. Calling it doesn't run it — it creates a coroutine object, much like calling a generator function creates a generator object.

`await` is the new `yield from`. It means "run this other coroutine and suspend me until it's done." When the event loop sees an `await`, it knows: this task is handing back control. Go do something else.

Here's the critical thing: `await` is the only place where the event loop can switch tasks. Between `await` points, your code runs uninterrupted. Remember the cook — they only check the toaster when they've finished chopping the current vegetable. They don't drop the knife mid-chop. This is why asyncio doesn't have the race condition problems that threading has. You always know exactly where task switches can happen. If there's no `await` between two lines, no other task can sneak in between them.

Running the loop

A coroutine by itself does nothing. It needs an event loop to drive it.

```python
import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())
```

`asyncio.run()` creates an event loop, runs the coroutine until it completes, and then shuts down the loop. This is the standard entry point since Python 3.7. Before that, you had to create and manage the loop yourself, which was a mess.

But wait — this still runs one coroutine. Where's the concurrency?

Awaitables

Before we get to concurrency, it's worth being precise about what you can `await`. You can await three kinds of things. Coroutines are the most common — that's what you get when you call an `async def` function. Tasks are coroutines that have been handed to the event loop and scheduled to run — we'll meet these in the next section, and they're where the concurrency magic starts. Futures are low-level objects representing a result that doesn't exist yet — they're plumbing you rarely touch directly, but they're the foundation that tasks are built on.

You'll mostly work with coroutines and tasks. We'll get to why the distinction matters in a moment.

Tasks: fire and (almost) forget

Here's where concurrency actually starts.

When you `await` a coroutine directly, you wait for it to finish before moving on. That's sequential, not concurrent.

```python
async def main():
    await check_site("site-a.com")   # waits 2 seconds
    await check_site("site-b.com")   # waits 2 more seconds
    await check_site("site-c.com")   # waits 2 more seconds
    # total: 6 seconds. No better than blocking.
```

To run coroutines concurrently, you wrap them in Tasks. A Task tells the event loop "schedule this coroutine to run, but don't wait for it right now."

```python
async def main():
    task_a = asyncio.create_task(check_site("site-a.com"))
    task_b = asyncio.create_task(check_site("site-b.com"))
    task_c = asyncio.create_task(check_site("site-c.com"))

    await task_a
    await task_b
    await task_c
```

Now all three tasks are scheduled immediately. When `task_a` hits its `await asyncio.sleep(2)`, it yields control. The event loop picks up `task_b`, which also starts and then yields. Same for `task_c`. All three are now waiting simultaneously. When the 2 seconds are up, they all finish in rapid succession.

Let me trace through the event loop's iterations, because seeing it step by step is what made it click for me:

```
Iteration 1: task_a runs → prints "Checking site-a.com..." → hits await sleep(2) → yields
Iteration 2: task_b runs → prints "Checking site-b.com..." → hits await sleep(2) → yields
Iteration 3: task_c runs → prints "Checking site-c.com..." → hits await sleep(2) → yields
[all three are now sleeping, 2 seconds pass]
Iteration 4: task_a wakes up → prints "site-a.com is up!" → done
Iteration 5: task_b wakes up → prints "site-b.com is up!" → done
Iteration 6: task_c wakes up → prints "site-c.com is up!" → done
```

```
Checking site-a.com...
Checking site-b.com...
Checking site-c.com...
site-a.com is up!
site-b.com is up!
site-c.com is up!
Done in 2.0 seconds
```

Two seconds. Down from six. The CPU did the same amount of work. We just stopped wasting time.

gather: running things together

Creating tasks and awaiting them one by one is fine but verbose. `asyncio.gather` is a shortcut that runs multiple coroutines concurrently and collects their results.

```python
async def check_site(url):
    print(f"Checking {url}...")
    await asyncio.sleep(2)
    return f"{url} is up!"

async def main():
    results = await asyncio.gather(
        check_site("site-a.com"),
        check_site("site-b.com"),
        check_site("site-c.com"),
    )
    for r in results:
        print(r)
```

`gather` creates tasks for each coroutine, runs them concurrently, and returns a list of results in the same order you passed them in. It's the workhorse of asyncio concurrency. It has some sharp edges around error handling that we'll get to in the pitfalls section, but for the happy path, it just works.

There's also `asyncio.as_completed()` if you want to process results as they finish rather than waiting for all of them:

```python
async def main():
    coros = [check_site(url) for url in urls]
    for future in asyncio.as_completed(coros):
        result = await future
        print(result)  # prints in order of completion, not submission
```

And since Python 3.11, there's `asyncio.TaskGroup`, which adds structured concurrency. Structured concurrency is the idea that a group of concurrent tasks should have a clear lifetime — they all start together, and if one fails, the rest get cancelled rather than left dangling. It's a cleaner contract than `gather`:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(check_site("site-a.com"))
        tg.create_task(check_site("site-b.com"))
        tg.create_task(check_site("site-c.com"))
    # all done by the time we get here
```

The `async with` here is an async context manager — it works exactly like a regular `with` statement, but its setup and teardown steps are themselves awaitable. You'll see `async with` a lot in asyncio code, especially for managing connections and sessions that need async cleanup.

Real example: checking multiple websites

Let's put together a complete, runnable example that does actual network I/O. No more `sleep` pretending.

```python
import asyncio
import aiohttp
import time

async def check_site(session, url):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
            return f"{url} — {response.status}"
    except Exception as e:
        return f"{url} — Error: {e}"

async def main():
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org",
        "https://www.stackoverflow.com",
        "https://httpbin.org/delay/2",
    ]

    start = time.time()

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[check_site(session, url) for url in urls]
        )

    for r in results:
        print(r)

    print(f"\nDone in {time.time() - start:.1f} seconds")

asyncio.run(main())
```

Five websites, checked concurrently. The total time is roughly equal to the slowest single response, not the sum of all of them. That's the payoff.

Notice `aiohttp` instead of `requests`. The `requests` library is blocking — it doesn't know how to yield control to the event loop. You need async-aware libraries to get the benefit. This is the single biggest practical gotcha with asyncio, and we'll come back to it.

asyncio.Queue and producer-consumer

Another rest stop. If you just need to fire off a bunch of network calls and collect the results, you now have everything you need. `asyncio.run`, `create_task`, and `gather` will carry you a long way. What follows is for when your concurrent work has more structure — when some tasks produce data and others consume it — and for the mistakes that will bite you if you're not ready for them.

When your concurrent work has structure, `asyncio.Queue` is the coordination tool. Imagine we have 100 websites to check but only want 3 workers making requests at a time. That's a classic producer-consumer problem.

```python
import asyncio

async def producer(queue, urls):
    for url in urls:
        await queue.put(url)
    # signal that we're done
    for _ in range(3):  # one sentinel per consumer
        await queue.put(None)

async def consumer(queue, name):
    while True:
        url = await queue.get()
        if url is None:
            break
        print(f"{name}: checking {url}")
        await asyncio.sleep(1)  # simulate work
        print(f"{name}: {url} is up!")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    urls = [f"site-{i}.com" for i in range(9)]

    await asyncio.gather(
        producer(queue, urls),
        consumer(queue, "worker-1"),
        consumer(queue, "worker-2"),
        consumer(queue, "worker-3"),
    )

asyncio.run(main())
```

Three consumers pull URLs from the queue and check them concurrently. The queue handles all the coordination. No locks, no race conditions, no shared mutable state. This pattern scales cleanly to hundreds of concurrent workers.

Common pitfalls

After spending some time with asyncio, the same mistakes come up over and over. Here are the ones that bit me.

**1. Calling a coroutine without awaiting it**

```python
async def main():
    check_site("example.com")  # This does NOTHING
```

Calling an `async def` function returns a coroutine object. It doesn't execute it. You get a silent warning in the console if you're lucky. You need `await check_site("example.com")` or `asyncio.create_task(check_site("example.com"))`.

**2. Using blocking code inside async functions**

```python
async def bad():
    time.sleep(5)  # This blocks the ENTIRE event loop
```

`time.sleep` is not async-aware. It freezes the whole event loop for 5 seconds. Every other task stops. It's like the cook falling asleep at the counter — the toaster dings, the coffee finishes, but nobody's there to notice. Use `await asyncio.sleep(5)` instead, or for blocking libraries you can't avoid, use `asyncio.to_thread()` (Python 3.9+):

```python
async def okay():
    await asyncio.to_thread(time.sleep, 5)  # runs in a thread, doesn't block the loop
```

**3. CPU-bound work starving the event loop**

```python
async def compute_heavy():
    # This runs for 10 seconds without any await
    result = sum(i * i for i in range(100_000_000))
    return result
```

No `await` means no opportunity for the event loop to switch tasks. Everything else is frozen. For CPU-bound work, use `asyncio.to_thread()` (Python 3.9+) or `concurrent.futures.ProcessPoolExecutor`.

**4. Forgetting how gather handles exceptions**

By default, `gather` does not swallow exceptions — it raises the first one and lets it propagate. The problem is subtler: the remaining tasks keep running in the background, and if they also fail, those exceptions may get silently lost.

```python
results = await asyncio.gather(
    might_fail_1(),
    might_fail_2(),
    return_exceptions=True,  # Now exceptions are returned as values, not raised
)
# With return_exceptions=True, you can inspect each result
# and handle failures individually
```

I find `return_exceptions=True` almost always the right choice when gathering tasks that might fail independently. Without it, one bad apple cancels your ability to see what the other tasks did.

**5. Trying to run asyncio inside asyncio**

```python
async def outer():
    asyncio.run(inner())  # RuntimeError: cannot run nested event loops
```

You're already inside an event loop. Just `await inner()` directly.

When NOT to use asyncio

Asyncio is not universally better than synchronous code. It adds complexity — `async` and `await` infect your entire call stack. If you make one function async, every function that calls it needs to be async too, all the way up. This is sometimes called the function coloring problem: your code divides into two "colors" — sync and async — and they don't mix well. Once you paint one function async, the color spreads upward through every caller.

I wish someone had told me this earlier: don't reach for asyncio when your I/O is minimal. If you're reading one file and processing it, the overhead of the event loop machinery isn't worth it. Don't use it when your work is CPU-bound — asyncio can't parallelize computation, and you'll get better results from `multiprocessing`. Don't use it when your dependencies are all blocking — if you're committed to `requests`, `psycopg2`, or other blocking libraries and can't switch to async alternatives, you'll spend more time working around asyncio than benefiting from it. And don't use it for simple scripts. Not everything needs to be concurrent. Sometimes sequential code that finishes in 3 seconds is perfectly fine, and the simpler code is a feature, not a compromise.

Where asyncio shines is when you're making many network requests, building a web server or API, writing a bot or scraper, or running hundreds of I/O-bound tasks that can overlap. If your code spends most of its time waiting on the world outside the CPU, asyncio is almost certainly the right call.

Wrap up

If you're still with me, thank you. I hope it was worth it.

We started with the observation that programs waste enormous amounts of time waiting, and that a smart cook in a kitchen can juggle many dishes by switching between them during downtimes. We built up from blocking code to callbacks to generators to coroutines, each step motivated by the frustrations of the last. We arrived at `async`/`await`, Python's clean syntax for cooperative multitasking, and saw how tasks, gather, and queues give us practical tools for real concurrent work.

My hope is that the next time you see `async def` and `await` in someone's code, instead of nodding politely and moving on, you'll know exactly what's happening: one worker, many tasks, smart switching, and a `while True` loop making it all work.

I'll confess that even now, I occasionally get tripped up by the subtleties — a forgotten `await`, a blocking call that slips in, an exception that vanishes into the void. Asyncio rewards understanding over memorization. The more you internalize the event loop's perspective — "who's waiting? who's ready? what do I run next?" — the more natural it all becomes.

Resources

    Python asyncio documentation — the official reference.
    aiohttp — the async HTTP client/server library.
    Real Python's asyncio walkthrough — a thorough practical guide.
    David Beazley's "Build Your Own Async" talk — builds asyncio from scratch live on stage. Unforgettable.
    PEP 492 — the proposal that introduced async/await syntax.

