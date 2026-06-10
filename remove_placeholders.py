import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all interview__qa-item blocks that contain placeholder text
# Pattern matches a Q&A item div containing "[Isi Pertanyaan..."
pattern = re.compile(
    r'\s*<div class="interview__qa-item">\s*'
    r'<div class="interview__sticky--red">\s*'
    r'<strong>Question \d+:</strong><br>\s*'
    r'\[Isi Pertanyaan \d+ di sini\]\s*'
    r'</div>\s*'
    r'<div class="interview__sticky--yellow">\s*'
    r'<strong>Answer:</strong><br>\s*'
    r'\[Isi Jawaban \d+ di sini\]\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)

matches = pattern.findall(content)
print(f"Found {len(matches)} placeholder Q&A items to remove")

content = pattern.sub('', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
remaining = len(re.findall(r'\[Isi (?:Pertanyaan|Jawaban) \d+ di sini\]', content))
print(f"Remaining placeholders: {remaining}")
print("Done!")
