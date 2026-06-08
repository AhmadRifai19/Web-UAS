with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Head exists:', '<head>' in content)
print('Personas content exists:', '<div class="personas__content">' in content)
print('Length:', len(content))
