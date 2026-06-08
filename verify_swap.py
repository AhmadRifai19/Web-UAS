import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

panels = re.split(r'(<div class="persona__panel".*?>)', content)
for i in range(1, len(panels), 2):
    panel_body = panels[i+1]
    
    interview_match = re.search(r'<!-- Interview Data -->', panel_body)
    journey_match = re.search(r'<!-- User Journey Map -->', panel_body)
    
    if interview_match and journey_match:
        print(f'Panel {i//2 + 1}: Interview at {interview_match.start()}, Journey at {journey_match.start()}')
        if interview_match.start() > journey_match.start():
            print('  -> SUCCESS: Interview is AFTER Journey')
        else:
            print('  -> FAILED: Interview is BEFORE Journey')
