import os
import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

names = ['Fikri Ramadhan', 'Susanto H. Wibowo', 'Haris W. Ramadhani', 'Widya D. Yuanika R.', 'Zaskiya Soaldi A.A.']
# Wait, inside the HTML it's <h3 class="persona__name">Fikri Ramadhan</h3>. Let's use the full names from h3.
h3_names = ['Fikri Ramadhan', 'Susanto Hari Wibowo', 'Haris Wahyu Ramadhani', 'Widya Dny Yuanika R.', 'Zaskiya Soaldi A.A.']

extracted_blocks = []

for name in h3_names:
    name_idx = content.find(f'<h3 class="persona__name">{name}</h3>')
    top_start = content.rfind('<div class="persona__top">', 0, name_idx)
    bottom_start = content.find('<div class="persona__bottom">', top_start)
    
    # We find the start of the next section to slice properly
    next_journey = content.find('<!-- User Journey Map -->', bottom_start)
    next_interview = content.find('<!-- Interview Data -->', bottom_start)
    next_panel = content.find('<div class="persona__panel"', bottom_start)
    end_candidates = [i for i in [next_journey, next_interview, next_panel, len(content)] if i != -1]
    block_end = min(end_candidates)
    
    block = content[top_start:block_end].strip()
    
    opens = len(re.findall(r'<div\b[^>]*>', block))
    closes = len(re.findall(r'</div>', block))
    diff = opens - closes
    
    # Fix the tags
    if diff > 0:
        block += '\n              </div>' * diff
    elif diff < 0:
        for _ in range(-diff):
            if block.endswith('</div>'):
                block = block[:-6].strip()
            else:
                last_div = block.rfind('</div>')
                block = block[:last_div] + block[last_div+6:]
    
    extracted_blocks.append(block)

# Get top_html up to the first panel
panel_1_idx = content.find('<div class="persona__panel active"')
top_html = content[:panel_1_idx]

# Get everything from Empathize to end
emp_idx = content.find('<!-- ============================== AFFINITY MAP / EMPATHIZE ============================== -->')
empathize_and_after = content[emp_idx:]

import sys
sys.path.append('c:/semester 2/Web UAS')
from rebuild import personas_data, build_table, build_interview

panels_html = ""
for i, name in enumerate(h3_names):
    p_data = personas_data[i]
    is_active = ' active' if i == 0 else ''
    data_attr = f' data-panel="{i}"'
    
    # The comment
    panels_html += f'        <!-- Panel {i+1}: {name} -->\n'
    panels_html += f'        <div class="persona__panel{is_active}"{data_attr}>\n'
    panels_html += '          <div class="persona__grid">\n'
    
    # 1. Base content (Top, Mid, Bottom)
    # the block already has indentation of its own, so we just paste it.
    panels_html += '            ' + extracted_blocks[i] + '\n\n'
    
    # 2. Journey Map
    panels_html += build_table(p_data) + '\n\n'
    
    # 3. Interview Data
    panels_html += build_interview() + '\n'
    
    panels_html += '          </div>\n'
    panels_html += '        </div>\n\n'

new_index = top_html + panels_html + '      </div>\n    </section>\n\n    ' + empathize_and_after

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Rebuilt perfectly preserving head and wrapper.")
