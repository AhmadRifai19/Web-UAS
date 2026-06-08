import re
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<section class="about" id="features">.*?</section>', content, re.DOTALL)
if match:
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(0))
