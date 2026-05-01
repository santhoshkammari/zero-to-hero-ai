# Section Review Guide — Apply to Every Section

When reviewing or rewriting any section HTML, apply these rules systematically.

---

## 🔇 Noise Reduction

### Kill These Patterns
- **"I used to think X, then I realized Y"** — use ONCE max per section for the opening hook. After that, get to the point.
- **Meta-commentary** — "Before we start...", "This isn't a short journey...", "If you're still with me..." — DELETE. The reader is here. Teach them.
- **Rest stops / recaps mid-section** — no "Congratulations on making it this far." No summarizing what was just said. No previewing what's coming next.
- **Wrap-up sections that just recap** — either add NEW insight in the closing or cut it to 1-2 sentences max.
- **History lessons** — "OOP has been around since the 1960s" — unless the history directly explains a design choice, cut it.
- **"I hope you'll be glad you came"** — no cheerleading. Let the content speak.

### Friendly Tone: Keep But Tighten
- One conversational opener is fine. One "I once spent an afternoon debugging X" anecdote per section is fine.
- After the hook, switch to **dense teaching mode**. Every paragraph must teach something new.
- Analogies (sealed envelope, kitchen) are GOOD — keep them. But one analogy per concept, stated once.

---

## 🐛 Code Bug Checklist

- [ ] All variables used in examples are defined or clearly imported
- [ ] Code would actually run if copy-pasted (no undefined `targets`, missing imports)
- [ ] Comments in code are accurate (especially `super()` MRO comments — verify the chain)
- [ ] Type hints are consistent within an example
- [ ] No mixing of Python 2 and Python 3 idioms

---

## 🕳️ Missing Topics Checklist (Python/OOP Specific)

These should be covered if the section claims comprehensive OOP coverage:

| Topic | Why it matters for ML |
|-------|----------------------|
| `@property` | `model.device`, `dataset.num_classes`, lazy attributes — used EVERYWHERE |
| `@classmethod` / `@staticmethod` | `from_pretrained()`, `from_config()` — must explain, not just mention |
| `__init_subclass__` | Modern registry pattern without metaclasses |
| `__slots__` | Memory optimization for millions of instances |
| `__iter__` / `__next__` | Custom data pipelines, streaming datasets |
| Dependency injection for testing | Compose + mock = testable code. Connect the dots. |
| Cooperative `super()` with `**kwargs` | How to actually WRITE correct multi-inheritance code |

Skip these (per general-approach.md rules):
- Custom metaclasses (nobody builds these)
- Decorator factories (tangential)
- `__new__` (edge case, not daily use)
- Enums (nice-to-know level, not main section)
- Descriptors (under-the-hood, mention once if at all)

---

## ✂️ Verbose → Dense Transformation

### Before (verbose)
> I used to think design patterns were an enterprise Java thing — abstract factories and visitor patterns and twenty classes to print "hello world." Then I started reading PyTorch and HuggingFace source code, and I realized I'd been using these patterns all along. I was living in the design patterns house without knowing the names of the rooms.

### After (dense, still has voice)
> Design patterns have a bad reputation from enterprise Java, but you're already using them — every `nn.Module` subclass is a Template Method, every optimizer you pass in is a Strategy. Let's name what you already know.

### The Rule
- If a paragraph can be reduced to 1 sentence without losing information → reduce it.
- If two paragraphs say the same thing in different ways → keep the better one.
- Every paragraph must pass the test: "What NEW thing does the reader learn here?"

---

## 📐 Structure Rules

1. **TOC "subtopics" count** must match actual H2 sections
2. **No duplicate TOC** — either use the `<nav class="section-toc">` OR the `<div class="callout-info">` TOC, not both
3. **Every code example must have context** — at minimum one sentence before saying what it demonstrates
4. **After complex code, explain the non-obvious** — don't explain the obvious (`self.lr = lr`), DO explain the tricky (`__setattr__` intercepting assignments)

---

## ✅ What to Preserve

- Analogies that make concepts click (sealed envelope, kitchen/recipe)
- "Mutable default" style gotcha callouts — real bugs people hit
- Comparison tables and decision rules ("use ABC when X, Protocol when Y")
- Code examples from real frameworks (sklearn, PyTorch, HuggingFace)
- The "20% inheritance, 80% composition" kind of practical ratios

---

## 🔄 Apply Order

1. Fix code bugs first
2. Cut noise (meta-commentary, recaps, history, cheerleading)
3. Add missing topics that belong
4. Verify structure (TOC counts, no duplicate TOCs)
5. Final read: every paragraph teaches something new?
