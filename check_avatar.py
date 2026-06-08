with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
idx = content.find('<span class="persona__avatar">')
if idx != -1:
    print(content[idx:idx+350])
