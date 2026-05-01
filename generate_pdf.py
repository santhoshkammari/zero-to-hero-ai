#!/usr/bin/env python3
"""Generate Zero to Hero AI book as PDF.

Features:
  - Parallel chapter rendering across all CPU cores
  - Anthropic/Claude brand theme
  - Automatic PDF merging
"""

import os
import re
import sys
import tempfile
import time
from pathlib import Path
from multiprocessing import Pool, cpu_count

from bs4 import BeautifulSoup
import weasyprint
from pypdf import PdfWriter, PdfReader


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


# ── Anthropic/Claude Brand Colors ─────────────────────────────────────
# Terra Cotta #D97757 · Near-Black #191918 · Pampas #F4F3EE
# Cloudy #B1ADA1 · Crail #C15F3C · Light #E8E6DC

BOOK_CSS = r"""
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2.5cm;
    @top-center {
        content: "ZERO TO HERO AI";
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 7.5pt;
        color: #B1ADA1;
        letter-spacing: 2px;
    }
}

@page :first {
    @top-center { content: ""; }
}

* { box-sizing: border-box; }

body {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 10.5pt;
    line-height: 1.7;
    color: #191918;
    background: #fff;
    margin: 0; padding: 0;
}

/* ── Cover ──────────────────────────────────── */
.cover-page {
    page-break-after: always;
    text-align: center;
    padding: 3cm 2cm;
    min-height: 100vh;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
}

.cover-bar {
    width: 60px; height: 4px;
    background: #D97757; border-radius: 2px;
    margin: 0 auto 1.5em;
}

.cover-page h1 {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 44pt; font-weight: 700;
    color: #191918; margin: 0 0 0.15em;
    letter-spacing: -1px; line-height: 1.1;
}

.cover-page .subtitle {
    font-family: Georgia, serif;
    font-size: 13pt; color: #B1ADA1;
    font-style: italic; margin-bottom: 2.5em;
}

.cover-page .stat {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 10pt; color: #D97757;
    font-weight: 600; letter-spacing: 1.5px;
    text-transform: uppercase; margin: 0.4em 0;
}

.cover-page .meta {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 8.5pt; color: #B1ADA1;
    margin-top: 4em;
}

.cover-bottom-bar {
    width: 120px; height: 2px;
    background: #E8E6DC; border-radius: 1px;
    margin: 3em auto 0;
}

/* ── TOC ────────────────────────────────────── */
.toc-page {
    page-break-after: always;
    padding: 1cm 0;
}

.toc-page h2 {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 20pt; color: #191918; font-weight: 700;
    border-bottom: 2px solid #D97757;
    padding-bottom: 0.3em; margin-bottom: 1.2em;
}

.toc-part {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 9pt; font-weight: 700; color: #D97757;
    text-transform: uppercase; letter-spacing: 1.5px;
    margin-top: 1.4em; margin-bottom: 0.4em;
    padding-top: 0.8em; border-top: 1px solid #E8E6DC;
}

.toc-chapter {
    font-size: 11pt; font-weight: bold;
    color: #191918; margin: 0.3em 0 0.1em;
}

.toc-section {
    font-size: 9pt; color: #B1ADA1;
    margin-left: 1.5em; line-height: 1.6;
}

/* ── Part Divider ───────────────────────────── */
.part-divider {
    page-break-before: always; page-break-after: always;
    text-align: center;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    min-height: 60vh;
}

.part-divider .part-num {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt; color: #D97757;
    text-transform: uppercase; letter-spacing: 4px;
    font-weight: 600; margin-bottom: 0.6em;
}

.part-divider .part-bar {
    width: 40px; height: 3px;
    background: #D97757; border-radius: 2px;
    margin: 0.8em auto;
}

.part-divider h2 {
    font-family: Georgia, serif;
    font-size: 28pt; color: #191918;
    font-weight: bold; line-height: 1.2;
}

/* ── Chapter Header ─────────────────────────── */
.chapter-header {
    page-break-before: always;
    padding-bottom: 1.5em; margin-bottom: 2em;
    border-bottom: 3px solid #D97757;
}

.chapter-header .ch-label {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 9pt; color: #D97757;
    text-transform: uppercase; letter-spacing: 3px;
    font-weight: 600; margin-bottom: 0.4em;
}

.chapter-header h2 {
    font-family: Georgia, serif;
    font-size: 26pt; color: #191918;
    margin: 0; line-height: 1.2;
}

/* ── Section Header ─────────────────────────── */
.section-header {
    padding-top: 1.5em; padding-bottom: 0.4em;
    margin-top: 1.2em; margin-bottom: 1em;
    border-bottom: 1px solid #E8E6DC;
}

.section-header h3 {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 15pt; color: #191918;
    margin: 0; font-weight: 600;
}

/* ── Typography ─────────────────────────────── */
h1, h2, h3, h4, h5, h6 {
    font-family: Georgia, serif;
    color: #191918; line-height: 1.3;
}

h1 { font-size: 20pt; margin: 1.2em 0 0.5em; }
h2 { font-size: 16pt; margin: 1em 0 0.4em; }
h3 { font-size: 13pt; margin: 0.9em 0 0.3em; }
h4 { font-size: 11pt; margin: 0.8em 0 0.3em; }
h5, h6 { font-size: 10.5pt; margin: 0.7em 0 0.2em; }

p { margin: 0.5em 0 0.8em; orphans: 3; widows: 3; }

a { color: #C15F3C; text-decoration: none; }

/* ── Code ───────────────────────────────────── */
code, pre {
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt; background: #F4F3EE;
    border-radius: 3px;
}

code { padding: 1px 5px; color: #C15F3C; }

pre {
    padding: 0.9em 1.1em;
    border-left: 3px solid #D97757;
    overflow-x: auto; white-space: pre-wrap;
    word-wrap: break-word; line-height: 1.45;
    margin: 0.8em 0;
}

pre code { color: #191918; padding: 0; background: none; }

/* ── Lists ──────────────────────────────────── */
ul, ol { margin: 0.4em 0 0.8em 1.5em; padding: 0; }
li { margin: 0.25em 0; }

/* ── Tables ─────────────────────────────────── */
table {
    border-collapse: collapse; width: 100%;
    margin: 0.8em 0; font-size: 9.5pt;
}

th {
    background: #D97757; color: white;
    padding: 7px 10px; text-align: left;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 600; font-size: 9pt;
}

td { border: 1px solid #E8E6DC; padding: 5px 10px; }

tr:nth-child(even) td { background: #F4F3EE; }

/* ── Blockquote ─────────────────────────────── */
blockquote {
    border-left: 4px solid #D97757;
    margin: 0.8em 0; padding: 0.6em 1.2em;
    background: #F4F3EE; color: #555;
    font-style: italic; border-radius: 0 4px 4px 0;
}

/* ── Math ───────────────────────────────────── */
.math, .formula {
    font-family: 'Courier New', monospace;
    background: #F4F3EE; padding: 0.5em 1em;
    border-radius: 4px; border-left: 3px solid #D97757;
    margin: 0.5em 0; font-size: 9.5pt;
}

/* ── Hide UI ────────────────────────────────── */
.sidebar, .sidebar-toggle, .progress-bar, .topbar,
nav, .nav-chapter, .nav-section, .nav-part,
.breadcrumb, .prev-next, button,
.github-star, #github-star-btn,
.toc-panel, .search-overlay {
    display: none !important;
}

.main-content, main, .content, article {
    max-width: 100%; margin: 0; padding: 0;
}

img { max-width: 100%; height: auto; }

.page-break { page-break-after: always; }
.avoid-break { page-break-inside: avoid; }
"""

FRONT_CSS = BOOK_CSS + "\n@page { @top-center { content: ''; } }\n"


# ── HTML Extraction ───────────────────────────────────────────────────

def extract_nav_links():
    """Parse index.html for ordered (chapter, section_file, section_name) list."""
    soup = BeautifulSoup(INDEX_HTML.read_text(), "html.parser")
    nav = soup.find("nav", class_="sidebar-nav")
    items = []
    current_ch = None
    for el in nav.find_all(["a", "div"]):
        cls = el.get("class", [])
        if "nav-chapter" in cls:
            href = el.get("href", "")
            m = re.search(r"chapters/(ch\d+)/index\.html", href)
            if m:
                current_ch = m.group(1)
                items.append((current_ch, CHAPTERS_DIR / current_ch / "index.html",
                              el.get_text(strip=True), "chapter"))
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
    for sel in [".sidebar", ".sidebar-toggle", ".progress-bar", ".topbar",
                "nav", ".breadcrumb", ".prev-next", "button",
                ".toc-panel", ".search-overlay", "script", "style",
                "[class*='sidebar']", "[class*='topbar']", "[class*='nav-']"]:
        for el in soup.select(sel):
            el.decompose()
    main = (soup.find("main") or soup.find(class_="main-content") or
            soup.find(class_="content") or soup.find("article") or soup.body)
    if main:
        for img in main.find_all("img"):
            src = img.get("src", "")
            if src and not src.startswith("http") and not src.startswith("data:"):
                abs_path = (html_path.parent / src).resolve()
                img["src"] = abs_path.as_uri()
        return str(main)
    return ""


# ── Book Structure Builders ───────────────────────────────────────────

def build_toc(nav_items):
    """Build table of contents HTML."""
    html = ['<div class="toc-page"><h2>Table of Contents</h2>']
    for ch_id, fp, label, typ in nav_items:
        if typ == "chapter":
            if ch_id in PART_NAMES:
                html.append(f'<div class="toc-part">{PART_NAMES[ch_id]}</div>')
            ch_num = int(ch_id[2:])
            html.append(f'<div class="toc-chapter">Chapter {ch_num}: '
                        f'{CHAPTER_NAMES.get(ch_id, label)}</div>')
        elif typ == "section":
            html.append(f'<div class="toc-section">· {label}</div>')
    html.append('</div>')
    return "\n".join(html)


def build_cover():
    """Build cover page HTML with Anthropic theme."""
    return """
<div class="cover-page">
  <div>
    <div class="cover-bar"></div>
    <h1>Zero to Hero AI</h1>
    <div class="subtitle">A Complete Guide from Python to Large Language Models</div>
    <div class="cover-bar"></div>
    <div class="stat">18 Chapters · 6,972 Concepts</div>
    <div class="meta">
      <p>github.com/santhoshkammari/zero-to-hero-ai</p>
    </div>
    <div class="cover-bottom-bar"></div>
  </div>
</div>
"""


def build_chunks(nav_items):
    """Split the book into independently-renderable chunks.

    Returns list of (name, html_body, use_page_header) tuples.
    Each chunk becomes a separate PDF rendered in parallel.
    """
    chunks = []

    # Front matter: cover + TOC
    chunks.append(("front", build_cover() + build_toc(nav_items), False))

    # One chunk per chapter (with optional part divider prefix)
    current_parts = []
    current_ch = None
    emitted_parts = set()

    for ch_id, fp, label, typ in nav_items:
        if typ == "chapter":
            if current_parts and current_ch:
                chunks.append((current_ch, "\n".join(current_parts), True))
                current_parts = []

            current_ch = ch_id

            # Part divider page
            if ch_id in PART_NAMES and ch_id not in emitted_parts:
                pl = PART_NAMES[ch_id]
                pnum, pname = pl.split(":", 1)
                current_parts.append(
                    f'<div class="part-divider">'
                    f'<div class="part-num">{pnum.strip()}</div>'
                    f'<div class="part-bar"></div>'
                    f'<h2>{pname.strip()}</h2></div>'
                )
                emitted_parts.add(ch_id)

            ch_num = int(ch_id[2:])
            ch_name = CHAPTER_NAMES.get(ch_id, label)
            current_parts.append(
                f'<div class="chapter-header">'
                f'<div class="ch-label">Chapter {ch_num}</div>'
                f'<h2>{ch_name}</h2></div>'
            )
            print(f"  Chapter {ch_num}: {ch_name}")

        elif typ == "section":
            if not fp.exists():
                print(f"  [skip] {fp}")
                continue
            current_parts.append(
                f'<div class="section-header"><h3>{label}</h3></div>'
            )
            current_parts.append(extract_content(fp))
            print(f"    Section: {label}")

    # Flush last chapter
    if current_parts and current_ch:
        chunks.append((current_ch, "\n".join(current_parts), True))

    return chunks


# ── Rendering ─────────────────────────────────────────────────────────

def _wrap_html(body_html: str, css: str) -> str:
    """Wrap body HTML with full document structure."""
    return (
        f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        f'<title>Zero to Hero AI</title><style>{css}</style></head>'
        f'<body>{body_html}</body></html>'
    )


def _render_worker(args):
    """Multiprocessing worker: render one HTML file to PDF."""
    html_path, pdf_path = args
    weasyprint.HTML(filename=html_path).write_pdf(pdf_path)
    return pdf_path


def main():
    t0 = time.time()
    ncpu = cpu_count()
    print(f"╔══ Zero to Hero AI · PDF Generator ══╗")
    print(f"║  Theme: Anthropic/Claude             ║")
    print(f"║  Cores: {ncpu:<28}║")
    print(f"╚══════════════════════════════════════╝\n")

    # 1. Parse structure & build chunks
    print("① Parsing chapters...")
    nav_items = extract_nav_links()
    chunks = build_chunks(nav_items)
    print(f"\n  → {len(chunks)} chunks ready\n")

    # 2. Write chunk HTML files to temp dir
    tmp_dir = tempfile.mkdtemp(prefix="zta_pdf_")
    tasks = []

    for i, (name, body_html, use_header) in enumerate(chunks):
        css = BOOK_CSS if use_header else FRONT_CSS
        full_html = _wrap_html(body_html, css)

        html_path = os.path.join(tmp_dir, f"{i:03d}_{name}.html")
        pdf_path = os.path.join(tmp_dir, f"{i:03d}_{name}.pdf")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        tasks.append((html_path, pdf_path))

    # 3. Parallel render
    num_workers = min(ncpu, len(tasks))
    print(f"② Rendering {len(tasks)} chunks across {num_workers} workers...")
    t1 = time.time()

    with Pool(processes=num_workers) as pool:
        pdf_paths = pool.map(_render_worker, tasks)

    print(f"  → Rendered in {time.time() - t1:.1f}s\n")

    # 4. Merge PDFs in order
    print("③ Merging PDFs...")
    writer = PdfWriter()
    for path in pdf_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    with open(str(OUTPUT_PDF), "wb") as f:
        writer.write(f)

    # 5. Cleanup temp files
    for f in Path(tmp_dir).iterdir():
        f.unlink()
    os.rmdir(tmp_dir)

    elapsed = time.time() - t0
    size_mb = OUTPUT_PDF.stat().st_size / 1024 / 1024
    print(f"\n✓ Done! {OUTPUT_PDF.name} ({size_mb:.1f} MB) in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
