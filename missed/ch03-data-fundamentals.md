# Missing Topics: Ch03 Data Fundamentals

The missed directory is empty. Now I have all the information I need. Let me compile the comprehensive findings.

Here is my comprehensive analysis of missing topics from Chapter 3 "Data Fundamentals":

---

## Summary

After thorough analysis of all 8 sections in Chapter 3 and cross-referencing with the rest of the book (Ch9 CNNs covers image augmentation, Ch11 NLP covers text pipelines/tokenization/embeddings, Ch15 ML Systems covers data infrastructure/DVC/feature stores/data catalogs in production context), I identified **10 significant topic gaps** that belong in a "Data Fundamentals" chapter. These are topics that are either (a) completely absent from the entire book, (b) only briefly mentioned in "Nice to Know" but deserve full treatment in a data chapter, or (c) are data-preparation-specific concepts that don't naturally fit in the domain-specific chapters where related topics appear.

## Current Coverage Inventory

What Ch03 **already covers** (verified from HTML heading structure):

- **Data Exploration** (`data-exploration.html`): Anscombe, data types, file formats (Parquet), summary stats, distributions, missing data mechanisms, correlations, target variable analysis, automated profiling
- **Data Cleaning & FE** (`data-cleaning-feature-engineering.html`): Missing data handling, outliers, feature scaling, skewed distributions, categorical encoding, feature creation (ratios, datetime, aggregation, binning), data leakage
- **Feature Selection & Splitting** (`feature-selection-data-splitting.html`): Variance threshold, correlation, mutual info, wrapper/embedded methods, L1/Lasso, train/val/test, stratified/time-based/group-based splits, cross-validation
- **Preprocessing Pipelines** (`preprocessing-pipelines.html`): Pipeline assembly, ColumnTransformer, custom transformers, leakage trap, hyperparameter tuning, serialization, brief feature stores mention
- **Data Quality & Preparation** (`data-quality-preparation.html`): Labeling problem, annotation guidelines, annotator agreement, weak supervision, active learning, finding bad labels, data augmentation (image + mixing + text), TTA, data validation (Great Expectations-style), drift detection, data contracts
- **Nice to Know** (`nice-to-know.html`): Data leakage, imbalanced datasets, DVC (brief), feature stores (brief), synthetic data (brief), tabular augmentation, Delta Lake/Lakehouse, privacy regs, differential privacy, data catalogs/contracts
- **Handling Imbalanced Datasets** (`handling-imbalanced-datasets.html`): Sampling techniques (random, stratified, systematic, reservoir, importance), SMOTE, ADASYN, combining approaches
- **Time Series Preprocessing** (`time-series-preprocessing.html`): Also contains Privacy & Compliance section (GDPR/CCPA/HIPAA, anonymization, differential privacy, federated learning data aspects, synthetic data for privacy, data governance)

**What other chapters cover (to avoid overlap):**
- Ch9 (CNNs): `image-augmentation.html` — image-specific augmentation techniques
- Ch11 (NLP): `text-pipeline-from-raw-text-to-features.html`, `embeddings-tokenization.html` — text preprocessing, tokenization, embeddings
- Ch15 (ML Systems): `data-infrastructure.html` — lakes/warehouses/lakehouses, batch/streaming pipelines, orchestration, feature stores in production, data versioning (DVC/lakeFS), labeling at scale, data validation, data catalogs, privacy. Also `mlops.html` — feature stores in production, CI/CD for ML, continuous training

## Identified Missing Topics

### 1. Text Data Preprocessing (Data Chapter Perspective)

**Why it's missing here specifically**: Ch11 NLP covers text pipelines from an NLP perspective, but Ch03 should establish the *data preparation fundamentals* for text — the same way it covers numerical/categorical preprocessing. A data engineer encountering text columns needs to know basic text cleaning before the NLP chapter.

**Key concepts that belong in Ch03**:
- Basic text cleaning: lowercasing, punctuation removal, HTML stripping, regex normalization
- Tokenization as a data preparation concept (word, subword, character-level)
- Stopword removal and stemming/lemmatization as data reduction
- Bag-of-words, TF-IDF as feature engineering from text (Spark MLlib covers these as feature extractors: `spark.apache.org/docs/latest/ml-features.html`)
- When to use text as a feature column vs. when to use dedicated NLP models
- The concept of vocabulary construction from training data only (local vs. global preprocessing, per MadeWithML: "constructs are learned only from the training split")

**Common interview questions** (sourced from khangich/machine-learning-interview study guide and Stanford CS 329S):
- "How would you handle a dataset with a mix of numerical and free-text columns?"
- "Why must you build your vocabulary only on the training set?"
- "When would you use TF-IDF vs. embeddings for feature engineering?"

**Citation**: `madewithml.com/courses/mlops/preprocessing/` — "Certain preprocessing steps are global (don't depend on our dataset, ex. lower casing text, removing stop words, etc.) and others are local (constructs are learned only from the training split)"

---

### 2. Image Data Preprocessing (Data Chapter Perspective)

**Why it matters**: Ch9 covers image augmentation for CNNs, but Ch03 should cover the *data preparation* fundamentals: how to load, resize, normalize, and prepare image datasets. This is analogous to how Ch03 covers numerical data prep before Ch5 covers supervised learning.

**Key concepts**:
- Image loading and format considerations (JPEG compression artifacts, PNG vs JPEG, DICOM for medical)
- Resizing strategies (interpolation methods: bilinear, bicubic, nearest neighbor)
- Pixel normalization (0-1 scaling, ImageNet mean/std normalization, per-channel stats)
- Color space considerations (RGB, BGR, grayscale, HSV)
- Channel ordering (channels-first vs channels-last)
- Image dataset organization (folder structure, manifest files, lazy loading)
- Basic quality checks: corrupt images, resolution distribution, aspect ratio analysis

**Common interview questions**:
- "Why do we normalize images to ImageNet mean and standard deviation?"
- "What happens if you resize all images to a square but your data has varying aspect ratios?"
- "How would you handle a dataset where 5% of images are corrupted?"

---

### 3. Audio & Signal Data Preprocessing

**Why it matters**: Audio ML is growing rapidly (speech recognition, music classification, environmental sound detection). The book has no coverage of audio data preparation anywhere.

**Key concepts**:
- Audio loading: sample rates, bit depth, mono vs stereo
- Time-domain features: amplitude envelope, zero-crossing rate, RMS energy
- Frequency-domain features: spectrograms, mel-spectrograms, MFCCs
- Preprocessing steps: resampling, noise reduction, silence trimming, normalization
- Windowing and framing (overlap, window functions)
- Audio augmentation: time stretching, pitch shifting, noise injection, SpecAugment

**Common interview questions**:
- "What are MFCCs and why are they useful for speech recognition?"
- "Why do we use mel-scale spectrograms instead of linear-scale?"
- "How would you preprocess audio data for a classification model?"

---

### 4. Automated Feature Engineering

**Why it matters**: The chapter covers manual feature engineering (ratios, datetime, aggregation) but doesn't cover automated approaches — a major topic in Kaggle competitions and industry (per Pedro Domingos: "One of the holy grails of machine learning is to automate more and more of the feature engineering process" — cited in `github.com/alteryx/featuretools README`).

**Key concepts**:
- **Deep Feature Synthesis (DFS)**: Featuretools' core algorithm that automatically generates features from relational datasets by stacking transformation and aggregation primitives across entity relationships
- **Entity sets and relationships**: Modeling multi-table data for automated feature generation
- **Primitive operations**: Transform primitives (applied to single column) vs aggregation primitives (applied across related tables)
- **Feature explosion problem**: Generating thousands of features → need feature selection afterward
- **AutoML feature engineering**: How AutoML tools (H2O, AutoGluon) handle feature creation
- **Target encoding automation**: Auto-detection and encoding of high-cardinality categoricals

**Common interview questions**:
- "How does deep feature synthesis work in Featuretools?"
- "When would automated feature engineering outperform manual feature engineering?"
- "How do you prevent data leakage when using automated feature engineering?"

**Citation**: Featuretools README (`github.com/alteryx/featuretools`) shows DFS example creating features across customer-transaction-session entity relationships automatically.

---

### 5. Embedding-Based Features for Tabular Data

**Why it matters**: Ch11 covers embeddings for NLP, but using embeddings as features for *tabular* data is a distinct data preparation technique increasingly used in production (entity embeddings for categorical variables, pretrained embeddings as features).

**Key concepts**:
- **Entity embeddings for categoricals**: Learning dense vector representations for high-cardinality categorical features (the Kaggle Rossmann competition technique)
- **Pretrained embeddings as features**: Using Word2Vec/FastText/BERT embeddings of text fields as numerical features in tabular models
- **Geographic embeddings**: Hex2Vec, location embeddings for lat/lon data
- **Graph-based embeddings**: Node2Vec, DeepWalk for network-structured data
- **Embedding dimension selection**: Rules of thumb (min(50, cardinality/2))
- **When embeddings beat one-hot**: High-cardinality categoricals, semantic relationships

**Common interview questions**:
- "How would you handle a categorical feature with 100,000 unique values?"
- "What are entity embeddings and when would you use them instead of one-hot encoding?"
- "How can pretrained language model embeddings be used as features for tabular prediction?"

---

### 6. Data Versioning & Lineage (Practitioner Depth)

**Why it matters**: Ch03's "Nice to Know" briefly mentions DVC, and Ch15's data-infrastructure covers it from a production perspective. But for a "Data Fundamentals" chapter aimed at practitioners, there's no hands-on coverage of how to version datasets during the exploration/experimentation phase. This is a commonly asked topic in MLE interviews.

**Key concepts**:
- **DVC (Data Version Control)**: Git-like commands for data (`dvc add`, `dvc push`, `dvc pull`), `.dvc` files as pointers, remote storage backends (S3, GCS, Azure). Per `dvc.org/doc`, DVC provides data warehouse capabilities for ML.
- **lakeFS**: Git-like branching for data lakes, zero-copy branching
- **Data lineage**: Tracking where each feature came from (raw data → transformations → final feature)
- **Reproducibility**: Pinning exact dataset versions to experiment runs
- **Dataset snapshots vs. incremental updates**: Tradeoffs in storage and auditability
- **Metadata tracking**: Schema evolution, column statistics over time

**Common interview questions**:
- "How would you ensure reproducibility of ML experiments when the training data changes frequently?"
- "What's the difference between DVC and Git LFS?"
- "How do you track data lineage in a feature engineering pipeline?"

---

### 7. Synthetic Data Generation (Beyond SMOTE)

**Why it matters**: The chapter covers SMOTE/ADASYN for class imbalance and briefly mentions synthetic data in "Nice to Know." But synthetic data generation is a much broader topic — it's used for privacy, testing, augmentation, and addressing data scarcity. This is a rapidly growing area in industry.

**Key concepts**:
- **Tabular data synthesis**: CTGAN, TVAE, Gaussian Copulas for generating realistic tabular data
- **SDV (Synthetic Data Vault)**: Library for multi-table synthetic data generation
- **Privacy-preserving synthetic data**: Generating data that preserves statistical properties without exposing individual records
- **Evaluation metrics for synthetic data**: Statistical similarity, ML utility (train-on-synthetic-test-on-real), privacy metrics (nearest-neighbor distance)
- **Conditional generation**: Generating data that meets specific constraints
- **Few-shot data generation**: Using LLMs to generate labeled training examples
- **Simulation-based data**: Domain-specific simulators (robotics, autonomous driving, finance)

**Common interview questions**:
- "How would you evaluate the quality of synthetically generated data?"
- "When is synthetic data better than collecting more real data?"
- "What are the risks of training exclusively on synthetic data?"

---

### 8. Working with Large-Scale Data (Dask & Spark Basics)

**Why it matters**: The entire chapter assumes data fits in pandas DataFrames in memory. Ch15 covers data infrastructure from a systems perspective, but doesn't teach the *practitioner skills* of working with data that doesn't fit in RAM — a fundamental data preparation skill asked in nearly every MLE interview.

**Key concepts**:
- **Chunked processing with pandas**: `pd.read_csv(chunksize=...)`, iterative aggregation
- **Dask DataFrames**: Drop-in pandas replacement for larger-than-memory data. Per `docs.dask.org`: "One Dask dataframe is simply a collection of pandas dataframes" — provides larger-than-memory execution, parallel execution, distributed computation
- **PySpark basics**: SparkSession, DataFrame API, transformations vs actions, lazy evaluation
- **Spark MLlib feature processing**: Tokenizer, StopWordsRemover, TF-IDF, StandardScaler, StringIndexer, VectorAssembler (per `spark.apache.org/docs/latest/ml-features.html`)
- **Partitioning strategies**: By date, by category, hash partitioning
- **Memory estimation**: Calculating DataFrame memory usage, dtype optimization
- **Polars**: Modern alternative to pandas with lazy evaluation and better performance
- **When to switch**: Rules of thumb (>1GB → Polars/Dask, >100GB → Spark)

**Common interview questions**:
- "Your dataset is 500GB. How do you perform EDA and feature engineering?"
- "What's the difference between Dask and Spark?"
- "How would you compute the median of a column across a distributed dataset?"
- "Explain lazy evaluation in the context of Dask or Spark."

**Citation**: `docs.dask.org/en/stable/` — Dask provides "Larger-than-memory execution for single machines" and "Distributed computation for terabyte-sized datasets"

---

### 9. Data Documentation (Datasheets & Data Cards)

**Why it matters**: Datasheets for Datasets (Gebru et al., 2021, published CACM) is a foundational concept in responsible AI that directly relates to data preparation. The chapter covers data contracts and validation but not structured documentation practices. This is increasingly asked in industry interviews, especially at FAANG companies.

**Key concepts**:
- **Datasheets for Datasets**: Standardized documentation covering motivation, composition, collection process, preprocessing, uses, distribution, maintenance (per `arxiv.org/abs/1803.09010`: "we propose that every dataset be accompanied with a datasheet that documents its motivation, composition, collection process, recommended uses")
- **Data Cards** (Google's PAIR framework): Per `pair.withgoogle.com/chapter/data-collection/` — documenting data decisions including features, labels, collection methodology
- **Dataset specification documents**: Writing requirements before collecting data
- **Nutrition labels for datasets**: Summarizing key statistics, biases, limitations
- **Data documentation tools**: Automatically generating dataset reports (pandas-profiling, ydata-profiling)

**Common interview questions**:
- "How would you document a dataset for a new ML project?"
- "What information should a datasheet for a dataset contain?"
- "How does data documentation help prevent bias in ML models?"

---

### 10. Experiment Tracking for Data Transformations

**Why it matters**: The chapter covers how to build preprocessing pipelines but not how to *track and log* the data transformation decisions and their impact on model performance. This is the bridge between data preparation and reproducible ML.

**Key concepts**:
- **Tracking data preprocessing choices**: Logging which imputation strategy, scaling method, or encoding was used for each experiment
- **MLflow / Weights & Biases / Neptune**: Logging data artifacts, transformation parameters, dataset metadata alongside model metrics
- **Data artifact versioning in experiments**: Linking specific dataset versions to experiment runs
- **Preprocessing hyperparameters**: Treating data preparation choices (e.g., outlier threshold, binning strategy) as hyperparameters to tune
- **Reproducibility checklist**: Random seeds, library versions, data snapshots, transformation order
- **Experiment comparison**: Comparing model performance across different preprocessing strategies

**Common interview questions** (per Stanford CS 329S syllabus, which includes lecture on "Experiment tracking & versioning with Weights & Biases"):
- "How do you ensure your ML experiments are reproducible?"
- "How would you track the impact of different preprocessing strategies on model performance?"
- "What artifacts should be logged for a complete experiment record?"

---

## Additional Minor Gaps Worth Noting

These are smaller topics that could be subsections rather than full sections:

11. **Geospatial data preprocessing**: Coordinate systems (WGS84, UTM), spatial indexing (H3, S2), haversine distance features, spatial joins — increasingly relevant for ride-sharing, logistics, real estate ML
12. **Graph/network data preprocessing**: Adjacency matrices, node feature extraction, graph sampling, ego-networks — relevant for social networks, fraud detection, recommendation systems
13. **Multi-modal data fusion**: Strategies for combining tabular + text + image features in a single pipeline
14. **Data collection strategies**: Active data collection, data flywheel, cold start problem — covered conceptually in Google PAIR guidebook but absent from the book
15. **Streaming data preprocessing**: Window functions, feature computation on streaming data, online statistics (Welford's algorithm for running mean/variance) — Ch15 covers streaming infrastructure but not the preprocessing specifics

## Sources Consulted

| Source | URL | What it Contributed |
|--------|-----|---------------------|
| Stanford CS 329S Syllabus | `stanford-cs329s.github.io/syllabus.html` | Training data, feature engineering, experiment tracking as course topics |
| MadeWithML Preprocessing | `madewithml.com/courses/mlops/preprocessing/` | Global vs local preprocessing, point-in-time joins |
| Chip Huyen's ML Interview Book | `huyenchip.com/ml-interviews-book/` | 200+ interview questions covering data topics |
| khangich ML Interview Guide | `github.com/khangich/machine-learning-interview` | MLE interview study plan, data topics |
| Featuretools README | `github.com/alteryx/featuretools` | Deep Feature Synthesis, automated FE |
| FeatureStore.org | `featurestore.org/what-is-a-feature-store` | Feature store concepts, train/serve skew |
| Datasheets for Datasets | `arxiv.org/abs/1803.09010` | Dataset documentation standard |
| Google PAIR Data Collection | `pair.withgoogle.com/chapter/data-collection/` | Data quality planning, data cascades, labeling |
| Dask Documentation | `docs.dask.org/en/stable/` | Larger-than-memory data processing |
| Spark MLlib Features | `spark.apache.org/docs/latest/ml-features.html` | Feature extractors/transformers at scale |
| DVC Documentation | `dvc.org/doc` | Data versioning tool capabilities |
| Huyenchip Data Distribution Shifts | `huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html` | Distribution shift taxonomy |
