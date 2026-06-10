import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove all badge elements from Define section
# <span class="define__card-badge define__card-badge--X">Name</span>
content = re.sub(
    r'\s*<span class="define__card-badge[^"]*">[^<]*</span>',
    '',
    content
)

# 2. Remove interviewer name from sticky notes
# <span class="define__sticky-interviewer">...</span>
content = re.sub(
    r'\s*<span class="define__sticky-interviewer">[^<]*</span>',
    '',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
badges_left = content.count('define__card-badge')
interviewers_left = content.count('define__sticky-interviewer')
print(f"Badges removed: {badges_left} remaining")
print(f"Interviewer names removed: {interviewers_left} remaining")
print("Done!")
