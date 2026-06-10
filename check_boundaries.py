import re

with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()

panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', bak)]
section_end = bak.find('</section>', panel_starts[-1])

out = []

for i in range(1, len(panel_starts)):
    prev_start = panel_starts[i-1]
    start = panel_starts[i]
    region = bak[prev_start:start]
    
    depth = 0
    last_lines = []
    for line in region.split('\n'):
        stripped = line.strip()
        if not stripped:
            continue
        opens = len(re.findall(r'<div[\s>]', stripped))
        closes = len(re.findall(r'</div>', stripped))
        old_depth = depth
        depth += opens - closes
        if opens or closes:
            # Only show class names, not content (to avoid encoding issues)
            cls = ''
            m2 = re.search(r'class="([^"]+)"', stripped)
            if m2: cls = ' class=' + m2.group(1).split()[0]
            tag = 'open' if opens else 'close'
            if opens and closes: tag = 'self'
            last_lines.append(f"    D{old_depth}->D{nd} {tag} {cls}" if False else
                            f"    D{old_depth}->D{depth} {cls or stripped[:40]}")
    
    out.append(f"\n--- Before Panel {i} ---")
    for l in last_lines[-8:]:
        out.append(l)
    out.append(f"  Final depth: {depth}")

# Panel 4 to section end
region = bak[panel_starts[-1]:section_end]
depth = 0
last_lines = []
for line in region.split('\n'):
    stripped = line.strip()
    if not stripped:
        continue
    opens = len(re.findall(r'<div[\s>]', stripped))
    closes = len(re.findall(r'</div>', stripped))
    old_depth = depth
    depth += opens - closes
    if opens or closes:
        cls = ''
        m2 = re.search(r'class="([^"]+)"', stripped)
        if m2: cls = ' class=' + m2.group(1).split()[0]
        last_lines.append(f"    D{old_depth}->D{depth} {cls or stripped[:40]}")

out.append(f"\n--- Panel 4 to section end ---")
for l in last_lines[-8:]:
    out.append(l)
out.append(f"  Final depth: {depth}")

with open('c:/semester 2/Web UAS/boundaries.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
