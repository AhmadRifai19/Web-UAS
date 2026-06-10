import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# From the trace, we know exactly where the missing </div> should go:
# After each sticky section, there should be 3 closing </div> but there are only 2+1
# The issue: persona__top/mid/bottom each need their own </div> after all children close
# But the regex merged the closing structure

# The pattern in the file is:
# Line N:   </div>     (closes stickies)
# Line N+1: </div>     (closes section-box)  
# Line N+2: </div>     (closes persona__top/mid/bottom - BUT this is premature for the first section)

# For panels 0 and similar:
# Key Attribute has 3 closes (stickies, section-box, persona__top) - WRONG, should be 2
# Short Description has 1 close (section-box) - WRONG, should also close persona__top

# The correct structure should be:
# Key Attribute: 2 closes (stickies, section-box)
# Short Description: 2 closes (section-box, persona__top)
# Needs: 2 closes (stickies, section-box)  
# Challenges: 2 closes (stickies, section-box) + 1 close (persona__mid)
# Opportunities: 2 closes (stickies, section-box) + 1 close (persona__bottom)

# Instead of trying to fix the complex structure, let me just add the missing </div>
# at the right positions by tracking depth.

new_lines = []
i = 0
fixes = 0
in_persona_panel = False
panel_depth = 0

while i < len(lines):
    line = lines[i]
    stripped = line.strip()
    
    # Track persona panels
    if 'data-panel="' in line and 'persona__panel' in line:
        in_persona_panel = True
        panel_depth = 0
    
    if in_persona_panel:
        opens = len(re.findall(r'<div[\s>]', line))
        closes = line.count('</div>')
        
        for _ in range(opens):
            panel_depth += 1
        for _ in range(closes):
            panel_depth -= 1
        
        # Check if we're at a critical boundary
        # Before persona__mid, depth should go from 3 (inside top) to 2 (grid level)
        # Currently it stays at 3 because top wasn't closed
        if '<!-- Middle Row -->' in line or (i + 1 < len(lines) and '<div class="persona__mid">' in lines[i+1]):
            if panel_depth > 2:
                # Need to close persona__top
                indent = line[:len(line) - len(line.lstrip())]
                if not indent.strip():
                    indent = '            '
                new_lines.append(indent + '</div>\n')
                panel_depth -= 1
                fixes += 1
        
        if '<!-- Bottom Row -->' in line or (i + 1 < len(lines) and '<div class="persona__bottom">' in lines[i+1]):
            if panel_depth > 2:
                indent = line[:len(line) - len(line.lstrip())]
                if not indent.strip():
                    indent = '            '
                new_lines.append(indent + '</div>\n')
                panel_depth -= 1
                fixes += 1
        
        if '<!-- User Journey Map -->' in line:
            if panel_depth > 2:
                indent = line[:len(line) - len(line.lstrip())]
                if not indent.strip():
                    indent = '            '
                new_lines.append(indent + '</div>\n')
                panel_depth -= 1
                fixes += 1
        
        # End of persona panel
        if panel_depth <= 0 and ('data-panel="' not in line or i > 0):
            in_persona_panel = False
    
    new_lines.append(line)
    i += 1

with open(html_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Applied {fixes} fixes")
