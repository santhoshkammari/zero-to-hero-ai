# Part 2: Machine Learning Core

> 600+ interview questions covering ML Fundamentals, Supervised Learning, and Unsupervised Learning.
> Difficulty levels: [Basic] [Intermediate] [Advanced] [Expert]

---

## 4. ML Fundamentals & Core Concepts

### 4.1 Bias-Variance Tradeoff & Regularization

1. [Basic] Explain the bias-variance tradeoff in machine learning. How does it relate to model complexity?
2. [Basic] What is underfitting? What is overfitting? How do you identify each from training/validation curves?
3. [Basic] How do you identify if your model is suffering from high bias or high variance by looking at training and validation errors?
4. [Intermediate] Draw and explain a typical bias-variance tradeoff curve. Where is the optimal model complexity?
5. [Intermediate] What is the mathematical decomposition of expected prediction error into bias², variance, and irreducible error? Derive it.
6. [Intermediate] Suppose your model has high training error and high validation error. What does this indicate, and what steps would you take?
7. [Intermediate] Your model has very low training error but high validation error. What does this indicate, and what remedies would you apply?
8. [Advanced] Given a scenario where increasing the amount of training data does not reduce high variance, what might be the reason?
9. [Advanced] Can a model have both high bias and high variance simultaneously? Explain with an example.
10. [Advanced] How does the bias-variance tradeoff manifest differently in parametric vs. non-parametric models?
11. [Basic] What is regularization? Why is it important in machine learning?
12. [Basic] Name and briefly describe L1 and L2 regularization techniques.
13. [Intermediate] How do L1 and L2 regularization impact the learned parameters differently? Why does L1 produce sparse solutions?
14. [Intermediate] Derive the closed-form solution for Ridge Regression (L2). How does it differ from OLS?
15. [Intermediate] Why does L1 regularization (Lasso) tend to produce exactly zero coefficients while L2 (Ridge) does not? Explain geometrically.
16. [Advanced] What is Elastic Net regularization? When is it preferred over pure L1 or L2?
17. [Advanced] How does the regularization parameter λ affect the bias-variance tradeoff? What happens as λ → 0 and λ → ∞?
18. [Intermediate] Describe how dropout works as a regularization technique in neural networks.
19. [Advanced] How is dropout mathematically equivalent to an approximate Bayesian inference? Explain the connection.
20. [Intermediate] Explain early stopping as a regularization technique. How does it relate to L2 regularization?
21. [Advanced] Describe data augmentation as a form of regularization. When is it most effective?
22. [Expert] Explain the double descent phenomenon. How does it challenge the classical bias-variance tradeoff?
23. [Expert] What is the relationship between regularization and Bayesian priors? Show how L2 corresponds to a Gaussian prior.
24. [Intermediate] How does batch normalization act as a regularizer? Why?
25. [Advanced] Compare weight decay and L2 regularization. Are they always the same? When do they differ (e.g., Adam optimizer)?
26. [Intermediate] What is the effect of increasing model capacity (e.g., adding layers/neurons) on bias and variance?
27. [Basic] What are learning curves? How do you use them to diagnose bias vs. variance?
28. [Advanced] Explain the concept of structural risk minimization (SRM) and its connection to bias-variance tradeoff.
29. [Expert] Describe the PAC learning framework. How does it formalize the concept of generalization?
30. [Expert] What is VC dimension? How does it relate to model capacity and the bias-variance tradeoff?
31. [Intermediate] How does feature selection help with the bias-variance tradeoff?
32. [Advanced] Explain how ensemble methods (bagging, boosting) affect bias and variance differently.
33. [Intermediate] What is the difference between parameter norm penalties and constrained optimization for regularization?
34. [Advanced] Explain multi-task learning as a form of regularization. When does it help?
35. [Expert] Describe the lottery ticket hypothesis and its implications for model complexity and regularization.

### 4.2 Loss Functions & Optimization

36. [Basic] What is a loss function? What is a cost function? How do they differ?
37. [Basic] Name common loss functions used in regression (MSE, MAE, Huber) and classification (cross-entropy, hinge).
38. [Basic] Why is cross-entropy loss preferred over MSE for classification tasks?
39. [Intermediate] Derive the gradient of the binary cross-entropy loss with respect to model parameters.
40. [Intermediate] What is the difference between L1 loss (MAE) and L2 loss (MSE)? When would you use each?
41. [Intermediate] Explain the Huber loss function. Why is it useful?
42. [Advanced] What is the hinge loss? How is it used in SVMs? Derive its subgradient.
43. [Advanced] Explain the KL divergence loss. When is it used in machine learning?
44. [Expert] What is the focal loss? How does it address class imbalance in object detection?
45. [Advanced] Describe the triplet loss function and its use in metric learning / face recognition.
46. [Expert] Explain contrastive loss and its role in self-supervised learning frameworks.
47. [Basic] What is gradient descent? Explain the update rule mathematically.
48. [Basic] What is the difference between batch gradient descent, stochastic gradient descent (SGD), and mini-batch gradient descent?
49. [Intermediate] What are the drawbacks of vanilla SGD? How does momentum address them?
50. [Intermediate] Explain the momentum-based gradient descent. Write the update equations.
51. [Intermediate] What is Nesterov accelerated gradient? How does it improve upon standard momentum?
52. [Intermediate] Explain the AdaGrad optimizer. What problem does it solve? What is its main drawback?
53. [Intermediate] How does RMSprop differ from AdaGrad? Why was it developed?
54. [Intermediate] Explain the Adam optimizer. Write out its update equations including bias correction.
55. [Advanced] What are the hyperparameters of Adam (α, β₁, β₂, ε)? How do you tune them?
56. [Advanced] Compare Adam and RMSprop. When would you use one over the other?
57. [Advanced] What is AdamW? How does it differ from standard Adam? Why is this distinction important?
58. [Expert] Explain the LAMB optimizer. Why was it developed for large-batch training?
59. [Expert] What is the SAM (Sharpness-Aware Minimization) optimizer? How does it improve generalization?
60. [Intermediate] What is a learning rate schedule? Describe step decay, exponential decay, and cosine annealing.
61. [Advanced] Explain warmup learning rate schedules. Why are they important for training transformers?
62. [Intermediate] What is the effect of batch size on optimization? How does it relate to learning rate?
63. [Advanced] Explain the linear scaling rule for learning rate when increasing batch size.
64. [Expert] Describe cyclical learning rates and the super-convergence phenomenon.
65. [Intermediate] What are saddle points? Why are they a bigger problem than local minima in high-dimensional optimization?
66. [Advanced] Explain the concept of loss landscape smoothness and its impact on optimization.
67. [Expert] What is the relationship between the conditioning number of the Hessian and convergence speed?
68. [Advanced] Explain second-order optimization methods (Newton's method, L-BFGS). Why are they rarely used in deep learning?
69. [Expert] What is natural gradient descent? How does it relate to Fisher information?
70. [Advanced] What causes gradient explosion and vanishing gradients? How do you mitigate them?
71. [Intermediate] What is gradient clipping? When and how do you apply it?
72. [Expert] Explain the connection between loss function design and the implicit bias of gradient descent.
73. [Advanced] Why might you choose a non-standard loss function in a project? Give examples.
74. [Intermediate] What might cause an optimizer to not converge? List at least 5 reasons.
75. [Expert] Explain mixed-precision training. How does it affect optimization and what loss scaling is needed?

### 4.3 Model Evaluation Metrics

76. [Basic] Explain the components of a confusion matrix (TP, TN, FP, FN).
77. [Basic] Define accuracy, precision, recall, and F1-score. When is accuracy misleading?
78. [Basic] Given the confusion matrix: Actual 0 → [Pred 0: 80, Pred 1: 20], Actual 1 → [Pred 0: 10, Pred 1: 90]. Calculate precision, recall, and F1.
79. [Intermediate] In a medical diagnosis model, would you prioritize precision or recall? Justify your answer.
80. [Intermediate] Explain the precision-recall tradeoff. How do you choose the optimal threshold?
81. [Intermediate] What is the F-beta score? When would you use F2 vs F0.5?
82. [Basic] What is the ROC curve? What does AUC represent?
83. [Intermediate] What does an AUC of 0.5 mean? What about 0.8? What about 1.0?
84. [Intermediate] How is ROC AUC affected by class imbalance? When is PR-AUC better?
85. [Advanced] A model has F1 = 0.7 but AUC = 0.9. How do you interpret this discrepancy?
86. [Intermediate] How do you extend precision, recall, and F1 to multi-class problems? Explain macro, micro, and weighted averaging.
87. [Advanced] How would you visualize and interpret ROC AUC in a multi-class classification problem (one-vs-rest)?
88. [Intermediate] What is log loss (cross-entropy loss) as an evaluation metric? Why is it preferred over accuracy for probabilistic classifiers?
89. [Advanced] What is calibration of a classifier? How do you assess it (reliability diagram, Brier score)?
90. [Advanced] Explain the Matthews Correlation Coefficient (MCC). When is it more informative than F1?
91. [Intermediate] What is Cohen's Kappa? When would you use it?
92. [Intermediate] For regression tasks, compare MSE, RMSE, MAE, and MAPE. When is each appropriate?
93. [Advanced] What is the R² score? Can it be negative? What does a negative R² mean?
94. [Advanced] What is adjusted R²? Why is it preferred over R² when comparing models with different numbers of features?
95. [Intermediate] What evaluation metric would you use for a ranking problem? Explain NDCG and MAP.
96. [Advanced] What is the difference between offline metrics and online metrics? Why might they disagree?
97. [Expert] Design a custom evaluation metric for a business problem where false negatives cost $1000 and false positives cost $10.
98. [Advanced] How would you use the confusion matrix and ROC curve together to improve model performance?
99. [Advanced] Design a process for tuning thresholds to optimize for either F1, precision, or recall depending on business needs.
100. [Expert] What are the limitations of F1-score? In what scenarios would you prefer MCC or balanced accuracy?
101. [Intermediate] How do you evaluate a model's performance on imbalanced data? What metrics are most reliable?
102. [Advanced] Explain the concept of statistical significance in model evaluation. How do you determine if one model is significantly better than another?

### 4.4 Cross-Validation & Hyperparameter Tuning

103. [Basic] What is cross-validation and why is it important?
104. [Basic] Describe k-fold cross-validation. How does it work step by step?
105. [Intermediate] What is the difference between k-fold cross-validation and leave-one-out cross-validation (LOOCV)?
106. [Intermediate] When would you use stratified k-fold cross-validation?
107. [Intermediate] Why is standard k-fold cross-validation inappropriate for time series data? What alternatives exist?
108. [Advanced] Describe nested cross-validation. Why is it necessary for unbiased model selection?
109. [Advanced] What is the computational cost of LOOCV vs k-fold? When is LOOCV tractable?
110. [Basic] What are hyperparameters? How do they differ from model parameters?
111. [Basic] Explain how grid search works for hyperparameter tuning.
112. [Intermediate] What are the drawbacks of grid search? How does random search improve upon it?
113. [Intermediate] Explain random search for hyperparameter tuning. Why can it outperform grid search?
114. [Advanced] Describe Bayesian optimization for hyperparameter tuning. How does it use a surrogate model?
115. [Advanced] What is a Gaussian Process surrogate? Explain acquisition functions (EI, UCB, PI) in Bayesian optimization.
116. [Expert] Compare Bayesian optimization with Tree-structured Parzen Estimators (TPE) used in Optuna/Hyperopt.
117. [Intermediate] What is Hyperband? How does it combine early stopping with random search?
118. [Advanced] Explain BOHB (Bayesian Optimization + Hyperband). Why is it considered state-of-the-art?
119. [Intermediate] How do you prevent data leakage during cross-validation and hyperparameter tuning?
120. [Advanced] Give an example of a situation where cross-validation might give misleading results (e.g., grouped or temporal data).
121. [Intermediate] How do you combine cross-validation with hyperparameter tuning in a scikit-learn pipeline?
122. [Expert] Describe multi-fidelity hyperparameter optimization. How does it reduce computation?
123. [Advanced] How would you tune hyperparameters when model training takes 12+ hours per run?
124. [Intermediate] What is the role of the validation set vs. test set? When is a separate holdout test set necessary?
125. [Advanced] Explain the concept of information leakage through hyperparameter tuning on the test set (Goodhart's law in ML).

### 4.5 Ensemble Methods

126. [Basic] What is an ensemble method? Why do ensemble methods generally outperform single models?
127. [Basic] Explain the difference between bagging and boosting.
128. [Intermediate] How does bootstrap sampling in bagging work? What is the expected proportion of unique samples (~63.2%)?
129. [Intermediate] Explain why bagging reduces variance but not bias. Provide the mathematical intuition.
130. [Intermediate] What is the Out-of-Bag (OOB) error? How does it compare to k-fold cross-validation?
131. [Advanced] Can you modify bagging for non-i.i.d. data? How?
132. [Intermediate] Explain how AdaBoost works step by step. How does it adjust sample weights?
133. [Advanced] Derive the weight update formula in AdaBoost. What loss function does it implicitly minimize?
134. [Advanced] Compare Gradient Boosting with AdaBoost. What loss functions do they minimize?
135. [Intermediate] What is the role of the learning rate (shrinkage) in boosting? Why is a low learning rate with many estimators preferred?
136. [Advanced] What are the major causes of overfitting in boosting, and how can they be mitigated?
137. [Advanced] How does early stopping work in gradient boosting? What are its pros and cons?
138. [Intermediate] What is stacking (stacked generalization)? How does it combine base learners?
139. [Advanced] What are the theoretical advantages of stacking over bagging and boosting?
140. [Advanced] How do you prevent data leakage between base learners and the meta-learner in stacking?
141. [Advanced] How do you select base models and the meta-model in stacking to maximize diversity?
142. [Expert] Describe cross-validated stacking. How does it produce unbiased meta-features?
143. [Intermediate] What is blending? How does it differ from stacking?
144. [Advanced] How would you ensemble models of different types (trees, NNs, linear) to tackle imbalanced data?
145. [Advanced] What are the disadvantages of ensembling in production systems? How do you mitigate latency/memory costs?
146. [Expert] Describe a real-world scenario where ensemble methods failed to outperform a strong single model. Why?
147. [Intermediate] How would you diagnose whether your ensemble suffers from bias or variance?
148. [Advanced] How does diversity among base learners affect ensemble performance? How do you measure/encourage it?
149. [Expert] Explain the concept of ensemble pruning. How do you select the optimal subset of base models?
150. [Advanced] Describe the difference in interpretability between single models and ensembles. How do you approach ensemble explainability?

### 4.6 Feature Importance & Model Interpretability

151. [Basic] What is feature importance? Name at least three methods to calculate it.
152. [Basic] What is the difference between feature importance and feature selection?
153. [Intermediate] Explain permutation importance. What are its advantages over built-in tree feature importance?
154. [Intermediate] What are the limitations of traditional (impurity-based) feature importance in tree models?
155. [Advanced] What is SHAP (SHapley Additive exPlanations)? What theoretical concept is it based on?
156. [Advanced] How are SHAP values calculated? Explain the connection to cooperative game theory.
157. [Intermediate] What is the difference between TreeSHAP and KernelSHAP? When would you use each?
158. [Advanced] How does SHAP guarantee additivity and consistency in feature attributions?
159. [Advanced] Explain a scenario where SHAP can provide misleading explanations.
160. [Intermediate] What is LIME (Local Interpretable Model-agnostic Explanations)? How does it work?
161. [Intermediate] Describe the algorithm behind LIME: perturbation, locality, interpretable surrogate.
162. [Advanced] Discuss potential drawbacks or limitations of LIME (instability, sensitivity to perturbation).
163. [Advanced] Explain a case where LIME might give inconsistent explanations for similar data points.
164. [Intermediate] How does LIME differ from SHAP, both in methodology and application?
165. [Intermediate] What is the difference between global and local model interpretability?
166. [Advanced] How do correlated features affect SHAP and LIME explanations?
167. [Advanced] What computational challenges arise when using SHAP for high-dimensional data?
168. [Expert] Argue for or against using LIME/SHAP in production systems. What safeguards are needed?
169. [Advanced] Can SHAP or LIME be used for real-time model explanations? What are the constraints?
170. [Intermediate] What are partial dependence plots (PDPs)? How do they differ from SHAP dependence plots?
171. [Advanced] What are Accumulated Local Effects (ALE) plots? When are they preferred over PDPs?
172. [Intermediate] How would you explain a model's prediction to a non-technical stakeholder?
173. [Advanced] If SHAP values and built-in feature importances disagree, what steps would you take?
174. [Expert] You need to explain a model's decisions for a regulatory audit. Would you choose SHAP or LIME? Justify.
175. [Advanced] Suggest ways to validate or sanity-check SHAP/LIME explanations.
176. [Expert] Explain counterfactual explanations. How do they complement SHAP/LIME?
177. [Expert] What is the relationship between model interpretability and model fairness? How do you use explainability tools to detect bias?
178. [Advanced] Discuss the trade-off between model accuracy and interpretability. When is an interpretable model preferable?
179. [Expert] Explain concept-based explanations (TCAV). How do they go beyond feature-level attributions?
180. [Advanced] How do you handle feature importance in the presence of feature interactions?

### 4.7 Data Preprocessing & Feature Engineering

181. [Basic] What is feature scaling? Compare standardization (Z-score) and min-max normalization.
182. [Basic] Why is feature scaling important for algorithms like SVM and KNN but not for tree-based models?
183. [Intermediate] How do you handle missing values in a dataset? Compare imputation strategies (mean, median, KNN, MICE).
184. [Intermediate] What is one-hot encoding? When would you use it vs. label encoding vs. target encoding?
185. [Advanced] Explain target encoding. What is target leakage, and how do you prevent it with target encoding?
186. [Intermediate] How do you handle categorical features with very high cardinality (e.g., 10,000 categories)?
187. [Advanced] What is feature hashing? When is it useful?
188. [Intermediate] How do you detect and handle outliers? When should you remove them vs. keep them?
189. [Advanced] Explain the Box-Cox and Yeo-Johnson transformations. Why are they used?
190. [Intermediate] How would you handle heavily skewed features?
191. [Advanced] What is feature interaction? How do you create polynomial features, and when is this useful?
192. [Intermediate] Explain the difference between filter, wrapper, and embedded feature selection methods.
193. [Advanced] What is mutual information? How is it used for feature selection?
194. [Expert] How would you handle a dataset with 1 million features? Describe your feature engineering/selection pipeline.
195. [Intermediate] How do you handle date/time features for machine learning?
196. [Advanced] What is data leakage? Give three common examples and how to prevent them.
197. [Expert] Describe feature engineering for text data, image data, and tabular data. How do they differ?
198. [Intermediate] What is the curse of dimensionality? How does it affect model performance?
199. [Advanced] How do you create meaningful features from raw geospatial data?
200. [Expert] Design a feature engineering pipeline for a fraud detection system that processes 10M transactions/day.

### 4.8 ML System Design & Production

201. [Intermediate] What is the difference between offline (batch) and online (real-time) model serving?
202. [Advanced] How do you version data and models in a production ML workflow?
203. [Advanced] What is model drift? How do you detect and handle it?
204. [Intermediate] What is feature drift vs. concept drift? How do they differ?
205. [Advanced] How would you design an A/B test for a new ML model?
206. [Expert] Design a recommendation system for an e-commerce platform. Describe the end-to-end architecture.
207. [Expert] How would you architect a system to generate recommendations for millions of users in real-time?
208. [Advanced] How do you handle the cold-start problem in recommendation systems?
209. [Expert] Design a fraud detection system that handles 1M transactions per day with <100ms latency.
210. [Advanced] How do you ensure low latency for an inference pipeline in production?
211. [Advanced] What monitoring metrics would you track for a production ML model?
212. [Expert] Describe how to implement a model rollback strategy when a deployed model degrades.
213. [Advanced] What is a feature store? Why is it important for production ML?
214. [Expert] Explain the challenges of training-serving skew. How do you mitigate it?

---

## 5. Supervised Learning

### 5.1 Linear Regression

215. [Basic] What is linear regression? What problem does it solve?
216. [Basic] What are the assumptions of linear regression? (Linearity, independence, homoscedasticity, normality, no multicollinearity)
217. [Intermediate] Explain why each assumption matters. What can go wrong if each assumption is violated?
218. [Basic] What is the difference between simple and multiple linear regression?
219. [Intermediate] Derive the closed-form solution (Normal Equation) for OLS: θ = (X^T X)^(-1) X^T y.
220. [Advanced] Why do we use the least squares criterion instead of absolute error? Explain mathematical tractability and properties.
221. [Intermediate] What is the geometric interpretation of linear regression? Explain the projection onto column space.
222. [Advanced] If the matrix X^T X is not invertible (singular), what does that imply? How do you fix it?
223. [Intermediate] Derive the gradient of the MSE loss for linear regression. Write the gradient descent update rule.
224. [Advanced] How would you implement linear regression using gradient descent instead of the normal equation? When is GD preferred?
225. [Intermediate] How do you check for multicollinearity? What is VIF (Variance Inflation Factor)?
226. [Advanced] Describe the bias-variance tradeoff specifically for OLS regression.
227. [Intermediate] How does Ridge Regression (L2) alter the OLS solution? Derive the regularized closed form.
228. [Intermediate] How does Lasso Regression (L1) alter the OLS solution? Why is there no closed-form solution?
229. [Advanced] How does regularization (Ridge/Lasso) change the effective degrees of freedom of the model?
230. [Advanced] Explain the probabilistic interpretation of linear regression (MLE with Gaussian noise).
231. [Expert] Show that Ridge regression is equivalent to MAP estimation with a Gaussian prior on weights.
232. [Advanced] How do you handle categorical features in linear regression? Explain dummy variables and the dummy variable trap.
233. [Intermediate] What is heteroscedasticity? How do you detect it (Breusch-Pagan test) and handle it (WLS)?
234. [Advanced] Explain Weighted Least Squares (WLS). When is it necessary?
235. [Advanced] What are influence points and leverage points? How do Cook's distance help identify them?
236. [Intermediate] How do you interpret the coefficients of a linear regression model?
237. [Expert] What is Generalized Least Squares (GLS)? When would you use it instead of OLS?
238. [Intermediate] What is the difference between R² and adjusted R²?
239. [Advanced] Can R² be negative? What does a negative R² mean?
240. [Expert] Explain the Gauss-Markov theorem. Under what conditions is OLS the Best Linear Unbiased Estimator (BLUE)?
241. [Intermediate] How do you diagnose model misspecification in linear regression (residual plots)?
242. [Advanced] What are polynomial regression and its limitations? How is it related to linear regression?
243. [Expert] Implement linear regression from scratch in Python using only numpy. Include gradient descent and the normal equation.

### 5.2 Logistic Regression

244. [Basic] What is logistic regression? Why is it called "regression" even though it's used for classification?
245. [Basic] Explain the sigmoid function. What are its properties?
246. [Intermediate] Why can't we use MSE as a loss function for logistic regression? Explain non-convexity.
247. [Intermediate] Derive the likelihood function for logistic regression: P(y|X) = ∏ σ(Xθ)^y · (1-σ(Xθ))^(1-y).
248. [Advanced] Write and derive the log-likelihood and its gradient for logistic regression.
249. [Advanced] Derive the update rule for gradient descent in logistic regression. Show the gradient computation step by step.
250. [Intermediate] Why is there no closed-form solution for logistic regression? Why must we use iterative methods?
251. [Intermediate] Explain the difference between odds and probability. What is the logit function?
252. [Intermediate] How do you interpret the coefficients of a logistic regression model in terms of odds ratios?
253. [Advanced] What are the assumptions of logistic regression?
254. [Intermediate] How does L1 and L2 regularization change the logistic regression loss? Write the new objective function.
255. [Advanced] What is the difference between softmax regression and multinomial logistic regression?
256. [Advanced] Explain multinomial logistic regression (softmax). Derive the softmax function and its gradient.
257. [Advanced] Discuss techniques to handle imbalanced data in logistic regression (class weights, oversampling, threshold tuning).
258. [Expert] What is "complete separation" and "quasi-separation" in logistic data? What are the implications for logistic regression?
259. [Intermediate] Explain how p-values and confidence intervals are interpreted in logistic regression.
260. [Advanced] Compare logistic regression with probit regression. When would you use each?
261. [Advanced] What is the Newton-Raphson (IRLS) method for fitting logistic regression? How does it differ from gradient descent?
262. [Expert] Implement logistic regression from scratch in Python with L2 regularization and gradient descent.
263. [Intermediate] How would you diagnose model misspecification in logistic regression?
264. [Advanced] Explain the deviance and its use as a goodness-of-fit measure for logistic regression.
265. [Expert] What is the relationship between logistic regression and exponential family distributions?

### 5.3 Decision Trees

266. [Basic] How does a decision tree make predictions for classification and regression?
267. [Basic] What is information gain? How is it calculated using entropy?
268. [Intermediate] Explain entropy, Gini impurity, and variance reduction as split criteria. When do you use each?
269. [Intermediate] Derive the formula for information gain: IG(S,A) = H(S) - Σ (|Sv|/|S|) · H(Sv).
270. [Intermediate] Compare entropy-based and Gini-based splitting. Do they produce different trees?
271. [Advanced] What is the gain ratio? How does it address the bias of information gain toward features with many values?
272. [Intermediate] What is pruning? Compare pre-pruning and post-pruning techniques.
273. [Advanced] Explain cost-complexity pruning (minimal cost-complexity pruning) with the α parameter. How do you select optimal α?
274. [Intermediate] What are the advantages and disadvantages of decision trees?
275. [Intermediate] Why are decision trees considered non-parametric models?
276. [Intermediate] How do decision trees handle missing data?
277. [Advanced] Explain feature selection bias in decision trees. How do conditional inference trees address it?
278. [Intermediate] What is the computational complexity of building a decision tree?
279. [Advanced] How do you handle continuous features in decision trees?
280. [Advanced] What is the minimum description length (MDL) principle in the context of decision trees?
281. [Expert] Implement a decision tree classifier from scratch including entropy calculation and recursive splitting.
282. [Intermediate] How do you visualize decision trees and extract human-readable rules?
283. [Advanced] How do oblique decision trees differ from axis-aligned trees? When are they useful?
284. [Expert] Implement cost-complexity pruning from scratch. Show how to select optimal tree depth using cross-validation.

### 5.4 Random Forests

285. [Basic] What is a Random Forest? How does it combine decision trees?
286. [Intermediate] How does Random Forest introduce randomness? Explain both bagging and feature subsampling.
287. [Intermediate] Why is Random Forest less prone to overfitting than individual deep decision trees?
288. [Intermediate] What is the "feature subspace" parameter (max_features)? How do you choose it?
289. [Advanced] Discuss the trade-off between the number of trees and computational cost. Is there a point of diminishing returns?
290. [Intermediate] How does Random Forest calculate feature importance (impurity-based vs. permutation)?
291. [Advanced] What are the limitations of impurity-based feature importance in Random Forests? When can it be biased?
292. [Intermediate] What is the Out-of-Bag (OOB) score? How is it computed and why is it useful?
293. [Advanced] How can Random Forests be used for unsupervised learning (proximity matrix, outlier detection)?
294. [Advanced] Explain how Random Forests handle missing values during prediction.
295. [Expert] What is the theoretical relationship between the number of trees, correlation between trees, and ensemble variance?
296. [Intermediate] Compare Random Forest with a single deep decision tree in terms of bias, variance, and interpretability.
297. [Advanced] How would you parallelize Random Forest training? What makes it embarrassingly parallel?
298. [Expert] Implement Random Forest from scratch including bootstrap sampling and feature subsampling.

### 5.5 Gradient Boosting (XGBoost, LightGBM, CatBoost)

299. [Basic] What is gradient boosting? How does it differ from Random Forests?
300. [Intermediate] Explain the gradient boosting algorithm step by step. How are residuals used?
301. [Advanced] Derive the gradient boosting update for squared loss. Show how each tree fits the negative gradient.
302. [Advanced] How does the learning rate (shrinkage) interact with the number of estimators in gradient boosting?
303. [Intermediate] How does XGBoost prevent overfitting? Explain the role of L1 (alpha) and L2 (lambda) regularization in its objective.
304. [Advanced] Describe the histogram-based split finding in XGBoost and its computational benefits.
305. [Advanced] How does XGBoost handle missing values natively during training and inference?
306. [Advanced] What is the DMatrix in XGBoost? Why is it important for optimization?
307. [Intermediate] What are the differences between the gbtree and gblinear boosters in XGBoost?
308. [Advanced] Explain how XGBoost parallelizes tree construction. How is it different from LightGBM?
309. [Expert] Describe the Approximate, Exact, and Histogram split finding algorithms in XGBoost.
310. [Advanced] What are monotonic constraints in XGBoost? When would you use them?
311. [Advanced] Explain the DART booster (Dropouts meet Multiple Additive Regression Trees). When is it useful?
312. [Intermediate] What is Gradient-based One-Side Sampling (GOSS) in LightGBM? How does it speed up training?
313. [Advanced] Explain Exclusive Feature Bundling (EFB) in LightGBM. How does it handle high-dimensional sparse data?
314. [Advanced] How does LightGBM's leaf-wise growth strategy differ from XGBoost's level-wise strategy?
315. [Intermediate] What are the risks of leaf-wise growth in LightGBM? How do you mitigate overfitting?
316. [Intermediate] How does LightGBM handle categorical features natively?
317. [Advanced] What is the impact of the max_bin parameter in LightGBM on accuracy and speed?
318. [Advanced] How does CatBoost handle categorical variables differently from LightGBM and XGBoost?
319. [Advanced] Explain ordered boosting in CatBoost. How does it reduce prediction shift?
320. [Expert] How does CatBoost mitigate target leakage when encoding categorical features?
321. [Advanced] What are symmetric (oblivious) trees in CatBoost? What are their trade-offs?
322. [Intermediate] CatBoost claims to be less sensitive to hyperparameter tuning. Why?
323. [Advanced] Compare XGBoost, LightGBM, and CatBoost: speed, accuracy, categorical handling, and missing values.
324. [Expert] In what situations would you prefer CatBoost over LightGBM or XGBoost?
325. [Advanced] Given a highly imbalanced, high-cardinality categorical dataset, which boosting framework would you choose and why?
326. [Advanced] How do you perform feature importance analysis in gradient boosting models? What are the limitations?
327. [Advanced] How do each framework's GPU capabilities differ? When is GPU boosting beneficial?
328. [Expert] How would you debug slow training in XGBoost on a 100M row dataset?
329. [Expert] How do gradient boosting models rank for interpretability in regulated industries (e.g., finance)?
330. [Advanced] Discuss partial dependence plots and SHAP values for gradient boosting models. How reliable are they?
331. [Expert] You notice your LightGBM model overfits even after reducing learning rate and increasing regularization. What else do you try?
332. [Expert] Design an AutoML pipeline that intelligently selects between XGBoost, LightGBM, and CatBoost.
333. [Advanced] Explain the second-order Taylor expansion used in XGBoost's objective function. Why does it improve convergence?
334. [Expert] Implement a simplified gradient boosting machine from scratch for regression.

### 5.6 Support Vector Machines (SVMs)

335. [Basic] What is a Support Vector Machine? What is the geometric intuition behind it?
336. [Basic] What are support vectors? Why are they important?
337. [Intermediate] Explain the concept of maximum margin classifier. Why does maximizing margin lead to better generalization?
338. [Intermediate] Derive the optimization problem for a linear hard-margin SVM.
339. [Advanced] Explain the dual formulation of SVM. Why is the dual form useful?
340. [Advanced] Write the dual SVM optimization problem. Show where the kernel function enters.
341. [Intermediate] What is a soft-margin SVM? Explain the role of slack variables (ξ) and the C parameter.
342. [Advanced] How does the C parameter control the bias-variance tradeoff in SVMs?
343. [Intermediate] What is the kernel trick? Why is it important?
344. [Advanced] Explain mathematically how the kernel trick allows computing inner products in high-dimensional spaces without explicit mapping.
345. [Intermediate] Name four common kernel functions: linear, polynomial, RBF, and sigmoid. Write their mathematical forms.
346. [Advanced] How does the parameter σ (or γ) in the RBF kernel affect the decision boundary?
347. [Advanced] What is Mercer's theorem? Why is it critical for valid kernel functions?
348. [Expert] Show that the RBF kernel corresponds to an infinite-dimensional feature mapping.
349. [Advanced] Explain the ε-SVR (Support Vector Regression). How does it differ from classification SVM?
350. [Intermediate] How do you choose between linear, polynomial, and RBF kernels?
351. [Advanced] What is the computational complexity of training an SVM? Why doesn't it scale well to large datasets?
352. [Advanced] How does SMO (Sequential Minimal Optimization) solve the SVM optimization problem?
353. [Expert] Prove that the linear SVM with kernel K(x,x') = x^T x' reduces to the standard maximal margin classifier.
354. [Advanced] Compare SVMs with logistic regression for binary classification. When would you choose one over the other?
355. [Expert] Why might you not want to use a very high-degree polynomial kernel?
356. [Advanced] How do you handle multi-class classification with SVMs? Explain one-vs-one and one-vs-rest.
357. [Intermediate] How do SVMs handle imbalanced datasets?
358. [Expert] Implement a linear SVM from scratch using the hinge loss and gradient descent.
359. [Advanced] What is the relationship between SVMs and regularization (L2 penalty)?
360. [Expert] Explain the connection between SVMs and the structural risk minimization (SRM) principle.

### 5.7 K-Nearest Neighbors (KNN)

361. [Basic] Explain the KNN algorithm for classification and regression.
362. [Basic] Is KNN a parametric or non-parametric model? Is it lazy or eager? Why?
363. [Intermediate] How does KNN handle high dimensionality? What are the consequences (curse of dimensionality)?
364. [Intermediate] Compare majority voting and distance-weighted voting in KNN.
365. [Basic] Why is it important to scale features before using KNN?
366. [Intermediate] How do you choose the optimal value of K? What happens when K is too small vs. too large?
367. [Intermediate] What is the time and space complexity of KNN for training and prediction?
368. [Advanced] How would you speed up KNN for large datasets? Explain KD-trees, Ball trees, and approximate nearest neighbors.
369. [Advanced] How does KNN perform with imbalanced classes? What strategies can mitigate this?
370. [Intermediate] How do different distance metrics (Euclidean, Manhattan, Minkowski, cosine) affect KNN?
371. [Advanced] How would you handle missing data in KNN?
372. [Expert] Implement KNN from scratch using numpy for both classification and regression.
373. [Expert] Given a dataset too large to fit in RAM, how would you optimize KNN search?
374. [Advanced] Explain the relationship between KNN and kernel density estimation.
375. [Intermediate] When would you use KNN vs. a model-based approach like logistic regression?

### 5.8 Naive Bayes

376. [Basic] Explain the Naive Bayes algorithm. What assumption does it make?
377. [Intermediate] What is the "naive" conditional independence assumption? Give an example where it fails.
378. [Intermediate] Despite the naive assumption often being violated, why does Naive Bayes still perform well in practice?
379. [Intermediate] Explain the difference between Multinomial, Bernoulli, and Gaussian Naive Bayes. When do you use each?
380. [Intermediate] How do you handle continuous features in Naive Bayes (Gaussian NB)?
381. [Intermediate] What is Laplace smoothing (additive smoothing)? Why is it needed?
382. [Advanced] How do you handle correlated features in Naive Bayes?
383. [Advanced] Derive the Naive Bayes classifier from Bayes' theorem. Show the simplification with the independence assumption.
384. [Intermediate] Why is Naive Bayes particularly effective for text classification?
385. [Advanced] How does Naive Bayes handle zero-frequency problems? What happens without smoothing?
386. [Expert] Implement Gaussian Naive Bayes from scratch for classification.
387. [Expert] Write code to perform text classification using Multinomial Naive Bayes with Laplace smoothing.
388. [Intermediate] Compare Naive Bayes with logistic regression for text classification.
389. [Advanced] What is the computational complexity of training and prediction for Naive Bayes?
390. [Advanced] How can Naive Bayes be used for out-of-core (incremental) learning?

### 5.9 Time Series Forecasting

391. [Basic] What is time series analysis? What are the key components of a time series (trend, seasonality, cyclicity, noise)?
392. [Basic] What is stationarity? Why is it important in time series modeling?
393. [Intermediate] How do you test for stationarity? Explain the ADF test and KPSS test.
394. [Intermediate] Explain the difference between additive and multiplicative seasonality.
395. [Intermediate] What is autocorrelation? How is it measured using ACF and PACF plots?
396. [Basic] What does ARIMA stand for? What are the parameters (p, d, q)?
397. [Intermediate] How would you select the values for p, d, and q in ARIMA? Use ACF/PACF plots and information criteria.
398. [Intermediate] How do you make a non-stationary time series stationary (differencing, detrending, log transform)?
399. [Advanced] What is the difference between ARIMA and SARIMA? When do you need the seasonal component?
400. [Advanced] Explain seasonal decomposition (STL decomposition).
401. [Intermediate] What is the role of differencing in ARIMA?
402. [Advanced] What are the residual diagnostics for ARIMA? (Ljung-Box test, normality check)
403. [Advanced] How can exogenous variables be incorporated into ARIMA models (ARIMAX/SARIMAX)?
404. [Intermediate] What is Prophet? What are its main advantages over ARIMA?
405. [Intermediate] How does Prophet model trend and seasonality differently from ARIMA?
406. [Intermediate] What are changepoints in Prophet? How does it detect trend changes?
407. [Intermediate] How does Prophet handle holidays and special events?
408. [Advanced] What are the limitations of Prophet?
409. [Intermediate] Explain exponential smoothing methods: Simple, Holt's, and Holt-Winters.
410. [Advanced] How does exponential smoothing relate to ARIMA models? (ETS as a special case)
411. [Intermediate] How do you evaluate time series forecast accuracy? (MAE, RMSE, MAPE, SMAPE)
412. [Advanced] Explain cross-validation strategies for time series data (walk-forward validation, expanding/sliding window).
413. [Advanced] What are the advantages/disadvantages of using ML models (XGBoost, LSTMs) for time series vs. statistical models?
414. [Advanced] How do you structure time series data for supervised learning (lag features, rolling statistics)?
415. [Advanced] Discuss the risks of data leakage in time series forecasting.
416. [Expert] How would you ensemble different time series models (ARIMA + XGBoost + Prophet)?
417. [Advanced] What is multivariate time series forecasting? How does it differ from univariate?
418. [Expert] Explain transfer learning in time series forecasting (e.g., foundation models for time series).
419. [Advanced] How do you detect and handle outliers in time series data?
420. [Intermediate] How do you handle missing values in time series data?
421. [Expert] Implement ARIMA from scratch for a simple time series dataset.
422. [Advanced] Compare ARIMA, Prophet, and neural approaches (LSTM, Transformer) for time series. When would you use each?

### 5.10 Practical Model Selection & Real-World Scenarios

423. [Basic] When would you use linear regression vs. logistic regression vs. decision trees?
424. [Intermediate] You have 100 features and 500 samples. Which models would you consider and why?
425. [Intermediate] You have 10M samples and 50 features. Which models would you consider and why?
426. [Intermediate] How do you handle a multi-class classification problem with 100 classes?
427. [Advanced] You're given a dataset with 95% class imbalance. Walk through your complete approach.
428. [Intermediate] How do you decide between using a simple model (logistic regression) vs. a complex one (gradient boosting)?
429. [Advanced] Describe a scenario where you'd use linear regression despite having access to XGBoost.
430. [Intermediate] How would you handle a dataset with both numerical and categorical features (high cardinality)?
431. [Advanced] You have a model with excellent offline metrics but poor production performance. What went wrong?
432. [Expert] Design a complete ML pipeline for predicting customer churn: data collection → feature engineering → model selection → deployment → monitoring.
433. [Expert] Design a credit scoring model that must be explainable to regulators. What model do you choose and why?
434. [Advanced] How would you approach a multi-label classification problem? What models and evaluation metrics?
435. [Intermediate] When would you use regression vs. classification to solve the same business problem?
436. [Advanced] How do you handle non-stationary distributions in a production prediction system?
437. [Expert] You need to build a model that processes 100K predictions per second. What architecture do you design?
438. [Advanced] Compare the trade-offs of model complexity, training time, inference time, and interpretability for a business use case.
439. [Advanced] How would you adapt supervised learning for a problem with very few labeled examples (few-shot learning, semi-supervised)?
440. [Intermediate] Given a regression target with extreme outliers, how would you choose and configure your model?
441. [Expert] Design a multi-objective optimization framework where you need to simultaneously optimize accuracy, latency, and fairness.
442. [Advanced] How would you build a model that must work across different geographic regions with varying data distributions?
443. [Intermediate] How do you handle data that arrives in streams vs. batch for supervised learning?
444. [Advanced] Explain online learning vs. batch learning. When is online learning preferable?
445. [Expert] Design a real-time bidding system for online advertising using supervised learning.
446. [Advanced] How do you handle label noise in supervised learning?
447. [Expert] Design a model for predicting rare events (probability < 0.01%). What special considerations apply?
448. [Intermediate] How do you select between L1 vs. L2 regularization for a specific use case?
449. [Advanced] When should you use a probabilistic model vs. a point prediction model?
450. [Expert] You're building a medical diagnosis system. What special considerations apply regarding model selection, evaluation, and deployment?
451. [Advanced] How do you handle features that are only available at training time but not at prediction time?
452. [Intermediate] What is the difference between discriminative and generative models? Give examples.
453. [Advanced] How do you handle multi-modal data (images + text + tabular) in a supervised learning pipeline?
454. [Expert] Describe how to implement active learning to minimize labeling costs while maximizing model performance.
455. [Advanced] How would you build a model that needs to be robust to adversarial inputs?
456. [Intermediate] Compare batch prediction vs. real-time prediction architectures. When do you use each?
457. [Advanced] How do you handle seasonality and trends in a production ML model for sales forecasting?
458. [Expert] Design a complete NLP pipeline for sentiment analysis from data collection to deployment.
459. [Advanced] How do you handle covariate shift between training and test/production data?
460. [Expert] Explain transfer learning in the context of tabular data. When does it work?
461. [Advanced] How would you build a calibrated classifier? Why is calibration important?
462. [Intermediate] Explain the difference between parametric and non-parametric models with examples.
463. [Advanced] When should you use a Bayesian approach vs. frequentist approach for supervised learning?
464. [Expert] Design a real-time anomaly detection system that operates on streaming sensor data with supervised labels.

---

## 6. Unsupervised Learning

### 6.1 K-Means Clustering

465. [Basic] What is clustering? Name at least five popular clustering algorithms.
466. [Basic] Describe the K-Means algorithm step by step.
467. [Basic] What are the limitations of K-Means?
468. [Intermediate] How do you choose the value of K? Explain the elbow method.
469. [Intermediate] What is cluster inertia? Why does it always decrease as K increases?
470. [Intermediate] What is the silhouette score? How is it calculated and interpreted?
471. [Intermediate] Why does K-Means fail on non-convex, elongated, or clusters of different densities?
472. [Advanced] What initialization strategies exist for K-Means? Explain K-Means++ and why it's better than random.
473. [Advanced] Prove that K-Means always converges. Does it converge to a global optimum?
474. [Advanced] What is the computational complexity of K-Means? How does it scale with n, d, and k?
475. [Intermediate] How do distance metrics affect K-Means? Why is Euclidean the default?
476. [Advanced] Can K-Means work with non-Euclidean distance metrics? Explain K-Medoids.
477. [Advanced] What is Mini-Batch K-Means? When is it preferred over standard K-Means?
478. [Expert] Implement K-Means from scratch in Python using numpy. Include the elbow method for choosing K.
479. [Intermediate] How do you handle categorical data in clustering? (K-Modes, K-Prototypes)
480. [Advanced] What pre-processing steps are critical before applying K-Means?
481. [Advanced] How would you use K-Means for image compression? Implement it.
482. [Expert] Explain the connection between K-Means and Gaussian Mixture Models (when covariances are spherical and equal).
483. [Intermediate] How does feature scaling affect K-Means results?
484. [Advanced] How would you parallelize K-Means for very large datasets?

### 6.2 DBSCAN

485. [Intermediate] How does DBSCAN work? Explain core points, border points, and noise points.
486. [Intermediate] What are the advantages of DBSCAN over K-Means?
487. [Intermediate] Explain the eps and min_samples parameters. How do they affect clustering?
488. [Advanced] How do you systematically choose eps and min_samples? (k-distance graph method)
489. [Advanced] How does DBSCAN handle clusters of varying density? What are its limitations?
490. [Intermediate] How does DBSCAN handle noise and outliers?
491. [Advanced] What is the computational complexity of DBSCAN? How do KD-trees and Ball trees help?
492. [Advanced] How would you apply DBSCAN to very high-dimensional data (embeddings)?
493. [Expert] What is HDBSCAN? How does it improve upon DBSCAN?
494. [Expert] Compare DBSCAN, OPTICS, and HDBSCAN. When would you use each?
495. [Advanced] Can DBSCAN handle non-Euclidean distance metrics? Give an example.
496. [Intermediate] When would DBSCAN fail to find meaningful clusters?
497. [Expert] Implement DBSCAN from scratch in Python.

### 6.3 Hierarchical Clustering

498. [Basic] What is hierarchical clustering? Explain agglomerative vs. divisive approaches.
499. [Intermediate] What is a dendrogram? How do you read it and choose the number of clusters?
500. [Intermediate] Compare linkage criteria: single, complete, average, and Ward's. When would you use each?
501. [Advanced] What are the advantages and disadvantages of different linkage methods?
502. [Advanced] What are the scalability challenges of hierarchical clustering? What is its computational complexity?
503. [Advanced] Is it possible for hierarchical clustering to produce inversions? What does this mean?
504. [Intermediate] How do you cut a dendrogram at a specific height or number of clusters?
505. [Advanced] Compare hierarchical clustering with K-Means. When is each preferable?
506. [Expert] How would you scale hierarchical clustering to large datasets? (BIRCH, CURE algorithms)
507. [Advanced] Can hierarchical clustering handle non-convex clusters? Depends on linkage.
508. [Expert] Implement agglomerative hierarchical clustering from scratch.

### 6.4 Gaussian Mixture Models (GMM)

509. [Intermediate] What is a Gaussian Mixture Model? How does it differ from K-Means?
510. [Intermediate] Explain the Expectation-Maximization (EM) algorithm in the context of GMM step by step.
511. [Advanced] Derive the E-step and M-step for fitting a GMM.
512. [Advanced] What are potential convergence issues with EM for GMMs? (Local optima, singularities)
513. [Advanced] How do you determine the number of components in a GMM? (AIC, BIC, silhouette analysis)
514. [Intermediate] What is the difference between hard clustering (K-Means) and soft clustering (GMM)?
515. [Advanced] Explain the role of covariance type (full, tied, diagonal, spherical) in GMMs. How does each affect cluster shapes?
516. [Expert] What assumptions does GMM make about the data? How would you handle non-elliptical clusters?
517. [Expert] Show mathematically how K-Means is a special case of GMM with hard assignments and isotropic covariance.
518. [Advanced] How do you initialize GMM parameters? Does initialization affect convergence?
519. [Expert] Implement GMM with the EM algorithm from scratch in Python.

### 6.5 Principal Component Analysis (PCA)

520. [Basic] What is PCA and why is it used?
521. [Intermediate] Explain the mathematical steps of PCA: centering, covariance matrix, eigendecomposition, projection.
522. [Intermediate] What is the explained variance ratio? How do you use it to decide how many components to keep?
523. [Advanced] Derive PCA from the perspective of maximizing variance of projections.
524. [Advanced] Derive PCA from the perspective of minimizing reconstruction error. Show they are equivalent.
525. [Intermediate] How does scaling/normalization affect PCA results? Why must you standardize first?
526. [Intermediate] Can PCA handle non-linear relationships? What alternatives exist?
527. [Advanced] What is Kernel PCA? How does it extend PCA to non-linear dimensionality reduction?
528. [Advanced] What are the limitations of PCA?
529. [Intermediate] What is the difference between PCA and SVD? How are they related?
530. [Advanced] Explain incremental PCA. When is it necessary?
531. [Advanced] Can PCA be used with sparse data? What challenges arise?
532. [Expert] Explain probabilistic PCA. What Bayesian interpretation does it provide?
533. [Expert] Implement PCA from scratch using numpy (eigendecomposition approach and SVD approach).
534. [Intermediate] How can you use PCA for data visualization?
535. [Advanced] Discuss a scenario where PCA led to loss of important information. How would you detect this?
536. [Advanced] What is the scree plot? How do you use it alongside the Kaiser criterion?
537. [Expert] Explain sparse PCA. How does it differ from standard PCA and when is it useful?
538. [Advanced] How does PCA relate to autoencoders? When does a linear autoencoder learn PCA?

### 6.6 t-SNE

539. [Intermediate] What is t-SNE? What is the main motivation behind it?
540. [Intermediate] How does t-SNE preserve local structure vs. global structure?
541. [Advanced] Explain the perplexity hyperparameter. What are the trade-offs of different values?
542. [Advanced] What is the cost function of t-SNE (KL divergence)? Why is the Student-t distribution used in the low-dimensional space?
543. [Advanced] What are the key limitations of t-SNE, especially with large datasets?
544. [Advanced] Why should t-SNE plots NOT be used for making clustering decisions?
545. [Expert] How do batch effects and random seeds influence t-SNE plots? How do you ensure reproducibility?
546. [Advanced] Compare t-SNE's cost function to that of classical MDS (Multidimensional Scaling).
547. [Advanced] Can t-SNE handle new, unseen data points (out-of-sample)? What are the limitations?
548. [Expert] Explain how Barnes-Hut approximation speeds up t-SNE. What is its time complexity?
549. [Advanced] How do you interpret distances and cluster sizes in t-SNE visualizations?
550. [Expert] Compare t-SNE with PCA for high-dimensional data visualization. When would you use each?

### 6.7 UMAP

551. [Intermediate] What is UMAP? How does it differ from t-SNE conceptually?
552. [Advanced] Describe the mathematical intuition behind UMAP (fuzzy topological structures, Riemannian manifolds).
553. [Advanced] How does UMAP compare to t-SNE in terms of speed, scalability, and global structure preservation?
554. [Advanced] Explain the n_neighbors, min_dist, and metric hyperparameters in UMAP.
555. [Advanced] How does UMAP handle new, unseen data (out-of-sample embedding)? How does this compare to t-SNE?
556. [Expert] Explain potential distortions that UMAP might introduce. How do you assess or trust the output?
557. [Advanced] When would you choose UMAP over t-SNE and vice versa?
558. [Expert] How does UMAP's theoretical foundation (algebraic topology) differ from t-SNE's (probability distributions)?
559. [Advanced] How would you use UMAP in combination with clustering algorithms?
560. [Expert] How do you use UMAP for supervised or semi-supervised dimensionality reduction?

### 6.8 Autoencoders for Dimensionality Reduction

561. [Intermediate] What is an autoencoder? How is it used for dimensionality reduction?
562. [Intermediate] Compare autoencoders with PCA for dimensionality reduction. When are autoencoders preferable?
563. [Advanced] What is a variational autoencoder (VAE)? How does it differ from a standard autoencoder?
564. [Advanced] Explain the bottleneck layer in autoencoders. How do you choose its dimensionality?
565. [Advanced] What are denoising autoencoders? How do they improve learned representations?
566. [Expert] Explain the relationship between a linear autoencoder and PCA. Prove they learn the same subspace.
567. [Advanced] How do you use autoencoders for anomaly detection?
568. [Expert] Implement a simple autoencoder in PyTorch for dimensionality reduction on MNIST.
569. [Advanced] What is the trade-off between reconstruction quality and latent space regularity in autoencoders?
570. [Expert] Explain contractive autoencoders and their regularization technique.

### 6.9 Association Rules

571. [Basic] What are association rules? Give an example from retail (market basket analysis).
572. [Basic] Define support, confidence, and lift. How do you interpret each?
573. [Intermediate] How does the Apriori algorithm work? Explain the key principle (downward closure).
574. [Intermediate] What are the limitations of the Apriori algorithm?
575. [Advanced] Why is the FP-Growth algorithm faster than Apriori? Explain the FP-tree data structure.
576. [Intermediate] When would you use association rules instead of supervised learning?
577. [Advanced] How do you handle the explosion of candidate itemsets in association rule mining?
578. [Intermediate] How can you use association rules for recommendation systems?
579. [Advanced] Give a scenario where high-confidence rules are misleading without considering lift.
580. [Expert] How would you implement association rule mining on a very large distributed dataset?
581. [Advanced] How do you interpret negative association rules?
582. [Expert] Implement the Apriori algorithm from scratch in Python.

### 6.10 Anomaly Detection

583. [Basic] What is anomaly detection? List real-world use cases.
584. [Intermediate] Describe the difference between supervised, semi-supervised, and unsupervised anomaly detection.
585. [Intermediate] How does the Isolation Forest algorithm work? Why is it effective for anomaly detection?
586. [Advanced] Explain One-Class SVM for anomaly detection. When would you use it?
587. [Advanced] How can clustering (e.g., DBSCAN) be used for anomaly detection?
588. [Intermediate] How do you handle imbalanced data in anomaly detection?
589. [Advanced] How do you tune the threshold for flagging anomalies?
590. [Advanced] What evaluation metrics are appropriate for anomaly detection?
591. [Advanced] What are the challenges in detecting contextual vs. collective anomalies?
592. [Expert] Design a fraud detection system using unsupervised anomaly detection. What features would you engineer?
593. [Advanced] How do autoencoders help with anomaly detection? What is the reconstruction error approach?
594. [Expert] Compare statistical methods (Z-score, Grubbs' test) with ML methods (Isolation Forest, LOF) for anomaly detection.
595. [Advanced] How would you detect anomalies in time series data?
596. [Expert] How do you handle concept drift in a production anomaly detection system?
597. [Advanced] What is Local Outlier Factor (LOF)? How does it define anomalies based on local density?

### 6.11 Topic Modeling (LDA)

598. [Basic] What is topic modeling? Why is it useful?
599. [Intermediate] Explain Latent Dirichlet Allocation (LDA). What are its main assumptions?
600. [Intermediate] Describe the generative process in LDA.
601. [Advanced] How do you interpret the document-topic distribution (θ) and topic-word distribution (β) in LDA?
602. [Intermediate] How do you choose the number of topics in LDA?
603. [Advanced] What are the hyperparameters α and β in LDA? How do they affect the output?
604. [Advanced] What is perplexity in topic modeling? How is it used for evaluation?
605. [Advanced] How do you evaluate topic coherence/quality?
606. [Intermediate] How does LDA compare to NMF (Non-negative Matrix Factorization) for topic modeling?
607. [Advanced] What are the limitations of LDA?
608. [Intermediate] How would you preprocess text data for LDA (tokenization, stopword removal, lemmatization)?
609. [Advanced] How can LDA be used for document classification or clustering?
610. [Expert] Explain the variational inference and Gibbs sampling approaches for fitting LDA. How do they differ?
611. [Expert] What are dynamic topic models? How do they capture topic evolution over time?
612. [Expert] Implement a simplified version of LDA using Gibbs sampling from scratch.

### 6.12 Evaluation of Unsupervised Methods

613. [Basic] Why is evaluating unsupervised learning harder than supervised learning?
614. [Intermediate] Explain the silhouette score. How is it calculated for each data point?
615. [Intermediate] What is the elbow method? How do you use it for choosing the number of clusters?
616. [Intermediate] What is the Davies-Bouldin Index? How does it measure cluster quality?
617. [Advanced] What is the Calinski-Harabasz Index? When is it preferred?
618. [Advanced] How do you evaluate clustering quality when ground truth labels are available? (ARI, NMI, V-measure)
619. [Advanced] What is the Adjusted Rand Index (ARI)? Why is adjustment for chance important?
620. [Advanced] What is Normalized Mutual Information (NMI)? How does it compare to ARI?
621. [Intermediate] How do you evaluate the quality of dimensionality reduction (reconstruction error, trustworthiness)?
622. [Advanced] What are internal vs. external clustering evaluation metrics? Give examples.
623. [Expert] How do you evaluate whether your clusters are meaningful for a business application?
624. [Advanced] What are stability-based methods for evaluating clustering? How do you assess cluster robustness?
625. [Expert] Design a complete evaluation framework for an unsupervised customer segmentation system.
626. [Advanced] How do you compare two different clustering algorithms on the same dataset?

### 6.13 Advanced Unsupervised Topics

627. [Advanced] How would you use clustering or PCA in conjunction with deep learning (e.g., for embeddings)?
628. [Expert] Explain the use of UMAP for visualizing embedding spaces from transformer models.
629. [Advanced] How would you adapt unsupervised techniques for real-time or streaming data?
630. [Expert] Discuss fairness or ethical issues in clustering (e.g., when used for market segmentation or hiring).
631. [Advanced] How do you handle mixed data types (numerical + categorical + text) in unsupervised learning?
632. [Expert] What is spectral clustering? How does it use the graph Laplacian?
633. [Expert] Explain the connection between spectral clustering and normalized graph cuts.
634. [Advanced] What is self-supervised learning? How does it bridge supervised and unsupervised learning?
635. [Expert] Explain contrastive learning (SimCLR, MoCo) as an unsupervised representation learning technique.
636. [Advanced] How do you choose between PCA, t-SNE, UMAP, and autoencoders for a dimensionality reduction task?
637. [Expert] What is manifold learning? Compare Isomap, LLE, and Laplacian Eigenmaps.
638. [Advanced] How do you handle the curse of dimensionality in unsupervised learning?
639. [Expert] Design an unsupervised pipeline for customer segmentation: feature engineering → dimensionality reduction → clustering → evaluation → business interpretation.
640. [Expert] Explain deep clustering methods (DEC, IDEC). How do they combine autoencoders with clustering?
641. [Advanced] How do you detect if your clustering result is meaningful or just an artifact of the algorithm?
642. [Expert] What is the gap statistic? How does it help determine the optimal number of clusters?
643. [Advanced] How do you handle very large datasets (100M+ rows) for clustering?
644. [Expert] Explain non-negative matrix factorization (NMF). When is it preferred over PCA?
645. [Advanced] How do you perform unsupervised feature selection? What methods exist?

---

## Quick Reference: Question Count by Category

| Category | Subcategory | Count |
|----------|-------------|-------|
| **4. ML Fundamentals** | 4.1 Bias-Variance & Regularization | 35 |
| | 4.2 Loss Functions & Optimization | 40 |
| | 4.3 Model Evaluation Metrics | 27 |
| | 4.4 Cross-Validation & Hyperparameter Tuning | 23 |
| | 4.5 Ensemble Methods | 25 |
| | 4.6 Feature Importance & Interpretability | 30 |
| | 4.7 Data Preprocessing & Feature Engineering | 20 |
| | 4.8 ML System Design & Production | 14 |
| **Subtotal Cat 4** | | **214** |
| **5. Supervised Learning** | 5.1 Linear Regression | 29 |
| | 5.2 Logistic Regression | 22 |
| | 5.3 Decision Trees | 19 |
| | 5.4 Random Forests | 14 |
| | 5.5 Gradient Boosting | 36 |
| | 5.6 SVMs | 26 |
| | 5.7 KNN | 15 |
| | 5.8 Naive Bayes | 15 |
| | 5.9 Time Series | 32 |
| | 5.10 Practical & Model Selection | 42 |
| **Subtotal Cat 5** | | **250** |
| **6. Unsupervised Learning** | 6.1 K-Means | 20 |
| | 6.2 DBSCAN | 13 |
| | 6.3 Hierarchical Clustering | 11 |
| | 6.4 GMM | 11 |
| | 6.5 PCA | 19 |
| | 6.6 t-SNE | 12 |
| | 6.7 UMAP | 10 |
| | 6.8 Autoencoders | 10 |
| | 6.9 Association Rules | 12 |
| | 6.10 Anomaly Detection | 15 |
| | 6.11 Topic Modeling (LDA) | 15 |
| | 6.12 Evaluation | 14 |
| | 6.13 Advanced Topics | 19 |
| **Subtotal Cat 6** | | **181** |
| **GRAND TOTAL** | | **645** |

---

*Compiled from FAANG interview guides, Glassdoor ML engineering interviews, ML engineering prep resources, and domain expert compilations. Updated 2024.*
