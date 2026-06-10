import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match each interview grid with its Q&A items
# Captures the inner content of persona__interview-grid
grid_pattern = re.compile(
    r'(<div class="persona__interview-grid">)\s*\n'
    r'(.*?)'
    r'\n\s*(</div>\s*</div>\s*</div>\s*</div>)',
    re.DOTALL
)

# Pattern to match individual Q&A items
qa_pattern = re.compile(
    r'<div class="interview__qa-item">\s*'
    r'<div class="interview__sticky--red">\s*'
    r'<strong>Question (\d+):</strong><br>\s*'
    r'(.*?)\s*'
    r'</div>\s*'
    r'<div class="interview__sticky--yellow">\s*'
    r'<strong>Answer:</strong><br>\s*'
    r'(.*?)\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)

all_matches = list(grid_pattern.finditer(content))
print(f"Found {len(all_matches)} interview grids")

# Process from last to first to avoid position shifting
for match in reversed(all_matches):
    grid_open = match.group(1)
    grid_inner = match.group(2)
    grid_close = match.group(3)
    
    # Extract all Q&A pairs from this grid
    qa_items = qa_pattern.findall(grid_inner)
    
    if not qa_items:
        print(f"  WARNING: No Q&A items found in grid at pos {match.start()}")
        continue
    
    # Build table HTML
    rows = []
    for q_num, q_text, a_text in qa_items:
        # Clean up whitespace
        q_text = re.sub(r'\s+', ' ', q_text.strip())
        a_text = re.sub(r'\s+', ' ', a_text.strip())
        row = f'''                    <tr>
                      <th>Question {q_text}</th>
                      <td>{a_text}</td>
                    </tr>'''
        rows.append(row)
    
    table_html = f'''{grid_open}
                <div class="interview__table-wrapper">
                  <table class="interview__table">
                    <tbody>
{chr(10).join(rows)}
                    </tbody>
                  </table>
                </div>
              {grid_close}'''
    
    content = content[:match.start()] + table_html + content[match.end():]
    print(f"  OK: Converted grid with {len(qa_items)} Q&A items at pos {match.start()}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! All interview grids converted to table format.")
