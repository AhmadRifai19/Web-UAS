"""Fix remaining garbled characters in index.html."""

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix middle dot separator: Â· -> ·  (garbled U+00B7)
content = content.replace('\u00c2\u00b7', '\u00b7')

# Fix play button: â–¶ -> ▶  (garbled U+25B6)
# The garbled form is the UTF-8 bytes of ▶ interpreted as latin-1 then re-encoded
# ▶ = E2 96 B6 in UTF-8, as latin-1: â(0xE2) –(U+2013?) ¶(U+00B6?)
# Just replace the specific garbled sequence
import re
content = re.sub(r'prototype__placeholder-icon">[^<]+</p>',
                  'prototype__placeholder-icon">\u25b6</p>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()
remaining = [(i+1, l.rstrip()) for i, l in enumerate(c.splitlines()) if any(ord(ch) > 127 for ch in l)]
print(f"Lines with non-ASCII: {len(remaining)}")
for ln, text in remaining:
    print(f"  L{ln}: {text[:80]}")
print("Done!")
