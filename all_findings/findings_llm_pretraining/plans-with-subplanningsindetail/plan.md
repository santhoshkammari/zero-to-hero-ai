# Rewrite Plan for ch12/s01.html

## Running Example: Training a tiny language model for a recipe website
- Start with 3 recipes, 50 tokens
- Scale up to illustrate data curation, tokenizer choices, objectives, scaling decisions
- Return to it in every section

## Concept Ladder
1. Why pretraining? (motivation: the blank-brain problem)
2. Data: where does training text come from? (Common Crawl → toy crawl of 3 recipe sites)
3. Cleaning the mess (dedup, quality filtering — hands-on with recipe data)
4. Tokenizer training (BPE from scratch on recipe vocabulary)
5. Pretraining objectives: CLM (predict next ingredient), MLM (fill in the blank), Prefix LM
6. REST STOP — you now know enough to plan a small training run
7. Scaling laws: Kaplan (bigger model) vs Chinchilla (more data)
8. Compute-optimal training: the budget spreadsheet
9. Training infrastructure: clusters and interconnects
10. Training stability: loss spikes, checkpoint averaging, gradient clipping
11. Curriculum and data mixing strategies (DoReMi)
12. Wrap-up

## Vulnerability Moments
1. Opening confession: avoided understanding pretraining, treated models as black boxes
2. Dedup section: "I assumed web data was mostly unique. I was wrong by an embarrassing margin."
3. Scaling laws: "I still have to look up the Chinchilla ratio every time"
4. Loss spikes: "The first time I saw a loss spike, I thought the run was dead"
5. Data mixing: "No one is completely certain about the optimal data mix"

## Recurring Analogies
1. Kitchen/cooking analogy (ingredients = data, recipe = objective, oven = compute)
2. Library curation analogy (acquiring books, deduplicating, cataloging)
