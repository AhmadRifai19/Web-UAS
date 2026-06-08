import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

panels = re.split(r'(<div class="persona__panel".*?>)', content)

for i in range(1, len(panels), 2):
    panel_start = panels[i]
    panel_body = panels[i+1]
    name_match = re.search(r'<h3 class="persona__name">(.*?)</h3>', panel_body)
    name = name_match.group(1) if name_match else 'Unknown'
    
    div_opens = len(re.findall(r'<div\b[^>]*>', panel_body)) + 1 # +1 for panel_start
    div_closes = len(re.findall(r'</div>', panel_body))
    
    print(f'Persona: {name} | Opens: {div_opens} | Closes: {div_closes} | Diff: {div_opens - div_closes}')
