# Metaclasses & Descriptors - Findings

## Metaclasses
- A class whose instances are classes - controls class creation
- Django ORM ModelBase: auto-registers models, sets up field mappings, wires signals
- SQLAlchemy uses similar patterns
- __init_subclass__ (3.6+) covers 80% of metaclass use cases more simply
- Rule: if you think you need a metaclass, try __init_subclass__ or class decorator first

## Descriptors
- Objects implementing __get__, __set__, __delete__
- property, classmethod, staticmethod are ALL descriptors
- Data descriptors (with __set__) override instance __dict__
- Non-data descriptors (only __get__) can be overridden by instance attrs
- __set_name__ (3.6+) - descriptor learns its own attribute name

## Lookup Order
1. Data descriptor on class
2. Instance __dict__
3. Non-data descriptor on class

## Production Relevance
- You READ code using these, rarely write them yourself
- Understanding descriptors demystifies @property, @classmethod magic
- ORMs and validation frameworks are built on these
