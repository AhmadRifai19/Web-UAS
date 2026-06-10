import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Build original placeholder Q&A items
def build_placeholder():
    items = []
    for i in range(1, 11):
        items.append(f'''                  <div class="interview__qa-item">
                    <div class="interview__sticky--red">
                      <strong>Question {i}:</strong><br>
                      [Isi Pertanyaan {i} di sini]
                    </div>
                    <div class="interview__sticky--yellow">
                      <strong>Answer:</strong><br>
                      [Isi Jawaban {i} di sini]
                    </div>
                  </div>''')
    return '\n'.join(items)

placeholder_html = build_placeholder()

# Find all interview grids and replace with placeholders
pattern = r'(<div class="persona__interview-grid">\s*)(.*?)(\s*</div>\s*</div>\s*</div>)'
count = 0

def replacer(match):
    global count
    count += 1
    return match.group(1) + '\n' + placeholder_html + '\n' + match.group(3)

content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Reverted {count} interview grids to placeholders.")
