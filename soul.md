# Soul

This is the writing soul of this project. Every piece of content must pass through this filter.

---

## Who is the reader?

Someone who *knows* the words — class, inheritance, tensor, gradient — but doesn't *feel* them. They've used `model.fit()` a hundred times but couldn't explain what happens inside. They're preparing for interviews and the real terror isn't "I don't know the answer" — it's "I know the answer but I don't trust my own understanding."

The goal is not to teach. The goal is to build the reader's confidence by making them *see the machine running* inside their own head.

---

## The method

**Start from nothing.** Not from a definition. Not from code. From a situation, a frustration, a tiny scenario that anyone can hold in their head. Then build — one small, inevitable step at a time — until the concept assembles itself in the reader's mind.

**Concepts first. Code is evidence, not explanation.** You explain to a person, not to a compiler. When you'd explain something in an interview or to a five-year-old, you don't open a code editor. You talk. You draw. You say "imagine..." The code comes *after* the idea clicks — to prove it, not to introduce it.

**Name things last.** Show the thing working. Let the reader feel it. *Then* say "by the way, this is called polymorphism." Brandon's move: the concept earns its name by being useful before being labeled.

**Each step motivates the next.** Don't introduce a concept because "it's next in the syllabus." Introduce it because the previous idea hit a wall. Limitation → need → solution → new limitation. The reader should feel *why* each concept exists, not just *what* it is.

**Arrive, don't announce.** Never say "the key insight is..." and hand it over. Walk the reader close enough that they reach it themselves. The "aha" belongs to them.

---

## What this is NOT

**Not verbose.** Every sentence must carry weight. If a paragraph can be a sentence, make it a sentence. If a sentence can be cut, cut it. Dense ≠ long. The enemy is filler — not depth.

**Not a blog post.** No "I was sitting in a coffee shop when..." No rambling personal stories. A *brief* vulnerability moment is fine ("I got this wrong for two years") — it normalizes struggle. But it earns one sentence, not a paragraph.

**Not high-level summaries.** "Inheritance is like a kitchen, composition is like Lego" — these sound clever but leave the reader exactly where they started. They nod, they move on, they can't answer the follow-up question. Go *inside the machine*. What actually happens when you call `super()`? What does Python do, step by step?

**Not bullet-point mapping.** "A maps to B, B maps to C" — this is a reference card, not understanding. Reference cards are for people who already understand. We're building understanding.

**Not code-first.** If the first thing the reader sees is a code block, something went wrong. The concept should already be taking shape before any code appears.

**Not everything.** Only what matters. Curate ruthlessly. If a concept doesn't show up in real interviews, real framework source code, or real production bugs — cut it. Covering less deeply beats covering more shallowly.

---

## The feel

- **Density of a good lecture, not a textbook.** Imagine a teacher at a whiteboard who *respects your time*. They don't repeat themselves. They don't pad. But they don't skip steps either.
- **Confidence through construction.** After reading a section, the reader should be able to reconstruct the concept from scratch — not because they memorized it, but because they watched it being built and understood each step.
- **Calm authority.** No hype. No "this is amazing!" No "simply do X." The tone is: I've been in the mud with this, here's what I found, and here's how it actually works.

---

## Checklist (before shipping any section)

1. Can I explain this concept to an interviewer *without* opening a code editor?
2. Does every step follow inevitably from the previous one?
3. Did I name the concept *after* demonstrating it?
4. Is there a single sentence I can cut without losing meaning? Cut it.
5. Would the reader's reaction be "oh, so THAT'S why" — not "okay, noted"?
