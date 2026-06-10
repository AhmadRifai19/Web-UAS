import re

with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()

out = []
out.append(f"journey__table occurrences: {bak.count('journey__table')}")
out.append(f"journey__table-wrapper: {bak.count('journey__table-wrapper')}")
out.append(f"persona__journey-row: {bak.count('persona__journey-row')}")
out.append(f"persona__journey-table-wrapper: {bak.count('persona__journey-table-wrapper')}")

# Check each panel for journey content
panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', bak)]
for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else len(bak)
    html = bak[start:end]
    has_journey_row = 'persona__journey-row' in html
    has_journey_table = 'journey__table' in html
    has_journey_wrapper = 'journey' in html.lower()
    out.append(f"Panel {i}: journey_row={has_journey_row}, journey_table={has_journey_table}, any_journey={has_journey_wrapper}")

with open('c:/semester 2/Web UAS/journey_check.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
