# HuggingFace Registry + Factory Patterns

- PreTrainedModel: base class with save/load/from_pretrained
- AutoModel: registry that maps config.model_type to concrete class
- Flow: load config → read model_type → lookup in registry → instantiate correct class → load weights
- Same pattern: AutoTokenizer, AutoConfig, AutoModelForSequenceClassification
- Factory method from_pretrained is a classmethod on the base, inherited by all
