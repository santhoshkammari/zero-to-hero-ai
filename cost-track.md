# Claude Opus 4.6 — Cost Tracker

```
┌─────────────────────────────────────────────────────┐
│                  ALL-TIME SUMMARY                   │
├──────────────────────┬──────────────────────────────┤
│  Tokens In (burned)  │  124.8M                      │
│  Tokens Out          │    4.27M                     │
│  Cached              │  102.5M                      │
│  Sessions            │  2                           │
├──────────────────────┼──────────────────────────────┤
│  TOTAL COST          │  ~ $269.59                   │
└──────────────────────┴──────────────────────────────┘
```

## Pricing Reference

| Type | Rate |
|------|------|
| Input | $5.00 / MTok |
| Cache Write (5min) | $6.25 / MTok |
| Cache Write (1hr) | $10.00 / MTok |
| Cache Hits & Refreshes | $0.50 / MTok |
| Output | $25.00 / MTok |

---

## Overview

| Metric | Value |
|--------|-------|
| Total Input Burned | 124.8M tokens |
| Total Output Received | 4.27M tokens |
| Total Cached | 102.5M tokens |
| **Total Cost** | **~$269.59** |

---

## Session Logs

### Session 1

`↑ 44.8M  ↓ 1.1M  cached 37.5M`

| Item | Tokens | Cost |
|------|--------|------|
| Input (non-cached) | 7.3M | $36.50 |
| Cache hits | 37.5M | $18.75 |
| Output | 1.1M | $27.50 |
| **Total** | | **$82.75** |

---

### Session 2 — 2026-05-02

`↑ 80M  ↓ 3.17M  cached 65M`

**Output breakdown (tiktoken cl100k_base):**

| Folder | Files | Tokens |
|--------|-------|--------|
| `chapters/` | 151 | 2,278,693 |
| `css/` | 1 | 4,897 |
| `js/` | 1 | 765 |
| `src/all_findings/` | 332 | 157,255 |
| `src/data/expanded/` | 4 | 56,730 |
| `src/data/questions/` | 7 | 111,920 |
| `src/data/research/` | 12 | 163,537 |
| `src/dont-know-where-to-keep/` | 19 | 222,154 |
| `src/DSA/` | 50 | 157,570 |
| `src/prompts/` | 7 | 20,033 |
| **Total** | **584** | **3,173,554 (~3.17M)** |

| Item | Tokens | Cost |
|------|--------|------|
| Input (non-cached) | 15M | $75.00 |
| Cache hits | 65M | $32.50 |
| Output | 3.174M | $79.34 |
| **Total** | | **$186.84** |

---

## Grand Total: $269.59
