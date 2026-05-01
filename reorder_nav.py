import glob, re, os

base = '/home/ntlpt24/Master/buildmode/personal/zta'

# Collect all HTML files
files = glob.glob(os.path.join(base, 'chapters', '**', '*.html'), recursive=True)
files.append(os.path.join(base, 'index.html'))

print(f"Found {len(files)} files to process")

# Pattern to match the Production Systems block (nav-part + ch13 chapter + ch13 sections)
# followed by Probabilistic & Generative AI block (nav-part + ch14 + sections + ch15 + sections)
# We need to swap these two blocks.

# The pattern in chapter files uses ../ch13/ paths
# The pattern in root index.html uses chapters/ch13/ paths

nav_pattern = re.compile(
    r'(  <div class="nav-part">Production Systems</div>\n'
    r'  <a class="nav-chapter" href="[^"]*ch13/index\.html" data-href="ch13">\n'
    r'.*?</div>\n)'  # through the end of ch13 nav-sections
    r'(  <div class="nav-part">Probabilistic &amp; Generative AI</div>\n'
    r'  <a class="nav-chapter" href="[^"]*ch14/index\.html" data-href="ch14">\n'
    r'.*?'
    r'  <a class="nav-chapter" href="[^"]*ch15/index\.html" data-href="ch15">\n'
    r'.*?</div>\n)',  # through the end of ch15 nav-sections
    re.DOTALL
)

count = 0
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    m = nav_pattern.search(content)
    if m:
        production_block = m.group(1)
        probabilistic_block = m.group(2)
        new_content = content[:m.start()] + probabilistic_block + production_block + content[m.end():]
        with open(filepath, 'w') as f:
            f.write(new_content)
        count += 1
    else:
        print(f"WARNING: No match in {filepath}")

print(f"Updated {count} files")
