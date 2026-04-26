# LLM Evaluation Research Summary

## Perplexity
- Exp of avg neg log-likelihood: PPL = exp(-1/N * Σ log P(xi|x1...xi-1))
- PPL of 10 means model is as confused as choosing from 10 options
- Lower = better. Sensitive to tokenization, domain, cannot compare across tokenizers
- Does NOT measure usefulness, safety, factual accuracy

## Key Benchmarks
- **MMLU**: 57 subjects, 14k+ MCQ. Saturating >90%. MMLU-Pro: 10 options instead of 4, harder
- **HellaSwag**: Commonsense sentence completion. Saturated >95%
- **HumanEval**: 164 code problems, pass@k metric. Still useful
- **GSM8K**: 8500 grade-school math. Tests CoT reasoning. Saturating
- **ARC**: Science reasoning MCQ (Easy + Challenge)
- **TruthfulQA**: 817 questions designed to trigger misconceptions
- **MT-Bench**: 80 multi-turn questions, GPT-4 judged, 1-10 score, 8 categories

## Chatbot Arena / Elo
- LMSYS crowdsourced blind pairwise battles
- Elo rating system from chess
- Users don't know which model is which
- Most robust eval - can't game it (until Meta Llama 4 scandal)

## LLM-as-Judge
- G-Eval: Use GPT-4 to evaluate outputs with rubrics
- Patterns: single-score, pairwise comparison, reference-guided
- Biases: position, verbosity, self-preference, format/authority
- >80% agreement with human annotators
- $0.01-0.10 per sample vs $10-50+ for human eval

## Benchmark Gaming & Contamination
- Training data includes benchmark questions (web crawl leakage)
- Models memorize rather than reason
- Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure"
- Llama 4 Arena manipulation scandal
- 2024 "evaluation crisis"

## Evaluation Frameworks
- lm-eval-harness (EleutherAI): plug-and-play, hundreds of tasks
- HELM (Stanford): holistic - accuracy, bias, robustness, toxicity, calibration

## Custom Evals / Production
- Build 50-200 examples from real use cases
- Eval flywheel: deploy → find failures → add to eval set → improve → redeploy
- LLM-as-judge in CI/CD for fast iteration
- Human eval for safety-critical, final validation
- Every production failure = new test case
