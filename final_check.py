import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = []

# Tabs check
tabs = re.findall(r'class="persona__tab[^"]*"\s+data-index="(\d+)"', content)
out.append(f"Tabs found: {len(tabs)} with data-index values: {tabs}")

# Journey check
out.append(f"persona__journey-row: {content.count('persona__journey-row')}")
out.append(f"persona__journey-table-wrapper: {content.count('persona__journey-table-wrapper')}")

# Non-ASCII
non_ascii = [(i, ch, hex(ord(ch))) for i, ch in enumerate(content) if ord(ch) > 127]
out.append(f"\nNon-ASCII chars ({len(non_ascii)} total):")
for i, ch, h in non_ascii:
    line = content[:i].count('\n') + 1
    context = content[max(0,i-10):i+10].replace('\n', '\\n')
    out.append(f"  Line {line}: char={h} context='{context}'")

with open('c:/semester 2/Web UAS/final_check.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
