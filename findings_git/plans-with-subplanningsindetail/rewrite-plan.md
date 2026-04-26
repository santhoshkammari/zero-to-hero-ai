# Rewrite Plan: Version Control with Git (ch01/s11.html)

## Problems with Current Section
- Too superficial—just a command cheat sheet
- No internals explanation (object model, DAG, three-tree architecture)
- No running example or narrative journey
- No Brandon Rohrer style (no personal confession, no vulnerability, no build-up)
- Listicle format for "When Things Go Wrong"
- Missing interview-depth content (reflog, bisect, merge strategies, packfiles)

## Rewrite Architecture

### Opening (Brandon style)
- Personal confession: avoided understanding Git internals, just memorized commands
- Orientation: what Git actually is (2005, Linus Torvalds, distributed VCS)
- Heads-up: no prior knowledge needed
- Journey invitation

### Table of Contents

### Build-Up Sections:
1. **The Snapshot, Not the Diff** — Git's mental model. Running example: ML project with model.py, data pipeline, config files.
2. **The Object Model** — blobs, trees, commits. Build from scratch with tiny example. Show `git cat-file`. Content-addressable storage, SHA-1 hashing, deduplication.
3. **The Three Trees** — working directory, staging area, repository. Why the staging area exists (selective commits).
4. **Refs: Where Branches Really Live** — branches are just files with SHA hashes. HEAD as a symbolic ref. Detached HEAD explained.
5. **The DAG** — commits form a directed acyclic graph. Merge commits. Why this matters.

### Rest Stop
- You now understand what Git actually does under the hood.

6. **Merge vs Rebase** — three-way merge, fast-forward, rebase. When to use each. The golden rule.
7. **When Everything Goes Wrong** — reflog as safety net, bisect for bug hunting, cherry-pick, interactive rebase. Narrative, not listicle.
8. **Git for ML Teams** — .gitignore, DVC, Git LFS, experiment tracking, commit messages that matter. The real divergence from regular software.
9. **Packfiles and Garbage Collection** — how Git stays efficient at scale.

### Wrap-Up
- Gratitude, journey recap, future hope

### Resources

## Style Notes
- Running example: small ML project (train.py, config.yaml, data/ folder)
- Analogies: Git as a photo album (snapshots not diffs), branches as sticky notes on photos
- Vulnerability moments: "I used git for 2 years without knowing what HEAD actually was", etc.
- No listicles for explanations, narrative prose throughout
- Interview-depth: cover what senior engineers would ask about
