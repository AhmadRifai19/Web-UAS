"""Check div nesting balance for each persona panel."""
import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', content)]
section_end = content.find('</section>', content.find('class="persona"'))

print(f"Found {len(panel_starts)} panels, section ends at char {section_end}")

for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else section_end
    panel_html = content[start:end]
    
    opens = len(re.findall(r'<div[\s>]', panel_html))
    closes = len(re.findall(r'</div>', panel_html))
    
    name_match = re.search(r'persona__name">([^<]+)', panel_html)
    name = name_match.group(1) if name_match else f"Panel {i}"
    
    has_interview = 'interview__table' in panel_html
    interview_rows = len(re.findall(r'<tr>', panel_html))
    has_journey = 'journey__table' in panel_html
    
    print(f"Panel {i} ({name}): opens={opens}, closes={closes}, diff={opens-closes}")
    print(f"  interview_table={has_interview}, rows={interview_rows}, journey={has_journey}")
