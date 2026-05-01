#!/usr/bin/env python3
"""Generate a single book-style PDF from all Zero to Hero AI chapters."""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import weasyprint

BASE = Path(__file__).parent
CHAPTERS_DIR = BASE / "chapters"
INDEX_HTML = BASE / "index.html"
OUTPUT_PDF = BASE / "Zero_to_Hero_AI_Book.pdf"

CHAPTER_NAMES = {
    "ch01": "Python & Programming Foundations",
    "ch02": "Mathematical Foundations",
    "ch03": "Data Fundamentals",
    "ch04": "ML Fundamentals & Core Concepts",
    "ch05": "Supervised Learning",
    "ch06": "Unsupervised Learning",
    "ch07": "Deep Learning Foundations",
    "ch08": "Training Deep Networks",
    "ch09": "CNNs & Computer Vision",
    "ch10": "Sequence Models & Attention",
    "ch11": "Natural Language Processing",
    "ch12": "Large Language Models",
    "ch13": "ML Systems and Production",
    "ch14": "Probabilistic & Bayesian ML",
    "ch15": "Generative Models",
    "ch16": "Advanced Deep Learning",
    "ch17": "Learning Theory & Advanced ML",
    "ch18": "Reinforcement Learning",
}

PART_NAMES = {
    "ch01": "Part I: Foundations",
    "ch04": "Part II: Classical Machine Learning",
    "ch07": "Part III: Deep Learning",
    "ch11": "Part IV: Language & LLMs",
    "ch13": "Part V: Production Systems",
    "ch14": "Part VI: Probabilistic & Generative AI",
    "ch16": "Part VII: Advanced Topics",
}

BOOK_CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2.5cm;
    @bottom-center {
        content: counter(page);
        font-family: 'Georgia', serif;
        font-size: 10pt;
        color: #666;
    }
    @top-center {
        content: "Zero to Hero AI";
        font-family: 'Georgia', serif;
        font-size: 9pt;
        color: #888;
    }
}

@page :first {
    @top-center { content: ""; }
    @bottom-center { content: ""; }
}

* { box-sizing: border-box; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 10.5pt;
    line-height: 1.65;
    color: #1a1a1a;
    background: white;
    margin: 0;
    padding: 0;
}

/* Cover page */
.cover-page {
    page-break-after: always;
    text-align: center;
    padding: 6cm 2cm 4cm;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.cover-page h1 {
    font-family: 'Georgia', serif;
    font-size: 36pt;
    font-weight: bold;
    color: #1a1a2e;
    margin-bottom: 0.3em;
    letter-spacing: -0.5px;
}

.cover-page .subtitle {
    font-size: 16pt;
    color: #4a4a6a;
    margin-bottom: 3em;
    font-style: italic;
}

.cover-page .meta {
    font-size: 11pt;
    color: #666;
    margin-top: 4em;
}

.cover-page .stat {
    font-size: 13pt;
    color: #333;
    margin: 0.3em 0;
}

/* TOC */
.toc-page {
    page-break-after: always;
    padding: 1cm 0;
}

.toc-page h2 {
    font-size: 20pt;
    color: #1a1a2e;
    border-bottom: 2px solid #1a1a2e;
    padding-bottom: 0.3em;
    margin-bottom: 1em;
}

.toc-part {
    font-size: 10pt;
    font-weight: bold;
    color: #4a4a6a;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
}

.toc-chapter {
    font-size: 11pt;
    font-weight: bold;
    color: #1a1a2e;
    margin: 0.2em 0 0.1em 0;
}

.toc-section {
    font-size: 9.5pt;
    color: #555;
    margin-left: 1.5em;
    line-height: 1.5;
}

/* Part divider */
.part-divider {
    page-break-before: always;
    page-break-after: always;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 60vh;
}

.part-divider .part-num {
    font-size: 13pt;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 0.5em;
}

.part-divider h2 {
    font-size: 28pt;
    color: #1a1a2e;
    font-weight: bold;
    text-align: center;
}

/* Chapter header */
.chapter-header {
    page-break-before: always;
    padding-bottom: 1.5em;
    margin-bottom: 1.5em;
    border-bottom: 3px solid #1a1a2e;
}

.chapter-header .ch-label {
    font-size: 10pt;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0.3em;
}

.chapter-header h2 {
    font-size: 24pt;
    color: #1a1a2e;
    margin: 0;
    line-height: 1.2;
}

/* Section header */
.section-header {
    padding-top: 1.5em;
    padding-bottom: 0.5em;
    margin-top: 1em;
    margin-bottom: 1em;
    border-bottom: 1px solid #ddd;
}

.section-header h3 {
    font-size: 16pt;
    color: #1a1a2e;
    margin: 0;
}

/* Content headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Georgia', serif;
    color: #1a1a2e;
    line-height: 1.3;
}

h1 { font-size: 20pt; margin: 1.2em 0 0.5em; }
h2 { font-size: 16pt; margin: 1em 0 0.4em; }
h3 { font-size: 13pt; margin: 0.9em 0 0.3em; }
h4 { font-size: 11pt; margin: 0.8em 0 0.3em; }
h5, h6 { font-size: 10.5pt; margin: 0.7em 0 0.2em; }

p { margin: 0.5em 0 0.8em; orphans: 3; widows: 3; }

a { color: #2563eb; text-decoration: none; }

/* Code */
code, pre {
    font-family: 'Courier New', 'Courier', monospace;
    font-size: 9pt;
    background: #f5f5f5;
    border-radius: 3px;
}

code { padding: 1px 4px; }

pre {
    padding: 0.8em 1em;
    border-left: 3px solid #ccc;
    overflow-x: auto;
    white-space: pre-wrap;
    word-wrap: break-word;
    line-height: 1.45;
    margin: 0.8em 0;
}

/* Lists */
ul, ol { margin: 0.4em 0 0.8em 1.5em; padding: 0; }
li { margin: 0.2em 0; }

/* Tables */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.8em 0;
    font-size: 9.5pt;
}
th {
    background: #1a1a2e;
    color: white;
    padding: 6px 10px;
    text-align: left;
}
td {
    border: 1px solid #ddd;
    padding: 5px 10px;
}
tr:nth-child(even) td { background: #f9f9f9; }

/* Blockquote */
blockquote {
    border-left: 4px solid #4a4a6a;
    margin: 0.8em 0;
    padding: 0.5em 1em;
    color: #555;
    font-style: italic;
}

/* Math-like formulas */
.math, .formula {
    font-family: 'Courier New', monospace;
    background: #f0f4ff;
    padding: 0.5em 1em;
    border-radius: 4px;
    margin: 0.5em 0;
    font-size: 9.5pt;
}

/* Hide nav/sidebar/UI elements */
.sidebar, .sidebar-toggle, .progress-bar, .topbar,
nav, .nav-chapter, .nav-section, .nav-part,
.breadcrumb, .prev-next, button,
.github-star, #github-star-btn,
.toc-panel, .search-overlay {
    display: none !important;
}

/* Main content area */
.main-content, main, .content, article {
    max-width: 100%;
    margin: 0;
    padding: 0;
}

img { max-width: 100%; height: auto; }

/* Page break helpers */
.page-break { page-break-after: always; }
.avoid-break { page-break-inside: avoid; }
"""


def extract_nav_links():
    """Parse index.html to get ordered list of (chapter, section_file, section_name)."""
    soup = BeautifulSoup(INDEX_HTML.read_text(), "html.parser")
    nav = soup.find("nav", class_="sidebar-nav")

    items = []  # (ch_id, file_path, label, type)
    current_ch = None

    for el in nav.find_all(["a", "div"]):
        cls = el.get("class", [])
        if "nav-chapter" in cls:
            href = el.get("href", "")
            m = re.search(r"chapters/(ch\d+)/index\.html", href)
            if m:
                current_ch = m.group(1)
                items.append((current_ch, CHAPTERS_DIR / current_ch / "index.html", el.get_text(strip=True), "chapter"))
        elif "nav-section" in cls and current_ch:
            href = el.get("href", "")
            m = re.search(r"chapters/(ch\d+)/(.+\.html)", href)
            if m:
                ch, sf = m.group(1), m.group(2)
                fp = CHAPTERS_DIR / ch / sf
                if fp.exists():
                    items.append((ch, fp, el.get_text(strip=True), "section"))
    return items


def extract_content(html_path: Path) -> str:
    """Extract main content from an HTML file, stripping nav/sidebar."""
    soup = BeautifulSoup(html_path.read_text(), "html.parser")

    # Remove unwanted elements
    for sel in [".sidebar", ".sidebar-toggle", ".progress-bar", ".topbar",
                "nav", ".breadcrumb", ".prev-next", "button",
                ".toc-panel", ".search-overlay", "script", "style",
                "[class*='sidebar']", "[class*='topbar']", "[class*='nav-']"]:
        for el in soup.select(sel):
            el.decompose()

    # Try to find main content
    main = (soup.find("main") or soup.find(class_="main-content") or
            soup.find(class_="content") or soup.find("article") or soup.body)

    if main:
        # Fix relative image paths
        for img in main.find_all("img"):
            src = img.get("src", "")
            if src and not src.startswith("http") and not src.startswith("data:"):
                abs_path = (html_path.parent / src).resolve()
                img["src"] = abs_path.as_uri()
        return str(main)
    return ""


def build_toc(nav_items):
    """Build a table of contents HTML."""
    html = ['<div class="toc-page"><h2>Table of Contents</h2>']
    current_ch = None

    for ch_id, fp, label, typ in nav_items:
        if typ == "chapter":
            if ch_id in PART_NAMES:
                html.append(f'<div class="toc-part">{PART_NAMES[ch_id]}</div>')
            ch_num = int(ch_id[2:])
            html.append(f'<div class="toc-chapter">Chapter {ch_num}: {CHAPTER_NAMES.get(ch_id, label)}</div>')
            current_ch = ch_id
        elif typ == "section":
            html.append(f'<div class="toc-section">· {label}</div>')

    html.append('</div>')
    return "\n".join(html)


def build_cover():
    return """
<div class="cover-page">
  <div>
    <h1>Zero to Hero AI</h1>
    <div class="subtitle">A Complete Guide from Python to Large Language Models</div>
    <div class="stat">18 Chapters · 6,972 Concepts</div>
    <div class="meta">
      <p>github.com/santhoshkammari/zero-to-hero-ai</p>
    </div>
  </div>
</div>
"""


def build_html():
    nav_items = extract_nav_links()

    parts = []
    parts.append(build_cover())
    parts.append(build_toc(nav_items))

    current_ch = None
    emitted_parts = set()

    for ch_id, fp, label, typ in nav_items:
        if not fp.exists():
            print(f"  [skip] {fp} not found")
            continue

        if typ == "chapter":
            # Part divider
            if ch_id in PART_NAMES and ch_id not in emitted_parts:
                part_label = PART_NAMES[ch_id]
                part_num = part_label.split(":")[0]
                part_name = part_label.split(":")[1].strip()
                parts.append(f'''
<div class="part-divider">
  <div class="part-num">{part_num}</div>
  <h2>{part_name}</h2>
</div>''')
                emitted_parts.add(ch_id)

            ch_num = int(ch_id[2:])
            ch_name = CHAPTER_NAMES.get(ch_id, label)
            parts.append(f'''
<div class="chapter-header">
  <div class="ch-label">Chapter {ch_num}</div>
  <h2>{ch_name}</h2>
</div>''')
            current_ch = ch_id
            print(f"  Chapter {ch_num}: {ch_name}")

        elif typ == "section":
            parts.append(f'''
<div class="section-header">
  <h3>{label}</h3>
</div>''')
            content = extract_content(fp)
            parts.append(content)
            print(f"    Section: {label}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Zero to Hero AI — Complete Book</title>
  <style>{BOOK_CSS}</style>
</head>
<body>
{"".join(parts)}
</body>
</html>"""
    return full_html


def main():
    print("Building book HTML...")
    html = build_html()

    tmp_html = BASE / "_book_tmp.html"
    tmp_html.write_text(html, encoding="utf-8")
    print(f"HTML written ({len(html)//1024} KB)")

    print(f"Generating PDF → {OUTPUT_PDF.name} ...")
    doc = weasyprint.HTML(filename=str(tmp_html))
    doc.write_pdf(str(OUTPUT_PDF))

    tmp_html.unlink()
    size_mb = OUTPUT_PDF.stat().st_size / 1024 / 1024
    print(f"Done! PDF saved: {OUTPUT_PDF} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
