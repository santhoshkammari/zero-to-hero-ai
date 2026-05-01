# Rewrite Plan: Data Visualization (ch01/s09)

## Brandon Rohrer Style Requirements
1. Personal confession opening
2. Build from absolute zero — why do we even visualize?
3. Running example: building a model to predict house prices, tracking its behavior
4. Toy examples for each concept
5. Show limitations to motivate next section
6. Vulnerability moments (4-5)
7. Recurring analogies
8. Rest stop
9. No listicles for explanations — narrative prose
10. Resources with personality

## Section Architecture

### Opening
- Confession: avoided learning viz properly, just copied code
- Orientation: what data viz actually is
- Heads-up: we'll cover matplotlib internals, not just API calls
- Journey invitation

### TOC
- Why we visualize (it's not about pretty pictures)
- The anatomy of a plot (Figure, Axes, Artists)
- Your first plot from scratch
- Choosing the right chart (the real skill)
- Seaborn — statistical visualization without the suffering
- Rest Stop
- The color problem nobody talks about
- Interactive visualization — Plotly and when you need it
- Production patterns — viz that doesn't break at 3am
- Visualization as communication
- Wrap-up
- Resources

### Key Concepts to Cover (depth order)
1. WHY visualize — two audiences: yourself and others
2. Matplotlib architecture (Figure/Canvas/Axes/Artist) — from scratch
3. OO interface vs pyplot state machine — why it matters
4. Chart selection framework — motivated by actual questions
5. Seaborn as statistical layer on top of matplotlib
6. Color theory — perceptual uniformity, colorblind accessibility
7. Plotly for interactive/stakeholder-facing
8. Production: memory leaks, saving, experiment tracking (wandb/mlflow)
9. Misleading visualizations — truncated axes, cherry-picked scales
10. Tufte principles — data-ink ratio

### Running Example
Building a house price prediction model — visualizing the data, the model's behavior, and communicating results to stakeholders.

### Vulnerability Moments
1. "I spent years plt.plot()-ing everything and wondering why my figures broke in loops"
2. "I still have to look up which seaborn function to use for violin plots"
3. "The first time I saw a perceptually uniform colormap explanation, I realized every heatmap I'd ever made was subtly lying"
4. "I'm still developing my intuition for when a visualization is 'done'"

### Analogies
1. Matplotlib as assembly language / construction tools — you CAN build anything, but it's manual
2. Figure as a blank canvas on an easel — Axes are the picture frames you nail to it
3. Colormaps as rulers with uneven markings — jet distorts your measurements
