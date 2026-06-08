import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print('Interview Data tags:', content.count('<!-- Interview Data -->'))
print('User Journey Map tags:', content.count('<!-- User Journey Map -->'))

panels = re.split(r'(<div class="persona__panel" data-panel="\d+">)', content)
print('Found panels:', len(panels)//2)

for i in range(1, len(panels), 2):
    panel_body = panels[i+1]
    
    interview_match = re.search(r'(<!-- Interview Data -->.*?)(?=<!-- User Journey Map -->)', panel_body, re.DOTALL)
    if interview_match:
        print(f'Panel {i//2 + 1}: Interview data is BEFORE journey map.')
    else:
        # Maybe it's after?
        interview_after = re.search(r'<!-- User Journey Map -->.*?<!-- Interview Data -->', panel_body, re.DOTALL)
        if interview_after:
            print(f'Panel {i//2 + 1}: Interview data is AFTER journey map.')
        else:
            print(f'Panel {i//2 + 1}: Interview data NOT FOUND.')

    journey_match = re.search(r'(<!-- User Journey Map -->.*?</table>\s*</div>\s*</div>\s*</div>)', panel_body, re.DOTALL)
    if not journey_match:
        print(f'Panel {i//2 + 1}: Journey match failed. Let\'s check the end of the block.')
        journey_match2 = re.search(r'(<!-- User Journey Map -->.*?</div>\s*</div>\s*</div>)', panel_body, re.DOTALL)
        if journey_match2:
            print(f'Panel {i//2 + 1}: Journey match succeeded without table.')
