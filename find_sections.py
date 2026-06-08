import re
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<section class="(hero|about)[^>]*>.*?</section>', content, re.DOTALL)
if match:
    print('Found section:', match.group(0)[:800])
