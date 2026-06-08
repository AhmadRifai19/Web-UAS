with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
idx1 = content.find('<section class="persona" id="persona">')
idx2 = content.find('<div class="persona__panel')
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(content[idx1:idx2])
