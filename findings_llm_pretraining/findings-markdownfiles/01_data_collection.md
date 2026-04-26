# Data Collection & Curation for LLM Pretraining

## Key Datasets
- **Common Crawl**: Terabytes of web data in WARC format, monthly snapshots. Extremely noisy.
- **The Pile** (EleutherAI): 825GB, 22 subsets including Books3, OpenWebText2, Wikipedia, ArXiv, PubMed, Stack Exchange, GitHub, FreeLaw, USPTO, Ubuntu IRC, PhilPapers, HackerNews, Enron Emails, YouTube Subtitles, EuroParl, OpenSubtitles, DM Mathematics, Gutenberg, NIH ExPorter, Pile-CC
- **RedPajama** (Together): Open reproduction of LLaMA training data — CommonCrawl, Wikipedia, Books, ArXiv, Stack Exchange, PubMed, GitHub, C4
- **FineWeb** (HuggingFace, 2024): 15T tokens, aggressive quality filtering from Common Crawl
- **RefinedWeb** (Falcon team): Aggressive MinHash dedup + multi-layer filtering + human annotation loop

## Deduplication
- Near-duplicate: Shingling → MinHash → LSH → Jaccard similarity (threshold ~0.8)
- Exact duplicate: Hash full content
- Reduces data 30-50% while IMPROVING quality
- LLaMA: exact dedup at line level + fuzzy dedup with MinHash at document level

## Quality Filtering
- **Perplexity-based**: Train small LM (KenLM) on Wikipedia, score crawl docs. High perplexity = low quality (CCNet pipeline)
- **Heuristic rules**: Too short, too many special chars, low word-to-symbol ratio, repeated lines (RefinedWeb lists dozens)
- **Classifier-based**: fastText binary classifier trained on curated vs low-quality

## Data Mix (typical)
- Web crawl (filtered): 60-70%
- Code (GitHub): 5-15%
- Books: 5-10%
- Wikipedia: 3-5%
- Academic papers: 3-5%
- Conversational: 2-5%

Code data improves reasoning even on non-code tasks.
