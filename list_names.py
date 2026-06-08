import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'<h3 class="persona__name">(.*?)</h3>', content)
for m in matches:
    print(m.group(1))
