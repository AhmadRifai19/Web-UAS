html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Count overall opens/closes
opens = len(re.findall(r'<div[\s>]', content))
closes = content.count('</div>')
print(f"Overall: opens={opens}, closes={closes}, diff={opens-closes}")

# Check per-panel
for i in range(5):
    # Find panel start
    panel_start_marker = f'data-panel="{i}"'
    start = content.find(panel_start_marker)
    if start == -1:
        print(f"Panel {i}: NOT FOUND")
        continue
    # Find next panel or end of section
    if i < 4:
        next_marker = f'data-panel="{i+1}"'
        end = content.find(next_marker, start + 1)
    else:
        end = content.find('<!-- Define Problem Statement', start)
    
    panel_html = content[start:end]
    p_opens = len(re.findall(r'<div[\s>]', panel_html))
    p_closes = panel_html.count('</div>')
    
    # Also count journey tables in this panel
    has_journey = 'persona__journey-table' in panel_html
    has_interview = 'interview__table' in panel_html
    
    print(f"Panel {i}: opens={p_opens}, closes={p_closes}, diff={p_opens-p_closes}, journey={has_journey}, interview={has_interview}")

# Check persona section
persona_start = content.find('id="persona"')
persona_end = content.find('<!-- Define Problem Statement', persona_start)
persona_html = content[persona_start:persona_end]
ps_opens = len(re.findall(r'<div[\s>]', persona_html))
ps_closes = persona_html.count('</div>')
print(f"\nPersona section: opens={ps_opens}, closes={ps_closes}, diff={ps_opens-ps_closes}")
