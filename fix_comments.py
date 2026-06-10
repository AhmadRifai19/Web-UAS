"""Fix panel comments with garbled box-drawing chars."""
import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

replacements = {
    'Panel 1: Fikri Ramadhan': '<!-- === Panel 1: Fikri Ramadhan === -->\n',
    'Panel 2: Susanto Hari Wibowo': '<!-- === Panel 2: Susanto Hari Wibowo === -->\n',
    'Panel 3: Haris Wahyu Ramadhani': '<!-- === Panel 3: Haris Wahyu Ramadhani === -->\n',
    'Panel 4: Widya Dny Yuanika Rahayu': '<!-- === Panel 4: Widya Dny Yuanika R. === -->\n',
    'Panel 5: Zaskiya Soaldi A.A.': '<!-- === Panel 5: Zaskiya Soaldi A.A. === -->\n',
}

for i, line in enumerate(lines):
    for key, replacement in replacements.items():
        if key in line and '===' not in line:
            indent = line[:len(line) - len(line.lstrip())]
            lines[i] = indent + replacement
            print(f"  Line {i+1}: Fixed {key}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")
