with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<div class="persona__panel active">')
if idx != -1:
    print(content[idx-500:idx+100])
