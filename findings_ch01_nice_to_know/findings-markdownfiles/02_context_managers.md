# Context Managers - Findings

## Key Insights
- __enter__/__exit__ protocol - exit gets exception info, can suppress by returning True
- contextlib.contextmanager - generator-based, code before yield = enter, after = exit
- ExitStack - dynamic context management for unknown number of resources
- suppress() - clean way to ignore specific exceptions
- Async context managers: __aenter__/__aexit__ for async with

## Production Relevance
- Database connections, file handles, locks, temporary state changes
- ExitStack is invaluable in testing and when opening variable number of files
- Real pattern: managing GPU memory contexts in ML training loops

## Why It Matters
- Resource leaks are silent killers in production
- Context managers guarantee cleanup even on exceptions
- The generator-based approach with @contextmanager is how most library authors write them
