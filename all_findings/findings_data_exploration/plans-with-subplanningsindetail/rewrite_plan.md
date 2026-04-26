# Rewrite Plan: Data Exploration (ch03/s01)

## Running Example
A small e-commerce dataset: 6 columns (user_id, age, city, purchase_amount, signup_date, churned)
Start with 8 rows, grow as needed. Relatable, production-relevant.

## Concept Ladder (dependency order)
1. Why EDA matters at all (Anscombe's Quartet motivation)
2. The first look: shape, types, memory (the 30-second scan)
3. Data types that affect modeling (nominal/ordinal/continuous/time)
4. File formats (Parquet vs CSV — why it matters)
5. Summary statistics — and why they lie (datasaurus dozen)
6. Distribution analysis (skewness, kurtosis, multimodality, sentinel values)
7. Missing data — the three mechanisms (MCAR/MAR/MNAR)
8. REST STOP
9. Relationships and correlations (Pearson vs Spearman, Simpson's paradox)
10. Target variable analysis (class imbalance, leakage detection)
11. Data quality and integrity (duplicates, schema validation, domain checks)
12. Automated profiling tools (ydata-profiling, sweetviz, whylogs)
13. Wrap-up

## Recurring Analogies
1. "Medical checkup" — EDA is like a doctor's checkup before surgery (model building)
   - Returns when discussing symptoms (distributions) vs diagnosis (root cause)
   - Returns in production context (regular checkups, not one-time)
2. "Crime scene investigation" — each piece of evidence (column) tells part of the story
   - Returns with correlation (connecting evidence), leakage (planted evidence)

## Vulnerability Moments
1. Opening: avoided EDA, went straight to modeling, model was garbage
2. Anscombe's quartet: "I didn't believe identical stats could look that different"
3. Missing data: "I still get tripped up distinguishing MAR from MNAR"
4. Correlation: confession about Simpson's paradox surprising me
5. Target leakage: "I once spent a week debugging a model that was 'too good'"

## Rest Stop Placement
After missing data section — reader now has: shape, types, distributions, missing patterns
Useful mental model for basic dataset understanding
