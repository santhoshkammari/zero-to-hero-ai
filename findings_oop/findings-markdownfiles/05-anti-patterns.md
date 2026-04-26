# OOP Anti-Patterns in ML

- God Class: one class does model def, data handling, training, logging, metrics
- Deep inheritance: 4+ levels deep, can't trace where methods are defined
- Too much magic: reflection, monkey-patching, **kwargs everywhere
- Global state: singleton config objects used everywhere
- Fix: composition over inheritance, dependency injection, explicit is better than implicit
