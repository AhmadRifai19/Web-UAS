with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    content = f.read()

import re
match = re.search(r'<div[^>]*personas__content[^>]*>', content)
if match:
    print('Found tag:', match.group(0))
else:
    print('personas__content not found!')
