"""
Find and remove extra </div> in each panel from the .bak file.
The extra closes are NOT in the interview section (already fixed),
they're in the journey/bottom/mid sections.
"""
import re

with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()

panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', bak)]
persona_sec_end = bak.find('</section>', panel_starts[-1]) + len('</section>')

out = []
for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else persona_sec_end
    html = bak[start:end]
    
    lines = html.split('\n')
    depth = 0
    problem_lines = []
    
    for li, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        opens = len(re.findall(r'<div[\s>]', stripped))
        closes = len(re.findall(r'</div>', stripped))
        old_depth = depth
        depth += opens - closes
        
        # Track where depth goes below 0 or where consecutive closes happen
        if depth < 0:
            problem_lines.append((li, old_depth, depth, stripped[:60]))
    
    name_m = re.search(r'persona__name">([^<]+)', html)
    name = name_m.group(1) if name_m else f'Panel {i}'
    
    out.append(f"\nPanel {i} ({name}): final_depth={depth}")
    if problem_lines:
        out.append(f"  Lines where depth < 0:")
        for li, od, nd, text in problem_lines:
            out.append(f"    Line {li}: D{od}->D{nd}: {text}")
    
    # Also show the last 15 div lines to understand closing structure
    div_lines = []
    depth = 0
    for li, line in enumerate(lines):
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
            div_lines.append(f"    L{li:3d} D{old_depth:2d}->D{depth:2d} {cls or stripped[:50]}")
    
    out.append(f"  Last 10 div lines:")
    for dl in div_lines[-10:]:
        out.append(dl)

with open('c:/semester 2/Web UAS/panel_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
