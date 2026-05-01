# No Free Lunch Theorem — Deeper

## Beyond the Slogan
- Averaged over ALL possible problems, every algorithm performs equally
- But real-world problems aren't random — they have structure
- The theorem's real message: your assumptions (inductive bias) are everything
- Every algorithm is a bet on the structure of reality

## Inductive Bias Connection
- Linear models bet on linearity
- Decision trees bet on axis-aligned splits
- CNNs bet on translation invariance
- The NFL theorem says: pick the right bet for your problem

## Practical Consequences
- No single benchmark king translates to universal superiority
- Ensemble methods work because they hedge multiple bets
- Domain knowledge > algorithm sophistication
- Transfer learning fails when domains diverge (NFL predicts this)

## What Most People Get Wrong
- NFL does NOT mean "all algorithms are equal" — it means equal ONLY averaged over all possible distributions
- On any specific real-world problem, some algorithms are definitively better
- The theorem justifies experimentation, not nihilism
