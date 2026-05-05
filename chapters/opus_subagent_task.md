# Caveman Rewrite Task

## What To Do
Rewrite ALL prose text in the given HTML file using "caveman style" — keeping the same structure, same code blocks, same HTML tags.

## Caveman Style Rules (from caveman.md)
1. Drop articles (a, an, the), filler (just, really, basically, actually)
2. Drop pleasantries (sure, certainly, happy to)
3. No hedging. Fragments fine. Short synonyms.
4. Technical terms stay exact. Code blocks unchanged.
5. Pattern: [thing] [action] [reason]. [next step].

## What To Keep Unchanged
- ALL HTML structure, tags, classes, attributes
- ALL `<pre><code>` blocks (code examples) — don't touch these
- ALL navigation, sidebar, head, script sections
- Section headings (h2, h3) — can shorten slightly but keep meaning
- The TOC nav section — can shorten entries slightly

## What To Rewrite
- All `<p>` paragraph text — apply caveman style
- Keep technical accuracy, keep all concepts
- Keep all bold/code/em inline formatting
- This is interview prep + self-study material — keep substance, cut fluff

## Examples of Transformation

BEFORE:
"This is a common source of bugs. You slice an array, modify the slice thinking you have your own copy, and then wonder why the original array changed. The fix is straightforward — use .copy() when you need independence."

AFTER:
"Common bug source. Slice array, modify slice thinking you have own copy, original array changes. Fix: .copy() when you need independence."

BEFORE:
"The reason it hurts is architectural. A Python list is not a block of numbers. It's a collection of pointers, each pointing to a separate Python object somewhere in memory."

AFTER:
"Reason: architectural. Python list ≠ block of numbers. It's collection of pointers, each pointing to separate Python object in memory."

## Process
1. Read the HTML file fully
2. Edit each prose paragraph section by section (use edit tool with old_str/new_str)
3. Work through the file top to bottom
4. Don't skip any prose sections
5. Keep it concise but interview-ready — substance over style
