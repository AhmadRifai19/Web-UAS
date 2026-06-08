import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I want to find each persona panel and swap the Interview Data with User Journey Map.
panels = re.split(r'(<div class="persona__panel" data-panel="\d+">)', content)

new_content = panels[0]

count = 0
for i in range(1, len(panels), 2):
    panel_start = panels[i]
    panel_body = panels[i+1]
    
    # We look for the interview data and user journey map
    # The structure:
    # <!-- Interview Data -->
    # ...
    # <!-- User Journey Map -->
    # ...
    
    interview_match = re.search(r'(<!-- Interview Data -->.*?)(?=<!-- User Journey Map -->)', panel_body, re.DOTALL)
    journey_match = re.search(r'(<!-- User Journey Map -->.*?</table>\s*</div>\s*</div>\s*</div>)', panel_body, re.DOTALL)
    
    if interview_match and journey_match:
        interview_str = interview_match.group(1)
        journey_str = journey_match.group(1)
        
        # Original block
        original_chunk = interview_str + journey_str
        
        # New block
        new_chunk = journey_str + '\n' + interview_str
        
        # Replace only the first occurrence in this panel body
        panel_body = panel_body.replace(original_chunk, new_chunk, 1)
        count += 1
        
    new_content += panel_start + panel_body

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Swapped {count} blocks.')
else:
    print('No blocks swapped.')
