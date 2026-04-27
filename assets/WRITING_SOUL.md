# WRITING_SOUL.md
> The complete skeleton for writing any concept in this project.
> Source: Brandon Rohrer's transformer article + soul.md.
> Apply this graph to every concept, every section, every paragraph block.

---

## The Graph

```
N1: SITUATION
      ↓
N2: INSTINCT
      ↓
N3: BREAK
      ↓
N4: FIX
      ↓
N5: PROOF
      ↓
N6: NAME
      ↓
N7: EDGE ─────────────────────────────────────→ N1 of next concept
```

Visual: `assets/teaching-graph.svg`

---

## The 7 Nodes — What Each One Is and How to Write It

---

### N1 · SITUATION

**What it is:** One concrete scenario that creates a felt need. The reader must feel the itch before you offer the scratch.

**How to write it:**
- One paragraph, sometimes one sentence.
- No preamble. No "In this section we will explore..."
- Drop the reader into a situation: they're trying to do X, and something is missing or broken.
- The scenario must be small enough to hold in one's head.

**Brandon's move:** "Predicting the next word based on only the current word is hard. That's like predicting the rest of a tune after being given just the first note."

**soul.md alignment:** *"Start from nothing. Not from a definition. Not from code. From a situation, a frustration, a tiny scenario that anyone can hold in their head."*

**Cut:** Definitions. History. "In 1986, researcher X invented..." Background framing. Anything that could go in a Wikipedia intro.

---

### N2 · INSTINCT

**What it is:** The dumb solution anyone would try. You say it out loud — before the reader does.

**How to write it:**
- One short paragraph.
- Always framed as: "A naïve approach would be..." or "The obvious thing to try is..."
- Never dismiss it. Treat it with respect. The reader thought of it too.
- Don't poke holes yet. Just state it plainly.

**Why this node exists:** It respects the reader's intelligence. It also sets up N3 — the break only lands if the instinct was genuinely reasonable.

**Cut:** Caveats. Alternatives. "But of course there are many approaches..." — not yet.

---

### N3 · BREAK

**What it is:** One precise reason the instinct fails. One sentence. The reader feels the collapse, not just hears about it.

**How to write it:**
- One sentence, sometimes two.
- The failure must be specific, not vague. "This doesn't scale" is vague. "If you have 50,000 words, this matrix has 2.5 billion cells — most of them zero" is specific.
- Don't explain all the ways it fails. Pick the one that hurts most.

**Brandon's move:** "Not so with neural networks." (single sentence paragraph — the break lands like a punch)

**soul.md alignment:** *"Each step motivates the next."* The break IS the motivation.

**Cut:** Multiple failure modes. Nuance. Edge cases. If you're listing more than one reason the instinct fails, you're padding.

---

### N4 · FIX

**What it is:** The minimal solution. It fixes only this specific break. Not a general solution. Not elegant. Just enough.

**How to write it:**
- Explain the mechanism of the fix in words first. No code yet.
- Small. Precise. The fix is exactly as big as the break.
- If the fix introduces a new mechanism, explain it step by step, one sub-step at a time.
- Code, if any, comes at the END of the fix — as evidence, not explanation.

**The discipline:** Resist the urge to build the full solution here. The full solution will emerge across multiple N1→N7 cycles. Each fix only patches this one break.

**soul.md alignment:** *"Concepts first. Code is evidence, not explanation."*

**Cut:** Full generalization. "And this approach also handles the case where..." — that's N7 territory.

---

### N5 · PROOF

**What it is:** Image, diagram, or concrete worked example. Comes AFTER the fix is explained in words. Confirms — does not introduce.

**How to write it:**
- The reader's mental model is already forming. The image snaps it into place.
- Images must show the exact thing just described. Not a related thing. Not a more general thing.
- If using an SVG/diagram: label it minimally. Let the structure speak. Caption in one line.
- If using a worked example: walk through one concrete case with real values. Not "suppose we have variables a and b" — use "apple", "cat", "17".

**Brandon's move:** Text describes one-hot encoding → image shows it. Not the other way around.

**The rule:** If the image appeared before the prose, something went wrong.

**Cut:** Images that introduce concepts. Images that show more than what was just explained.

---

### N6 · NAME

**What it is:** The vocabulary word. It arrives here — after the reader has seen the thing working — as a label for something already understood.

**How to write it:**
- "By the way, this is called [X]."
- Or: "This structure has a name: [X]."
- One sentence. Then optionally one sentence connecting it to the wild (how it appears in papers/docs).
- You may also mention aliases: "You'll also see this called inner product, or scalar product."

**Why this works:** The name is a reward. The reader doesn't decode it — they recognize it. Recognition feels like mastery.

**Brandon's move:** "These are also known by other intimidating names like inner product and scalar product." (The word "intimidating" does emotional work — it says: you were right to be wary, now you're not.)

**soul.md alignment:** *"Name things last. Show the thing working. Let the reader feel it. Then say 'by the way, this is called polymorphism.'"*

**Cut:** Definitions that arrive before the concept. Dictionary-style vocab introductions at the start of sections.

---

### N7 · EDGE

**What it is:** The new limitation revealed by the fix. The forward pull into the next concept. The reader should feel "wait, but what about X?" — and then you confirm: yes, exactly, that's next.

**How to write it:**
- One short paragraph, sometimes one sentence.
- Name the limitation. Don't solve it. Just name it.
- Optional: a rhetorical question. "What happens when we need to look back further than one word?"
- Then move. No announcement. No "In the next section, we will cover..."

**Why this node is load-bearing:** Without N7, you're assembling a syllabus. With N7, you're building an argument. The reader follows because each concept reveals why the next one exists.

**soul.md alignment:** *"Each step motivates the next. Limitation → need → solution → new limitation."*

**Cut:** Summaries of what was just covered. "In this section, we learned that..." — this is the enemy.

---

## The Three Emotional Moves (layered underneath the 7 nodes)

These run in the background across the whole piece. They are not nodes — they are tone.

### 1. Earned Vulnerability
One sentence admitting you struggled with this. Max one sentence. Then deliver.

> "I got this wrong for two years."
> "I procrastinated on transformers for a few years. Finally the discomfort of not knowing grew too great."

**Never:** a paragraph of struggle. One sentence. Then move.

### 2. Permission to Stop
At the midpoint of a long piece, tell the reader they can leave. This makes continuing feel chosen, not forced.

> "You can stop here if you want. What follows gets harder."

The reader who stays after this is invested. Their attention is a decision, not inertia.

### 3. "Notice that..."
Never say "the key insight is." Never hand over the insight.
Say "notice that" — and let the reader arrive.

> "Notice how the dot product acts as a similarity score here."

The insight belongs to the reader. This is not a stylistic preference — it's the mechanism that produces the "aha."

---

## The Cut Rule

> If you can remove it without breaking the chain from N1 to N7, cut it.

Every sentence must be load-bearing. Run this test on every paragraph:
- Does it set up a need? (N1/N2)
- Does it create or resolve a failure? (N3/N4)
- Does it confirm something just explained? (N5)
- Does it name something just demonstrated? (N6)
- Does it pull forward? (N7)

If the answer is none of the above, cut it.

---

## What This Skeleton Is NOT

- Not a template to fill in mechanically. The nodes flow. N2 and N3 sometimes merge. N5 is sometimes a worked example in prose, not an image.
- Not a guarantee that every concept needs all 7 nodes. Short concepts may run N1→N3→N4→N6. Long concepts may cycle N1→N7 multiple times before resolving.
- Not a substitute for knowing the concept deeply. The skeleton only works if you understand the material well enough to know what the real break is, what the minimal fix is, and what the edge reveals.

---

## Applying This to Any Concept — The Checklist

Before writing:
1. What is the situation — the one scenario that makes the reader feel the need?
2. What would anyone naively try?
3. What is the ONE precise way that fails?
4. What is the minimal fix — only big enough to patch that one break?
5. What image or example confirms it?
6. What is the name — and when exactly do I say it?
7. What does this fix still not handle — and is that the next concept?

Before shipping:
1. Can every paragraph be assigned to one of N1–N7?
2. Is there a single sentence I can cut without losing the chain? Cut it.
3. Does the name appear before the concept is demonstrated? Move it to N6.
4. Does any image appear before its concept is explained in prose? Move it after.
5. Would the reader's reaction be "oh, so THAT'S why" — not "okay, noted"?

---

## Quick Reference Card

| Node | One-line job | Brandon's signal phrase | Cut if... |
|------|-------------|------------------------|-----------|
| N1 SITUATION | Create the itch | *(just drops you in)* | you start with a definition |
| N2 INSTINCT | Say the naive thing | "A naïve approach..." | you skip straight to the fix |
| N3 BREAK | Show it failing, precisely | "Not so with..." | you list multiple failures |
| N4 FIX | Minimal patch only | *(mechanism in words)* | you generalize too early |
| N5 PROOF | Confirm with image/example | *(image appears here)* | image comes before prose |
| N6 NAME | Attach the label | "By the way, this is called..." | name appears at N1 |
| N7 EDGE | Reveal the next itch | "What about when...?" | you summarize instead |
