"""Trace div nesting depth in each panel to find extra closes."""
import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

panel_starts = [i for i, l in enumerate(lines) if 'persona__panel' in l and '<div' in l]
panel_starts_line = [i+1 for i in panel_starts]  # 1-based
print(f"Panel start lines: {panel_starts_line}")

# For each panel, trace nesting
for pi, start_idx in enumerate(panel_starts):
    end_idx = panel_starts[pi+1] if pi+1 < len(panel_starts) else len(lines)
    
    depth = 0
    name = ""
    max_depth = 0
    problems = []
    
    for li in range(start_idx, min(end_idx, len(lines))):
        line = lines[li]
        # Count opens and closes on this line
        opens = len(re.findall(r'<div[\s>]', line))
        closes = len(re.findall(r'</div>', line))
        
        if 'persona__name' in line:
            m = re.search(r'persona__name">([^<]+)', line)
            if m: name = m.group(1)
        
        for _ in range(opens):
            depth += 1
            max_depth = max(max_depth, depth)
        
        for _ in range(closes):
            depth -= 1
            if depth < 0:
                problems.append(f"  L{li+1}: depth went to {depth} (EXTRA CLOSE!) -> {line.strip()[:60]}")
    
    print(f"\nPanel {pi} ({name}): max_depth={max_depth}, final_depth={depth}")
    if problems:
        print(f"  PROBLEMS:")
        for p in problems:
            print(p)
    else:
        print(f"  Final depth should be 0 (panel closed)")
