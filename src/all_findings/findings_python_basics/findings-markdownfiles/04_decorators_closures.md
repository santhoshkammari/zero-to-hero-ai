# Decorators, Closures, First-Class Functions

## First-Class Functions
- Functions are objects: can be passed, returned, assigned
- This is the foundation for decorators and functional patterns

## Closures
- Inner function captures variables from enclosing scope
- Variables are captured by reference, not value (late binding!)
- The closure cell keeps the variable alive after outer function returns

## Decorators
- @decorator is syntax sugar for func = decorator(func)
- A function that takes a function and returns a modified function
- functools.wraps preserves original function's metadata
- Real uses: logging, caching (lru_cache), retry, auth, timing

## Production patterns
- @retry for flaky API calls
- @lru_cache for expensive computations
- @torch.no_grad() for inference
- Custom decorators for input validation
