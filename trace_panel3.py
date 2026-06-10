import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Panel 3: line 671 to ~line 844
start = 670  # 0-indexed
end = 844    # 0-indexed (exclusive)

depth = 0
for i in range(start, end):
    line = lines[i]
    # Count opens and closes
    opens = len(re.findall(r'<div[\s>]', line))
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        for _ in range(opens):
            depth += 1
        for _ in range(closes):
            depth -= 1
        linenum = i + 1
        stripped = line.strip()[:80]
        print(f"L{linenum:4d}  +{opens} -{closes}  d={depth:3d}  {stripped}")

print(f"\nFinal depth: {depth}")
