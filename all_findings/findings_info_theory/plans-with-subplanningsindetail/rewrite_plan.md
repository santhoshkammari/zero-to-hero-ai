# Rewrite Plan: Information Theory Section

## Running Example: Weather Prediction App
A tiny weather app that predicts tomorrow's weather from {sunny, rainy, cloudy}. 
Starts with 3 outcomes, scales as we add more complexity.

## Concept Ladder (each motivated by limitation of previous)
1. **Surprise & Entropy** — Start with "what is information?" using weather predictions
2. **Cross-Entropy** — Our model's predictions vs reality → how do we measure model quality?
3. **KL Divergence** — The exact gap between model and truth → forward vs reverse
4. **Mutual Information** — Which features actually help predict weather? 
5. **Data Processing Inequality** — Why garbage in = garbage out, formalized
6. **Information Bottleneck** — What deep networks actually learn to do
7. **Fisher Information** — How sensitive is our model to parameter tweaks?
8. **The Bigger Picture** — MDL, variational inference, why information theory IS the language of ML

## Rest Stop After: KL Divergence section (you now understand the loss function deeply)

## Vulnerability Moments
1. Opening: avoided information theory because it felt like physics, not ML
2. After entropy formula: "the log base was the thing that tripped me up for years"
3. Forward vs reverse KL: "I'll be honest, I mixed these up repeatedly"
4. Information bottleneck: "still developing intuition for whether compression phase is universal"
5. Fisher information: "I haven't figured out a great way to visualize this"

## Analogies
1. **Filing cabinet** — entropy as how messy/organized your cabinet is. Recurs for compression.
2. **Translation phrasebook** — cross-entropy as using wrong phrasebook for a language. Recurs for KL.
