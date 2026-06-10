import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The problem: each sticky section (Key Attribute, Needs, Challenges, Opportunities) 
# in each panel is missing one </div>.
# Currently: </div>\n                </div>\n              </div>\n  (3 closes)
# Should be: </div>\n                </div>\n              </div>\n            </div>\n  (but this varies)
#
# Actually, looking at the trace:
# - stickies close (d goes from 5 to 4) 
# - section-box close (d goes from 4 to 3)
# - ONE more close (d goes from 3 to 2) -- this closes persona__top prematurely
#
# The issue: persona__top should close AFTER both Key Attribute and Short Description sections.
# But it closes after just Key Attribute.
# That means there's a MISSING </div> somewhere between Short Description close and persona__mid open.

# Let me check: between </div> (Short Description section-box close) and <div class="persona__mid">,
# there should be a </div> to close persona__top.

# Find all persona__mid openings and check if persona__top is properly closed before them
fixes = 0

# Fix 1: Add missing </div> before persona__mid (closes persona__top)
# This is needed because Key Attribute's 3rd </div> was incorrectly closing persona__top
# instead of just closing the section-box
pattern = re.compile(r'(</div>\s*)\n(\s*<!-- Middle Row -->\s*\n\s*<div class="persona__mid">)')
matches = list(pattern.finditer(content))
for m in reversed(matches):
    # Check if we need to add a </div>
    # Count the depth up to this point in the panel
    panel_start = content.rfind('data-panel="', 0, m.start())
    if panel_start == -1:
        continue
    # Find the panel opening div
    panel_div_start = content.rfind('<div', 0, panel_start)
    
    segment = content[panel_div_start:m.start()]
    opens = len(re.findall(r'<div[\s>]', segment))
    closes = segment.count('</div>')
    depth_at_mid = opens - closes
    
    # persona__top opens at depth 3 (panel=1, grid=2, top=3)
    # After top closes, mid opens at depth 3
    # So depth_at_mid should be 2 (panel + grid are still open)
    if depth_at_mid > 2:
        # Need to add extra </div> to close persona__top
        indent = '            '  # same as persona__top's parent level
        old_text = m.group(0)
        new_text = old_text.rstrip() + '\n' + indent + '</div>\n' + m.group(2).lstrip()
        # Actually just insert a </div> line before persona__mid
        insert_pos = m.start(2)
        line_before = content.rfind('\n', 0, insert_pos)
        # Get indentation of the persona__mid line
        mid_line_start = content.find('<div class="persona__mid">', insert_pos)
        mid_indent = content[line_before+1:mid_line_start]
        mid_indent = mid_indent[:len(mid_indent) - len(mid_indent.lstrip())]
        
        # The closing </div> for persona__top should be at the same indent as persona__mid
        content = content[:insert_pos] + mid_indent + '</div>\n' + mid_indent.lstrip() + content[insert_pos:]
        fixes += 1
        print(f"Added </div> before persona__mid (depth was {depth_at_mid}, should be 2)")

# Fix 2: Add missing </div> before persona__bottom (closes persona__mid)
pattern2 = re.compile(r'(</div>\s*)\n(\s*<!-- Bottom Row -->\s*\n\s*<div class="persona__bottom">)')
matches2 = list(pattern2.finditer(content))
for m in reversed(matches2):
    panel_start = content.rfind('data-panel="', 0, m.start())
    if panel_start == -1:
        continue
    panel_div_start = content.rfind('<div', 0, panel_start)
    
    segment = content[panel_div_start:m.start()]
    opens = len(re.findall(r'<div[\s>]', segment))
    closes = segment.count('</div>')
    depth_at_bottom = opens - closes
    
    if depth_at_bottom > 2:
        insert_pos = m.start(2)
        line_before = content.rfind('\n', 0, insert_pos)
        bottom_line_start = content.find('<div class="persona__bottom">', insert_pos)
        bottom_indent = content[line_before+1:bottom_line_start]
        bottom_indent = bottom_indent[:len(bottom_indent) - len(bottom_indent.lstrip())]
        
        content = content[:insert_pos] + bottom_indent + '</div>\n' + bottom_indent.lstrip() + content[insert_pos:]
        fixes += 1
        print(f"Added </div> before persona__bottom (depth was {depth_at_bottom}, should be 2)")

# Fix 3: Add missing </div> before User Journey Map (closes persona__bottom)
pattern3 = re.compile(r'(</div>\s*)\n(\s*<!-- User Journey Map -->)')
matches3 = list(pattern3.finditer(content))
for m in reversed(matches3):
    panel_start = content.rfind('data-panel="', 0, m.start())
    if panel_start == -1:
        continue
    panel_div_start = content.rfind('<div', 0, panel_start)
    
    segment = content[panel_div_start:m.start()]
    opens = len(re.findall(r'<div[\s>]', segment))
    closes = segment.count('</div>')
    depth_at_journey = opens - closes
    
    if depth_at_journey > 2:
        insert_pos = m.start(2)
        line_before = content.rfind('\n', 0, insert_pos)
        journey_line_start = content.find('<!-- User Journey Map -->', insert_pos)
        journey_indent = content[line_before+1:journey_line_start]
        journey_indent = journey_indent[:len(journey_indent) - len(journey_indent.lstrip())]
        
        content = content[:insert_pos] + journey_indent + '</div>\n' + journey_indent.lstrip() + content[insert_pos:]
        fixes += 1
        print(f"Added </div> before User Journey Map (depth was {depth_at_journey}, should be 2)")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nApplied {fixes} fixes total")
