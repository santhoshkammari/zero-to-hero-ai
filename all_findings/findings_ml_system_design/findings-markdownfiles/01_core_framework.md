# ML System Design - Core Framework

## Running Example: Movie Recommendation System for "StreamFlix"
- Start tiny: 3 users, 5 movies
- Grow naturally through each concept
- Thread from problem formulation through serving and monitoring

## Concept Ladder (dependency order):
1. Why ML system design matters (the model is the smallest part)
2. Problem formulation - translating business to ML (running example: StreamFlix)
3. Metrics hierarchy - offline vs online vs business
4. Data strategy - where signal lives
5. Feature engineering at scale - the feature store concept
6. Model selection - matching complexity to problem
7. Training pipeline design
8. Serving architecture - batch vs real-time vs hybrid
9. Feedback loops - the system eating its own tail
10. Design patterns - retrieve→rank, cascade, shadow mode
11. Full walkthrough: recommendation system, fraud detection, search ranking, content moderation
12. Iterative improvement - the flywheel

## Key Insights from Research:
- Google's "Hidden Technical Debt" paper: ML code is tiny rectangle, everything around it dwarfs it
- Two-tower models for candidate generation (user tower + item tower)
- Cascade pattern: cheap first, expensive last (90% handled by cheap models)
- Training-serving skew is the silent killer
- Feedback loops amplify biases and create echo chambers
- Delayed labels in fraud detection (chargebacks take weeks)
- Content moderation: multimodal challenge, adversarial evasion
- Search ranking: query understanding → retrieval → ranking → re-ranking

## Vulnerability Moments:
1. Personal confession: avoided system design, focused on models
2. Admit: still developing intuition for when to use batch vs real-time
3. Confess oversimplification: the "five layers" is a simplification
4. Acknowledge: nobody fully knows the right metric hierarchy until they test it
5. Share struggle: feedback loops are genuinely hard to detect

## Recurring Analogies:
1. Restaurant kitchen - chef (model) vs entire restaurant operation (system)
2. Funnel/sieve - retrieve→rank as progressive filtering
