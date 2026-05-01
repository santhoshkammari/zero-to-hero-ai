# Part 8: Theory, Puzzles, Advanced Topics & Applications

> 700+ interview questions spanning mathematical brain teasers, learning theory, cutting-edge ML topics, and domain-specific applications. Each question tagged by difficulty: **[Basic]**, **[Intermediate]**, **[Advanced]**, **[Expert]**.

---

## E. Mathematical Brain Teasers & Probability Puzzles

### E.1 Birthday Problem & Variants

1. In a room of 23 people, what is the probability that at least two share a birthday? Derive the formula. **[Basic]**
2. How many people are needed in a room for a >50% chance that someone shares YOUR specific birthday? **[Intermediate]**
3. Generalize the birthday problem: given N equally likely categories and k samples, derive the collision probability. **[Intermediate]**
4. In the birthday problem, if the year has d days, derive the approximation using e^(-k(k-1)/(2d)). When does this approximation break down? **[Advanced]**
5. You have a hash function with 2^128 possible outputs. How many inputs must you hash before expecting a collision with probability > 50%? Relate this to the birthday problem. **[Advanced]**
6. In a group of n people, what is the expected number of birthday pairs (not just whether a pair exists)? **[Intermediate]**
7. Suppose birthdays are not uniformly distributed (some months are more popular). Does this increase or decrease the collision probability vs. the uniform case? Prove your answer. **[Expert]**
8. Three people are in a room. What is the probability that at least two share a birthday month? **[Basic]**
9. How does the birthday problem change if we consider birth hour (8,760 possibilities per year) instead of birth day? **[Intermediate]**
10. In a class of 50 students, what is the expected number of pairs sharing a birthday? **[Intermediate]**
11. Derive the birthday problem result using the Poisson approximation. Under what conditions is this valid? **[Advanced]**
12. In cryptography, the birthday attack reduces brute-force from O(2^n) to O(2^(n/2)). Explain the mathematical connection to the birthday paradox. **[Advanced]**
13. You are building a deduplication system for a dataset with 10 million records. Using a 64-bit hash, estimate the probability of at least one hash collision. **[Intermediate]**
14. Extend the birthday problem to "triples": how many people are needed for a >50% chance that three people share a birthday? **[Expert]**
15. If you randomly assign training samples to k GPU workers, what is the probability that at least two workers receive the same sample in a given batch? Relate to the birthday problem. **[Intermediate]**

### E.2 Monty Hall Problem & Bayesian Reasoning

16. Explain the Monty Hall problem. Why does switching give a 2/3 probability of winning? **[Basic]**
17. Generalize Monty Hall to n doors (1 car, n-1 goats). The host opens k doors (all goats). What is the probability of winning if you switch? **[Intermediate]**
18. In the Monty Hall problem, suppose the host opens a door randomly (might reveal the car). How does this change the analysis? **[Intermediate]**
19. A medical test has 99% sensitivity and 99% specificity. The disease prevalence is 1/10,000. You test positive. What is the probability you have the disease? **[Basic]**
20. You are screening emails for spam. Your classifier has 95% recall and 90% precision. If 5% of emails are spam, what fraction of flagged emails are actually spam? **[Intermediate]**
21. A drug test is 98% accurate. 0.5% of the population uses drugs. Given a positive test, what is P(user | positive)? **[Basic]**
22. You have two coins: one fair, one double-headed. You pick one at random and flip heads. What is the probability you picked the fair coin? **[Intermediate]**
23. You have three coins: P(H) = 0.3, 0.5, 0.7. You pick one at random and flip 3 heads in a row. What is the posterior probability for each coin? **[Intermediate]**
24. In a factory, Machine A produces 60% of parts with 2% defect rate. Machine B produces 40% with 5% defect rate. A part is defective — which machine likely produced it? **[Basic]**
25. How would you use Bayesian updating to update your belief about a model's accuracy as new test data arrives? **[Intermediate]**
26. You are playing a modified Monty Hall where the host has a 70% chance of opening the door nearest to the car. How does this affect the switching strategy? **[Advanced]**
27. Explain the difference between frequentist and Bayesian interpretations of the Monty Hall problem. **[Intermediate]**
28. A patient tests positive on two independent tests (sensitivity 95%, specificity 90% each). Disease prevalence is 1%. What is the posterior probability after both tests? **[Advanced]**
29. Explain how Bayes' theorem connects to the likelihood ratio and how this is used in sequential hypothesis testing. **[Advanced]**
30. You observe data D from a model with unknown parameter θ. Explain the relationship between the prior P(θ), likelihood P(D|θ), and posterior P(θ|D). When does the prior dominate? When does the likelihood dominate? **[Intermediate]**

### E.3 Expected Value Problems (Dice, Cards, Coins)

31. What is the expected value of a single fair six-sided die roll? **[Basic]**
32. You roll two fair dice. What is the expected value of their sum? Their product? **[Basic]**
33. You roll a fair die repeatedly until you get a 6. What is the expected number of rolls? **[Basic]**
34. You flip a fair coin until you get heads. What is the expected number of flips? **[Basic]**
35. You flip a fair coin repeatedly until you get two consecutive heads. What is the expected number of flips? **[Intermediate]**
36. You flip a fair coin until the pattern HTH appears. What is the expected number of flips? How does this differ from HHH? **[Advanced]**
37. You draw cards from a standard 52-card deck without replacement. What is the expected number of draws until you get the first ace? **[Intermediate]**
38. From a shuffled deck, you turn over cards one at a time. What is the expected position of the ace of spades? **[Basic]**
39. You roll a fair die and win $N where N is the number shown. What is the expected value? What if you can re-roll once (and must keep the second roll)? **[Intermediate]**
40. You roll a die. If you get a 6, you win $100. Otherwise, you lose $X. What value of X makes this a fair game? **[Basic]**
41. Two players take turns rolling a die. The first to roll a 6 wins. What is the probability the first player wins? **[Intermediate]**
42. You draw a card from a deck. If it's red, you get $1. If it's a face card, you get $5. If it's the ace of spades, you get $50. What is the expected payout? **[Intermediate]**
43. You have a biased coin with P(H) = p. What is the expected number of flips to see both a head and a tail? **[Intermediate]**
44. A casino game: you flip a fair coin until tails. You win 2^n dollars if heads appears n consecutive times. What is the expected payout (St. Petersburg paradox)? Why is this problematic? **[Advanced]**
45. You roll n fair dice simultaneously. What is the expected number of distinct values shown? **[Advanced]**
46. Compute E[max(X, Y)] where X and Y are independent uniform random variables on [0, 1]. Generalize to n variables. **[Intermediate]**
47. You play a game: start with $100. Each round you either double your money (p=0.6) or lose it all (p=0.4). What is the expected value after one round? After n rounds? Would you play? **[Intermediate]**
48. Derive the expected value of the geometric distribution from first principles. **[Intermediate]**
49. You roll a die repeatedly and keep a running sum. What is the expected number of rolls until the sum exceeds 100? **[Advanced]**
50. A stick of length 1 is broken at two random points. What is the expected length of the longest piece? **[Advanced]**

### E.4 Conditional Probability Brain Teasers

51. Two coins are tossed. Given that at least one is heads, what is the probability both are heads? **[Basic]**
52. A family has two children. Given that at least one is a boy, what is the probability both are boys? What if you know the elder child is a boy? **[Intermediate]**
53. A family has two children. You meet one child and it's a boy born on a Tuesday. What is the probability both children are boys? **[Advanced]**
54. Three prisoners A, B, C. One will be pardoned (chosen uniformly). A asks the guard to name one of the other two who will NOT be pardoned. The guard says "B." What is A's probability of pardon now? **[Intermediate]**
55. You have three cards: one red on both sides, one blue on both sides, one red on one side and blue on the other. You draw a card and see a red side. What is the probability the other side is also red? **[Intermediate]**
56. In the "boy or girl" paradox, why does "I have two children and one is a boy named John" change the probability that both are boys? **[Advanced]**
57. 100 lockers are all closed. 100 students walk by. Student 1 opens every locker. Student 2 toggles every 2nd locker. Student k toggles every kth locker. Which lockers are open at the end? **[Intermediate]**
58. You randomly seat n couples around a circular table. What is the probability that no couple sits adjacent? **[Expert]**
59. There are 100 people on a plane, and the first person sits in a random seat. Everyone else sits in their assigned seat if available, otherwise picks randomly. What is the probability the last person gets their assigned seat? **[Intermediate]**
60. You have n red and n blue socks in a drawer. You draw two at random. What is the probability they match? **[Basic]**
61. Five friends each flip a fair coin. What is the probability that one person's result differs from all others? **[Intermediate]**
62. You are told someone rolled two dice and the sum is even. What is the probability both dice show the same number? **[Intermediate]**
63. A jar has 3 red, 4 blue, and 5 green marbles. You draw two without replacement. Given the first was red, what is the probability the second is blue? **[Basic]**
64. You shuffle a deck of cards. What is the probability that the top two cards are both aces? What is the probability given that the top card is an ace? **[Basic]**
65. A test has a 5% false positive rate and 10% false negative rate. The prior probability of the condition is 2%. You test positive. Update your belief using Bayes' theorem. **[Intermediate]**

### E.5 Geometric Probability

66. Two people agree to meet at a coffee shop between 12:00 and 1:00 PM. Each arrives at a uniformly random time and waits 15 minutes. What is the probability they meet? **[Intermediate]**
67. A stick of length 1 is broken at two uniformly random points. What is the probability the three pieces form a triangle? **[Intermediate]**
68. You drop a needle of length L on a plane with parallel lines spaced D apart (D ≥ L). What is the probability the needle crosses a line? (Buffon's needle) **[Advanced]**
69. Two points are chosen uniformly at random on the circumference of a circle. What is the probability the chord they define is longer than the side of an inscribed equilateral triangle? **[Intermediate]**
70. A point is chosen uniformly at random inside a unit square. What is the expected distance to the nearest edge? **[Intermediate]**
71. Two points are chosen uniformly inside a unit square. What is the expected distance between them? **[Advanced]**
72. A point is chosen uniformly at random inside a unit circle. What is the expected distance from the center? **[Intermediate]**
73. Three points are chosen uniformly at random on a circle. What is the probability they all lie on the same semicircle? **[Intermediate]**
74. You throw a dart uniformly at random at a circular dartboard of radius R. What is the expected distance from the center? **[Basic]**
75. A square with side 1 has a circle of radius 1/2 inscribed in it. A point is chosen uniformly in the square. What is the probability it falls in the circle? **[Basic]**
76. Explain how geometric probability can be used for Monte Carlo estimation of π. **[Basic]**
77. You randomly choose a point inside a triangle with vertices at (0,0), (1,0), (0,1). What is the expected distance to the origin? **[Advanced]**
78. Extend Buffon's needle: what if the needle length L > D (the line spacing)? **[Expert]**

### E.6 Markov Chain Puzzles

79. A frog jumps between lily pads 1, 2, 3 with equal probability of jumping to any other pad. Starting at pad 1, what is the expected number of jumps to return to pad 1? **[Intermediate]**
80. A gambler starts with $k. Each round he wins $1 with probability p or loses $1 with probability 1-p. What is the probability he goes bankrupt before reaching $N? (Gambler's ruin) **[Intermediate]**
81. A drunk man stands at position 0 on a number line and takes steps of +1 or -1 with equal probability. What is the expected number of steps to reach position +n for the first time? **[Advanced]**
82. You have a 1D random walk starting at 0 with absorbing barriers at -a and +b. What is the probability of being absorbed at +b? **[Advanced]**
83. A Markov chain has states {A, B, C}. From A: go to B (0.5) or C (0.5). From B: go to A (1.0). From C: stay at C (1.0). What are the absorbing states? What is the probability of absorption in C starting from A? **[Intermediate]**
84. A mouse is in room 1 of 3 rooms. Room 3 has cheese (absorbing). From room 1, equal probability of going to room 2 or room 3. From room 2, equal probability of room 1 or room 3. Expected steps to reach room 3 starting from room 1? **[Intermediate]**
85. Show that the stationary distribution of a simple random walk on a complete graph with n nodes is uniform. **[Intermediate]**
86. PageRank can be modeled as a Markov chain. Explain the damping factor and its effect on convergence. **[Intermediate]**
87. Prove that an irreducible, aperiodic, finite Markov chain has a unique stationary distribution. **[Advanced]**
88. A simplified weather model: if sunny today, tomorrow is sunny (0.8) or rainy (0.2). If rainy today, tomorrow is sunny (0.4) or rainy (0.6). What fraction of days are sunny in the long run? **[Intermediate]**
89. A particle starts at state 0 on {0, 1, 2, ..., n} with reflecting barrier at 0 and absorbing barrier at n. What is the expected time to absorption? **[Advanced]**
90. You shuffle cards by repeatedly choosing two random cards and swapping them. Model this as a Markov chain. How many swaps until the deck is approximately random? **[Expert]**
91. Explain the mixing time of a Markov chain. Why is rapid mixing important in MCMC methods for ML? **[Advanced]**
92. Design a Markov chain whose stationary distribution is a given target distribution π. Explain the Metropolis-Hastings algorithm. **[Intermediate]**

### E.7 Random Walk Problems

93. In a symmetric 1D random walk, what is the probability of returning to the origin? (Pólya's recurrence theorem in 1D) **[Intermediate]**
94. What happens to the return probability in a symmetric random walk in 2D? In 3D? Why is the 3D case fundamentally different? **[Advanced]**
95. A random walk on Z starts at 0. After n steps, what is the expected absolute displacement? **[Intermediate]**
96. In a 1D random walk with absorbing barriers at 0 and N, starting at k, derive the absorption probabilities. **[Advanced]**
97. A particle does a random walk on a cycle graph of n nodes. What is the expected time to visit all nodes (cover time)? **[Expert]**
98. Relate the random walk on a graph to the eigenvalues of the graph Laplacian. **[Expert]**
99. How is the random walk used in the Word2Vec Skip-gram model (DeepWalk)? **[Intermediate]**
100. A 2D random walk on a grid: starting at origin, what is the expected number of steps to reach distance d from the origin? **[Advanced]**
101. Explain how random walks are used in graph-based semi-supervised learning (label propagation). **[Intermediate]**
102. You have a biased random walk with P(+1) = p > 1/2. What is the expected first passage time to reach position +n? **[Advanced]**

### E.8 Coupon Collector Problem

103. There are n distinct coupons. Each purchase gives you one coupon uniformly at random. What is the expected number of purchases to collect all n coupons? **[Intermediate]**
104. Derive the coupon collector's expected value using the harmonic series: E = n·H_n. **[Intermediate]**
105. In the coupon collector problem, what is the variance of the total number of purchases? **[Advanced]**
106. You are collecting Pokémon cards. There are 151 unique cards. What is the expected number of packs to buy to collect them all? **[Basic]**
107. Relate the coupon collector problem to the expected number of random samples needed to see every class at least once in a k-class classification dataset. **[Intermediate]**
108. How does the coupon collector problem change if coupons have non-uniform probabilities? **[Advanced]**
109. You are randomly sampling mini-batches with replacement from a dataset of N items. After how many samples (in expectation) will you have seen every data point at least once? **[Intermediate]**
110. In the coupon collector problem with n coupons, what is the probability that all coupons are collected in at most n·H_n + n·t purchases (concentration inequality)? **[Expert]**
111. A company runs random A/B test assignments. There are k variants. What is the expected number of visitors before every variant has been tested at least once? **[Intermediate]**

### E.9 Secretary Problem / Optimal Stopping

112. You interview N candidates one at a time. You must accept or reject each immediately. What strategy maximizes the probability of hiring the best candidate? **[Intermediate]**
113. Prove that the optimal strategy for the secretary problem is to reject the first N/e candidates, then accept the next one who is best so far. **[Advanced]**
114. What is the probability of selecting the best candidate using the optimal stopping strategy? Show it converges to 1/e ≈ 36.8%. **[Advanced]**
115. How does the secretary problem relate to optimal stopping in online learning (explore-exploit tradeoff)? **[Intermediate]**
116. You are shopping for a house. You will see N houses, one per day. How would you adapt the secretary problem strategy if you can go back to a previous house with probability p? **[Advanced]**
117. Relate the secretary problem to the multi-armed bandit problem in ML. **[Intermediate]**
118. In a modified secretary problem, you can hire up to k candidates. How does the optimal strategy change? **[Expert]**
119. Explain how the secretary problem relates to early stopping in neural network training. **[Intermediate]**

### E.10 Estimation Problems (Fermi Questions for ML)

120. Estimate the number of parameters in GPT-3. How much memory is needed to store them in float16? **[Basic]**
121. How much compute (FLOPs) is roughly needed to train a 175B parameter language model? **[Intermediate]**
122. Estimate the size of the Common Crawl dataset in tokens. **[Intermediate]**
123. How many labeled ImageNet images would you need to annotate per day to complete the dataset in one year? Estimate annotation time per image. **[Basic]**
124. Estimate the number of Google searches per day. How many of those might benefit from ML-generated answers? **[Basic]**
125. How much energy (kWh) does a single inference call to a large language model consume? Estimate the carbon footprint. **[Intermediate]**
126. Estimate the total number of ML engineers worldwide. **[Basic]**
127. How many NVIDIA H100 GPUs would you need to train a model equivalent to GPT-4? Estimate training time. **[Advanced]**
128. Estimate the number of floating-point operations your laptop's GPU can perform per second. How long would it take to train a ResNet-50 on ImageNet on a single laptop GPU? **[Intermediate]**
129. How many parameters can fit in the L2 cache of a modern CPU? What implications does this have for model inference? **[Advanced]**
130. Estimate the number of distinct words in the English language. How does this compare to typical tokenizer vocabulary sizes? **[Basic]**
131. How many recommendation requests does Netflix process per second? Estimate the latency budget for each. **[Intermediate]**
132. Estimate the total number of images on the internet. What fraction are useful for pre-training a vision model? **[Intermediate]**

### E.11 Matrix Puzzles & Linear Algebra Riddles

133. You have a 2×2 matrix A with eigenvalues 2 and 3. What are the eigenvalues of A², A⁻¹, and A + I? **[Basic]**
134. A matrix A satisfies A² = A. What are its possible eigenvalues? What is such a matrix called? **[Basic]**
135. Prove that a real symmetric matrix has only real eigenvalues. **[Intermediate]**
136. If A is an n×n matrix with rank 1, how many zero eigenvalues does it have? **[Basic]**
137. Given an n×n orthogonal matrix Q, what are the possible values of det(Q)? **[Basic]**
138. You perform PCA on data in R^100 and the first eigenvalue of the covariance matrix is 1000 while the rest are each 1. How much variance does the first principal component explain? **[Basic]**
139. A 3×3 matrix has eigenvalues 1, 2, 3. What is its determinant? Its trace? **[Basic]**
140. Prove that the trace of a matrix equals the sum of its eigenvalues. **[Advanced]**
141. Why is the condition number of a matrix important in numerical optimization? Relate to gradient descent convergence. **[Intermediate]**
142. If A is positive semi-definite, prove that all its eigenvalues are non-negative. **[Intermediate]**
143. You are given that AB has eigenvalue λ. Does BA also have eigenvalue λ? Prove or give counterexample. **[Advanced]**
144. What is the rank of the outer product of two non-zero vectors u·v^T? **[Basic]**
145. Explain why SVD is more numerically stable than eigendecomposition for computing PCA. **[Intermediate]**
146. You have a sparse matrix with 1 million rows and 1 million columns but only 10 million non-zero entries. How would you efficiently compute its top-k singular values? **[Advanced]**
147. A linear transformation T maps R² to R² and doubles all areas. What is |det(T)|? **[Basic]**
148. Prove that the column space and row space of a matrix have the same dimension. **[Intermediate]**
149. What is the geometric interpretation of a matrix with determinant zero? **[Basic]**
150. Prove: for any matrix A, rank(A^T A) = rank(A). **[Advanced]**
151. If A is a rotation matrix in 2D by angle θ, what are its eigenvalues? Explain why they are complex for θ ≠ 0, π. **[Intermediate]**
152. Given a Gram matrix G where G_ij = <x_i, x_j>, prove that G is positive semi-definite. **[Intermediate]**
153. Why does the matrix (X^T X)^(-1) X^T y give the least-squares solution? Derive from the normal equations. **[Intermediate]**
154. What is the Sherman-Morrison formula? Give a practical application in online learning when you add one data point. **[Advanced]**
155. Explain the connection between the nuclear norm of a matrix and low-rank matrix completion. **[Expert]**

---

## F. Learning Theory & Theoretical ML

### F.1 PAC Learning

156. Define Probably Approximately Correct (PAC) learning. What are the roles of ε and δ? **[Basic]**
157. What does it mean for a hypothesis class H to be PAC-learnable? **[Basic]**
158. Derive the sample complexity for PAC learning a finite hypothesis class in the realizable setting. **[Intermediate]**
159. What is the difference between "realizable" and "agnostic" PAC learning? How do sample complexity bounds differ? **[Intermediate]**
160. Explain the Empirical Risk Minimization (ERM) principle. Under what conditions does ERM lead to PAC learning? **[Intermediate]**
161. If a concept class has VC dimension d, what is the sample complexity for PAC learning it (up to constants)? **[Intermediate]**
162. Can every concept class be PAC-learned? What are the necessary and sufficient conditions? **[Advanced]**
163. Explain the No Free Lunch theorem for PAC learning. What does it imply about universal learners? **[Intermediate]**
164. In the PAC framework, what role does the distribution D over instances play? Does the learner need to know D? **[Basic]**
165. Compare PAC learning with online learning. What are the key differences in assumptions and guarantees? **[Intermediate]**
166. What is the fundamental theorem of statistical learning? State it formally. **[Advanced]**
167. Explain the concept of "proper" vs "improper" PAC learning. Give an example of improper learning. **[Intermediate]**
168. How does noise affect PAC learnability? Define the PAC learning model with random classification noise. **[Advanced]**
169. What is the relationship between PAC learning and Occam's razor? **[Intermediate]**
170. Explain the concept of efficient PAC learning. Why is polynomial sample complexity not sufficient; we also need polynomial time? **[Advanced]**

### F.2 VC Dimension

171. Define the VC (Vapnik-Chervonenkis) dimension of a hypothesis class. **[Basic]**
172. What does it mean for a hypothesis class to "shatter" a set of points? **[Basic]**
173. What is the VC dimension of the class of linear classifiers (half-spaces) in R^d? Prove it. **[Intermediate]**
174. What is the VC dimension of intervals on the real line? Of axis-aligned rectangles in R²? **[Intermediate]**
175. Prove that the VC dimension of the class of threshold functions over R is 1. **[Intermediate]**
176. What is the VC dimension of the class of all subsets of a finite domain of size n? **[Intermediate]**
177. A hypothesis class has VC dimension d. Using Sauer's lemma, upper-bound the number of distinct labelings on m points. **[Advanced]**
178. State Sauer's lemma (Sauer-Shelah lemma). What is its significance in learning theory? **[Intermediate]**
179. Can a hypothesis class with infinite VC dimension be PAC-learnable? Justify. **[Advanced]**
180. What is the VC dimension of a neural network with d weights? What bounds are known? **[Advanced]**
181. What is the VC dimension of the class of circles in R²? (classify points inside/outside) **[Intermediate]**
182. What is the VC dimension of k-nearest neighbor classifiers? **[Advanced]**
183. Prove that adding a bias term to a linear classifier increases the VC dimension by 1. **[Advanced]**
184. Explain the relationship between VC dimension and the number of free parameters of a model. Why are they not always equal? **[Advanced]**
185. What is the VC dimension of decision trees of depth d over binary features? **[Expert]**
186. How is the VC dimension used in deriving generalization bounds? State the VC generalization bound. **[Intermediate]**
187. What is the fat-shattering dimension? How does it extend VC dimension to regression? **[Expert]**

### F.3 Rademacher Complexity

188. Define Rademacher complexity. How does it measure the richness of a hypothesis class? **[Intermediate]**
189. What is the relationship between Rademacher complexity and generalization bounds? State the bound. **[Advanced]**
190. Compare Rademacher complexity with VC dimension as measures of hypothesis class complexity. When is one preferred? **[Advanced]**
191. Compute the Rademacher complexity of the class of linear functions with bounded norm. **[Advanced]**
192. How does Rademacher complexity depend on the sample size? What does this tell us about generalization? **[Intermediate]**
193. Explain how Rademacher complexity captures data-dependent complexity, unlike VC dimension. **[Advanced]**
194. What is the empirical Rademacher complexity? How is it estimated in practice? **[Advanced]**
195. Show that the Rademacher complexity of a finite hypothesis class of size |H| is at most sqrt(2 log|H| / n). **[Expert]**
196. How does L2 regularization reduce the Rademacher complexity of linear models? **[Advanced]**
197. Explain the contraction lemma (Talagrand's lemma) for Rademacher complexity. **[Expert]**

### F.4 Bias-Complexity Tradeoff (Formal)

198. Define approximation error and estimation error in the context of learning theory. **[Basic]**
199. Explain the bias-complexity (bias-variance) tradeoff in terms of hypothesis class size. **[Basic]**
200. If you increase the complexity of your hypothesis class, what happens to approximation error? Estimation error? **[Basic]**
201. Derive the decomposition of expected risk into approximation error and estimation error. **[Intermediate]**
202. How do structural risk minimization (SRM) principles balance bias and complexity? **[Intermediate]**
203. Explain the double descent phenomenon. How does it challenge the classical bias-variance tradeoff? **[Advanced]**
204. What role does model interpolation play in the double descent curve? **[Advanced]**
205. Explain benign overfitting. Under what conditions can a model perfectly fit noisy training data and still generalize? **[Expert]**
206. How does regularization affect the bias-complexity tradeoff? Give a formal argument using generalization bounds. **[Intermediate]**
207. Relate the bias-complexity tradeoff to the choice of neural network width and depth. **[Advanced]**

### F.5 Generalization Bounds

208. State the Hoeffding inequality. How is it used to derive generalization bounds? **[Intermediate]**
209. What is uniform convergence? Why is it important for generalization? **[Intermediate]**
210. Derive a generalization bound for a finite hypothesis class using the union bound and Hoeffding's inequality. **[Intermediate]**
211. State the VC generalization bound. What are its strengths and limitations? **[Advanced]**
212. What are PAC-Bayes bounds? How do they improve upon VC-type bounds for practical models? **[Advanced]**
213. Explain the margin-based generalization bound for SVMs. Why do larger margins imply better generalization? **[Intermediate]**
214. How do norm-based generalization bounds work for neural networks? Why are they tighter than VC dimension bounds? **[Advanced]**
215. What is the McAllester PAC-Bayes bound? How does it connect Bayesian learning to generalization? **[Expert]**
216. Explain the compression-based generalization bound. If a learning algorithm compresses the training data, what does this imply? **[Advanced]**
217. Why are VC dimension-based bounds often vacuous for deep neural networks? What alternatives exist? **[Advanced]**
218. How does algorithmic stability lead to generalization bounds? Define uniform stability. **[Expert]**
219. Explain the relationship between mutual information and generalization bounds. **[Expert]**
220. What is the chaining technique in empirical process theory? How does it give tighter bounds than Rademacher complexity alone? **[Expert]**

### F.6 No Free Lunch Theorem

221. State the No Free Lunch (NFL) theorem for machine learning. **[Basic]**
222. What are the practical implications of the NFL theorem for ML practitioners? **[Basic]**
223. Does the NFL theorem mean that all learning algorithms perform equally? Explain the subtlety. **[Intermediate]**
224. How does the NFL theorem relate to the importance of inductive bias? **[Intermediate]**
225. Prove a simplified version of the NFL theorem for binary classification with a uniform distribution over all possible target functions. **[Advanced]**
226. How does the NFL theorem reconcile with the empirical observation that deep learning works well across many tasks? **[Intermediate]**
227. Explain the difference between the NFL theorem in optimization and the NFL theorem in supervised learning. **[Advanced]**

### F.7 Universal Approximation Theorem

228. State the universal approximation theorem for neural networks. **[Basic]**
229. Does the universal approximation theorem guarantee that neural networks will learn any function? Explain the gap between approximation and learning. **[Intermediate]**
230. What are the requirements on the activation function for the universal approximation theorem to hold? **[Intermediate]**
231. The universal approximation theorem guarantees a sufficiently wide network can approximate any continuous function. What about depth — are there functions that require exponential width with bounded depth? **[Advanced]**
232. Compare the universal approximation theorem for width (Cybenko/Hornik) vs. for depth (Telgarsky, Eldan-Shamir). **[Advanced]**
233. How does the universal approximation theorem relate to the representation power vs. learnability debate? **[Intermediate]**
234. Do transformers satisfy a universal approximation theorem? What has been shown? **[Advanced]**
235. What is the practical relevance of the universal approximation theorem given that SGD may not find the optimal weights? **[Intermediate]**

### F.8 Convergence Rates of Optimization Algorithms

236. What is the convergence rate of gradient descent for convex functions with L-Lipschitz gradients? **[Intermediate]**
237. Define strong convexity. How does it improve the convergence rate of gradient descent? **[Intermediate]**
238. What is the convergence rate of SGD? How does it compare to full-batch gradient descent? **[Intermediate]**
239. Explain the role of the learning rate in the convergence of SGD. What is the optimal learning rate schedule for convex objectives? **[Advanced]**
240. What is the convergence rate of Adam? Under what conditions does Adam fail to converge? **[Advanced]**
241. Explain the difference between O(1/t) and O(1/√t) convergence rates in stochastic optimization. When does each apply? **[Advanced]**
242. What is the Polyak-Łojasiewicz (PL) condition? How does it enable linear convergence for non-convex functions? **[Advanced]**
243. Prove that gradient descent with step size 1/L converges at rate O(1/t) for smooth convex functions. **[Advanced]**
244. What is Nesterov's accelerated gradient descent? What convergence rate does it achieve and why is it optimal? **[Advanced]**
245. Explain the role of momentum in accelerating convergence. Relate to the condition number of the optimization problem. **[Intermediate]**
246. What is the convergence rate of coordinate descent? When is it preferable to gradient descent? **[Advanced]**
247. Explain the effect of mini-batch size on SGD convergence rate. Is there a critical batch size? **[Advanced]**
248. What are lower bounds for first-order optimization methods? State Nesterov's lower bound. **[Expert]**

### F.9 Information-Theoretic Limits

249. What is Fano's inequality? How does it provide lower bounds on classification error? **[Advanced]**
250. Explain the connection between mutual information I(X;Y) and the minimum achievable prediction error for Y given X. **[Advanced]**
251. What is the information bottleneck method? How does it relate to representation learning? **[Advanced]**
252. Explain Le Cam's method for deriving minimax lower bounds. **[Expert]**
253. What is the minimax rate of estimation for a d-dimensional Gaussian mean? **[Advanced]**
254. How does the data processing inequality constrain what learned representations can capture? **[Intermediate]**
255. Explain rate-distortion theory. How does it relate to lossy compression in autoencoders? **[Advanced]**
256. What is the information-theoretic lower bound for the sample complexity of learning a d-dimensional linear classifier? **[Expert]**
257. How does Assouad's lemma provide minimax lower bounds? Give an example application. **[Expert]**
258. Explain the connection between differential entropy and the quality of generative models. **[Advanced]**
259. What is the role of entropy in decision tree splitting? Derive the information gain criterion from first principles. **[Intermediate]**

### F.10 Computational Complexity of ML Algorithms

260. What is the computational complexity of training a linear SVM with n samples and d features using SMO? **[Intermediate]**
261. What is the time complexity of performing k-means clustering with k clusters, n points, d dimensions, for t iterations? **[Basic]**
262. Why is exact inference in general Bayesian networks NP-hard? **[Advanced]**
263. What is the computational complexity of the backpropagation algorithm for a fully connected network with L layers? **[Intermediate]**
264. Why is training a neural network NP-hard in general, yet SGD works well in practice? **[Advanced]**
265. What is the computational complexity of exact nearest-neighbor search in d dimensions? How do approximate methods (LSH, ANN) reduce this? **[Intermediate]**
266. Explain why kernel methods scale as O(n³) for training and O(n) for prediction. How do approximations like Nyström and random features help? **[Advanced]**
267. What is the computational complexity of computing the SVD of an m×n matrix? **[Intermediate]**
268. Why is finding the optimal decision tree NP-complete? What heuristics make it tractable? **[Advanced]**
269. What is the complexity of the Viterbi algorithm for HMMs with T time steps and N states? **[Intermediate]**
270. Explain the computational bottleneck in self-attention (O(n²)) and methods to reduce it (linear attention, sparse attention). **[Advanced]**
271. What is the time complexity of random forest training and inference? How does it scale with the number of trees? **[Intermediate]**
272. What is the EM algorithm's computational complexity per iteration? Does EM guarantee convergence to the global optimum? **[Intermediate]**

### F.11 Sample Complexity

273. What is sample complexity? How does it differ from computational complexity? **[Basic]**
274. Derive the sample complexity for learning a d-dimensional linear classifier in the PAC framework. **[Intermediate]**
275. How does sample complexity scale with VC dimension? State the upper and lower bounds. **[Intermediate]**
276. In the agnostic learning setting, how much more data is needed compared to the realizable setting? **[Advanced]**
277. What is the sample complexity of learning a mixture of k Gaussians? **[Expert]**
278. How does active learning reduce sample complexity? Give a formal example where active learning has exponentially better sample complexity than passive learning. **[Advanced]**
279. What is the sample complexity of kernel SVMs in terms of the margin? **[Advanced]**
280. Explain the information-theoretic vs. computational sample complexity gap. Give an example where they differ. **[Expert]**
281. How does data augmentation effectively increase the sample size? Is there a formal framework for this? **[Advanced]**
282. What is the sample complexity of learning with distribution shift (domain adaptation)? **[Expert]**
283. In few-shot learning, how do meta-learning approaches achieve low effective sample complexity? **[Advanced]**

### F.12 Kernel Theory & RKHS

284. What is a kernel function? State Mercer's theorem. **[Basic]**
285. What is a Reproducing Kernel Hilbert Space (RKHS)? Define the reproducing property. **[Intermediate]**
286. Explain the kernel trick. Why does it allow SVMs to operate in infinite-dimensional spaces? **[Basic]**
287. Prove that the Gaussian (RBF) kernel corresponds to an infinite-dimensional feature space. **[Advanced]**
288. What is the representer theorem? Why is it important for kernel methods? **[Intermediate]**
289. Compare the polynomial kernel, RBF kernel, and linear kernel. When would you use each? **[Basic]**
290. What is a characteristic kernel? Why does it matter for kernel two-sample tests (MMD)? **[Advanced]**
291. Explain the connection between Gaussian processes and kernel methods through RKHS. **[Advanced]**
292. What is the kernel alignment and how is it used for kernel selection? **[Advanced]**
293. Explain multiple kernel learning (MKL). When is it beneficial? **[Advanced]**
294. How do random Fourier features approximate the RBF kernel? What is the approximation error? **[Advanced]**
295. What is the Nyström approximation for kernel matrices? How does it reduce computational cost? **[Intermediate]**
296. Explain why deep neural networks can be viewed through the lens of the Neural Tangent Kernel (NTK). **[Expert]**
297. What is the kernel PCA algorithm? How does it differ from standard PCA? **[Intermediate]**
298. Prove that any positive definite function is a valid kernel (one direction of Mercer's theorem). **[Advanced]**
299. What happens to the RKHS norm of the solution as regularization decreases? Relate to overfitting. **[Intermediate]**
300. Explain the connection between kernel ridge regression and Gaussian process regression. **[Advanced]**
301. What is the spectral decay of a kernel matrix and why does it matter for generalization? **[Expert]**
302. Describe the kernel trick for computing distances in feature space without explicit feature maps. **[Intermediate]**

---

## G. Advanced & Niche Topics

### G.1 Graph Neural Networks

303. What is the message-passing paradigm in GNNs? Describe the aggregate-update framework. **[Basic]**
304. Explain the Graph Convolutional Network (GCN). How does it approximate spectral convolutions? **[Intermediate]**
305. How does the Graph Attention Network (GAT) differ from GCN? What attention mechanism does it use? **[Intermediate]**
306. Explain GraphSAGE and its inductive learning capability. How does it differ from transductive methods like GCN? **[Intermediate]**
307. What is the over-smoothing problem in deep GNNs? How does it relate to the number of message-passing layers? **[Intermediate]**
308. Describe techniques to mitigate over-smoothing in GNNs (residual connections, JK-Net, DropEdge). **[Advanced]**
309. Compare spectral and spatial approaches to graph convolution. What are the tradeoffs? **[Advanced]**
310. How do you handle heterogeneous graphs (multiple node/edge types) in GNNs? **[Intermediate]**
311. What is the Weisfeiler-Leman (WL) graph isomorphism test? How does it relate to the expressiveness of GNNs? **[Advanced]**
312. Prove that standard message-passing GNNs are at most as powerful as the 1-WL test. What are higher-order GNNs? **[Expert]**
313. How do you incorporate edge features into message-passing GNNs? **[Intermediate]**
314. Explain the GNN architecture used in AlphaFold for protein structure prediction. **[Advanced]**
315. How would you scale a GNN to a billion-node graph? Describe sampling strategies (GraphSAGE, ClusterGCN, GraphSAINT). **[Advanced]**
316. What are positional encodings in graph transformers? Why are they needed (unlike in standard GNNs)? **[Advanced]**
317. How do you perform link prediction with GNNs? Describe common approaches. **[Intermediate]**
318. Explain the concept of graph pooling. Compare DiffPool, SAGPool, and global mean/sum pooling. **[Advanced]**
319. How do GNNs handle dynamic (temporal) graphs? Describe temporal graph networks. **[Advanced]**
320. What is the relationship between GNNs and belief propagation on graphical models? **[Expert]**
321. Explain the expressive power limitations of GNNs for detecting certain graph substructures (e.g., triangles). **[Advanced]**
322. How are GNNs used for molecular property prediction? What graph representations are used for molecules? **[Intermediate]**
323. Describe the use of GNNs in combinatorial optimization (e.g., TSP, graph coloring). **[Advanced]**
324. What is a graph transformer? How does it differ from message-passing GNNs? **[Intermediate]**
325. Explain the SignNet and BasisNet approaches for handling sign ambiguity in graph eigenvector features. **[Expert]**

### G.2 Self-Supervised Learning

326. What is self-supervised learning? How does it differ from unsupervised and supervised learning? **[Basic]**
327. Explain the contrastive learning framework. What are positive and negative pairs? **[Basic]**
328. Describe the SimCLR architecture and training procedure. Why does it need large batch sizes? **[Intermediate]**
329. How does BYOL (Bootstrap Your Own Latent) work without negative samples? Why doesn't it collapse to trivial solutions? **[Advanced]**
330. Explain the role of the momentum encoder in MoCo and BYOL. How does the momentum parameter affect training? **[Advanced]**
331. What is the InfoNCE loss? Derive it from mutual information maximization. **[Advanced]**
332. Describe DINO (self-distillation with no labels). How does it produce attention maps that segment objects? **[Advanced]**
333. What is representation collapse in self-supervised learning? What mechanisms prevent it? **[Intermediate]**
334. Compare contrastive (SimCLR, MoCo), non-contrastive (BYOL, SimSiam), and clustering-based (SwAV, DeepCluster) self-supervised methods. **[Advanced]**
335. Explain the role of data augmentation in self-supervised learning. Which augmentations are critical for vision tasks? **[Intermediate]**
336. What is the projection head in contrastive learning? Why do representations before the projection head transfer better than those after? **[Advanced]**
337. Explain Barlow Twins. How does its redundancy-reduction objective differ from contrastive loss? **[Advanced]**
338. How does VICReg prevent collapse? What do the variance, invariance, and covariance terms do? **[Advanced]**
339. Describe MAE (Masked Autoencoder). How does masking work as a self-supervised pretext task for vision? **[Intermediate]**
340. What is the connection between self-supervised learning and the information bottleneck principle? **[Expert]**
341. How do self-supervised pre-trained models compare to supervised pre-trained models for transfer learning? **[Intermediate]**
342. Explain how contrastive learning can be viewed as a form of metric learning. **[Intermediate]**
343. What are the main pretext tasks used in NLP self-supervised learning (masked language modeling, next sentence prediction, etc.)? **[Basic]**
344. How has DINO v2 improved upon the original DINO? What architectural and training changes were made? **[Advanced]**
345. Explain the theoretical justification for why self-supervised learning learns useful representations (e.g., augmentation invariance hypothesis). **[Expert]**

### G.3 Meta-Learning

346. Define meta-learning. What does "learning to learn" mean? **[Basic]**
347. Compare model-based, metric-based, and optimization-based meta-learning approaches. Give examples of each. **[Intermediate]**
348. Explain MAML (Model-Agnostic Meta-Learning). What is the inner loop? What is the outer loop? **[Intermediate]**
349. How does Reptile differ from MAML? What are the computational advantages? **[Intermediate]**
350. Explain Prototypical Networks. How do they perform few-shot classification? **[Intermediate]**
351. What is the N-way K-shot classification setup? How is it used to evaluate meta-learning methods? **[Basic]**
352. Describe Matching Networks. How do they use attention for few-shot learning? **[Intermediate]**
353. What is the computational cost of second-order MAML? How does first-order MAML (FOMAML) approximate it? **[Advanced]**
354. How does task distribution affect meta-learning performance? What happens when test tasks differ from training tasks? **[Advanced]**
355. Explain the relationship between meta-learning and transfer learning. When would you prefer one over the other? **[Intermediate]**
356. How is meta-learning used for hyperparameter optimization (learning learning rates, architectures, etc.)? **[Advanced]**
357. Describe the task-augmented meta-learning approach for handling task scarcity. **[Advanced]**
358. What is meta-overfitting? How do you detect and prevent it? **[Advanced]**
359. Explain how meta-learning can be applied to reinforcement learning (Meta-RL). Give an example. **[Advanced]**
360. How does Relation Network differ from Prototypical Networks for few-shot classification? **[Intermediate]**
361. Describe LEO (Latent Embedding Optimization) and how it addresses the limitations of MAML in high-dimensional parameter spaces. **[Expert]**
362. How does meta-learning relate to the Bayesian framework? Explain Neural Processes. **[Expert]**
363. What is the CAVIA approach to meta-learning and how does it reduce the number of inner-loop parameters? **[Advanced]**

### G.4 Continual / Lifelong Learning

364. What is catastrophic forgetting? Why does it occur in neural networks? **[Basic]**
365. Describe the three main approaches to continual learning: regularization-based, replay-based, and architecture-based. **[Intermediate]**
366. Explain Elastic Weight Consolidation (EWC). How does the Fisher information matrix identify important weights? **[Intermediate]**
367. How does Progressive Neural Networks handle continual learning? What are its limitations? **[Intermediate]**
368. Describe experience replay and episodic memory approaches for continual learning. **[Intermediate]**
369. What is the stability-plasticity dilemma? How do different continual learning methods balance it? **[Intermediate]**
370. Explain Synaptic Intelligence (SI) and how it differs from EWC. **[Advanced]**
371. What are the three continual learning scenarios: task-incremental, domain-incremental, and class-incremental? How do they differ in difficulty? **[Intermediate]**
372. How does PackNet use pruning for continual learning? **[Advanced]**
373. Explain the role of knowledge distillation in continual learning (LwF - Learning without Forgetting). **[Intermediate]**
374. What is the relationship between continual learning and meta-learning? Can meta-learning help with catastrophic forgetting? **[Advanced]**
375. Describe the avalanche benchmark for continual learning evaluation. **[Intermediate]**
376. How does gradient episodic memory (GEM) constrain gradient updates to prevent forgetting? **[Advanced]**
377. What is forward and backward transfer in continual learning? How are they measured? **[Intermediate]**
378. Explain how sparse representations can help mitigate catastrophic forgetting. **[Advanced]**

### G.5 Federated Learning

379. What is federated learning? How does FedAvg (Federated Averaging) work? **[Basic]**
380. What are the key challenges of non-IID data in federated learning? How do methods like FedProx address them? **[Intermediate]**
381. Explain the privacy guarantees of federated learning. Is it inherently private? **[Intermediate]**
382. How does differential privacy integrate with federated learning? What is the privacy-utility tradeoff? **[Advanced]**
383. Describe secure aggregation. Why is it necessary even when data stays on-device? **[Advanced]**
384. What are model poisoning and data poisoning attacks in federated learning? How do you defend against them? **[Advanced]**
385. How do you handle communication efficiency in federated learning? Describe gradient compression and sparsification. **[Intermediate]**
386. What is FedBN? How does it handle batch normalization heterogeneity across clients? **[Advanced]**
387. Explain the straggler problem in federated learning and asynchronous aggregation strategies. **[Intermediate]**
388. How does personalized federated learning work? Describe approaches like local fine-tuning, multi-task FL, and per-FedAvg. **[Advanced]**
389. What is federated distillation? How does it reduce communication cost? **[Advanced]**
390. Explain the difference between horizontal and vertical federated learning. **[Intermediate]**
391. How do you evaluate a federated learning system? What metrics beyond accuracy are important? **[Intermediate]**
392. Describe the challenges of deploying federated learning on mobile/edge devices. **[Intermediate]**
393. How does FedMA (Federated Matched Averaging) handle model heterogeneity where clients have different architectures? **[Expert]**
394. What is the role of Secure Multi-Party Computation (SMPC) in federated learning? **[Advanced]**
395. How does SCAFFOLD correct for client drift in federated optimization? **[Expert]**

### G.6 Causal Inference in ML

396. What is the fundamental difference between correlation and causation? Give an ML example where ignoring this distinction leads to failure. **[Basic]**
397. Define a Structural Causal Model (SCM). What are its components? **[Intermediate]**
398. Explain the do-operator. What is the difference between P(Y|X=x) and P(Y|do(X=x))? **[Intermediate]**
399. What is the backdoor criterion? How do you use it to identify causal effects from observational data? **[Intermediate]**
400. What is the frontdoor criterion? Give an example where backdoor adjustment fails but frontdoor works. **[Advanced]**
401. Explain Pearl's three-step procedure for computing counterfactuals: abduction, action, prediction. **[Advanced]**
402. What is an instrumental variable? How is it used to estimate causal effects? **[Intermediate]**
403. Explain the difference between Average Treatment Effect (ATE) and Conditional Average Treatment Effect (CATE). **[Intermediate]**
404. How can causal reasoning improve ML fairness? Explain counterfactual fairness. **[Advanced]**
405. What is the do-calculus? State its three rules and explain when each is applicable. **[Expert]**
406. How does causal discovery differ from causal inference? Describe the PC algorithm. **[Advanced]**
407. Explain how randomized controlled trials (RCTs) relate to the do-operator. **[Intermediate]**
408. What is Simpson's paradox? Give an example and explain it using causal graphs. **[Intermediate]**
409. How are Granger causality tests different from true causal inference? **[Intermediate]**
410. Describe the use of propensity score matching for causal effect estimation. **[Intermediate]**
411. Explain Double Machine Learning (DML) for causal inference. **[Advanced]**
412. How does causal inference relate to out-of-distribution generalization? **[Advanced]**
413. What is the Independent Causal Mechanisms (ICM) principle? **[Expert]**
414. Describe CausalForest for heterogeneous treatment effect estimation. **[Advanced]**

### G.7 Optimal Transport in ML

415. Define the Wasserstein distance (Earth Mover's Distance). How does it differ from KL divergence? **[Intermediate]**
416. Why is the Wasserstein distance sometimes preferred over KL divergence for training generative models? **[Intermediate]**
417. Explain the Kantorovich formulation of optimal transport. **[Advanced]**
418. What is the Sinkhorn algorithm? How does it provide an efficient approximation to optimal transport? **[Advanced]**
419. How is optimal transport used in the Wasserstein GAN (WGAN)? What problem does it solve compared to vanilla GAN? **[Intermediate]**
420. Explain sliced Wasserstein distance. Why is it computationally cheaper? **[Advanced]**
421. How is optimal transport used for domain adaptation? Describe the OTDA framework. **[Advanced]**
422. What is the Wasserstein barycenter? How is it used in multi-source domain adaptation? **[Expert]**
423. Explain the connection between optimal transport and attention mechanisms. **[Expert]**
424. How is optimal transport used in NLP for document similarity (Word Mover's Distance)? **[Intermediate]**
425. Describe the use of Sinkhorn divergence as a training loss. What are its advantages over exact Wasserstein distance? **[Advanced]**
426. How does entropic regularization in optimal transport relate to maximum entropy principles? **[Expert]**

### G.8 Neural ODEs & Continuous-Depth Models

427. What is a Neural ODE? How does it parameterize continuous-time dynamics? **[Intermediate]**
428. Explain the adjoint sensitivity method for computing gradients in Neural ODEs. How does it compare to backpropagation through discretized steps? **[Advanced]**
429. What are the memory advantages of Neural ODEs over discrete residual networks? **[Intermediate]**
430. How do Neural ODEs relate to residual networks in the limit of infinite depth? **[Intermediate]**
431. Describe continuous normalizing flows. How do they extend the change-of-variables formula? **[Advanced]**
432. What are the computational bottlenecks of Neural ODEs? How does the adaptive step-size solver affect training? **[Advanced]**
433. Explain the augmented Neural ODE. Why is augmenting the state space necessary for certain problems? **[Advanced]**
434. How are Neural ODEs used in time series modeling (irregular sampling, continuous-time dynamics)? **[Intermediate]**
435. What is the relationship between Neural ODEs and stochastic differential equations (Neural SDEs)? **[Expert]**
436. Describe flow matching as an alternative to Neural ODEs for generative modeling. How does it relate to diffusion models? **[Advanced]**

### G.9 Equivariant Neural Networks & Geometric Deep Learning

437. What does it mean for a neural network to be equivariant to a transformation group? **[Basic]**
438. Explain the difference between invariance and equivariance. Give examples of each in ML. **[Basic]**
439. How are convolutional neural networks equivariant to translation? **[Intermediate]**
440. What is a group-equivariant convolution? How does it extend standard convolution? **[Advanced]**
441. Explain E(n)-equivariant networks. Why are they important for molecular and physics applications? **[Advanced]**
442. What is the Geometric Deep Learning blueprint (Bronstein et al.)? How does it unify CNNs, GNNs, and Transformers? **[Advanced]**
443. Describe spherical CNNs and their applications. **[Advanced]**
444. How do steerable CNNs achieve equivariance to rotation? **[Expert]**
445. Explain SE(3)-Transformers and their use in 3D molecular modeling. **[Expert]**
446. What is gauge equivariance and why is it important for learning on manifolds? **[Expert]**
447. How does data augmentation relate to equivariance? When is explicit equivariance better than augmentation? **[Intermediate]**
448. Describe Tensor Field Networks and their use of spherical harmonics. **[Expert]**

### G.10 Neural Architecture Search (NAS)

449. What is Neural Architecture Search? What are the three main components: search space, search strategy, and performance estimation? **[Basic]**
450. Describe the RL-based approach to NAS (Zoph & Le). What are its computational costs? **[Intermediate]**
451. What is DARTS (Differentiable Architecture Search)? How does it make the search space continuous? **[Intermediate]**
452. Compare one-shot NAS, weight-sharing NAS, and supernet-based NAS approaches. **[Advanced]**
453. What is the search space bias problem in NAS? How do you design good search spaces? **[Advanced]**
454. How does evolutionary NAS work? Compare it with RL-based and gradient-based methods. **[Intermediate]**
455. What is the performance estimation problem in NAS? Describe early stopping, weight sharing, and performance predictors. **[Advanced]**
456. How does hardware-aware NAS (e.g., MnasNet, EfficientNet) optimize for latency and FLOPS? **[Advanced]**
457. What is the NAS-Bench benchmark? Why is it important for fair comparison of NAS methods? **[Intermediate]**
458. Explain the "lottery ticket" hypothesis. How does it relate to NAS and pruning? **[Intermediate]**
459. How does ProxylessNAS directly search on the target hardware? **[Advanced]**
460. What are the limitations and criticisms of NAS methods in practice? **[Intermediate]**

### G.11 Knowledge Distillation

461. What is knowledge distillation? Explain the teacher-student framework. **[Basic]**
462. What are "soft targets" in knowledge distillation? Why do they contain more information than hard labels? **[Basic]**
463. Explain the temperature parameter in distillation loss. What is the effect of high vs. low temperature? **[Intermediate]**
464. Describe the KL divergence loss used in knowledge distillation. How is it combined with the task loss? **[Intermediate]**
465. What is self-distillation? How does a model distill knowledge from itself? **[Intermediate]**
466. Explain feature-based distillation (FitNets). How does it transfer intermediate representations? **[Advanced]**
467. How is knowledge distillation used in model compression for deployment? Give a practical pipeline. **[Intermediate]**
468. Describe relational knowledge distillation. How does it capture relationships between samples? **[Advanced]**
469. How is distillation used in BERT compression (DistilBERT, TinyBERT)? What aspects of knowledge are transferred? **[Intermediate]**
470. What are the failure modes of knowledge distillation? When does the student fail to learn from the teacher? **[Advanced]**
471. Explain data-free knowledge distillation. How does it work without access to the original training data? **[Advanced]**
472. How does online distillation (mutual learning) work? How does it differ from offline distillation? **[Advanced]**
473. Describe the use of knowledge distillation in ensemble compression. **[Intermediate]**

### G.12 Model Compression: Pruning, Quantization, Distillation

474. What is weight pruning? Explain unstructured vs. structured pruning. **[Basic]**
475. Describe magnitude-based pruning. What is its main assumption and when does it fail? **[Intermediate]**
476. What is the lottery ticket hypothesis? How does iterative magnitude pruning find "winning tickets"? **[Intermediate]**
477. Explain movement pruning. How does it differ from magnitude pruning for fine-tuned models? **[Advanced]**
478. What is quantization? Compare post-training quantization (PTQ) and quantization-aware training (QAT). **[Intermediate]**
479. Explain INT8 quantization for neural networks. How do you handle the range difference between weights and activations? **[Intermediate]**
480. What is mixed-precision training? How does it use FP16 for computation while maintaining FP32 master weights? **[Intermediate]**
481. Describe GPTQ and AWQ methods for quantizing large language models. **[Advanced]**
482. What is 4-bit quantization (QLoRA)? How does it enable fine-tuning of large models on consumer GPUs? **[Advanced]**
483. Explain structured pruning of attention heads in transformers. How do you identify unimportant heads? **[Advanced]**
484. What is channel pruning in CNNs? How does it differ from weight pruning in terms of actual speedup? **[Intermediate]**
485. Describe the three-stage pipeline: train → prune → fine-tune. When might iterative pruning outperform one-shot pruning? **[Intermediate]**
486. How does network architecture search relate to model compression? **[Advanced]**
487. What is SparseGPT? How does it prune LLMs in one shot without retraining? **[Expert]**
488. Explain the accuracy-efficiency tradeoff in model compression. How do you decide when compression goes too far? **[Intermediate]**
489. What are binary neural networks? What are their practical limitations? **[Advanced]**
490. How does pruning interact with quantization? Can you combine both for maximum compression? **[Advanced]**
491. Explain the ONNX runtime optimizations for deploying compressed models. **[Intermediate]**
492. What is activation sparsity? How do models like Mixture of Experts exploit it? **[Advanced]**

---

## H. Domain-Specific Applications

### H.1 ML for Healthcare

493. How is deep learning used for medical image analysis (X-ray, CT, MRI)? What architectures are commonly used? **[Basic]**
494. What is the FDA approval process for ML-based medical devices? What does SaMD (Software as a Medical Device) mean? **[Intermediate]**
495. Explain the challenge of class imbalance in disease diagnosis. How do you handle it when positive cases are < 1%? **[Intermediate]**
496. How are Electronic Health Records (EHR) represented as input to ML models? Describe temporal encoding approaches. **[Intermediate]**
497. What is the role of attention mechanisms in clinical NLP (extracting information from medical notes)? **[Intermediate]**
498. How is federated learning applied in healthcare to enable multi-hospital collaboration without sharing patient data? **[Advanced]**
499. Explain the MIMIC dataset. What ethical considerations apply when training models on clinical data? **[Intermediate]**
500. How do graph neural networks model drug-drug interactions and drug-target interactions? **[Advanced]**
501. What is survival analysis in ML? Explain the Cox proportional hazards model and its deep learning extensions (DeepSurv). **[Intermediate]**
502. How is ML used in genomics? Explain variant calling and its ML approaches. **[Advanced]**
503. What is the challenge of distribution shift in medical imaging (different scanners, hospitals, patient populations)? **[Intermediate]**
504. Describe the use of generative models (GANs, diffusion models) for synthetic medical data generation. **[Advanced]**
505. How do you ensure model interpretability for clinical decision support? Compare SHAP, attention visualization, and concept-based explanations. **[Intermediate]**
506. Explain the role of ML in drug discovery: virtual screening, molecular property prediction, and de novo drug design. **[Advanced]**
507. How is reinforcement learning used for adaptive clinical trial design? **[Expert]**
508. What are the challenges of label noise in medical datasets? How do you handle disagreement among annotators (radiologists)? **[Intermediate]**
509. Describe the Med-PaLM and similar medical LLMs. How are they evaluated for clinical accuracy? **[Advanced]**
510. How is segmentation used in medical imaging (tumor segmentation, organ delineation)? Describe the U-Net architecture and its variants. **[Intermediate]**
511. What is few-shot learning in the context of rare disease diagnosis? **[Advanced]**
512. How does multi-modal learning combine imaging, lab values, clinical notes, and genomics for patient outcome prediction? **[Advanced]**

### H.2 ML for Finance

513. How is ML used for algorithmic trading? Describe common features and model architectures. **[Basic]**
514. What is the lookahead bias problem in financial ML? How do you prevent data leakage in time-series financial models? **[Intermediate]**
515. Explain the challenges of non-stationarity in financial time series for ML models. **[Intermediate]**
516. How do you build a credit scoring model? What features are commonly used and what fairness constraints apply? **[Intermediate]**
517. Describe ML approaches to fraud detection. How do you handle extreme class imbalance (fraud < 0.1%)? **[Intermediate]**
518. What is the difference between parametric and non-parametric approaches to risk modeling (VaR, CVaR)? **[Intermediate]**
519. How are autoencoders used for anomaly detection in financial transactions? **[Intermediate]**
520. Explain the use of reinforcement learning for portfolio optimization. What are the main challenges? **[Advanced]**
521. What is the difference between alpha signals and risk factors in quantitative finance? How does ML help discover alpha? **[Advanced]**
522. How do you backtest an ML-based trading strategy? What are the pitfalls (overfitting, survivorship bias, transaction costs)? **[Intermediate]**
523. Explain the use of NLP in finance (sentiment analysis of news, earnings call analysis, SEC filing parsing). **[Intermediate]**
524. What is the challenge of regime change detection in financial markets? How does ML approach it? **[Advanced]**
525. How are graph neural networks used for modeling financial networks (inter-bank lending, supply chains)? **[Advanced]**
526. Explain the use of GANs for synthetic financial data generation. Why is it useful? **[Advanced]**
527. What regulatory requirements (Basel III, GDPR, Fair Lending Act) constrain ML deployment in finance? **[Intermediate]**
528. How is ML used for high-frequency trading? What latency constraints exist? **[Advanced]**
529. Describe the use of Bayesian methods for uncertainty quantification in financial risk models. **[Advanced]**
530. What is adversarial robustness in the context of financial ML? How might adversaries exploit model weaknesses? **[Advanced]**
531. How do you build an ML model that explains its credit decisions to regulators and consumers? **[Intermediate]**
532. Explain the concept of market microstructure. How does ML model order book dynamics? **[Expert]**

### H.3 ML for Autonomous Vehicles

533. Describe the perception pipeline in an autonomous vehicle. What sensors are used and how are they fused? **[Basic]**
534. What is sensor fusion? Compare early fusion, late fusion, and mid-level fusion approaches. **[Intermediate]**
535. How is 3D object detection performed on LiDAR point clouds? Describe PointPillars and VoxelNet. **[Intermediate]**
536. What is SLAM (Simultaneous Localization and Mapping)? Describe both classical and deep learning approaches. **[Intermediate]**
537. Explain the BEV (Bird's Eye View) representation. Why has it become dominant in autonomous driving perception? **[Intermediate]**
538. How does multi-camera 3D detection work without LiDAR (e.g., Tesla's approach, BEVFormer)? **[Advanced]**
539. What is motion planning in autonomous driving? Compare rule-based, search-based, and learning-based planners. **[Intermediate]**
540. How is imitation learning used for autonomous driving (behavior cloning, DAgger)? What are the distributional shift challenges? **[Advanced]**
541. Explain the concept of safety-critical ML. How do you certify that an ML model meets safety standards (ISO 26262)? **[Advanced]**
542. What is the long-tail problem in autonomous driving? How do you handle rare but safety-critical scenarios? **[Advanced]**
543. Describe the use of simulation for autonomous driving (CARLA, nuPlan). How do you bridge the sim-to-real gap? **[Intermediate]**
544. How does HD map creation work? What role does ML play? **[Intermediate]**
545. What is occupancy prediction/grid prediction in autonomous driving? How does it complement object detection? **[Advanced]**
546. Explain end-to-end autonomous driving (raw sensor input to driving commands). What are its advantages and risks? **[Advanced]**
547. How do transformer architectures improve perception in autonomous driving? **[Advanced]**
548. What is the role of uncertainty estimation in autonomous driving decisions? **[Intermediate]**
549. Describe the prediction task: forecasting the future trajectories of other road agents. What methods are used? **[Intermediate]**
550. How does reinforcement learning apply to autonomous driving? What are the safety challenges? **[Advanced]**
551. What are the ethical considerations in autonomous driving ML (trolley problem, bias in pedestrian detection)? **[Intermediate]**
552. Explain how lane detection works using segmentation and parametric curve fitting. **[Intermediate]**

### H.4 ML for Recommender Systems

553. What is collaborative filtering? Explain user-based and item-based approaches. **[Basic]**
554. Describe matrix factorization for recommender systems. How does it relate to SVD? **[Intermediate]**
555. What is the cold-start problem? How do you handle new users and new items? **[Basic]**
556. Explain content-based filtering. What features are typically used for items? **[Basic]**
557. How do hybrid recommender systems combine collaborative and content-based approaches? **[Intermediate]**
558. Describe the implicit vs. explicit feedback distinction. How does it change the loss function? **[Intermediate]**
559. What is the BPR (Bayesian Personalized Ranking) loss? Why is it suitable for implicit feedback? **[Intermediate]**
560. Explain neural collaborative filtering (NCF). How does it extend matrix factorization? **[Intermediate]**
561. How are GNNs used in recommender systems (PinSage, LightGCN)? **[Advanced]**
562. What is the "filter bubble" problem? How do you balance relevance, diversity, and serendipity? **[Intermediate]**
563. Describe two-tower models for recommendation. How are they used for retrieval and ranking? **[Intermediate]**
564. How do you evaluate a recommender system? Compare offline metrics (NDCG, MAP, Recall@K) vs. online A/B testing. **[Intermediate]**
565. Explain the exploration-exploitation tradeoff in recommender systems. How do multi-armed bandits help? **[Intermediate]**
566. What is session-based recommendation? How do RNNs and transformers model sequential user behavior? **[Advanced]**
567. Describe the YouTube recommendation system architecture (candidate generation → ranking). **[Intermediate]**
568. How do you handle position bias in recommendation rankings? **[Advanced]**
569. What is the role of knowledge graphs in recommender systems? **[Advanced]**
570. Explain multi-task learning in recommendation (e.g., predicting click, purchase, and dwell time simultaneously). **[Advanced]**
571. How does reinforcement learning improve long-term user engagement in recommender systems? **[Advanced]**
572. What are the challenges of deploying recommendation models at scale (latency, freshness, A/B testing)? **[Intermediate]**

### H.5 ML for Speech

573. Describe the traditional ASR pipeline: feature extraction → acoustic model → language model → decoder. **[Basic]**
574. What are Mel-Frequency Cepstral Coefficients (MFCCs)? Why have they been the standard acoustic feature? **[Basic]**
575. Explain CTC (Connectionist Temporal Classification). How does it handle alignment in end-to-end ASR? **[Intermediate]**
576. Describe the RNN-Transducer (RNN-T) model for ASR. How does it combine acoustic and language modeling? **[Advanced]**
577. How does Whisper (OpenAI) achieve robust speech recognition across languages and domains? **[Intermediate]**
578. What is the attention-based encoder-decoder approach to ASR (Listen, Attend, and Spell)? **[Intermediate]**
579. How do you handle noisy and far-field audio in ASR systems? **[Intermediate]**
580. Explain text-to-speech (TTS) using Tacotron and WaveNet. How does the two-stage approach work? **[Intermediate]**
581. What is FastSpeech? How does it achieve non-autoregressive TTS? **[Advanced]**
582. Describe neural vocoder architectures (WaveNet, WaveRNN, HiFi-GAN). How do they synthesize raw waveforms? **[Advanced]**
583. What is speaker verification vs. speaker identification? How are embeddings (x-vectors, d-vectors) used? **[Intermediate]**
584. How does speaker diarization work? What ML approaches are used? **[Intermediate]**
585. Explain zero-shot TTS (voice cloning with minimal speaker samples). What are the ethical concerns? **[Advanced]**
586. How is self-supervised learning used in speech (wav2vec 2.0, HuBERT)? What pretext tasks are used? **[Advanced]**
587. Describe the use of language models for ASR rescoring and error correction. **[Intermediate]**
588. What is keyword spotting? How do you build an always-on wake-word detector with minimal power consumption? **[Intermediate]**
589. How do you handle code-switching (multilingual speech) in ASR? **[Advanced]**
590. What is speech emotion recognition? What features and architectures are used? **[Intermediate]**
591. Describe the use of diffusion models for speech synthesis (DiffWave, Grad-TTS). **[Expert]**

### H.6 ML for Tabular Data

592. Why do gradient-boosted tree ensembles (XGBoost, LightGBM, CatBoost) often outperform deep learning on tabular data? **[Basic]**
593. Under what conditions might deep learning outperform tree-based methods on tabular data? **[Intermediate]**
594. Describe TabNet. How does it use attention for feature selection on tabular data? **[Intermediate]**
595. What is FT-Transformer? How does it adapt the transformer architecture for tabular data? **[Advanced]**
596. How does CatBoost handle categorical features differently from XGBoost? **[Intermediate]**
597. Compare target encoding, one-hot encoding, and learned embeddings for categorical features. **[Intermediate]**
598. What are the challenges of missing data in tabular datasets? Compare imputation strategies. **[Intermediate]**
599. How does SAINT (Self-Attention and Intersample Attention Transformer) work for tabular data? **[Advanced]**
600. Explain the importance of feature engineering for tabular data. Does deep learning eliminate the need for it? **[Intermediate]**
601. How do you handle high-cardinality categorical features (e.g., ZIP codes, user IDs)? **[Intermediate]**
602. What is the role of regularization in preventing overfitting on tabular data? Compare L1, L2, and dropout. **[Basic]**
603. How does AutoML (Auto-sklearn, AutoGluon, H2O) approach tabular data modeling? **[Intermediate]**
604. Describe the NODE (Neural Oblivious Decision Ensembles) architecture. How does it bridge neural networks and decision trees? **[Advanced]**
605. What is the "unreasonable effectiveness of default hyperparameters" observation for XGBoost? **[Intermediate]**
606. How do you perform model selection between tree-based and DL-based models for a new tabular dataset? **[Intermediate]**
607. Explain SHAP (SHapley Additive exPlanations) for feature importance in tabular models. How does it differ from permutation importance? **[Intermediate]**
608. What is the Grinsztajn et al. (2022) benchmark comparing DL and tree methods on tabular data? What were the key findings? **[Advanced]**

### H.7 ML for Time Series

609. Compare classical time series methods (ARIMA, exponential smoothing) with deep learning approaches. When does each shine? **[Basic]**
610. Explain the Temporal Fusion Transformer (TFT). How does it handle static covariates, known future inputs, and observed past inputs? **[Advanced]**
611. What is N-BEATS? How does its interpretable architecture decompose time series into trend and seasonality? **[Advanced]**
612. Describe PatchTST. How does patching improve transformer performance on time series? **[Advanced]**
613. What is the challenge of non-stationarity in time series forecasting? How do methods like RevIN address it? **[Intermediate]**
614. How do you handle multiple time series with different frequencies and lengths? **[Intermediate]**
615. Explain the difference between global models (one model for all series) and local models (one model per series). When does each approach work better? **[Intermediate]**
616. How is DeepAR used for probabilistic time series forecasting? **[Intermediate]**
617. What is the "linear models beat transformers" finding in time series forecasting? What does DLinear show? **[Advanced]**
618. How do you perform anomaly detection in time series data? Compare statistical and DL approaches. **[Intermediate]**
619. Explain the challenge of evaluation in time series forecasting (rolling window, expanding window, temporal cross-validation). **[Intermediate]**
620. How are foundation models (TimesFM, Lag-Llama, Chronos) approaching time series as a pre-training task? **[Advanced]**
621. What is the difference between point forecasting and probabilistic (distributional) forecasting? Why does the latter matter? **[Intermediate]**
622. How do you handle missing values and irregular sampling in time series? **[Intermediate]**
623. Explain how wavelet decomposition can be integrated with neural networks for time series. **[Advanced]**
624. What is the Informer architecture? How does its ProbSparse attention improve long-sequence forecasting? **[Advanced]**
625. How is conformal prediction used for calibrated prediction intervals in time series? **[Advanced]**
626. Describe the use of state-space models (S4, Mamba) for long-range time series modeling. **[Expert]**

### H.8 AI for Science

627. How does AlphaFold2 predict protein structure? Describe the Evoformer and structure module. **[Intermediate]**
628. What is the multiple sequence alignment (MSA) representation in AlphaFold? Why is it important? **[Intermediate]**
629. How has RoseTTAFold improved upon AlphaFold for protein structure prediction? **[Advanced]**
630. Describe the use of ML for weather forecasting (GraphCast, Pangu-Weather, FourCastNet). How do they compare to numerical weather prediction? **[Advanced]**
631. How is ML used in materials science? Describe crystal structure prediction and property prediction. **[Advanced]**
632. Explain the use of equivariant neural networks in molecular dynamics simulations. **[Advanced]**
633. How are generative models used for molecule generation (SMILES-based, graph-based, 3D generation)? **[Intermediate]**
634. What is the role of ML in particle physics (jet classification, event reconstruction at the LHC)? **[Advanced]**
635. Describe the application of ML to climate science (downscaling, parameterization of subgrid processes). **[Advanced]**
636. How is reinforcement learning used for experimental design and active learning in scientific discovery? **[Advanced]**
637. What is the scientific ML approach to solving PDEs (Physics-Informed Neural Networks, PINN)? **[Intermediate]**
638. Describe the DeePMD framework for molecular dynamics. How does it achieve ab initio accuracy at classical MD speeds? **[Expert]**
639. How are foundation models being developed for scientific domains (protein language models, chemical language models)? **[Advanced]**
640. What is the role of ML in astronomy (galaxy classification, exoplanet detection, gravitational wave analysis)? **[Intermediate]**
641. How does the neural operator approach (Fourier Neural Operator) solve families of PDEs? **[Advanced]**
642. Describe the application of diffusion models to protein design and molecular conformation generation. **[Expert]**
643. What challenges are unique to ML for science (physical constraints, conservation laws, extrapolation requirements)? **[Intermediate]**
644. How is ML used in genomics for gene expression prediction from DNA sequence (Enformer)? **[Advanced]**

### H.9 ML for Code

645. How does code completion work in models like Codex and GitHub Copilot? What training data and objectives are used? **[Basic]**
646. Explain the transformer architecture choices for code generation models (decoder-only vs. encoder-decoder). **[Intermediate]**
647. What is the HumanEval benchmark? How is pass@k evaluated? **[Intermediate]**
648. How do code LLMs handle long contexts (entire repositories)? What are the challenges? **[Intermediate]**
649. Describe fill-in-the-middle (FIM) training for code models. Why is it important for code completion? **[Intermediate]**
650. How is code understanding different from code generation? What tasks does code understanding include (summarization, bug detection, type inference)? **[Intermediate]**
651. What is the role of AST (Abstract Syntax Tree) representations in ML for code? **[Intermediate]**
652. How do you evaluate code generation models beyond correctness (code quality, security, efficiency)? **[Advanced]**
653. Describe retrieval-augmented code generation. How does it help with repository-level understanding? **[Advanced]**
654. What is program synthesis? How does it differ from code generation? **[Advanced]**
655. How are LLMs used for automated bug fixing and code review? **[Intermediate]**
656. Explain the use of execution feedback for improving code generation (AlphaCode, CodeRL). **[Advanced]**
657. How do you handle security vulnerabilities introduced by code generation models? **[Intermediate]**
658. What is the contamination problem in evaluating code LLMs (training data overlapping with benchmarks)? **[Intermediate]**
659. Describe the SWE-bench benchmark. How is it different from HumanEval? **[Advanced]**
660. How do multi-turn code generation agents work (e.g., for complex software engineering tasks)? **[Advanced]**
661. What is the role of static analysis tools in verifying LLM-generated code? **[Intermediate]**
662. How are code embeddings used for code search and clone detection? **[Intermediate]**
663. Describe the use of tree-sitter and other parsers for structural code understanding in ML. **[Advanced]**

### H.10 Additional Cross-Domain Questions

664. How do you decide whether to use ML or a rule-based system for a given domain problem? **[Basic]**
665. What is the role of domain expertise in feature engineering across different application areas? **[Basic]**
666. How do data availability and labeling costs differ across domains (healthcare vs. finance vs. autonomous driving)? What impact does this have on model choice? **[Intermediate]**
667. Explain the concept of a "human-in-the-loop" system. In which domains is it most critical? **[Intermediate]**
668. How do regulatory requirements differ across domains and how do they impact ML system design? **[Intermediate]**
669. What is the role of simulation in ML for different domains? Compare driving simulation, clinical trial simulation, and financial market simulation. **[Intermediate]**
670. How does the interpretability requirement differ across healthcare, finance, and autonomous driving? **[Intermediate]**
671. What are the ethical considerations unique to ML in healthcare vs. ML in advertising? **[Intermediate]**
672. How does the cost of errors differ across domains? A wrong movie recommendation vs. a wrong medical diagnosis vs. a wrong trading decision. **[Basic]**
673. Explain how transfer learning is applied differently across domains (vision → medical imaging, NLP → legal documents, etc.). **[Intermediate]**
674. How do you handle domain-specific evaluation metrics (clinical sensitivity, Sharpe ratio, mAP for detection)? **[Intermediate]**
675. What is the role of synthetic data generation in domains where real data is scarce or sensitive? **[Intermediate]**
676. How do privacy-preserving techniques (federated learning, differential privacy, synthetic data) apply differently in healthcare vs. finance? **[Advanced]**
677. Describe the concept of "AI readiness" for an organization. What infrastructure and data maturity is needed? **[Basic]**
678. How do you monitor model performance in production across different domains? What domain-specific drift signals exist? **[Intermediate]**
679. Explain the concept of "model risk management" in regulated industries. **[Intermediate]**
680. How does the ML development lifecycle differ between a research lab and a production deployment in a regulated industry? **[Intermediate]**
681. What is the role of active learning in reducing annotation costs in domain-specific applications? **[Intermediate]**
682. How do foundation models (LLMs, vision foundation models) change the approach to domain-specific ML? **[Advanced]**
683. Explain the concept of a "digital twin." In which domains is it most impactful? **[Intermediate]**
684. How do you handle multi-modal data integration across domains (text + images in healthcare, sensor fusion in driving)? **[Advanced]**
685. What is the role of causal inference in domain-specific ML (treatment effects in healthcare, policy evaluation in finance)? **[Advanced]**
686. How do you build trust in ML systems for high-stakes domains? Describe calibration, uncertainty quantification, and human oversight. **[Intermediate]**
687. What lessons from ML deployment in one domain can transfer to another? Give specific examples. **[Intermediate]**
688. How does continual learning apply to domain-specific models that face evolving data distributions (new diseases, market regime changes, new road infrastructure)? **[Advanced]**
689. What is the role of benchmark datasets in advancing domain-specific ML? Name key benchmarks for 5 different domains. **[Intermediate]**
690. How do you handle the "last mile" deployment challenge in different domains (edge devices for driving, hospital IT systems for healthcare, low-latency for trading)? **[Advanced]**
691. Explain the concept of "AI alignment" in domain-specific contexts. How do you ensure models optimize for the right objective? **[Advanced]**
692. How do large multimodal models (GPT-4V, Gemini) change the landscape for domain-specific applications? **[Advanced]**
693. What is the "build vs. buy" decision for ML in different industries? When should you use a general-purpose API vs. training your own model? **[Intermediate]**
694. How do you handle catastrophic edge cases in safety-critical domains? Describe formal verification approaches for ML. **[Expert]**
695. What is the role of reinforcement learning from human feedback (RLHF) in domain-specific applications beyond chatbots? **[Advanced]**
696. How do you design ML systems that gracefully degrade when they encounter out-of-distribution inputs in production? **[Intermediate]**
697. Explain the concept of "responsible AI" and how it manifests differently across industries. **[Basic]**
698. How are retrieval-augmented generation (RAG) systems customized for domain-specific knowledge (medical, legal, financial)? **[Advanced]**
699. What is the future of AI agents in domain-specific applications? Describe agentic workflows for healthcare, coding, and scientific discovery. **[Advanced]**
700. How do you measure ROI of ML projects in different domains? What non-obvious costs should be considered? **[Intermediate]**
701. Describe the challenge of reproducibility in ML across different domains. What practices help? **[Intermediate]**
702. How does data governance differ across domains and how does it impact ML development? **[Intermediate]**
703. What is the role of explainability in debugging domain-specific ML models vs. explaining decisions to end users? **[Intermediate]**
704. How do small language models and edge AI change the deployment landscape for domain-specific applications? **[Advanced]**
705. Describe how the ML tech stack differs across domains (healthcare: DICOM + FHIR; finance: FIX protocol; autonomous driving: ROS + sensor APIs). **[Intermediate]**

---

## Quick Reference: Question Count by Section

| Section | Topic | Count |
|---------|-------|-------|
| E.1 | Birthday Problem & Variants | 15 |
| E.2 | Monty Hall & Bayesian Reasoning | 15 |
| E.3 | Expected Value Problems | 20 |
| E.4 | Conditional Probability Brain Teasers | 15 |
| E.5 | Geometric Probability | 13 |
| E.6 | Markov Chain Puzzles | 14 |
| E.7 | Random Walk Problems | 10 |
| E.8 | Coupon Collector Problem | 9 |
| E.9 | Secretary Problem / Optimal Stopping | 8 |
| E.10 | Estimation Problems (Fermi) | 13 |
| E.11 | Matrix Puzzles & Linear Algebra | 23 |
| **E Total** | **Math Brain Teasers & Probability** | **155** |
| F.1 | PAC Learning | 15 |
| F.2 | VC Dimension | 17 |
| F.3 | Rademacher Complexity | 10 |
| F.4 | Bias-Complexity Tradeoff | 10 |
| F.5 | Generalization Bounds | 13 |
| F.6 | No Free Lunch Theorem | 7 |
| F.7 | Universal Approximation Theorem | 8 |
| F.8 | Convergence Rates | 13 |
| F.9 | Information-Theoretic Limits | 11 |
| F.10 | Computational Complexity of ML | 13 |
| F.11 | Sample Complexity | 11 |
| F.12 | Kernel Theory & RKHS | 19 |
| **F Total** | **Learning Theory & Theoretical ML** | **147** |
| G.1 | Graph Neural Networks | 23 |
| G.2 | Self-Supervised Learning | 20 |
| G.3 | Meta-Learning | 18 |
| G.4 | Continual/Lifelong Learning | 15 |
| G.5 | Federated Learning | 17 |
| G.6 | Causal Inference in ML | 19 |
| G.7 | Optimal Transport in ML | 12 |
| G.8 | Neural ODEs & Continuous-Depth | 10 |
| G.9 | Equivariant Networks & Geometric DL | 12 |
| G.10 | Neural Architecture Search | 12 |
| G.11 | Knowledge Distillation | 13 |
| G.12 | Model Compression | 19 |
| **G Total** | **Advanced & Niche Topics** | **190** |
| H.1 | ML for Healthcare | 20 |
| H.2 | ML for Finance | 20 |
| H.3 | ML for Autonomous Vehicles | 20 |
| H.4 | ML for Recommender Systems | 20 |
| H.5 | ML for Speech | 19 |
| H.6 | ML for Tabular Data | 17 |
| H.7 | ML for Time Series | 18 |
| H.8 | AI for Science | 18 |
| H.9 | ML for Code | 19 |
| H.10 | Cross-Domain Questions | 42 |
| **H Total** | **Domain-Specific Applications** | **213** |
| **GRAND TOTAL** | | **705** |

---

> **Difficulty Distribution:**
> - **[Basic]**: ~15% — Foundational concepts every ML practitioner should know
> - **[Intermediate]**: ~40% — Standard interview depth for ML Engineer roles
> - **[Advanced]**: ~35% — Expected for Senior/Staff ML roles and ML Scientists
> - **[Expert]**: ~10% — PhD qualifier / Research Scientist level
