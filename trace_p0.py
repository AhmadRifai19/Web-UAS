import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Panel 0: line 161 to line ~340
start = 160  # 0-indexed (line 161)
end = 340    # 0-indexed

depth = 0
for i in range(start, end):
    line = lines[i]
    opens = len(re.findall(r'<div[\s>]', line))
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        for _ in range(opens):
            depth += 1
        for _ in range(closes):
            depth -= 1
        linenum = i + 1
        stripped = line.strip()[:80]
        if depth < 0:
            print(f"L{linenum:4d}  +{opens} -{closes}  d={depth:3d}  *** NEGATIVE ***  {stripped}")
        else:
            print(f"L{linenum:4d}  +{opens} -{closes}  d={depth:3d}  {stripped}")

print(f"\nFinal depth: {depth}")
