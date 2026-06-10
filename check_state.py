c = open('index.html', 'r', encoding='utf-8').read()
print('Panel 5 present:', 'Panel 5' in c)
print('Zaskiya panel:', 'data-panel="4"' in c)
print('Define section:', 'class="define"' in c)
print('Total lines:', c.count('\n'))

# Check if interview data exists for Zaskiya
import re
markers = [m.start() for m in re.finditer(r'<!-- Interview Data -->', c)]
print(f'Interview Data markers: {len(markers)}')

# Check Zaskiya journey table
print('Zaskiya journey:', 'ZASKIYA SOALDI' in c)
