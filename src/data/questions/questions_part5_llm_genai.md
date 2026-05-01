# Part 5: LLMs, Generative AI & AI Agents

> 600+ interview questions covering Large Language Models, Generative Models, and RAG/AI Agents
> Difficulty levels: [Basic] [Intermediate] [Advanced] [Expert]

---

## 13. Large Language Models

### 13.1 LLM Fundamentals

**Core Concepts**

1. [Basic] What is a Large Language Model (LLM)? How does it differ from traditional NLP models?
2. [Basic] Explain the transformer architecture and why it is essential for LLMs.
3. [Basic] What is tokenization, and why does it matter for LLM performance?
4. [Basic] What is the "context window" of an LLM, and how does it affect performance?
5. [Basic] Describe the difference between encoder-only, decoder-only, and encoder-decoder transformer architectures. Give examples of each.
6. [Basic] What is the difference between autoregressive and autoencoding language models?
7. [Basic] What are the key hyperparameters of an LLM (model size, attention heads, layers, hidden dimensions)?
8. [Basic] Explain positional encoding. Why do transformers need it?
9. [Basic] Describe the self-attention mechanism in transformers. What is the computational complexity?
10. [Basic] What is the softmax bottleneck in language modeling, and how does it affect output quality?
11. [Intermediate] Compare and contrast GPT, BERT, and T5 architectures. When would you use each?
12. [Intermediate] Explain multi-head attention. Why use multiple heads instead of a single attention mechanism?
13. [Intermediate] What is the difference between absolute, relative, and rotary positional embeddings (RoPE)?
14. [Intermediate] Explain ALiBi (Attention with Linear Biases). How does it handle extrapolation to longer sequences?
15. [Intermediate] What are embedding layers, and how do they transform discrete tokens into continuous representations?
16. [Intermediate] Explain causal masking in decoder-only models. Why is it necessary for autoregressive generation?
17. [Intermediate] What is the difference between sparse attention and dense attention? Give examples of sparse attention patterns.
18. [Intermediate] Describe FlashAttention. How does it achieve better memory efficiency and speed?
19. [Advanced] Derive the scaled dot-product attention formula. Why do we scale by √d_k?
20. [Advanced] Explain the relationship between perplexity and cross-entropy loss in language modeling.
21. [Advanced] What is the theoretical maximum context length a transformer can handle, and what are the practical bottlenecks?
22. [Advanced] Explain the connection between attention mechanisms and kernel methods.

**Pretraining**

23. [Basic] What is pretraining in the context of LLMs? What objective functions are typically used?
24. [Basic] What is the next-token prediction objective? How does it enable general language understanding?
25. [Basic] What is masked language modeling (MLM)? How does it differ from causal language modeling?
26. [Intermediate] What types of data are used for pretraining LLMs? How does data composition affect model capabilities?
27. [Intermediate] Explain the role of data deduplication in pretraining. What happens if you don't deduplicate?
28. [Intermediate] What is curriculum learning in the context of LLM pretraining?
29. [Intermediate] How does data quality filtering work during pretraining? What heuristics are commonly used?
30. [Intermediate] What is the difference between pretraining from scratch vs. continual pretraining?
31. [Advanced] Describe the pretraining pipeline of a modern LLM from data collection to final checkpoint.
32. [Advanced] How do you handle multilingual data during pretraining? What challenges arise?
33. [Advanced] What is the role of learning rate scheduling (warmup, cosine decay) in LLM pretraining?
34. [Expert] Explain how pretraining data contamination affects benchmark evaluations. How can you detect it?

**Scaling Laws & Emergent Abilities**

35. [Intermediate] What are scaling laws in the context of neural networks and LLMs?
36. [Intermediate] Describe the Chinchilla scaling laws. How do they relate model size, dataset size, and compute?
37. [Intermediate] How did Chinchilla's findings differ from earlier scaling assumptions (e.g., GPT-3)?
38. [Intermediate] Why is it suboptimal to simply scale up model parameters without increasing dataset size proportionally?
39. [Intermediate] What are emergent abilities in LLMs? Provide specific examples.
40. [Advanced] Why do certain abilities appear abruptly at specific model scales rather than improving smoothly?
41. [Advanced] How can scaling laws inform budget allocation for training a state-of-the-art LLM?
42. [Advanced] Can you describe the mathematical form of the scaling law (L = aN^α + bD^β + c)?
43. [Advanced] Are all model capabilities emergent, or do some scale predictably? Which tasks tend to be emergent?
44. [Expert] How do scaling laws and emergent abilities challenge our approach to benchmarking LLM performance?
45. [Expert] What risks or unknowns are associated with emergent behaviors as we continue to scale LLMs?
46. [Expert] Discuss the debate around whether emergent abilities are a mirage (Schaeffer et al., 2023). What are the counterarguments?

**Architecture Deep Dives**

47. [Intermediate] What is a decoder-only architecture, and why has it become dominant for LLMs?
48. [Intermediate] Explain Multi-Query Attention (MQA). What problem does it solve?
49. [Intermediate] What is Grouped Query Attention (GQA)? How does it differ from MHA and MQA?
50. [Advanced] Explain the trade-offs between MHA, MQA, and GQA in terms of KV cache memory, parallelism, and quality.
51. [Advanced] What is a Mixture of Experts (MoE) architecture? How does it differ from dense transformers?
52. [Advanced] How does MoE routing (gating) work? What are Top-K routing and expert capacity?
53. [Advanced] What are the challenges of load balancing in MoE models? How is auxiliary loss used?
54. [Advanced] Describe the architecture of Mixtral. How does it achieve efficiency?
55. [Expert] How does MoE token routing impact GPU memory layout and communication overhead in distributed inference?
56. [Expert] Explain the Switch Transformer architecture. How does it simplify MoE?
57. [Expert] How does the presence of multiple experts impact KV cache design?
58. [Expert] Describe the Mamba architecture (state space models). How does it compare to transformers?
59. [Expert] What are linear attention mechanisms? How do they achieve O(n) complexity?
60. [Expert] Explain the RWKV architecture. How does it combine RNN and transformer properties?

---

### 13.2 Training & Alignment

**Pretraining Strategies**

61. [Basic] What is transfer learning, and how is it applied in LLMs?
62. [Basic] Explain the difference between pretraining and fine-tuning.
63. [Intermediate] What are common optimization strategies for training LLMs (Adam, AdamW, Adafactor)?
64. [Intermediate] Describe gradient checkpointing. Why is it used during training?
65. [Intermediate] What is mixed-precision training (FP16, BF16)? Why is BF16 preferred for LLM training?
66. [Intermediate] Explain data parallelism, tensor parallelism, and pipeline parallelism for distributed training.
67. [Advanced] What is ZeRO (Zero Redundancy Optimizer)? Describe ZeRO stages 1, 2, and 3.
68. [Advanced] Explain FSDP (Fully Sharded Data Parallelism). How does it compare to ZeRO?
69. [Advanced] What is gradient accumulation, and when is it necessary?
70. [Advanced] Describe the challenges of training instabilities in large-scale models. How are they mitigated?
71. [Expert] Design the distributed training infrastructure for a 70B parameter model. What hardware and software choices would you make?

**RLHF (Reinforcement Learning from Human Feedback)**

72. [Basic] What is RLHF? Why is human feedback important for aligning LLMs?
73. [Basic] Describe the three stages of the RLHF pipeline: SFT, reward modeling, and RL optimization.
74. [Intermediate] How is a reward model trained in RLHF? What data format does it require?
75. [Intermediate] Explain PPO (Proximal Policy Optimization) in the context of RLHF. Why is it preferred?
76. [Intermediate] What is the KL divergence penalty in RLHF, and why is it important?
77. [Intermediate] What are common challenges when collecting human feedback for training LLMs?
78. [Intermediate] How would you address bias or inconsistency in human feedback datasets?
79. [Advanced] Write pseudocode for reward model training from human preference pairs.
80. [Advanced] Compare RLHF with traditional RL that uses well-defined reward functions. What are the key differences?
81. [Advanced] What is reward hacking/overoptimization in RLHF? How can you detect and mitigate it?
82. [Advanced] Explain the concept of "Goodhart's Law" in the context of reward modeling.
83. [Expert] Discuss the tradeoffs between sample efficiency and alignment quality in RLHF.
84. [Expert] How would you design a human annotation pipeline for RLHF at scale? What quality controls are needed?

**DPO (Direct Preference Optimization)**

85. [Intermediate] What is DPO, and how does it differ from RLHF via PPO?
86. [Intermediate] What loss function does DPO use? Explain the intuition behind it.
87. [Advanced] Derive the DPO loss function from the RLHF objective. Show how it eliminates the need for a separate reward model.
88. [Advanced] What are potential failure modes of DPO?
89. [Advanced] How do you handle noisy or ambiguous human preferences in DPO?
90. [Advanced] How would you empirically evaluate a DPO-trained LLM against an RLHF-trained one?
91. [Expert] Compare DPO, IPO (Identity Preference Optimization), and KTO (Kahneman-Tversky Optimization). What are their relative strengths?
92. [Expert] What is the relationship between the DPO loss and the Bradley-Terry model?

**GRPO & Other Alignment Methods**

93. [Advanced] What is GRPO (Group Relative Policy Optimization)? How does it differ from PPO and DPO?
94. [Advanced] How does GRPO incorporate group-level comparison instead of pairwise preferences?
95. [Advanced] Explain the GRPO objective function and how it handles uncertainty in reward signals.
96. [Expert] How does DeepSeek-R1 use GRPO for training? What results did it achieve?
97. [Expert] Compare sample efficiency of GRPO vs PPO vs DPO for LLM alignment.

**Constitutional AI**

98. [Intermediate] What is Constitutional AI (CAI)? How does it differ from standard RLHF?
99. [Intermediate] How does CAI reduce reliance on human feedback?
100. [Advanced] Describe how you would design a "constitution" (set of principles) for an AI assistant.
101. [Advanced] What are the challenges in ensuring constitutional rules are robust and interpretable?
102. [Advanced] Describe a failure mode where a constitutional approach might not prevent misalignment.
103. [Expert] How does RLAIF (RL from AI Feedback) work in Constitutional AI? What are its limitations?

**Reward Modeling**

104. [Intermediate] What is reward modeling, and why is it essential for AI alignment?
105. [Intermediate] How do you train a reward model from human preference data?
106. [Advanced] How would you detect reward hacking vs. genuine reward pursuit in a trained model?
107. [Advanced] What techniques ensure robustness of a reward model against adversarial manipulation?
108. [Advanced] Explain Inverse Reinforcement Learning (IRL) and its relevance to reward modeling.
109. [Advanced] How does sparse vs. dense feedback affect exploration and alignment?
110. [Expert] Explain process reward models vs. outcome reward models. When would you use each?
111. [Expert] How do you scale reward modeling when the task requires expert-level knowledge?

**General Alignment**

112. [Intermediate] What is model alignment, and why is it critical for LLMs?
113. [Intermediate] Explain "outer alignment" vs. "inner alignment."
114. [Advanced] What alignment problems are unique to LLMs compared to other AI systems?
115. [Advanced] Describe a scenario where an aligned model may still act in a misaligned way.
116. [Advanced] What is scalable oversight, and why is it critical for advanced AI systems?
117. [Expert] Discuss the risk of mesa-optimizers and how you would detect them.
118. [Expert] How would you quantitatively and qualitatively evaluate model alignment?
119. [Expert] What is the "alignment tax"? How do you balance capability and safety?

---

### 13.3 Fine-tuning & PEFT

**Full Fine-tuning**

120. [Basic] What is fine-tuning, and when would you use it instead of prompting?
121. [Basic] Explain the difference between full fine-tuning, feature-based transfer learning, and parameter-efficient fine-tuning.
122. [Intermediate] What is catastrophic forgetting during fine-tuning? How can you mitigate it?
123. [Intermediate] What are common challenges encountered during fine-tuning of large models?
124. [Intermediate] How do you select the learning rate and number of epochs for fine-tuning?
125. [Advanced] When should you fine-tune vs. use RAG vs. use in-context learning?
126. [Advanced] How does instruction tuning differ from task-specific fine-tuning?
127. [Advanced] What is the difference between SFT (Supervised Fine-Tuning) data formats: instruction-following, chat, and completion?

**LoRA (Low-Rank Adaptation)**

128. [Basic] What is LoRA, and what problem does it solve?
129. [Intermediate] Explain how LoRA reduces the number of trainable parameters during fine-tuning.
130. [Intermediate] Describe the process of injecting LoRA modules into a transformer layer. Where are they typically inserted?
131. [Intermediate] How does the rank parameter (r) affect performance and efficiency in LoRA?
132. [Intermediate] What are the advantages of LoRA over traditional full-model fine-tuning?
133. [Advanced] What is the mathematical formulation of LoRA? Express W = W₀ + BA where B ∈ R^(d×r) and A ∈ R^(r×k).
134. [Advanced] How do you merge LoRA weights back into the base model for inference?
135. [Advanced] Can you stack multiple LoRA adapters? What are the challenges?
136. [Advanced] Discuss limitations of LoRA. In what scenarios does it underperform full fine-tuning?
137. [Expert] How does DoRA (Weight-Decomposed Low-Rank Adaptation) improve upon standard LoRA?
138. [Expert] Explain LoRA+ and its modifications to the learning rate scheme.

**QLoRA**

139. [Intermediate] What is QLoRA, and how does it differ from standard LoRA?
140. [Intermediate] Explain the quantization technique used in QLoRA (NF4 data type).
141. [Intermediate] How does QLoRA allow fine-tuning of 65B+ parameter models on a single GPU?
142. [Advanced] What is double quantization in QLoRA? How does it further reduce memory?
143. [Advanced] Discuss the trade-offs between model quality and quantization level in QLoRA.
144. [Advanced] When would you choose QLoRA over LoRA? What are the key hyperparameters to tune?
145. [Expert] How does paged optimizers work in QLoRA to handle memory spikes?

**Other PEFT Methods**

146. [Basic] What is Parameter-Efficient Fine-Tuning (PEFT)? Why is it important for LLMs?
147. [Intermediate] Compare and contrast PEFT strategies: adapters, LoRA, prompt-tuning, and prefix-tuning.
148. [Intermediate] What are adapter layers? Where are they inserted in the transformer architecture?
149. [Intermediate] Explain prefix tuning. How does it differ from prompt tuning?
150. [Intermediate] What is soft prompt tuning? How does it work?
151. [Advanced] How does (IA)³ (Infused Adapter by Inhibiting and Amplifying Inner Activations) work?
152. [Advanced] Compare the memory footprint of LoRA, adapters, prefix-tuning, and prompt-tuning.
153. [Advanced] How does PEFT impact downstream task adaptation and model deployment?
154. [Advanced] How can the Hugging Face PEFT library be used to implement these techniques?
155. [Expert] How does PEFT help in federated or privacy-preserving learning scenarios?
156. [Expert] Design a multi-task serving system that uses different LoRA adapters for different tasks on a single base model.
157. [Expert] What are the latest developments in PEFT methods (2024-2025)?

**Practical Fine-tuning**

158. [Intermediate] Describe the end-to-end pipeline for PEFT fine-tuning and evaluation.
159. [Intermediate] How do you prepare and format instruction-tuning datasets?
160. [Intermediate] What metrics would you monitor to evaluate the effectiveness of a PEFT method?
161. [Advanced] How do you handle domain-specific fine-tuning when labeled data is scarce?
162. [Advanced] What are safety and bias considerations when fine-tuning language models?
163. [Advanced] How do you save and load only the PEFT weights for efficient deployment?
164. [Expert] Design a continuous fine-tuning pipeline that adapts to new data without forgetting previous knowledge.

---

### 13.4 Inference Optimization

**Decoding Strategies**

165. [Basic] Compare greedy decoding, beam search, top-k sampling, and nucleus (top-p) sampling.
166. [Basic] What is the temperature parameter in LLM generation? How does it affect outputs?
167. [Basic] What are stop sequences or stopping criteria?
168. [Intermediate] Explain the trade-offs between diversity and quality in different decoding strategies.
169. [Intermediate] What is repetition penalty, and how does it prevent degenerate outputs?
170. [Intermediate] How do you set optimal decoding parameters for different use cases (creative writing vs. code generation)?
171. [Advanced] Explain contrastive decoding. How does it improve generation quality?
172. [Advanced] What is Minimum Bayes Risk (MBR) decoding?

**KV Cache**

173. [Basic] What is a KV cache in transformer-based language models? Why is it important?
174. [Intermediate] Explain how the KV cache improves inference speed in autoregressive decoders.
175. [Intermediate] Given a prompt of 1000 tokens generating 10 more tokens, how does the KV cache help?
176. [Intermediate] How does GPU memory footprint scale with KV cache size?
177. [Advanced] How do you manage KV cache in batch inference with different sequence lengths?
178. [Advanced] What challenges arise in updating KV cache during prefix-tuning or sequence editing?
179. [Advanced] Explain PagedAttention (vLLM). How does it optimize KV cache memory management?
180. [Advanced] What is KV cache compression? Describe techniques like quantized KV cache and sliding window attention.
181. [Expert] How does Multi-Query Attention reduce KV cache memory? Quantify the savings.
182. [Expert] Design an efficient KV cache management system for serving models with 128K+ context windows.

**Speculative Decoding**

183. [Intermediate] What is speculative decoding? Why does it speed up LLM inference?
184. [Intermediate] How does speculative decoding work with a draft model and a target model?
185. [Advanced] What are the correctness guarantees of speculative decoding? Prove that it doesn't change the output distribution.
186. [Advanced] What are the tradeoffs (acceptance rate, latency, throughput) in speculative decoding?
187. [Advanced] How does speculative decoding interact with the KV cache?
188. [Expert] When does speculative decoding fail to provide speedups? What factors determine the optimal draft model size?
189. [Expert] Explain Medusa: multi-head speculative decoding without a separate draft model.

**Quantization**

190. [Basic] What is model quantization? Why is it important for LLM deployment?
191. [Intermediate] Explain the differences between INT8, INT4, FP8, and NF4 quantization.
192. [Intermediate] Compare weight-only, activation-only, and full (weights + activations) quantization.
193. [Intermediate] What are the tradeoffs between model size, speed, and accuracy in quantization?
194. [Advanced] What is GPTQ? Explain its layer-wise quantization approach.
195. [Advanced] What is AWQ (Activation-Aware Weight Quantization)? How does it differ from GPTQ?
196. [Advanced] Explain GGUF format. What advantages does it offer for CPU/edge deployment?
197. [Advanced] What is quantization-aware training (QAT) vs. post-training quantization (PTQ)?
198. [Advanced] Describe SmoothQuant. How does it handle activation outliers?
199. [Expert] How do you assess if a quantized model is "good enough" for production? What evaluation methodology do you use?
200. [Expert] Explain the mathematical basis for round-to-nearest vs. optimal brain quantization.
201. [Expert] How can quantization both help and hinder memory bandwidth utilization?

**General Inference Optimization**

202. [Intermediate] Explain continuous batching. How does it differ from static batching?
203. [Intermediate] What is model distillation for inference? How does it differ from quantization?
204. [Intermediate] Describe tensor parallelism for inference. How do you shard a model across GPUs?
205. [Advanced] Compare vLLM, TGI (Text Generation Inference), and TensorRT-LLM for serving.
206. [Advanced] What are the biggest bottlenecks in LLM inference at scale (compute-bound vs. memory-bound)?
207. [Advanced] Explain the roofline model for analyzing LLM inference performance.
208. [Advanced] How does model pruning work for inference acceleration?
209. [Expert] Design an LLM serving infrastructure that can handle 10,000 QPS with P99 latency < 200ms.
210. [Expert] How would you combine quantization, KV caching, speculative decoding, and continuous batching for optimal throughput?
211. [Expert] Explain prefix caching. How can shared prompt prefixes be exploited for efficiency?
212. [Expert] What is disaggregated serving (separating prefill and decode phases)? Why is it beneficial?

---

### 13.5 Prompting Techniques

**Basic Prompting**

213. [Basic] What is prompt engineering? Why is it important for LLM applications?
214. [Basic] Explain zero-shot prompting. When does it work well?
215. [Basic] What is few-shot (in-context) learning? How do you select effective examples?
216. [Basic] What are system prompts, and how do they influence model behavior?
217. [Intermediate] How does the order and format of few-shot examples affect LLM performance?
218. [Intermediate] What is prompt sensitivity? How do you design robust prompts?
219. [Intermediate] Explain the difference between instruction-based and completion-based prompting.

**Advanced Prompting**

220. [Intermediate] What is Chain-of-Thought (CoT) prompting? How does it improve LLM reasoning?
221. [Intermediate] Explain zero-shot CoT ("Let's think step by step"). When is it effective?
222. [Intermediate] What is self-consistency in prompting? How does it use majority voting?
223. [Advanced] Describe Tree-of-Thought (ToT) prompting. How does it differ from CoT?
224. [Advanced] What is Graph-of-Thought prompting?
225. [Advanced] Explain ReAct (Reasoning + Acting) prompting. How does it combine reasoning with tool use?
226. [Advanced] What is self-reflection/self-critique prompting? How can an LLM improve its own outputs?
227. [Advanced] Describe least-to-most prompting. How does it handle complex, multi-step problems?
228. [Advanced] What is prompt chaining? How do you decompose complex tasks into prompt sequences?
229. [Expert] Compare CoT, ToT, and self-consistency in terms of accuracy, latency, and cost for mathematical reasoning.
230. [Expert] How do you automatically optimize prompts? Describe DSPy or similar frameworks.
231. [Expert] What is meta-prompting? How can LLMs be used to generate better prompts?

**Prompt Safety**

232. [Intermediate] What is prompt injection? How can it be prevented?
233. [Intermediate] How do you assess prompt robustness against adversarial inputs?
234. [Advanced] Describe common jailbreaking techniques used against LLMs.
235. [Advanced] How do you design a system-level defense against prompt injection attacks?

---

### 13.6 Evaluation & Benchmarks

236. [Basic] What is perplexity? How is it used to evaluate language models?
237. [Basic] What are BLEU and ROUGE scores? When is each appropriate?
238. [Basic] How do you evaluate an LLM's performance on generation tasks?
239. [Intermediate] Describe the MMLU benchmark. What capabilities does it measure?
240. [Intermediate] What is HumanEval? How does it evaluate code generation?
241. [Intermediate] Explain the difference between automatic metrics and human evaluation for LLMs.
242. [Intermediate] What are the limitations of perplexity as an evaluation metric?
243. [Intermediate] Describe LLM-as-a-judge evaluation. What are its advantages and pitfalls?
244. [Advanced] How do you design a comprehensive evaluation suite for an LLM-based product?
245. [Advanced] What is benchmark contamination? How can you detect if a model has seen test data during training?
246. [Advanced] Describe ELO rating systems for comparing LLMs (e.g., Chatbot Arena).
247. [Advanced] What are the key evaluation dimensions: helpfulness, harmlessness, honesty? How do you measure each?
248. [Expert] Design an evaluation framework that captures both capability and safety for a production LLM.
249. [Expert] How do you evaluate multi-turn conversation quality? What metrics capture coherence and context retention?
250. [Expert] What are dynamic benchmarks, and why are they important as models improve?
251. [Expert] Critique common LLM leaderboards. What do they miss?

---

### 13.7 Safety & Responsible AI

252. [Basic] What is hallucination in LLMs? Why does it occur?
253. [Basic] What strategies can reduce hallucinations in LLM outputs?
254. [Intermediate] How would you evaluate hallucination rate quantitatively and qualitatively?
255. [Intermediate] Can RAG help minimize hallucinations? Explain the mechanism.
256. [Intermediate] Design an experiment to test the factuality of LLM outputs on a novel domain.
257. [Intermediate] What is toxicity in LLM outputs? How is it measured?
258. [Intermediate] How do you detect and mitigate bias in LLMs?
259. [Advanced] What is "jailbreaking" in the context of LLMs? Give examples of techniques.
260. [Advanced] How can you design prompts or systems robust against jailbreaking attempts?
261. [Advanced] What is red teaming for LLMs? How does it differ from traditional software red teaming?
262. [Advanced] How can synthetic adversarial prompts improve LLM robustness?
263. [Advanced] What tools and frameworks exist for automated LLM safety evaluation?
264. [Advanced] Describe the difference between technical and social mitigations for LLM safety.
265. [Expert] Design a comprehensive red teaming exercise for a production LLM. What metrics and reporting would you use?
266. [Expert] What regulatory frameworks (EU AI Act, NIST AI RMF) influence LLM safety practices?
267. [Expert] How would you build a real-time content safety filter for LLM outputs at scale?
268. [Expert] What are watermarking techniques for LLM-generated text? How do they work?
269. [Expert] Discuss the tradeoff between preventing jailbreaking and maintaining legitimate user utility.
270. [Expert] How do you handle multi-modal safety concerns (text + image generation)?

---

## 14. Generative Models

### 14.1 Autoencoders

**Vanilla Autoencoders**

271. [Basic] What is an autoencoder? Describe the encoder-decoder structure.
272. [Basic] What is the purpose of the bottleneck (latent space) in an autoencoder?
273. [Basic] What loss function is typically used for training autoencoders?
274. [Intermediate] What is the difference between undercomplete and overcomplete autoencoders?
275. [Intermediate] Explain denoising autoencoders. How does adding noise improve representation learning?
276. [Intermediate] What is a sparse autoencoder? How does the sparsity constraint help?
277. [Intermediate] How are autoencoders used for dimensionality reduction? Compare with PCA.
278. [Advanced] What is a contractive autoencoder? How does the Jacobian penalty work?
279. [Advanced] Explain how autoencoders can be used for anomaly detection.

**Variational Autoencoders (VAE)**

280. [Basic] What is a Variational Autoencoder (VAE)? How does it differ from a vanilla autoencoder?
281. [Intermediate] Explain the Evidence Lower Bound (ELBO) in VAE training. Derive it from first principles.
282. [Intermediate] Why is the KL divergence used in VAEs? What is its role in the loss function?
283. [Intermediate] Explain the reparameterization trick. Why is it necessary for backpropagation through stochastic nodes?
284. [Intermediate] Why do VAEs tend to generate blurry images compared to GANs?
285. [Intermediate] What is posterior collapse in VAEs? How can you mitigate it?
286. [Advanced] Derive the full ELBO objective: E[log p(x|z)] - KL(q(z|x) || p(z)). Explain each term.
287. [Advanced] What is β-VAE? How does the β hyperparameter affect disentangled representations?
288. [Advanced] Describe hierarchical VAEs (NVAE, VDVAE). What benefits do they offer?
289. [Advanced] Explain VQ-VAE (Vector Quantized VAE). How does discrete latent space modeling work?
290. [Advanced] How is VQ-VAE-2 used as a component in modern image generation pipelines?
291. [Expert] Compare the ELBO tightness of different variational inference methods (mean-field, normalizing flow posterior).
292. [Expert] How do importance-weighted autoencoders (IWAE) improve upon the standard VAE bound?
293. [Expert] Describe how VAE-based models are used in drug discovery and molecular generation.

### 14.2 Generative Adversarial Networks (GANs)

**GAN Fundamentals**

294. [Basic] What is a GAN? Describe the roles of the generator and discriminator.
295. [Basic] Explain the minimax game formulation of GANs.
296. [Basic] What is the training process of a classical GAN?
297. [Intermediate] What is mode collapse in GANs? How can it be detected?
298. [Intermediate] What strategies mitigate mode collapse (minibatch discrimination, unrolled GANs)?
299. [Intermediate] What is training instability in GANs? Why do generator and discriminator training need to be balanced?
300. [Intermediate] Explain the challenges of evaluating GAN-generated samples.
301. [Intermediate] What are FID (Fréchet Inception Distance) and IS (Inception Score)? How do they measure generation quality?
302. [Advanced] Derive the optimal discriminator for the original GAN objective.
303. [Advanced] Show that the GAN objective minimizes the Jensen-Shannon divergence between real and generated distributions.
304. [Advanced] What is the vanishing gradient problem in GAN training? How does it relate to the discriminator being too strong?

**GAN Variants**

305. [Intermediate] What is a Conditional GAN (cGAN)? How does conditioning change the architecture?
306. [Intermediate] Explain Wasserstein GAN (WGAN). What improvements does the Wasserstein loss bring?
307. [Intermediate] What is the gradient penalty in WGAN-GP? Why is weight clipping problematic?
308. [Advanced] Describe the Wasserstein distance (Earth Mover's distance) mathematically. Why is it a better training signal?
309. [Advanced] Explain spectral normalization. How does it stabilize GAN training?
310. [Advanced] What is Progressive GAN? How does progressive growing of layers help?
311. [Advanced] Describe StyleGAN and StyleGAN2. What innovations did they introduce for controllable generation?
312. [Advanced] What is CycleGAN? How does cycle consistency loss enable unpaired image-to-image translation?
313. [Advanced] Explain Pix2Pix. How does it perform paired image-to-image translation?
314. [Expert] Compare LSGAN, WGAN, WGAN-GP, and hinge loss GANs. When would you use each?
315. [Expert] How do GANs compare to diffusion models in terms of sample quality, diversity, and training stability?
316. [Expert] What is GAN inversion? How do you find the latent code corresponding to a real image?
317. [Expert] Describe the theoretical convergence properties of GANs. Under what conditions do they converge?

### 14.3 Diffusion Models

**DDPM (Denoising Diffusion Probabilistic Models)**

318. [Basic] What is the fundamental intuition behind diffusion models?
319. [Basic] Describe the forward (noising) and reverse (denoising) processes in DDPM.
320. [Intermediate] Write the mathematical formulation of the forward diffusion process. What assumptions are made?
321. [Intermediate] Explain the reverse process in DDPM and how the model learns to denoise.
322. [Intermediate] What is a variance/noise schedule? Why is it important?
323. [Intermediate] How does the DDPM training objective relate to denoising score matching?
324. [Intermediate] Why are diffusion models less prone to mode collapse compared to GANs?
325. [Advanced] Derive the ELBO (variational lower bound) for DDPM. Show how it decomposes into reconstruction and KL terms.
326. [Advanced] Explain the simplified training objective (ε-prediction). Why does predicting noise work?
327. [Advanced] What is the connection between the score function ∇_x log p(x) and the denoising objective?
328. [Advanced] How does parameterizing noise prediction vs. mean prediction vs. velocity prediction differ?
329. [Expert] Derive the closed-form expression for q(x_t | x_0) using the reparameterization trick and cumulative noise schedule.
330. [Expert] Explain continuous-time diffusion models and their connection to SDEs (Stochastic Differential Equations).

**DDIM & Accelerated Sampling**

331. [Intermediate] How does DDIM differ from DDPM conceptually and technically?
332. [Intermediate] What makes DDIM sampling deterministic? How does it enable fewer diffusion steps?
333. [Advanced] Derive the DDIM sampling formula. How does the η parameter control stochasticity?
334. [Advanced] How does DDIM enable meaningful latent space interpolation?
335. [Advanced] What is DPM-Solver? How does it accelerate sampling?
336. [Expert] Compare DDPM, DDIM, and DPM-Solver++ in terms of sample quality vs. number of function evaluations.
337. [Expert] Explain consistency models (Song et al., 2023). How do they enable single-step generation?

**Score Matching & Theory**

338. [Intermediate] What is score matching? How is it related to diffusion models?
339. [Advanced] Describe the "denoising score matching" objective. Connect it to ε-prediction.
340. [Advanced] Compare maximum likelihood estimation (MLE) and score matching in generative modeling.
341. [Advanced] Explain the connection between SDEs, score-based models, and diffusion models.
342. [Expert] How do you evaluate the likelihood of data under a trained diffusion model?
343. [Expert] Describe the probability flow ODE. Why is it useful for exact likelihood computation?

**Conditioning & Guidance**

344. [Intermediate] How do you condition a diffusion model on class labels or text?
345. [Intermediate] What is classifier guidance? How does it use an external classifier to steer generation?
346. [Advanced] What is classifier-free guidance (CFG)? How does it work mathematically?
347. [Advanced] Why has CFG become the dominant conditioning method? What is the guidance scale parameter?
348. [Expert] Explain negative prompting in diffusion models. How is it implemented via CFG?
349. [Expert] What is ControlNet? How does it add spatial conditioning to pretrained diffusion models?

**Stable Diffusion & Architecture**

350. [Basic] What is Stable Diffusion? How does it differ from pixel-space diffusion models?
351. [Intermediate] Explain the latent diffusion model (LDM) architecture. What is the role of the VAE encoder/decoder?
352. [Intermediate] How does the U-Net architecture integrate with diffusion models?
353. [Intermediate] How does CLIP guidance enable text-to-image generation in Stable Diffusion?
354. [Intermediate] What role does the text encoder (CLIP/T5) play in the generation process?
355. [Advanced] Describe DALL-E's architecture. How does it use a discrete VAE (dVAE)?
356. [Advanced] How does DALL-E 2 use CLIP embeddings and a diffusion prior?
357. [Advanced] Compare DALL-E 2, Stable Diffusion, Imagen, and Midjourney at an architectural level.
358. [Advanced] What is SDXL? What architectural improvements does it introduce?
359. [Expert] Explain Stable Diffusion 3's MMDiT (Multi-Modal Diffusion Transformer) architecture.
360. [Expert] How do DiT (Diffusion Transformers) replace U-Nets? What advantages do they offer?
361. [Expert] Describe the architecture of Flux. How does it improve upon previous diffusion models?

### 14.4 Flow Models

**Normalizing Flows**

362. [Intermediate] What is a normalizing flow? Explain the core idea.
363. [Intermediate] How do you ensure invertibility in normalizing flow transformations?
364. [Intermediate] Why is the Jacobian determinant important in training normalizing flows?
365. [Advanced] What base distributions are commonly used, and why?
366. [Advanced] Describe RealNVP. How do affine coupling layers work?
367. [Advanced] Explain Glow architecture. What improvements does it offer over RealNVP?
368. [Advanced] What are autoregressive flows (e.g., MAF, IAF)? How do they trade off training vs. sampling speed?
369. [Expert] Compare normalizing flows with VAEs and diffusion models in terms of exact likelihood computation.
370. [Expert] What are continuous normalizing flows (CNFs)? How do they relate to neural ODEs?

**Flow Matching**

371. [Advanced] What is flow matching? How is it different from standard normalizing flows?
372. [Advanced] How does flow matching relate to probability path sampling in diffusion models?
373. [Advanced] Explain conditional flow matching (CFM). Why is it more practical than vanilla flow matching?
374. [Expert] How does Stable Diffusion 3 use flow matching instead of traditional diffusion?
375. [Expert] Compare flow matching, score matching, and denoising diffusion in terms of training objectives and sample quality.
376. [Expert] What is rectified flow? How does it create straight-line trajectories for faster sampling?

### 14.5 Image, Video & Audio Generation

**Image Generation**

377. [Intermediate] Describe the complete pipeline for text-to-image generation using Stable Diffusion.
378. [Intermediate] What is image inpainting with diffusion models? How does it work?
379. [Intermediate] Explain image-to-image translation (img2img) with diffusion models.
380. [Advanced] What is textual inversion? How does it learn new concepts from a few images?
381. [Advanced] Explain DreamBooth. How does it fine-tune diffusion models for personalization?
382. [Advanced] What is LoRA for diffusion models? How does it enable efficient style adaptation?
383. [Expert] Design a production image generation system. What components, models, and safety filters would you include?

**Video Generation**

384. [Intermediate] What are the key challenges in video generation compared to image generation?
385. [Intermediate] How do temporal consistency and coherence work in video diffusion models?
386. [Advanced] Describe the architecture of video generation models (e.g., Sora, Runway, Kling concepts).
387. [Advanced] What is temporal attention, and how does it extend image diffusion to video?
388. [Expert] How do modern video generation models handle long-duration temporal coherence?
389. [Expert] What are the compute requirements for video generation vs. image generation?

**Audio Generation**

390. [Intermediate] How are diffusion models applied to audio/music generation?
391. [Intermediate] Describe the architecture of text-to-speech models using diffusion (e.g., Tortoise TTS).
392. [Advanced] How do mel-spectrogram diffusion models work?
393. [Advanced] What is AudioLDM? How does it apply latent diffusion to audio?
394. [Expert] Compare autoregressive vs. diffusion-based approaches for music generation.

### 14.6 Generative Models - Theory & Comparison

395. [Intermediate] Compare and contrast VAEs, GANs, diffusion models, and normalizing flows in a table format.
396. [Intermediate] What are the practical tradeoffs between these generative model families?
397. [Advanced] How would you combine VAEs and GANs in a hybrid model? What advantages does it offer?
398. [Advanced] Explain latent space interpolation in generative models. How is it performed?
399. [Advanced] Contrast how overfitting manifests in discriminative vs. generative models.
400. [Advanced] What is the FID-CLIP tradeoff in text-to-image models?
401. [Expert] How do energy-based models relate to other generative model families?
402. [Expert] What are the theoretical connections between score matching, diffusion, and normalizing flows?
403. [Expert] Discuss the "Modes, Memorization, and Generalization" tradeoff in generative models.
404. [Expert] What ethical considerations arise when deploying generative models (deepfakes, copyright, consent)?
405. [Expert] How do you detect AI-generated images? What are current forensic techniques?

**Evaluation of Generative Models**

406. [Intermediate] How do you evaluate the quality of generated samples? Name at least five metrics.
407. [Intermediate] What is FID (Fréchet Inception Distance)? How is it computed?
408. [Intermediate] What is Inception Score (IS)? What are its limitations?
409. [Advanced] Explain LPIPS (Learned Perceptual Image Patch Similarity).
410. [Advanced] How do you evaluate diversity vs. quality tradeoffs in generative models?
411. [Advanced] What is the CLIP score for text-image alignment evaluation?
412. [Expert] Design a comprehensive evaluation pipeline for a text-to-image generative model.

---

## 15. RAG & AI Agents

### 15.1 RAG Fundamentals

**Core Concepts**

413. [Basic] What is Retrieval-Augmented Generation (RAG)? Explain the motivation behind it.
414. [Basic] What are the key components of a RAG system?
415. [Basic] How does RAG differ from pure generative models or pure retrieval systems?
416. [Basic] When would you use RAG vs. fine-tuning vs. in-context learning?
417. [Intermediate] Describe a typical RAG workflow for question answering end-to-end.
418. [Intermediate] What are the advantages of RAG over fine-tuning for knowledge-intensive tasks?
419. [Intermediate] What are common failure modes of RAG systems?
420. [Intermediate] How do you evaluate a RAG system? What metrics would you use?
421. [Advanced] Compare naive RAG, advanced RAG, and modular RAG architectures.
422. [Advanced] What is the "lost in the middle" problem in RAG? How do you mitigate it?
423. [Expert] Design a production RAG system. What components and tradeoffs would you consider?

**Chunking Strategies**

424. [Basic] What is chunking, and why is it important for RAG?
425. [Intermediate] Name and describe different chunking strategies (fixed-size, sentence-level, paragraph-level, semantic).
426. [Intermediate] How does chunk size affect retrieval granularity and generation quality?
427. [Intermediate] What is overlapping/sliding window chunking? When is it beneficial?
428. [Advanced] Explain recursive chunking and hierarchical chunking strategies.
429. [Advanced] How would you handle chunking for structured documents (tables, code, PDFs)?
430. [Advanced] What is semantic chunking? How does it use embeddings to determine chunk boundaries?
431. [Expert] Design a chunking strategy for a corpus of legal documents with cross-references and citations.
432. [Expert] How do you evaluate the optimal chunk size empirically for a given use case?

**Embedding Models**

433. [Basic] What are embeddings? How are they created from text data?
434. [Basic] Explain the difference between static word embeddings and contextual embeddings.
435. [Intermediate] Compare popular embedding models (OpenAI Ada, Sentence-Transformers, Cohere, E5, BGE).
436. [Intermediate] How do you choose embedding dimensionality? What are the tradeoffs?
437. [Intermediate] What is a bi-encoder vs. a cross-encoder? When would you use each?
438. [Advanced] How do you fine-tune embedding models for domain-specific retrieval?
439. [Advanced] Explain contrastive learning for training embedding models (e.g., SimCLR, InfoNCE loss).
440. [Advanced] What is Matryoshka Representation Learning? How does it enable flexible dimensionality?
441. [Expert] How do you evaluate embedding quality for retrieval tasks (recall@k, NDCG, MRR)?
442. [Expert] Design an embedding training pipeline for a specialized medical corpus.

**Vector Databases**

443. [Basic] What is a vector database? Why is it important for RAG?
444. [Intermediate] Compare popular vector databases (Pinecone, Weaviate, Milvus, Qdrant, Chroma, FAISS).
445. [Intermediate] Explain different similarity search algorithms (cosine similarity, dot product, Euclidean distance).
446. [Intermediate] What is approximate nearest neighbor (ANN) search? Describe HNSW and IVF algorithms.
447. [Intermediate] How do you ensure scalability and high availability with a vector database?
448. [Advanced] What are the tradeoffs between recall and latency in ANN search?
449. [Advanced] How do you handle vector database updates when source documents change?
450. [Advanced] What is metadata filtering in vector search? How do you combine it with similarity search?
451. [Expert] Design the indexing and retrieval infrastructure for a RAG system serving millions of documents.
452. [Expert] How do you benchmark vector database performance for your use case?
453. [Expert] What are privacy/security considerations in storing embeddings in vector databases?

### 15.2 Advanced RAG Techniques

**Retrieval Strategies**

454. [Intermediate] What is hybrid search? How does it combine dense and sparse retrieval?
455. [Intermediate] Compare BM25 (sparse) and dense retrieval. When is each better?
456. [Intermediate] What is reciprocal rank fusion (RRF)? How does it combine multiple retrieval methods?
457. [Advanced] Explain query expansion and query rewriting for improving retrieval.
458. [Advanced] What is HyDE (Hypothetical Document Embeddings)? How does it improve retrieval?
459. [Advanced] Describe multi-hop retrieval. When is it necessary?
460. [Advanced] What is self-RAG? How does the model decide when to retrieve?
461. [Expert] How do you implement adaptive retrieval that decides whether to retrieve based on query complexity?

**Reranking**

462. [Intermediate] What is reranking in RAG? Why is a two-stage retrieve-then-rerank pipeline common?
463. [Intermediate] Explain cross-encoder reranking. How does it differ from bi-encoder retrieval?
464. [Advanced] Compare reranking models (Cohere Rerank, BGE Reranker, ColBERT).
465. [Advanced] What is ColBERT? How does late interaction enable efficient yet accurate retrieval?
466. [Advanced] How do you balance latency and relevance in the reranking stage?
467. [Expert] Design a multi-stage retrieval pipeline: sparse retrieval → dense retrieval → reranking → LLM.

**RAG Architecture Patterns**

468. [Intermediate] What is the role of a query router in complex RAG systems?
469. [Advanced] Explain corrective RAG (CRAG). How does it verify retrieved document relevance?
470. [Advanced] What is Graph RAG? How does knowledge graph integration improve RAG?
471. [Advanced] Describe agentic RAG. How do agents decide when and what to retrieve?
472. [Advanced] What is RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)?
473. [Expert] Design a multi-modal RAG system that handles text, images, and tables.
474. [Expert] How would you build a RAG system for a real-time knowledge base that updates frequently?
475. [Expert] Design a RAG system for legal documents. What unique challenges would you face?

**RAG Evaluation & Optimization**

476. [Intermediate] How do you evaluate retrieval quality separately from generation quality in RAG?
477. [Intermediate] What are context relevance, answer faithfulness, and answer relevance in RAG evaluation?
478. [Advanced] Describe RAGAS (RAG Assessment) framework. What metrics does it provide?
479. [Advanced] How do you diagnose and fix poor RAG performance (bad retrieval vs. bad generation)?
480. [Advanced] What is the impact of the number of retrieved documents (top-k) on generation performance?
481. [Expert] How do you A/B test RAG system improvements in production?
482. [Expert] Design a continuous evaluation and monitoring system for a production RAG pipeline.

### 15.3 AI Agents

**Agent Fundamentals**

483. [Basic] What is an AI agent? How does it differ from a standard LLM chatbot?
484. [Basic] What are the core components of an LLM-based agent (planning, memory, tools, action)?
485. [Intermediate] Explain the ReAct (Reasoning + Acting) framework. How does it combine reasoning with tool use?
486. [Intermediate] How does ReAct differ from standard Chain-of-Thought prompting?
487. [Intermediate] What is the difference between "reasoning" and "acting" in agentic workflows?
488. [Advanced] Describe the agent loop: Observe → Think → Act → Observe. How is it implemented?
489. [Advanced] What are common failure modes of AI agents (infinite loops, wrong tool selection, hallucinated actions)?
490. [Advanced] How do you implement error recovery and self-correction in agent systems?

**Tool Use & Function Calling**

491. [Basic] Why is function calling important in modern LLM-based agents?
492. [Intermediate] How does OpenAI's function calling mechanism work? Explain tools and function schemas.
493. [Intermediate] Describe scenarios where direct function calls are superior to text-only generation.
494. [Intermediate] What are potential risks of improper tool use in agents (input validation, security, hallucination)?
495. [Advanced] How do you design a robust tool schema for an agent? What error handling is needed?
496. [Advanced] How does parallel function calling work? When is it beneficial?
497. [Advanced] Explain the MCP (Model Context Protocol). What problem does it solve?
498. [Expert] Design a secure tool-use system that prevents agents from executing harmful actions.
499. [Expert] How do you handle tool failures gracefully in a multi-step agent workflow?

**Planning & Reasoning**

500. [Intermediate] What planning strategies do AI agents use (task decomposition, subgoal generation)?
501. [Intermediate] Explain how agents use reflection to improve their performance over multiple iterations.
502. [Advanced] What is the Plan-and-Execute pattern? How does it separate planning from execution?
503. [Advanced] Describe LATS (Language Agent Tree Search). How does it combine planning with search?
504. [Advanced] How do you evaluate an agent's planning ability? What benchmarks exist?
505. [Expert] What is the difference between open-loop and closed-loop planning in agents?
506. [Expert] How do you handle planning under uncertainty when agent tools may return unexpected results?

**Memory Systems**

507. [Basic] Why do AI agents need memory? What types of memory exist (short-term, long-term)?
508. [Intermediate] Explain the difference between conversational memory, episodic memory, and semantic memory in agents.
509. [Intermediate] How do you implement a sliding window memory for managing long conversations?
510. [Advanced] Describe how vector databases can serve as long-term memory for agents.
511. [Advanced] What is memory summarization? How do you compress conversation history while preserving key information?
512. [Advanced] How do you implement memory retrieval that surfaces the most relevant past interactions?
513. [Expert] Design a memory architecture for an agent that handles both structured and unstructured information over weeks of interaction.
514. [Expert] How does MemGPT's virtual context management work?

**Context Management**

515. [Intermediate] How do you manage context window limitations in agent systems?
516. [Intermediate] What strategies exist for context compression and summarization?
517. [Advanced] How do you decide what to include in the agent's context at each step?
518. [Advanced] What is attention sink? How does it affect long-context agent performance?
519. [Expert] Design a context management system for an agent that processes 100-page documents.

### 15.4 Multi-Agent Systems

520. [Intermediate] What is a multi-agent system? How does it differ from single-agent architectures?
521. [Intermediate] Describe use cases for multi-agent LLM applications in enterprise settings.
522. [Intermediate] What are the key challenges in coordination and communication within multi-agent systems?
523. [Advanced] Explain different multi-agent communication patterns (sequential, hierarchical, broadcast, debate).
524. [Advanced] What strategies are used for agent cooperation and conflict resolution?
525. [Advanced] How do you assign roles and responsibilities to different agents in a multi-agent system?
526. [Advanced] What is the "society of mind" approach to multi-agent systems?
527. [Expert] How do you ensure scalability and reliability when deploying multi-agent systems in production?
528. [Expert] Discuss emergent behavior in multi-agent systems and its implications.
529. [Expert] Design a multi-agent system where agents with different expertise collaborate on a complex task.
530. [Expert] How do you debug and monitor multi-agent interactions in production?

**Agent Orchestration**

531. [Intermediate] What is agent orchestration? Why is it needed?
532. [Advanced] Compare different orchestration patterns: router, supervisor, swarm.
533. [Advanced] How do you handle state management across multiple agents?
534. [Advanced] What is agent handoff? How do you transfer context between agents seamlessly?
535. [Expert] Design an orchestration system for a customer support application with specialized agents.
536. [Expert] How do you implement observability and tracing in a multi-agent system?

### 15.5 Frameworks & Tools

**LangChain**

537. [Basic] What is LangChain? What problems does it solve?
538. [Intermediate] What is an agent in LangChain? How is it different from a chain?
539. [Intermediate] How do you integrate external tools (calculators, search APIs, databases) in LangChain agents?
540. [Intermediate] Explain LangChain's memory management for multi-turn conversations.
541. [Advanced] How does LangChain Expression Language (LCEL) work?
542. [Advanced] Describe LangGraph. How does it enable stateful, multi-agent workflows?
543. [Advanced] How do you implement a conversational multi-agent workflow using LangChain/LangGraph?
544. [Expert] What are the performance and scalability limitations of LangChain? How do you work around them?

**LlamaIndex**

545. [Intermediate] What is LlamaIndex? How does it differ from LangChain?
546. [Intermediate] Describe how LlamaIndex enables document indexing and retrieval for RAG.
547. [Intermediate] What node and query routing strategies does LlamaIndex offer?
548. [Advanced] Explain custom retrievers and query engines in LlamaIndex.
549. [Advanced] How would you set up a multi-agent information retrieval pipeline with LlamaIndex?
550. [Expert] What are performance considerations when using LlamaIndex at scale?

**AutoGen & Other Frameworks**

551. [Intermediate] What is Microsoft AutoGen? How does it approach multi-agent conversation?
552. [Intermediate] How does AutoGen manage role assignment and communication between agents?
553. [Advanced] Describe CrewAI. How does it structure agent teams with roles and goals?
554. [Advanced] Compare LangGraph, AutoGen, and CrewAI for multi-agent systems.
555. [Advanced] What is OpenAI's Assistants API? How does it support agent-like functionality?
556. [Expert] When would you build a custom agent framework vs. using LangChain/AutoGen?

### 15.6 System Design

**RAG System Design**

557. [Intermediate] Design a RAG-based FAQ system for a company's internal documentation.
558. [Advanced] Design a RAG system for legal document question answering. Address domain-specific challenges.
559. [Advanced] Design a RAG-based customer support chatbot that handles multi-turn conversations.
560. [Advanced] How would you build a RAG system for a codebase (code search + code generation)?
561. [Expert] Design a multi-tenant RAG system where each tenant has isolated document collections.
562. [Expert] Design a RAG system that handles real-time updates from streaming data sources.
563. [Expert] How would you reduce LLM hallucinations in a production RAG system? Describe your complete strategy.

**Agent System Design**

564. [Intermediate] Design an AI agent that can browse the web and answer questions.
565. [Advanced] Design a coding agent that can write, test, and debug code autonomously.
566. [Advanced] Design an AI agent for automated data analysis (query databases, create visualizations, generate reports).
567. [Advanced] How would you build an agent that interacts with multiple APIs and handles authentication?
568. [Expert] Design a multi-agent research assistant capable of literature review, summarization, and Q&A.
569. [Expert] Design an autonomous software engineering agent. What safeguards would you include?
570. [Expert] Design a production-ready agent system with observability, error handling, and cost management.

**Production Considerations**

571. [Intermediate] How do you deploy a RAG system in production? What monitoring is needed?
572. [Intermediate] What are common latency optimization techniques for RAG systems?
573. [Advanced] How do you handle data privacy and security in RAG/agent deployments?
574. [Advanced] What caching strategies can reduce costs and latency in LLM-powered applications?
575. [Advanced] How do you implement guardrails for agent actions in production?
576. [Expert] Design a cost-optimization strategy for an LLM-powered application serving 1M users/day.
577. [Expert] How do you implement human-in-the-loop oversight for autonomous agents?
578. [Expert] What is the testing strategy for RAG and agent systems? How do you do regression testing?

### 15.7 Cutting-Edge Topics (2024-2025)

**Latest RAG Innovations**

579. [Advanced] What is GraphRAG (Microsoft)? How does it use knowledge graphs with RAG?
580. [Advanced] Explain late chunking. How does it preserve document-level context in embeddings?
581. [Advanced] What is contextual retrieval (Anthropic)? How does adding context to chunks improve retrieval?
582. [Advanced] Describe ColPali / ColQwen. How do vision-language models change document retrieval?
583. [Expert] What is speculative RAG? How does it parallelize retrieval and generation?
584. [Expert] How do long-context LLMs (1M+ tokens) change the need for RAG?

**Latest Agent Innovations**

585. [Advanced] What is the MCP (Model Context Protocol)? How does it standardize tool integration?
586. [Advanced] Explain computer-use agents (Anthropic's Computer Use, OpenAI Operator concepts). How do they work?
587. [Advanced] What is an agentic coding workflow (Copilot, Cursor, Devin concepts)?
588. [Advanced] How do reasoning models (o1, o3, DeepSeek-R1) change agent capabilities?
589. [Expert] What are the safety implications of increasingly autonomous AI agents?
590. [Expert] How do you implement verifiable and auditable agent actions?
591. [Expert] What is the "agent protocol" effort? Why is standardization important?

**Emerging Patterns**

592. [Advanced] What is structured output generation (JSON mode, constrained decoding)? How does it help agents?
593. [Advanced] How does tool-augmented generation differ from pure RAG?
594. [Advanced] What is model routing (choosing between different models based on query complexity)?
595. [Expert] Explain compound AI systems. How do they combine multiple models and retrievers?
596. [Expert] What is DSPy? How does it approach LLM programming differently from prompt engineering?
597. [Expert] How do you build evaluation-driven development pipelines for LLM applications?
598. [Expert] What is the "LLM OS" concept? How do agents, memory, and tools compose into an operating system analogy?
599. [Expert] Describe the current state of AI agent benchmarks (SWE-bench, WebArena, GAIA). What do they measure?
600. [Expert] How do you think about the reliability-autonomy tradeoff in agent systems?

---

## Bonus: Cross-Cutting & Integration Questions

601. [Advanced] Compare fine-tuning, RAG, and prompt engineering as approaches to customize LLM behavior. When would you use each?
602. [Advanced] How would you build an end-to-end system that combines RAG, agents, and fine-tuned models?
603. [Advanced] What is the role of embedding models in both RAG systems and recommendation systems?
604. [Expert] Design a complete AI platform that supports RAG, agents, fine-tuning, and evaluation for an enterprise.
605. [Expert] How do you manage the lifecycle of ML/LLM models in production (versioning, A/B testing, rollback)?
606. [Expert] What are the cost tradeoffs between using large frontier models vs. smaller fine-tuned models vs. RAG?
607. [Expert] How do multi-modal models (GPT-4V, Gemini) change the landscape of RAG and agent systems?
608. [Expert] Discuss the convergence of search, RAG, and agents. Where is the field heading in 2025-2026?
609. [Expert] What are the key open research problems in LLMs, generative AI, and AI agents?
610. [Expert] If you had unlimited compute and data, how would you build the ideal AI assistant from scratch?

---

> **Total: 610 questions**
> - Category 13 (LLMs): ~270 questions
> - Category 14 (Generative Models): ~142 questions
> - Category 15 (RAG & AI Agents): ~198 questions
>
> Difficulty distribution: ~60 Basic, ~170 Intermediate, ~230 Advanced, ~150 Expert
