"""Check .bak file panel structure."""
import re

try:
    with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
        content = f.read()
    print("Read as UTF-8 OK")
except UnicodeDecodeError as e:
    print(f"UTF-8 error: {e}, trying latin-1...")
    with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='latin-1') as f:
        content = f.read()

panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', content)]
section_end = content.find('</section>', content.find('class="persona"'))

print(f"BAK: {len(panel_starts)} panels, section_end={section_end}")

for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else section_end
    panel_html = content[start:end]
    
    opens = len(re.findall(r'<div[\s>]', panel_html))
    closes = len(re.findall(r'</div>', panel_html))
    
    name_match = re.search(r'persona__name">([^<]+)', panel_html)
    name = name_match.group(1) if name_match else f"Panel {i}"
    
    has_sticky = 'interview__qa-list' in panel_html
    has_table = 'interview__table' in panel_html
    has_journey = 'journey__table' in panel_html or 'persona__journey-row' in panel_html
    
    print(f"Panel {i} ({name}): opens={opens}, closes={closes}, diff={opens-closes}")
    print(f"  sticky={has_sticky}, table={has_table}, journey={has_journey}")

# Overall persona section
persona_start = content.find('<section class="persona"')
persona_end = content.find('</section>', persona_start) + len('</section>')
persona_html = content[persona_start:persona_end]
opens = len(re.findall(r'<div[\s>]', persona_html))
closes = len(re.findall(r'</div>', persona_html))
print(f"\nPersona section total: opens={opens}, closes={closes}, diff={opens-closes}")
