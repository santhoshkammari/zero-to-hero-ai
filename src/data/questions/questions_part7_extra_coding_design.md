# Part 7: Coding, System Design, Case Studies & Cutting-Edge

> 800+ questions covering hands-on ML implementation, system design, real-world debugging scenarios, and cutting-edge research topics. These reflect what top companies (FAANG, startups, AI labs) actually ask in 2024–2025 interviews.

---

## A. ML Coding & Implementation (250+ Questions)

### A.1 Linear Models from Scratch

1. [Intermediate] Implement simple linear regression using only NumPy with the closed-form (normal equation) solution. Include bias handling.
2. [Intermediate] Implement linear regression with mini-batch gradient descent using only NumPy. Support configurable learning rate and epochs.
3. [Intermediate] Add L2 regularization (Ridge) to your linear regression implementation. Show how the gradient changes.
4. [Intermediate] Add L1 regularization (Lasso) to your linear regression. Implement subgradient descent for the non-differentiable L1 term.
5. [Advanced] Implement Elastic Net regression from scratch combining L1 and L2 penalties with a mixing parameter alpha.
6. [Intermediate] Implement polynomial regression by manually constructing polynomial features and applying linear regression.
7. [Intermediate] Implement logistic regression from scratch using NumPy with sigmoid activation and binary cross-entropy loss.
8. [Intermediate] Extend your logistic regression to multi-class using the one-vs-rest (OvR) strategy.
9. [Advanced] Implement multinomial logistic regression (softmax regression) from scratch with cross-entropy loss.
10. [Advanced] Implement Newton's method for logistic regression optimization. Compare convergence speed with gradient descent.
11. [Intermediate] Write a function to compute the analytical solution for Ridge regression and compare with your gradient descent version.
12. [Basic] Implement the sigmoid function with numerical stability (handling large positive/negative inputs).
13. [Basic] Implement the softmax function with numerical stability using the log-sum-exp trick.
14. [Intermediate] Implement weighted linear regression where each sample has an associated weight.
15. [Advanced] Implement Bayesian linear regression from scratch. Compute the posterior distribution of weights.
16. [Intermediate] Implement Locally Weighted Linear Regression (LWLR) from scratch. Explain the kernel bandwidth parameter.
17. [Advanced] Implement IRLS (Iteratively Reweighted Least Squares) for logistic regression.
18. [Intermediate] Implement Perceptron learning algorithm from scratch. Show convergence on linearly separable data.
19. [Intermediate] Write code to compute the closed-form solution and compare it numerically with gradient descent for different dataset sizes. At what point does one become preferable?
20. [Advanced] Implement Huber regression from scratch that is robust to outliers. Compare with ordinary least squares on contaminated data.

### A.2 Tree-Based Models from Scratch

21. [Advanced] Implement a decision tree classifier from scratch using Gini impurity as the splitting criterion.
22. [Advanced] Implement a decision tree classifier using information gain (entropy) as the splitting criterion.
23. [Advanced] Add support for continuous features in your decision tree (find optimal split thresholds).
24. [Advanced] Implement pre-pruning in your decision tree (max depth, min samples per leaf, min impurity decrease).
25. [Expert] Implement post-pruning (reduced error pruning) for your decision tree.
26. [Advanced] Implement a decision tree regressor from scratch using variance reduction as the splitting criterion.
27. [Expert] Implement a Random Forest classifier from scratch using bootstrap sampling and random feature subsets.
28. [Expert] Implement out-of-bag (OOB) error estimation for your Random Forest.
29. [Expert] Implement feature importance computation for your Random Forest using mean decrease in impurity.
30. [Expert] Implement a basic Gradient Boosting classifier from scratch using decision tree stumps.
31. [Expert] Implement Gradient Boosting for regression with configurable loss functions (MSE, MAE, Huber).
32. [Expert] Implement a simplified version of XGBoost with L2-regularized objective and approximate split finding.
33. [Advanced] Implement the AdaBoost algorithm from scratch using decision stumps as weak learners.
34. [Advanced] Implement CART (Classification and Regression Trees) that handles both classification and regression.
35. [Intermediate] Write code to visualize a decision tree's splits on a 2D dataset.
36. [Advanced] Implement Extra Trees (Extremely Randomized Trees) from scratch — what changes vs Random Forest?
37. [Expert] Implement histogram-based gradient boosting (similar to LightGBM's approach) for faster split finding.
38. [Advanced] Implement feature importance using permutation importance for any tree-based model.
39. [Advanced] Implement a decision tree that handles missing values (surrogate splits or missing value direction).
40. [Expert] Implement the isolation forest algorithm from scratch for anomaly detection.

### A.3 Clustering Algorithms from Scratch

41. [Intermediate] Implement K-Means clustering from scratch with random initialization. Handle convergence detection.
42. [Intermediate] Implement K-Means++ initialization to improve cluster quality.
43. [Advanced] Modify your K-Means to handle empty clusters gracefully (reinitialize from farthest point).
44. [Intermediate] Implement the elbow method to determine optimal K. Plot within-cluster sum of squares vs K.
45. [Advanced] Implement the silhouette score from scratch. Use it to evaluate clustering quality.
46. [Advanced] Implement DBSCAN clustering from scratch. Handle core points, border points, and noise.
47. [Advanced] Implement hierarchical agglomerative clustering with single, complete, and average linkage.
48. [Expert] Implement Gaussian Mixture Models (GMM) from scratch using the EM algorithm.
49. [Expert] Implement the full EM algorithm for GMM including E-step, M-step, and log-likelihood monitoring.
50. [Intermediate] Implement Mini-Batch K-Means for scalability. Compare convergence with standard K-Means.
51. [Advanced] Implement the Mean Shift clustering algorithm from scratch.
52. [Advanced] Implement spectral clustering from scratch using the graph Laplacian.
53. [Intermediate] Implement the Calinski-Harabasz index for evaluating clustering quality.
54. [Intermediate] Implement the Davies-Bouldin index from scratch.
55. [Advanced] Implement K-Medoids (PAM algorithm) from scratch. How does it differ from K-Means?
56. [Expert] Implement online/streaming K-Means that can process data points one at a time.
57. [Advanced] Implement fuzzy C-Means clustering where each point has a membership degree to each cluster.
58. [Intermediate] Write code to compare different distance metrics (Euclidean, Manhattan, Cosine) in K-Means.
59. [Advanced] Implement OPTICS clustering algorithm from scratch. How does it relate to DBSCAN?
60. [Expert] Implement a clustering algorithm that automatically determines the number of clusters (e.g., X-Means).

### A.4 Dimensionality Reduction from Scratch

61. [Intermediate] Implement PCA from scratch using eigendecomposition of the covariance matrix.
62. [Intermediate] Implement PCA using SVD. Explain why SVD is preferred over eigendecomposition.
63. [Advanced] Implement incremental/online PCA that can process data in batches.
64. [Advanced] Implement kernel PCA from scratch using the RBF kernel.
65. [Advanced] Implement t-SNE from scratch with Barnes-Hut approximation awareness (implement naive version).
66. [Expert] Implement the core t-SNE algorithm: compute pairwise affinities, gradient of KL divergence, and optimization.
67. [Intermediate] Implement LDA (Linear Discriminant Analysis) for dimensionality reduction from scratch.
68. [Advanced] Implement UMAP from scratch (simplified version with nearest neighbor graph and fuzzy set operations).
69. [Intermediate] Write code to determine the optimal number of PCA components using explained variance ratio.
70. [Advanced] Implement Isomap from scratch: k-nearest neighbor graph, shortest paths, and MDS embedding.
71. [Advanced] Implement Non-negative Matrix Factorization (NMF) from scratch using multiplicative update rules.
72. [Intermediate] Implement random projection (Johnson-Lindenstrauss) for dimensionality reduction.
73. [Advanced] Implement Sparse PCA from scratch with L1 penalty on the components.
74. [Intermediate] Implement truncated SVD from scratch using power iteration method.
75. [Expert] Implement an autoencoder in NumPy (without deep learning frameworks) for non-linear dimensionality reduction.

### A.5 Neural Networks from Scratch

76. [Intermediate] Implement a single-layer perceptron for binary classification from scratch in NumPy.
77. [Intermediate] Implement a multi-layer perceptron (MLP) with one hidden layer from scratch with forward and backward pass.
78. [Advanced] Implement a full MLP with arbitrary number of hidden layers, configurable activations, and backpropagation.
79. [Intermediate] Implement ReLU, Sigmoid, Tanh, and their derivatives from scratch.
80. [Advanced] Implement Leaky ReLU, ELU, GELU, Swish/SiLU activations and their derivatives.
81. [Advanced] Implement batch normalization from scratch — both training and inference modes.
82. [Advanced] Implement layer normalization from scratch. Compare with batch normalization.
83. [Advanced] Implement dropout from scratch. Handle the scaling factor during training and inference.
84. [Expert] Implement a convolutional layer (Conv2D) from scratch with forward and backward pass using im2col.
85. [Expert] Implement max pooling and average pooling layers from scratch with forward and backward pass.
86. [Advanced] Implement SGD with momentum from scratch. Show the momentum update equations.
87. [Advanced] Implement the Adam optimizer from scratch with bias correction.
88. [Advanced] Implement AdaGrad and RMSProp optimizers from scratch.
89. [Expert] Implement the AdamW optimizer (Adam with decoupled weight decay) from scratch.
90. [Expert] Implement learning rate schedulers: step decay, cosine annealing, warm-up + cosine from scratch.
91. [Intermediate] Implement binary cross-entropy loss and its gradient from scratch.
92. [Intermediate] Implement categorical cross-entropy loss with softmax and its gradient (numerically stable).
93. [Advanced] Implement focal loss from scratch. Explain when and why it helps.
94. [Expert] Implement gradient clipping (by norm and by value) from scratch.
95. [Expert] Implement a simple automatic differentiation engine (like micrograd) supporting basic operations.
96. [Advanced] Implement weight initialization methods: Xavier/Glorot, He/Kaiming initialization from scratch.
97. [Expert] Implement a recurrent neural network (vanilla RNN) cell from scratch with BPTT.
98. [Expert] Implement an LSTM cell from scratch with all gates (forget, input, output, cell state).
99. [Expert] Implement a GRU cell from scratch. Compare the number of parameters with LSTM.
100. [Expert] Implement a bidirectional RNN from scratch.

### A.6 Attention & Transformers from Scratch

101. [Advanced] Implement scaled dot-product attention from scratch in NumPy.
102. [Expert] Implement multi-head self-attention from scratch in PyTorch (no nn.MultiheadAttention).
103. [Expert] Implement a full transformer encoder block from scratch: multi-head attention + FFN + LayerNorm + residual connections.
104. [Expert] Implement positional encoding (sinusoidal) from scratch.
105. [Expert] Implement a full transformer decoder block with masked self-attention and cross-attention.
106. [Expert] Implement causal (autoregressive) attention masking from scratch.
107. [Expert] Implement Rotary Position Embedding (RoPE) from scratch. Show the rotation matrix formulation.
108. [Expert] Implement ALiBi (Attention with Linear Biases) positional encoding from scratch.
109. [Expert] Implement grouped query attention (GQA) from scratch. Compare memory usage with standard MHA.
110. [Expert] Implement KV-cache for efficient autoregressive generation.
111. [Expert] Implement a simple GPT-style language model from scratch in PyTorch (embeddings, transformer blocks, LM head).
112. [Advanced] Implement the BERT masked language model training objective from scratch.
113. [Expert] Implement multi-query attention from scratch. What is the memory saving vs multi-head attention?
114. [Expert] Implement sliding window attention from scratch (as used in Mistral/Longformer).
115. [Expert] Implement a simple vision transformer (ViT) patch embedding + transformer encoder from scratch.
116. [Expert] Implement cross-attention between two different sequences from scratch.
117. [Advanced] Implement attention score visualization code that creates heatmaps of attention weights.
118. [Expert] Implement flash-attention-style tiled computation in Python/NumPy (conceptual, not CUDA-optimized).
119. [Expert] Implement a mixture-of-experts layer with top-k routing from scratch in PyTorch.
120. [Expert] Implement the SwiGLU activation function used in modern transformers (LLaMA) from scratch.

### A.7 NLP & Tokenization from Scratch

121. [Intermediate] Implement Bag-of-Words (BoW) text representation from scratch.
122. [Intermediate] Implement TF-IDF from scratch. Handle document frequency computation.
123. [Advanced] Implement BPE (Byte Pair Encoding) tokenizer from scratch — both training and encoding.
124. [Advanced] Implement WordPiece tokenizer from scratch.
125. [Advanced] Implement a character-level language model with RNN from scratch.
126. [Advanced] Implement Word2Vec (Skip-gram with negative sampling) training loop from scratch.
127. [Expert] Implement the GloVe training objective from scratch.
128. [Intermediate] Implement text preprocessing pipeline: tokenization, stemming, lemmatization, stop word removal.
129. [Advanced] Implement beam search decoding from scratch for sequence generation.
130. [Advanced] Implement greedy decoding, top-k sampling, top-p (nucleus) sampling, and temperature scaling for text generation.
131. [Expert] Implement the SentencePiece unigram language model tokenizer from scratch.
132. [Advanced] Implement a simple seq2seq model with attention from scratch in PyTorch.
133. [Intermediate] Implement the Levenshtein (edit) distance algorithm from scratch.
134. [Advanced] Implement the Viterbi algorithm for sequence labeling (POS tagging / NER).
135. [Expert] Implement a CRF (Conditional Random Field) layer for sequence labeling from scratch.
136. [Intermediate] Implement n-gram language model with Laplace smoothing from scratch.
137. [Advanced] Implement BLEU score computation from scratch.
138. [Advanced] Implement ROUGE score computation from scratch.
139. [Intermediate] Implement cosine similarity based document retrieval from scratch.
140. [Advanced] Implement the BM25 ranking algorithm from scratch.
141. [Expert] Implement a simple RAG (Retrieval Augmented Generation) pipeline from scratch using embeddings + vector similarity + LLM prompting.
142. [Advanced] Implement a text classification pipeline with CNN (TextCNN) from scratch in PyTorch.
143. [Expert] Implement a simple version of the RLHF reward model training loop.
144. [Advanced] Implement perplexity computation for a language model from scratch.
145. [Advanced] Implement the CTC (Connectionist Temporal Classification) loss forward pass from scratch.

### A.8 Computer Vision Coding

146. [Intermediate] Implement image convolution (2D) from scratch using nested loops. Then optimize with im2col.
147. [Advanced] Implement a basic CNN for MNIST from scratch in PyTorch (no torchvision models).
148. [Advanced] Implement data augmentation transforms from scratch: random crop, horizontal flip, rotation, color jitter.
149. [Advanced] Implement non-maximum suppression (NMS) for object detection from scratch.
150. [Expert] Implement IoU (Intersection over Union) computation and the mAP metric from scratch.
151. [Advanced] Implement a basic ResNet residual block from scratch in PyTorch.
152. [Expert] Implement depthwise separable convolution (MobileNet-style) from scratch.
153. [Intermediate] Implement image histogram equalization from scratch using NumPy.
154. [Advanced] Implement bilinear interpolation for image resizing from scratch.
155. [Expert] Implement RoI Pooling from scratch for object detection.
156. [Advanced] Implement the anchor generation mechanism for object detection (like Faster R-CNN).
157. [Expert] Implement a simple U-Net architecture from scratch in PyTorch for segmentation.
158. [Advanced] Implement Grad-CAM visualization from scratch in PyTorch.
159. [Expert] Implement a simple GAN (Generator + Discriminator) from scratch in PyTorch. Train on MNIST.
160. [Expert] Implement the DDPM (Denoising Diffusion Probabilistic Model) forward and reverse process from scratch.
161. [Advanced] Implement the FPN (Feature Pyramid Network) architecture from scratch.
162. [Expert] Implement patch embedding for Vision Transformers from scratch.
163. [Intermediate] Implement Gaussian blur filter from scratch using NumPy.
164. [Advanced] Implement the Sobel edge detection filter from scratch.
165. [Expert] Implement the YOLO-style grid-based detection head from scratch.

### A.9 Recommender Systems Coding

166. [Intermediate] Implement collaborative filtering (user-based) from scratch using cosine similarity.
167. [Intermediate] Implement item-based collaborative filtering from scratch.
168. [Advanced] Implement matrix factorization for recommendations using ALS (Alternating Least Squares) from scratch.
169. [Advanced] Implement matrix factorization using SGD from scratch with bias terms.
170. [Expert] Implement a simple neural collaborative filtering model from scratch in PyTorch.
171. [Advanced] Implement the SVD++ algorithm from scratch.
172. [Intermediate] Implement content-based filtering using TF-IDF features from scratch.
173. [Advanced] Implement the BPR (Bayesian Personalized Ranking) loss and training loop from scratch.
174. [Advanced] Implement evaluation metrics for recommender systems: precision@k, recall@k, NDCG@k, MAP from scratch.
175. [Expert] Implement a two-tower model (query tower + item tower) from scratch in PyTorch.

### A.10 Evaluation Metrics & Cross-Validation from Scratch

176. [Basic] Implement accuracy, precision, recall, and F1-score from scratch.
177. [Intermediate] Implement the confusion matrix computation from scratch.
178. [Intermediate] Implement ROC curve and AUC computation from scratch.
179. [Intermediate] Implement precision-recall curve computation from scratch.
180. [Intermediate] Implement K-fold cross-validation from scratch.
181. [Intermediate] Implement stratified K-fold cross-validation from scratch.
182. [Advanced] Implement leave-one-out cross-validation (LOOCV) from scratch.
183. [Advanced] Implement time-series cross-validation (expanding window) from scratch.
184. [Advanced] Implement the log-loss (binary cross-entropy) metric from scratch with numerical stability.
185. [Advanced] Implement the Matthews Correlation Coefficient (MCC) from scratch.
186. [Intermediate] Implement mean squared error, mean absolute error, and R-squared from scratch.
187. [Advanced] Implement the Brier score from scratch for probability calibration evaluation.
188. [Advanced] Implement calibration curve (reliability diagram) computation from scratch.
189. [Advanced] Implement Cohen's Kappa score from scratch.
190. [Intermediate] Implement the bootstrap method for confidence interval estimation of any metric.

### A.11 Feature Engineering & Preprocessing

191. [Basic] Implement min-max normalization from scratch.
192. [Basic] Implement z-score standardization from scratch.
193. [Intermediate] Implement one-hot encoding from scratch (handling unseen categories at test time).
194. [Intermediate] Implement label encoding from scratch.
195. [Advanced] Implement target encoding (mean encoding) with smoothing from scratch.
196. [Intermediate] Implement missing value imputation strategies: mean, median, mode, KNN-imputation from scratch.
197. [Advanced] Implement feature hashing (hashing trick) from scratch.
198. [Intermediate] Implement ordinal encoding from scratch.
199. [Advanced] Implement binning/discretization of continuous features from scratch.
200. [Advanced] Implement weight-of-evidence (WoE) encoding from scratch.
201. [Intermediate] Implement robust scaler (using median and IQR) from scratch.
202. [Advanced] Implement quantile transformation from scratch.
203. [Advanced] Implement SMOTE (Synthetic Minority Over-sampling) from scratch.
204. [Intermediate] Implement stratified train/test split from scratch.
205. [Advanced] Implement Recursive Feature Elimination (RFE) from scratch using any base model.

### A.12 Classical ML Algorithms from Scratch

206. [Intermediate] Implement k-Nearest Neighbors (k-NN) classifier from scratch with configurable distance metrics.
207. [Intermediate] Implement k-NN regressor from scratch.
208. [Advanced] Implement a KD-Tree from scratch for efficient nearest neighbor search.
209. [Advanced] Implement Naive Bayes classifier (Gaussian, Multinomial, Bernoulli) from scratch.
210. [Advanced] Implement Support Vector Machine (SVM) with SMO (Sequential Minimal Optimization) from scratch.
211. [Expert] Implement kernel SVM from scratch with RBF kernel.
212. [Advanced] Implement the kernel trick for SVM: polynomial, RBF, and sigmoid kernels.
213. [Expert] Implement the Gaussian Process regressor from scratch with kernel functions.
214. [Intermediate] Implement the k-NN algorithm with weighted voting (distance-weighted).
215. [Advanced] Implement Locally Linear Embedding (LLE) from scratch.

### A.13 Optimization & Training Techniques

216. [Intermediate] Implement grid search with cross-validation from scratch.
217. [Intermediate] Implement random search for hyperparameter optimization from scratch.
218. [Advanced] Implement early stopping with patience from scratch.
219. [Advanced] Implement learning rate warm-up from scratch.
220. [Expert] Implement cyclical learning rate scheduler from scratch.
221. [Expert] Implement a simple Bayesian Optimization loop from scratch with Gaussian Process surrogate.
222. [Advanced] Implement gradient accumulation from scratch in PyTorch for simulating larger batch sizes.
223. [Advanced] Implement mixed precision training wrapper from scratch (conceptual implementation).
224. [Expert] Implement a distributed data-parallel training loop skeleton from scratch.
225. [Advanced] Implement label smoothing from scratch.
226. [Advanced] Implement mixup data augmentation from scratch.
227. [Advanced] Implement cutmix data augmentation from scratch.
228. [Expert] Implement the LAMB optimizer from scratch (used for large-batch training).
229. [Intermediate] Implement L2 regularization as weight decay in training loop from scratch.
230. [Advanced] Implement exponential moving average (EMA) of model weights from scratch.

### A.14 Code Debugging & Bug Finding

231. [Intermediate] Debug: This training loop has a bug where the model never learns. The loss is constant. Find the issue.
```python
model = MyModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
for epoch in range(100):
    for x, y in dataloader:
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        # Bug: missing optimizer.step() and optimizer.zero_grad()
```

232. [Intermediate] Debug: The model trains fine but predictions at inference are random. What's wrong?
```python
# Bug: model.eval() is never called, so dropout/batchnorm behave differently
model.train()  # Should be model.eval() at inference
predictions = model(test_data)
```

233. [Advanced] Debug: Training loss goes to NaN after a few epochs. Identify potential causes and fixes.
234. [Advanced] Debug: The model performs perfectly on training data but terribly on validation. Accuracy: train=99.9%, val=52%. Diagnose.
235. [Advanced] Debug: A data pipeline has a subtle label leakage bug. Find it in this preprocessing code that applies transformations before train/test split.
236. [Intermediate] Debug: This evaluation code reports 95% accuracy but the model is actually terrible. Find the metric computation bug (hint: class imbalance + accuracy).
237. [Advanced] Debug: This multi-GPU training code produces different results each run despite setting random seeds. Find the non-determinism source.
238. [Advanced] Debug: The learning rate scheduler is applied but the learning rate never actually changes. Find the bug.
239. [Expert] Debug: A transformer model's attention weights are all uniform (1/seq_len). What could cause this and how to fix it?
240. [Advanced] Debug: The model checkpoint saves correctly but loading it produces worse performance. What could be wrong?
241. [Intermediate] Debug: Data augmentation is applied to both training AND validation sets causing inflated validation metrics. Fix the pipeline.
242. [Advanced] Debug: Gradient accumulation code produces different results than actual large-batch training. Find the normalization bug.
243. [Expert] Debug: A distributed training job hangs indefinitely. Diagnose the deadlock.
244. [Advanced] Debug: The tokenizer truncates inputs at 512 tokens but important information is at the end. Fix the approach.
245. [Advanced] Debug: Two seemingly identical models produce different outputs due to floating-point non-determinism. How to ensure reproducibility?
246. [Intermediate] Debug: A classification model outputs all zeros. The sigmoid outputs are all < 0.5. Diagnose threshold and class imbalance issues.
247. [Advanced] Debug: The contrastive learning loss produces NaN. Find the numerical stability issue in cosine similarity computation.
248. [Expert] Debug: A custom CUDA kernel for attention produces wrong gradients. How would you verify and debug?
249. [Advanced] Debug: Memory usage grows linearly with each training step, indicating a memory leak. Find common PyTorch memory leak patterns.
250. [Advanced] Debug: Model training is extremely slow despite using a GPU. Profile and identify the CPU-GPU data transfer bottleneck.
251. [Intermediate] Debug: The feature engineering pipeline uses future data when creating lag features. Find the temporal leakage.
252. [Advanced] Debug: An ensemble model's cross-validation score is much higher than the actual test score. What's the meta-leakage issue?
253. [Advanced] Debug: The BLEU score is 0.0 for a seemingly working translation model. Find the tokenization mismatch.

### A.15 Data Pipeline & Infrastructure Coding

254. [Intermediate] Implement a custom PyTorch Dataset and DataLoader for a CSV file with on-the-fly preprocessing.
255. [Advanced] Implement a streaming dataset that reads data lazily from disk (for datasets that don't fit in memory).
256. [Advanced] Implement a data pipeline with parallel preprocessing using Python multiprocessing.
257. [Advanced] Implement a custom collate function for variable-length sequences with padding.
258. [Expert] Implement a distributed data sampler for multi-GPU training.
259. [Intermediate] Implement a simple feature store that caches computed features to disk.
260. [Advanced] Implement a data validation pipeline that checks for schema violations, missing values, and distribution drift.
261. [Advanced] Implement an efficient data loading pipeline with prefetching and caching.
262. [Intermediate] Implement a balanced batch sampler that ensures equal class representation in each batch.
263. [Advanced] Implement a curriculum learning data sampler that presents examples in order of difficulty.
264. [Expert] Implement a simple model serving API using Flask/FastAPI with batched inference.
265. [Advanced] Implement A/B testing framework for model comparison with statistical significance testing.
266. [Intermediate] Write code to convert between common ML data formats: CSV, Parquet, TFRecord, HDF5.
267. [Advanced] Implement a simple experiment tracking system that logs hyperparameters, metrics, and artifacts.

---

## B. ML System Design (200+ Questions)

### B.1 Recommendation Systems

268. [Advanced] Design a recommendation system for a streaming platform (Netflix-scale). Cover: candidate generation, ranking, re-ranking, and real-time personalization.
269. [Advanced] Sub-question: What features would you use for the candidate generation stage? How do you handle the cold-start problem for new users?
270. [Advanced] Sub-question: How do you design the ranking model? What loss function and architecture would you use?
271. [Advanced] Sub-question: How do you handle the explore-exploit tradeoff in recommendations?
272. [Advanced] Sub-question: Design the data pipeline for collecting implicit feedback (watches, clicks, skips) at scale.
273. [Advanced] Sub-question: How would you evaluate the recommendation system? What online and offline metrics would you use?
274. [Advanced] Sub-question: How do you handle position bias in the training data?
275. [Expert] Sub-question: How would you serve recommendations with <100ms latency for 200M users? Describe the architecture.
276. [Advanced] Design a product recommendation system for an e-commerce platform (Amazon-scale). Cover the full stack from data to serving.
277. [Advanced] Sub-question: How would you handle the item cold-start problem when new products are added daily?
278. [Advanced] Sub-question: How do you incorporate real-time signals (what the user just viewed) into recommendations?
279. [Expert] Sub-question: Design the feature store for this recommendation system. What features are precomputed vs computed in real-time?
280. [Advanced] Design a music recommendation system (Spotify-scale). How does audio content similarity factor in?
281. [Advanced] Design a "People You May Know" system for a social network (LinkedIn/Facebook-scale).
282. [Advanced] Sub-question: How do you balance relevance, diversity, and freshness in the friend recommendation list?
283. [Expert] Design a multi-objective recommendation system that balances engagement, revenue, and user satisfaction simultaneously.
284. [Advanced] Design a notification recommendation system. When and what notifications should be sent to maximize engagement without annoying users?
285. [Expert] Design a conversational recommendation system powered by an LLM. How does it differ from traditional approaches?

### B.2 Search & Ranking Systems

286. [Advanced] Design a search ranking system for a large e-commerce platform. Cover retrieval, ranking, and re-ranking stages.
287. [Advanced] Sub-question: How do you design the retrieval stage? Compare inverted index, embedding-based retrieval, and hybrid approaches.
288. [Advanced] Sub-question: What features would you use in the ranking model? How do you handle query-document relevance?
289. [Advanced] Sub-question: How do you collect training data for the ranking model? Discuss click models and position bias.
290. [Expert] Sub-question: How would you implement learning-to-rank? Compare pointwise, pairwise, and listwise approaches.
291. [Advanced] Sub-question: How do you evaluate search quality? Discuss NDCG, MRR, and online metrics.
292. [Advanced] Design a web search engine ranking system (Google-scale). What signals beyond text relevance matter?
293. [Expert] Sub-question: How would you incorporate LLMs into the search stack? Where in the pipeline and at what cost?
294. [Advanced] Design a job search ranking system (LinkedIn/Indeed-scale). How do you match candidates to jobs?
295. [Advanced] Design a semantic search system using dense retrieval. Cover embedding model training, indexing, and serving.
296. [Expert] Sub-question: How do you scale approximate nearest neighbor search to billions of documents? Compare FAISS, ScaNN, and HNSW.
297. [Advanced] Design a query understanding system that handles typos, synonyms, and query expansion.
298. [Advanced] Design a search autocomplete/suggestion system. How do you rank suggestions?
299. [Expert] Design a multi-modal search system that can search across text, images, and video.
300. [Advanced] Sub-question: How would you detect and handle adversarial SEO/manipulation in your ranking system?

### B.3 Fraud Detection & Anomaly Detection

301. [Expert] Design a real-time fraud detection system processing 10K transactions/second for a payment platform.
302. [Expert] Sub-question: How do you handle extreme class imbalance (99.9% legitimate, 0.1% fraud)?
303. [Expert] Sub-question: What features would you engineer? Discuss velocity features, aggregation features, and graph features.
304. [Advanced] Sub-question: How do you design the model to handle concept drift as fraud patterns evolve?
305. [Expert] Sub-question: Design the real-time scoring infrastructure. How do you achieve <50ms latency?
306. [Advanced] Sub-question: How do you handle the cold-start problem for new users/merchants?
307. [Expert] Sub-question: Design the feedback loop: how do confirmed fraud cases get incorporated into model retraining?
308. [Advanced] Sub-question: How do you set the decision threshold? Discuss the cost of false positives vs false negatives.
309. [Advanced] Design an anomaly detection system for monitoring cloud infrastructure metrics.
310. [Advanced] Sub-question: How do you handle seasonality and trends in the baseline metrics?
311. [Expert] Design a money laundering detection system using graph neural networks on transaction networks.
312. [Advanced] Design an account takeover detection system. What behavioral signals indicate a compromised account?
313. [Advanced] Design a bot detection system for a social media platform. How do you distinguish bots from humans?
314. [Expert] Design an insider threat detection system for a financial institution. What data sources and models would you use?
315. [Advanced] Design a credit risk scoring system. How do you ensure fairness and regulatory compliance?

### B.4 Content Understanding & Moderation

316. [Advanced] Design a content moderation system for a social media platform (Facebook/YouTube-scale) that handles text, images, and video.
317. [Advanced] Sub-question: How do you handle borderline content that requires nuanced judgment?
318. [Expert] Sub-question: How do you design the multi-modal model architecture? How are text and image features fused?
319. [Advanced] Sub-question: How do you handle adversarial content designed to evade detection?
320. [Advanced] Sub-question: How do you scale the system to process millions of posts per minute?
321. [Advanced] Design a hate speech detection system. How do you handle context, sarcasm, and cultural differences?
322. [Advanced] Design a spam detection system for email (Gmail-scale). Cover both content and behavioral signals.
323. [Advanced] Design a fake news / misinformation detection system. What signals beyond content would you use?
324. [Expert] Design a toxicity detection system that works across 100+ languages. How do you handle low-resource languages?
325. [Advanced] Design an NSFW content detection system. Cover classification confidence thresholds and appeal workflows.

### B.5 NLP & Language Systems

326. [Advanced] Design an autocomplete system for a code editor (GitHub Copilot-style). Cover data, model, and serving.
327. [Expert] Sub-question: How do you handle code context (file, project, language) in the model?
328. [Expert] Sub-question: How do you serve completions with <200ms latency? Discuss caching, speculative decoding, and model distillation.
329. [Advanced] Design a machine translation system (Google Translate-scale). Cover model architecture, data, and quality.
330. [Advanced] Sub-question: How do you handle low-resource language pairs with limited parallel data?
331. [Advanced] Design a chatbot for customer service. Cover intent detection, entity extraction, dialog management, and response generation.
332. [Expert] Design an LLM-powered RAG system for enterprise document search. Cover chunking, embedding, retrieval, and generation.
333. [Expert] Sub-question: How do you handle document updates? How do you keep the index fresh?
334. [Expert] Sub-question: How do you evaluate the RAG system? What metrics capture retrieval quality vs generation quality?
335. [Expert] Sub-question: How do you handle hallucination in the generated answers? What guardrails do you implement?
336. [Advanced] Design a sentiment analysis system for product reviews at scale. Cover aspect-level sentiment.
337. [Advanced] Design a document summarization system for legal/financial documents.
338. [Expert] Design a real-time speech-to-text system with speaker diarization.
339. [Advanced] Design an entity resolution system that deduplicates records across multiple data sources.
340. [Expert] Design a knowledge graph construction pipeline from unstructured text.

### B.6 Ads & Monetization

341. [Advanced] Design a click-through rate (CTR) prediction system for a digital ads platform. Cover features, model, and serving.
342. [Advanced] Sub-question: How do you handle feature interactions? Compare manual feature crosses vs deep learning approaches.
343. [Expert] Sub-question: How do you serve predictions at 1M QPS with <10ms latency?
344. [Advanced] Sub-question: How do you handle data freshness? How quickly should new click data be incorporated?
345. [Advanced] Design a bid optimization system for an ads platform. How do you maximize advertiser ROI?
346. [Expert] Design a conversion attribution model. How do you attribute conversions across multiple touchpoints?
347. [Advanced] Design a dynamic pricing system for a ride-sharing platform (Uber-style surge pricing).
348. [Advanced] Design a budget pacing system that evenly distributes ad spend across the day.
349. [Expert] Design a multi-objective optimization system that balances ad revenue, user experience, and advertiser satisfaction.
350. [Advanced] Design an ad relevance model that measures how well an ad matches a user query/context.

### B.7 Computer Vision Systems

351. [Advanced] Design an autonomous driving perception system. Cover object detection, lane detection, and depth estimation.
352. [Expert] Sub-question: How do you fuse data from cameras, LiDAR, and radar? Discuss early vs late fusion.
353. [Advanced] Sub-question: How do you handle edge cases (construction zones, unusual objects)?
354. [Advanced] Design a visual search system (Google Lens / Pinterest Lens style).
355. [Advanced] Sub-question: How do you build and serve the visual embedding index for billions of images?
356. [Expert] Design a real-time video understanding system for content recommendation.
357. [Advanced] Design a face verification system for a mobile device (Face ID style). Cover accuracy, fairness, and security.
358. [Advanced] Design a document OCR + understanding pipeline for automated data extraction (invoices, receipts).
359. [Expert] Design a medical image analysis system (X-ray/CT diagnosis). Cover model architecture, regulatory requirements, and uncertainty estimation.
360. [Advanced] Design an image generation system (DALL-E / Midjourney style). Cover architecture, training data, safety, and serving.

### B.8 ML Infrastructure & Platform

361. [Expert] Design a feature store for a large ML platform. Cover offline and online feature serving, feature versioning, and consistency.
362. [Expert] Sub-question: How do you handle point-in-time correctness to prevent data leakage?
363. [Expert] Sub-question: How do you support both batch and real-time feature computation?
364. [Expert] Design a model serving platform that can serve thousands of models simultaneously with auto-scaling.
365. [Expert] Sub-question: How do you handle model versioning, canary deployments, and rollbacks?
366. [Expert] Sub-question: How do you optimize for latency vs throughput? Discuss batching, model optimization, and hardware selection.
367. [Expert] Design an ML experiment tracking and management platform (MLflow/W&B-style).
368. [Advanced] Design an automated model retraining pipeline with drift detection triggers.
369. [Expert] Design a data labeling platform with active learning to minimize annotation costs.
370. [Expert] Design a distributed training infrastructure that supports both data parallelism and model parallelism.
371. [Advanced] Design an A/B testing platform for ML models with proper statistical rigor.
372. [Expert] Design a model monitoring system that detects data drift, prediction drift, and model degradation in real-time.
373. [Expert] Sub-question: How do you distinguish between data drift, concept drift, and model staleness?
374. [Expert] Sub-question: What statistical tests do you use for drift detection? Compare PSI, KS-test, and MMD.
375. [Expert] Sub-question: How do you set up alerts without excessive false alarms?
376. [Advanced] Design a CI/CD pipeline for ML models (MLOps). What tests should run before deployment?

### B.9 Time Series & Forecasting Systems

377. [Advanced] Design a demand forecasting system for an e-commerce platform (predicting next 7/30 days of sales).
378. [Advanced] Sub-question: How do you handle hierarchical forecasting (product → category → total)?
379. [Advanced] Sub-question: How do you incorporate external signals (holidays, promotions, weather)?
380. [Expert] Design a real-time anomaly detection system for financial time series data.
381. [Advanced] Design a capacity planning system that predicts infrastructure needs 3-6 months ahead.
382. [Advanced] Design an ETA prediction system for a delivery/ride-sharing platform.
383. [Expert] Sub-question: How do you handle real-time traffic conditions and dynamic routing in your predictions?
384. [Advanced] Design a predictive maintenance system for manufacturing equipment.
385. [Advanced] Design a stock portfolio optimization system using ML-based return predictions and risk models.

### B.10 Graph & Social Systems

386. [Advanced] Design a social network feed ranking system (Facebook/Twitter/LinkedIn-scale).
387. [Advanced] Sub-question: How do you balance engagement, content quality, and diversity?
388. [Advanced] Sub-question: How do you handle viral content and prevent filter bubbles?
389. [Expert] Design a graph-based fraud detection system for a financial network.
390. [Advanced] Design a drug-drug interaction prediction system using graph neural networks.
391. [Advanced] Design a knowledge graph embedding system for question answering.
392. [Expert] Design a real-time community detection system for a social network.
393. [Advanced] Design a link prediction system for a professional network.
394. [Expert] Design a supply chain optimization system using graph-based models.
395. [Advanced] Design an influence maximization system for viral marketing campaigns.

### B.11 Multi-Modal & Generative Systems

396. [Expert] Design a text-to-image generation system (Stable Diffusion / DALL-E scale). Cover architecture, training, safety, and serving.
397. [Expert] Sub-question: How do you implement safety filters and prevent generation of harmful content?
398. [Expert] Sub-question: How do you serve the model with acceptable latency? Discuss diffusion step optimization.
399. [Expert] Design a video generation system. How does it extend from image generation?
400. [Advanced] Design a multi-modal embedding system that aligns text, image, and audio in a shared space (CLIP-style).
401. [Expert] Design an AI agent system that can use tools (web search, calculator, code interpreter) to answer questions.
402. [Advanced] Design a voice cloning / text-to-speech system with safety considerations.
403. [Expert] Design a document understanding system that handles PDFs with text, tables, and figures.
404. [Advanced] Design a music generation system. What are the unique challenges vs text generation?
405. [Expert] Design an LLM-based code generation system with test-driven validation.

### B.12 Healthcare & Specialized Domains

406. [Expert] Design a clinical decision support system that recommends treatments based on patient records.
407. [Expert] Sub-question: How do you handle regulatory requirements (HIPAA, FDA) and model explainability?
408. [Advanced] Design a drug discovery pipeline using ML for molecular property prediction.
409. [Expert] Design a medical image screening system (e.g., mammography, diabetic retinopathy) with uncertainty estimation.
410. [Advanced] Design a patient risk stratification system for hospital readmission prediction.
411. [Advanced] Design a clinical trial matching system using NLP on medical records.
412. [Expert] Design a protein structure prediction pipeline (AlphaFold-inspired). Cover data, architecture, and evaluation.
413. [Advanced] Design a genomics variant calling pipeline using deep learning.
414. [Advanced] Design a wearable health monitoring system with on-device ML for anomaly detection.
415. [Expert] Design a federated learning system for training models across hospitals without sharing patient data.

### B.13 Edge & Embedded ML Systems

416. [Advanced] Design an on-device ML system for a smartphone keyboard (next-word prediction, autocorrect).
417. [Advanced] Sub-question: How do you fit the model in <50MB with acceptable quality?
418. [Expert] Design a real-time object detection system for an edge device (security camera, drone).
419. [Advanced] Design a wake word detection system ("Hey Siri" / "OK Google" style) for an embedded device.
420. [Expert] Design a federated learning system for improving on-device models while preserving user privacy.
421. [Advanced] Design a model compression pipeline: pruning, quantization, and knowledge distillation.
422. [Expert] Sub-question: Compare INT8, INT4, and binary quantization. When is each appropriate?
423. [Advanced] Design a smart home system that learns user preferences for lighting, temperature, and routines.
424. [Expert] Design an ML system for real-time translation on a mobile device with offline capability.
425. [Advanced] Design an anomaly detection system for IoT sensor networks with limited compute.

### B.14 Safety, Fairness & Ethics Systems

426. [Advanced] Design a bias detection and mitigation system for a hiring/lending ML model.
427. [Expert] Sub-question: How do you define and measure fairness? Compare demographic parity, equalized odds, and individual fairness.
428. [Advanced] Design a model explainability system that provides human-understandable explanations for any ML model's predictions.
429. [Expert] Design a differential privacy system for training ML models on sensitive data.
430. [Advanced] Design a system for detecting and mitigating adversarial attacks on deployed ML models.
431. [Expert] Design a red-teaming framework for evaluating LLM safety. What attack vectors do you test?
432. [Advanced] Design a consent and data governance system for an ML platform.
433. [Expert] Design a system for model unlearning (removing the influence of specific training data).

---

## C. Case Studies & Scenario Questions (200+ Questions)

### C.1 Model Performance Issues

434. [Intermediate] Your model achieves 99% accuracy but stakeholders say it doesn't work. What could be happening? (Hint: class imbalance, wrong metric, data leakage)
435. [Intermediate] Your classification model has high accuracy but low precision for the minority class. How do you improve it?
436. [Advanced] Training loss decreases steadily but validation loss plateaus and then increases. Diagnose systematically and propose at least 5 interventions.
437. [Advanced] Your model performs well on the test set but poorly in production. List all possible causes and how to diagnose each.
438. [Intermediate] Your regression model has low RMSE but users complain predictions are always "average." What's happening?
439. [Advanced] Your NLP model works great on English but poorly on Spanish despite similar training data sizes. Diagnose.
440. [Expert] Your recommendation model has high offline NDCG but A/B tests show no engagement improvement. Analyze why.
441. [Advanced] Two team members train the same model architecture on the same data but get different results. What could cause this?
442. [Intermediate] Your model's performance varies wildly across different K-fold splits. What does this indicate and how do you address it?
443. [Advanced] You added a new feature that improves validation metrics but degrades production performance. Explain possible causes.
444. [Advanced] Your model performs well on aggregate metrics but terribly for a specific user segment. How do you discover and fix this?
445. [Expert] Your LLM fine-tune achieves lower perplexity than the base model but generates worse responses according to human evaluators. Explain.
446. [Intermediate] Your binary classifier always predicts the positive class. What is likely wrong?
447. [Advanced] Your model's calibration is poor — predicted probabilities don't match actual frequencies. How do you diagnose and fix?
448. [Expert] Your multi-task model shows negative transfer on one task while improving others. How do you handle this?
449. [Advanced] Your ensemble outperforms individual models on validation but not on the test set. What happened?
450. [Intermediate] Your image classifier works on curated datasets but fails on real-world photos. Identify the domain gap issues.
451. [Advanced] Your model regresses on performance after adding more training data. How is this possible and what do you investigate?
452. [Expert] Your reinforcement learning agent achieves high reward in simulation but fails in the real world (sim-to-real gap). Diagnose.
453. [Advanced] Your time series model accurately predicts the next day but terribly predicts next week. What's happening?

### C.2 Training & Optimization Issues

454. [Advanced] Training loss goes to NaN after epoch 3. Walk through your systematic debugging process.
455. [Advanced] Your model trains extremely slowly on GPU. Profile and identify at least 5 potential bottlenecks.
456. [Expert] Training loss oscillates wildly instead of decreasing smoothly. Diagnose and fix.
457. [Advanced] Your model converges to a bad local minimum. What strategies can escape it?
458. [Intermediate] Your model overfits after 5 epochs. List all regularization techniques you would try and in what order.
459. [Advanced] Gradient norms explode during training of a deep network. How do you diagnose and resolve?
460. [Advanced] Your transformer model takes 2 weeks to train. The deadline is in 3 days. What do you do?
461. [Expert] You notice that the gradients for the first few layers are extremely small (vanishing gradients). How do you address this in 2024?
462. [Advanced] Your GAN training is unstable — the generator produces mode collapse. Diagnose and propose solutions.
463. [Expert] Your distributed training job doesn't scale linearly with the number of GPUs. What could cause the slowdown?
464. [Advanced] Your contrastive learning model suddenly collapses (all embeddings become identical). Diagnose.
465. [Advanced] You're fine-tuning a pretrained model and it catastrophically forgets its pretraining. How do you prevent this?
466. [Expert] Your RLHF training causes reward hacking — the model finds exploits in the reward model. How to detect and fix?
467. [Advanced] Your model's loss plateaus at a value much higher than expected. What systematic steps do you take?
468. [Intermediate] You have limited compute budget. Should you train a small model for many epochs or a large model for few epochs? Discuss the Chinchilla scaling laws.
469. [Advanced] Your model trains fine on a single GPU but produces garbage results on multi-GPU. Diagnose the distributed training bug.
470. [Expert] Training loss decreases but the model generates repetitive/degenerate text. Explain the phenomenon and solutions.

### C.3 Data Issues & Data Engineering

471. [Intermediate] You discover that 30% of your labels are noisy/incorrect. What approaches can you use to still train a good model?
472. [Advanced] You have 100M training examples but only 1000 labels. Design a complete approach using semi-supervised and self-supervised learning.
473. [Advanced] Your training data is heavily imbalanced (99:1 ratio). Compare at least 6 approaches to handle this.
474. [Intermediate] Your features have very different scales (age: 0-100, income: 0-1M). How does this affect different ML algorithms?
475. [Advanced] You discover data leakage in your pipeline after deploying. How do you identify the source and fix it?
476. [Advanced] Your model is biased against a protected group. Trace the bias back to the data and propose mitigation strategies.
477. [Expert] You need to train an NLP model for a language with almost no labeled data. Design a complete strategy.
478. [Advanced] Your production data distribution has shifted significantly from training data. How do you detect and adapt?
479. [Intermediate] You have 1000 labeled images for a 100-class classification problem. What approaches maximize performance with limited data?
480. [Advanced] Your dataset has significant selection bias. How do you detect it and what can you do about it?
481. [Advanced] You're building a model on user behavioral data that has survivorship bias (you only see data from users who stayed). How do you handle this?
482. [Expert] Your training data was collected under a different policy than deployment (distribution shift due to policy change). How do you adjust?
483. [Intermediate] Your features have many missing values (some columns are 40% missing). Compare imputation strategies.
484. [Advanced] You need to merge training data from 5 different sources with different schemas and quality levels. Design the pipeline.
485. [Expert] Design a data flywheel system where model predictions are used to improve future training data.
486. [Advanced] Your text data contains PII that must be removed before training. Design the de-identification pipeline.
487. [Advanced] You have a dataset with label inconsistency — different annotators disagree on 20% of labels. How to handle?
488. [Expert] You're training on web-scraped data that may contain copyrighted or toxic content. Design the data curation pipeline.

### C.4 Deployment & Production Issues

489. [Expert] Your model inference latency is 500ms but the SLA requires <50ms. Walk through all optimization approaches: model compression, hardware, architecture changes, caching.
490. [Advanced] Your model works in staging but fails silently in production (no errors, just bad predictions). Design monitoring to catch this.
491. [Advanced] A model update improves average metrics but degrades experience for 5% of users. How do you handle the deployment decision?
492. [Expert] Your serving infrastructure can't handle traffic spikes (10x normal load during events). Design the scaling strategy.
493. [Advanced] You need to deploy your model to 50 countries with different data regulations (GDPR, CCPA, etc.). How do you design the system?
494. [Advanced] Your model becomes stale and its performance degrades over time. Design an automated retraining and deployment pipeline.
495. [Expert] You're deploying an LLM-based feature and need to estimate the inference cost. Walk through token economics and cost optimization.
496. [Advanced] Your A/B test shows the new model is statistically significantly better, but it took 2 weeks. The CEO wants faster iteration. What do you propose?
497. [Advanced] A customer reports that the model gave a harmful/offensive output. Design the incident response process.
498. [Expert] Your model serves 1B requests/day and 0.1% are adversarial. Design the adversarial input detection system.
499. [Advanced] You need to roll back a model deployment, but the new model already processed user data that affected downstream systems. How do you handle this?
500. [Advanced] Your model's output changes meaning depending on the user's locale/language. Design the internationalization approach.
501. [Expert] You need to serve a 70B parameter LLM with <100ms first-token latency. Walk through model parallelism, quantization, and KV-cache optimization strategies.
502. [Advanced] Your team deploys 10 models per week but has no confidence in production quality. Design the ML testing strategy.
503. [Advanced] The monitoring dashboard shows a sudden 5% drop in model accuracy. Is it data drift, model degradation, or a bug? Design the triage process.

### C.5 Business & Stakeholder Scenarios

504. [Intermediate] The PM asks you to build a model to predict which customers will churn. What questions do you ask before starting?
505. [Intermediate] A stakeholder insists on using deep learning for a tabular dataset with 1000 samples. How do you push back constructively?
506. [Advanced] The CEO wants to deploy an LLM chatbot for customer service within 2 weeks. What risks do you flag and what's your realistic timeline proposal?
507. [Advanced] Your model flags a transaction as fraud but the customer is a VIP. The business wants to override the model. How do you handle this?
508. [Intermediate] The marketing team asks "what's the accuracy?" of your model. Why might this be the wrong question and what would you present instead?
509. [Advanced] Your model has 95% accuracy but the 5% errors cause significant financial losses. How do you communicate risk and propose mitigations?
510. [Advanced] Two teams have competing approaches to the same problem. How do you design a fair evaluation framework to decide between them?
511. [Expert] The legal team asks whether your model can be explained to regulators. What's your strategy for model explainability and compliance?
512. [Advanced] Your model is ready but the data engineering team says the real-time features won't be ready for 3 months. What do you do?
513. [Intermediate] A non-technical VP asks why the model "got it wrong" on a specific example. How do you explain it?
514. [Advanced] You're asked to estimate the ROI of an ML project before building it. What framework do you use?
515. [Expert] The company wants to build an "AI strategy." You're asked to identify the top 3 highest-impact ML use cases. What's your process?
516. [Advanced] Your competitor launched a similar ML feature. The CEO wants yours deployed ASAP. How do you balance speed with quality?
517. [Advanced] The model is deployed but business metrics don't improve despite strong ML metrics. Diagnose the gap between ML metrics and business value.
518. [Intermediate] A data analyst asks whether correlation in the data means they should build a predictive model. What do you explain?

### C.6 Scaling & Architecture Decisions

519. [Advanced] Your current model training takes 3 days on a single GPU. The team wants to scale to multi-GPU. Walk through the considerations.
520. [Expert] You need to train a foundation model on 1T tokens. Design the training infrastructure: hardware, parallelism, fault tolerance.
521. [Advanced] Your feature pipeline processes 100GB of data daily. It now needs to handle 10TB. Design the scaling strategy.
522. [Expert] You're designing a model that needs to serve both latency-sensitive (real-time) and throughput-sensitive (batch) use cases. How?
523. [Advanced] Your team has 100 models in production. How do you manage model lifecycle, versioning, and deprecation?
524. [Expert] You need to choose between building ML infrastructure in-house vs using managed services (SageMaker, Vertex AI). What factors drive this decision?
525. [Advanced] Your ML pipeline is a tangled Jupyter notebook. How do you refactor it into a production-grade system?
526. [Expert] Design the architecture for a multi-tenant ML platform serving 50 different teams with different model types and SLAs.
527. [Advanced] You need to reduce your ML infrastructure costs by 50%. What approaches do you consider?
528. [Expert] Your training data lake is growing 1TB/day. Design the data management and governance architecture.

### C.7 Model Selection & Architecture Decisions

529. [Intermediate] When would you choose a simple logistic regression over a deep learning model? Give 5 concrete scenarios.
530. [Intermediate] You have a tabular dataset with 50 features and 100K rows. Compare gradient boosting vs neural networks. Which do you try first and why?
531. [Advanced] You need to build an NLP classifier. Compare fine-tuning BERT, using an LLM with few-shot prompting, and training a simple TF-IDF + logistic regression. When is each appropriate?
532. [Advanced] You're designing a retrieval system. Compare BM25, dense retrieval, and hybrid approaches. What factors determine the choice?
533. [Expert] You need to choose between a monolithic multi-task model and separate specialized models. Discuss the tradeoffs.
534. [Advanced] Your classification problem has 10K classes. What architectural choices handle this extreme multi-class setting?
535. [Advanced] You have a problem that could be framed as classification or regression. How do you decide?
536. [Expert] Compare using a pre-trained foundation model vs training from scratch for your specific domain. When is each better?
537. [Advanced] You need a model that provides uncertainty estimates for safety-critical decisions. Compare approaches.
538. [Intermediate] Your dataset has both tabular and text features. How do you build a model that uses both?

### C.8 Ethics, Fairness & Safety Scenarios

539. [Advanced] Your hiring model rejects significantly more candidates from a minority group. How do you investigate and address this?
540. [Expert] An LLM chatbot deployed for customer service generates a response that could be interpreted as medical advice. Design the guardrails.
541. [Advanced] Your facial recognition system has significantly different error rates across ethnicities. How do you measure and mitigate this?
542. [Expert] A government agency wants to use your predictive model for pre-crime risk assessment. What ethical concerns do you raise?
543. [Advanced] Your recommendation system creates a filter bubble that radicalizes users over time. How do you detect and prevent this?
544. [Advanced] Users discover they can manipulate your model's outputs through adversarial inputs. Design the defense strategy.
545. [Expert] Your training data contains biases from historical discrimination. How do you build a model that doesn't perpetuate these biases?
546. [Advanced] Your model makes a decision that significantly harms a user (denied loan, rejected application). Design the appeal and explanation process.
547. [Expert] You're asked to build a deepfake detection system. What are the arms-race dynamics and how do you stay ahead?
548. [Advanced] Your model's explanations (SHAP values) reveal that it's using a proxy for a protected attribute. How do you handle this?
549. [Advanced] An audit reveals your model violates GDPR's "right to explanation." How do you make it compliant?
550. [Expert] Your company wants to use customer data for a new ML use case not covered by the original consent. What do you advise?

### C.9 Team & Process Scenarios

551. [Intermediate] You're the first ML engineer at a startup. How do you set up the ML infrastructure and practices from scratch?
552. [Advanced] Your data scientists hand off Jupyter notebooks to production. The models keep breaking. How do you fix the process?
553. [Advanced] Your team of 5 ML engineers is struggling with experiment tracking — everyone has their own approach. Design the standardized workflow.
554. [Advanced] You need to decide between using a pre-built ML platform (SageMaker, Vertex) or building custom. How do you evaluate?
555. [Intermediate] A new team member wants to use the latest paper's approach. How do you evaluate whether to adopt it vs stick with proven methods?
556. [Advanced] Your team maintains 50 models but only has 5 engineers. How do you prioritize maintenance vs new development?
557. [Expert] You're tasked with building an ML Center of Excellence for a non-tech company. What's your strategy?
558. [Advanced] Two data scientists had differing experiment results because they used different data snapshots. How do you prevent this?
559. [Intermediate] How do you write an ML design doc? What sections should it include?
560. [Advanced] Your company is switching from batch ML to real-time ML. What organizational and technical changes are needed?

### C.10 Debugging Specific Model Types

561. [Advanced] Your BERT fine-tuned model overfits after 1 epoch. What's happening and how do you fix it?
562. [Advanced] Your GAN generates blurry images despite training for days. Diagnose the issue.
563. [Expert] Your diffusion model generates high-quality images but ignores the text prompt. What's wrong with your classifier-free guidance implementation?
564. [Advanced] Your object detection model has high recall but low precision — lots of false positive detections. Diagnose.
565. [Expert] Your LLM generates factually incorrect information confidently. How do you reduce hallucination?
566. [Advanced] Your speech recognition model works well in quiet environments but fails in noisy ones. Design the fix.
567. [Expert] Your reinforcement learning agent learns to exploit a bug in the reward function instead of solving the actual task (reward hacking). How do you detect and fix?
568. [Advanced] Your transfer learning model performs worse than training from scratch. When does transfer learning fail?
569. [Advanced] Your image segmentation model produces noisy/jagged boundaries. How do you improve it?
570. [Expert] Your multi-modal model (text + image) ignores one modality and relies only on the other. Diagnose modality laziness.

### C.11 Real-World Production Scenarios

571. [Advanced] You receive an alert that model accuracy dropped 10% overnight. Walk through your incident response procedure step by step.
572. [Expert] Your company is migrating from TensorFlow to PyTorch. 30 models need migration. Design the plan.
573. [Advanced] A model you deployed 6 months ago has never been retrained. Performance has degraded gradually. Design the monitoring that would have caught this earlier.
574. [Expert] You need to run an A/B test but the treatment group is too small for statistical significance. What alternatives do you consider?
575. [Advanced] Your model serves different predictions for the same input at different times (non-determinism in serving). Diagnose.
576. [Advanced] A model update causes a 2% drop in one metric but 5% improvement in another. How do you make the deployment decision?
577. [Expert] Your model training pipeline is bottlenecked by data preprocessing. The GPU utilization is only 30%. How do you optimize?
578. [Advanced] You discover that your model has memorized some training examples and can regurgitate them verbatim. What are the privacy and copyright implications?
579. [Expert] Your ML system has a cascading failure — one model's outputs feed into another's inputs. How do you design resilience?
580. [Advanced] Your model needs to handle a sudden distribution shift (e.g., COVID-19 changes user behavior). How do you quickly adapt?
581. [Advanced] The on-call ML engineer is paged at 3 AM for a model failure. Design the runbook.
582. [Expert] Your model training costs $50K per run. How do you minimize wasted compute through better experiment design?
583. [Advanced] A customer data deletion request arrives. How do you handle the "right to be forgotten" for your trained models?
584. [Expert] Your serving infrastructure needs 99.99% uptime. Design the redundancy and failover strategy for ML serving.

### C.12 LLM-Specific Scenarios

585. [Advanced] You're evaluating whether to use GPT-4, an open-source LLM (LLaMA), or a fine-tuned smaller model for your use case. What factors drive this decision?
586. [Expert] Your RAG system retrieves relevant documents but the LLM still hallucinates. How do you debug the full pipeline?
587. [Advanced] Your LLM-based chatbot sometimes generates toxic or biased responses. Design the safety layer.
588. [Expert] You need to fine-tune an LLM on proprietary data but can't afford to fine-tune the full model. Compare LoRA, QLoRA, prefix tuning, and prompt tuning.
589. [Advanced] Your LLM application's inference costs are $100K/month. How do you reduce costs while maintaining quality?
590. [Expert] Design an evaluation framework for an LLM-based application. How do you measure quality without ground-truth labels?
591. [Advanced] Your LLM generates valid JSON 90% of the time but the other 10% causes downstream failures. How do you ensure structured output?
592. [Expert] You need to add new knowledge to your LLM without retraining (knowledge cutoff problem). Compare RAG, tool use, and continual learning.
593. [Advanced] Your prompt engineering improves results but the prompts are fragile — small changes break them. How do you make them robust?
594. [Expert] Your LLM agent calls tools in an infinite loop. Design the safety mechanisms.
595. [Advanced] Compare the total cost of ownership: using an API-based LLM (OpenAI) vs hosting your own open-source LLM.
596. [Expert] Your LLM needs to process documents longer than its context window. Compare chunking strategies, hierarchical summarization, and long-context models.

---

## D. Cutting-Edge & Recent Topics (200+ Questions)

### D.1 State Space Models & Alternatives to Transformers

597. [Advanced] Compare State Space Models (Mamba) with Transformers. What are the computational complexity differences for training and inference?
598. [Advanced] Explain the selective state space mechanism in Mamba. How does it achieve input-dependent dynamics?
599. [Expert] Derive the continuous-time state space model equations and show how they are discretized for sequence modeling.
600. [Advanced] What is the hardware-aware algorithm design in Mamba? How does it optimize for modern GPU memory hierarchies?
601. [Expert] Compare the associative scan algorithm used in Mamba with the parallel scan for RNNs. What are the parallelization trade-offs?
602. [Advanced] When would you prefer Mamba over a Transformer? Give specific use cases (long sequences, streaming, edge devices).
603. [Expert] Explain how Mamba-2 improves upon Mamba-1. What is the connection between SSMs and structured attention?
604. [Advanced] Compare RWKV with Mamba and Transformers. How does RWKV achieve linear complexity?
605. [Expert] Explain the S4 (Structured State Spaces for Sequence Modeling) model. What is the HiPPO initialization and why is it important?
606. [Advanced] Can SSMs handle tasks that require precise retrieval of information from context (like key-value lookup)? What are their limitations?
607. [Expert] How do hybrid architectures (combining SSM layers with attention layers) work? What is the motivation?
608. [Advanced] Compare the memory footprint of Mamba vs Transformer during inference with sequence length 100K.
609. [Expert] Explain the connection between linear attention and state space models. Are they equivalent?
610. [Advanced] What are RetNet and its retention mechanism? How does it compare to standard attention?
611. [Expert] Discuss the theoretical expressiveness limitations of SSMs compared to Transformers. What tasks can Transformers solve that SSMs cannot?

### D.2 LLM Alignment: RLHF, DPO & Beyond

612. [Advanced] Explain the RLHF pipeline end-to-end: reward model training, PPO optimization, and KL divergence constraint.
613. [Expert] Derive the DPO (Direct Preference Optimization) objective mathematically. Show how it eliminates the need for a separate reward model.
614. [Expert] What is the Bradley-Terry model used in DPO? How does it relate preference rankings to reward values?
615. [Advanced] Compare DPO with PPO-based RLHF. What are the practical advantages and disadvantages of each?
616. [Expert] What are the failure modes of DPO? When does it perform worse than RLHF?
617. [Advanced] Explain KTO (Kahneman-Tversky Optimization). How does it differ from DPO by not requiring paired preferences?
618. [Expert] Explain IPO (Identity Preference Optimization) and how it addresses the overfitting issues in DPO.
619. [Advanced] How does Constitutional AI (CAI) work? How does it reduce the need for human preference data?
620. [Expert] Explain ORPO (Odds Ratio Preference Optimization). How does it simplify the preference optimization pipeline?
621. [Advanced] What is the role of the reference model in DPO? What happens if you remove it?
622. [Expert] Derive the reward model implicit in DPO. How do you extract reward scores from a DPO-trained model?
623. [Advanced] Compare online DPO vs offline DPO. What is the impact of on-policy vs off-policy preference data?
624. [Expert] Explain iterative/online DPO (self-play or rejection sampling DPO). How does it improve over single-iteration DPO?
625. [Advanced] What is SPIN (Self-Play Fine-Tuning)? How does it use the model's own generations for alignment?
626. [Expert] Explain reward hacking in RLHF. Give concrete examples and mitigation strategies.
627. [Advanced] How do you evaluate alignment quality? What benchmarks and metrics are used (MT-Bench, AlpacaEval, Chatbot Arena)?
628. [Expert] Explain the Nash Learning from Human Feedback (NLHF) framework. How does game theory improve alignment?
629. [Advanced] What is RLAIF (RL from AI Feedback)? How does it reduce human annotation costs?
630. [Expert] Explain the theoretical connection between DPO and contrastive learning. How are they related?
631. [Advanced] How do you collect high-quality preference data at scale? Discuss inter-annotator agreement and quality control.

### D.3 Efficient Attention & Long Context

632. [Advanced] How does Flash Attention achieve O(N) memory instead of O(N²)? Walk through the tiling algorithm.
633. [Expert] Explain the IO-awareness in Flash Attention. How does it optimize for GPU SRAM vs HBM access patterns?
634. [Expert] What improvements does Flash Attention 2 bring over Flash Attention 1? Discuss parallelism and work partitioning.
635. [Advanced] Explain Ring Attention for distributed long-context training. How does it partition the attention computation across devices?
636. [Expert] Compare Flash Attention, Flash Decoding, and PagedAttention. When is each appropriate?
637. [Advanced] What is PagedAttention (used in vLLM)? How does it optimize KV-cache memory management?
638. [Expert] Explain the sliding window attention in Mistral. How does it maintain quality while limiting attention span?
639. [Advanced] Compare sparse attention patterns: local, strided, global tokens (as in Longformer/BigBird). What are the tradeoffs?
640. [Expert] Explain Multi-Query Attention (MQA) and Grouped Query Attention (GQA). Derive the memory savings.
641. [Advanced] How does context window extension work? Compare position interpolation, NTK-aware scaling, and YaRN.
642. [Expert] Explain the Infini-attention mechanism. How does it handle unbounded context with bounded memory?
643. [Advanced] What is the memory-efficient attention in xFormers? How does it compare to Flash Attention?
644. [Expert] Derive the arithmetic intensity of standard attention vs Flash Attention. Why is attention memory-bound on modern GPUs?
645. [Advanced] How do you handle KV-cache compression for long-context inference? Compare eviction policies and quantization approaches.
646. [Expert] Explain how Mixture of Depths works. How does it skip computation for less important tokens?

### D.4 Parameter-Efficient Fine-Tuning (PEFT)

647. [Advanced] Explain LoRA (Low-Rank Adaptation) mathematically. Why does low-rank decomposition work for fine-tuning?
648. [Expert] Derive the LoRA update rule. What is the effective weight update and how does the rank r affect capacity?
649. [Advanced] Compare LoRA, QLoRA, AdaLoRA, and LoRA+. What does each variant improve?
650. [Expert] Explain QLoRA in detail. How does 4-bit quantization + LoRA achieve full fine-tuning quality?
651. [Advanced] What is the double quantization technique in QLoRA? How does it reduce memory further?
652. [Expert] Explain DoRA (Weight-Decomposed Low-Rank Adaptation). How does it decompose magnitude and direction?
653. [Advanced] Compare prefix tuning, prompt tuning, and P-tuning. How do they differ from LoRA?
654. [Expert] Explain adapter layers for fine-tuning. Compare with LoRA in terms of parameters, latency, and quality.
655. [Advanced] How do you select the rank r in LoRA? What is the empirical guidance from the paper?
656. [Expert] Can you merge LoRA weights back into the base model? What are the implications for serving?
657. [Advanced] How do you apply LoRA to different parts of the transformer (attention matrices, FFN layers)? What's most effective?
658. [Expert] Explain the connection between LoRA and intrinsic dimensionality of the fine-tuning task.
659. [Advanced] How does LoRA affect training dynamics compared to full fine-tuning? Are there convergence differences?
660. [Expert] Explain S-LoRA for serving multiple LoRA adapters efficiently. How does it batch requests with different adapters?
661. [Advanced] Compare the total cost (compute, memory, storage) of full fine-tuning vs LoRA vs QLoRA for a 70B model.
662. [Expert] What is the lottery ticket hypothesis and how does it relate to parameter-efficient fine-tuning?
663. [Advanced] Implement LoRA forward pass pseudocode showing how the low-rank matrices modify the output.

### D.5 Model Compression & Efficient Inference

664. [Advanced] Explain speculative decoding. What is the acceptance criterion and why does it produce exact same distribution?
665. [Expert] Derive the acceptance probability in speculative decoding mathematically. Prove that it preserves the target distribution.
666. [Advanced] What draft models work best for speculative decoding? Compare smaller versions, Medusa heads, and EAGLE.
667. [Expert] Explain Medusa decoding. How does it use multiple heads to predict future tokens in parallel?
668. [Advanced] Compare post-training quantization (PTQ) methods: GPTQ, AWQ, SqueezeLLM, QuIP. What are the tradeoffs?
669. [Expert] Explain the GPTQ quantization algorithm. How does it use the Hessian for optimal weight rounding?
670. [Advanced] What is AWQ (Activation-aware Weight Quantization)? How does it identify salient channels?
671. [Expert] Explain FP8, INT8, INT4, and NF4 (NormalFloat4) quantization formats. When is each appropriate?
672. [Advanced] How does knowledge distillation work for LLMs? Compare white-box and black-box distillation.
673. [Expert] Explain the distillation techniques behind models like Phi, Orca, and LLaMA-distilled variants.
674. [Advanced] What is model pruning? Compare unstructured, structured, and semi-structured (2:4 sparsity) pruning.
675. [Expert] Explain SparseGPT. How does it achieve one-shot pruning of LLMs without retraining?
676. [Advanced] Compare continuous batching (used in vLLM, TGI) with static batching. What are the throughput improvements?
677. [Expert] Explain tensor parallelism vs pipeline parallelism vs expert parallelism for LLM serving.
678. [Advanced] What is the roofline model for inference? How do you determine if your model is compute-bound or memory-bound?
679. [Expert] Explain GGUF/GGML format and llama.cpp inference optimization. How does it enable LLM inference on CPUs?
680. [Advanced] Compare TensorRT-LLM, vLLM, and TGI for production LLM serving. When would you use each?
681. [Expert] What are the trade-offs of using INT4 vs FP8 quantization for a production LLM?

### D.6 Mixture of Experts (MoE)

682. [Advanced] Explain how Mixture of Experts routing works in transformers. What is the gating function?
683. [Expert] What is the load balancing loss in MoE? Derive it and explain why it's necessary.
684. [Advanced] Compare Switch Transformer, GShard, and Mixtral MoE architectures. What are the key differences?
685. [Expert] Explain the expert capacity and buffer overflow handling in MoE. What happens when an expert is overloaded?
686. [Advanced] How does Mixtral 8x7B achieve the quality of a much larger dense model? What is the effective parameter count during inference?
687. [Expert] Explain expert parallelism for serving MoE models. How do you distribute experts across devices?
688. [Advanced] What are the training stability challenges with MoE models? How do you prevent routing collapse?
689. [Expert] Compare top-1 vs top-2 expert routing. What is the impact on quality and compute?
690. [Advanced] How does the auxiliary load balancing loss work? What coefficient is typically used?
691. [Expert] Explain the connection between MoE and ensemble learning. How are they fundamentally different?
692. [Advanced] What are the communication costs of MoE in distributed training? How does all-to-all communication scale?
693. [Expert] Design an MoE system where experts specialize in different domains/languages. How do you encourage specialization?
694. [Advanced] Compare dense scaling vs sparse (MoE) scaling given a fixed compute budget. When does each win?
695. [Expert] Explain Soft MoE and its differentiable routing mechanism. How does it differ from discrete top-k routing?

### D.7 Retrieval-Augmented Generation (RAG)

696. [Advanced] Explain the RAG architecture end-to-end. What are the retriever, reader, and generator components?
697. [Expert] Compare dense retrieval (DPR, Contriever) with sparse retrieval (BM25) and hybrid approaches for RAG.
698. [Advanced] How do you chunk documents for RAG? Compare fixed-size, semantic, and recursive chunking strategies.
699. [Expert] Explain advanced RAG patterns: query rewriting, HyDE (Hypothetical Document Embeddings), and multi-hop retrieval.
700. [Advanced] How do you evaluate a RAG system? What metrics capture retrieval quality, generation quality, and faithfulness?
701. [Expert] Explain the RAGAS evaluation framework. What are its component metrics?
702. [Advanced] How do you handle multi-modal RAG (documents with tables, figures, and text)?
703. [Expert] Explain ColBERT and late interaction retrieval. How does it balance quality and efficiency?
704. [Advanced] What is the lost-in-the-middle problem in RAG? How do you mitigate it?
705. [Expert] Design a production RAG system with real-time index updates, versioning, and fallback strategies.
706. [Advanced] Compare vector databases (Pinecone, Weaviate, Qdrant, Milvus) for RAG. What factors drive the choice?
707. [Expert] Explain RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval). How does hierarchical summarization improve retrieval?
708. [Advanced] How do you prevent RAG hallucination? Compare citation generation, verification chains, and constrained decoding.
709. [Expert] Explain self-RAG. How does the model learn when to retrieve and when to rely on its parametric knowledge?
710. [Advanced] What is the tradeoff between chunk size and retrieval accuracy in RAG? How do you optimize it empirically?
711. [Expert] Design a RAG system that handles conflicting information across retrieved documents.

### D.8 Generative Models: Diffusion & Flow Matching

712. [Advanced] Explain the forward and reverse process in diffusion models (DDPM). What is the noise schedule?
713. [Expert] Derive the ELBO (Evidence Lower Bound) for diffusion models. Show how it decomposes into KL divergence terms.
714. [Advanced] Compare DDPM, DDIM, and DPM-Solver for diffusion sampling. What are the speed-quality tradeoffs?
715. [Expert] Explain flow matching for generative models. How does it differ from score-based diffusion?
716. [Expert] Derive the conditional flow matching objective. Why is it simpler than the score matching objective?
717. [Advanced] Compare flow matching, diffusion models, and GANs for image generation in 2024.
718. [Expert] Explain rectified flows and their connection to optimal transport. How do they enable few-step generation?
719. [Advanced] What is classifier-free guidance (CFG)? How does it control the generation quality-diversity tradeoff?
720. [Expert] Explain the latent diffusion architecture (Stable Diffusion). What is the role of the VAE, U-Net, and text encoder?
721. [Advanced] How does Stable Diffusion XL improve over Stable Diffusion 1.x? What are the architectural changes?
722. [Expert] Explain consistency models. How do they enable single-step generation from diffusion models?
723. [Advanced] What is the v-prediction parameterization in diffusion models? How does it compare to epsilon-prediction?
724. [Expert] Explain DiT (Diffusion Transformers). How do they replace U-Net with a transformer architecture?
725. [Advanced] How does ControlNet work for conditional image generation? What is the zero-convolution trick?
726. [Expert] Explain the IP-Adapter mechanism for image-prompted generation. How does it inject image features into diffusion?
727. [Advanced] Compare text-to-video generation approaches: temporal convolutions, temporal attention, and frame interpolation.
728. [Expert] Explain Stable Video Diffusion. How does it extend image diffusion to video?
729. [Advanced] What is the role of the noise schedule in diffusion models? Compare linear, cosine, and learned schedules.
730. [Expert] Explain the connection between score matching and denoising. Derive Vincent's theorem.

### D.9 LLM Architecture & Training Innovations

731. [Advanced] Compare GPT, LLaMA, Mistral, and Gemma architectures. What are the key architectural differences?
732. [Expert] Explain the SwiGLU activation function. Why do modern LLMs use it instead of ReLU/GELU?
733. [Advanced] What is RMSNorm? Why do modern LLMs prefer it over LayerNorm?
734. [Expert] Explain pre-normalization vs post-normalization in transformers. Why did the community shift to pre-norm?
735. [Advanced] Compare learned positional embeddings, sinusoidal, RoPE, and ALiBi. What are the context length implications?
736. [Expert] Explain the Chinchilla scaling laws. How do you determine optimal model size given a fixed compute budget?
737. [Advanced] What are the training stability techniques for large models? Discuss gradient checkpointing, mixed precision, and loss scaling.
738. [Expert] Explain 3D parallelism (data, tensor, pipeline) for training large models. How do you choose the parallelism configuration?
739. [Advanced] What is DeepSpeed ZeRO? Explain stages 1, 2, and 3 and their memory savings.
740. [Expert] Explain FSDP (Fully Sharded Data Parallel) in PyTorch. How does it compare to DeepSpeed ZeRO?
741. [Advanced] How does gradient checkpointing (activation recomputation) trade compute for memory?
742. [Expert] Explain the training recipe for a modern LLM: pre-training, supervised fine-tuning, and alignment. What data is used at each stage?
743. [Advanced] What is curriculum learning for LLM pre-training? How do you order training data for better quality?
744. [Expert] Explain the data mixture decisions for LLM pre-training. How do you balance code, web text, books, and other sources?
745. [Advanced] What are the differences between causal LMs, prefix LMs, and encoder-decoder models? When to use each?
746. [Expert] Explain the Phi model series' approach: can smaller models match larger ones with better data curation?
747. [Advanced] How does context distillation work for LLMs? What is the process?
748. [Expert] Explain the Mixture of Depths (MoD) concept. How does it allocate compute dynamically across tokens?

### D.10 LLM Agents & Tool Use

749. [Advanced] Explain the ReAct (Reasoning + Acting) framework for LLM agents. How does it interleave reasoning and action?
750. [Expert] Compare tool-use approaches: function calling, code generation, and API integration for LLM agents.
751. [Advanced] What is the planning problem for LLM agents? Compare chain-of-thought, tree-of-thought, and graph-of-thought approaches.
752. [Expert] Design a multi-agent system where specialized LLM agents collaborate to solve complex tasks.
753. [Advanced] How do you evaluate LLM agents? What benchmarks exist (WebArena, SWE-bench, GAIA)?
754. [Expert] Explain the memory mechanisms for LLM agents: short-term (context), working (scratchpad), and long-term (external store).
755. [Advanced] What are the safety risks of LLM agents with tool access? How do you implement sandboxing and permission systems?
756. [Expert] Explain how code interpreters (like in ChatGPT) work. What is the execution and verification loop?
757. [Advanced] How do you ground LLM agents in real-world environments (web browsing, computer use)?
758. [Expert] Compare autonomous coding agents (Devin, SWE-Agent, OpenHands). What architectural patterns do they share?
759. [Advanced] What is the tool-use fine-tuning process? How do you train an LLM to use tools effectively?
760. [Expert] Design an LLM agent system with self-reflection and error recovery capabilities.

### D.11 Multimodal Models

761. [Advanced] Explain the CLIP architecture. How does contrastive pre-training align text and image representations?
762. [Expert] How do vision-language models like LLaVA and GPT-4V process images? Compare the image encoding approaches.
763. [Advanced] What is the visual instruction tuning approach used in LLaVA? How does it create training data?
764. [Expert] Explain the Flamingo architecture for few-shot visual understanding. What is the perceiver resampler?
765. [Advanced] Compare early fusion vs late fusion for multimodal models. What are the compute and quality tradeoffs?
766. [Expert] Explain SigLIP and how it improves over CLIP's contrastive objective.
767. [Advanced] How do text-to-image models (DALL-E 3, Midjourney) handle text rendering? Why is it challenging?
768. [Expert] Explain the architecture of multimodal models like Gemini that natively handle text, image, audio, and video.
769. [Advanced] How do you evaluate multimodal model capabilities? What benchmarks exist?
770. [Expert] Explain the any-to-any generation paradigm (e.g., CoDi, NExT-GPT). How do models generate across modalities?
771. [Advanced] How does audio understanding work in multimodal LLMs (like Whisper, AudioPaLM)?
772. [Expert] Explain the challenges of training multimodal models: data imbalance, modality dominance, and representation alignment.

### D.12 Reinforcement Learning & Decision Making

773. [Advanced] Explain PPO (Proximal Policy Optimization) and why it's used in RLHF. What is the clipping mechanism?
774. [Expert] Compare on-policy (PPO) vs off-policy (DPO) approaches for LLM alignment. When is each preferred?
775. [Advanced] Explain offline RL and its application to LLM training (decision transformers, trajectory optimization).
776. [Expert] What is GRPO (Group Relative Policy Optimization) used in DeepSeek? How does it differ from PPO?
777. [Advanced] Explain the reward model training process. What makes a good reward model?
778. [Expert] How does process reward modeling (PRM) differ from outcome reward modeling (ORM) for reasoning tasks?
779. [Advanced] Explain the challenge of reward hacking and specification gaming in RL-based alignment.
780. [Expert] What is the theoretical foundation of the KL constraint in RLHF? Why is it necessary?
781. [Advanced] How does RLHF scale? What are the computational challenges of training at billion-parameter scale?
782. [Expert] Explain Constitutional AI's approach to self-improvement through self-critique and revision.

### D.13 Reasoning & Chain-of-Thought

783. [Advanced] Explain chain-of-thought (CoT) prompting. Why does it improve reasoning in LLMs?
784. [Expert] Compare zero-shot CoT, few-shot CoT, and self-consistency decoding. When does each work best?
785. [Advanced] What is tree-of-thought (ToT) reasoning? How does it explore multiple reasoning paths?
786. [Expert] Explain the reasoning capabilities of o1/o3-style models. How does test-time compute scaling work?
787. [Advanced] How do you evaluate reasoning quality in LLMs? What benchmarks test mathematical and logical reasoning?
788. [Expert] Explain verification-based approaches to improving reasoning (self-verification, majority voting, process rewards).
789. [Advanced] What is the difference between System 1 and System 2 reasoning in the context of LLMs?
790. [Expert] Explain how models like DeepSeek-R1 achieve strong reasoning through RL without supervised CoT data.
791. [Advanced] How does step-by-step reasoning in training data affect model capabilities? Discuss the "teaching to think" paradigm.
792. [Expert] What are the limitations of chain-of-thought reasoning? When does it fail or mislead?

### D.14 Data-Centric AI & Synthetic Data

793. [Advanced] Explain the data-centric AI paradigm. How does it differ from model-centric approaches?
794. [Expert] How do you generate high-quality synthetic training data using LLMs? What are the quality control mechanisms?
795. [Advanced] What is self-instruct? How do models generate their own instruction-following training data?
796. [Expert] Explain the Textbooks Are All You Need (Phi) approach. How does data quality compensate for quantity?
797. [Advanced] How do you detect and remove low-quality or duplicate data from web-scale datasets?
798. [Expert] Explain data influence functions. How do you identify which training examples most influence a prediction?
799. [Advanced] What is active learning? How do you select the most informative examples for labeling?
800. [Expert] Explain the constitutional approach to synthetic data: generating, filtering, and refining synthetic examples.
801. [Advanced] How does curriculum learning for pre-training work? What ordering of data improves final model quality?
802. [Expert] Design a data flywheel for an LLM application: how do user interactions improve future model quality?

### D.15 Security, Privacy & Robustness

803. [Advanced] Explain prompt injection attacks on LLMs. What are direct and indirect injection?
804. [Expert] Design a defense system against prompt injection. Compare input filtering, output filtering, and instruction hierarchy.
805. [Advanced] What is model extraction / model stealing? How can an adversary clone your model through API access?
806. [Expert] Explain membership inference attacks. How do you determine if a specific example was in the training data?
807. [Advanced] What is differential privacy in ML training? How does DP-SGD work?
808. [Expert] Explain federated learning with privacy guarantees. How do you combine DP with federated aggregation?
809. [Advanced] What are adversarial examples in NLP? How do character-level, word-level, and sentence-level attacks work?
810. [Expert] Explain model watermarking for LLMs. How do you embed and detect watermarks in generated text?
811. [Advanced] How do you prevent training data extraction from LLMs? What is the memorization vs generalization tradeoff?
812. [Expert] Design a red-teaming framework for evaluating LLM safety. What attack categories do you test?
813. [Advanced] What are jailbreaking techniques for LLMs? How do automated red-teaming methods discover them?
814. [Expert] Explain the concept of machine unlearning. How do you remove the influence of specific data from a trained model?
815. [Advanced] How do you audit an LLM for bias? What systematic evaluation framework do you use?

### D.16 Emerging Architectures & Paradigms

816. [Expert] Explain the test-time training (TTT) paradigm. How do models adapt at inference time?
817. [Advanced] What are state-space duality models? How do they unify SSMs and attention?
818. [Expert] Explain the xLSTM architecture. How do modern LSTM variants compete with transformers?
819. [Advanced] What is the JEPA (Joint Embedding Predictive Architecture) proposed by Yann LeCun? How does it differ from generative models?
820. [Expert] Explain energy-based models and their resurgence in modern ML. How do they relate to diffusion models?
821. [Advanced] What is the Hyena operator? How does it replace attention with long convolutions?
822. [Expert] Explain the Griffin architecture. How does it combine gated linear recurrences with attention?
823. [Advanced] Compare tokenization approaches: BPE, WordPiece, Unigram, byte-level. How does tokenization impact multilingual performance?
824. [Expert] What is matryoshka representation learning? How does it create embeddings useful at multiple dimensions?
825. [Advanced] Explain the concept of model merging (model soups, TIES merging, DARE). How do you combine independently trained models?
826. [Expert] What are 1-bit LLMs (BitNet)? How does extreme quantization during training work?
827. [Advanced] Explain the concept of mixture of agents. How do multiple LLMs collaborate in a mixture?
828. [Expert] What is neural architecture search (NAS) in the LLM era? How do you efficiently search for optimal architectures?
829. [Advanced] Explain the concept of model distillation chains (GPT-4 → GPT-3.5 → smaller model). How does multi-step distillation work?
830. [Expert] What are liquid neural networks? How do they enable continuous-time adaptation?

### D.17 Evaluation & Benchmarking

831. [Advanced] How do you evaluate LLM capabilities comprehensively? Compare MMLU, HellaSwag, HumanEval, and MT-Bench.
832. [Expert] What is contamination in LLM evaluation? How do you detect if benchmark data leaked into training?
833. [Advanced] Explain the Chatbot Arena evaluation methodology. Why is it considered more reliable than static benchmarks?
834. [Expert] How do you evaluate factual accuracy in LLM outputs? Compare FActScore, TruthfulQA, and custom evaluation.
835. [Advanced] What are the challenges of evaluating generative models? Compare FID, CLIP score, and human evaluation.
836. [Expert] Design an evaluation framework for a domain-specific LLM (medical, legal, financial). What metrics matter?
837. [Advanced] How do you evaluate reasoning ability? Compare GSM8K, MATH, ARC, and Big-Bench Hard.
838. [Expert] Explain the concept of evaluation saturation. What do you do when models max out existing benchmarks?
839. [Advanced] How do you evaluate code generation quality? Compare HumanEval, MBPP, and SWE-bench.
840. [Expert] What is LLM-as-a-judge evaluation? When is it reliable and when does it fail?
841. [Advanced] How do you run reliable A/B tests for LLM applications where outputs are open-ended text?

---

## Summary Statistics

| Category | Subcategories | Question Count |
|----------|--------------|----------------|
| A. ML Coding & Implementation | 15 subcategories | 267 |
| B. ML System Design | 14 subcategories | 168 |
| C. Case Studies & Scenarios | 12 subcategories | 151 |
| D. Cutting-Edge & Recent Topics | 17 subcategories | 255 |
| **Total** | **58 subcategories** | **841** |

---

> **How to use this question bank:**
> - **Self-study:** Work through questions by category, starting with [Basic/Intermediate] and progressing to [Advanced/Expert].
> - **Interview prep:** Focus on categories relevant to your target role (MLE → A+B, Research → A+D, Applied Scientist → all).
> - **Coding practice:** Category A questions should be implemented and tested in a notebook.
> - **System design practice:** Category B questions should be practiced with a 45-minute whiteboard format.
> - **Mock interviews:** Use Category C scenarios for behavioral/case study rounds.
> - **Stay current:** Category D reflects 2024-2025 cutting-edge topics asked at top AI labs.
