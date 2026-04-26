# BERT Variants

## RoBERTa
- Same architecture, better training: 10x data, no NSP, dynamic masking, bigger batches
- Showed BERT was undertrained

## ALBERT
- Cross-layer parameter sharing (80% fewer params)
- Factorized embedding parameterization
- Sentence Order Prediction (SOP) replaces NSP

## DeBERTa
- Disentangled attention: content and position attend SEPARATELY
- A_ij = Q^c_i·K^c_j + Q^p_{i-j}·K^p_{i-j}
- Enhanced mask decoder for MLM
- Combines relative + absolute position encoding
- Surpassed human baseline on SuperGLUE
