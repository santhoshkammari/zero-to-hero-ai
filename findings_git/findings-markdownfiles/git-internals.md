# Git Internals Research Findings

## Object Model (Content-Addressable Storage)
- Git is a content-addressable filesystem. Every piece of data is stored as an **object** identified by SHA-1 hash.
- Four object types: **blob** (file contents), **tree** (directory listing), **commit** (snapshot + metadata + parent pointers), **tag** (labeled pointer).
- Objects stored in `.git/objects/XX/YYYY...` (first 2 hex chars = directory, rest = filename), zlib compressed.
- Identical content → identical hash → stored only once (**deduplication**).

## DAG Structure
- Commits form a Directed Acyclic Graph (DAG). Each commit points backward to parent(s).
- Merge commits have multiple parents. No cycles possible.
- Branches, tags, HEAD are just refs—text files containing commit hashes.

## Three-Tree Architecture
- Working Directory (your actual files), Staging Area/Index (what's queued for next commit), Repository (.git).
- `git add` moves changes from working dir → index. `git commit` moves from index → repository.

## Refs and HEAD
- Branches = files in `.git/refs/heads/` containing a commit SHA.
- Tags = files in `.git/refs/tags/`. Lightweight (just pointer) vs annotated (full object).
- HEAD = `.git/HEAD` usually contains `ref: refs/heads/main` (symbolic ref) or a raw SHA (detached HEAD).

## Packfiles and Delta Compression
- Loose objects → packed into `.pack` files by `git gc`.
- Delta compression: similar objects stored as diffs against each other.
- Garbage collection prunes unreachable objects and repacks.

## Advanced Commands
- `git bisect`: binary search for bug-introducing commit.
- `git reflog`: safety net—records every HEAD movement, even after reset/rebase.
- `git cherry-pick`: apply specific commit(s) to current branch.
- `git rebase -i`: rewrite history—squash, reorder, reword commits.

## ML-Specific
- DVC: `.dvc` pointer files in git, actual data in remote storage (S3/GCS).
- DVC pipelines (`dvc.yaml`) for reproducible ML workflows.
- Git LFS: simpler alternative, transparent large file handling.
- `.gitignore` critical: data/, models/, *.pt, *.pkl, __pycache__/, .env, wandb/.

## Merge Strategies
- Fast-forward: linear history, no merge commit.
- Three-way merge: creates merge commit with two parents.
- Rebase: replay commits on top of target branch for linear history.
- Golden rule: never rebase shared/public branches.
