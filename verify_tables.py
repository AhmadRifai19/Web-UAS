import re

c = open('index.html', 'r', encoding='utf-8').read()

# Count rows in each interview table
tables = list(re.finditer(r'interview__table-wrapper', c))
print(f"Interview tables found: {len(tables)}")

panels = ['Fikri Ramadhan', 'Susanto Hari Wibowo', 'Haris Ridho Ramadhan', 'Widya Ony', 'Zaskiya Sandi']

for i, t in enumerate(tables):
    # Find the table content
    table_start = t.start()
    table_end = c.find('</table>', table_start)
    table_content = c[table_start:table_end]
    row_count = table_content.count('<tr>')
    name = panels[i] if i < len(panels) else f'Panel {i}'
    print(f"  {name}: {row_count} Q&A")

total = sum(c[t.start():c.find('</table>', t.start())].count('<tr>') for t in tables)
print(f"\nTotal Q&A rows: {total}")
