import os
import re

file_path = 'c:/semester 2/Web UAS/index.html'
bak_path = 'c:/semester 2/Web UAS/index.html.bak'
with open(bak_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will use a simple regex to grab the exact blocks:
# <div class="persona__top"> ... up to <div class="persona__journey-row">
# Actually, the most robust way is to just find the start of persona__top and the start of persona__journey-row (or whatever comes after bottom)
# In index.html.bak, each panel has:
# <div class="persona__top">
# <div class="persona__mid">
# <div class="persona__bottom">
#   ...
# </div>
# </div> (wait, persona__bottom is just one div, but it contains a section-box, so 2 closing divs)

names = ['Fikri Ramadhan', 'Susanto Hari Wibowo', 'Haris Wahyu Ramadhani', 'Widya Dny Yuanika R.', 'Zaskiya Soaldi A.A.']
extracted_blocks = []

for name in names:
    # find the name
    name_idx = content.find(f'<h3 class="persona__name">{name}</h3>')
    top_start = content.rfind('<div class="persona__top">', 0, name_idx)
    
    bottom_start = content.find('<div class="persona__bottom">', top_start)
    
    # Let's find exactly the matching closing divs for bottom.
    # It contains exactly `<div class="persona__section-box">` and `<div class="persona__stickies">` ...
    # Instead of counting divs, let's just find the start of the next section!
    next_journey = content.find('<!-- User Journey Map -->', bottom_start)
    next_interview = content.find('<!-- Interview Data -->', bottom_start)
    next_panel = content.find('<div class="persona__panel"', bottom_start)
    end_candidates = [i for i in [next_journey, next_interview, next_panel, len(content)] if i != -1]
    block_end = min(end_candidates)
    
    block_content = content[top_start:block_end].strip()
    # If the original block was broken with extra </div>, it might have them here.
    # In index.html.bak, Fikri, Susanto had Journey Map originally.
    
    extracted_blocks.append(block_content)

# Now, we need to ensure that `block_content` has exactly the same number of <div> and </div>
for i, block in enumerate(extracted_blocks):
    opens = len(re.findall(r'<div\b[^>]*>', block))
    closes = len(re.findall(r'</div>', block))
    diff = opens - closes
    
    print(f"{names[i]}: opens={opens}, closes={closes}, diff={diff}")
    
    # Fix it!
    if diff > 0:
        block += '\n              </div>' * diff
    elif diff < 0:
        # Too many closing divs, strip them from the end
        for _ in range(-diff):
            if block.endswith('</div>'):
                block = block[:-6].strip()
            else:
                last_div = block.rfind('</div>')
                block = block[:last_div] + block[last_div+6:]
    
    extracted_blocks[i] = block

# Now we rebuild
with open('rebuild.py', 'r', encoding='utf-8') as f:
    rebuild_code = f.read()

# We will just patch the rebuild.py logic right here.
parts = content.split('<!-- ============================== AFFINITY MAP / EMPATHIZE ============================== -->')
before_emp = parts[0]
empathize_and_after = '<!-- ============================== AFFINITY MAP / EMPATHIZE ============================== -->' + parts[1]

personas_content_idx = before_emp.find('<div class="personas__content">')
top_html = before_emp[:personas_content_idx + len('<div class="personas__content">')]

# Using the personas_data from rebuild.py
# (I'll just import it)
import sys
sys.path.append('c:/semester 2/Web UAS')
from rebuild import personas_data, build_table, build_interview

panels_html = ""
for i, name in enumerate(names):
    p_data = personas_data[i]
    is_active = ' active' if i == 0 else ''
    data_attr = '' if i == 0 else f' data-panel="{i}"'
    
    panels_html += f'\n          <div class="persona__panel{is_active}"{data_attr}>\n'
    panels_html += '            <div class="persona__grid">\n'
    
    # 1. Base content (Top, Mid, Bottom)
    panels_html += '              ' + extracted_blocks[i] + '\n\n'
    
    # 2. Journey Map
    panels_html += build_table(p_data) + '\n\n'
    
    # 3. Interview Data
    panels_html += build_interview() + '\n'
    
    panels_html += '            </div>\n'
    panels_html += '          </div>\n'

new_index = top_html + '\n' + panels_html + '\n        </div>\n      </div>\n    </section>\n\n    ' + empathize_and_after

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Re-rebuilt index.html and perfectly balanced <div> tags!")
