import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The problem: for each panel, the closing structure is:
# After Key Attribute section-box: 3 </div> (stickies, section-box, persona__top) ← WRONG, should be 2
# After Short Description section-box: 1 </div> (section-box) ← needs 1 more for persona__top
# After Needs section-box: 3 </div> (stickies, section-box, persona__mid) ← WRONG, should be 2
# After Challenges section-box: 3 </div> (stickies, section-box, persona__mid) ← WRONG, should be 2+1
# After Opportunities section-box: 3 </div> (stickies, section-box, persona__bottom) ← WRONG, should be 2+1

# Actually the REAL issue is simpler: the original had 3 </div> after Key Attribute sticky (closing top prematurely)
# But it should have been 2 (just stickies and section-box).
# The 3rd </div> (closing persona__top) should come AFTER Short Description.

# So the fix is:
# 1. REMOVE one </div> after Key Attribute (the one that prematurely closes persona__top)
# 2. ADD one </div> after Short Description (to properly close persona__top)
# Same for Needs→Challenges and Challenges→Opportunities boundaries

# From the grep results, here are the exact line numbers to fix:
# Panel 0: Short Desc closes at L183,184 | Challenges close at L207,208
# Panel 1: Short Desc closes at L357,358 | Challenges close at L380,381
# Panel 2: Short Desc closes at L532,533 | Challenges close at L554,555
# Panel 3: Short Desc closes at L704,705 | Challenges close at L727,728
# Panel 4: Short Desc closes at L878,879 | Challenges close at L903,904

# And before User Journey Map, after Opportunities:
# Panel 0: L220,221 | Panel 1: L393,394 | Panel 2: L567,568 | Panel 3: L741,742 | Panel 4: L918,919

# The simplest approach: insert </div> before persona__mid, persona__bottom, and User Journey Map
# using unique text anchors from the grep output.

# For each panel, I'll insert a </div> right before <div class="persona__mid">
# and before <div class="persona__bottom"> and before <!-- User Journey Map -->

fixes = 0

# Fix: insert </div> before each persona__mid, persona__bottom, and User Journey Map
# These appear at specific lines with specific context

# Pattern: </div>\n            </div>\n            <!-- Middle Row -->\n<div class="persona__mid">
# OR:      </div>\n            </div>\n<div class="persona__mid">
# Need to add </div> between the last </div> and the persona__mid

# Let's use line-based approach
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    
    # Check if NEXT line starts with <div class="persona__mid">
    if i + 1 < len(lines) and lines[i+1].strip().startswith('<div class="persona__mid">'):
        # Check if current line is </div> - we need to add one more </div>
        if line.strip() == '</div>':
            # Get indentation from the persona__mid line
            mid_indent = len(lines[i+1]) - len(lines[i+1].lstrip())
            # The </div> for persona__top should be at the grid level (same as persona__top)
            # persona__top opens at 12 spaces indent, so its close should also be at 12 spaces
            new_lines.append(' ' * mid_indent + '</div>')
            fixes += 1
    
    # Same for persona__bottom
    if i + 1 < len(lines) and lines[i+1].strip().startswith('<div class="persona__bottom">'):
        if line.strip() == '</div>':
            bottom_indent = len(lines[i+1]) - len(lines[i+1].lstrip())
            new_lines.append(' ' * bottom_indent + '</div>')
            fixes += 1
    
    # Same for User Journey Map comment
    if i + 1 < len(lines) and '<!-- User Journey Map -->' in lines[i+1]:
        if line.strip() == '</div>':
            journey_indent = len(lines[i+1]) - len(lines[i+1].lstrip())
            new_lines.append(' ' * journey_indent + '</div>')
            fixes += 1
    
    i += 1

content = '\n'.join(new_lines)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Applied {fixes} fixes")
