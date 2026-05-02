# framework.md — Universal Writer Agent Framework
# For producing "Final Boss" concept pages in Zero to Hero AI

> This framework takes ANY concept and produces an HTML page that leaves ZERO gaps.
> After reading it, the reader has no dependency on any other resource. Period.

---

## PHASE 0: RESEARCH (before writing a single word)

The writer agent MUST complete ALL research steps before writing begins.
This is non-negotiable. Writing without research = guaranteed gaps.

### Step 0A: Internet Reality Check

**Search the internet for ALL of the following:**

1. **FAANG interview questions** for this concept
   - "Google [concept] interview questions"
   - "Meta [concept] interview questions"
   - "Amazon [concept] interview questions"
   - "Apple [concept] interview questions"
   - "Microsoft [concept] interview questions"

2. **Top company engineering blogs** mentioning this concept
   - How Google/Meta/Netflix actually USE this concept in production
   - What patterns they chose and WHY

3. **Reddit r/cscareerquestions and r/experienceddevs** for this concept
   - "What [concept] questions did you get at [company]?"
   - "What do senior interviewers actually ask about [concept]?"

4. **Common misconceptions** about this concept
   - "Common [concept] mistakes"
   - "[concept] gotchas"
   - "[concept] myths"

**Output of Step 0A:** A raw list of:
- Every distinct question/topic found (deduplicated)
- Which company/source asked it
- Frequency (how many sources mention it)

### Step 0B: Build the Knowledge Graph

Using the internet research + domain knowledge, map the concept into clusters:

```
For concept X, identify:
├── CLUSTER: Core Foundations (what it IS, why it EXISTS)
├── CLUSTER: Mechanics (HOW it works under the hood)  
├── CLUSTER: Application (WHERE and WHEN to use it)
├── CLUSTER: Design & Architecture (how it fits in SYSTEMS)
└── CLUSTER: Edge Cases & Traps (what BREAKS and WHY)
```

For each cluster, list every sub-concept. Then for each sub-concept, tag it:

| Sub-concept | Priority | Reasoning |
|-------------|----------|-----------|
| ... | 🔴 MUST (90%+ interviews ask, used daily) | ... |
| ... | 🟡 IMPORTANT (senior interviews, used weekly) | ... |
| ... | 🟢 FANCY (rarely asked, rarely used) | ... |
| ... | ❌ SKIP (theoretical, not practical) | reason to skip |

**The rule:** Every 🔴 MUST concept gets full N1→N7 treatment. Every 🟡 IMPORTANT concept gets N1→N4→N6 (situation, fix, name — compressed). 🟢 FANCY concepts get a callout box ("if an interviewer asks..."). ❌ SKIP concepts are listed in a "what we deliberately left out" section at the end with one-line reasons.

### Step 0C: Gap Analysis

Cross-reference the research list from Step 0A against the knowledge graph from Step 0B.

```
For every question found in research:
  → Is it covered by a sub-concept in the graph?
  → If NO → add it to the graph or flag it
  
For every sub-concept in the graph:
  → Was it found in research?
  → If NO → either it's truly niche (tag 🟢/❌) or your graph is wrong
```

**No concept in the research list should be uncovered. No sub-concept in the graph should be ungrounded in reality.**

### Step 0D: Compile the Question Bank

From ALL research, create a structured question bank:

```
BASICS (what every developer should answer in 30 seconds):
  - Q: ...
  - Q: ...

INTERMEDIATE (what mid-level should answer with examples):
  - Q: ...
  - Q: ...

SENIOR (what separates senior from mid — needs deep understanding):
  - Q: ...
  - Q: ...

CRUSHER (the questions that make people freeze — needs tracing/debugging):  
  - Q: ...
  - Q: ...
```

This question bank is NOT included in the HTML directly — it's used to VERIFY that the written content answers every single one of these questions. After writing, run the check:

```
For each question in the bank:
  → Can a reader answer this from the HTML content alone?
  → If NO → the content has a gap → fix it
```

---

## PHASE 1: STRUCTURE

### The HTML Page Structure

```
OPENING
  Personal confession → orientation → heads-up → journey invitation
  (follow SYSTEM_PROMPT.md Phase 1 exactly)

TABLE OF CONTENTS
  Cluster names + sub-concept names, no numbering
  (follow SYSTEM_PROMPT.md Phase 2 exactly)

MOTIVATION SECTION
  The spaghetti/broken scenario that makes the reader FEEL why this concept matters
  This is the "before" — the world without this concept
  (N1: SITUATION for the entire topic)

CLUSTER B: [Core Foundations]
  Sub-concepts in N1→N7 chains
  Each chain's EDGE can point to any other cluster

CLUSTER C: [Mechanics / How It Works]
  Sub-concepts in N1→N7 chains

CLUSTER D: [Application / When & Where]
  Sub-concepts in N1→N7 chains

  ── REST STOP ──
  "You can stop here. You have [X]% of what you need."
  Summary of what they know. Preview of what's ahead.
  "But if a senior interviewer is going to sit across from you..."

CLUSTER E: [Design & Architecture]
  Sub-concepts in N1→N7 chains

THE MACHINERY (if applicable)
  Deep internals that explain the "magic" behind earlier clusters
  Sub-concepts in N1→N7 chains

ANTI-PATTERNS / TRAPS
  What breaks. Before/after refactoring code.

WRAP-UP
  Gratitude → journey recap → future hope
  (follow SYSTEM_PROMPT.md Phase 5 exactly)

WHAT WE LEFT OUT (AND WHY)
  Table of ❌ SKIP concepts with one-line reasoning each
  Reader knows what exists, knows why we skipped it, can look it up if needed
```

---

## PHASE 2: WRITING — The N1→N7 Engine

Every sub-concept follows this chain from WRITING_SOUL.md:

```
N1: SITUATION  — Drop the reader into a concrete scenario. They feel the itch.
N2: INSTINCT   — The naive/obvious approach anyone would try.
N3: BREAK      — ONE precise reason the instinct fails.
N4: FIX        — The minimal solution. Words first, then code as evidence.
N5: PROOF      — Concrete worked example with real values. Code block.
N6: NAME       — "By the way, this is called [X]." AFTER they've seen it work.
N7: EDGE       — The new limitation. Pulls into the next concept.
```

### Writing Rules (from SYSTEM_PROMPT.md + WRITING_SOUL.md)

**Voice:**
- First person singular for experience: "I got this wrong for two years."
- First person plural for journey: "Let's build this."
- Reader is companion, not student. Never test them.

**Structure:**
- Paragraphs: 2-5 sentences. Single-sentence paragraphs for punch.
- Code blocks: small, self-contained, ONE concept each. 5-25 lines.
- Bold/italic: ONLY for first introduction of a key term.
- No bullet-point explanations. Narrative prose only.
- Bullet lists ONLY for short enumerations (3-5 items max).

**Transitions:**
- NO "In this section we will..." 
- Organic: "With those gymnastics behind us..." / "The pain begins when..."
- Or motivation-driven: N7 of previous concept IS the transition

**Terminology:**
- Every term defined inline on first use. No exceptions.
- Use real terms: "This is called a descriptor" — don't avoid jargon.

**Vulnerability (distribute 4-5 across the page):**
- "I got this wrong for two years."
- "I'm still developing my intuition for..."
- "No one is completely certain why..."
- "...exposing the oversimplification I made when..."

**The Cut Rule:**
- Every sentence must be N1, N2, N3, N4, N5, N6, or N7.
- If it's none of those, cut it.

### Depth Calibration Per Priority

**🔴 MUST KNOW concepts** get the full treatment:
```
N1 → N2 → N3 → N4 → N5 (with code) → N6 → N7
   + Senior depth callout box (1-2 paragraphs)
   + "In interviews, they ask it like this: [real question from research]"
```

**🟡 IMPORTANT concepts** get compressed treatment:
```
N1 → N3 → N4 → N5 (with code) → N6
   + "Senior interviewers probe this by asking: [real question]"
```

**🟢 FANCY concepts** get a callout box:
```
<div class="callout-warning">
  <strong>If an interviewer asks about [X]:</strong> [2-3 sentence answer].
  The short version: [one-liner]. You rarely need this in practice because [reason].
</div>
```

---

## PHASE 3: VERIFICATION

After the full HTML is written, run these checks:

### Check 1: Question Bank Coverage
```
For EVERY question in the Phase 0D question bank:
  Read the HTML content.
  Can a reader answer this question using ONLY the HTML?
  
  If YES → ✅
  If NO  → ❌ GAP — add content to cover it
```

### Check 2: Internet Cross-Reference
```
For EVERY topic found in Phase 0A research:
  Is it addressed in the HTML?
  
  If YES → ✅  
  If NO and tagged 🔴/🟡 → ❌ GAP — must add
  If NO and tagged 🟢 → check if callout box exists
  If NO and tagged ❌ → check if "What We Left Out" mentions it
```

### Check 3: SYSTEM_PROMPT.md Checklist
Run the self-review checklist from SYSTEM_PROMPT.md:
- [ ] Opening has confession, orientation, heads-up, invitation
- [ ] TOC present
- [ ] Every concept: motivation → example → name → limitation
- [ ] At least one rest stop
- [ ] Running example threads throughout
- [ ] 4+ vulnerability moments
- [ ] Every term defined inline on first use
- [ ] No unexplained syntax/jargon
- [ ] 2+ recurring analogies
- [ ] No bullet-point explanations
- [ ] Wrap-up has gratitude, recap, future hope
- [ ] No "simply," "just," "obviously," "clearly," "of course"
- [ ] No "In this section we will..."
- [ ] Paragraphs 2-5 sentences
- [ ] Short sentences follow long ones for rhythm

### Check 4: Zero-Dependency Test
```
Imagine a reader who has:
  - Basic Python knowledge (variables, functions, loops, if/else)
  - No OOP knowledge whatsoever
  - Never read any other resource on this topic

After reading this page:
  - Can they pass a junior interview? → must be YES
  - Can they pass a mid-level interview? → must be YES
  - Can they hold their own in a senior interview? → must be YES for 🔴+🟡 questions
  - Do they know what they DON'T know? → must be YES (via "What We Left Out")
```

### Check 5: The "Crush Test"
```
Imagine a senior interviewer who:
  - Has 15 years of Python experience
  - Knows every CPython internals detail
  - Loves asking "why" three levels deep
  - Tests with broken code and asks "what's wrong?"

For each 🔴 MUST concept:
  - Does the page explain the WHY, not just the WHAT?
  - Is there enough depth to answer "why is it designed this way?"
  - Is there a gotcha/trap that demonstrates deep understanding?
  
For each 🟡 IMPORTANT concept:
  - Can the reader trace through the mechanism step by step?
  - Can they spot a subtle bug related to this concept?
```

---

## PHASE 4: HTML FORMATTING

Use the same HTML patterns as the existing site:

```html
<!-- Section headings -->
<h2>Section Title</h2>
<h3>Subsection Title</h3>

<!-- Prose -->
<p>Narrative text. <strong>Bold for first use of key terms.</strong> 
<code>inline_code()</code> for Python references. <em>Italic for emphasis.</em></p>

<!-- Code blocks -->
<pre><code class="language-python">
# Code here — small, self-contained, ONE concept
class Example:
    def method(self):
        return "evidence, not explanation"
</code></pre>

<!-- Warning/callout boxes -->
<div class="callout-warning">
  <strong>Title.</strong> Content of the callout.
</div>

<!-- Rest stops -->
<!-- Use a horizontal rule + distinct paragraph style -->
<hr>
<p><strong>Rest stop.</strong> If you've made it this far, you can stop. ...</p>
<hr>
```

---

## USAGE — How to Invoke This Framework

When creating a page for concept [X]:

```
1. Agent receives: "Write the [X] page using framework.md"

2. Agent executes Phase 0 (RESEARCH):
   - Searches internet for FAANG questions, StackOverflow, blogs
   - Builds knowledge graph with clusters
   - Tags priorities (🔴/🟡/🟢/❌)
   - Compiles question bank
   - Runs gap analysis

3. Agent executes Phase 1 (STRUCTURE):
   - Maps clusters to page sections
   - Plans N1→N7 chains for each sub-concept
   - Places rest stop(s)
   - Identifies running example

4. Agent executes Phase 2 (WRITING):
   - Writes full HTML following N1→N7 chains
   - Uses SYSTEM_PROMPT.md voice and WRITING_SOUL.md structure
   - Calibrates depth per priority tag

5. Agent executes Phase 3 (VERIFICATION):
   - Runs all 5 checks
   - Fixes gaps
   - Final output

6. Output: Complete HTML content section ready to insert into site template
```

---

## THE PROMISE

A page produced by this framework should satisfy this contract:

> "I read this one page. I didn't Google anything else. I didn't watch any YouTube video.
> I didn't read any StackOverflow answer. I walked into a senior interview and I held my ground.
> Not because I memorized answers — because I understood the WHY behind every concept,
> the HOW of every mechanism, and the WHEN of every design choice.
> I knew what I knew. I knew what I didn't know. And I knew why I chose to skip what I skipped."

That's the bar. Nothing less.
