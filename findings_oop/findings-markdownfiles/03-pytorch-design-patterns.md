# PyTorch nn.Module Design Patterns

- Template Method: __call__() runs hooks then delegates to forward()
- Strategy: pass activation functions/modules as constructor args for runtime swapping
- Observer: forward/backward hooks for debugging, gradient clipping, feature extraction
- Composition: nn.Sequential, nn.ModuleList, nn.ModuleDict for building from simple parts
- Parameter auto-discovery: assigns nn.Parameter and sub-modules automatically via __setattr__
