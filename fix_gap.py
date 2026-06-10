"""Fix the gap between persona section end and define section start."""
import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the define section start
define_start = content.find('<section class="define"')
if define_start < 0:
    print("ERROR: Define section not found!")
    exit(1)

# Find the persona section start
persona_start = content.find('<section class="persona"')
if persona_start < 0:
    print("ERROR: Persona section not found!")
    exit(1)

# Find the LAST panel end (the closing </div> of the last persona__panel)
last_panel_start = content.rfind('<div class="persona__panel', 0, define_start)
if last_panel_start < 0:
    print("ERROR: Last panel not found!")
    exit(1)

# Find where the last panel ends by tracking depth
depth = 0
pos = last_panel_start
panel_end = -1
for m in re.finditer(r'<div[\s>]|</div>', content[last_panel_start:]):
    if m.group().startswith('<div'):
        depth += 1
    else:
        depth -= 1
    if depth == 0:
        panel_end = last_panel_start + m.end()
        break

if panel_end < 0:
    print("ERROR: Could not find panel end!")
    exit(1)

# The gap between panel_end and define_start should be:
# \n\n      </div>\n    </section>\n\n
# Replace whatever is there
correct_gap = '\n\n      </div>\n    </section>\n\n'
new_content = content[:panel_end] + correct_gap + content[define_start:]

with open('c:/semester 2/Web UAS/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Fixed gap: replaced {define_start - panel_end} chars with correct closing")
print(f"New file size: {len(new_content)}")
