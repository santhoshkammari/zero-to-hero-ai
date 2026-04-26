# Findings: Interpretability & Visualization (ch09/s08)

## Key Research Findings

### Grad-CAM (Selvaraju et al., ICCV 2017)
- Gradient-weighted Class Activation Mapping
- Forward pass → record feature maps from last conv layer
- Backward pass → gradient of target class score w.r.t. those feature maps
- Global average pool each gradient map → one importance weight per channel (alpha_k)
- Weighted sum of feature maps, ReLU, then upscale
- Works on ANY CNN architecture (unlike original CAM which required GAP→linear)
- Coarse heatmap (resolution of conv layer grid, typically 7x7 for ResNet)
- Grad-CAM++ uses second-order gradients for multi-instance localization

### Saliency Maps
- Vanilla gradient: gradient of class score w.r.t. input pixels
- Very noisy, highlights individual pixels not regions
- SmoothGrad: add noise N times, average saliency maps → smoother
- Integrated Gradients (Sundararajan et al., 2017): interpolate from baseline to input, average gradients along path
  - Satisfies axioms: sensitivity (if feature matters, gets nonzero attribution) and implementation invariance
  - Baseline choice matters (usually black image, but dataset mean for medical)

### SHAP for Images (DeepSHAP)
- Uses Shapley values from game theory
- For images: segment into superpixels (SLIC), each superpixel = "player"
- Perturb superpixels on/off, measure prediction changes
- DeepSHAP approximates Shapley values efficiently using DeepLIFT rules
- Theoretically grounded but slow for high-res images

### LIME for Images
- Local Interpretable Model-agnostic Explanations
- Segment image into superpixels
- Randomly turn superpixels on/off, run through model
- Fit weighted linear regression locally → coefficients = importance
- Model-agnostic (works on any classifier)
- Unstable: different runs can give different explanations

### Feature Visualization / Activation Maximization
- Olah et al., Distill 2017
- Gradient ascent on input to maximize neuron activation
- Shows what neurons "want to see"
- Early layers: edges, colors; Middle: textures, parts; Deep: objects, concepts
- DeepDream is a variant (applied to whole image)
- Regularization needed (jitter, transforms, frequency penalties) for natural-looking results

### Concept Activation Vectors (TCAV)
- Kim et al., 2018
- Define human-understandable concepts (e.g., "striped", "furry")
- Train linear classifier in activation space to find concept direction
- TCAV score: what fraction of examples have increased prediction when you add more of concept
- Bridges gap between human concepts and model internals

### Mechanistic Interpretability (2024-2025)
- Superposition: single neurons encode multiple features (entangled)
- Sparse autoencoders: train to disentangle features into overcomplete sparse space
- Anthropic's work: scaling to large models, finding interpretable features
- Circuit discovery: mapping how groups of neurons perform specific computations

### Sanity Checks (Adebayo et al., NeurIPS 2018)
- CRITICAL: Many saliency methods fail sanity checks
- Parameter randomization test: randomize weights, check if explanation changes
- Some methods (guided backprop) produce same heatmap regardless of weights!
- Grad-CAM partially fails these tests
- Implication: don't trust a single method, use multiple

### Interpretability vs Explainability Taxonomy
- Intrinsic vs post-hoc
- Local vs global explanations
- Model-specific vs model-agnostic

### Clever Hans / Shortcut Learning
- Husky vs wolf: model learned "snow in background" = wolf
- Medical imaging: models learning hospital watermarks, scanner artifacts
- Tank legend (possibly apocryphal): model learned weather/time-of-day

### Interview-Depth Topics
- Why last conv layer for Grad-CAM? (balance of spatial + semantic info)
- Attention ≠ Attribution (attention shows where model looks, not what causes prediction)
- Insertion/deletion metrics for quantitative evaluation
- How to debug with interpretability: misclassification → Grad-CAM → check if focusing on right region
- Libraries: captum (Meta/PyTorch), pytorch-grad-cam, tf-explain
