# Web Search Insights Summary

## Key Insights Gathered

1. **Content-addressable storage** is the foundational concept - everything in Git is identified by SHA-1 of its content. This enables deduplication automatically.

2. **The DAG structure** - commits point backward to parents only (no cycles). This is what makes Git's history model work. Merge commits have multiple parents.

3. **Refs are just text files** - a branch is literally a 41-byte file containing a SHA hash. This demystifies branching entirely.

4. **Three-tree architecture** - working dir, index/staging, repository. Understanding this explains why `git add` exists separately from `git commit`.

5. **Packfiles with delta compression** - Git's efficiency comes from packing similar objects together and storing deltas. `git gc` triggers this.

6. **DVC workflow for ML** - `dvc add` creates pointer files, actual data goes to remote storage. DVC pipelines (`dvc.yaml`) enable reproducible ML workflows.

7. **Merge strategies** - fast-forward (linear), three-way merge (merge commit), rebase (replay). Golden rule: never rebase public branches.

8. **Recovery tools** - reflog records every HEAD movement (safety net), bisect does binary search for bugs, cherry-pick applies specific commits.

9. **Git LFS vs DVC** - LFS is simpler (transparent), DVC is more powerful (pipelines, experiments, metrics tracking).

10. **Loose objects vs packfiles** - objects start loose in `.git/objects/`, get packed by `git gc` for efficiency.
