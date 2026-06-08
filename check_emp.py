import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print('Empathize section:', 'id="empathize"' in content)
print('Is Empathize inside a panel?', re.search(r'<div class="persona__panel.*?</section>', content, re.DOTALL) is not None)
