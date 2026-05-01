# Matplotlib Internals

## Architecture: Figure → Canvas → Renderer → Artist
- Everything visible is an **Artist** (base class)
- **Figure**: top-level container
- **Axes**: region where data is plotted (the actual plot)
- **Canvas**: the drawing surface (backend-specific: Agg, Qt, SVG, PDF)
- **Renderer**: low-level drawing engine that knows how to draw primitives

## Rendering Pipeline
1. User creates Figure + Axes
2. Artists (Line2D, Text, Patch) are added to Axes
3. On draw event: Figure.draw(renderer) → Axes.draw() → each Artist.draw(renderer)
4. Renderer issues low-level drawing commands to backend

## OO vs pyplot (state machine)
- pyplot maintains hidden "current figure" and "current axes" state
- OO interface: `fig, ax = plt.subplots()` gives explicit objects
- OO is essential for: subplots, loops, functions, production code
- pyplot breaks silently when you have multiple figures

## Memory Management
- Each unclosed figure leaks memory
- `plt.close(fig)` is mandatory in loops/scripts
- `plt.clf()` and `plt.cla()` do NOT free memory
- Use `matplotlib.use('Agg')` for headless/production
- try/finally pattern for exception safety

## Key Insight
Matplotlib is like assembly language for viz — verbose but everything else compiles down to it.
