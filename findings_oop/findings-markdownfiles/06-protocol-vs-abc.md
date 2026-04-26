# Protocol Classes vs ABC

- ABC: nominal subtyping (must inherit), runtime checks with isinstance
- Protocol (PEP 544, 3.8+): structural subtyping, no inheritance needed
- Protocol = "static duck typing" — checked by mypy/pyright without requiring inheritance
- Use Protocol for flexible data adapters, callbacks, plugin systems
- Use ABC when you need runtime isinstance checks or explicit class hierarchies
- Modern ML code increasingly uses Protocol for cleaner interfaces
