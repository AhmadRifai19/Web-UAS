import re

c = open('index.html', 'r', encoding='utf-8').read()

# Check all panels exist
print("Panel 1 (Fikri):", 'data-panel="0"' in c)
print("Panel 2 (Susanto):", 'data-panel="1"' in c)
print("Panel 3 (Haris):", 'data-panel="2"' in c)
print("Panel 4 (Widya):", 'data-panel="3"' in c)
print("Panel 5 (Zaskiya):", 'data-panel="4"' in c)

# Check interview tables
tables = list(re.finditer(r'class="interview__table-wrapper"', c))
print(f"\nInterview tables: {len(tables)}")

for i, t in enumerate(tables):
    table_start = t.start()
    table_end = c.find('</table>', table_start)
    table_content = c[table_start:table_end]
    row_count = table_content.count('<tr>')
    names = ['Fikri', 'Susanto', 'Haris', 'Widya', 'Zaskiya']
    print(f"  {names[i]}: {row_count} Q&A")

# Check closing structure
print(f"\nDefine section: {'class=\"define\"' in c}")
print(f"</section> count: {c.count('</section>')}")

# Check persona section closing
persona_end = c.find('</section>', c.find('class="persona"'))
define_start = c.find('<section class="define"')
between = c[persona_end:define_start]
print(f"Between persona end and define: {repr(between[:80])}")
