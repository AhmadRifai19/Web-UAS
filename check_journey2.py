import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = []
out.append(f"persona__journey-row: {content.count('persona__journey-row')}")
out.append(f"persona__journey-table-wrapper: {content.count('persona__journey-table-wrapper')}")

# Check each panel
panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', content)]
for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else content.find('</section>', start)
    html = content[start:end]
    has_journey_row = 'persona__journey-row' in html
    has_journey_wrapper = 'persona__journey-table-wrapper' in html
    has_interview = 'interview__table' in html
    
    # Count div balance
    o = len(re.findall(r'<div[\s>]', html))
    c = len(re.findall(r'</div>', html))
    
    nm = re.search(r'persona__name">([^<]+)', html)
    n = nm.group(1) if nm else f'P{i}'
    out.append(f"P{i} ({n}): diff={o-c}, journey_row={has_journey_row}, journey_wrap={has_journey_wrapper}, interview={has_interview}")

with open('c:/semester 2/Web UAS/journey_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
