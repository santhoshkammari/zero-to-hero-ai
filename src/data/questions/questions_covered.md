# Zero to Hero AI — Interview Questions Bank

> **5,148 questions** covering Python, Mathematics, Data Science, Machine Learning,
> Deep Learning, Computer Vision, NLP, Transformers, LLMs, Generative AI, AI Agents,
> ML Systems, Bayesian ML, Reinforcement Learning, and Responsible AI.
>
> Difficulty levels: [Basic] → [Intermediate] → [Advanced] → [Expert]
>
> **Purpose**: A reader who masters all concepts in our Zero-to-Hero-AI book should be
> able to confidently answer every question in this bank.

## Summary

| Part | File | Questions |
|------|------|-----------|
| 1 | questions_part1_python_math_data.md | 522 |
| 2 | questions_part2_ml_core.md | 649 |
| 3 | questions_part3_dl_foundations.md | 610 |
| 4 | questions_part4_nlp_transformers.md | 609 |
| 5 | questions_part5_llm_genai.md | 614 |
| 6 | questions_part6_systems_ethics.md | 590 |
| 7 | questions_part7_extra_coding_design.md | 841 |
| 8 | questions_part8_theory_puzzles.md | 713 |
| | **TOTAL** | **5,148** |

---

# Part 1: Python, Mathematics & Data Fundamentals — 500+ Interview Questions

> A comprehensive collection of real-world interview questions for ML/AI roles, grounded in what top companies (FAANG, startups, research labs) actually ask. Questions progress from basic to expert within each subtopic.

---

## 1. Python Programming for ML/AI

### 1.1 Python Basics & Core Concepts

#### Data Types & Variables
1. [Basic] What are Python's mutable vs immutable data types? Give examples of each.
2. [Basic] What is the difference between a list and a tuple? When would you use one over the other?
3. [Basic] How does Python handle integer overflow compared to languages like C or Java?
4. [Basic] What is the difference between `==` and `is` in Python?
5. [Basic] Explain the difference between shallow copy and deep copy. When does each matter?
6. [Basic] What are Python's built-in numeric types? How does `float` differ from `Decimal`?
7. [Basic] How are strings stored in Python 3? What encoding does Python 3 use by default?
8. [Intermediate] What is string interning in Python? When does CPython intern strings automatically?
9. [Intermediate] Explain how Python dictionaries work internally. What changed in Python 3.7+ regarding dict ordering?
10. [Intermediate] What is the time complexity of common dict operations (get, set, delete)? How are hash collisions handled?
11. [Intermediate] What is a `frozenset` and when would you use it instead of a `set`?
12. [Intermediate] How does Python implement `defaultdict` vs a regular `dict`? Show a use case.
13. [Intermediate] Explain the `collections` module. When would you use `namedtuple`, `deque`, `Counter`, and `OrderedDict`?
14. [Advanced] What is the `__slots__` mechanism? How does it affect memory usage and attribute access?
15. [Advanced] How does CPython's small integer caching work? What range of integers are cached?
16. [Advanced] Explain Python's memory model for mutable default arguments. Why is `def f(x=[])` dangerous?

#### Control Flow & Comprehensions
17. [Basic] Explain the difference between `for` and `while` loops. When is each appropriate?
18. [Basic] What is a list comprehension? Convert a nested for-loop with a condition into a list comprehension.
19. [Basic] How do `break`, `continue`, and `else` clauses work in Python loops?
20. [Basic] What is the difference between `range()` and `xrange()` (Python 2 vs 3)?
21. [Intermediate] Explain dictionary and set comprehensions with examples.
22. [Intermediate] What is a generator expression? How does it differ from a list comprehension in terms of memory?
23. [Intermediate] How does the `enumerate()` function work, and why is it preferred over manual indexing?
24. [Intermediate] Explain `zip()` and `itertools.zip_longest()`. What happens when iterables have different lengths?
25. [Advanced] How would you implement a custom iterator class? What methods must it define?
26. [Advanced] Explain how `itertools.chain()`, `itertools.product()`, and `itertools.combinations()` work. Give ML-related use cases.

#### Functions & Scope
27. [Basic] What is the difference between positional and keyword arguments in Python?
28. [Basic] Explain `*args` and `**kwargs`. Write a function that uses both.
29. [Basic] What is a lambda function? When should and shouldn't you use one?
30. [Basic] Explain the LEGB rule for variable scoping in Python.
31. [Intermediate] What is a closure in Python? Give an example of when closures are useful in ML code.
32. [Intermediate] Explain the difference between `global` and `nonlocal` keywords.
33. [Intermediate] How does `functools.partial` work? Give an example of its use in ML pipelines.
34. [Intermediate] What does `functools.lru_cache` do? When would you use it in data processing?
35. [Advanced] Explain first-class functions in Python. How does treating functions as objects enable functional programming patterns?
36. [Advanced] What is the difference between `map()`, `filter()`, and `reduce()`? When are they preferable to comprehensions?
37. [Advanced] Explain how Python resolves function calls at runtime. What is the `__call__` method?

#### Decorators
38. [Intermediate] What is a decorator in Python? How does it work under the hood?
39. [Intermediate] Write a decorator that logs the execution time of a function.
40. [Intermediate] Write a decorator that counts how many times a function has been called.
41. [Intermediate] How do you preserve the original function's metadata when using decorators? (Hint: `functools.wraps`)
42. [Advanced] Write a parameterized decorator (a decorator that accepts arguments).
43. [Advanced] What is the difference between function decorators and class decorators? Give examples.
44. [Advanced] How do you stack multiple decorators? In what order are they applied?
45. [Expert] Implement a decorator that caches function results with an expiration time (TTL cache).
46. [Expert] How would you implement a retry decorator with exponential backoff for API calls?

#### Generators & Iterators
47. [Intermediate] What is a generator function? How does `yield` differ from `return`?
48. [Intermediate] Write an infinite Fibonacci sequence generator.
49. [Intermediate] What is the `send()` method on a generator? When would you use it?
50. [Intermediate] Explain the difference between `yield` and `yield from`. When is `yield from` useful?
51. [Advanced] What happens when you use `yield` inside a `try`/`finally` block?
52. [Advanced] How do generators help with memory efficiency when processing large datasets?
53. [Advanced] Write a generator that lazily reads and processes a large CSV file line by line.
54. [Expert] Explain how generator-based coroutines work (pre-`async`/`await` style). How are they different from native coroutines?

#### Context Managers
55. [Intermediate] What is a context manager? How does the `with` statement work?
56. [Intermediate] Write a custom context manager class using `__enter__` and `__exit__`.
57. [Intermediate] How does `contextlib.contextmanager` simplify writing context managers?
58. [Advanced] Write a context manager that temporarily changes the working directory and restores it.
59. [Advanced] How would you use a context manager to manage database connections in an ML pipeline?
60. [Advanced] Write a context manager that suppresses specific exceptions.

#### Object-Oriented Programming
61. [Basic] Explain the four pillars of OOP: encapsulation, abstraction, inheritance, and polymorphism in Python.
62. [Basic] What is `self` in Python? Why is it explicitly required in method definitions?
63. [Basic] What is the difference between class attributes and instance attributes?
64. [Basic] How do you create a class in Python? Write a simple class with `__init__`, `__str__`, and `__repr__`.
65. [Intermediate] What is the difference between `@staticmethod` and `@classmethod`? When do you use each?
66. [Intermediate] Explain Python's Method Resolution Order (MRO). How does it handle the diamond problem in multiple inheritance?
67. [Intermediate] What are properties (`@property`) in Python? How do they differ from getters/setters?
68. [Intermediate] What are dunder (magic) methods? Name at least 8 commonly used ones and their purposes.
69. [Intermediate] How does operator overloading work in Python? Implement `__add__` and `__eq__` for a Vector class.
70. [Advanced] What are metaclasses in Python? How does `type` serve as the default metaclass?
71. [Advanced] Implement a metaclass that automatically registers all subclasses of a base class.
72. [Advanced] How do abstract base classes (ABC) work in Python? When would you use them in an ML framework?
73. [Advanced] What is the descriptor protocol (`__get__`, `__set__`, `__delete__`)? How do properties use it internally?
74. [Expert] Explain how `__slots__` interacts with inheritance and multiple inheritance.
75. [Expert] Implement a Singleton pattern using both a metaclass and a decorator approach.

#### Error Handling
76. [Basic] What is the difference between `try`/`except` and `try`/`except`/`else`/`finally`?
77. [Basic] How do you raise a custom exception in Python?
78. [Intermediate] What is the exception hierarchy in Python? How does `BaseException` differ from `Exception`?
79. [Intermediate] Explain exception chaining with `raise ... from ...`. When is it useful?
80. [Advanced] How would you implement custom exception classes for an ML library with proper hierarchy?

### 1.2 Python Libraries for ML

#### NumPy
81. [Basic] What is NumPy? Why is it faster than pure Python lists for numerical computation?
82. [Basic] How do you create a NumPy array? What is the difference between `np.array()`, `np.zeros()`, `np.ones()`, and `np.arange()`?
83. [Basic] What is the `shape` and `dtype` of a NumPy array? How do you change them?
84. [Basic] Explain array indexing and slicing in NumPy. How does it differ from Python lists?
85. [Intermediate] What is broadcasting in NumPy? Explain the rules with examples.
86. [Intermediate] What is vectorization? Why is `np.dot(a, b)` faster than a Python loop computing the dot product?
87. [Intermediate] Explain the difference between `.copy()` and `.view()` in NumPy. What are the implications?
88. [Intermediate] How do you perform element-wise operations vs matrix operations in NumPy?
89. [Intermediate] What is `np.where()`? Give an example of using it for conditional operations.
90. [Intermediate] How do you compute column-wise and row-wise means, sums, and standard deviations?
91. [Intermediate] What are `np.concatenate`, `np.stack`, `np.vstack`, and `np.hstack`? When do you use each?
92. [Advanced] Write NumPy code to normalize each row of a 2D array to unit length using broadcasting.
93. [Advanced] What is `np.einsum()`? Give examples of using it for matrix multiplication, trace, and tensor operations.
94. [Advanced] How does NumPy handle memory layout (C-order vs Fortran-order)? When does this matter for performance?
95. [Advanced] Explain structured arrays and record arrays in NumPy. When would you use them?
96. [Expert] How do you use `np.memmap` for out-of-core computation on arrays larger than RAM?
97. [Expert] How does NumPy's random number generation work? What changed with `np.random.Generator` vs the legacy `np.random` API?

#### Pandas
98. [Basic] What is the difference between a Pandas Series and a DataFrame?
99. [Basic] How do you read a CSV file into a DataFrame? What are the most useful parameters of `pd.read_csv()`?
100. [Basic] How do you select a column, multiple columns, and rows by condition in a DataFrame?
101. [Basic] Explain `loc` vs `iloc` in Pandas. Give examples of each.
102. [Intermediate] What is the `groupby` operation? Explain split-apply-combine with an example.
103. [Intermediate] What is the difference between `merge()`, `join()`, and `concat()` in Pandas?
104. [Intermediate] How do you handle missing values (`NaN`) in a DataFrame? List at least 5 methods.
105. [Intermediate] What is `pivot_table()` vs `pivot()` vs `melt()`? When do you use each?
106. [Intermediate] How do you apply a function to every row or column of a DataFrame? Compare `apply()`, `map()`, and `applymap()`/`map()`.
107. [Intermediate] What are MultiIndex DataFrames? How do you create, access, and manipulate them?
108. [Advanced] How do you optimize Pandas operations for large datasets? (chunking, dtypes, vectorized operations)
109. [Advanced] What is the `query()` method in Pandas? When is it more readable than boolean indexing?
110. [Advanced] Explain the `pipe()` method for method chaining. How does it improve code readability?
111. [Advanced] How do you handle time series data in Pandas? Explain `resample()`, `rolling()`, and `shift()`.
112. [Advanced] What are Categorical dtypes in Pandas? How do they save memory and speed up operations?
113. [Expert] Compare Pandas with Polars. When would you choose Polars over Pandas for ML workflows?
114. [Expert] How does copy-on-write (CoW) work in recent Pandas versions? How does it affect performance?

#### Matplotlib & Visualization
115. [Basic] How do you create a basic line plot, scatter plot, and histogram using Matplotlib?
116. [Basic] What is the difference between `plt.plot()` (pyplot) and the object-oriented API (fig, ax)?
117. [Intermediate] How do you create subplots and customize figure size, titles, labels, and legends?
118. [Intermediate] How do you visualize a confusion matrix using Matplotlib and Seaborn?
119. [Intermediate] What is Seaborn and how does it differ from Matplotlib? When would you use each?
120. [Advanced] How do you create interactive plots for ML model analysis? Compare Plotly, Bokeh, and Matplotlib.

#### Scikit-learn
121. [Basic] What is the scikit-learn estimator API? Explain `fit()`, `predict()`, and `transform()`.
122. [Basic] How do you split data into training and test sets using `train_test_split()`?
123. [Basic] What is a `Pipeline` in scikit-learn? Why is it important?
124. [Intermediate] How does `ColumnTransformer` work? Give an example with mixed numeric and categorical features.
125. [Intermediate] Explain `StandardScaler` vs `MinMaxScaler` vs `RobustScaler`. When would you use each?
126. [Intermediate] How do you perform hyperparameter tuning with `GridSearchCV` vs `RandomizedSearchCV`?
127. [Intermediate] What is `cross_val_score()`? How is it different from `cross_validate()`?
128. [Intermediate] How do you save and load a trained scikit-learn model? Compare `pickle`, `joblib`, and `skops`.
129. [Advanced] How do you write a custom transformer that integrates with scikit-learn's `Pipeline`?
130. [Advanced] How do you write a custom estimator in scikit-learn? What base classes and mixins must you use?
131. [Advanced] Explain how `FeatureUnion` works and when to use it vs `ColumnTransformer`.
132. [Expert] How does scikit-learn handle parallel processing internally? Explain the `n_jobs` parameter and its use of `joblib`.

### 1.3 Advanced Python Concepts

#### Memory Management & Internals
133. [Intermediate] How does Python manage memory? Explain the private heap and memory allocator.
134. [Intermediate] What is reference counting in Python? How do you check an object's reference count?
135. [Intermediate] What is garbage collection in Python? How does the generational GC work?
136. [Intermediate] What is a circular reference? Why can't reference counting alone handle it?
137. [Advanced] How can you force garbage collection? What functions does the `gc` module provide?
138. [Advanced] What are memory leaks in Python? How do you detect and debug them?
139. [Advanced] Explain Python's memory pool (pymalloc). How does it optimize allocation for small objects?
140. [Advanced] What is the `__del__` method? Why is its use discouraged?
141. [Expert] How does the `weakref` module work? When would you use weak references in an ML application?
142. [Expert] Explain the `tracemalloc` module. How would you use it to profile memory usage in a data pipeline?

#### GIL & Concurrency
143. [Intermediate] What is the Global Interpreter Lock (GIL)? Why does CPython have it?
144. [Intermediate] How does the GIL affect multi-threaded Python programs?
145. [Intermediate] When is `threading` still useful despite the GIL? (I/O-bound vs CPU-bound tasks)
146. [Advanced] Explain the `multiprocessing` module. How does it bypass the GIL?
147. [Advanced] What is the difference between `multiprocessing.Pool` and `concurrent.futures.ProcessPoolExecutor`?
148. [Advanced] How do you share state between processes? Explain `Value`, `Array`, `Manager`, and `Queue`.
149. [Advanced] What is `concurrent.futures`? Compare `ThreadPoolExecutor` and `ProcessPoolExecutor`.
150. [Expert] What are the plans for removing the GIL in Python 3.13+ (PEP 703, free-threaded Python)? What implications does this have?
151. [Expert] How does `joblib` parallelize scikit-learn operations? What serialization challenges arise?

#### Async Programming
152. [Intermediate] What are coroutines in Python? How do `async def` and `await` work?
153. [Intermediate] What is the event loop in asyncio? How does it schedule and run coroutines?
154. [Intermediate] Write a simple async function that fetches data from multiple URLs concurrently.
155. [Advanced] What is `asyncio.gather()` vs `asyncio.wait()` vs `asyncio.TaskGroup()`?
156. [Advanced] Can async and threads be mixed? Explain `loop.run_in_executor()`.
157. [Advanced] How would you use async programming in an ML inference service (e.g., batching requests)?
158. [Expert] Explain the difference between concurrency and parallelism. How do async, threading, and multiprocessing relate?

#### Modern Python Features (3.10–3.13)
159. [Intermediate] What is structural pattern matching (`match`/`case`) introduced in Python 3.10? Give examples.
160. [Intermediate] What is the walrus operator (`:=`)? Give an example where it improves code clarity.
161. [Intermediate] Explain the new type parameter syntax in Python 3.12 (`def func[T](arg: T) -> T`).
162. [Intermediate] What are `TypeAlias`, `TypeGuard`, and `Self` in modern type hints?
163. [Advanced] What improvements to error messages were made in Python 3.11/3.12?
164. [Advanced] What is `ExceptionGroup` and `except*` (Python 3.11)? When would you use them?
165. [Advanced] What is the `tomllib` module (Python 3.11)? How is it useful for ML project configuration?
166. [Expert] What are the performance improvements in Python 3.11+ (the "Faster CPython" project)? How do they affect ML workloads?

### 1.4 Python Coding & Implementation

#### Algorithm Implementation
167. [Basic] Implement binary search on a sorted list. What is its time complexity?
168. [Basic] Implement bubble sort and explain its time complexity.
169. [Basic] Write a function to check if a string is a palindrome.
170. [Intermediate] Implement quicksort. What is its average and worst-case time complexity?
171. [Intermediate] Implement merge sort. Why is it preferred for linked lists?
172. [Intermediate] Write a function to find the top-K frequent elements in a list. (Use `collections.Counter` and `heapq`.)
173. [Intermediate] Implement a function to compute the running mean and standard deviation of a stream of numbers.
174. [Intermediate] Write a function that generates all permutations of a list.
175. [Advanced] Implement a simple hash map (dictionary) from scratch.
176. [Advanced] Implement a Trie data structure. When would it be useful in NLP preprocessing?
177. [Advanced] Implement a priority queue using a heap. When is it used in ML (e.g., beam search)?
178. [Expert] Implement K-means clustering from scratch using only NumPy.
179. [Expert] Implement gradient descent for linear regression from scratch using NumPy.
180. [Expert] Implement a simple decision tree classifier from scratch (ID3 or CART algorithm).

#### Data Manipulation & Processing
181. [Basic] Given a list of numbers, write a one-liner to get all even numbers greater than 10.
182. [Basic] Write a function to flatten a nested list of arbitrary depth.
183. [Intermediate] Given a dictionary of student scores, find the student with the highest average across subjects.
184. [Intermediate] Write a function to remove duplicate rows from a list of dictionaries based on a specific key.
185. [Intermediate] Implement a function to merge two sorted lists into one sorted list without using `sorted()`.
186. [Advanced] Write a function to parse a JSON log file and extract error messages, grouped by timestamp.
187. [Advanced] Implement a data pipeline function that chains multiple transformations (filter → map → reduce) on a dataset.
188. [Advanced] Write a function to detect and report data quality issues (missing values, type mismatches, outliers) in a CSV file.

#### Debugging & Testing
189. [Basic] How do you use `print()` debugging vs Python's `pdb` debugger?
190. [Intermediate] What is `pytest`? Write a simple test function with assertions and parameterized tests.
191. [Intermediate] How do you mock external dependencies (API calls, database) in unit tests? Explain `unittest.mock`.
192. [Intermediate] What is test-driven development (TDD)? How would you apply it to developing an ML preprocessing pipeline?
193. [Advanced] How do you profile Python code? Compare `cProfile`, `line_profiler`, and `memory_profiler`.
194. [Advanced] What are common pitfalls when debugging NumPy/Pandas code? (e.g., chained indexing, copy vs view)
195. [Expert] How would you set up property-based testing (using `hypothesis`) for a data transformation function?

---

## 2. Mathematical Foundations

### 2.1 Linear Algebra

#### Vectors & Basic Operations
196. [Basic] What is a vector? Explain the geometric interpretation of vector addition and scalar multiplication.
197. [Basic] What is the dot product of two vectors? What does it measure geometrically?
198. [Basic] What is the cross product? How does it differ from the dot product?
199. [Basic] What is the norm (magnitude) of a vector? Explain L1, L2, and L∞ norms.
200. [Basic] What does it mean for two vectors to be orthogonal? Why does this matter in ML?
201. [Intermediate] What is a unit vector? How do you normalize a vector?
202. [Intermediate] What is the cosine similarity between two vectors? Where is it used in ML and NLP?
203. [Intermediate] Explain the concept of linear independence. Why is it important in feature spaces?
204. [Intermediate] What is a basis of a vector space? What does it mean for a set of vectors to span a space?
205. [Advanced] Explain the concept of a vector space over a field. How does this abstraction help in ML?

#### Matrices & Operations
206. [Basic] What is a matrix? How do you perform matrix addition, scalar multiplication, and matrix multiplication?
207. [Basic] What is the transpose of a matrix? What are symmetric and skew-symmetric matrices?
208. [Basic] What is the identity matrix? What role does it play in linear algebra?
209. [Basic] What is matrix multiplication? Why is it not commutative (AB ≠ BA in general)?
210. [Intermediate] What is the determinant of a matrix? What does it represent geometrically?
211. [Intermediate] What is the inverse of a matrix? When does a matrix not have an inverse?
212. [Intermediate] What is the rank of a matrix? How do you compute it and why does it matter?
213. [Intermediate] What is the trace of a matrix? What is its relationship to eigenvalues?
214. [Intermediate] Explain the null space (kernel) and column space (range) of a matrix. How are they related to solutions of Ax = b?
215. [Intermediate] What are orthogonal matrices? Why are they important in numerical computation?
216. [Advanced] What is the condition number of a matrix? How does it affect numerical stability?
217. [Advanced] What are positive definite, positive semi-definite, and negative definite matrices? How do you check definiteness?
218. [Advanced] Explain the relationship between a matrix and a linear transformation. How does this connect to neural network layers?

#### Eigenvalues & Eigenvectors
219. [Intermediate] What are eigenvalues and eigenvectors? Explain the equation Av = λv.
220. [Intermediate] How do you compute eigenvalues? Explain the characteristic equation det(A - λI) = 0.
221. [Intermediate] What is the geometric interpretation of eigenvalues and eigenvectors?
222. [Intermediate] Why are eigenvalues important in PCA? What do they represent in terms of variance?
223. [Intermediate] Can all matrices be diagonalized? What conditions are required?
224. [Advanced] What is the spectral theorem? For which matrices does it guarantee an orthogonal eigendecomposition?
225. [Advanced] How are eigenvalues used in spectral clustering? Explain the graph Laplacian.
226. [Advanced] What is the power iteration method for computing the dominant eigenvalue? What are its limitations?
227. [Expert] Explain the eigendecomposition A = QΛQ⁻¹. When does A = QΛQᵀ hold?
228. [Expert] How do eigenvalues relate to the stability of dynamical systems and recurrent neural networks?

#### Singular Value Decomposition (SVD)
229. [Intermediate] What is Singular Value Decomposition? Explain A = UΣVᵀ.
230. [Intermediate] What are the interpretations of U, Σ, and V in SVD?
231. [Intermediate] How is SVD related to PCA? Derive the connection.
232. [Intermediate] How is SVD used for dimensionality reduction (truncated SVD)?
233. [Advanced] How is SVD used in recommender systems (matrix factorization)?
234. [Advanced] How is SVD used in Latent Semantic Analysis (LSA) for NLP?
235. [Advanced] What is the relationship between SVD and the pseudoinverse (Moore-Penrose inverse)?
236. [Advanced] How is SVD used for image compression? Explain the low-rank approximation.
237. [Expert] What is the Eckart-Young theorem? Why is truncated SVD the optimal low-rank approximation?
238. [Expert] Explain randomized SVD and its advantages for large-scale data.

#### Matrix Decompositions
239. [Intermediate] What is LU decomposition? When is it used?
240. [Intermediate] What is QR decomposition? How is it used in least squares problems?
241. [Intermediate] What is Cholesky decomposition? For which matrices is it valid?
242. [Advanced] When would you prefer Cholesky over LU decomposition?
243. [Advanced] Compare Gram-Schmidt vs Householder methods for QR decomposition in terms of numerical stability.
244. [Advanced] How is the QR algorithm used to compute eigenvalues?
245. [Expert] What is the non-negative matrix factorization (NMF)? How is it used in topic modeling and image processing?
246. [Expert] Explain how matrix decompositions are used to solve large linear systems efficiently in ML.

#### PCA & Applications
247. [Intermediate] Explain the step-by-step procedure of Principal Component Analysis.
248. [Intermediate] Why must you center (and often standardize) data before applying PCA?
249. [Intermediate] How do you decide how many principal components to retain? Explain the scree plot and cumulative explained variance.
250. [Intermediate] What is the difference between PCA and factor analysis?
251. [Advanced] Derive PCA from the perspective of maximizing variance.
252. [Advanced] Derive PCA from the perspective of minimizing reconstruction error.
253. [Advanced] What is Kernel PCA? When would you use it over standard PCA?
254. [Advanced] What is Incremental PCA? When is it necessary?
255. [Expert] How does Probabilistic PCA relate to standard PCA? What additional assumptions does it make?
256. [Expert] Explain Sparse PCA. When and why would you use it?

### 2.2 Calculus & Optimization

#### Derivatives & Gradients
257. [Basic] What is a derivative? Explain its geometric interpretation.
258. [Basic] What are partial derivatives? How do they extend derivatives to multivariate functions?
259. [Basic] What is the gradient of a function? How does it relate to the direction of steepest ascent?
260. [Basic] Compute the gradient of f(x, y) = x² + 3xy + y². Evaluate it at (1, 2).
261. [Intermediate] What is the directional derivative? How does it relate to the gradient?
262. [Intermediate] What is the chain rule? Why is it fundamental to backpropagation?
263. [Intermediate] Derive the gradient of the mean squared error (MSE) loss with respect to the weights.
264. [Intermediate] What is the difference between a total derivative and a partial derivative?
265. [Advanced] What is the Jacobian matrix? When is it needed instead of a simple gradient?
266. [Advanced] What is the Hessian matrix? What does it tell us about the curvature of a function?
267. [Advanced] How do you use the Hessian to determine if a critical point is a minimum, maximum, or saddle point?
268. [Advanced] What are higher-order derivatives? Why are they important in optimization (e.g., Newton's method)?
269. [Expert] Explain automatic differentiation (autograd). How does forward-mode differ from reverse-mode AD?
270. [Expert] What is the difference between symbolic, numerical, and automatic differentiation? Which does PyTorch/TensorFlow use?

#### Backpropagation
271. [Intermediate] Explain the backpropagation algorithm step by step.
272. [Intermediate] How does the chain rule enable gradient computation through multiple layers?
273. [Advanced] Derive the backpropagation equations for a simple two-layer neural network.
274. [Advanced] What is the vanishing gradient problem? How do activation functions and architectures address it?
275. [Advanced] What is the exploding gradient problem? How do gradient clipping and normalization help?
276. [Expert] Explain backpropagation through time (BPTT) in recurrent neural networks.
277. [Expert] What is the computational graph? How do frameworks like PyTorch build and traverse it?

#### Optimization Algorithms
278. [Basic] What is gradient descent? Explain the update rule.
279. [Basic] What is the learning rate? What happens if it is too large or too small?
280. [Intermediate] What is the difference between batch, stochastic, and mini-batch gradient descent?
281. [Intermediate] Why might gradient descent fail to find the global minimum? Discuss local minima and saddle points.
282. [Intermediate] What is momentum in gradient descent? How does it help?
283. [Intermediate] Explain the Adam optimizer. Why is it so widely used?
284. [Intermediate] What is learning rate scheduling? Describe step decay, exponential decay, and cosine annealing.
285. [Advanced] Explain the RMSprop optimizer. How does it differ from Adam?
286. [Advanced] What is Nesterov accelerated gradient (NAG)? How does look-ahead improve convergence?
287. [Advanced] Compare first-order methods (gradient descent) vs second-order methods (Newton's method, L-BFGS). When would you use each?
288. [Advanced] What is a convex function? Why does convexity guarantee that local minima are global minima?
289. [Advanced] Give examples of convex and non-convex loss functions in ML.
290. [Expert] What is the convergence rate of gradient descent for convex vs strongly convex functions?
291. [Expert] Explain the KKT (Karush-Kuhn-Tucker) conditions for constrained optimization.
292. [Expert] What is Lagrangian duality? How is it used in SVMs?
293. [Expert] What is proximal gradient descent? When is it used (e.g., L1 regularization)?

#### Calculus in ML Models
294. [Intermediate] Derive the gradient of the sigmoid function σ(x) and show that σ'(x) = σ(x)(1 − σ(x)).
295. [Intermediate] Derive the gradient of the softmax function.
296. [Intermediate] Derive the gradient of the cross-entropy loss combined with softmax.
297. [Advanced] What is the relationship between L2 regularization and weight decay? Derive it.
298. [Advanced] Derive the closed-form solution for ordinary least squares (OLS) using calculus.
299. [Expert] Derive the EM (Expectation-Maximization) algorithm and explain its convergence guarantees.
300. [Expert] Explain natural gradient descent. How does it use the Fisher information matrix?

### 2.3 Probability & Statistics

#### Probability Fundamentals
301. [Basic] What is the difference between a probability and a likelihood?
302. [Basic] Explain the axioms of probability (Kolmogorov axioms).
303. [Basic] What is conditional probability? Write the formula for P(A|B).
304. [Basic] What are independent events? How do you test for independence?
305. [Basic] What is the law of total probability?
306. [Intermediate] What is the difference between joint, marginal, and conditional probability?
307. [Intermediate] What is the difference between permutation and combination? Give an ML-related example.
308. [Advanced] What is the probability chain rule? How does it decompose a joint distribution?
309. [Advanced] Explain the concept of a probability measure and sigma-algebra (measure-theoretic probability).

#### Bayes Theorem
310. [Intermediate] State and explain Bayes' theorem. Give a real-world example.
311. [Intermediate] Explain the "base rate fallacy" using a medical testing example with Bayes' theorem.
312. [Intermediate] How is Bayes' theorem used in the Naive Bayes classifier?
313. [Advanced] What are prior, likelihood, posterior, and evidence in Bayesian inference? Explain each term.
314. [Advanced] What is a conjugate prior? Give examples for Bernoulli, Gaussian, and Poisson likelihoods.
315. [Expert] Explain the relationship between Bayesian inference and regularization (L2 regularization as Gaussian prior).
316. [Expert] What is Bayesian model comparison? Explain the marginal likelihood (model evidence).

#### Probability Distributions
317. [Basic] What is the difference between discrete and continuous probability distributions?
318. [Basic] What are the mean, variance, and standard deviation of a distribution?
319. [Basic] Describe the Bernoulli and Binomial distributions. When is each used?
320. [Basic] What is a uniform distribution? When is it used in ML (e.g., random initialization)?
321. [Intermediate] Describe the Normal (Gaussian) distribution. What are its key properties?
322. [Intermediate] What is the standard normal distribution? How do you standardize a normal variable (z-score)?
323. [Intermediate] Describe the Poisson distribution. When is it appropriate to use?
324. [Intermediate] Describe the exponential distribution. How is it related to the Poisson distribution?
325. [Intermediate] What is the multivariate Gaussian distribution? What role does the covariance matrix play?
326. [Advanced] What are the Beta and Dirichlet distributions? Where are they used in ML (e.g., topic modeling)?
327. [Advanced] What is a mixture model (e.g., Gaussian Mixture Model)? How is it different from a single distribution?
328. [Advanced] What is the Gamma distribution? What is its relationship to the exponential and chi-squared distributions?
329. [Expert] What is the Student's t-distribution? When should you use it instead of the normal distribution?
330. [Expert] What is the chi-squared distribution? How is it used in hypothesis testing?

#### Expectation, Variance & Moments
331. [Basic] What is the expected value (mean) of a random variable? How do you compute it?
332. [Basic] What is variance? What is the relationship between variance and standard deviation?
333. [Intermediate] What is covariance? What does it measure?
334. [Intermediate] What is the correlation coefficient? How does it relate to covariance?
335. [Intermediate] What is the law of large numbers? How does it justify using sample means?
336. [Intermediate] What is the Central Limit Theorem (CLT)? Why is it important in statistics?
337. [Advanced] What are skewness and kurtosis? What do they tell you about a distribution?
338. [Advanced] What is the moment-generating function (MGF)? How is it useful?
339. [Expert] What is the characteristic function of a distribution? When is it preferred over the MGF?

#### MLE & MAP
340. [Intermediate] What is Maximum Likelihood Estimation (MLE)? Write the formula.
341. [Intermediate] Derive the MLE for the mean and variance of a Gaussian distribution.
342. [Intermediate] What is Maximum a Posteriori (MAP) estimation? How does it differ from MLE?
343. [Advanced] When does MAP reduce to MLE? When would you prefer MAP?
344. [Advanced] Show that MAP with a Gaussian prior on weights is equivalent to L2 regularization.
345. [Advanced] Show that MAP with a Laplacian prior on weights is equivalent to L1 regularization.
346. [Expert] What are the limitations of point estimates (MLE/MAP) vs full Bayesian inference?
347. [Expert] Derive the MLE for the parameters of a Bernoulli distribution.

#### Hypothesis Testing
348. [Intermediate] What is a null hypothesis and an alternative hypothesis?
349. [Intermediate] What are Type I and Type II errors? How do they relate to false positives and false negatives?
350. [Intermediate] What is a p-value? How do you interpret it correctly?
351. [Intermediate] What is a significance level (α)? What does it mean to set α = 0.05?
352. [Intermediate] Explain the steps of a hypothesis testing workflow.
353. [Intermediate] What is the difference between a one-tailed and a two-tailed test?
354. [Advanced] What is statistical power? How does sample size affect it?
355. [Advanced] What is the multiple comparisons problem? How do Bonferroni and Benjamini-Hochberg corrections address it?
356. [Advanced] What is the t-test? When do you use a one-sample, two-sample, or paired t-test?
357. [Advanced] What is ANOVA? When is it used instead of a t-test?
358. [Advanced] What is the chi-squared test? When is it used?
359. [Expert] What is the likelihood ratio test? How does it relate to hypothesis testing?
360. [Expert] Explain the difference between frequentist and Bayesian approaches to hypothesis testing.

#### Confidence Intervals & Estimation
361. [Intermediate] What is a confidence interval? How do you interpret a 95% confidence interval?
362. [Intermediate] What factors affect the width of a confidence interval?
363. [Intermediate] How do you construct a confidence interval for the mean of a normal population?
364. [Advanced] What is a bootstrap confidence interval? When is bootstrapping preferred?
365. [Advanced] What is the difference between a confidence interval and a credible interval (Bayesian)?
366. [Expert] How do you compute confidence intervals for model performance metrics (accuracy, AUC)?

### 2.4 Information Theory

367. [Intermediate] What is entropy in information theory? Write the formula and explain intuitively.
368. [Intermediate] How is entropy used in decision trees to determine the best split?
369. [Intermediate] What is joint entropy? How does it relate to individual entropies?
370. [Intermediate] What is conditional entropy H(Y|X)? How does it relate to mutual information?
371. [Advanced] What is cross-entropy? Write the formula and explain its use as a loss function.
372. [Advanced] What is the relationship between cross-entropy, entropy, and KL divergence? (H(P,Q) = H(P) + D_KL(P||Q))
373. [Advanced] Why is cross-entropy used as the loss function for classification instead of MSE?
374. [Advanced] What happens to cross-entropy loss when the predicted probability for the true class approaches zero?
375. [Advanced] What is KL divergence (Kullback-Leibler divergence)? Write the formula.
376. [Advanced] Why is KL divergence not a true distance metric? (It is not symmetric.)
377. [Advanced] Where is KL divergence used in machine learning? (VAEs, knowledge distillation, policy optimization)
378. [Expert] What is mutual information? Write the formula and explain its relationship to entropy.
379. [Expert] How is mutual information used for feature selection?
380. [Expert] What is the information bottleneck method?
381. [Expert] What is the Jensen-Shannon divergence? How does it address the asymmetry of KL divergence?
382. [Expert] How do you estimate entropy or mutual information from finite data? Discuss bias and correction methods.
383. [Expert] Explain the Data Processing Inequality. What does it imply about feature transformation?

---

## 3. Data Fundamentals

### 3.1 Data Preprocessing & Cleaning

384. [Basic] What are the common steps in a data preprocessing pipeline?
385. [Basic] How do you identify missing values in a dataset? What tools do you use?
386. [Basic] List at least 5 strategies for handling missing data. When is each appropriate?
387. [Basic] What is the difference between removing and imputing missing values?
388. [Intermediate] What is mean/median/mode imputation? When does each fail?
389. [Intermediate] When would you use model-based imputation (e.g., KNN imputer, iterative imputer)?
390. [Intermediate] What is MICE (Multiple Imputation by Chained Equations)? How does it work?
391. [Intermediate] How do you handle missing data in categorical vs numerical features?
392. [Advanced] How would you handle data that is Missing Completely At Random (MCAR) vs Missing At Random (MAR) vs Missing Not At Random (MNAR)?
393. [Advanced] Should you flag missingness as a feature? When and why?

#### Outlier Detection & Treatment
394. [Basic] What is an outlier? Why do outliers matter in machine learning?
395. [Basic] How do you visually detect outliers? (box plots, scatter plots, histograms)
396. [Intermediate] Explain the IQR (Interquartile Range) method for outlier detection.
397. [Intermediate] How do you use z-scores to detect outliers? What threshold is typically used?
398. [Intermediate] What are the main approaches for treating outliers? (removal, capping/winsorizing, transformation)
399. [Advanced] When should you keep outliers in your data? Give examples from ML applications.
400. [Advanced] How does the Isolation Forest algorithm detect outliers?
401. [Advanced] How does DBSCAN identify outliers in the clustering process?

#### Data Scaling & Encoding
402. [Basic] What is feature scaling? Why is it important for ML algorithms?
403. [Basic] What is the difference between normalization (MinMax scaling) and standardization (z-score scaling)?
404. [Basic] Which ML algorithms are sensitive to feature scaling and which are not?
405. [Intermediate] What is `RobustScaler`? When is it preferred over StandardScaler?
406. [Intermediate] How do you encode categorical variables? Explain one-hot encoding vs label encoding.
407. [Intermediate] What is ordinal encoding? When is it appropriate?
408. [Intermediate] How do you handle high-cardinality categorical features? Discuss target encoding, frequency encoding, and hash encoding.
409. [Advanced] What are cyclical features (e.g., day of week, month)? How should they be encoded?
410. [Advanced] What is the entity embedding approach for categorical variables?
411. [Advanced] When would you use a log transform or Box-Cox transform on features?

#### Text & Time Series Preprocessing
412. [Intermediate] What steps are involved in preprocessing text data for NLP? (tokenization, lowercasing, stop words, stemming, lemmatization)
413. [Intermediate] How do you handle dates and timestamps as features? What features can you extract?
414. [Advanced] How do you preprocess time series data? What are lag features and rolling statistics?
415. [Advanced] How do you handle irregular time series (missing timestamps, uneven intervals)?

### 3.2 Feature Engineering

416. [Basic] What is feature engineering? Why is it often more impactful than model selection?
417. [Basic] Give examples of creating new features from existing ones (interaction terms, polynomial features, ratios).
418. [Intermediate] How do you engineer features from date/time columns? (day of week, month, is_weekend, is_holiday, time since event)
419. [Intermediate] What are interaction features? When are they useful?
420. [Intermediate] What are polynomial features? When do they help and when do they hurt?
421. [Intermediate] What is binning (discretization)? When would you bin continuous variables?
422. [Advanced] What is target encoding? What are the risks of naive target encoding (data leakage)?
423. [Advanced] How do you engineer features from text data? (TF-IDF, word counts, n-grams, embeddings)
424. [Advanced] How do you engineer features from geospatial data? (distance calculations, clustering, region encoding)
425. [Expert] What is automated feature engineering? Explain tools like Featuretools and feature stores.
426. [Expert] How do you engineer features for a recommendation system? (user-item interaction features, collaborative features)

### 3.3 Feature Selection & Dimensionality Reduction

427. [Basic] What is feature selection? Why is it important?
428. [Basic] What are the three main categories of feature selection methods? (filter, wrapper, embedded)
429. [Intermediate] Explain variance threshold as a feature selection method.
430. [Intermediate] How do you use correlation analysis for feature selection? What is multicollinearity?
431. [Intermediate] What is the chi-squared test for feature selection? When is it applicable?
432. [Intermediate] What is Recursive Feature Elimination (RFE)? How does it work?
433. [Intermediate] How do tree-based feature importances work? What are their limitations?
434. [Advanced] What is the Variance Inflation Factor (VIF)? How do you use it to detect multicollinearity?
435. [Advanced] How does L1 regularization (Lasso) perform feature selection?
436. [Advanced] What is permutation importance? How does it differ from model-based feature importance?
437. [Advanced] How do SHAP values help with feature selection?
438. [Expert] What is the curse of dimensionality? How does it affect ML model performance?

#### Dimensionality Reduction Techniques
439. [Intermediate] What is the difference between feature selection and feature extraction?
440. [Intermediate] When would you prefer dimensionality reduction over feature selection?
441. [Intermediate] What is t-SNE? How does it differ from PCA?
442. [Intermediate] What is UMAP? How does it compare to t-SNE?
443. [Advanced] What are the main differences between t-SNE and UMAP in terms of speed, scalability, and global structure preservation?
444. [Advanced] Can you use t-SNE or UMAP for feature reduction before model training? Why or why not?
445. [Advanced] What is Linear Discriminant Analysis (LDA)? How does it differ from PCA?
446. [Expert] What is an autoencoder-based dimensionality reduction? When is it preferred over PCA?
447. [Expert] What are random projections (Johnson-Lindenstrauss lemma)? When are they useful?

### 3.4 Handling Imbalanced Datasets

448. [Basic] What is an imbalanced dataset? Give real-world examples.
449. [Basic] Why is accuracy a poor metric for imbalanced datasets?
450. [Intermediate] What metrics should you use for imbalanced datasets? (Precision, Recall, F1, AUC-ROC, AUC-PR)
451. [Intermediate] Explain the precision-recall tradeoff.
452. [Intermediate] What is the difference between ROC curve and Precision-Recall curve? When is each more appropriate?
453. [Intermediate] What is random oversampling and random undersampling? What are the risks of each?
454. [Intermediate] What is SMOTE (Synthetic Minority Over-sampling Technique)? How does it work?
455. [Advanced] What are the risks of SMOTE? When can it produce unrealistic samples?
456. [Advanced] How does adjusting class weights in the loss function help with imbalanced data?
457. [Advanced] How do ensemble methods (e.g., BalancedRandomForest, EasyEnsemble) handle imbalanced datasets?
458. [Advanced] What is cost-sensitive learning? How do you implement it in scikit-learn?
459. [Expert] How do you handle extreme class imbalance (e.g., 1:10,000)? Discuss anomaly detection approaches.
460. [Expert] What is focal loss? How does it address class imbalance in deep learning?

### 3.5 Data Splitting & Validation

461. [Basic] Why do we split data into training, validation, and test sets?
462. [Basic] What is a typical ratio for train/validation/test split?
463. [Basic] What is data leakage? Give examples of how it can occur.
464. [Intermediate] What is k-fold cross-validation? How do you choose k?
465. [Intermediate] What is stratified k-fold cross-validation? When is it necessary?
466. [Intermediate] What is leave-one-out cross-validation (LOOCV)? What are its advantages and disadvantages?
467. [Intermediate] How does data leakage occur during preprocessing? How do you prevent it using pipelines?
468. [Advanced] How should you split time series data? Explain walk-forward validation.
469. [Advanced] What is group k-fold cross-validation? When do you use it?
470. [Advanced] What is nested cross-validation? When is it necessary?
471. [Expert] How do you handle data leakage when doing feature engineering (e.g., target encoding, scaling)?
472. [Expert] What is the difference between in-distribution and out-of-distribution evaluation? Why does it matter?

### 3.6 Data Augmentation

473. [Basic] What is data augmentation? Why is it useful?
474. [Basic] Give examples of data augmentation for images. (flip, rotate, crop, color jitter, noise)
475. [Intermediate] How does data augmentation help prevent overfitting?
476. [Intermediate] What are data augmentation techniques for text? (synonym replacement, back-translation, random insertion/deletion)
477. [Intermediate] Can data augmentation be applied to tabular data? How? (SMOTE, noise injection, mixup)
478. [Advanced] What is Mixup? What is CutMix? Explain how they work.
479. [Advanced] What is test-time augmentation (TTA)? How does it improve predictions?
480. [Expert] What are the potential downsides of data augmentation? When can it hurt performance?
481. [Expert] What is generative data augmentation (using GANs or diffusion models to create synthetic data)?

### 3.7 SQL & Data Pipelines for ML

#### SQL Fundamentals
482. [Basic] What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?
483. [Basic] Write a SQL query to find the count of records per category in a table.
484. [Basic] What is the difference between `WHERE` and `HAVING` in SQL?
485. [Basic] How do you handle NULL values in SQL? Explain `IS NULL`, `COALESCE`, and `IFNULL`.
486. [Intermediate] Explain window functions. What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?
487. [Intermediate] Write a SQL query to compute a running total using a window function.
488. [Intermediate] What is a CTE (Common Table Expression)? When is it preferable to a subquery?
489. [Intermediate] Write a SQL query to find the second highest salary in each department.
490. [Intermediate] Explain `LAG()` and `LEAD()` functions. Write a query to find day-over-day change in a metric.
491. [Advanced] Write a SQL query to detect consecutive events (e.g., users who logged in 3+ consecutive days).
492. [Advanced] What is a recursive CTE? Write one to traverse a hierarchical relationship.
493. [Advanced] How do you optimize slow SQL queries? Discuss indexing, query plans, and partitioning.
494. [Expert] How do you write SQL for feature engineering at scale? (rolling aggregates, sessionization, pivoting)

#### Data Pipelines & Infrastructure
495. [Intermediate] What is ETL vs ELT? When would you choose one over the other?
496. [Intermediate] What is idempotency in data pipelines? Why is it important?
497. [Intermediate] What tools are commonly used for ML data pipelines? (Airflow, Prefect, Dagster, Luigi)
498. [Advanced] What is a feature store? Why is it important for ML in production? (Feast, Tecton)
499. [Advanced] What is data versioning? What tools support it? (DVC, LakeFS, Delta Lake)
500. [Advanced] How do you ensure data quality in an ML pipeline? Discuss validation frameworks (Great Expectations, Pandera).
501. [Advanced] How do you handle schema evolution in data pipelines?
502. [Expert] How do you design a data pipeline for real-time ML inference vs batch inference?
503. [Expert] What is data drift? How do you monitor for it in production?
504. [Expert] Explain the difference between data versioning and model versioning. Why are both necessary?
505. [Expert] How do you build reproducible ML experiments? Discuss the role of data, code, and environment versioning.

### 3.8 Exploratory Data Analysis (EDA)

506. [Basic] What is EDA? Why is it an essential step before model building?
507. [Basic] What summary statistics should you compute for a new dataset?
508. [Basic] How do you visualize the distribution of a numerical variable? (histogram, KDE, box plot)
509. [Intermediate] How do you identify relationships between features? (scatter plots, correlation heatmaps, pair plots)
510. [Intermediate] How do you handle skewed distributions during EDA? When should you transform them?
511. [Intermediate] What is the difference between univariate, bivariate, and multivariate analysis?
512. [Advanced] How do you detect data drift during EDA? What statistical tests can you use?
513. [Advanced] How would you perform EDA on a dataset with 1000+ features?
514. [Expert] How do you automate EDA? Discuss tools like pandas-profiling/ydata-profiling, sweetviz, and D-Tale.

### 3.9 Data Ethics & Quality

515. [Basic] What is sampling bias? Give an example in ML.
516. [Basic] What is survivorship bias? How can it affect ML models?
517. [Intermediate] What is label noise? How does it affect model training and evaluation?
518. [Intermediate] How do you measure and ensure data quality? What are common data quality dimensions?
519. [Advanced] What is fairness in ML datasets? How do you detect and mitigate bias in training data?
520. [Advanced] What is differential privacy? How can it be applied during data collection?
521. [Expert] What are the ethical considerations when using web-scraped data for training ML models?
522. [Expert] How do you handle personally identifiable information (PII) in ML datasets?

---

## Quick Reference: Question Count by Section

| Section | Count |
|---------|-------|
| 1.1 Python Basics & Core Concepts | 80 |
| 1.2 Python Libraries for ML | 52 |
| 1.3 Advanced Python Concepts | 26 |
| 1.4 Python Coding & Implementation | 29 |
| **Total: Python Programming** | **195** |
| 2.1 Linear Algebra | 61 |
| 2.2 Calculus & Optimization | 44 |
| 2.3 Probability & Statistics | 66 |
| 2.4 Information Theory | 17 |
| **Total: Mathematics** | **188** |
| 3.1 Data Preprocessing & Cleaning | 28 |
| 3.2 Feature Engineering | 11 |
| 3.3 Feature Selection & Dimensionality Reduction | 21 |
| 3.4 Handling Imbalanced Datasets | 13 |
| 3.5 Data Splitting & Validation | 12 |
| 3.6 Data Augmentation | 9 |
| 3.7 SQL & Data Pipelines | 24 |
| 3.8 Exploratory Data Analysis | 9 |
| 3.9 Data Ethics & Quality | 8 |
| **Total: Data Fundamentals** | **139** |
| **GRAND TOTAL** | **522** |

---

> **Difficulty Distribution:** ~25% Basic, ~35% Intermediate, ~28% Advanced, ~12% Expert
>
> **Sources:** Compiled from real interview questions reported on Glassdoor, LeetCode Discuss, Towards Data Science, Medium, Analytics Vidhya, KDNuggets, Machine Learning Mastery, company-specific interview guides (Google, Meta, Amazon, Netflix), and academic resources (2024–2025).



---


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



---


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



---


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



---


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



---


# Part 6: ML Systems, Bayesian ML, RL & Ethics

---

## 16. ML Systems & Production

### 16.1 Model Serving & Inference

1. What is model serving, and how does it differ from model training? [Basic]
2. Compare REST APIs vs gRPC for model serving — when would you choose one over the other? [Intermediate]
3. What are the latency and throughput tradeoffs between REST and gRPC for inference endpoints? [Intermediate]
4. Explain the difference between batch inference and real-time (online) inference. [Basic]
5. When would you choose batch inference over real-time serving? Give three concrete examples. [Intermediate]
6. How would your deployment architecture differ between batch and real-time inference? [Intermediate]
7. What is dynamic batching in model serving, and how does it improve throughput? [Intermediate]
8. Compare TensorFlow Serving, TorchServe, Triton Inference Server, and BentoML — what are the pros and cons of each? [Intermediate]
9. How does NVIDIA Triton Inference Server handle multiple model frameworks simultaneously? [Advanced]
10. What is model warm-up, and why is it important to avoid cold-start latencies? [Intermediate]
11. How would you design a system to serve multiple models with different versions at the same endpoint? [Advanced]
12. What is the role of an API gateway in a model serving architecture? [Intermediate]
13. How do you handle request queuing and backpressure in a model serving system? [Advanced]
14. What is model ensembling at serving time, and when is it practical? [Intermediate]
15. Explain how you would implement request batching to optimize GPU utilization during inference. [Advanced]
16. How do you handle model inference timeouts gracefully? [Intermediate]
17. What are the key differences between synchronous and asynchronous inference endpoints? [Basic]
18. How would you serve a model that requires preprocessing (e.g., tokenization, image resizing) — where does preprocessing happen? [Intermediate]
19. What is a prediction cache, and when would you use one? [Intermediate]
20. How do you implement graceful degradation when a model serving endpoint becomes overloaded? [Advanced]
21. What is the role of Protocol Buffers (protobuf) in gRPC-based model serving? [Intermediate]
22. How would you design a multi-model serving system where different models are chained in a pipeline? [Advanced]
23. What is the difference between model-as-a-service and embedded model inference? [Basic]
24. How do you handle feature computation at serving time vs pre-computed features? [Intermediate]
25. Explain streaming inference and give a use case where it's essential. [Advanced]
26. What is server-side vs client-side batching for inference? [Intermediate]
27. How would you reduce the memory footprint of a model in production serving? [Intermediate]
28. What is model serialization, and what formats are commonly used (ONNX, SavedModel, TorchScript, pickle)? [Basic]
29. How do you benchmark model serving performance? What metrics matter? [Intermediate]
30. What are the trade-offs between using a custom Flask/FastAPI server vs a dedicated serving framework? [Intermediate]

### 16.2 Model Deployment

31. What are the key steps in deploying an ML model from development to production? [Basic]
32. Why is Docker important for ML model deployment? What problems does it solve? [Basic]
33. What is a Dockerfile? What are best practices for writing one for ML models? [Intermediate]
34. How would you reduce Docker image size for faster deployments of ML models? [Intermediate]
35. What are multi-stage builds in Docker, and why are they important for ML? [Intermediate]
36. How do you manage secrets (API keys, credentials) when deploying containerized models? [Intermediate]
37. Explain Kubernetes Pods, Deployments, and Services in the context of ML model serving. [Intermediate]
38. How would you deploy a machine learning model as a service on Kubernetes? [Intermediate]
39. How do you perform rolling updates and rollbacks of ML services on Kubernetes? [Intermediate]
40. Explain Horizontal Pod Autoscaler (HPA) and how you'd tune it for dynamic ML workloads. [Advanced]
41. What is KServe (formerly KFServing), and how does it simplify ML model deployment on Kubernetes? [Advanced]
42. Compare Seldon Core vs KServe for model deployment — when would you choose each? [Advanced]
43. How would you deploy an ML model using AWS SageMaker endpoints? [Intermediate]
44. What is serverless inference, and when is it appropriate for ML? [Intermediate]
45. Compare AWS Lambda, Google Cloud Functions, and Azure Functions for ML inference. [Intermediate]
46. What are the challenges of deploying models on edge devices vs cloud? [Intermediate]
47. How would you deploy a model on mobile devices using TensorFlow Lite or Core ML? [Advanced]
48. What is ONNX Runtime, and how does it enable cross-platform model deployment? [Intermediate]
49. How do you handle GPU resource management in Kubernetes for ML models? [Advanced]
50. What is model quantization, and how does it enable edge deployment? [Intermediate]
51. Compare INT8 quantization, FP16 mixed precision, and pruning for deployment optimization. [Advanced]
52. How would you deploy a model to an NVIDIA Jetson device for edge inference? [Advanced]
53. What is model distillation, and how does it help with deployment on resource-constrained devices? [Intermediate]
54. How do you manage and roll out model updates at the edge? [Advanced]
55. Discuss strategies for monitoring, logging, and debugging at the edge. [Advanced]
56. How would you secure model inference and data in low-trust edge locations? [Advanced]
57. What is blue/green deployment in the context of ML inference services? [Intermediate]
58. How would you implement an immutable deployment pipeline for ML models? [Advanced]
59. What is infrastructure-as-code (IaC), and how do tools like Terraform/Pulumi help with ML deployment? [Intermediate]
60. How do you handle model dependencies and environment reproducibility across deployment stages? [Intermediate]
61. What is the role of container registries in ML deployment pipelines? [Basic]
62. How would you deploy a 70B parameter LLM for production inference? Discuss hardware, quantization, and serving strategies. [Expert]
63. What is tensor parallelism vs pipeline parallelism for serving large models? [Expert]
64. How does vLLM optimize LLM serving with PagedAttention? [Expert]
65. Compare NVIDIA TensorRT, ONNX Runtime, and torch.compile for inference optimization. [Advanced]

### 16.3 MLOps & CI/CD for ML

66. What is MLOps, and how does it differ from traditional DevOps? [Basic]
67. Describe the key components of an MLOps pipeline. [Basic]
68. How would you design a CI/CD pipeline for ML models? [Intermediate]
69. What tools would you use for ML CI/CD (Kubeflow, MLflow, Argo, TFX, SageMaker Pipelines)? [Intermediate]
70. What is experiment tracking, and why is it critical in ML projects? [Basic]
71. Compare MLflow, Weights & Biases (W&B), Neptune.ai, and Comet.ml for experiment tracking. [Intermediate]
72. How would you organize experiments to compare different model architectures? [Intermediate]
73. What is a model registry, and what problems does it solve in MLOps? [Basic]
74. How would you set up a promotion workflow (Staging → Production) using a model registry? [Intermediate]
75. Compare MLflow Model Registry, SageMaker Model Registry, and Vertex AI Model Registry. [Intermediate]
76. What is model lineage, and why is tracking it important? [Intermediate]
77. How do you ensure reproducibility from dataset to model deployment? [Intermediate]
78. What is a feature store, and why is it important in an MLOps pipeline? [Basic]
79. How does a feature store help with feature consistency between training and inference? [Intermediate]
80. Compare Feast, Tecton, AWS SageMaker Feature Store, and Databricks Feature Store. [Intermediate]
81. What is training-serving skew, and how does a feature store prevent it? [Intermediate]
82. How do you design online and offline feature stores for serving? [Advanced]
83. What is data versioning, and why is it important in ML projects? [Basic]
84. How does DVC (Data Version Control) work, and what are its key benefits? [Intermediate]
85. How does DVC manage large datasets alongside Git? [Intermediate]
86. Explain a scenario where DVC would help in collaboration within an ML team. [Intermediate]
87. Compare DVC, LakeFS, Delta Lake, and Pachyderm for data versioning. [Advanced]
88. How would you version both data and model artifacts in a production ML system? [Intermediate]
89. What is a DAG (Directed Acyclic Graph) in the context of ML pipelines, and how do tools like Airflow use them? [Intermediate]
90. How do you handle schema evolution in ML data pipelines? [Advanced]
91. What is the difference between data validation and data testing in MLOps? [Intermediate]
92. How would you implement automated model validation before deployment? [Intermediate]
93. What is Great Expectations, and how can it be used for data quality in ML pipelines? [Intermediate]
94. How do you handle pipeline failures and retries in production ML workflows? [Intermediate]
95. What is the role of metadata stores in MLOps? [Intermediate]
96. How do you implement automated retraining triggers based on performance degradation? [Advanced]
97. What is continuous training (CT) in MLOps, and how does it differ from CI/CD? [Intermediate]
98. How would you design an ML pipeline that handles both streaming and batch data? [Advanced]
99. What is the ML lifecycle, and what are the key stages? [Basic]
100. How do you manage configuration drift across ML environments (dev, staging, production)? [Advanced]

### 16.4 Monitoring & Observability

101. What metrics would you log and monitor after deploying an ML model? [Basic]
102. What is data drift, and how does it differ from concept drift? [Basic]
103. How do you detect data drift in production? Name specific statistical tests. [Intermediate]
104. Explain the KS-test (Kolmogorov-Smirnov) for detecting data drift. [Intermediate]
105. What is Population Stability Index (PSI), and how is it used for drift detection? [Intermediate]
106. How do you detect concept drift in a deployed model? [Intermediate]
107. What is model degradation, and what are the common causes? [Basic]
108. How would you set up alerting for model performance degradation? [Intermediate]
109. What tools can you use for drift monitoring at scale (Evidently AI, Alibi Detect, Arize AI, Fiddler)? [Intermediate]
110. How do you monitor prediction confidence distributions to spot out-of-distribution data? [Intermediate]
111. What is prediction drift, and how does it relate to input data drift? [Intermediate]
112. How do you handle monitoring when ground truth labels are delayed (e.g., fraud, churn models)? [Advanced]
113. Suppose your model's accuracy drops suddenly in production but feature distributions look unchanged — what do you investigate? [Advanced]
114. How can you reduce false positives in drift or degradation alerts? [Advanced]
115. Discuss trade-offs between sensitivity and stability in drift detection. [Advanced]
116. How does data drift monitoring change with GenAI and LLMs (embedding-based drift)? [Advanced]
117. What is the role of logging and tracing in ML systems (OpenTelemetry, Jaeger)? [Intermediate]
118. How do you implement distributed tracing across an ML inference pipeline? [Advanced]
119. What is model observability, and how does it differ from model monitoring? [Intermediate]
120. How would you design a dashboard for ML model health in production? [Intermediate]
121. What are the key SLAs/SLOs for an ML serving system? [Intermediate]
122. How do you monitor GPU utilization and memory usage for inference workloads? [Intermediate]
123. What is the difference between technical metrics (latency, throughput) and business metrics (conversion rate, CTR) for ML monitoring? [Intermediate]
124. How do you correlate model prediction quality with business outcomes? [Advanced]
125. What is a feedback loop in ML monitoring, and how can it cause model degradation? [Advanced]
126. How would you automate drift detection and model retraining? [Intermediate]
127. What is a shadow evaluation, and how does it help with monitoring? [Intermediate]
128. How do you monitor fairness metrics in production? [Advanced]
129. What is the role of canary analysis in detecting model issues before full rollout? [Intermediate]
130. How do you handle multivariate drift detection (drift across multiple features simultaneously)? [Advanced]

### 16.5 A/B Testing, Canary & Shadow Deployments

131. What is A/B testing for ML models, and how does it differ from traditional A/B testing? [Basic]
132. How do you design a robust A/B test to compare two ML models in production? [Intermediate]
133. What are the key metrics you would monitor during an A/B test for an ML model? [Intermediate]
134. How do you ensure statistical significance in A/B testing? [Intermediate]
135. What sample size do you need for a valid A/B test, and how do you calculate it? [Intermediate]
136. What are common pitfalls or biases in A/B testing for ML? [Intermediate]
137. How do you handle the multiple comparisons problem in A/B testing? [Advanced]
138. What is a multi-armed bandit approach to A/B testing, and when is it preferred? [Advanced]
139. What is canary deployment, and how does it differ from blue/green deployment? [Basic]
140. How would you implement a canary deployment for a new ML model? [Intermediate]
141. What metrics would you monitor during a canary rollout? [Intermediate]
142. How do you decide whether to promote, roll back, or halt a canary deployment? [Intermediate]
143. What percentage of traffic would you route to a canary, and how would you ramp up? [Intermediate]
144. Explain shadow deployment (shadow mode) for ML systems. [Basic]
145. How would you evaluate a new ML model using shadow mode before full production release? [Intermediate]
146. How do you handle discrepancies in predictions between the shadow model and the live model? [Intermediate]
147. What infrastructure is needed to support shadow deployments? [Advanced]
148. Compare A/B testing, canary deployment, and shadow mode — when do you use each? [Intermediate]
149. How would you implement interleaving experiments for ranking models? [Advanced]
150. What is a holdout group, and how do you use it in ML experimentation? [Intermediate]
151. How do you handle network effects and interference in A/B tests? [Advanced]
152. What is a switchback experiment design, and when is it useful? [Advanced]

### 16.6 Scaling & Infrastructure

153. How would you scale an ML inference service to handle 10x traffic? [Intermediate]
154. What is horizontal vs vertical scaling in the context of ML deployments? [Basic]
155. What are common bottlenecks when scaling ML systems? [Intermediate]
156. How does batch inference differ from real-time inference at scale? [Intermediate]
157. Explain the importance of load balancing in ML model serving. [Basic]
158. What strategies can be used to load balance inference requests between multiple model servers? [Intermediate]
159. How would you ensure session consistency (sticky sessions) if required in ML serving? [Intermediate]
160. What load balancer technologies have you used (NGINX, AWS ELB/ALB, Kubernetes Services, Envoy)? [Intermediate]
161. How can caching improve the performance of an ML inference pipeline? [Intermediate]
162. What data or results would you consider caching in an ML system? [Intermediate]
163. What are cache invalidation strategies for model predictions? [Advanced]
164. Compare in-memory caching (Redis, Memcached) vs distributed cache solutions for ML. [Intermediate]
165. How do you handle auto-scaling for GPU-based inference workloads? [Advanced]
166. What is spot/preemptible instance usage for ML training and inference, and what are the risks? [Intermediate]
167. How do you handle model replication across multiple regions? [Advanced]
168. What is a content delivery network (CDN), and how can it be used in ML serving? [Intermediate]
169. How do you optimize network latency for global ML inference services? [Advanced]
170. What is resource isolation, and why is it important in multi-tenant ML systems? [Intermediate]
171. How would you design an inference system that can handle 1 million requests per second? [Expert]
172. What is the role of message queues (Kafka, RabbitMQ, SQS) in ML systems? [Intermediate]
173. How do you handle data parallelism vs model parallelism at serving time? [Advanced]
174. What is the difference between scale-up and scale-out strategies for ML workloads? [Basic]
175. How do you manage cost optimization for ML inference in the cloud? [Intermediate]

### 16.7 ML System Design

176. Design a real-time fraud detection system for an online payments company. [Advanced]
177. How do you handle imbalanced classes in a fraud detection system? [Intermediate]
178. What features would you engineer for real-time fraud detection? [Intermediate]
179. How would you ensure sub-100ms latency for fraud scoring at transaction time? [Advanced]
180. Design a movie recommendation system for a streaming platform like Netflix. [Advanced]
181. Compare collaborative filtering vs content-based approaches for recommendations. [Intermediate]
182. How do you handle the cold-start problem in recommendation systems? [Intermediate]
183. How would you scale a recommender to support hundreds of millions of users and items? [Advanced]
184. How do you prevent echo chambers and filter bubbles in recommendations? [Advanced]
185. How would you incorporate multi-modal data (text, images, reviews) into a recommender system? [Advanced]
186. Design the ranking system for a large-scale e-commerce search engine. [Advanced]
187. How do you represent queries and documents — classic IR vs embedding-based techniques? [Intermediate]
188. How would you evaluate a search ranking algorithm (NDCG, MAP, precision@k)? [Intermediate]
189. How do you gather labeled data for training a learning-to-rank model? [Intermediate]
190. How would you apply Learning-to-Rank (LTR) with gradient-boosted trees vs neural approaches? [Advanced]
191. How would you implement and serve real-time ranking at scale with low latency? [Advanced]
192. Design an ad click-through rate (CTR) prediction system at scale. [Advanced]
193. Design a real-time content moderation system for a social media platform. [Advanced]
194. Design an ML system for dynamic pricing (e.g., ride-sharing, e-commerce). [Advanced]
195. Design a document classification system that handles millions of documents per day. [Intermediate]
196. Design a spam detection system for email. How do you handle adversarial attacks? [Intermediate]
197. Design an ML-based anomaly detection system for server infrastructure monitoring. [Advanced]
198. Design a churn prediction system for a SaaS product. [Intermediate]
199. Design a credit scoring system. How do you ensure regulatory compliance? [Advanced]
200. Design a real-time bidding (RTB) system for programmatic advertising. [Expert]
201. How would you design a multi-armed bandit system for website optimization? [Advanced]
202. Design a news feed ranking system. How do you balance relevance, freshness, and diversity? [Advanced]
203. Design an ML system for autonomous vehicle perception. [Expert]
204. How would you design an ML pipeline that handles both structured and unstructured data? [Intermediate]
205. Design a recommendation system that must comply with GDPR privacy requirements. [Advanced]
206. How would you build an explainable fraud detection system for regulatory compliance? [Advanced]
207. Design a voice assistant's intent classification and routing system. [Advanced]
208. How would you leverage unsupervised learning or graph neural networks to detect coordinated fraud? [Expert]
209. Design a system to detect and prevent fake reviews at scale. [Advanced]
210. Design a real-time personalization engine for an e-commerce homepage. [Advanced]

### 16.8 Security, Privacy & Reliability

211. How would you secure your model serving endpoints? [Intermediate]
212. How do you ensure PII is protected when serving models? [Intermediate]
213. What is adversarial attack on ML models, and how do you defend against it in production? [Advanced]
214. How do you implement rate limiting and authentication for ML APIs? [Intermediate]
215. What is model extraction attack, and how do you prevent it? [Advanced]
216. How do you handle data encryption at rest and in transit for ML systems? [Intermediate]
217. What are the reliability patterns (circuit breaker, retry, fallback) for ML serving? [Intermediate]
218. How do you design for high availability in ML inference systems? [Advanced]
219. What is chaos engineering, and how would you apply it to ML infrastructure? [Advanced]
220. How do you handle partial failures in a multi-model pipeline? [Advanced]

---

## 17. Probabilistic & Bayesian ML

### 17.1 Bayesian Inference Fundamentals

221. What is Bayesian inference? How does it differ from frequentist inference? [Basic]
222. State Bayes' theorem and explain each component (prior, likelihood, posterior, evidence). [Basic]
223. What is the role of the prior in Bayesian inference? [Basic]
224. How does the choice of prior affect the posterior, especially with limited data? [Intermediate]
225. What is an uninformative (flat/diffuse) prior, and when would you use one? [Basic]
226. What is a weakly informative prior, and why are they often preferred? [Intermediate]
227. What are informative priors, and give an example of when you'd use them. [Intermediate]
228. What is a conjugate prior? Give three examples of conjugate prior-likelihood pairs. [Intermediate]
229. Why are conjugate priors mathematically convenient? What are their limitations? [Intermediate]
230. Explain the Beta-Binomial conjugate pair and derive the posterior. [Intermediate]
231. Explain the Normal-Normal conjugate pair for unknown mean with known variance. [Intermediate]
232. What is the Dirichlet-Multinomial conjugate pair, and where is it used? [Intermediate]
233. What is the evidence (marginal likelihood), and why is it often intractable? [Intermediate]
234. How does the posterior update with sequential data in Bayesian inference? [Intermediate]
235. What is the difference between the MAP (Maximum A Posteriori) estimate and the full posterior distribution? [Basic]
236. How does MAP relate to regularization in frequentist machine learning? [Intermediate]
237. When would you prefer a point estimate (MAP) vs the full posterior? [Intermediate]
238. What is the posterior predictive distribution, and how do you compute it? [Intermediate]
239. Explain the difference between epistemic and aleatoric uncertainty in a Bayesian framework. [Intermediate]
240. How does Bayesian inference naturally handle uncertainty quantification? [Intermediate]
241. What is Bayesian model comparison, and how does the Bayes factor work? [Advanced]
242. How do you compute the Bayes factor for model selection? [Advanced]
243. What is the Bayesian information criterion (BIC), and how does it approximate model evidence? [Intermediate]
244. How does the Bayesian approach handle overfitting differently from frequentist methods? [Intermediate]
245. What is Bayesian shrinkage, and how does it relate to the prior? [Intermediate]
246. Explain the concept of hierarchical Bayesian models with an example. [Advanced]
247. What is empirical Bayes, and how does it differ from full Bayesian inference? [Advanced]
248. What is the difference between parametric and non-parametric Bayesian methods? [Intermediate]
249. Give an example of a real-world problem where Bayesian inference is clearly superior to frequentist approaches. [Intermediate]
250. How does Bayesian inference handle small sample sizes compared to frequentist methods? [Basic]

### 17.2 MCMC Methods

251. What is Monte Carlo estimation? Why do we use sampling methods? [Basic]
252. What is Markov Chain Monte Carlo (MCMC)? Why do we need it? [Basic]
253. Explain the key properties a Markov chain must satisfy for MCMC to work (ergodicity, detailed balance). [Intermediate]
254. Describe the Metropolis-Hastings algorithm step by step. [Intermediate]
255. What is the acceptance probability in Metropolis-Hastings, and what does it control? [Intermediate]
256. How do you choose a proposal distribution in Metropolis-Hastings? [Intermediate]
257. What happens if the proposal distribution is too wide or too narrow in MH? [Intermediate]
258. What is the ideal acceptance rate for Metropolis-Hastings, and why? [Advanced]
259. What is Gibbs sampling, and how does it differ from Metropolis-Hastings? [Intermediate]
260. When is Gibbs sampling more efficient than general Metropolis-Hastings? [Intermediate]
261. What are the conditions required for Gibbs sampling to work (conditional distributions must be known)? [Intermediate]
262. Explain blocked Gibbs sampling and when it's used. [Advanced]
263. What is Hamiltonian Monte Carlo (HMC), and why was it developed? [Advanced]
264. Explain the leapfrog integrator in HMC. [Advanced]
265. What are the key hyperparameters of HMC (step size, number of leapfrog steps)? [Advanced]
266. What is the No-U-Turn Sampler (NUTS), and how does it improve on HMC? [Advanced]
267. Why is NUTS the default sampler in Stan and PyMC? [Advanced]
268. What is the burn-in (warm-up) period in MCMC sampling? [Basic]
269. How do you assess convergence of an MCMC chain? [Intermediate]
270. What is the Gelman-Rubin diagnostic (R-hat), and how do you interpret it? [Intermediate]
271. What are trace plots, and what do they tell you about MCMC convergence? [Basic]
272. What is effective sample size (ESS), and why does it matter? [Intermediate]
273. How do you diagnose and fix high autocorrelation in MCMC samples? [Intermediate]
274. What is thinning in MCMC, and is it always beneficial? [Intermediate]
275. What are the challenges of MCMC in high-dimensional parameter spaces? [Advanced]
276. How does the mixing time of an MCMC chain relate to the target distribution geometry? [Advanced]
277. What is Slice Sampling, and when is it useful? [Advanced]
278. Compare MCMC methods: Metropolis-Hastings, Gibbs, HMC, and NUTS — strengths and weaknesses. [Advanced]
279. What is parallel tempering, and how does it help with multi-modal distributions? [Expert]
280. How do you implement MCMC in practice using PyMC, Stan, or TensorFlow Probability? [Intermediate]
281. What is the difference between adaptive and non-adaptive MCMC? [Advanced]
282. How do you handle discrete parameters in MCMC? [Advanced]
283. What is Reversible Jump MCMC, and when is it needed? [Expert]
284. How do you estimate posterior summaries (mean, credible intervals) from MCMC samples? [Basic]
285. What is the difference between a credible interval and a confidence interval? [Basic]

### 17.3 Variational Inference

286. What is Variational Inference (VI), and how does it differ from MCMC? [Basic]
287. What is the Evidence Lower Bound (ELBO), and why is it important in VI? [Intermediate]
288. Derive the ELBO and show its relationship to KL divergence and log evidence. [Advanced]
289. What is the mean-field approximation in VI? What are its limitations? [Intermediate]
290. Why do we often assume factorized distributions in VI? [Intermediate]
291. What is coordinate ascent variational inference (CAVI)? [Advanced]
292. What is Stochastic Variational Inference (SVI), and how does it scale VI? [Advanced]
293. Explain the reparameterization trick and its importance in stochastic VI. [Advanced]
294. Compare the computational requirements and scalability of MCMC vs VI. [Intermediate]
295. When would you prefer VI over MCMC, and vice versa? [Intermediate]
296. What is amortized variational inference? How is it used in deep learning (VAEs)? [Advanced]
297. What is Black Box Variational Inference (BBVI)? [Advanced]
298. How do you evaluate the quality of variational approximations? [Advanced]
299. What is the KL divergence, and why do we minimize KL(q||p) rather than KL(p||q) in VI? [Advanced]
300. What are normalizing flows, and how do they improve variational approximations? [Expert]
301. What is the difference between forward and reverse KL divergence? What behaviors do they induce? [Advanced]
302. How does VI handle multi-modal posterior distributions? [Advanced]
303. What is Expectation Propagation (EP), and how does it relate to VI? [Expert]
304. Compare VI, MCMC, and Laplace approximation for posterior inference. [Advanced]
305. How would you implement VI using Pyro or TensorFlow Probability? [Intermediate]

### 17.4 Gaussian Processes

306. What is a Gaussian Process (GP), and how does it differ from a Gaussian distribution? [Basic]
307. Define a GP formally — what are the mean function and covariance function? [Intermediate]
308. What is the role of the kernel (covariance function) in a GP? [Intermediate]
309. Name and describe five common GP kernels (RBF, Matérn, periodic, linear, polynomial). [Intermediate]
310. How do you select or tune the hyperparameters of a GP kernel? [Intermediate]
311. What is marginal likelihood maximization for GP hyperparameter optimization? [Advanced]
312. What is the computational complexity of GP regression, and why is it O(n³)? [Intermediate]
313. How do you address the scalability limitations of GPs? [Advanced]
314. What are sparse GPs and inducing points? [Advanced]
315. Explain the Sparse Variational GP (SVGP) method. [Advanced]
316. How does GP classification differ from GP regression? [Intermediate]
317. How would you adapt GPs to model non-Gaussian likelihoods? [Advanced]
318. Compare GP uncertainty quantification to neural network uncertainty. [Intermediate]
319. What is Deep Kernel Learning — combining GPs with neural networks? [Expert]
320. What is a GP latent variable model (GPLVM)? [Expert]
321. How would you use GPs for time series forecasting? [Intermediate]
322. What is the predictive distribution of a GP, and what does it provide? [Intermediate]
323. Explain the connection between GPs and Bayesian linear regression. [Advanced]
324. What is the Matérn kernel family, and how does the smoothness parameter ν affect the GP? [Advanced]
325. How do you handle non-stationary patterns with GPs? [Advanced]

### 17.5 Bayesian Neural Networks

326. What is a Bayesian Neural Network (BNN), and how does it differ from a standard neural network? [Basic]
327. Why do we place distributions over weights instead of point estimates? [Intermediate]
328. Explain variational inference in the context of BNNs. [Intermediate]
329. What is the Bayes by Backprop algorithm? [Advanced]
330. What are the challenges of MCMC in BNNs, and what alternatives exist? [Advanced]
331. What is Stochastic Gradient Langevin Dynamics (SGLD) for BNNs? [Expert]
332. What is Stochastic Gradient Hamiltonian Monte Carlo (SGHMC)? [Expert]
333. How is epistemic vs aleatoric uncertainty quantified in BNNs? [Intermediate]
334. Compare Monte Carlo Dropout and deep ensembles to true Bayesian inference in NNs. [Advanced]
335. How does MC Dropout approximate Bayesian inference? [Intermediate]
336. When would you prefer a BNN over a standard neural network with dropout? [Intermediate]
337. What are the scalability challenges of BNNs for large datasets and architectures? [Advanced]
338. How would you implement a BNN using PyTorch or TensorFlow Probability? [Intermediate]
339. What is the cold posterior effect in BNNs? [Expert]
340. How do BNNs help with out-of-distribution detection? [Advanced]
341. What is the relationship between BNNs and neural network ensembles? [Advanced]
342. How do you evaluate the calibration of uncertainty estimates from BNNs? [Advanced]
343. What are the practical applications of BNNs in safety-critical domains? [Intermediate]
344. How do BNNs relate to PAC-Bayes bounds? [Expert]
345. What is the lottery ticket hypothesis, and how does it relate to Bayesian pruning? [Expert]

### 17.6 Bayesian Optimization

346. Describe the general workflow of Bayesian Optimization (BO). [Basic]
347. What is the surrogate model in Bayesian Optimization, and why is a GP commonly used? [Intermediate]
348. What is an acquisition function? Name and compare three common ones. [Intermediate]
349. Explain Expected Improvement (EI) and how it balances exploration and exploitation. [Intermediate]
350. What is Upper Confidence Bound (UCB) in the context of BO? [Intermediate]
351. What is Probability of Improvement (PI), and what are its limitations? [Intermediate]
352. How does the choice of kernel in the GP surrogate affect BO performance? [Advanced]
353. Why does Bayesian Optimization struggle in high-dimensional spaces? [Advanced]
354. What are solutions for high-dimensional Bayesian Optimization (random embeddings, trust regions, BOHB)? [Advanced]
355. How would you use BO for hyperparameter tuning of a deep learning model? [Intermediate]
356. Compare Bayesian Optimization with random search and grid search. [Basic]
357. What is Tree-structured Parzen Estimator (TPE) in Optuna/Hyperopt? [Intermediate]
358. How does BOHB (Bayesian Optimization with HyperBand) work? [Advanced]
359. What is multi-fidelity Bayesian Optimization? [Advanced]
360. How do you handle categorical and conditional hyperparameters in BO? [Advanced]
361. What is multi-objective Bayesian Optimization? [Expert]
362. Compare Optuna, Hyperopt, BoTorch, and Ax for Bayesian hyperparameter tuning. [Intermediate]
363. What is the knowledge gradient acquisition function? [Expert]
364. How do you handle noisy observations in Bayesian Optimization? [Advanced]
365. What is transfer learning in the context of Bayesian Optimization across tasks? [Expert]
366. How do you warm-start Bayesian Optimization with prior knowledge? [Advanced]
367. What are the limitations of Bayesian Optimization, and when should you use other methods? [Intermediate]
368. How would you combine Bayesian Optimization with neural architecture search (NAS)? [Expert]
369. What is Thompson Sampling in the context of Bayesian Optimization? [Intermediate]
370. Explain the exploration-exploitation tradeoff in BO and how different acquisition functions handle it. [Intermediate]

---

## 18. Reinforcement Learning

### 18.1 Foundations & MDPs

371. What is reinforcement learning, and how does it differ from supervised and unsupervised learning? [Basic]
372. Define the key components of an RL problem: agent, environment, state, action, reward. [Basic]
373. What is a Markov Decision Process (MDP)? Define it formally. [Basic]
374. What is the Markov property, and why is it important for RL? [Basic]
375. What is a state-value function V(s) and an action-value function Q(s,a)? [Basic]
376. State the Bellman equation for V(s) and explain its significance. [Intermediate]
377. State the Bellman optimality equation for Q*(s,a). [Intermediate]
378. What is a policy? Differentiate between deterministic and stochastic policies. [Basic]
379. What is the discount factor γ, and how does it affect learning? [Basic]
380. What happens when γ = 0 vs γ = 1? [Basic]
381. What is the difference between finite-horizon and infinite-horizon MDPs? [Intermediate]
382. What is a Partially Observable MDP (POMDP), and when does it arise? [Advanced]
383. What is the difference between episodic and continuing tasks in RL? [Basic]
384. How do you handle continuous state and action spaces in RL? [Intermediate]
385. What is the reward hypothesis in RL? [Basic]
386. What is reward shaping, and what are its risks? [Intermediate]
387. What is the credit assignment problem in RL? [Intermediate]
388. How does temporal difference (TD) learning address the credit assignment problem? [Intermediate]
389. What are the differences between Monte Carlo methods and TD learning? [Intermediate]
390. What is TD(0), TD(λ), and eligibility traces? [Advanced]

### 18.2 Value-Based Methods

391. What is Q-learning? Write the update rule and explain each component. [Basic]
392. Is Q-learning on-policy or off-policy? Why? [Basic]
393. What is SARSA? Write the update rule. [Basic]
394. How does SARSA differ from Q-learning? [Intermediate]
395. Give a scenario where you would prefer SARSA over Q-learning. [Intermediate]
396. What are the tradeoffs between on-policy and off-policy methods? [Intermediate]
397. What is the exploration-exploitation tradeoff in RL? [Basic]
398. How does ε-greedy exploration work? What are its limitations? [Basic]
399. What is the softmax (Boltzmann) exploration policy? [Intermediate]
400. What is UCB (Upper Confidence Bound) exploration in RL? [Intermediate]
401. What is Deep Q-Network (DQN)? What innovations made it work? [Intermediate]
402. Explain experience replay in DQN and why it's important. [Intermediate]
403. What is the target network in DQN, and why is it needed? [Intermediate]
404. What is Double DQN, and what problem does it solve? [Intermediate]
405. What is Dueling DQN architecture? [Advanced]
406. What is Prioritized Experience Replay? [Advanced]
407. What are the limitations of value-based methods for continuous action spaces? [Intermediate]
408. What is the deadly triad in RL (function approximation + bootstrapping + off-policy)? [Advanced]
409. How do you handle overestimation bias in Q-learning? [Intermediate]
410. What is n-step return, and how does it bridge MC and TD? [Intermediate]

### 18.3 Policy Gradient Methods

411. What are policy gradient methods, and how do they differ from value-based methods? [Basic]
412. State the policy gradient theorem. [Intermediate]
413. What is the REINFORCE algorithm? [Intermediate]
414. What is the high variance problem in vanilla policy gradients, and how do baselines help? [Intermediate]
415. What is a baseline in policy gradient methods, and why is the value function a good choice? [Intermediate]
416. What is the advantage function A(s,a), and how does it reduce variance? [Intermediate]
417. Explain Generalized Advantage Estimation (GAE). [Advanced]
418. What is the Actor-Critic architecture? [Intermediate]
419. How do Actor-Critic methods combine the strengths of policy gradient and value-based methods? [Intermediate]
420. What is A2C (Advantage Actor-Critic) vs A3C (Asynchronous Advantage Actor-Critic)? [Advanced]
421. What is Trust Region Policy Optimization (TRPO)? [Advanced]
422. What is Proximal Policy Optimization (PPO), and why is it widely used? [Intermediate]
423. How does the clipping mechanism in PPO work? [Advanced]
424. Why is PPO preferred over TRPO in practice? [Intermediate]
425. What is the entropy bonus in policy gradient methods, and why is it important? [Intermediate]
426. What is Soft Actor-Critic (SAC), and how does it incorporate entropy maximization? [Advanced]
427. Compare PPO, SAC, and TD3 for continuous control tasks. [Advanced]
428. What is the natural policy gradient, and how does it relate to Fisher information? [Expert]
429. What are deterministic policy gradient (DPG) methods? [Advanced]
430. What is DDPG (Deep Deterministic Policy Gradient)? [Advanced]

### 18.4 RLHF & LLM Connection

431. What is RLHF (Reinforcement Learning from Human Feedback)? [Basic]
432. Describe the three stages of RLHF: SFT, reward model training, and PPO fine-tuning. [Intermediate]
433. How is the reward model trained in RLHF? [Intermediate]
434. Why is PPO commonly used in RLHF for LLMs? [Intermediate]
435. What is the KL penalty in RLHF, and why is it important? [Advanced]
436. What are the challenges of scaling RLHF? [Advanced]
437. What is Constitutional AI (CAI), and how does it relate to RLHF? [Advanced]
438. What is Direct Preference Optimization (DPO), and how does it avoid explicit reward modeling? [Advanced]
439. Compare RLHF, DPO, and RLAIF approaches. [Advanced]
440. How are Large Language Models like GPT-4 and Claude trained using RL? [Intermediate]
441. What is the reward hacking problem in RLHF? [Advanced]
442. How do you evaluate RLHF-trained models vs base models? [Intermediate]
443. What is Rejection Sampling Fine-Tuning (RST), and how does it compare to PPO-based RLHF? [Expert]
444. What is the role of human annotators in RLHF, and how do you handle annotator disagreement? [Advanced]
445. How does RLHF affect model creativity vs safety? [Intermediate]

### 18.5 Multi-Armed Bandits

446. What is the multi-armed bandit (MAB) problem? [Basic]
447. How does the MAB problem relate to the full RL problem? [Intermediate]
448. Explain the ε-greedy strategy for bandits. [Basic]
449. What is the UCB1 algorithm for bandits? [Intermediate]
450. Explain Thompson Sampling for bandits. [Intermediate]
451. Compare ε-greedy, UCB, and Thompson Sampling — pros and cons. [Intermediate]
452. What is a contextual bandit, and how does it differ from a standard MAB? [Intermediate]
453. How are contextual bandits used in recommendation systems? [Intermediate]
454. What is the regret metric in bandit problems, and what is sublinear regret? [Intermediate]
455. What is the Gittins index, and why is it theoretically optimal for discounted bandits? [Expert]
456. How would you adapt bandit algorithms to non-stationary environments? [Advanced]
457. What is the EXP3 algorithm for adversarial bandits? [Advanced]
458. How are bandits used for online A/B testing and adaptive experimentation? [Intermediate]
459. What is the difference between stochastic and adversarial bandits? [Advanced]
460. How do you apply bandits to clinical trial design? [Advanced]

### 18.6 Model-Based vs Model-Free RL

461. What is model-based RL, and how does it differ from model-free RL? [Basic]
462. What are the advantages of model-based RL in terms of sample efficiency? [Intermediate]
463. What is Dyna-Q, and how does it combine model-based and model-free approaches? [Intermediate]
464. What are world models in RL, and how do they learn environment dynamics? [Advanced]
465. What is model predictive control (MPC) in the context of RL? [Advanced]
466. What are the challenges of model-based RL (model inaccuracy, compounding errors)? [Intermediate]
467. How do you handle model errors in model-based RL? [Advanced]
468. What is the MBPO (Model-Based Policy Optimization) algorithm? [Expert]
469. Compare model-free (DQN, PPO) vs model-based approaches for Atari games. [Advanced]
470. What is the Dreamer algorithm for model-based RL in latent space? [Expert]
471. How is AlphaGo an example of combining model-based planning with model-free learning? [Advanced]
472. What is Monte Carlo Tree Search (MCTS), and how does it relate to model-based RL? [Advanced]
473. What are the key differences between planning and learning in RL? [Intermediate]
474. How do you decide whether to use model-based or model-free RL for a given problem? [Intermediate]
475. What is sim-to-real transfer, and why is it important for robotics RL? [Advanced]

---

## 19. Responsible AI & Ethics

### 19.1 Fairness & Bias

476. What does "responsible AI" mean in a business or product context? [Basic]
477. What is algorithmic bias, and how can it affect ML models and their users? [Basic]
478. Name three sources of bias in ML systems (data, label, representation, measurement). [Basic]
479. How do you identify and measure bias in a dataset? [Intermediate]
480. What are the different definitions of fairness: demographic parity, equalized odds, calibration? [Intermediate]
481. Why can't you satisfy all fairness criteria simultaneously (impossibility theorem)? [Advanced]
482. What are fairness-aware machine learning techniques (pre-processing, in-processing, post-processing)? [Intermediate]
483. How would you ensure a model remains fair as data distribution shifts over time? [Advanced]
484. Give an example of a fairness trade-off (accuracy vs demographic parity) and how you would approach it. [Intermediate]
485. What is disparate impact, and how is it measured (80% rule)? [Intermediate]
486. How do you audit a model for bias before deployment? [Intermediate]
487. What tools exist for fairness auditing (Fairlearn, IBM AI Fairness 360, Google What-If Tool)? [Intermediate]
488. How can proxy variables introduce hidden bias into a model? [Intermediate]
489. What is representation bias, and how does it manifest in training data? [Intermediate]
490. How do you handle intersectional fairness (bias across multiple protected attributes)? [Advanced]
491. What is the role of causal inference in understanding and mitigating bias? [Advanced]
492. How do you communicate fairness metrics and limitations to non-technical stakeholders? [Intermediate]
493. What is algorithmic redlining, and how do you prevent it? [Advanced]
494. How do feedback loops amplify bias in deployed ML systems? [Advanced]
495. What is historical bias, and why can't simply removing protected attributes fix it? [Intermediate]

### 19.2 Explainability & Interpretability

496. What is the difference between explainability and interpretability in ML? [Basic]
497. Why is explainability important in high-stakes domains (healthcare, finance, criminal justice)? [Basic]
498. What is the explainability-accuracy tradeoff? Is it always real? [Intermediate]
499. Compare inherently interpretable models (linear, decision trees) vs post-hoc explanations. [Intermediate]
500. What is SHAP (SHapley Additive exPlanations), and how does it work? [Intermediate]
501. What is LIME (Local Interpretable Model-agnostic Explanations)? [Intermediate]
502. Compare SHAP vs LIME — strengths, weaknesses, and when to use each. [Intermediate]
503. What are attention weights in transformers, and are they reliable explanations? [Advanced]
504. What is counterfactual explanation in ML? [Advanced]
505. How do you provide real-time explanations for predictions in a serving system? [Advanced]
506. What is feature attribution, and how does it differ from feature importance? [Intermediate]
507. How do you explain a model's prediction to a non-technical end user? [Intermediate]
508. What are concept-based explanations (TCAV)? [Advanced]
509. How do you audit predictions in regulated industries (banking, insurance)? [Intermediate]
510. What is the right to explanation under GDPR? [Intermediate]
511. How do you validate that explanations are faithful to the model's actual reasoning? [Advanced]
512. What are the risks of misleading explanations? [Intermediate]

### 19.3 Privacy & Data Protection

513. What is differential privacy, and why is it important? [Basic]
514. Explain the epsilon (ε) parameter in differential privacy in simple terms. [Intermediate]
515. What are the trade-offs of using differential privacy in AI systems? [Intermediate]
516. How does the Laplace mechanism add noise for differential privacy? [Intermediate]
517. What is the Gaussian mechanism for differential privacy? [Advanced]
518. What is local vs global differential privacy? [Advanced]
519. Give a practical application of differential privacy in ML (e.g., Apple, Google, US Census). [Intermediate]
520. What challenges arise when implementing differential privacy in a real-world ML pipeline? [Advanced]
521. What is federated learning, and how does it differ from centralized training? [Basic]
522. What are the main privacy advantages of federated learning? [Intermediate]
523. What are the technical challenges of federated learning (statistical heterogeneity, communication costs, security)? [Intermediate]
524. How can federated learning be combined with differential privacy? [Advanced]
525. Provide a use case where federated learning is preferable (e.g., healthcare, mobile keyboards). [Intermediate]
526. What is Federated Averaging (FedAvg), and how does it work? [Intermediate]
527. What are the security threats to federated learning (model poisoning, inference attacks)? [Advanced]
528. What is secure multi-party computation (SMPC), and how does it relate to privacy-preserving ML? [Advanced]
529. What is homomorphic encryption, and can it be used for ML inference? [Advanced]
530. How do you handle the privacy-utility tradeoff in ML systems? [Intermediate]
531. What is data anonymization, and why is it insufficient for privacy in ML? [Intermediate]
532. How can membership inference attacks compromise model privacy? [Advanced]
533. What is model inversion attack, and how do you defend against it? [Advanced]

### 19.4 AI Regulation & Governance

534. What are the main objectives of the EU AI Act? [Basic]
535. How does the EU AI Act classify AI systems by risk (unacceptable, high, limited, minimal)? [Intermediate]
536. What specific requirements does the EU AI Act impose on providers of high-risk AI systems? [Intermediate]
537. What are the penalties for non-compliance with the EU AI Act? [Intermediate]
538. How does the EU AI Act impact development and deployment of AI models globally? [Intermediate]
539. What are the challenges of implementing the EU AI Act for global tech companies? [Advanced]
540. How does GDPR intersect with ML model development and deployment? [Intermediate]
541. What is the "right to be forgotten" in GDPR, and how does it affect ML models trained on personal data? [Advanced]
542. How do you implement machine unlearning to comply with data deletion requests? [Expert]
543. What is AI governance, and what does it look like in practice at an organization? [Intermediate]
544. What is a model card, and why is it important for transparency? [Intermediate]
545. What is a datasheet for datasets, and what information should it contain? [Intermediate]
546. How do you establish an AI ethics review board in an organization? [Intermediate]
547. What role should AI regulation play in promoting ethical AI development? [Intermediate]
548. How do you balance innovation with regulation in AI? [Intermediate]
549. What is the NIST AI Risk Management Framework? [Intermediate]
550. How do you conduct an algorithmic impact assessment before deployment? [Advanced]
551. What is red-teaming for AI systems, and why is it important? [Intermediate]
552. How do you document AI system limitations and failure modes? [Intermediate]

### 19.5 Environmental Impact & Sustainability

553. Why is training large language models considered environmentally costly? [Basic]
554. How much energy and CO2 does training a large model like GPT-3 or GPT-4 produce? [Intermediate]
555. What steps can companies take to mitigate the carbon footprint of model training? [Intermediate]
556. How does model efficiency relate to sustainability in AI research? [Intermediate]
557. What is the tradeoff between model performance and environmental impact? [Intermediate]
558. How does model distillation reduce the environmental cost of inference? [Intermediate]
559. What is the role of efficient architectures (MobileNet, EfficientNet) in reducing compute costs? [Intermediate]
560. How do hardware choices (TPUs vs GPUs, chip efficiency) affect the carbon footprint of training? [Intermediate]
561. What is carbon-aware computing, and how can it be applied to ML training? [Advanced]
562. How do you measure and report the carbon footprint of your ML experiments? [Intermediate]
563. What tools exist for tracking ML carbon emissions (CodeCarbon, ML CO2 Impact)? [Intermediate]
564. Should there be regulations on the energy consumption of AI training? Argue both sides. [Advanced]
565. How does the reuse of pre-trained models (transfer learning) reduce environmental impact? [Basic]
566. What is the environmental cost of inference at scale vs training? [Intermediate]
567. How do mixture-of-experts (MoE) architectures improve compute efficiency? [Advanced]
568. What is the role of sparsity and pruning in reducing the environmental footprint of AI? [Intermediate]

### 19.6 Societal Impact & Safety

569. What are the key risks of deploying biased AI systems in society? [Basic]
570. How do you mitigate the risk of AI perpetuating or amplifying societal inequalities? [Intermediate]
571. What is AI safety, and how does it differ from AI ethics? [Intermediate]
572. What are the risks of autonomous decision-making systems (self-driving cars, criminal sentencing)? [Intermediate]
573. How should responsibility be assigned when an AI system causes harm? [Intermediate]
574. What is the alignment problem in AI? [Advanced]
575. How does Goodhart's Law apply to ML systems ("When a measure becomes a target, it ceases to be a good measure")? [Intermediate]
576. What are deepfakes, and what are the ethical implications of generative AI? [Basic]
577. How do you prevent misuse of generative AI models? [Intermediate]
578. What is the dual-use dilemma in AI research? [Intermediate]
579. How do you balance open-sourcing AI models with safety concerns? [Advanced]
580. What is the impact of AI on employment, and how should society prepare? [Intermediate]
581. How do you ensure AI systems respect human autonomy and dignity? [Intermediate]
582. What is value alignment in the context of LLMs? [Advanced]
583. How do guardrails and content filters work in production LLM systems? [Intermediate]
584. What is the role of human-in-the-loop systems in responsible AI? [Intermediate]
585. How do you handle the tension between AI personalization and manipulation? [Advanced]
586. What are the ethical considerations of using AI in healthcare diagnosis? [Intermediate]
587. What is the Asilomar AI Principles document, and what are its key points? [Intermediate]
588. How do you build a culture of responsible AI within an engineering organization? [Intermediate]
589. What lessons can we learn from past AI failures (Amazon hiring tool, COMPAS, Microsoft Tay)? [Intermediate]
590. How should AI companies approach transparency about model capabilities and limitations? [Intermediate]

---

## Appendix: Quick Reference

### Question Count Summary
| Category | Subcategory | Count |
|----------|------------|-------|
| 16. ML Systems & Production | 16.1 Model Serving & Inference | 30 |
| | 16.2 Model Deployment | 35 |
| | 16.3 MLOps & CI/CD for ML | 35 |
| | 16.4 Monitoring & Observability | 30 |
| | 16.5 A/B Testing, Canary & Shadow | 22 |
| | 16.6 Scaling & Infrastructure | 23 |
| | 16.7 ML System Design | 35 |
| | 16.8 Security, Privacy & Reliability | 10 |
| **16 Total** | | **220** |
| 17. Probabilistic & Bayesian ML | 17.1 Bayesian Inference Fundamentals | 30 |
| | 17.2 MCMC Methods | 35 |
| | 17.3 Variational Inference | 20 |
| | 17.4 Gaussian Processes | 20 |
| | 17.5 Bayesian Neural Networks | 20 |
| | 17.6 Bayesian Optimization | 25 |
| **17 Total** | | **150** |
| 18. Reinforcement Learning | 18.1 Foundations & MDPs | 20 |
| | 18.2 Value-Based Methods | 20 |
| | 18.3 Policy Gradient Methods | 20 |
| | 18.4 RLHF & LLM Connection | 15 |
| | 18.5 Multi-Armed Bandits | 15 |
| | 18.6 Model-Based vs Model-Free RL | 15 |
| **18 Total** | | **105** |
| 19. Responsible AI & Ethics | 19.1 Fairness & Bias | 20 |
| | 19.2 Explainability & Interpretability | 17 |
| | 19.3 Privacy & Data Protection | 21 |
| | 19.4 AI Regulation & Governance | 19 |
| | 19.5 Environmental Impact & Sustainability | 16 |
| | 19.6 Societal Impact & Safety | 22 |
| **19 Total** | | **115** |
| **Grand Total** | | **590** |

### Difficulty Distribution
| Difficulty | Count | Percentage |
|-----------|-------|-----------|
| Basic | ~80 | ~14% |
| Intermediate | ~310 | ~52% |
| Advanced | ~160 | ~27% |
| Expert | ~40 | ~7% |



---


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



---


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



---

