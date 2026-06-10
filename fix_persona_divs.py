import re

html_path = r'c:\semester 2\Web UAS\index.html'

# First, let's restore the missing </div> tags
# Each section-box needs 3 closing </div>: stickies, section-box, and parent (top/mid/bottom)
# The previous script accidentally removed one </div> per section

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all section-box closings that are missing a </div>
# The correct pattern after stickies should be: </div>\n              </div>\n              </div>
# But currently it's: </div>\n              </div>  (missing one)

# Let's fix by finding each section's closing pattern and adding the missing </div>

# Pattern for Key Attribute, Needs, Challenges (blue sections)
# and Opportunities (orange section)
# They all end with: </div>\n              </div>  followed by another section or closing tag

# Actually, let me just count and add the missing divs

# Find all instances where a section-box closes with only 2 </div> instead of 3
# The sections we modified are inside persona__top, persona__mid, and persona__bottom

# Let's use a targeted approach: find each section title and fix its closing

fixes = 0

# Fix Key Attribute sections (5 panels)
for title in ["Key Attribute", "Needs", "Challenges"]:
    pattern = re.compile(
        rf'(<h4 class="persona__section-title persona__section-title--blue">{title}</h4>\s*'
        r'<div class="persona__stickies">.*?</div>\s*)'
        r'(</div>)\s*'
        r'(</div>)\s*'
        r'(?=\n\s*<div class="persona__section-box">|\n\s*</div>\s*</div>\s*\n|\n\s*<div class="persona__(mid|bottom))',
        re.DOTALL
    )
    matches = list(pattern.finditer(content))
    for m in reversed(matches):
        # Check if there are exactly 2 closing divs after stickies
        after_stickies = content[m.start(2):m.end(3)]
        # Insert an additional </div> between the two existing ones
        old = m.group(1) + m.group(2) + '\n' + m.group(3)
        # Actually, let me just look at the raw content around each match
        pass

# This approach is getting complicated. Let me take a simpler approach:
# Just revert to the backup and redo with correct regex.

# Actually, the simplest fix: for each section, the closing should be:
# </div>  (closes stickies)
# </div>  (closes section-box)  
# Then the NEXT sibling section starts or the parent (top/mid/bottom) closes

# Let me find the exact pattern that's wrong and fix it

# The broken pattern is:
# </div>
#               </div>
# 
#               <div class="persona__section-box">  (or </div> for last section)
#
# It should be:
# </div>
#               </div>
#               </div>
# 
#               <div class="persona__section-box">  (or </div>)

# Find all places where </div>\n followed by </div>\n followed by blank or new section
# but NOT followed by another </div>

lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    new_lines.append(lines[i])
    # Check if this line closes stickies (</div> with proper indentation)
    stripped = lines[i].strip()
    if stripped == '</div>' and i + 1 < len(lines):
        next_stripped = lines[i+1].strip() if i+1 < len(lines) else ''
        # Check if next line is also </div> (section-box close)
        if next_stripped == '</div>' and i + 2 < len(lines):
            next2_stripped = lines[i+2].strip() if i+2 < len(lines) else ''
            # If the line after that is NOT </div>, we might be missing one
            # But only inside persona panels where we made changes
            # Check if we're inside a persona section by looking at context
            context = '\n'.join(lines[max(0,i-20):i])
            if 'persona__section-title--blue' in context or 'persona__section-title--orange' in context:
                if 'persona__stickies' in context:
                    # We're closing a stickies section
                    # Check if the next line after the two </div> is NOT </div>
                    if next2_stripped != '</div>':
                        # Check if we should add a </div> here
                        # Look at indentation - the stickies close should be indented more than section-box
                        indent_stickies = len(lines[i]) - len(lines[i].lstrip())
                        indent_section = len(lines[i+1]) - len(lines[i+1].lstrip())
                        # If stickies indent > section indent, we need a 3rd closing div at section-box parent level
                        if indent_stickies > indent_section:
                            # Add the missing </div> at the same indentation as section-box close
                            parent_indent = indent_section  # same level as section-box parent
                            # Actually, the 3rd </div> closes persona__top/mid/bottom, which is at a lower indent
                            # Let me look at the correct structure from before the fix
                            # persona__top closes at 12 spaces indent (            </div>)
                            # section-box closes at 14 spaces indent (              </div>)
                            # stickies close at 16 spaces indent (                </div>)
                            # So the missing </div> should be at 12 spaces indent
                            # But this varies. Let me just check the line BEFORE the section-box opening
                            pass
    i += 1

# This line-by-line approach is too complex. Let me use a much simpler method.
print("Trying different approach...")

# Reset
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The issue: each of the 5 sections per panel (Key Attribute, Short Desc, Needs, Challenges, Opportunities)
# is missing one </div> at the end. That's 25 missing </div> tags.
# But Short Description uses <p> tags not <div>, so it doesn't have this issue.
# So it's 4 sections × 5 panels = 20 missing </div> tags.

# Fix: after each section-box that contains stickies, ensure there are 3 </div> at the end
# Pattern: find </div>\n              </div>\n followed by something that's NOT </div>
# and IS inside a persona panel

# Let's find and fix each one by looking for the section titles
for title_class, title_text in [
    ('blue', 'Key Attribute'),
    ('blue', 'Needs'),
    ('blue', 'Challenges'),
    ('orange', 'Opportunities'),
]:
    # Find each occurrence
    search_str = f'persona__section-title--{title_class}">{title_text}</h4>'
    start = 0
    while True:
        pos = content.find(search_str, start)
        if pos == -1:
            break
        
        # Find the stickies container after this
        stickies_start = content.find('<div class="persona__stickies">', pos)
        if stickies_start == -1:
            start = pos + 1
            continue
        
        # Find the end of stickies content (first </div> that closes stickies)
        # Then find the section-box close and parent close
        # Count divs to find the right closing tags
        depth = 0
        scan_pos = stickies_start
        close_positions = []
        for m in re.finditer(r'<div[\s>]|</div>', content[scan_pos:]):
            if m.group().startswith('<div'):
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    close_positions.append(scan_pos + m.end())
                    break
        
        if close_positions:
            # After stickies close, check what follows
            after_close = content[close_positions[0]:close_positions[0]+100]
            # Count how many </div> follow before the next section or closing
            remaining_closes = 0
            check_pos = close_positions[0]
            while True:
                next_div = content.find('</div>', check_pos)
                next_open = re.search(r'<div[\s>]', content[check_pos:])
                if next_div == -1:
                    break
                if next_open and check_pos + next_open.start() < next_div:
                    break  # Found an opening div before next close
                remaining_closes += 1
                check_pos = next_div + 6
            
            if remaining_closes < 2:
                # Missing closing divs - add them
                needed = 2 - remaining_closes
                # Find the indentation from context
                line_start = content.rfind('\n', 0, close_positions[0]) + 1
                indent = content[line_start:close_positions[0]]
                indent = indent[:len(indent) - len(indent.lstrip())]
                
                insertion = ''
                for _ in range(needed):
                    insertion += indent + '</div>\n'
                
                content = content[:close_positions[0]] + '\n' + insertion + content[close_positions[0]:]
                fixes += 1
                print(f"Fixed {title_text} at pos {pos}: added {needed} </div>")
        
        start = pos + 1

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nApplied {fixes} fixes")
