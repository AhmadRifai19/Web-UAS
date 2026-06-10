"""Full structural verification of rebuilt index.html."""
import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = []

# Check overall section balance
sections = ['hero', 'about', 'persona', 'define', 'hmw', 'prioritization', 'design', 'prototype']
for sec in sections:
    start = content.find(f'<section class="{sec}"')
    if start < 0:
        start = content.find(f'id="{sec}"')
        if start < 0: continue
        start = content.rfind('<section', 0, start)
    end = content.find('</section>', start)
    if end < 0: continue
    sec_html = content[start:end + len('</section>')]
    o = len(re.findall(r'<div[\s>]', sec_html))
    c = len(re.findall(r'</div>', sec_html))
    out.append(f"Section {sec}: opens={o}, closes={c}, diff={o-c}")

# Check journey tables
out.append(f"\nJourney tables found: {len(re.findall(r'journey__table', content))}")
out.append(f"Interview tables found: {len(re.findall(r'interview__table', content))}")

# Check panel count
out.append(f"Panels: {len(re.findall(r'persona__panel', content))}")
out.append(f"Tabs: {len(re.findall(r'persona__tab\"', content))}")

# Check no garbled chars remain
garbled = len(re.findall(r'[\xc0-\xff]', content))
out.append(f"Non-ASCII chars: {garbled}")

# Check for SVG icons
out.append(f"SVG icons: {len(re.findall(r'<svg', content))}")

# Check main/container balance
main_start = content.find('<main>')
main_end = content.find('</main>')
if main_start >= 0 and main_end >= 0:
    main_html = content[main_start:main_end]
    o = len(re.findall(r'<div[\s>]', main_html))
    c = len(re.findall(r'</div>', main_html))
    out.append(f"\nMain section: opens={o}, closes={c}, diff={o-c}")

with open('c:/semester 2/Web UAS/verify_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
