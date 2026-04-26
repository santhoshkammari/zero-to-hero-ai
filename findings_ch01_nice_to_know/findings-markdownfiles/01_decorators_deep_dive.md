# Decorators Deep Dive - Findings

## Key Insights
- Decorators are syntactic sugar: `@dec` on `def f` is just `f = dec(f)`
- Stacking: `@a @b def f` = `f = a(b(f))` - innermost applied first
- `functools.wraps` preserves __name__, __doc__, __module__ - critical for debugging
- Without wraps, decorated functions lose their identity in tracebacks
- Decorator factories (decorators with arguments) add an extra nesting level
- Class-based decorators use __call__ - useful for maintaining state (e.g., call counting)
- ParamSpec (3.10+) finally lets you type-hint decorators that preserve signatures

## Production Relevance
- Every Python framework uses decorators heavily (Flask routes, pytest fixtures, Django views)
- Missing functools.wraps causes debugging nightmares - stack traces show "wrapper" instead of real function name
- Understanding decorator order matters when stacking auth + logging + caching decorators

## Interview Angles
- "What happens when you stack decorators?" - execution order question
- "Why does functools.wraps matter?" - practical debugging question
- Understanding that decorators are just higher-order functions
