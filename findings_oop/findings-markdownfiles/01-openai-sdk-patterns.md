# OpenAI SDK OOP Architecture

- Each API resource (Chat, File, Model) is a class with CRUD methods
- Base `APIResource` class defines generic retrieve/list/create
- `ChatCompletion`, `File`, etc. inherit and specialize
- `from_pretrained` and `create` are classmethods (factory methods)
- Singleton-like pattern for global config (API keys)
- Composition: HTTP client, response parsers, config objects are composed, not inherited
