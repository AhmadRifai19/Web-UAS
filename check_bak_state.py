c = open('index.html.bak', 'r', encoding='utf-8').read()
print('BAK - Total lines:', c.count('\n'))
print('BAK - Panel 5:', 'Panel 5' in c)
print('BAK - Zaskiya:', 'data-panel="4"' in c)
print('BAK - Zaskiya journey:', 'ZASKIYA SOALDI' in c)

import re
markers = [m.start() for m in re.finditer(r'<!-- Interview Data -->', c)]
print(f'BAK - Interview Data markers: {len(markers)}')
