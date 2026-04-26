# Scaling Laws

## Kaplan (2020, OpenAI)
- Three power laws: L(N), L(D), L(C)
- αN ≈ 0.076, αD ≈ 0.095, αC ≈ 0.050
- Conclusion: prioritize model size over data
- 10x compute → 5x params, 2x data
- Shaped GPT-3: 175B params, only 300B tokens

## Chinchilla (Hoffmann 2022, DeepMind)
- D ≈ 20 × N for compute-optimal training
- Both scale as √C
- Proof: Chinchilla 70B/1.4T beat Gopher 280B/300B at same compute
- GPT-3 was 12x undertrained by this standard

## Beyond Chinchilla
- LLaMA explicitly over-trains (7B on 1T tokens = 7x Chinchilla-optimal)
- Reason: inference cost depends on model size, training cost is one-time
- No new law has displaced Chinchilla for text LLMs as of 2024
- Data wall: publicly available internet estimated 5-15T tokens of quality text

## Emergent Abilities
- Capabilities appearing suddenly at scale thresholds
- Schaeffer et al. (2023): may be mirage of metric choice
- Continuous metrics show smooth improvement; discrete metrics show sharp transitions
