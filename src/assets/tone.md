# tone.md — How Every Concept Gets Written

This file governs the voice, structure, and rules for writing any concept in this project.
Any agent writing content reads this first. No exceptions.

---

## The Core Principle

A concept must land in the reader's brain and stay there. Not as memorized words. As understanding.

The reader has ADHD. They will leave if you bore them. They will leave if you confuse them.
They will stay if you make them feel like they're discovering something genuinely interesting
alongside someone who finds it genuinely interesting.

After reading, the reader should be able to explain the concept in an interview — in their own words,
not yours. That means the concept has to live in their head as a mental model, not as a sentence
they memorized.

---

## The Structure — Situation → Fix → Click

Derived from Brandon Rohrer's teaching graph, but shorter and tighter.

### 1. SITUATION
Drop the reader into a scenario. Something concrete. Something small.
They're trying to do X. Something goes wrong or gets awkward.

- One paragraph max.
- No preamble. No "In this section we will..."
- The reader must feel the problem before you offer the solution.

### 2. INSTINCT (optional — only when it adds)
What would anyone naively try? Say it out loud. Respect it.
Don't poke holes yet.

### 3. BREAK
The precise reason the instinct fails. One thing. Specific. Not "it doesn't scale" —
show WHY it doesn't scale with something concrete.

### 4. FIX
The solution. Explain in words first. The mechanism. How it actually works.
Code comes AFTER, only if needed, only the minimum lines that demonstrate the fix.
Not a full implementation. Not multiple variations.

### 5. NAME (when applicable)
"That's called [X]." — AFTER the reader already understands what it is.
Never lead with the name. The name is a label on something already understood.

### 6. EDGE (optional)
What this fix still doesn't handle. The itch that pulls into the next concept.
One sentence. Don't solve it here.

---

## The Two Laws

### Law 1: Zero Dependencies

A concept explanation must not depend on understanding another concept that hasn't been
explained yet.

BAD: Using "SGD" and "Adam" to explain composition — now the reader needs to know
what SGD and Adam are. That's a dependency. That's a loop.

GOOD: Using "Printer" and "output destination" to explain composition — everyone knows
what printing is. Zero dependencies.

Every example must be self-contained. If explaining concept A, the example must use
things the reader already knows from everyday Python or everyday life. Not from ML.
Not from frameworks. Not from other sections they haven't read yet.

**Test:** Can someone who knows only Python syntax (variables, functions, classes, loops)
follow this explanation? If no — you introduced a dependency. Remove it.

### Law 2: No Mental Model Breaks

Once the reader is building a mental model, don't shatter it by introducing foreign terms.

BAD: Concept is clicking → suddenly "PyTorch Trainer receives an optimizer" → reader
doesn't know what PyTorch Trainer is → mental model collapses → curiosity dies.

GOOD: Concept clicks fully with the simple example → THEN, only if it genuinely helps,
a brief "you'll see this same shape in [production thing]" — but the concept already
stands without it.

Production mapping is NOT mandatory. It's a bonus. Only use it when:
- The concept is fully landed already
- The production reference doesn't introduce new unknowns
- It makes the reader go "oh, so THAT'S why that framework works that way"

If it breaks flow or requires explaining something new — skip it entirely.

---

## The Voice

### What It Sounds Like

Someone genuinely fascinated by the concept. Not performing enthusiasm. Actually interested.
Like a senior engineer who still finds this stuff cool after 15 years, explaining it because
they enjoy explaining it — not because they're being paid to teach.

Calm confidence. Not rushing. Not lecturing. Not trying to impress.

The reader should feel: "this person knows this deeply and is enjoying showing me why it works."

### What It Does NOT Sound Like

- ❌ Textbook: "Encapsulation is the bundling of data and methods that operate on that data."
- ❌ Bullet-point reference: "Encapsulation → bundle data + methods. Hide internals."
- ❌ Blog-bro: "Here's the thing about encapsulation that took me years to get..."
- ❌ Rushed magic words: "Inheritance locks you into a hierarchy. Composition flips this. Done."
- ❌ Teaching voice: "Let me explain why this matters..."
- ❌ Metaphor-heavy: "Think of a class like a blueprint and an object like a house..."

### What It DOES Sound Like

Concept flowing naturally. The reader builds understanding step by step because each
sentence earns the next one. No sentence is there for decoration. Every sentence either
sets up the problem, shows the failure, delivers the fix, or pulls forward.

Example of the voice done right (composition):

> You make a class `Printer` that prints to console. Tomorrow someone wants file output.
> You copy the whole class, change one line. Next week, database output. Another copy.
> Three classes, 95% identical.
>
> Fix: Printer doesn't decide where output goes. You hand it an output object.
> It calls `self.output.write(text)`. Console, file, database — Printer never changes.
> You swapped behavior without touching the class.
>
> That's composition. The class receives its parts from outside.

Notice: no metaphors, no "here's the thing," no prior knowledge needed, no rushed conclusions.
The concept builds, lands, gets named. Done.

---

## Code Rules

- **Minimum necessary.** Only the lines that demonstrate the concept. Not a full implementation.
- **No variations.** Don't show "and here's another way" or "you could also do..."
  One example. Clean. Done.
- **Self-contained.** The code uses plain Python. No imports from ML libraries to explain
  a general programming concept. No numpy, no torch, no sklearn — unless the concept
  IS about that specific library.
- **After prose, not before.** The concept is explained in words. Code confirms it.
  Code is evidence. Not explanation.
- **No boilerplate.** Don't show imports, don't show `if __name__ == "__main__"`,
  don't show anything the reader's brain has to skip over to find the point.

---

## What to Cut

If you can remove a sentence and the concept still lands — cut the sentence.

Specifically cut:
- Definitions at the start ("X is defined as...")
- History ("Introduced in 1994 by...")
- Multiple examples showing the same point (one is enough)
- Caveats and edge cases mid-explanation (save for later or skip)
- Summaries of what was just said ("So in summary, we learned that...")
- Transitions ("Now let's move on to...")
- Meta-commentary ("This is important because...")
- Any sentence that exists for completeness, not for understanding

---

## Depth Rules

Not everything gets the same treatment.

| Concept type | Treatment |
|---|---|
| Core "why" concept (needs intuition) | Full SITUATION → FIX → NAME flow. Take the space it needs. |
| Decision point (X vs Y) | Short comparison. When to use which. Maybe a table. |
| Common knowledge (reader already knows) | One line. Maybe two. Move on. |
| Gotcha/trap (things that bite) | State the trap. State the fix. That's it. |
| Nobody cares / will never use | Don't write it. Silence is content. |

The depth follows real-world value, not completeness.
A concept that trips people up in every interview gets more space than a concept
that's technically part of the topic but never comes up.

---

## The Enthusiasm Rule

The writing should feel like genuine curiosity. Not performed. Not forced.

This comes through in:
- Picking examples that are actually interesting (not "class Animal, class Dog")
- Noticing surprising things ("Notice how one change removed the need for three classes entirely")
- The natural rhythm of discovery — problem, attempt, failure, insight, resolution

If a concept is genuinely boring and mechanical — keep it short. Don't fake enthusiasm.
Say what needs saying and move forward. Enthusiasm is for concepts where there's something
genuinely elegant or surprising to notice.

---

## The Interview Test

After reading any concept section, the reader should be able to:

1. Explain the concept in a conversation (not recite a definition)
2. Explain WHY it exists (what problem it solves)
3. Explain WHEN to use it vs alternatives
4. Spot it in code they haven't seen before
5. Answer the tricky "what happens if..." questions interviewers love

If a section doesn't achieve all five — it's not done.

---

## The Feeling Test

The reader's mind should feel RELAXED after reading. Not because it's easy —
because it's clear. Nothing left to wonder about. No "do I really get this?"
lingering in the back of their head. Just calm confidence.

That's the bar. If reading a section doesn't produce that feeling, rewrite it.

---

## Quick Decision Guide for Agents

Before writing any concept, answer:

1. What does the reader need to already know? (Must be: only Python syntax, or previously covered concepts)
2. What's the simplest scenario that makes this concept necessary?
3. Can I explain the fix without code? (Start there)
4. Does the name come after the concept is understood? (Must be yes)
5. Am I introducing any term that needs its own explanation? (Must be no)
6. Would I be genuinely interested explaining this to a smart friend? (Must be yes — or shorten)

---

## Never Do These

- ❌ Start with a definition
- ❌ Use domain-specific examples to explain general concepts
- ❌ Create circular dependencies (using concept B to explain concept A, when B isn't covered yet)
- ❌ List multiple failure modes (pick the ONE that hurts most)
- ❌ Show code before explaining in words
- ❌ Use metaphors as the primary teaching tool
- ❌ Rush to conclusions with magic words
- ❌ Write bullet-point reference material
- ❌ Force production examples when the concept doesn't need them
- ❌ Break mental flow with foreign terms
- ❌ Say "In this section we will..."
- ❌ Summarize what was just said
- ❌ Write for completeness instead of understanding

---

*This file is self-contained. Any agent can read this and produce content that matches.
The reader will feel the difference.*
