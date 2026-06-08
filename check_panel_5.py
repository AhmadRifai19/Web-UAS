import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

panels = re.split(r'(<div class="persona__panel".*?>)', content)
panel_5_body = panels[10]

print('Interview Data in Panel 5:', '<!-- Interview Data -->' in panel_5_body)
print('User Journey Map in Panel 5:', '<!-- User Journey Map -->' in panel_5_body)
