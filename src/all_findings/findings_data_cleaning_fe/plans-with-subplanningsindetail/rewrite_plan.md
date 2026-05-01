# Rewrite Plan for ch03/s03.html

## Running Example
A small apartment rental pricing dataset - 6 apartments with features like sqft, neighborhood, has_parking, listed_date, and some missing values. This threads through the entire section.

## Concept Ladder (each motivated by limitation of previous)
1. **The Mess** - Raw data is never clean. Our rental dataset has missing values, weird types, inconsistent strings.
2. **Missing Data** - Why values vanish (MCAR/MAR/MNAR). What to do about it. The danger of imputing the target.
3. **Outliers** - That one apartment listing for $1/month. Error or signal? How to decide.
4. **Feature Scaling** - Models that use distance are fooled by scale differences. When to care, when not to.
5. **Log Transforms** - Taming long right tails (rent prices, income).
6. **REST STOP** - You can clean data now. That's already powerful.
7. **Categorical Encoding** - Models eat numbers. How to translate categories (neighborhood names) into numbers without lying.
8. **Creating Features** - The real gains: ratios, interactions, aggregations, datetime features, cyclical encoding.
9. **Data Leakage** - The silent model killer. Train-test contamination, target leakage, temporal leakage.
10. **Wrap-up** - Gratitude, recap, future hope.

## Vulnerability Moments
1. Opening: confessing I avoided data cleaning because it felt "un-glamorous"
2. Missing data: admitting I once imputed the target variable by accident
3. Encoding: still get confused by when to use drop='first' 
4. Feature engineering: oversimplified when I said "domain knowledge" as if it's obvious
5. Leakage: confessing a leakage bug that took days to find

## Recurring Analogies
1. **Kitchen analogy**: Data cleaning = prep work before cooking. You don't start with unwashed, uncut ingredients.
2. **Translation analogy**: Encoding = translating between languages. Some translations lose meaning, some don't.

## Style
- Brandon Rohrer voice: practitioner, not professor
- First person narrative
- No "simply", "just", "obviously"
- Toy examples walked through step by step
- Every concept motivated by limitation of previous
