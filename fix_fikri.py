import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fikri is in panels[0] if we split by <div class="persona__panel" data-panel="1">
panels = re.split(r'(<div class="persona__panel" data-panel="1">)', content)
fikri_body = panels[0]

interview_match = re.search(r'(<!-- Interview Data -->.*?)(?=<!-- User Journey Map -->)', fikri_body, re.DOTALL)
if interview_match:
    interview_str = interview_match.group(1)
    # Remove it from its current position
    fikri_body = fikri_body.replace(interview_str, '', 1)
    
    # Now find the end of the Journey Map.
    journey_end_match = re.search(r'(<!-- User Journey Map -->.*?</div>\s*</div>\s*</div>)', fikri_body, re.DOTALL)
    
    if journey_end_match:
        journey_full_str = journey_end_match.group(1)
        # Replace the journey block with itself + interview_str
        fikri_body = fikri_body.replace(journey_full_str, journey_full_str + '\n' + interview_str, 1)

new_content = fikri_body + panels[1] + panels[2]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed Fikri.")
