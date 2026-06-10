"""Remove garbled duplicate panel comments."""
import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and remove garbled comment lines (lines containing â• or similar garbled chars)
# These are duplicate comments before the clean ones
to_remove = []
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('<!--') and 'â' in stripped and 'Panel' in stripped:
        to_remove.append(i)

# Also remove the blank line before each garbled comment if it exists
# (to avoid double blank lines after removal)
for idx in reversed(to_remove):
    # Remove the garbled comment line
    del lines[idx]
    # If the line before is also blank, remove it too
    if idx > 0 and lines[idx-1].strip() == '':
        del lines[idx-1]

with open('c:/semester 2/Web UAS/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Removed {len(to_remove)} garbled comment lines")
