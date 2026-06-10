import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Card data: name, color number, story count
cards = [
    ('Zaskiya Sandi A.A.', 1, 9),
    ('Widya Ony Yusnita Rahayu', 2, 14),
    ('Fikri Ramadhan', 3, 9),
    ('Susanto Hari Wibowo', 4, 10),
    ('Haris Ridho Ramadhan', 5, 11),
]

for name, color, count in cards:
    escaped_name = re.escape(name)

    # 1. Add color class to card div
    # Find: <div class="define__card"> or <div class="define__card define__card--full">
    # Right after the name appears in the header
    pattern = re.compile(
        r'(<div class="define__card)(.*?)">\s*'
        r'<div class="define__card-header">\s*'
        r'<div class="define__card-avatar define__card-avatar--' + str(color) + r'">\s*'
        + escaped_name[0] + r'\s*</div>',
        re.DOTALL
    )
    match = pattern.search(content)
    if match:
        existing = match.group(2)
        if f'define__card--{color}' not in existing:
            new_classes = existing + f' define__card--{color}'
            content = content[:match.start()] + match.group(1) + new_classes + '">' + content[match.start(2) + len(existing) + 1:]
            print(f"OK: Added color class to {name}'s card")

    # 2. Add story count badge before closing </div> of card-header
    # Find the card-role paragraph for this person, then add count after it
    count_pattern = re.compile(
        r'(<p class="define__card-role">Narasumber \d+ &mdash; [^<]*</p>\s*'
        r'</div>\s*)'
        r'(</div>\s*'  # closing of card-header
        r'<div class="define__card-body">)',
        re.DOTALL
    )
    # More specific: match by the avatar color to find the right card
    header_pattern = re.compile(
        r'(define__card-avatar--' + str(color) + r'">\s*'
        + escaped_name[0] + r'\s*</div>\s*'
        r'<div class="define__card-info">\s*'
        r'<h3 class="define__card-name">' + escaped_name + r'</h3>\s*'
        r'<p class="define__card-role">[^<]*</p>\s*'
        r'</div>)\s*'
        r'(</div>)',  # closing of card-header
        re.DOTALL
    )
    match2 = header_pattern.search(content)
    if match2:
        count_html = f'\n            <span class="define__card-count">{count} Temuan</span>\n          '
        content = content[:match2.end(1)] + count_html + content[match2.start(2):]
        print(f"OK: Added count badge ({count}) to {name}'s card")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone updating HTML cards!")
