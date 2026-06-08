import re
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<div[^>]*persona__panel[^>]*>', content)
if match:
    idx = match.start()
    print(content[idx-200:idx+100])
else:
    print("No persona panel found!")
