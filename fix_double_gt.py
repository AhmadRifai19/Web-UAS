import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix double >> in define cards
content = content.replace('define__card--1">>', 'define__card--1">')
content = content.replace('define__card--full define__card--2">>', 'define__card--full define__card--2">')
content = content.replace('define__card--3">>', 'define__card--3">')
content = content.replace('define__card--4">>', 'define__card--4">')
content = content.replace('define__card--5">>', 'define__card--5">')

# Also fix any remaining double >>
content = re.sub(r'(class="define__card[^"]*")>>', r'\1>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
double_gt = content.count('>>')
print(f"Remaining '>>': {double_gt}")
print("Fixed!")
