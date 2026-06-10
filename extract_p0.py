import re

with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()

# Find panel boundaries
panels = []
for m in re.finditer(r'<div class="persona__panel', bak):
    panels.append(m.start())

section_end = bak.find('</section>', bak.find('class="persona"'))

# Extract each panel
for i, start in enumerate(panels):
    end = panels[i+1] if i+1 < len(panels) else section_end
    html = bak[start:end]
    
    depth = 0
    lines_out = []
    for line in html.split('\n'):
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
            if m2: cls = ' [' + m2.group(1).split()[0] + ']'
            lines_out.append(f"D{old_depth}->D{depth} {stripped[:80]}{cls}")
    
    lines_out.append(f"Panel {i}: opens={len(re.findall(r'<div[\s>]', html))}, closes={len(re.findall(r'</div>', html))}, final_depth={depth}")
    
    with open(f'c:/semester 2/Web UAS/panel_{i}_struct.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines_out))

print("Done - wrote panel structure files")
