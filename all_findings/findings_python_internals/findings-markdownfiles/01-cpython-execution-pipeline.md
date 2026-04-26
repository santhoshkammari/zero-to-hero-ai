# CPython Execution Pipeline

## Key Insights
- Source code → Parser → AST → Bytecode Compilation → VM Execution
- Code objects contain co_code (bytecode), co_consts, co_names, co_varnames
- dis module reveals the opcodes: LOAD_FAST, LOAD_CONST, BINARY_OP, RETURN_VALUE
- .pyc files in __pycache__/ are marshalled code objects
- Python 3.11+ has adaptive/quickened bytecode that specializes at runtime
- The main interpreter loop lives in ceval.c - a giant switch statement
- Frame objects store local/global variables, stack, instruction pointer per call

## Why This Matters for ML Engineers
- Understanding bytecode explains why Python loops are slow (each iteration = multiple bytecode ops)
- Explains why vectorized NumPy is fast (one bytecode call into C)
- dis module is practical for understanding performance characteristics
