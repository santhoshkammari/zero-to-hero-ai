# Why OOP Matters in Production ML

- Google's TFX: each pipeline component (Trainer, Evaluator, Pusher) is a class with standard I/O
- Meta's FBLearner Flow: pluggable OOP-based pipelines
- Interface consistency across teams: standard .fit(), .predict(), .load(), .save()
- SOLID principles in ML: SRP for data loaders vs trainers, OCP for abstract base classes, LSP for any custom model working in pipelines, DIP for injecting models/data stores
- Composition wins 80% of the time; inheritance only when frameworks require it
