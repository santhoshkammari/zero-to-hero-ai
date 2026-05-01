# Part 4: NLP & Transformers

---

## 10. Sequence Models & Attention

### 10.1 RNN Fundamentals

1. [Basic] What is a Recurrent Neural Network (RNN) and how does it differ from a feedforward neural network?
2. [Basic] Draw and explain the unrolled computational graph of a simple RNN processing a sequence of length T.
3. [Basic] Write out the mathematical equations that govern the hidden state update in a vanilla RNN: h_t = f(W_hh · h_{t-1} + W_xh · x_t + b).
4. [Basic] What is the role of the hidden state h_t in an RNN? Why is it sometimes called "memory"?
5. [Basic] What types of tasks are RNNs typically used for? Give examples of one-to-many, many-to-one, and many-to-many architectures.
6. [Intermediate] Explain Backpropagation Through Time (BPTT). How does it differ from standard backpropagation?
7. [Intermediate] What is Truncated BPTT? Why is it used in practice and what are the trade-offs?
8. [Intermediate] Derive the gradient of the loss with respect to the recurrent weight matrix W_hh in a vanilla RNN. Show where the product of Jacobians appears.
9. [Intermediate] Explain the vanishing gradient problem in RNNs. What happens to the gradient signal as it flows backward through many time steps?
10. [Intermediate] Explain the exploding gradient problem. How does gradient clipping help mitigate it?
11. [Intermediate] Mathematically, why does the vanishing gradient problem arise when the spectral radius of the recurrent weight matrix is less than 1?
12. [Intermediate] What is the difference between gradient clipping by value and gradient clipping by norm?
13. [Advanced] How does the choice of activation function (tanh vs. ReLU) affect the vanishing/exploding gradient problem in RNNs?
14. [Advanced] Describe the Jacobian matrix ∂h_t/∂h_{t-k} and explain how its eigenvalues determine whether gradients vanish or explode.
15. [Basic] What is a bidirectional RNN? When is it useful and when is it not applicable?
16. [Intermediate] Explain how stacking multiple RNN layers (deep RNNs) works. What are the benefits and challenges?
17. [Basic] What is teacher forcing in RNN training? What are its advantages and disadvantages?
18. [Intermediate] Explain the exposure bias problem that arises from teacher forcing. How can scheduled sampling help?
19. [Advanced] Compare RNNs with 1D Convolutional Neural Networks for sequence modeling. What are the relative advantages of each?
20. [Intermediate] How do you handle variable-length sequences in RNNs? Explain the role of padding and masking.
21. [Basic] What is the computational complexity of processing a sequence of length T through an RNN? Why can't RNNs be easily parallelized?
22. [Intermediate] How do you initialize the hidden state of an RNN? What is the impact of different initialization strategies?
23. [Advanced] Explain Echo State Networks (ESNs) and the concept of reservoir computing. How do they differ from trainable RNNs?
24. [Expert] Derive the conditions under which a vanilla RNN can preserve long-term dependencies based on the weight matrix eigenvalue spectrum.
25. [Intermediate] What is the Elman network vs. the Jordan network? How do their architectures differ?

### 10.2 LSTMs & GRUs

26. [Basic] What is an LSTM and what problem does it solve compared to vanilla RNNs?
27. [Basic] Draw and label the architecture of an LSTM cell, showing the forget gate, input gate, output gate, and cell state.
28. [Intermediate] Write out the full set of LSTM equations: forget gate (f_t), input gate (i_t), cell candidate (c̃_t), cell state update (c_t), output gate (o_t), and hidden state (h_t).
29. [Basic] Explain the role of the forget gate in an LSTM. How does it decide what information to discard from the cell state?
30. [Basic] Explain the role of the input gate. How does it decide what new information to store in the cell state?
31. [Basic] Explain the role of the output gate. How does it determine what part of the cell state becomes the hidden state?
32. [Intermediate] Why does the cell state in LSTM help alleviate the vanishing gradient problem? Explain the concept of the "gradient highway."
33. [Intermediate] What is the role of the tanh and sigmoid activation functions in the LSTM gates? Why are they chosen?
34. [Advanced] Derive the gradient flow through the cell state in an LSTM. Show how the forget gate multiplicative factor allows gradients to flow unchanged over many time steps.
35. [Intermediate] How does the peephole connection variant of LSTM work? When would you use it?
36. [Basic] What is a GRU (Gated Recurrent Unit)? How does it differ from an LSTM?
37. [Intermediate] Write out the GRU equations: update gate (z_t), reset gate (r_t), candidate hidden state (h̃_t), and final hidden state (h_t).
38. [Intermediate] Compare and contrast the gates in LSTM (forget, input, output) with those in GRU (update, reset). What is combined/eliminated?
39. [Intermediate] When would you choose LSTM over GRU and vice versa? What are the computational trade-offs?
40. [Advanced] GRU has fewer parameters than LSTM. Under what conditions does LSTM outperform GRU despite this extra complexity?
41. [Intermediate] How many parameters does an LSTM layer have given input dimension d_x and hidden dimension d_h? Derive the formula.
42. [Intermediate] How many parameters does a GRU layer have given the same input and hidden dimensions? Compare with LSTM.
43. [Advanced] Explain the coupled forget-input gate variant of LSTM where i_t = 1 - f_t. What are its implications?
44. [Expert] Describe the LSTM ablation study by Greff et al. (2017). Which gates were found to be most critical?
45. [Advanced] What is the Minimal Gated Unit? How does it further simplify the GRU architecture?
46. [Intermediate] Explain how you would implement dropout in an LSTM. What is the difference between naive dropout and variational dropout (Gal & Ghahramani)?
47. [Intermediate] What is zoneout regularization for LSTMs? How does it differ from dropout?
48. [Advanced] Describe the Highway LSTM architecture. How do highway connections further improve gradient flow?
49. [Intermediate] How do you handle multi-layer (stacked) LSTMs? What is the effect of depth on sequence modeling?
50. [Advanced] Compare the memory capacity of LSTM vs. vanilla RNN. How does the cell state mechanism effectively increase the network's ability to store information?

### 10.3 Sequence-to-Sequence & Encoder-Decoder

51. [Basic] What is the sequence-to-sequence (seq2seq) architecture? Draw a diagram of the encoder-decoder framework.
52. [Basic] What is the role of the encoder in a seq2seq model? What is the role of the decoder?
53. [Intermediate] What is the "context vector" or "thought vector" in a basic seq2seq model? What are its limitations?
54. [Intermediate] Why is compressing an entire input sequence into a single fixed-length context vector problematic for long sequences?
55. [Basic] Explain how seq2seq models are used for machine translation. Walk through the encoding and decoding steps.
56. [Intermediate] What is greedy decoding? Why can it produce suboptimal outputs?
57. [Intermediate] Explain beam search decoding. How does beam width affect the quality and diversity of outputs?
58. [Advanced] What is the time and space complexity of beam search with beam width B and maximum sequence length T?
59. [Intermediate] What is the difference between autoregressive decoding and non-autoregressive decoding?
60. [Advanced] Explain the length bias problem in beam search. How do length normalization techniques address it?
61. [Intermediate] How do you train a seq2seq model? Explain the cross-entropy loss applied at each decoder time step.
62. [Intermediate] What are start-of-sequence (SOS) and end-of-sequence (EOS) tokens? How are they used during training and inference?
63. [Intermediate] Explain the difference between training mode (with teacher forcing) and inference mode in seq2seq models.
64. [Advanced] What is Minimum Risk Training for seq2seq models? How does it differ from maximum likelihood training?
65. [Advanced] Describe how you would use reinforcement learning (e.g., REINFORCE algorithm) to train a seq2seq model to optimize BLEU score directly.
66. [Intermediate] What is copy mechanism or pointer network? When is it useful in seq2seq tasks?
67. [Advanced] Explain the pointer-generator network (See et al., 2017). How does it combine copying and generation?
68. [Expert] Compare the encoder-decoder architecture using RNNs vs. Transformers for machine translation. What are the key advantages of the Transformer approach?

### 10.4 Attention Mechanisms

69. [Basic] What is the attention mechanism in neural networks? Why was it introduced for seq2seq models?
70. [Basic] Explain the intuition behind attention: why should the decoder "look at" different parts of the input at different decoding steps?
71. [Intermediate] Describe Bahdanau attention (additive attention). Write out the mathematical formulation including the alignment model.
72. [Intermediate] Describe Luong attention (multiplicative attention). What are the three scoring functions Luong proposed (dot, general, concat)?
73. [Intermediate] Compare Bahdanau (additive) vs. Luong (multiplicative) attention in terms of computation, parameters, and typical performance.
74. [Intermediate] What is the alignment score in attention? How is it computed and converted to attention weights using softmax?
75. [Intermediate] What is the context vector in attention-based seq2seq? How is it computed as a weighted sum of encoder hidden states?
76. [Advanced] Derive the gradient of the loss with respect to the attention weights. How does the attention mechanism affect gradient flow?
77. [Intermediate] What is local attention vs. global attention as described by Luong? When would you use each?
78. [Intermediate] What is monotonic attention? In what applications is it particularly useful?
79. [Basic] What is self-attention (intra-attention)? How does it differ from cross-attention in seq2seq models?
80. [Intermediate] Explain the Query, Key, Value (Q, K, V) framework in self-attention. What do each of Q, K, and V represent?
81. [Intermediate] Write out the scaled dot-product attention formula: Attention(Q, K, V) = softmax(QK^T / √d_k)V. Explain each component.
82. [Intermediate] Why do we scale by 1/√d_k in scaled dot-product attention? What happens if we don't scale?
83. [Advanced] Prove that without scaling, the dot products grow as O(d_k) in expectation, causing softmax to saturate.
84. [Intermediate] What is multi-head attention? Why use multiple attention heads instead of a single attention head?
85. [Intermediate] Write out the multi-head attention formula: MultiHead(Q, K, V) = Concat(head_1, ..., head_h)W^O. How are the heads computed?
86. [Intermediate] If the model dimension is d_model and we have h heads, what is the dimension of each head? Why is this efficient?
87. [Advanced] What is the computational complexity of self-attention with respect to sequence length n and model dimension d? Compare with RNN complexity.
88. [Advanced] Why is self-attention O(n²·d) in time complexity? When does this become a bottleneck?
89. [Intermediate] What is cross-attention in the Transformer decoder? How does it differ from self-attention?
90. [Advanced] Explain the concept of attention heads learning different "types" of relationships. Give examples (syntactic, positional, semantic heads).
91. [Expert] Describe the attention visualization analysis by Clark et al. (2019). What patterns did they find in BERT's attention heads?
92. [Advanced] What is attention rollout? How does it aggregate attention across layers to estimate token-level importance?
93. [Expert] Derive the backward pass for multi-head attention. What are the gradients with respect to W^Q, W^K, W^V, and W^O?
94. [Advanced] How can attention weights be interpreted? What are the limitations of using attention weights as explanations?
95. [Expert] Explain the relationship between attention and kernel methods. How does linearized attention connect to kernel feature maps?
96. [Advanced] What is the difference between hard attention and soft attention? How do you train hard attention (REINFORCE vs. straight-through estimator)?
97. [Intermediate] How does relative position attention (Shaw et al., 2018) modify the attention computation to incorporate positional information?
98. [Expert] Explain the connection between self-attention and Hopfield networks as described by Ramsauer et al. (2020).

### 10.5 Positional Encoding

99. [Basic] Why do Transformers need positional encoding? What happens if you remove it entirely?
100. [Intermediate] Explain sinusoidal positional encoding as described in "Attention Is All You Need." Write out the formulas for PE(pos, 2i) and PE(pos, 2i+1).
101. [Intermediate] Why were sine and cosine functions chosen for positional encoding? What property allows the model to learn relative positions?
102. [Intermediate] Show that sinusoidal positional encodings allow representing PE(pos+k) as a linear function of PE(pos). Why is this useful?
103. [Intermediate] What are learned positional embeddings? How do they differ from sinusoidal encodings?
104. [Intermediate] What are the advantages and disadvantages of learned positional embeddings compared to sinusoidal?
105. [Advanced] Explain Rotary Positional Encoding (RoPE). How does it encode position as rotations in the complex plane?
106. [Advanced] Write out the mathematical formulation of RoPE. How are queries and keys modified before computing attention scores?
107. [Advanced] What property makes RoPE encode relative positions? Prove that the inner product of RoPE-encoded queries and keys depends only on relative position.
108. [Advanced] Explain ALiBi (Attention with Linear Biases). How does it add a position-dependent bias to attention logits?
109. [Advanced] How does ALiBi achieve length extrapolation (generalizing to longer sequences than seen during training)?
110. [Advanced] Compare RoPE vs. ALiBi vs. sinusoidal vs. learned positional encodings in terms of: (a) extrapolation ability, (b) computational cost, (c) implementation complexity.
111. [Expert] What is NTK-aware scaling for RoPE? How does it help extend the context length of pretrained models?
112. [Expert] Explain YaRN (Yet another RoPE extensioN). How does it combine different scaling strategies?
113. [Advanced] What is relative positional encoding (RPE) as used in Transformer-XL? How does it modify the attention computation?
114. [Expert] Compare absolute positional encoding vs. relative positional encoding. When is each approach more appropriate?
115. [Advanced] How do Vision Transformers handle positional encoding for 2D image patches? What is the difference between 1D and 2D positional encodings?
116. [Expert] Explain the Randomized Positional Encoding scheme. How can it improve length generalization?
117. [Advanced] What happens when you try to use a model at a sequence length much longer than it was trained on? How do different positional encoding schemes handle this?
118. [Expert] Describe CoPE (Contextual Positional Encoding). How does it make positional encoding context-dependent?
119. [Intermediate] How is positional encoding added to the input? Is it added or concatenated? What are the implications of each choice?
120. [Expert] Explain the Fire (Functional Interpolation for Relative position Encoding) approach. How does it generalize existing relative position methods?

### 10.6 Advanced Sequence Modeling Topics

121. [Intermediate] Explain the Elman RNN vs. Jordan RNN architectures. How do their feedback connections differ?
122. [Advanced] What is the Clockwork RNN? How does it handle multiple timescales?
123. [Advanced] Describe Temporal Convolutional Networks (TCNs). How do they compare to RNNs for sequence modeling?
124. [Advanced] What are dilated causal convolutions? How do they enable large receptive fields without increasing parameter count?
125. [Intermediate] Compare the parallelizability of RNNs vs. CNNs vs. Transformers for sequence processing.
126. [Advanced] Explain the concept of memory networks. How do they augment neural networks with external memory?
127. [Expert] Describe the Neural Turing Machine (NTM) and Differentiable Neural Computer (DNC). How do they use attention to read/write from memory?
128. [Advanced] What is the Transformer-XL architecture? How does segment-level recurrence address the context fragmentation problem?
129. [Expert] Explain the recurrence mechanism in Transformer-XL. How is the hidden state from the previous segment reused?
130. [Intermediate] What are Independently Recurrent Neural Networks (IndRNNs)? How do they address gradient issues?
131. [Advanced] Explain the Structured State Space (S4) model. How does it connect linear state-space models with deep learning?
132. [Expert] Derive the convolutional representation of a linear state-space model. How does this enable efficient parallel training?
133. [Advanced] What is the HiPPO framework? How does it provide a theoretical foundation for state-space models?
134. [Expert] Compare the training and inference efficiency of S4 vs. Transformer for long-range sequence modeling.
135. [Intermediate] What is attention masking? Explain causal masking and how it prevents information leakage during autoregressive generation.
136. [Intermediate] What is the difference between causal (autoregressive) attention and bidirectional attention?
137. [Advanced] How do you combine local and global attention patterns? Explain the approach used in Longformer.
138. [Expert] What is Linear Attention? Derive how replacing softmax with kernel functions reduces complexity from O(n²) to O(n).
139. [Intermediate] What is the KV cache in autoregressive decoding? Why is it essential for efficient Transformer inference?
140. [Advanced] Explain grouped-query attention (GQA). How does it reduce KV cache memory compared to multi-head attention?
141. [Advanced] What is multi-query attention (MQA)? How does it differ from GQA and standard multi-head attention?
142. [Expert] Compare MHA, MQA, and GQA in terms of: quality, training speed, inference latency, and KV cache memory.
143. [Advanced] Explain sliding window attention as used in Mistral. How does it balance local context with computational efficiency?
144. [Intermediate] How do different attention patterns (full, local, strided, random) affect model quality and efficiency?
145. [Expert] Describe the Ring Attention mechanism. How does it enable training on very long sequences across multiple devices?
146. [Advanced] What is prefix caching in LLM inference? How does it improve throughput for common prompt prefixes?
147. [Expert] Explain speculative decoding. How does it use a small model to speed up inference from a large model?
148. [Advanced] What is the relationship between the softmax bottleneck and the expressiveness of attention?
149. [Expert] Explain Hyena: how does it replace attention with long convolutions and gating? What are the efficiency gains?
150. [Expert] Compare RWKV architecture with Transformers. How does RWKV achieve linear complexity while maintaining competitive performance?
151. [Advanced] What is the difference between additive attention and multiplicative attention? In which scenarios does each perform better?
152. [Expert] Explain the attention sink phenomenon. Why do autoregressive LLMs allocate disproportionate attention to the first token?

---

## 11. Transformers Architecture

### 11.1 Original Transformer Architecture

1. [Basic] Describe the original Transformer architecture from "Attention Is All You Need" (Vaswani et al., 2017). What are its main components?
2. [Basic] Draw the high-level architecture of the Transformer showing the encoder stack and decoder stack.
3. [Basic] How many encoder and decoder layers did the original Transformer have? What were the key hyperparameters (d_model, d_ff, h, etc.)?
4. [Intermediate] Explain the complete data flow through a single Transformer encoder layer: self-attention → add & norm → feed-forward → add & norm.
5. [Intermediate] Explain the complete data flow through a single Transformer decoder layer. Why does it have three sub-layers instead of two?
6. [Intermediate] What is the feed-forward network (FFN) in the Transformer? What are its dimensions and activation function?
7. [Basic] What are residual connections in the Transformer? Why are they important?
8. [Intermediate] Explain layer normalization in the Transformer. How does it differ from batch normalization?
9. [Advanced] Compare Pre-LayerNorm vs. Post-LayerNorm Transformer architectures. Which is more commonly used in modern models and why?
10. [Intermediate] Explain the Query, Key, Value computation in the Transformer. How are Q, K, V matrices obtained from the input?
11. [Advanced] If d_model = 512 and h = 8 heads, what is d_k = d_v = d_model/h? Calculate the total number of parameters in the multi-head attention layer.
12. [Intermediate] How does the decoder prevent attending to future tokens during training? Explain causal masking in detail.
13. [Intermediate] What is the role of the encoder-decoder attention (cross-attention) layer in the decoder? Where do Q, K, V come from?
14. [Intermediate] How is the final output of the Transformer decoder converted to token probabilities? Explain the linear + softmax layer.
15. [Advanced] What is weight tying between the embedding layer and the output projection layer? Why is it used?
16. [Intermediate] How is the Transformer trained? Explain the label smoothing technique used in the original paper.
17. [Intermediate] What learning rate schedule did the original Transformer use? Explain the warmup + inverse square root decay.
18. [Advanced] What is the total number of parameters in the original Transformer (base model)? Break it down by component.
19. [Advanced] What regularization techniques are used in the Transformer? (Dropout, label smoothing, etc.)
20. [Expert] Explain the relationship between the Transformer FFN and a key-value memory. How can the FFN be interpreted as storing factual knowledge?
21. [Advanced] What is the role of dropout in the Transformer? Where is it applied (attention weights, residual connections, embeddings)?
22. [Intermediate] How does the Transformer handle varying input lengths during training? Explain padding masks.
23. [Advanced] Explain embedding scaling in the Transformer. Why are embeddings multiplied by √d_model?
24. [Expert] Analyze the information-theoretic capacity of the Transformer. How many bits of information can attention layers theoretically store?

### 11.2 BERT & Variants

25. [Basic] What is BERT? What does the acronym stand for and what makes it "bidirectional"?
26. [Basic] Explain the two pre-training objectives of BERT: Masked Language Modeling (MLM) and Next Sentence Prediction (NSP).
27. [Intermediate] In MLM, what percentage of tokens are masked? Of those, what fraction are replaced with [MASK], random tokens, or left unchanged? Why this strategy?
28. [Intermediate] How does BERT's input representation work? Explain token embeddings, segment embeddings, and position embeddings.
29. [Intermediate] What are the special tokens [CLS] and [SEP] in BERT? What are their roles?
30. [Intermediate] How is BERT fine-tuned for text classification? Explain the process of adding a classification head on top of the [CLS] token.
31. [Intermediate] How is BERT fine-tuned for question answering (extractive QA)? Explain the start and end position prediction.
32. [Intermediate] How is BERT fine-tuned for named entity recognition? Explain the token-level classification approach.
33. [Intermediate] What is the maximum sequence length for BERT? How do you handle documents longer than 512 tokens?
34. [Advanced] Why was the Next Sentence Prediction (NSP) objective later found to be less useful? What evidence supports this claim?
35. [Intermediate] What are the differences between BERT-base and BERT-large in terms of layers, hidden size, attention heads, and parameters?
36. [Advanced] Explain RoBERTa. What changes did it make to BERT's pre-training (removal of NSP, dynamic masking, more data, larger batches)?
37. [Advanced] Explain ALBERT. How do cross-layer parameter sharing and factorized embedding parameterization reduce parameters?
38. [Intermediate] Explain DistilBERT. How does knowledge distillation create a smaller model that retains most of BERT's performance?
39. [Advanced] Explain ELECTRA. How does the replaced token detection objective differ from MLM? Why is it more sample-efficient?
40. [Advanced] What is the discriminator-generator setup in ELECTRA? How is it different from GANs?
41. [Advanced] Explain DeBERTa. What is disentangled attention and how does it separately handle content and position?
42. [Expert] Compare BERT, RoBERTa, ALBERT, ELECTRA, and DeBERTa on the GLUE benchmark. Which modifications had the largest impact?
43. [Intermediate] What is Sentence-BERT (SBERT)? How does it produce fixed-size sentence embeddings suitable for similarity tasks?
44. [Advanced] How does BERT handle WordPiece tokenization? What happens when a word is split into subword tokens during fine-tuning for NER?
45. [Intermediate] What is the difference between feature extraction (freezing BERT) and fine-tuning (updating BERT weights)? When would you use each?
46. [Advanced] Explain the probing methodology for analyzing what BERT has learned. What linguistic knowledge is captured in different layers?
47. [Expert] Describe the BERTology literature. What have researchers discovered about BERT's internal representations?
48. [Intermediate] How would you adapt BERT for a multilingual setting? Explain mBERT and XLM-RoBERTa.
49. [Advanced] Explain the [MASK] token mismatch problem in BERT (the pretrain-finetune discrepancy). How do different BERT variants address this?
50. [Expert] What are adapter layers for BERT? How do they enable parameter-efficient fine-tuning?

### 11.3 GPT Family & Autoregressive Models

51. [Basic] What is GPT? How does it differ from BERT architecturally?
52. [Basic] Explain the autoregressive nature of GPT. How does it generate text token by token?
53. [Intermediate] What is causal masking in GPT? How does the attention mask ensure that each token can only attend to previous tokens?
54. [Intermediate] How was GPT-1 pre-trained and fine-tuned? What was its training objective?
55. [Intermediate] What was the key insight of GPT-2 that demonstrated language models can perform tasks zero-shot?
56. [Intermediate] Explain the scale of GPT-3 (175B parameters). How did it demonstrate emergent few-shot learning capabilities?
57. [Advanced] What are scaling laws for language models (Kaplan et al., 2020)? What is the relationship between model size, data size, compute, and performance?
58. [Advanced] Explain the Chinchilla scaling laws (Hoffmann et al., 2022). How do they differ from the original scaling laws?
59. [Advanced] According to Chinchilla, given a fixed compute budget, what is the optimal ratio of model parameters to training tokens?
60. [Expert] Derive the power law relationship L(N) ∝ N^(-α) between loss and model size. What are typical values of α?
61. [Advanced] Why did pre-Chinchilla models like GPT-3 under-train relative to their parameter count? What are the practical implications?
62. [Intermediate] Explain the concept of in-context learning (ICL). How does GPT-3 perform tasks without gradient updates?
63. [Advanced] Compare zero-shot, one-shot, and few-shot prompting in GPT-3. How does performance scale with the number of examples?
64. [Expert] What is the theoretical explanation for in-context learning? Discuss the "implicit gradient descent" hypothesis.
65. [Advanced] Explain InstructGPT. How does RLHF (Reinforcement Learning from Human Feedback) align the model with human preferences?
66. [Advanced] Describe the three-step process of RLHF: (1) SFT, (2) reward model training, (3) PPO optimization.
67. [Expert] What is the reward hacking problem in RLHF? How can the model exploit the reward model?
68. [Advanced] Explain DPO (Direct Preference Optimization). How does it simplify RLHF by eliminating the explicit reward model?
69. [Advanced] Compare GPT-3.5, GPT-4, and GPT-4o in terms of architecture innovations and capabilities.
70. [Expert] What is the Mixture of Experts speculation for GPT-4? How would MoE allow scaling while controlling inference costs?
71. [Intermediate] What is temperature sampling in GPT? How does temperature affect the probability distribution over tokens?
72. [Intermediate] Explain top-k sampling and top-p (nucleus) sampling. How do they prevent degenerate text generation?
73. [Advanced] What is the repetition penalty in text generation? How do frequency and presence penalties work?
74. [Advanced] Explain the concept of perplexity. How is it used to evaluate language models?
75. [Intermediate] What is the context window of GPT models? How has it evolved from GPT-2 (1K) to GPT-4 (128K)?
76. [Expert] How do models like GPT-4 handle extremely long contexts (128K tokens)? What architectural modifications are needed?
77. [Advanced] Compare autoregressive (GPT) vs. masked (BERT) pre-training. For which downstream tasks is each approach better suited?
78. [Expert] Explain the Llama architecture innovations: RMSNorm, SwiGLU activation, RoPE, grouped-query attention. How does each improve upon the original Transformer?

### 11.4 T5, BART & Encoder-Decoder Models

79. [Intermediate] Explain the T5 (Text-to-Text Transfer Transformer) framework. How does it frame all NLP tasks as text-to-text problems?
80. [Intermediate] Give examples of how T5 converts different tasks (classification, summarization, translation) into a text-to-text format.
81. [Intermediate] What pre-training objective does T5 use? How does span corruption differ from BERT's MLM?
82. [Advanced] Describe the systematic study in the T5 paper. What did the authors find about pre-training objectives, architectures, and data?
83. [Intermediate] What is BART? How does its denoising autoencoder pre-training objective work?
84. [Intermediate] What noise transformations does BART use during pre-training (token masking, token deletion, sentence permutation, text infilling, document rotation)?
85. [Advanced] Compare T5 and BART in terms of pre-training objectives, architecture choices, and downstream task performance.
86. [Intermediate] Explain the encoder-decoder architecture used by T5 and BART. Why is this architecture well-suited for generation tasks?
87. [Advanced] What is Flan-T5? How does instruction tuning improve T5's zero-shot and few-shot performance?
88. [Advanced] Explain mT5 and mBART. How are these models adapted for multilingual settings?
89. [Advanced] Compare encoder-only (BERT), decoder-only (GPT), and encoder-decoder (T5) architectures. For which tasks is each most suitable?
90. [Expert] What is the UL2 (Unifying Language Learning Paradigms) objective? How does it combine different pre-training strategies?
91. [Intermediate] How does BART handle summarization? What makes it particularly effective for abstractive summarization?
92. [Advanced] Explain prefix language modeling as used in some encoder-decoder models. How does it combine bidirectional and autoregressive processing?

### 11.5 Efficient Transformers

93. [Intermediate] What is the memory and computational bottleneck in standard Transformer self-attention?
94. [Advanced] Explain Flash Attention (Dao et al., 2022). How does tiling and recomputation reduce memory from O(n²) to O(n)?
95. [Advanced] How does Flash Attention achieve exact attention computation (not approximate) while being faster?
96. [Expert] Describe the IO-awareness aspect of Flash Attention. How does it minimize HBM (High Bandwidth Memory) reads/writes?
97. [Advanced] What is Flash Attention 2? What improvements does it make over the original Flash Attention?
98. [Expert] Explain the tiling algorithm in Flash Attention. How does the online softmax trick enable block-wise computation?
99. [Advanced] What is Linformer? How does it approximate attention by projecting keys and values to lower dimensions?
100. [Advanced] Explain the Performer architecture. How does it use random feature maps to approximate softmax attention?
101. [Advanced] What is the Longformer? Describe its combination of local windowed attention and global attention.
102. [Advanced] Explain BigBird's attention pattern. How does it combine random, window, and global attention?
103. [Advanced] What is sparse attention (Child et al., 2019)? How do strided and fixed attention patterns work?
104. [Expert] Compare Flash Attention, Linformer, Performer, Longformer, and BigBird in terms of: complexity, exactness, quality, and practical speedup.
105. [Advanced] What is PagedAttention? How does it improve memory management for KV caches during LLM serving?
106. [Expert] Explain the vLLM system. How does PagedAttention enable efficient batched inference?
107. [Advanced] What is continuous batching for LLM inference? How does it differ from static batching?
108. [Advanced] Explain model parallelism strategies for Transformers: tensor parallelism, pipeline parallelism, and data parallelism.
109. [Expert] Describe the Megatron-LM approach to tensor parallelism. How does it split attention and FFN layers across GPUs?
110. [Advanced] What is activation checkpointing (gradient checkpointing)? How does it trade compute for memory?
111. [Advanced] Explain mixed-precision training (FP16/BF16). Why is BF16 preferred over FP16 for Transformer training?
112. [Expert] What is FP8 training? How do E4M3 and E5M2 formats differ and when is each used?
113. [Advanced] Explain quantization for Transformer inference. Compare INT8, INT4, and GPTQ approaches.
114. [Expert] What is AWQ (Activation-aware Weight Quantization)? How does it improve upon naive weight quantization?
115. [Advanced] Explain knowledge distillation for Transformers. How do you train a smaller model to mimic a larger one?
116. [Advanced] What is model pruning? Compare unstructured vs. structured pruning for Transformers.
117. [Expert] Explain SparseGPT. How does it prune GPT models to 50%+ sparsity without retraining?

### 11.6 Mixture of Experts & Modern Architectures

118. [Intermediate] What is a Mixture of Experts (MoE) architecture? Explain the gating mechanism that routes inputs to experts.
119. [Intermediate] How does MoE differ from a dense model with the same total parameter count?
120. [Advanced] Explain the top-k routing mechanism in MoE. Why is k typically set to 1 or 2?
121. [Advanced] What is the load balancing problem in MoE? Describe the auxiliary loss used to ensure even expert utilization.
122. [Advanced] What is expert collapse? How can you prevent all tokens from being routed to the same expert?
123. [Expert] Describe the Switch Transformer (Fedus et al., 2022). How does it scale to trillions of parameters using MoE?
124. [Expert] Explain the Mixtral 8x7B architecture. How does it use MoE layers and what is its effective parameter count during inference?
125. [Advanced] How are MoE models trained on distributed systems? Explain expert parallelism.
126. [Advanced] What are the inference challenges of MoE models? How does expert activation affect memory and latency?
127. [Expert] Compare dense scaling (increase all parameters) vs. sparse scaling (MoE) in terms of training efficiency and model quality.
128. [Advanced] Explain State Space Models (SSMs) for sequence modeling. How do they differ from Transformers?
129. [Advanced] What is Mamba? Describe the selective state space mechanism and how it provides input-dependent dynamics.
130. [Expert] How does Mamba achieve linear time complexity for sequence processing? Compare with Transformer's quadratic complexity.
131. [Expert] Explain the hardware-efficient implementation of Mamba using parallel scans on GPUs.
132. [Advanced] What is the S6 (Selective Structured State Space) layer in Mamba? How does selectivity improve over S4?
133. [Expert] Compare Mamba vs. Transformer on language modeling benchmarks. Where does each architecture excel?
134. [Advanced] What is RWKV? How does it combine the training efficiency of Transformers with the inference efficiency of RNNs?
135. [Expert] Describe the Jamba architecture. How does it combine Transformer layers, Mamba layers, and MoE?
136. [Advanced] What is the RetNet (Retentive Network) architecture? How does it enable recurrent, parallel, and chunkwise computation?
137. [Expert] Explain the Griffin architecture (De et al., 2024). How does it combine gated linear recurrences with local attention?
138. [Advanced] What is the Hyena hierarchy? How does it use long convolutions to replace attention?
139. [Expert] Compare the landscape of sub-quadratic architectures: linear attention, SSMs (Mamba), RWKV, RetNet, Hyena. What are their relative strengths?
140. [Advanced] What is the xLSTM architecture? How does it modernize LSTM with exponential gating and matrix memory?
141. [Expert] Explain the Test-Time Training (TTT) layers. How do they use self-supervised learning at inference time?

### 11.7 Transformer Training & Optimization

142. [Intermediate] What optimizer is most commonly used for training Transformers? Explain AdamW and its advantages.
143. [Intermediate] Explain the learning rate warmup strategy. Why is it important for Transformer training stability?
144. [Advanced] What is the cosine learning rate schedule? How does it compare to linear decay and inverse square root schedules?
145. [Advanced] Explain gradient accumulation. How does it enable training with larger effective batch sizes on limited GPU memory?
146. [Intermediate] What is the typical batch size for training large Transformers? How is it measured (tokens vs. sequences)?
147. [Advanced] What is the role of weight decay in Transformer training? How does it differ from L2 regularization with Adam?
148. [Advanced] Explain the μP (Maximal Update Parameterization) method. How does it enable hyperparameter transfer across model scales?
149. [Expert] Describe the training instabilities that can occur with very large Transformers. How are loss spikes handled in practice?
150. [Expert] Explain the concept of training compute optimal models. How do you balance model size, data, and compute?
151. [Advanced] What is curriculum learning for Transformers? How does data ordering affect training dynamics?
152. [Expert] Explain the Chinchilla-optimal data mixture. How do you balance different data sources (web, books, code) for pretraining?
153. [Advanced] What is the "grokking" phenomenon in Transformer training? How can models suddenly generalize long after memorizing the training data?

### 11.8 Parameter-Efficient Fine-Tuning

154. [Intermediate] What is parameter-efficient fine-tuning (PEFT)? Why is it important for large language models?
155. [Intermediate] Explain LoRA (Low-Rank Adaptation). How does it add trainable low-rank matrices to frozen model weights?
156. [Advanced] In LoRA, what are the rank r and scaling factor α? How do you choose these hyperparameters?
157. [Advanced] Explain QLoRA. How does it combine quantization with LoRA for memory-efficient fine-tuning?
158. [Intermediate] What are adapter layers? How do they add small trainable modules between frozen Transformer layers?
159. [Advanced] Explain prefix tuning. How does it prepend trainable continuous vectors to the key and value sequences?
160. [Intermediate] What is prompt tuning (Lester et al., 2021)? How does it differ from prompt engineering?
161. [Advanced] Compare LoRA, adapters, prefix tuning, and prompt tuning in terms of: parameter count, performance, and training cost.
162. [Expert] Explain DoRA (Weight-Decomposed Low-Rank Adaptation). How does it decompose weights into magnitude and direction?
163. [Expert] What is the theoretical justification for why LoRA works? How does the intrinsic dimensionality of the fine-tuning task relate to the rank?

### 11.9 Transformer Applications & Design

164. [Intermediate] How would you design a document classification system using a Transformer model?
165. [Advanced] Design a semantic search engine. Describe the indexing, retrieval, and ranking pipeline using Transformer embeddings.
166. [Advanced] How would you build a code completion system using a Transformer? What architectural choices would you make?
167. [Advanced] Design a multi-turn conversational AI system. How do you handle context, memory, and coherence?
168. [Expert] Design a real-time machine translation system. How do you balance latency, quality, and throughput?
169. [Intermediate] How do Vision Transformers (ViT) adapt the Transformer for image classification?
170. [Advanced] Explain CLIP (Contrastive Language-Image Pre-training). How does it connect vision and language?
171. [Advanced] How are Transformers used in speech recognition (Whisper, wav2vec 2.0)?
172. [Expert] Design a multimodal AI system that handles text, images, and audio. What architectural decisions would you make?
173. [Advanced] How would you build a retrieval-augmented generation (RAG) system? Describe the retriever and generator components.
174. [Expert] Design a production LLM serving system that handles thousands of concurrent requests. Address batching, caching, and load balancing.

### 11.10 Transformer Interpretability & Analysis

175. [Intermediate] What is probing in the context of Transformer analysis? How do you probe what information a model's representations contain?
176. [Advanced] Explain attention head pruning. How can you identify and remove redundant attention heads?
177. [Advanced] What is the "induction head" phenomenon? How do Transformers implement in-context learning through attention pattern composition?
178. [Expert] Describe mechanistic interpretability for Transformers. How do circuit-level analyses reveal how models compute?
179. [Expert] Explain the concept of superposition in neural networks. How do Transformers represent more features than they have dimensions?
180. [Advanced] What are logit lens and tuned lens approaches to Transformer interpretability?
181. [Expert] Explain the role of the residual stream in Transformers. How does the residual stream hypothesis guide interpretability research?
182. [Advanced] How do you analyze the knowledge stored in Transformer feed-forward layers?
183. [Expert] What is ROME (Rank-One Model Editing)? How can you edit specific facts stored in a Transformer?
184. [Advanced] What is the lottery ticket hypothesis? Does it apply to Transformers?
185. [Expert] Describe the scaling monosemanticity results from Anthropic. What did they find about feature interpretability in large models?
186. [Advanced] How do you detect and analyze hallucinations in Transformer-based language models?
187. [Expert] Explain the concept of emergent abilities in large language models. What capabilities appear at certain scales?
188. [Expert] What is the "phase transition" hypothesis for emergent abilities? Is there evidence that emergence is smooth vs. sudden?
189. [Intermediate] How do you evaluate whether a language model truly "understands" language vs. pattern matching? Discuss relevant benchmarks.
190. [Advanced] What is the difference between syntactic and semantic knowledge in Transformer representations?
191. [Expert] Explain the work on "Transformer circuits" (Elhage et al.). What are QK and OV circuits?
192. [Advanced] How can you visualize what different layers and heads in a Transformer have learned?
193. [Expert] Describe the phenomenon of "grokking" in Transformers. What does it tell us about generalization?
194. [Advanced] How does chain-of-thought prompting improve Transformer reasoning? What are its limitations?
195. [Expert] What is the relationship between Transformer depth and the computational problems they can solve? (Connection to circuit complexity)
196. [Advanced] Explain the reversal curse in LLMs. Why do models trained on "A is B" fail to infer "B is A"?
197. [Expert] What are the theoretical limitations of Transformers? Can they solve all problems in TC⁰ (constant-depth threshold circuits)?
198. [Expert] Explain the connection between Transformers and Turing completeness. Under what conditions are Transformers Turing complete?
199. [Advanced] How do you benchmark language models? Compare GLUE, SuperGLUE, MMLU, HellaSwag, HumanEval, and other benchmarks.
200. [Expert] What are contamination issues in LLM benchmarking? How do you detect and mitigate benchmark data leakage?
201. [Advanced] Compare different decoding strategies (greedy, beam search, sampling, nucleus sampling) and their impact on generation quality.
202. [Expert] Explain constitutional AI. How does it differ from RLHF for model alignment?

---

## 12. Natural Language Processing

### 12.1 Text Preprocessing

1. [Basic] What is tokenization in NLP? Why is it the first step in most NLP pipelines?
2. [Basic] Explain the difference between word-level, character-level, and subword-level tokenization.
3. [Basic] What are the challenges of word-level tokenization? (out-of-vocabulary words, morphology, compound words)
4. [Basic] What is stemming? How does it differ from lemmatization?
5. [Basic] Compare the Porter Stemmer and the Lancaster Stemmer. What are their trade-offs?
6. [Basic] What is lemmatization? Why does it require a dictionary or morphological analysis?
7. [Intermediate] When would you prefer stemming over lemmatization and vice versa? Give practical examples.
8. [Basic] What are stop words? Should you always remove them? Give examples where stop word removal is harmful.
9. [Basic] Explain lowercasing as a preprocessing step. When might it lose important information?
10. [Basic] What is text normalization? Give examples (handling contractions, Unicode normalization, removing special characters).
11. [Intermediate] What is the Bag of Words (BoW) representation? What are its limitations?
12. [Intermediate] Explain TF-IDF (Term Frequency-Inverse Document Frequency). Write out the formula and explain each component.
13. [Intermediate] How does TF-IDF improve upon raw term frequency for document representation?
14. [Intermediate] What is n-gram language modeling? How do bigrams and trigrams capture local context?
15. [Intermediate] Explain the Zipf's law in the context of word frequencies. How does it affect NLP systems?
16. [Basic] What is sentence segmentation? What challenges arise (abbreviations, decimal points, URLs)?
17. [Intermediate] How do you handle noisy text (social media, typos, informal language) in preprocessing?
18. [Intermediate] What is text deduplication? Why is it important for training data quality?
19. [Advanced] Explain MinHash and LSH (Locality-Sensitive Hashing) for approximate deduplication of text documents.
20. [Basic] What is regular expression-based tokenization? Give examples of patterns for splitting text.
21. [Intermediate] How do you preprocess text for different languages? What challenges arise for languages without whitespace (Chinese, Japanese)?
22. [Intermediate] What is the difference between type and token in NLP? Why does this distinction matter?
23. [Advanced] Explain the role of data cleaning in NLP. How does preprocessing quality affect downstream model performance?
24. [Intermediate] What is spell correction? Describe how edit distance (Levenshtein distance) is used for spelling suggestions.
25. [Advanced] How do you handle HTML/XML content, URLs, emails, and other structured text during preprocessing?

### 12.2 Word Embeddings

26. [Basic] What are word embeddings? How do they differ from one-hot encoding?
27. [Basic] What is the distributional hypothesis? How does it motivate word embeddings?
28. [Intermediate] Explain Word2Vec. What are the two training architectures (CBOW and Skip-gram)?
29. [Intermediate] In CBOW, how does the model predict the center word from surrounding context words?
30. [Intermediate] In Skip-gram, how does the model predict context words from the center word?
31. [Intermediate] What is negative sampling in Word2Vec? How does it approximate the full softmax?
32. [Advanced] Derive the negative sampling objective function for Skip-gram Word2Vec.
33. [Advanced] What is hierarchical softmax? How does it use a Huffman tree to speed up training?
34. [Intermediate] How do you evaluate word embeddings? Explain intrinsic evaluation (analogy tasks, similarity benchmarks).
35. [Intermediate] Explain the famous "king - man + woman = queen" analogy. How does it work with word vectors?
36. [Intermediate] What is GloVe (Global Vectors for Word Representation)? How does it differ from Word2Vec?
37. [Advanced] Explain the GloVe objective function. How does it use the co-occurrence matrix?
38. [Advanced] What is the weighting function in GloVe? Why is it necessary for handling frequent word pairs?
39. [Intermediate] What is FastText? How does it use character n-grams to represent words?
40. [Intermediate] How does FastText handle out-of-vocabulary (OOV) words? Why is this an advantage over Word2Vec?
41. [Advanced] Compare Word2Vec, GloVe, and FastText in terms of: training methodology, handling of rare words, and morphological awareness.
42. [Intermediate] What are the limitations of static word embeddings? Why can't they handle polysemy?
43. [Advanced] Explain ELMo (Embeddings from Language Models). How does it generate context-dependent word representations?
44. [Advanced] How does ELMo combine representations from different BiLSTM layers? What is the task-specific weighted combination?
45. [Intermediate] What is the embedding dimension? How do you choose it for your task?
46. [Intermediate] How do you train word embeddings from scratch vs. using pre-trained embeddings? When is each approach appropriate?
47. [Intermediate] How do you handle pre-trained embeddings for words not in your task vocabulary?
48. [Advanced] Explain the concept of embedding bias. How do word embeddings reflect and amplify societal biases?
49. [Advanced] Describe debiasing techniques for word embeddings (Bolukbasi et al., 2016). What are the limitations of these approaches?
50. [Advanced] What is the relationship between the dimensionality of word embeddings and their quality? What does the Yin & Shen analysis show?
51. [Expert] Explain the connection between word embeddings and pointwise mutual information (PMI). How are GloVe and Word2Vec related to matrix factorization?
52. [Intermediate] How do you visualize word embeddings? Explain t-SNE and UMAP for embedding visualization.
53. [Advanced] What is the difference between type-level and token-level embeddings? How did this distinction change from Word2Vec to BERT?

### 12.3 Subword Tokenization

54. [Basic] What is the motivation for subword tokenization? Why not use word-level or character-level tokenization exclusively?
55. [Intermediate] Explain Byte Pair Encoding (BPE). Describe the algorithm step by step.
56. [Intermediate] How is the BPE vocabulary built? What determines which byte pairs get merged?
57. [Intermediate] What is WordPiece tokenization? How does it differ from BPE in its merge criterion?
58. [Advanced] In WordPiece, the merge criterion is based on likelihood rather than frequency. Explain the formula and its implications.
59. [Intermediate] What is SentencePiece? Why is it useful for languages without explicit word boundaries?
60. [Intermediate] How does SentencePiece treat the input as a raw byte stream? What is the role of the "▁" (space) character?
61. [Advanced] Explain the Unigram Language Model tokenization algorithm used in SentencePiece. How does it differ from BPE?
62. [Advanced] In the Unigram model, how does the algorithm iteratively prune the vocabulary? What is the loss function being optimized?
63. [Intermediate] What is byte-level BPE (BBPE) as used in GPT-2? How does it handle any possible input without unknown tokens?
64. [Intermediate] How does vocabulary size affect tokenization? What are the trade-offs of smaller vs. larger vocabularies?
65. [Advanced] Compare BPE, WordPiece, Unigram, and SentencePiece. When would you use each?
66. [Intermediate] What tokenizer does BERT use? What tokenizer does GPT-2 use? What does Llama use?
67. [Intermediate] How do you train a custom tokenizer for a specific domain? What tools are available (HuggingFace tokenizers)?
68. [Advanced] What is the fertility of a tokenizer? How do you measure and compare tokenizer quality?
69. [Advanced] Explain the tokenizer-model interaction. Why is the tokenizer considered part of the model and not a preprocessing step?
70. [Advanced] How does tokenization affect model performance on different languages? Why do some languages require more tokens per word?
71. [Expert] What is the "tokenization mismatch" problem when fine-tuning models on domain-specific data?
72. [Advanced] Explain the concept of tokenizer-free models. How do character-level or byte-level models like ByT5 work?
73. [Intermediate] How do special tokens ([CLS], [SEP], [PAD], [MASK], <|endoftext|>) fit into the tokenization scheme?
74. [Advanced] What is the impact of tokenization on code generation models? How do tokenizers handle programming language syntax?
75. [Expert] Explain the MegaByte architecture. How does it process patches of bytes rather than individual tokens?
76. [Intermediate] How do you handle numbers in tokenization? Why do language models struggle with arithmetic?
77. [Advanced] What is the compression ratio of a tokenizer? How does it relate to model efficiency?
78. [Expert] Describe the tiktoken tokenizer used by OpenAI. How does it differ from HuggingFace's tokenizer implementations?

### 12.4 Named Entity Recognition & POS Tagging

79. [Basic] What is Named Entity Recognition (NER)? What are common entity types (PERSON, ORG, LOC, DATE, etc.)?
80. [Basic] Explain the BIO (Beginning, Inside, Outside) tagging scheme for NER. Why is it needed?
81. [Intermediate] What is the BIOES (BILOU) tagging scheme? How does it improve upon BIO?
82. [Intermediate] What evaluation metrics are used for NER? Explain entity-level F1 vs. token-level F1.
83. [Intermediate] Describe traditional NER approaches: rule-based, dictionary-based, CRF-based. What are their strengths and limitations?
84. [Advanced] How does a BiLSTM-CRF model work for NER? Why is the CRF layer on top of BiLSTM important?
85. [Advanced] Explain the Viterbi algorithm in the context of CRF-based NER. How does it find the optimal tag sequence?
86. [Advanced] How do you fine-tune BERT for NER? Explain the token classification approach and handling of subword tokens.
87. [Intermediate] What are the challenges of NER for social media text? How do you handle informal language, hashtags, and @mentions?
88. [Advanced] What is nested NER? How do you handle entities that are contained within other entities?
89. [Advanced] Explain few-shot NER. How can you recognize new entity types with limited labeled data?
90. [Intermediate] What is cross-domain NER? How does a model trained on news text transfer to medical or legal text?
91. [Basic] What is Part-of-Speech (POS) tagging? What are common POS tag sets (Penn Treebank, Universal Dependencies)?
92. [Intermediate] Compare rule-based POS tagging vs. statistical POS tagging (HMM, CRF) vs. neural POS tagging.
93. [Intermediate] How does an HMM-based POS tagger work? Explain the generative model and Viterbi decoding.
94. [Advanced] How does dependency parsing work? Explain the difference between transition-based and graph-based parsers.
95. [Intermediate] What is constituency parsing? How does it differ from dependency parsing?
96. [Advanced] Explain the concept of syntactic parsing with Transformers. How do models like BERT implicitly learn syntax?
97. [Intermediate] What is chunking (shallow parsing)? How does it relate to NER and POS tagging?
98. [Advanced] How do you evaluate parsing quality? Explain UAS (Unlabeled Attachment Score) and LAS (Labeled Attachment Score).
99. [Intermediate] What is coreference resolution? Why is it important for NLP applications?
100. [Advanced] Describe span-based models for information extraction. How do they identify and classify spans of text?

### 12.5 Sentiment Analysis & Text Classification

101. [Basic] What is sentiment analysis? What are the main levels of analysis (document, sentence, aspect)?
102. [Basic] What is the difference between binary sentiment analysis and fine-grained sentiment analysis?
103. [Intermediate] Describe the typical pipeline for a sentiment analysis system: data collection, preprocessing, feature extraction, modeling, evaluation.
104. [Intermediate] Compare lexicon-based sentiment analysis (e.g., VADER, SentiWordNet) with machine learning-based approaches.
105. [Intermediate] What is aspect-based sentiment analysis (ABSA)? Why is it more challenging than document-level sentiment analysis?
106. [Advanced] How would you build an ABSA system? Describe the subtasks: aspect extraction, opinion extraction, and sentiment classification.
107. [Intermediate] How do you handle sarcasm, irony, and negation in sentiment analysis?
108. [Advanced] Explain opinion mining and its challenges. How do you handle implicit opinions and comparative opinions?
109. [Intermediate] What evaluation metrics are appropriate for sentiment analysis? Why might accuracy be misleading for imbalanced datasets?
110. [Intermediate] How do you handle class imbalance in text classification? (oversampling, undersampling, class weights, focal loss)
111. [Intermediate] Describe the text classification pipeline using traditional ML: BoW/TF-IDF features + SVM/Naive Bayes/Logistic Regression.
112. [Intermediate] Why is Naive Bayes often a strong baseline for text classification? Explain the bag-of-words assumption.
113. [Intermediate] How does a CNN-based text classifier work? Explain Kim (2014)'s TextCNN architecture.
114. [Advanced] How do you fine-tune BERT for text classification? What is the typical architecture (BERT + linear layer on [CLS])?
115. [Intermediate] What is multi-label text classification? How does it differ from multi-class? What loss function do you use?
116. [Advanced] Explain contrastive learning for text classification. How does it improve representation quality?
117. [Intermediate] How do you handle multilingual text classification? What models support multiple languages?
118. [Advanced] What is zero-shot text classification using NLI (Natural Language Inference) models? How does it work?
119. [Advanced] How do you explain text classification decisions? Describe LIME and SHAP for text.
120. [Advanced] What is the role of data augmentation in text classification? Describe techniques (back-translation, synonym replacement, EDA).
121. [Expert] Design a production sentiment analysis system for customer reviews. Address scalability, real-time processing, and domain adaptation.

### 12.6 Machine Translation

122. [Basic] What is machine translation (MT)? Briefly describe the evolution from rule-based to statistical to neural MT.
123. [Intermediate] Explain Statistical Machine Translation (SMT). What are the main components (translation model, language model, decoder)?
124. [Intermediate] What is the noisy channel model for MT? How does Bayes' rule decompose the translation probability?
125. [Intermediate] Explain phrase-based statistical MT. How does it improve upon word-based MT?
126. [Intermediate] Describe the encoder-decoder approach for Neural Machine Translation (NMT). How does attention improve over the basic seq2seq model?
127. [Intermediate] What is BLEU score? Write out the formula including the brevity penalty. What are its limitations?
128. [Intermediate] What are other MT evaluation metrics? Explain METEOR, chrF, TER, and COMET.
129. [Advanced] Why is BLEU criticized as an evaluation metric? What are better alternatives for evaluating MT quality?
130. [Intermediate] How does beam search work in NMT decoding? What are common beam sizes?
131. [Advanced] What is back-translation? How does it leverage monolingual data to improve NMT?
132. [Advanced] How do you handle low-resource language pairs in NMT? Describe transfer learning and multilingual approaches.
133. [Advanced] What is multilingual NMT? How do models like mBART and NLLB handle many languages in a single model?
134. [Advanced] Explain the concept of zero-shot translation in multilingual NMT. How can a model translate between language pairs never seen during training?
135. [Advanced] What is the "off-target" translation problem in multilingual NMT? How do you mitigate it?
136. [Advanced] How do subword tokenization methods impact MT quality? What is the shared vocabulary approach for multilingual MT?
137. [Expert] Design a real-time translation system for a messaging app. Address latency requirements, language detection, and quality control.
138. [Intermediate] What are the ethical considerations in MT? How do you handle gender bias and cultural sensitivity?
139. [Advanced] Explain document-level machine translation. Why is it harder than sentence-level MT?
140. [Advanced] What is the quality estimation (QE) task in MT? How do you estimate translation quality without reference translations?
141. [Expert] Compare GPT-based translation (prompting) with dedicated NMT models. What are the trade-offs?

### 12.7 Summarization

142. [Basic] What is text summarization? Explain the difference between extractive and abstractive summarization.
143. [Intermediate] Describe extractive summarization methods. How do models like TextRank and BertSumExt select important sentences?
144. [Intermediate] How does TextRank (or LexRank) work? Explain the graph-based approach to sentence extraction.
145. [Intermediate] Describe abstractive summarization. How does the encoder-decoder architecture generate new text for summaries?
146. [Intermediate] Explain the pointer-generator network for summarization. How does it balance copying and generating?
147. [Intermediate] What evaluation metrics are used for summarization? Explain ROUGE-1, ROUGE-2, ROUGE-L, and their limitations.
148. [Advanced] What is BERTScore? How does it use BERT embeddings to evaluate generated text?
149. [Advanced] What is the faithfulness/factual consistency problem in abstractive summarization? How do you detect and prevent hallucinated content?
150. [Advanced] How do you summarize very long documents that exceed model context length? Describe hierarchical and chunking strategies.
151. [Advanced] Explain how T5, BART, and Pegasus are used for abstractive summarization. What pre-training objectives help with summarization?
152. [Intermediate] What is multi-document summarization? How does it differ from single-document summarization?
153. [Advanced] How can LLMs (GPT-4, Claude) be used for summarization? What prompting strategies work best?
154. [Advanced] What is controllable summarization? How do you control the length, style, or focus of generated summaries?
155. [Expert] Design a news summarization system that processes thousands of articles daily. Address deduplication, multi-document summarization, and real-time requirements.

### 12.8 Question Answering & Information Retrieval

156. [Basic] What are the main types of question answering: extractive QA, abstractive QA, and open-domain QA?
157. [Intermediate] How does extractive QA work? Explain the span prediction approach (predicting start and end positions).
158. [Intermediate] Describe the SQuAD dataset and benchmark. What metrics are used (Exact Match, F1)?
159. [Intermediate] How is BERT used for extractive QA? Explain the architecture and training process.
160. [Advanced] What is open-domain QA? Describe the retriever-reader architecture (e.g., DPR + reader model).
161. [Advanced] Explain Dense Passage Retrieval (DPR). How does it use BERT embeddings for passage retrieval?
162. [Advanced] Compare sparse retrieval (BM25/TF-IDF) with dense retrieval (DPR, ColBERT). What are the trade-offs?
163. [Advanced] What is ColBERT? How does its late interaction mechanism improve retrieval quality and efficiency?
164. [Advanced] Explain the retrieval-augmented generation (RAG) framework. How does it combine retrieval with generation?
165. [Advanced] What are the main components of a RAG system? Describe the retriever, generator, and how they interact.
166. [Advanced] How do you handle unanswerable questions in QA? How does SQuAD 2.0 address this?
167. [Intermediate] What is knowledge-grounded QA? How do you incorporate external knowledge bases?
168. [Advanced] Explain the concept of multi-hop question answering. How do models like HotpotQA handle questions requiring reasoning over multiple passages?
169. [Intermediate] What is conversational QA? How does it differ from single-turn QA?
170. [Advanced] How do you evaluate open-domain QA systems? Discuss metrics and challenges in evaluating retrieved passages and generated answers.
171. [Expert] Design a customer support QA system using RAG. Address document ingestion, embedding storage (vector database), retrieval, generation, and answer validation.
172. [Intermediate] What is BM25? Explain the scoring function and its relationship to TF-IDF.
173. [Advanced] Explain vector databases (Pinecone, Weaviate, Milvus, ChromaDB). How do they enable efficient similarity search?
174. [Advanced] What is Approximate Nearest Neighbor (ANN) search? Explain HNSW and IVF indexing methods.
175. [Advanced] How do you chunk documents for RAG? What are the strategies and trade-offs (fixed size, semantic, recursive)?
176. [Expert] What is the "lost in the middle" problem for long-context QA? How does it affect retrieval and generation?
177. [Advanced] How do reranking models (cross-encoders) improve retrieval quality? Compare bi-encoder vs. cross-encoder approaches.
178. [Expert] Design a semantic search engine for a large document corpus. Describe indexing, query processing, retrieval, reranking, and result presentation.

### 12.9 Modern NLP: Zero-Shot, Few-Shot & Prompt Engineering

179. [Basic] What is zero-shot learning in NLP? How do LLMs perform tasks they weren't explicitly trained on?
180. [Basic] What is few-shot learning? How does providing a few examples in the prompt help LLMs?
181. [Intermediate] What is prompt engineering? Why has it become a critical skill for working with LLMs?
182. [Intermediate] Compare zero-shot, one-shot, and few-shot prompting. When does each approach work best?
183. [Intermediate] What are the best practices for writing effective prompts? Give examples for different tasks.
184. [Intermediate] What is chain-of-thought (CoT) prompting? How does it improve reasoning in LLMs?
185. [Advanced] Explain zero-shot chain-of-thought ("Let's think step by step"). Why does this simple prompt improve performance?
186. [Advanced] What is self-consistency in CoT prompting? How does sampling multiple reasoning paths improve accuracy?
187. [Advanced] Explain the tree-of-thought prompting approach. How does it extend chain-of-thought?
188. [Intermediate] What is the role of system prompts in LLMs? How do they guide model behavior?
189. [Intermediate] Explain the difference between task instructions and demonstrations in prompting.
190. [Advanced] What is prompt chaining? How do you break complex tasks into sequential prompt steps?
191. [Advanced] Explain ReAct (Reasoning + Acting) prompting. How does it combine reasoning with tool use?
192. [Advanced] What is the sensitivity of LLMs to prompt formatting? How do small changes in prompt structure affect output quality?
193. [Advanced] What are the limitations of in-context learning? When should you fine-tune instead of prompt?
194. [Expert] Explain automatic prompt optimization (APO) and DSPy. How do they automate the prompt engineering process?
195. [Intermediate] How do you evaluate the quality of LLM-generated outputs? What metrics and human evaluation methods are used?
196. [Advanced] What is the "lost in the middle" effect for long-context LLMs? How does it impact information retrieval in prompts?
197. [Advanced] Explain structured output generation. How do you reliably get JSON, code, or other structured formats from LLMs?
198. [Advanced] What is the role of function calling / tool use in modern LLMs? How does it extend their capabilities?
199. [Expert] How do you build an LLM agent? Describe the planning, memory, tool use, and execution loop.
200. [Expert] Explain the challenges of LLM evaluation. Compare benchmarks (MMLU, HumanEval, GSM8K, ARC) and their limitations.
201. [Advanced] What is the hallucination problem in LLMs? What are the types (factual, faithful) and how do you mitigate them?
202. [Expert] How do you build a reliable, production-grade LLM application? Address prompt versioning, monitoring, fallbacks, and cost management.

### 12.10 Advanced NLP Topics

203. [Intermediate] What is transfer learning in NLP? Explain the pretrain-finetune paradigm.
204. [Advanced] Explain the concept of language model distillation. How do you create smaller models that maintain performance?
205. [Advanced] What is data augmentation for NLP? Describe techniques: back-translation, paraphrase generation, contextual word augmentation.
206. [Advanced] Explain active learning for NLP. How do you efficiently select examples for annotation?
207. [Intermediate] What is domain adaptation in NLP? How do you adapt pre-trained models to specialized domains (medical, legal, financial)?
208. [Advanced] Explain continued pre-training for domain adaptation. When is it better than just fine-tuning?
209. [Intermediate] What is multi-task learning in NLP? How does training on multiple tasks simultaneously improve performance?
210. [Advanced] What is curriculum learning for NLP? How does ordering training examples by difficulty affect learning?
211. [Advanced] Explain contrastive learning in NLP. How do models like SimCSE create sentence embeddings?
212. [Advanced] What is the relationship between NLP and knowledge graphs? How can you integrate structured knowledge with language models?
213. [Advanced] Explain cross-lingual transfer learning. How do multilingual models enable NLP in low-resource languages?
214. [Expert] What is instruction tuning? How does it improve the zero-shot capabilities of LLMs?
215. [Expert] Describe the RLHF pipeline in detail. What are the challenges of reward model training?
216. [Intermediate] What is text generation evaluation? Compare perplexity, BLEU, ROUGE, METEOR, BERTScore, and human evaluation.
217. [Advanced] What is the decoding strategy for open-ended generation? Compare sampling-based methods (top-k, top-p, temperature) with search-based methods (beam search).
218. [Advanced] Explain the concept of grounding in NLP. How do you ensure LLM outputs are grounded in provided context or retrieved information?
219. [Expert] What are the main challenges in building production NLP systems? Discuss data quality, model selection, latency, scalability, and monitoring.
220. [Advanced] How do you handle multimodal inputs in NLP (text + images, text + tables)? Describe relevant architectures.
221. [Intermediate] What is information extraction (IE)? Describe the subtasks: NER, relation extraction, event extraction.
222. [Advanced] Explain relation extraction. How do you identify relationships between entities in text?
223. [Advanced] What is event extraction? How do you identify events, triggers, and arguments in text?
224. [Intermediate] What is text-to-SQL? How do models translate natural language queries into database queries?
225. [Advanced] Explain the challenges of text-to-SQL. How do you handle schema understanding, complex queries, and domain adaptation?
226. [Advanced] What is semantic parsing? How does it differ from text-to-SQL?
227. [Intermediate] What is dialogue systems? Compare task-oriented dialogue and open-domain dialogue.
228. [Advanced] Explain the components of a task-oriented dialogue system: NLU, dialogue state tracking, dialogue policy, NLG.
229. [Advanced] What is dialogue state tracking (DST)? How do modern approaches use LLMs for DST?
230. [Intermediate] What is natural language inference (NLI)? Explain the entailment, contradiction, and neutral labels.
231. [Advanced] How is NLI used as a backbone for zero-shot classification? Explain the hypothesis-based approach.
232. [Intermediate] What is semantic similarity? How do you measure the similarity between two text passages?
233. [Advanced] Explain sentence transformers and their training with contrastive loss. How do they produce meaningful sentence embeddings?
234. [Advanced] What is cross-encoder vs. bi-encoder for semantic similarity? When would you use each?
235. [Expert] Design a document understanding system that processes contracts, invoices, and forms. Address OCR integration, layout understanding, and information extraction.
236. [Advanced] What are the privacy and security concerns with NLP models? Explain data leakage, prompt injection, and adversarial attacks.
237. [Expert] Explain prompt injection attacks. How do adversaries manipulate LLMs through crafted inputs?
238. [Expert] What are the approaches to LLM safety? Describe red-teaming, guardrails, and safety fine-tuning.
239. [Advanced] How do you build a multilingual NLP system from scratch for 50+ languages? Discuss data collection, model selection, and evaluation challenges.
240. [Expert] What is the future of NLP? Discuss trends: multimodal models, agents, long-context models, efficient architectures, and reasoning capabilities.
241. [Intermediate] What is Named Entity Linking (NEL)? How does it differ from Named Entity Recognition?
242. [Advanced] Explain the concept of temporal information extraction. How do you extract dates, durations, and temporal relations from text?
243. [Intermediate] What is topic modeling? Compare LDA (Latent Dirichlet Allocation) with neural topic models.
244. [Advanced] How do you build a text-based recommendation system? Describe content-based and collaborative filtering approaches.
245. [Advanced] What is abstractive question answering? How does it differ from extractive QA and when is it preferred?
246. [Intermediate] What are language model probes? How do you test what knowledge a model has without fine-tuning?
247. [Expert] Design an enterprise search system with semantic understanding, personalization, and multi-language support. Detail the full architecture.
248. [Advanced] Explain the concept of model cascading for NLP. How do you combine cheap models with expensive models for cost-effective inference?
249. [Expert] How do you build a fact-checking system using NLP? Describe claim detection, evidence retrieval, and verdict prediction.
250. [Expert] What is constitutional AI? How does it approach alignment through a set of principles rather than human feedback?
251. [Advanced] How do transformer models handle long documents (>100K tokens)? Compare chunking, hierarchical attention, and extended-context models.
252. [Expert] Describe the architecture and training of a modern code generation model (Codex, StarCoder, DeepSeek-Coder). How is it specialized for programming tasks?
253. [Advanced] What is instruction following vs. instruction tuning? How do they relate to aligning LLMs with user intent?
254. [Advanced] Explain the concept of model merging. How can you combine multiple fine-tuned models without retraining?
255. [Expert] What is federated learning for NLP? How can you train models on distributed private data without centralizing it?

---

## Appendix: Quick Reference Summary

### Key Formulas

**Vanilla RNN:**
h_t = tanh(W_hh · h_{t-1} + W_xh · x_t + b_h)

**LSTM Gates:**
f_t = σ(W_f · [h_{t-1}, x_t] + b_f)
i_t = σ(W_i · [h_{t-1}, x_t] + b_i)
c̃_t = tanh(W_c · [h_{t-1}, x_t] + b_c)
c_t = f_t ⊙ c_{t-1} + i_t ⊙ c̃_t
o_t = σ(W_o · [h_{t-1}, x_t] + b_o)
h_t = o_t ⊙ tanh(c_t)

**GRU Gates:**
z_t = σ(W_z · [h_{t-1}, x_t])
r_t = σ(W_r · [h_{t-1}, x_t])
h̃_t = tanh(W · [r_t ⊙ h_{t-1}, x_t])
h_t = (1 - z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t

**Scaled Dot-Product Attention:**
Attention(Q, K, V) = softmax(QK^T / √d_k) · V

**Multi-Head Attention:**
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) · W^O
where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)

**Sinusoidal Positional Encoding:**
PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

**TF-IDF:**
TF-IDF(t, d) = TF(t, d) × log(N / DF(t))

**BLEU Score:**
BLEU = BP · exp(Σ w_n · log(p_n))
BP = min(1, exp(1 - r/c))

### Question Count Summary

| Category | Subcategory | Count |
|----------|------------|-------|
| 10. Sequence Models & Attention | 10.1 RNN Fundamentals | 25 |
| | 10.2 LSTMs & GRUs | 25 |
| | 10.3 Seq2Seq & Encoder-Decoder | 18 |
| | 10.4 Attention Mechanisms | 30 |
| | 10.5 Positional Encoding | 22 |
| | 10.6 Advanced Sequence Modeling | 32 |
| **Subtotal** | | **152** |
| 11. Transformers Architecture | 11.1 Original Transformer | 24 |
| | 11.2 BERT & Variants | 26 |
| | 11.3 GPT Family | 28 |
| | 11.4 T5, BART & Enc-Dec | 14 |
| | 11.5 Efficient Transformers | 25 |
| | 11.6 MoE & Modern Architectures | 24 |
| | 11.7 Training & Optimization | 12 |
| | 11.8 PEFT | 10 |
| | 11.9 Applications & Design | 11 |
| | 11.10 Interpretability & Analysis | 28 |
| **Subtotal** | | **202** |
| 12. Natural Language Processing | 12.1 Text Preprocessing | 25 |
| | 12.2 Word Embeddings | 28 |
| | 12.3 Subword Tokenization | 25 |
| | 12.4 NER & POS Tagging | 22 |
| | 12.5 Sentiment & Classification | 21 |
| | 12.6 Machine Translation | 20 |
| | 12.7 Summarization | 14 |
| | 12.8 QA & Information Retrieval | 23 |
| | 12.9 Zero-Shot, Few-Shot, Prompts | 24 |
| | 12.10 Advanced NLP Topics | 53 |
| **Subtotal** | | **255** |
| **TOTAL** | | **609** |
