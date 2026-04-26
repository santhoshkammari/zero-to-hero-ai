# Mutual Information & Information Bottleneck — Key Findings

## Mutual Information
- I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
- Symmetric: X tells you as much about Y as Y tells about X
- Independent → I = 0. X determines Y → I = H(Y).
- Captures nonlinear dependencies (unlike Pearson correlation)
- Y = X² with symmetric X: zero correlation, high mutual information

## Feature Selection via MI
- sklearn: mutual_info_classif, mutual_info_regression
- Estimation is hard in high dimensions — k-NN based estimators (Kraskov)
- InfoNCE: lower bound on MI, scalable with neural nets (van den Oord 2018)

## Contrastive Learning Connection
- InfoNCE loss (SimCLR, CPC, CLIP) = lower bound on MI between views
- CLIP aligns image + text embeddings by maximizing MI between modalities

## Information Bottleneck (Tishby)
- Minimize I(X;T) - β·I(T;Y) — compress input, preserve label info
- Tishby 2017: two training phases — fitting (increase I(T;Y)), then compression (decrease I(T;X))
- Visualized via "information plane" plots
- Controversial: some argue compression phase depends on activation function (tanh yes, ReLU debated)

## Data Processing Inequality
- X → Y → Z: I(X;Z) ≤ I(X;Y)
- Processing can ONLY destroy information, never create it
- Each neural network layer = strategic bottleneck
- Motivates skip connections (ResNets) — preserve information across layers
- Motivates good feature engineering — you set the ceiling for all downstream models
