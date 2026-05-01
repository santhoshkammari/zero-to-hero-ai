# Part 3: Deep Learning & Computer Vision

> 600+ interview questions covering Deep Learning Foundations, CNNs & Computer Vision, and Training Deep Networks.
> Each question is tagged with difficulty: **[Basic]**, **[Intermediate]**, **[Advanced]**, or **[Expert]**.

---

## 7. Deep Learning Foundations

### 7.1 Neural Network Architecture

1. [Basic] What is a neuron in a neural network? How does it relate to a biological neuron?
2. [Basic] Explain the structure of a feedforward neural network. What are input, hidden, and output layers?
3. [Basic] What is the difference between a single-layer perceptron and a multi-layer perceptron (MLP)?
4. [Basic] Why do neural networks need non-linear activation functions? What happens if all activations are linear?
5. [Basic] What is a bias term in a neural network, and why is it necessary?
6. [Basic] Explain the concept of "depth" vs "width" of a neural network. How do they affect model capacity?
7. [Basic] What is the Universal Approximation Theorem? What does it guarantee and what does it NOT guarantee?
8. [Basic] What is the difference between a dense (fully connected) layer and a sparse layer?
9. [Intermediate] How do you decide the number of layers and neurons for a given problem? What heuristics or techniques can you use?
10. [Intermediate] What is the difference between feedforward, recurrent, and convolutional neural networks? When would you use each?
11. [Intermediate] Explain the concept of a computation graph. Why is it useful for neural network training?
12. [Intermediate] What is the difference between a static computation graph (TensorFlow 1.x) and a dynamic computation graph (PyTorch)?
13. [Intermediate] How does the forward pass work in a neural network? Walk through a 3-layer network mathematically.
14. [Intermediate] What is the relationship between the number of parameters in a network and its capacity to memorize vs generalize?
15. [Intermediate] Explain parameter sharing. Where is it used and why?
16. [Intermediate] What are skip connections (residual connections)? Why do they help in training deep networks?
17. [Intermediate] Describe the difference between a bottleneck layer and a standard layer. Where are bottleneck layers used?
18. [Advanced] How does the lottery ticket hypothesis relate to neural network architecture?
19. [Advanced] What is Neural Architecture Search (NAS)? Describe at least two approaches to NAS.
20. [Advanced] Explain the concept of over-parameterization in neural networks. Why can over-parameterized networks still generalize well?
21. [Advanced] What are mixture-of-experts (MoE) layers? How do they scale model capacity without proportionally scaling compute?
22. [Advanced] How do attention mechanisms enhance traditional neural networks? Derive the scaled dot-product attention formula.
23. [Expert] Design a neural network architecture for a problem where inputs have variable-length sequences AND tabular features. How would you fuse these modalities?
24. [Expert] Explain the double descent phenomenon in neural networks. How does it challenge traditional bias-variance tradeoff understanding?
25. [Expert] What is the relationship between the rank of weight matrices and the expressiveness of a neural network?

### 7.2 Activation Functions

26. [Basic] What is the sigmoid activation function? Write its formula and derivative. What are its drawbacks?
27. [Basic] What is the tanh activation function? How does it compare to sigmoid?
28. [Basic] What is ReLU? Write its formula and explain why it became the default activation function.
29. [Basic] What is the "dying ReLU" problem? How does it occur during training?
30. [Basic] What is Leaky ReLU and how does it address the dying ReLU problem?
31. [Intermediate] Compare and contrast ReLU, Leaky ReLU, PReLU, and ELU. When would you choose each?
32. [Intermediate] What is the softmax function? How is it used in multi-class classification? Write its formula and derivative.
33. [Intermediate] What is GELU (Gaussian Error Linear Unit)? Why is it used in Transformer models like BERT and GPT?
34. [Intermediate] What is the Swish activation function? Write its formula: f(x) = x · σ(βx). How does the learnable parameter β affect behavior?
35. [Intermediate] Explain the relationship between the choice of activation function and weight initialization scheme.
36. [Intermediate] Why does sigmoid activation cause the vanishing gradient problem? Show mathematically that the gradient is at most 0.25.
37. [Advanced] Compare the computational cost of ReLU vs GELU vs Swish. What are the implications for large-scale deployment on GPUs/TPUs?
38. [Advanced] From the perspective of function approximation, how do the smoothness properties of GELU and Swish contribute to network expressiveness compared to ReLU?
39. [Advanced] GELU is used in Transformers while CNNs typically use ReLU. Why? What happens if you replace GELU with ReLU in a Transformer?
40. [Advanced] Design an ablation study to compare ReLU, GELU, and Swish in ResNet-50. What metrics would you track and how would you interpret results?
41. [Expert] Derive the gradient of the Swish activation and show why it retains non-zero gradients for negative inputs.
42. [Expert] What are the conditions under which a custom activation function would be beneficial? Design an activation function for a task with highly noisy input data.

### 7.3 Forward and Backward Pass

43. [Basic] Explain the forward pass in a neural network step by step.
44. [Basic] What is the loss function? Name three common loss functions and when you'd use each.
45. [Basic] What is cross-entropy loss? Write the formula for binary and multi-class cross-entropy.
46. [Basic] What is the backward pass? How does it relate to the forward pass?
47. [Intermediate] Walk through the forward pass of a 2-layer network with ReLU activation and softmax output mathematically.
48. [Intermediate] Why do we compute the forward pass before the backward pass? Can we compute gradients without storing intermediate activations?
49. [Intermediate] What is the difference between the loss function and the cost function?
50. [Intermediate] Explain how PyTorch's autograd system tracks operations for the backward pass. What does `requires_grad=True` do?
51. [Intermediate] What happens if you call `.backward()` multiple times on the same computation graph in PyTorch? What is `retain_graph=True`?
52. [Intermediate] Why do we need to zero out gradients before each backward pass? What happens if we don't?
53. [Advanced] What is gradient checkpointing (activation checkpointing)? How does it trade compute for memory during the backward pass?
54. [Advanced] Explain the difference between forward-mode and reverse-mode automatic differentiation. Why is reverse-mode preferred for neural networks?
55. [Advanced] What is gradient checking? How would you implement it to verify your backpropagation is correct?
56. [Expert] Implement the forward and backward pass for a 2-layer network from scratch in NumPy with ReLU and softmax.
57. [Expert] How does the backward pass differ for operations like max pooling vs average pooling? Derive the gradients for each.

### 7.4 Backpropagation & Gradients

58. [Basic] What is backpropagation? Explain the algorithm in simple terms.
59. [Basic] What is the chain rule of calculus and how is it used in backpropagation?
60. [Basic] What are gradients in the context of neural network training?
61. [Basic] What is gradient descent? Distinguish between batch, mini-batch, and stochastic gradient descent.
62. [Intermediate] Derive the backpropagation update rule for a single neuron with sigmoid activation and MSE loss.
63. [Intermediate] Derive backpropagation for a 2-layer network with ReLU activation and cross-entropy loss. Write out all partial derivatives.
64. [Intermediate] What is the vanishing gradient problem? Which activation functions and architectures are most susceptible?
65. [Intermediate] What is the exploding gradient problem? What are modern solutions (gradient clipping, better activations, initialization)?
66. [Intermediate] How does the depth of a network affect the magnitude of gradients during backpropagation? Show mathematically.
67. [Intermediate] Explain backpropagation through time (BPTT). What challenges does it face for long sequences?
68. [Intermediate] What is the Jacobian matrix in the context of backpropagation? When is it computed explicitly?
69. [Advanced] Derive the gradients for a softmax layer combined with cross-entropy loss. Why is this combination computationally convenient?
70. [Advanced] What is the Hessian matrix? How can second-order information be used to improve optimization?
71. [Advanced] Explain the concept of gradient flow through a network. How do skip connections, normalization, and activation choices affect gradient flow?
72. [Advanced] What is the difference between symbolic differentiation, numerical differentiation, and automatic differentiation?
73. [Advanced] What is truncated BPTT? When and why is it used?
74. [Expert] Derive the full backpropagation equations for a convolutional layer (including the gradient w.r.t. the kernel and the input).
75. [Expert] How does backpropagation work through a batch normalization layer? Derive the gradients for γ, β, and the input.
76. [Expert] Explain how higher-order gradients (Hessian-vector products) are computed efficiently using automatic differentiation.

### 7.5 Weight Initialization

77. [Basic] Why is weight initialization important in neural networks? What happens if you initialize all weights to zero?
78. [Basic] What happens if you initialize all weights to the same value (e.g., 0.5)?
79. [Basic] What is random initialization? Why do we use small random values?
80. [Intermediate] Explain Xavier (Glorot) initialization. Write the formula and explain when to use it.
81. [Intermediate] Explain He initialization. Write the formula and explain why it's preferred for ReLU networks.
82. [Intermediate] Why does Xavier initialization use Var(W) = 2/(n_in + n_out) while He initialization uses Var(W) = 2/n_in?
83. [Intermediate] What is the relationship between activation function choice and weight initialization strategy?
84. [Intermediate] What happens when weight initialization and activation function are mismatched (e.g., Xavier init with ReLU)?
85. [Advanced] Derive Xavier initialization from the condition that variance of activations should be preserved across layers.
86. [Advanced] What is LSUV (Layer-Sequential Unit-Variance) initialization? How does it differ from analytical methods like Xavier/He?
87. [Advanced] What is orthogonal initialization? When is it preferred over Xavier or He?
88. [Advanced] How does weight initialization interact with batch normalization? Does BN make initialization less important?
89. [Expert] You're training a very deep network (100+ layers) without residual connections. Design an initialization strategy that prevents vanishing/exploding activations. Justify mathematically.
90. [Expert] Explain the fixup initialization. How does it enable training very deep residual networks without normalization layers?
91. [Expert] How would you initialize weights for a network with mixed activation functions (e.g., ReLU in some layers, tanh in others)?

### 7.6 Batch Normalization & Other Normalizations

92. [Basic] What is batch normalization? Explain the algorithm step by step.
93. [Basic] Why is batch normalization used in deep neural networks? What problem does it solve?
94. [Basic] What are the learnable parameters γ (scale) and β (shift) in batch normalization? Why are they needed?
95. [Basic] How does batch normalization behave differently during training vs inference?
96. [Intermediate] Should you apply batch normalization before or after the activation function? What are the arguments for each?
97. [Intermediate] How does batch normalization affect the learning rate and convergence speed?
98. [Intermediate] What is internal covariate shift? Is BN's success truly due to reducing it? (Discuss the Santurkar et al. 2018 paper.)
99. [Intermediate] What happens if you use batch normalization with a batch size of 1?
100. [Intermediate] What is layer normalization? How does it differ from batch normalization?
101. [Intermediate] Why is layer normalization preferred over batch normalization in Transformers and RNNs?
102. [Intermediate] What is group normalization? Why was it introduced?
103. [Intermediate] Compare batch normalization, layer normalization, instance normalization, and group normalization. Over which dimensions does each normalize?
104. [Advanced] How do residual connections interact with normalization layers? What is Pre-Norm vs Post-Norm in Transformers?
105. [Advanced] Implement batch normalization from scratch, including the running mean/variance for inference mode.
106. [Advanced] What is RMSNorm? How does it simplify layer normalization and where is it used (e.g., LLaMA)?
107. [Advanced] In what scenarios does group normalization outperform batch normalization? Why?
108. [Advanced] Can normalization layers and dropout be used together? What are the interactions?
109. [Expert] Derive the backpropagation gradients through a batch normalization layer for γ, β, and the input x.
110. [Expert] How does batch normalization affect the loss landscape? (Reference: "How Does Batch Normalization Help Optimization?" paper.)
111. [Expert] Design an experiment to determine whether batch normalization is acting as a regularizer or an optimizer aid in a specific training setup.

### 7.7 Dropout & Regularization for Deep Networks

112. [Basic] What is dropout? How does it work during training and inference?
113. [Basic] What is the intuition behind why dropout works as a regularizer?
114. [Basic] What is the typical dropout rate used in practice? How do you choose it?
115. [Basic] What is the difference between L1 and L2 regularization? How do they affect learned weights?
116. [Intermediate] How is dropout related to ensemble learning? Explain the "averaging over sub-networks" interpretation.
117. [Intermediate] What is inverted dropout? How does it differ from standard dropout? Why is it preferred in practice?
118. [Intermediate] Can dropout be used in convolutional layers? What is spatial dropout and when should you use it?
119. [Intermediate] What is the effect of dropout on training loss vs validation loss curves?
120. [Intermediate] How does dropout interact with batch normalization? Are there potential issues?
121. [Intermediate] What is DropConnect? How does it differ from dropout?
122. [Intermediate] What is weight decay? How does it relate to L2 regularization?
123. [Advanced] What is the difference between weight decay and L2 regularization when using adaptive optimizers like Adam? (This is the motivation for AdamW.)
124. [Advanced] What is label smoothing? How does it act as a regularizer?
125. [Advanced] What is stochastic depth? How does it regularize deep residual networks?
126. [Advanced] What is cutout / random erasing as data-level regularization? When is it effective?
127. [Advanced] Explain the connection between dropout rate and model uncertainty (MC Dropout for Bayesian approximation).
128. [Expert] Derive the expected output of a neuron with dropout at training time and show why we scale by 1/(1-p) at test time.
129. [Expert] You have a model that overfits severely. It already uses dropout (0.5), L2 regularization, and data augmentation. What other regularization strategies would you try and why?
130. [Expert] Implement MC Dropout inference: how many forward passes are needed, and how do you compute prediction uncertainty?

### 7.8 Learning Rate Schedules

131. [Basic] What is the learning rate in gradient descent? Why is choosing the right learning rate important?
132. [Basic] What happens if the learning rate is too high? Too low?
133. [Basic] What is a learning rate schedule? Name three common types.
134. [Intermediate] What is step decay learning rate schedule? When would you use it?
135. [Intermediate] What is exponential decay? Write the formula.
136. [Intermediate] What is cosine annealing? Write the mathematical equation and explain why it's popular.
137. [Intermediate] What is learning rate warmup? Why is it useful, especially with large batch sizes?
138. [Intermediate] Compare linear warmup vs exponential warmup. When would you use each?
139. [Intermediate] What is the "1cycle" learning rate policy? How does it combine warmup and annealing?
140. [Intermediate] What is cosine annealing with warm restarts (SGDR)? What is the T_mult parameter?
141. [Advanced] How would you set up a training schedule that combines AdamW with cosine annealing and linear warmup?
142. [Advanced] What is the learning rate finder (from the "Cyclical Learning Rates" paper by Leslie Smith)? How does it work?
143. [Advanced] Why might you switch from Adam to SGD with momentum in later stages of training? When does this help?
144. [Advanced] What signs indicate that your learning rate schedule is not optimal? How would you diagnose this?
145. [Advanced] How does the effective learning rate change when using gradient accumulation? Why must you account for this?
146. [Expert] Derive the optimal learning rate for a quadratic loss landscape. How does this inform practical learning rate selection?
147. [Expert] How do learning rate schedules interact with batch size scaling rules (e.g., linear scaling rule)? When does the linear scaling rule break down?
148. [Expert] Design a learning rate schedule for a training run that starts on 8 GPUs and elastically scales to 64 GPUs mid-training.

### 7.9 Optimizers Deep Dive

149. [Basic] What is gradient descent? Write the update rule.
150. [Basic] What is the difference between batch gradient descent, mini-batch gradient descent, and SGD?
151. [Basic] What is momentum in SGD? Write the update equations.
152. [Basic] Why does momentum help in optimization? Explain using the analogy of a ball rolling down a hill.
153. [Intermediate] What is Nesterov momentum? How does it differ from classical momentum? Write both update rules.
154. [Intermediate] What is RMSProp? How does it adapt the learning rate per parameter?
155. [Intermediate] What is the Adam optimizer? Write the complete update equations including bias correction.
156. [Intermediate] What are the key hyperparameters in Adam (β1, β2, ε)? What do they control and what are typical values?
157. [Intermediate] Why is the bias correction term in Adam necessary? What happens without it in early iterations?
158. [Intermediate] What is AdaGrad? What is its main limitation for deep learning training?
159. [Advanced] What is AdamW? How does it differ from Adam with L2 regularization? Why is the decoupling important?
160. [Advanced] Write the AdamW update equations. Show mathematically why weight decay ≠ L2 regularization in Adam.
161. [Advanced] What is LAMB (Layer-wise Adaptive Moments optimizer for Batch training)? When is it used?
162. [Advanced] What is LARS (Layer-wise Adaptive Rate Scaling)? How does it enable training with very large batch sizes?
163. [Advanced] Compare Adam, AdamW, LAMB, and LARS. In what training regimes does each excel?
164. [Advanced] What is the "sharp minima" problem with Adam? Why might SGD with momentum find flatter minima?
165. [Advanced] What is gradient clipping? When and how should you apply it (by value vs by norm)?
166. [Advanced] What is the difference between gradient clipping by value and gradient clipping by norm? Write both algorithms.
167. [Advanced] What is the Adafactor optimizer? Why is it more memory-efficient than Adam?
168. [Expert] Implement Adam from scratch in Python/NumPy. Include bias correction and epsilon for numerical stability.
169. [Expert] Your model trains well with Adam but poorly with SGD. What could be causing this? How would you investigate?
170. [Expert] Design an optimizer for training a 175B parameter model. Consider memory constraints, distributed training, and convergence properties.
171. [Expert] Explain the connection between natural gradient descent and Adam. How does the Fisher information matrix relate to adaptive learning rates?
172. [Expert] What is sharpness-aware minimization (SAM)? How does it find flatter minima and why does that improve generalization?
173. [Expert] When training with very large batch sizes (32K+), why does SGD with momentum + LARS outperform Adam? Explain the theoretical basis.

---

## 8. CNNs & Computer Vision

### 8.1 Convolution Operation Fundamentals

174. [Basic] What is a convolution operation in the context of CNNs? How does it differ from cross-correlation?
175. [Basic] What is a filter (kernel) in a convolutional layer? What does it learn to detect?
176. [Basic] Explain the concept of stride in convolution. How does stride affect the output size?
177. [Basic] What is padding in convolution? What is the difference between "valid" and "same" padding?
178. [Basic] What is pooling? Compare max pooling and average pooling.
179. [Basic] What is the formula for computing the output spatial dimension of a convolution? [O = (W - K + 2P) / S + 1]
180. [Basic] Why are CNNs preferred over fully connected networks for image tasks?
181. [Intermediate] What is the receptive field of a neuron in a CNN? How does it grow with depth?
182. [Intermediate] Calculate the receptive field of a 3-layer CNN where each layer has a 3×3 kernel with stride 1. What if stride is 2?
183. [Intermediate] What is a 1×1 convolution? What are its uses in CNN architectures?
184. [Intermediate] What is depthwise separable convolution? How does it reduce computation compared to standard convolution?
185. [Intermediate] What is dilated (atrous) convolution? How does it increase the receptive field without increasing parameters?
186. [Intermediate] Explain the concept of feature maps. How do the number of feature maps change through a CNN?
187. [Intermediate] What is transposed convolution (deconvolution)? How is it used for upsampling?
188. [Intermediate] Compare transposed convolution, bilinear upsampling, and nearest-neighbor upsampling.
189. [Intermediate] What is the difference between a convolution with kernel 5×5 and two stacked 3×3 convolutions? Which is preferred and why?
190. [Advanced] Calculate the number of parameters and FLOPs for a convolutional layer with input channels C_in, output channels C_out, kernel size K, and spatial dimensions H×W.
191. [Advanced] How does a depthwise separable convolution decompose the standard convolution? Calculate the computational savings for a specific example.
192. [Advanced] What is group convolution? How does it relate to depthwise convolution and standard convolution?
193. [Advanced] What is deformable convolution? When would you use it over standard convolution?
194. [Advanced] Explain channel attention (squeeze-and-excitation blocks). How do they improve CNN performance?
195. [Expert] Derive the backpropagation equations for a convolutional layer. Show that the gradient w.r.t. the input is itself a convolution.
196. [Expert] You need to design a CNN that runs in real-time on a mobile device with 2 GFLOPS compute budget. What architectural choices would you make?
197. [Expert] Explain the relationship between the frequency response of a CNN filter and the features it detects. How does this relate to the receptive field?

### 8.2 Classic CNN Architectures

198. [Basic] Describe the LeNet-5 architecture. What task was it designed for?
199. [Basic] What was AlexNet and why was it significant in the history of deep learning?
200. [Basic] What is the VGG architecture? What design principle does it follow?
201. [Basic] Why did VGG use only 3×3 convolutions throughout the network?
202. [Intermediate] What is ResNet? Explain the residual learning framework and skip connections.
203. [Intermediate] What is a bottleneck block in ResNet? Why does ResNet-50 use bottleneck blocks while ResNet-34 does not?
204. [Intermediate] What is the difference between ResNet-18, ResNet-34, ResNet-50, ResNet-101, and ResNet-152?
205. [Intermediate] How does the identity mapping in ResNet affect gradient flow? Show mathematically.
206. [Intermediate] What is the Inception (GoogLeNet) architecture? Explain the Inception module.
207. [Intermediate] Why do Inception modules use multiple filter sizes (1×1, 3×3, 5×5) in parallel?
208. [Intermediate] What role do 1×1 convolutions play in Inception for dimensionality reduction?
209. [Intermediate] What is auxiliary loss in GoogLeNet? Why was it used?
210. [Intermediate] How did Inception evolve from v1 to v4? What key optimizations were introduced?
211. [Intermediate] What is convolution factorization (e.g., 7×7 into 1×7 and 7×1) in Inception v3? How does it reduce parameters?
212. [Intermediate] What is EfficientNet? Explain compound scaling.
213. [Intermediate] How does EfficientNet's compound scaling differ from scaling depth, width, or resolution individually?
214. [Intermediate] What is MBConv (Mobile Inverted Bottleneck Convolution) and how is it used in EfficientNet?
215. [Advanced] What is the squeeze-and-excitation (SE) block used in EfficientNet? How does it learn channel importance?
216. [Advanced] Compare EfficientNet, MobileNet, and ShuffleNet for mobile/edge deployment. What are the tradeoffs?
217. [Advanced] What is DenseNet? How does it differ from ResNet in terms of feature reuse?
218. [Advanced] What were the key innovations that allowed each architecture to go deeper: AlexNet→VGG→ResNet→EfficientNet?
219. [Advanced] How would you adapt ResNet for a segmentation task? What modifications are needed?
220. [Advanced] What is ConvNeXt? How does it modernize the ConvNet design using ideas from Transformers?
221. [Expert] Given a compute budget of 5 GFLOPs, design a CNN architecture for ImageNet classification. Justify your choices of depth, width, and resolution.
222. [Expert] Compare the loss landscapes of VGG-16 and ResNet-56. Why does ResNet have a smoother loss landscape?
223. [Expert] How would you use Neural Architecture Search to discover an optimal CNN for a specific edge device with memory and latency constraints?

### 8.3 Object Detection

224. [Basic] What is object detection? How does it differ from image classification?
225. [Basic] What is a bounding box? What representation formats exist (e.g., x,y,w,h vs x1,y1,x2,y2)?
226. [Basic] What is Intersection over Union (IoU)? Write the formula.
227. [Basic] What are the standard metrics for object detection (mAP, precision, recall)?
228. [Basic] What is the difference between one-stage and two-stage object detectors?
229. [Intermediate] What are anchor boxes? Why are they needed in object detection?
230. [Intermediate] How are anchor boxes generated? Explain using k-means clustering on ground-truth boxes.
231. [Intermediate] Explain Faster R-CNN architecture: backbone, Region Proposal Network (RPN), ROI Pooling, classification/regression heads.
232. [Intermediate] What is the Region Proposal Network (RPN)? How does it generate region proposals?
233. [Intermediate] What is ROI Pooling? What is ROI Align and why was it introduced?
234. [Intermediate] Explain the YOLO (You Only Look Once) architecture. How does it differ from R-CNN based methods?
235. [Intermediate] How does YOLO divide the image into a grid and predict bounding boxes? Walk through the prediction process.
236. [Intermediate] What is SSD (Single Shot MultiBox Detector)? How does it use multi-scale feature maps?
237. [Intermediate] What is Non-Maximum Suppression (NMS)? Describe the algorithm step by step.
238. [Intermediate] What is the difference between class-agnostic and class-wise NMS?
239. [Intermediate] How does anchor box selection impact model performance (recall and precision)?
240. [Intermediate] How does YOLO handle objects of different scales?
241. [Advanced] What is Soft-NMS? When is it better than standard NMS (e.g., crowded scenes)?
242. [Advanced] How do YOLO, SSD, and Faster R-CNN use anchor boxes differently?
243. [Advanced] What is Feature Pyramid Network (FPN)? How does it improve multi-scale detection?
244. [Advanced] What is focal loss? Why was it introduced (RetinaNet) and how does it address class imbalance?
245. [Advanced] Compare YOLOv5, YOLOv7, and YOLOv8. What are the key improvements in each version?
246. [Advanced] What are anchor-free detectors (e.g., CenterNet, FCOS)? How do they eliminate the need for anchor boxes?
247. [Advanced] Explain the DETR (Detection Transformer) architecture. How does it use attention for object detection?
248. [Advanced] How does DETR handle the set prediction problem? What is the Hungarian matching algorithm used in DETR?
249. [Advanced] How would you debug an object detector with low recall? List systematic steps.
250. [Advanced] What is NMS threshold and how does it affect precision-recall tradeoff?
251. [Expert] Design an object detection system for autonomous driving that must handle objects at 10m to 200m distance with varying sizes. What architecture and training strategy would you use?
252. [Expert] How would you optimize a YOLO model to run at 30 FPS on an edge device with 4 TOPS compute? What techniques would you apply?
253. [Expert] Compare DETR with Faster R-CNN in terms of training convergence, computational cost, and detection accuracy. When would you choose each?
254. [Expert] How do you handle extremely small objects (e.g., 10×10 pixels) in detection? What architectural and training modifications are needed?

### 8.4 Semantic Segmentation

255. [Basic] What is semantic segmentation? How does it differ from instance segmentation and object detection?
256. [Basic] What is pixel-wise classification and why is it the core of semantic segmentation?
257. [Basic] What are common evaluation metrics for semantic segmentation (IoU, Dice coefficient, pixel accuracy)?
258. [Intermediate] What is a Fully Convolutional Network (FCN)? How does it differ from a standard CNN?
259. [Intermediate] Explain the upsampling strategy in FCN. What are FCN-32s, FCN-16s, and FCN-8s?
260. [Intermediate] What is U-Net? Describe its encoder-decoder architecture with skip connections.
261. [Intermediate] Why are skip connections critical in U-Net? What information do they preserve?
262. [Intermediate] How would you modify U-Net for multi-class segmentation (vs binary)?
263. [Intermediate] What is DeepLab? How does it use atrous (dilated) convolutions for segmentation?
264. [Intermediate] What is Atrous Spatial Pyramid Pooling (ASPP) in DeepLab? Why is multi-scale context important?
265. [Intermediate] Compare DeepLabV3 and DeepLabV3+. What improvements were introduced?
266. [Intermediate] What loss functions are commonly used for segmentation (cross-entropy, Dice loss, focal loss)?
267. [Intermediate] How do you handle class imbalance in segmentation tasks?
268. [Advanced] What is the difference between U-Net and ResU-Net? How do residual connections help in segmentation?
269. [Advanced] Explain Panoptic Segmentation. How does it unify semantic and instance segmentation?
270. [Advanced] What are lightweight segmentation models for edge/mobile deployment (e.g., BiSeNet, ENet)?
271. [Advanced] What is MaskFormer? How does it use Transformer architecture for segmentation?
272. [Advanced] How does patch-based training differ from full-image training in segmentation? What are the tradeoffs?
273. [Advanced] What data augmentation techniques are most effective for segmentation? (Consider that labels must be augmented too.)
274. [Expert] Design a segmentation pipeline for medical images (e.g., organ segmentation in CT scans) with only 50 labeled volumes. Detail architecture, augmentation, loss function, and training strategy.
275. [Expert] How would you handle real-time segmentation for video at 60 FPS on a mobile GPU? What architectural and engineering tradeoffs?
276. [Expert] Compare U-Net, DeepLab, and SegFormer for aerial/satellite image segmentation. Justify your choice for a production system.

### 8.5 Image Classification & Transfer Learning

277. [Basic] What is image classification? What is a softmax classifier?
278. [Basic] What is transfer learning? Why is it effective for vision tasks?
279. [Basic] What is the difference between feature extraction and fine-tuning in transfer learning?
280. [Basic] What is data augmentation? List 5 common augmentation techniques for images.
281. [Intermediate] How do you decide which layers of a pre-trained network to freeze vs fine-tune?
282. [Intermediate] What is domain shift? How does it affect transfer learning performance?
283. [Intermediate] What is "negative transfer"? When does transfer learning hurt performance?
284. [Intermediate] What is mixup augmentation? Write the formula and explain the intuition.
285. [Intermediate] What is CutMix? How does it differ from Cutout and Mixup?
286. [Intermediate] What is AutoAugment? How does it learn augmentation policies?
287. [Intermediate] How would you fine-tune a pre-trained model for a dataset with only 100 images per class?
288. [Intermediate] What is layer-wise learning rate decay? How does it help during fine-tuning?
289. [Intermediate] Should batch normalization layers be frozen during fine-tuning? Why or why not?
290. [Intermediate] What is discriminative fine-tuning?
291. [Intermediate] How do you handle class imbalance in image classification? (Oversampling, class weights, focal loss, etc.)
292. [Advanced] What is catastrophic forgetting in the context of fine-tuning? How can it be mitigated?
293. [Advanced] Compare CNN-based, ViT-based, and MLP-Mixer-based approaches for image classification. When would you choose each?
294. [Advanced] What is self-supervised pre-training for vision? How does it compare to supervised pre-training for transfer learning?
295. [Advanced] What is knowledge distillation? How can a smaller "student" model learn from a larger "teacher" model?
296. [Advanced] What are Test-Time Augmentation (TTA) techniques? How do they improve classification accuracy?
297. [Expert] Design a complete image classification pipeline for a production system: model selection, training, evaluation, serving. The dataset has 10K classes and 100M images.
298. [Expert] You need to classify satellite images into 50 land-use categories. You have 500 labeled images per class. Design the complete approach (pre-training, augmentation, architecture, training strategy).
299. [Expert] How would you adapt a model pre-trained on ImageNet to classify X-ray images? Discuss domain gap and adaptation strategies.

### 8.6 Modern Vision: ViT, CLIP, DINOv2, SAM

300. [Basic] What is a Vision Transformer (ViT)? How does it apply Transformer architecture to images?
301. [Basic] How does ViT tokenize an image into patches? What is the role of positional embeddings?
302. [Intermediate] Walk through the forward pass of a ViT model: image → patches → embeddings → Transformer → classification.
303. [Intermediate] What are the main advantages and disadvantages of ViT compared to CNNs?
304. [Intermediate] Why does ViT typically require pre-training on large datasets to perform well?
305. [Intermediate] What is the effect of patch size in ViT on performance and compute?
306. [Intermediate] How would you fine-tune a ViT for a downstream classification task?
307. [Intermediate] What is CLIP? What problem does it solve in vision-language modeling?
308. [Intermediate] How does CLIP's contrastive learning objective work? Explain the image-text alignment.
309. [Intermediate] How does CLIP enable zero-shot image classification?
310. [Intermediate] What is prompt engineering in the context of CLIP?
311. [Intermediate] What are the main limitations or failure modes of CLIP?
312. [Advanced] What is DINOv2? Explain the self-supervised learning approach using teacher-student architecture.
313. [Advanced] How is knowledge distilled in DINOv2? What is the role of the exponential moving average teacher?
314. [Advanced] What is the multi-crop strategy in DINO/DINOv2 and why is it important?
315. [Advanced] Why are DINO features particularly good for downstream tasks like segmentation and detection without fine-tuning?
316. [Advanced] What is SAM (Segment Anything Model)? Why is it significant for computer vision?
317. [Advanced] Explain promptable segmentation in SAM. What types of prompts does it support (points, boxes, masks)?
318. [Advanced] How does SAM achieve open-world (zero-shot) segmentation?
319. [Advanced] How does SAM use ViT as its backbone? What is the role of the mask decoder?
320. [Advanced] Compare SAM to traditional segmentation networks (Mask R-CNN, U-Net). When would you use SAM?
321. [Advanced] What are hybrid CNN-Transformer architectures? Give examples and explain when they outperform pure architectures.
322. [Expert] How would you choose between ViT, DINOv2 features, and a fine-tuned CNN for a medical imaging application? Discuss data requirements, performance, and compute.
323. [Expert] How can SAM be integrated with CLIP for interactive labeling tools? Design the system architecture.
324. [Expert] What are the compute and memory scaling properties of ViT as a function of image resolution and patch size? Derive the relationship.
325. [Expert] Compare the representation quality of DINOv2, CLIP, and supervised ViT features for a retrieval task. How would you evaluate them?
326. [Expert] Design a vision system for a robotics application that needs to segment novel objects it has never seen during training. Which combination of these modern models would you use and why?

---

## 9. Training Deep Networks

### 9.1 Gradient Accumulation & Mixed Precision

327. [Basic] What is gradient accumulation? Why is it useful?
328. [Basic] How does gradient accumulation simulate a larger batch size without increasing memory?
329. [Basic] What is mixed precision training? Why does it enable faster training?
330. [Basic] What is the difference between FP32, FP16, and BF16 number formats?
331. [Intermediate] Write pseudocode for a training loop with gradient accumulation over N steps.
332. [Intermediate] How does the effective batch size change with gradient accumulation? How should you adjust the learning rate?
333. [Intermediate] What is loss scaling in mixed precision training? Why is it necessary for FP16?
334. [Intermediate] What are the common numerical issues with FP16 (underflow, overflow)? How does loss scaling address them?
335. [Intermediate] How would you implement mixed precision training in PyTorch using `torch.cuda.amp`?
336. [Intermediate] What hardware support is needed for mixed precision training (Tensor Cores, etc.)?
337. [Intermediate] Why is BF16 often preferred over FP16 for training? What is its advantage in terms of dynamic range?
338. [Intermediate] How does mixed precision affect memory usage? Calculate the memory savings for a model with 1B parameters.
339. [Advanced] What is dynamic loss scaling? How does it automatically find the right scaling factor?
340. [Advanced] How does gradient accumulation interact with batch normalization statistics? What are the pitfalls?
341. [Advanced] Can you combine mixed precision with gradient accumulation? What considerations are needed?
342. [Advanced] What operations must remain in FP32 even during mixed precision training (e.g., loss computation, softmax)? Why?
343. [Advanced] How does mixed precision affect model convergence? Are there cases where it changes the final accuracy?
344. [Expert] Implement a custom mixed precision training loop that handles dynamic loss scaling, gradient accumulation, and gradient clipping together.
345. [Expert] Your model trains well in FP32 but diverges in mixed precision FP16. How would you systematically debug this?
346. [Expert] Compare FP16 mixed precision, BF16 mixed precision, and FP8 training. What are the tradeoffs for each?

### 9.2 Distributed Training

347. [Basic] What is distributed training? Why is it necessary for modern deep learning?
348. [Basic] What is data parallelism? Explain how it works.
349. [Basic] What is model parallelism? When do you need it?
350. [Basic] What are the main challenges in distributed training?
351. [Intermediate] Explain the difference between synchronous and asynchronous gradient updates in distributed training.
352. [Intermediate] What is the all-reduce operation? How is it used to aggregate gradients across workers?
353. [Intermediate] What is ring-allreduce? Why is it more efficient than parameter server approaches?
354. [Intermediate] What is the parameter server architecture? What are its advantages and limitations?
355. [Intermediate] How do bandwidth and network latency affect distributed training performance?
356. [Intermediate] What is the straggler problem in distributed training? How can it be mitigated?
357. [Intermediate] What is gradient compression? When would you use it?
358. [Intermediate] What is PyTorch DistributedDataParallel (DDP)? How does it differ from DataParallel?
359. [Intermediate] How does Horovod simplify distributed training?
360. [Advanced] Explain pipeline parallelism. How does it differ from data and model parallelism?
361. [Advanced] What is tensor parallelism? How does it split individual layers across multiple GPUs?
362. [Advanced] Compare data parallelism, model parallelism, pipeline parallelism, and tensor parallelism. When would you use each?
363. [Advanced] What is the impact of batch size scaling in distributed settings? Explain the linear scaling rule.
364. [Advanced] When does the linear scaling rule break down? What alternatives exist (e.g., LARS, LAMB)?
365. [Advanced] How do you implement fault tolerance in distributed training? What happens when a worker fails?
366. [Advanced] What is elastic training? How do frameworks like PyTorch Elastic handle dynamic worker counts?
367. [Advanced] What is communication overlap (overlapping computation with gradient communication)? How does it improve training throughput?
368. [Expert] Design a distributed training strategy for a 70B parameter model on a cluster of 64 A100 GPUs across 8 nodes. Specify the parallelism strategy.
369. [Expert] You observe lower-than-expected GPU utilization during distributed training. What diagnostic steps would you take? List at least 5 things to check.
370. [Expert] Explain the mathematical equivalence (or non-equivalence) of training with batch size B on 1 GPU vs batch size B/N on N GPUs with gradient aggregation.
371. [Expert] How do you handle non-uniform GPU configurations in a heterogeneous cluster for distributed training?

### 9.3 Training Stability & Loss Landscape

372. [Basic] What is a loss curve? What should a healthy training loss curve look like?
373. [Basic] What is overfitting? How do you detect it from training/validation curves?
374. [Basic] What is underfitting? What are common causes and fixes?
375. [Basic] What does it mean when training loss and validation loss diverge?
376. [Intermediate] What is the loss landscape of a neural network? Why do flat minima tend to generalize better than sharp minima?
377. [Intermediate] What causes training loss to oscillate? List at least 4 possible reasons and fixes.
378. [Intermediate] What is gradient norm monitoring? How do you use it to detect training instability?
379. [Intermediate] What is gradient clipping? When should you apply it and what are the tradeoffs?
380. [Intermediate] How does learning rate warmup improve training stability, especially for large batch training?
381. [Intermediate] What is the effect of batch size on the loss landscape and training stability?
382. [Intermediate] What is the learning rate finder? How does it help identify the optimal learning rate range?
383. [Advanced] Explain mode connectivity in neural networks. What does it imply about the loss landscape?
384. [Advanced] What is the "edge of stability" phenomenon? How does it relate to the largest eigenvalue of the Hessian?
385. [Advanced] How does batch normalization affect the loss landscape smoothness? (Reference: Santurkar et al. 2018)
386. [Advanced] What is the relationship between the condition number of the Hessian and training difficulty?
387. [Advanced] How do skip connections in ResNet affect the loss landscape geometry?
388. [Advanced] What is the role of noise in SGD for escaping local minima? How does batch size affect this noise?
389. [Expert] Training loss suddenly spikes to NaN at step 50,000 of a 100,000 step training run. Walk through your complete debugging process.
390. [Expert] How would you visualize the loss landscape of a neural network? Describe the filter-wise normalization technique from Li et al. 2018.
391. [Expert] Explain the Sharpness-Aware Minimization (SAM) approach. How does it modify the optimization to find flatter minima?

### 9.4 Debugging Training

392. [Basic] Your training loss is not decreasing. What are the first things you check?
393. [Basic] How do you know if your model is overfitting or underfitting from loss curves?
394. [Basic] What is a learning curve? How do you interpret it for debugging?
395. [Intermediate] Your training loss decreases but validation loss increases after a few epochs. What's happening and how do you fix it?
396. [Intermediate] Training loss is oscillating wildly. List possible causes and how to diagnose each.
397. [Intermediate] Your model's accuracy is stuck at the random baseline (e.g., 10% for 10-class problem). What could be wrong?
398. [Intermediate] How do you check if your data pipeline is correct before training? What sanity checks should you perform?
399. [Intermediate] What is the "overfit to one batch" debugging technique? Why is it useful?
400. [Intermediate] How do you diagnose whether the problem is in the data, the model, or the training configuration?
401. [Intermediate] What gradient norms indicate healthy training? What do very large or very small gradient norms suggest?
402. [Intermediate] What tools and techniques exist for visualizing activations and gradients during training?
403. [Advanced] Your model trains perfectly on the training set but performs poorly on a held-out test set that was drawn from the same distribution. What could cause this besides overfitting?
404. [Advanced] You're training a GAN and observe mode collapse. How do you diagnose and fix it?
405. [Advanced] Your transformer model's training loss shows periodic spikes. What could cause this and how would you investigate?
406. [Advanced] Training loss is decreasing but validation metrics (e.g., mAP) are not improving. What's going on?
407. [Advanced] How do you debug numerical instability in training? What operations are prone to numerical issues?
408. [Advanced] Your model works well on clean data but fails on slightly noisy inputs. How do you improve robustness?
409. [Expert] You're pre-training a large language model and observe a sudden loss spike at 20% through training. The spike does not recover. Walk through the complete debugging process with specific tools and checks.
410. [Expert] Design a comprehensive monitoring dashboard for a multi-day training run. What metrics would you track and what alerts would you set up?
411. [Expert] Your distributed training achieves 60% scaling efficiency (vs theoretical linear scaling). Diagnose the bottleneck: is it computation, communication, data loading, or synchronization?

### 9.5 Hardware: GPU, TPU, and Memory Optimization

412. [Basic] What is a GPU and why is it well-suited for deep learning computations?
413. [Basic] What is CUDA? What is a CUDA core?
414. [Basic] What is the difference between GPU memory (VRAM) and system memory (RAM) in the context of training?
415. [Basic] Why do larger batch sizes require more GPU memory?
416. [Intermediate] What is a Tensor Core? How does it accelerate matrix multiplications for deep learning?
417. [Intermediate] What is the difference between a GPU and a TPU? When would you choose one over the other?
418. [Intermediate] What are CUDA streams? How can they be used to overlap data transfer and computation?
419. [Intermediate] Explain GPU memory fragmentation. What causes it and how can it be mitigated?
420. [Intermediate] What is pinned (page-locked) memory? Why is it useful for GPU training?
421. [Intermediate] What is the memory footprint of training a neural network? Break it down: model parameters, gradients, optimizer states, activations.
422. [Intermediate] What is activation checkpointing (gradient checkpointing)? How does it trade compute for memory?
423. [Intermediate] What is CPU offloading? When would you offload parameters or optimizer states to CPU?
424. [Intermediate] What is NCCL? How does it facilitate communication for distributed GPU training?
425. [Advanced] Calculate the GPU memory required to train a 7B parameter model with Adam optimizer in FP32. Then calculate with mixed precision.
426. [Advanced] What is memory-efficient attention (e.g., FlashAttention)? How does it reduce memory usage for transformer training?
427. [Advanced] What is NVLink? How does it affect multi-GPU training performance compared to PCIe?
428. [Advanced] How do you profile GPU utilization and identify bottlenecks (e.g., using NVIDIA Nsight, PyTorch profiler)?
429. [Advanced] What is the difference between compute-bound and memory-bound operations? Give examples of each in deep learning.
430. [Advanced] What is operator fusion and how does it improve GPU performance?
431. [Advanced] Explain the roofline model for GPU performance analysis. How do you determine if a kernel is compute-bound or memory-bound?
432. [Expert] A model throws CUDA OOM with batch size 16 on an A100 80GB. With batch size 8, training proceeds but GPU utilization is only 40%. Describe how you would systematically profile and optimize.
433. [Expert] Compare the architectures of NVIDIA A100, H100, and AMD MI300X for deep learning training. What are the key differences?
434. [Expert] Design a memory optimization strategy for training a 13B parameter model on a single A100 80GB GPU. Specify exactly which techniques you'd apply and the expected memory savings.
435. [Expert] How would you optimize a custom CUDA kernel for a novel attention mechanism? What tools and techniques would you use?

### 9.6 DeepSpeed, FSDP & ZeRO Optimization

436. [Basic] What is DeepSpeed? What problem does it solve?
437. [Basic] What is FSDP (Fully Sharded Data Parallel)? How does it differ from standard DDP?
438. [Intermediate] Explain the ZeRO (Zero Redundancy Optimizer) framework. What are its three stages?
439. [Intermediate] What does ZeRO Stage 1 shard? What memory savings does it achieve?
440. [Intermediate] What does ZeRO Stage 2 shard in addition to Stage 1? What are the additional savings?
441. [Intermediate] What does ZeRO Stage 3 shard? Why is it the most memory-efficient but also has the most communication overhead?
442. [Intermediate] What is the difference between FSDP and DeepSpeed ZeRO? When would you choose one over the other?
443. [Intermediate] What is activation checkpointing in the context of DeepSpeed/FSDP? How does it complement ZeRO?
444. [Intermediate] What is CPU offloading in DeepSpeed? When is it beneficial and what are the tradeoffs?
445. [Advanced] Walk through the FSDP forward and backward pass. How is memory managed at each stage?
446. [Advanced] How does DeepSpeed overlap communication and computation to accelerate training?
447. [Advanced] What is ZeRO-Offload? How does it use CPU and NVMe for training models that don't fit in GPU memory?
448. [Advanced] What is ZeRO-Infinity? How does it enable training models with trillions of parameters?
449. [Advanced] What are the benefits and drawbacks of ZeRO Stage 3? When might Stage 2 be a better choice?
450. [Advanced] How does communication overhead scale with the number of GPUs in ZeRO Stage 3?
451. [Advanced] What is DeepSpeed's pipeline parallelism implementation? How does it reduce the pipeline bubble?
452. [Expert] Given a training cluster of 8 A100 GPUs, explain step by step how you would configure DeepSpeed to train a GPT-3 sized model (175B parameters).
453. [Expert] A model trains fine with DDP but switching to FSDP causes instability and slower convergence. What possible causes and fixes can you identify?
454. [Expert] Compare DeepSpeed ZeRO Stage 3, FSDP, and Megatron-LM for training a 70B parameter model. What are the tradeoffs in ease of use, performance, and scalability?
455. [Expert] Design a complete distributed training stack for a 100B parameter model on 256 GPUs across 32 nodes. Specify ZeRO stage, parallelism strategy, mixed precision, and communication optimization.
456. [Expert] How would you benchmark and compare DeepSpeed vs FSDP for your specific model and cluster? What metrics would you measure?

### 9.7 Advanced Training Techniques

457. [Intermediate] What is curriculum learning? How can training data ordering affect convergence?
458. [Intermediate] What is progressive resizing/training? How does training on small images first and then larger images improve efficiency?
459. [Intermediate] What is knowledge distillation for training? How does the teacher-student framework work?
460. [Intermediate] What is the difference between hard labels and soft labels in distillation? Why do soft labels help?
461. [Intermediate] What is multi-task learning? How do you balance losses from multiple tasks?
462. [Advanced] What is contrastive learning? Explain SimCLR and BYOL approaches.
463. [Advanced] What is self-supervised pre-training? Compare MAE (Masked Autoencoders) and contrastive methods for vision.
464. [Advanced] What is Exponential Moving Average (EMA) of model weights? Why is it used during training?
465. [Advanced] How do you handle training on datasets with noisy labels? What techniques exist?
466. [Advanced] What is adversarial training? How does it improve model robustness?
467. [Advanced] What is the lottery ticket hypothesis? How does it relate to pruning and efficient training?
468. [Expert] Design a pre-training strategy for a vision foundation model that will be used for 20 different downstream tasks. Consider data, augmentation, objectives, and compute budget.
469. [Expert] How would you implement elastic training that can dynamically add or remove GPUs without restarting? What framework support is needed?
470. [Expert] You need to train a model 10x faster without changing the model architecture. What techniques would you apply? (Discuss: larger batch, mixed precision, data parallelism, efficient data loading, compilation, etc.)

### 9.8 Practical Training Scenarios & System Design

471. [Intermediate] How do you set up a data loading pipeline to keep the GPU fully utilized? What is the role of num_workers and prefetching?
472. [Intermediate] What is the difference between `torch.compile`, `torch.jit.script`, and `torch.jit.trace` in PyTorch? When would you use each?
473. [Intermediate] How do you save and resume training from checkpoints? What state needs to be saved?
474. [Intermediate] What is reproducibility in deep learning training? How do you ensure deterministic results?
475. [Intermediate] How do you handle training on datasets that don't fit in memory?
476. [Advanced] What is torch.compile and how does it optimize training? What graph optimizations does it perform?
477. [Advanced] What is ONNX? How is it used for model export and inference optimization?
478. [Advanced] How do you profile a training pipeline end-to-end to find the bottleneck (data loading, forward pass, backward pass, optimizer step)?
479. [Advanced] What is the WebDataset format? How does it improve data loading for large-scale training?
480. [Advanced] How do you handle training with extremely large datasets (100TB+)? What storage and data loading strategies are needed?
481. [Expert] Design a complete training infrastructure for a team training multiple models simultaneously on a shared GPU cluster. Consider scheduling, monitoring, experiment tracking, and resource allocation.
482. [Expert] You have a budget of $100K in cloud compute. Design the most efficient training setup for a 30B parameter language model. Specify hardware, parallelism, and training schedule.
483. [Expert] How would you implement automatic hyperparameter tuning at scale? Compare Bayesian optimization, population-based training, and random search for a large-scale training job.

---

## Appendix: Additional Cross-Cutting Questions

### A.1 Mathematical & Derivation Questions

484. [Intermediate] Derive the gradient of the sigmoid function σ(x) and show that σ'(x) = σ(x)(1-σ(x)).
485. [Intermediate] Derive the gradient of the softmax function with respect to its inputs.
486. [Intermediate] Show that the gradient of cross-entropy loss combined with softmax simplifies to (ŷ - y).
487. [Intermediate] Derive the update equations for SGD with Nesterov momentum.
488. [Advanced] Derive the backpropagation equations for a 2-layer network: input → linear → ReLU → linear → softmax → cross-entropy loss. Write all partial derivatives.
489. [Advanced] Calculate the receptive field of a CNN with 5 convolutional layers, each with 3×3 kernels, where layers 2 and 4 have stride 2.
490. [Advanced] Derive Xavier initialization from the variance preservation condition. Start from Var(output) = Var(input).
491. [Advanced] Prove that the gradient of the L2 regularization term λ||w||² with respect to w is 2λw.
492. [Advanced] Derive the memory footprint formula for training a transformer with mixed precision: account for parameters, gradients, optimizer states, and activations.
493. [Expert] Derive the full backpropagation equations through a batch normalization layer, computing ∂L/∂γ, ∂L/∂β, and ∂L/∂x_i.
494. [Expert] Prove the computational equivalence of a 5×5 convolution and two stacked 3×3 convolutions in terms of receptive field, and calculate the parameter savings.
495. [Expert] Derive the communication volume for ZeRO Stage 1, 2, and 3 as a function of model size and number of GPUs.
496. [Expert] Calculate the theoretical peak TFLOPS for an A100 GPU in FP16 and the arithmetic intensity needed to reach peak performance.

### A.2 Design & Architecture Questions

497. [Intermediate] Design a CNN for classifying 224×224 RGB images into 1000 classes. Specify layers, filter sizes, and approximate parameter count.
498. [Intermediate] Design a data augmentation pipeline for training an object detection model on autonomous driving data.
499. [Advanced] Design a model architecture for a task that requires processing both images and text (e.g., visual question answering). How would you fuse the modalities?
500. [Advanced] Design a training pipeline for a self-driving car perception system. How would you handle multiple tasks (detection, segmentation, depth estimation) in a single model?
501. [Advanced] Design an efficient CNN backbone for edge deployment on a device with 1 GFLOP compute budget and 200MB memory.
502. [Advanced] Design a training strategy to fine-tune a ViT-Large model on a medical imaging dataset with only 1,000 labeled images.
503. [Expert] Design a complete MLOps pipeline for continuously training and deploying a computer vision model that needs to adapt to distribution shift over time.
504. [Expert] Design a multi-modal foundation model training setup that handles images, text, and video. Specify architecture, training objectives, data, and distributed training strategy.
505. [Expert] Design a training-serving system where model quality degrades gracefully as inference latency budget decreases (e.g., from 100ms to 10ms).

### A.3 Debugging & Troubleshooting Scenarios

506. [Intermediate] Your CNN model achieves 95% training accuracy but only 60% test accuracy. What do you do?
507. [Intermediate] Your segmentation model predicts all pixels as background. What's wrong and how do you fix it?
508. [Intermediate] Your object detection model has high precision but low recall. How do you improve recall?
509. [Intermediate] Training loss shows "sawtooth" pattern—drops then jumps back up periodically. What's causing this?
510. [Advanced] Your model trains well on one GPU but accuracy drops when you scale to 8 GPUs. What could be wrong?
511. [Advanced] You switch from SGD to Adam and your model's test accuracy drops by 2%. Why might this happen?
512. [Advanced] Your mixed precision training produces slightly different results than FP32 training. Is this expected? When is it a problem?
513. [Advanced] Training a ViT from scratch on a small dataset (10K images) yields poor results, but a CNN works fine. Why?
514. [Advanced] Your model's training loss is NaN. List 5 possible causes and how to diagnose each.
515. [Expert] You're training a 7B parameter model and observe periodic loss spikes every ~5000 steps. The spikes are getting larger. Diagnose and fix.
516. [Expert] Your training runs are not reproducible despite setting all random seeds. What else could be causing non-determinism?
517. [Expert] Training efficiency drops from 90% to 50% GPU utilization after adding gradient accumulation steps. Diagnose and fix.

### A.4 Compare & Contrast Questions

518. [Basic] Compare batch gradient descent, mini-batch gradient descent, and stochastic gradient descent.
519. [Basic] Compare CNNs and fully connected networks for image processing.
520. [Intermediate] Compare Adam and SGD with momentum. When would you use each?
521. [Intermediate] Compare batch normalization, layer normalization, and group normalization.
522. [Intermediate] Compare one-stage (YOLO, SSD) and two-stage (Faster R-CNN) detectors.
523. [Intermediate] Compare U-Net and FCN for semantic segmentation.
524. [Advanced] Compare data parallelism, model parallelism, and pipeline parallelism with specific examples.
525. [Advanced] Compare DeepSpeed ZeRO and PyTorch FSDP for training large models.
526. [Advanced] Compare ViT and ResNet for image classification in terms of inductive biases, data efficiency, and scalability.
527. [Advanced] Compare YOLO, DETR, and Faster R-CNN. When would you choose each?
528. [Expert] Compare the training efficiency of different parallelism strategies (data, tensor, pipeline, expert) for models of different sizes (1B, 10B, 100B parameters).
529. [Expert] Compare training on A100 GPUs vs Google TPU v4 for a large vision model. Consider throughput, cost, and ease of use.

### A.5 Conceptual Deep Dives

530. [Intermediate] Why do deeper networks tend to perform better than wider networks for the same parameter count?
531. [Intermediate] What is the information bottleneck principle and how does it relate to deep learning?
532. [Intermediate] How does the choice of optimizer affect the implicit regularization of the training process?
533. [Advanced] What is the neural tangent kernel (NTK) and what does it tell us about neural network training dynamics?
534. [Advanced] Explain the connection between dropout and Bayesian inference (MC Dropout).
535. [Advanced] How does label smoothing regularize training? What is the optimal smoothing parameter?
536. [Advanced] What is the relationship between the flatness of minima and generalization? Is SAM's approach theoretically justified?
537. [Expert] Explain the "grokking" phenomenon where models suddenly generalize long after memorizing the training data. What causes it?
538. [Expert] What is the connection between the loss landscape, the Hessian spectrum, and generalization in deep networks?
539. [Expert] How does the initialization scale affect the feature learning regime vs the lazy (kernel) regime of training?

### A.6 Additional Computer Vision Questions

540. [Basic] What is image preprocessing? What normalization is typically applied before feeding images to a CNN?
541. [Basic] What is the difference between grayscale, RGB, and RGBA images? How does channel count affect CNN design?
542. [Intermediate] What is style transfer? How does it use the Gram matrix of feature maps?
543. [Intermediate] What is Grad-CAM? How does it visualize which regions a CNN focuses on?
544. [Intermediate] How do you visualize the features learned by intermediate CNN layers?
545. [Intermediate] What is image super-resolution? What architectures are used (SRCNN, ESRGAN)?
546. [Intermediate] What is optical flow estimation? How are deep learning models used for it?
547. [Advanced] What is generative adversarial network (GAN) for image generation? Explain the training dynamics.
548. [Advanced] What is a diffusion model? How does it generate images through iterative denoising?
549. [Advanced] What is NeRF (Neural Radiance Fields)? How does it represent 3D scenes?
550. [Advanced] What is pose estimation? Compare top-down and bottom-up approaches.
551. [Advanced] What is video understanding? How do temporal models (3D CNNs, Video Transformers) extend image models?
552. [Expert] Design a real-time multi-object tracking system for surveillance. Specify detector, tracker, and re-identification components.
553. [Expert] Design a visual search system that can find similar products from a catalog of 10 million items given a query image.

### A.7 Additional Deep Learning Foundation Questions

554. [Basic] What is an epoch? What is an iteration? What is the relationship between them?
555. [Basic] What is early stopping? How do you implement it?
556. [Basic] What is a hyperparameter vs a parameter in neural networks?
557. [Intermediate] What is the difference between generative and discriminative models?
558. [Intermediate] What is an autoencoder? Describe the encoder-decoder architecture and its uses.
559. [Intermediate] What is a variational autoencoder (VAE)? How does it differ from a standard autoencoder?
560. [Intermediate] What is the reparameterization trick in VAEs and why is it necessary?
561. [Intermediate] What is teacher forcing in sequence-to-sequence models?
562. [Intermediate] What is scheduled sampling? How does it bridge the gap between training and inference?
563. [Advanced] What is the Straight-Through Estimator (STE)? When is it used?
564. [Advanced] What are implicit layers in neural networks (e.g., DEQ - Deep Equilibrium Models)?
565. [Advanced] What is meta-learning? Explain MAML (Model-Agnostic Meta-Learning) at a high level.
566. [Advanced] What is few-shot learning? How do metric learning approaches (Siamese networks, Prototypical Networks) work?
567. [Expert] Explain the relationship between information theory and deep learning. How does mutual information relate to layer representations?
568. [Expert] What is the PAC-Bayes framework and how does it provide generalization bounds for neural networks?

### A.8 Additional Training & Optimization Questions

569. [Intermediate] What is the difference between online learning and batch learning? When would you use each?
570. [Intermediate] What is federated learning? How does it relate to distributed training while preserving privacy?
571. [Intermediate] What is model pruning? Describe structured vs unstructured pruning.
572. [Intermediate] What is quantization-aware training (QAT)? How does it differ from post-training quantization?
573. [Intermediate] What is the difference between symmetric and asymmetric quantization?
574. [Advanced] What is Neural Architecture Search (NAS)? Compare differentiable NAS (DARTS) and reinforcement learning-based NAS.
575. [Advanced] What is progressive training? How can you gradually increase model complexity during training?
576. [Advanced] What is continual (lifelong) learning? How do you prevent catastrophic forgetting?
577. [Advanced] What is reward modeling and RLHF? How is it used to train models with human preferences?
578. [Expert] Design a training pipeline that automatically detects and handles training instabilities (loss spikes, gradient explosions) without human intervention.
579. [Expert] How would you train a model that is robust to adversarial examples? Compare adversarial training, certified defenses, and randomized smoothing.
580. [Expert] Design an efficient hyperparameter search strategy for a model that takes 48 hours per training run. Budget: 20 training runs.

### A.9 Real-World Company Interview Questions

581. [Intermediate] (Google) How would you design a visual search system for Google Lens? What embedding architecture and retrieval system would you use?
582. [Intermediate] (Meta) How would you train an image classification model for content moderation at Facebook's scale (billions of images)?
583. [Intermediate] (Tesla) Design the perception stack for autonomous driving: what models, what inputs, how do you handle edge cases?
584. [Advanced] (OpenAI) How would you scale training of a multimodal model (like GPT-4V) across thousands of GPUs? Discuss parallelism, memory, and communication.
585. [Advanced] (NVIDIA) Explain how Tensor Cores work and how they accelerate mixed-precision matrix multiplication.
586. [Advanced] (Apple) Design an on-device image segmentation model for iPhone. Constraints: <30ms latency, <100MB model size.
587. [Advanced] (Amazon) How would you build a visual product recommendation system? Walk through the ML pipeline from data to deployment.
588. [Expert] (DeepMind) Explain how AlphaFold uses deep learning for protein structure prediction. What training techniques enable it?
589. [Expert] (Anthropic) How do you ensure training stability when scaling up a foundation model? What monitoring and interventions do you use?
590. [Expert] (Microsoft) Design a training infrastructure for training multiple large models concurrently on a shared cluster of 10,000 GPUs.

### A.10 Rapid Fire Questions

591. [Basic] What does CNN stand for?
592. [Basic] What does ReLU stand for?
593. [Basic] What is the default learning rate for Adam in most frameworks?
594. [Basic] What is the typical β1 and β2 in Adam?
595. [Basic] What does "stride" mean in convolution?
596. [Basic] What does IoU stand for in object detection?
597. [Intermediate] What is the receptive field of a single 3×3 conv layer?
598. [Intermediate] If you have a 224×224 input and apply a 7×7 conv with stride 2 and padding 3, what is the output size?
599. [Intermediate] How many parameters does a conv layer with 64 input channels, 128 output channels, and 3×3 kernel have?
600. [Intermediate] What is the memory ratio of FP16 vs FP32 for the same model?
601. [Intermediate] In ZeRO Stage 1, what is sharded across GPUs?
602. [Advanced] What is the computational complexity of self-attention with respect to sequence length?
603. [Advanced] What is FlashAttention and why is it faster than standard attention?
604. [Advanced] How many bytes does an Adam optimizer state consume per parameter in FP32?
605. [Expert] What is the theoretical communication volume for an all-reduce operation on N GPUs with M bytes of data?
606. [Expert] What is the pipeline bubble fraction for a pipeline with P stages and M microbatches?

---

> **Total: 606 questions** across Deep Learning Foundations (173), CNNs & Computer Vision (153), Training Deep Networks (160), and Cross-Cutting/Appendix (120).
>
> Sources: Compiled from real interview questions reported at Google, Meta, Amazon, Apple, NVIDIA, OpenAI, DeepMind, Microsoft, Tesla, and other top AI companies (2023-2025), academic deep learning courses (Stanford CS231n, MIT 6.S191, fast.ai), and industry preparation resources.
