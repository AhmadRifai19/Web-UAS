import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for match in re.finditer(r'(<!-- User Journey Map -->.*?)(?=<!-- Interview Data -->|<!-- â• â• â•  Panel)', content, re.DOTALL):
    print("MATCH ENDS WITH:")
    print(match.group(1)[-300:])
    print("="*50)
