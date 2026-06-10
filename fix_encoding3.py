"""
Fix garbled UTF-8 characters (mojibake) in index.html.
The .bak reconstruction introduced double-encoded emoji characters.
Strategy: Read as UTF-8, replace garbled content inside known HTML tags with SVG icons.
"""
import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File length: {len(content)} chars, lines: {content.count(chr(10))}")

# Count garbled chars before
garbled_before = len(re.findall(r'[\xc0-\xff]', content))
print(f"Non-ASCII chars before fix: {garbled_before}")

# 1. Fix title - replace any non-ASCII dash between MarketSpace and Studi Kasus
content = re.sub(r'MarketSpace\s+.+?\s+Studi Kasus', 'MarketSpace - Studi Kasus', content)

# 2. Fix panel comments - replace garbled box-drawing with ===
for name in ['Fikri Ramadhan', 'Susanto Hari Wibowo', 'Haris Wahyu Ramadhani',
             'Widya Dny Yuanika R', 'Zaskiya Soaldi A']:
    # Match comment containing "Panel N:" with any garbled chars around it
    pattern = r'<!--\s*[^\w]*Panel \d:.*?' + re.escape(name) + r'.*?-->'
    clean_name = name.rstrip('.')
    if 'Widya' in name:
        clean_name = 'Widya Dny Yuanika R.'
    elif 'Zaskiya' in name:
        clean_name = 'Zaskiya Soaldi A.A.'
    replacement = f'<!-- === Panel: {clean_name} === -->'
    found = re.findall(pattern, content)
    if found:
        content = re.sub(pattern, replacement, content)
        print(f"  Fixed comment for {clean_name}")

# 3. Replace ALL persona__avatar spans (garbled emojis) with SVG user icon
svg_avatar = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
              'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
              'stroke-linejoin="round" style="color: var(--text);">'
              '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
              '<circle cx="12" cy="7" r="4"/></svg>')

avatar_count = len(re.findall(r'<span class="persona__avatar">', content))
content = re.sub(
    r'<span class="persona__avatar">[^<]*</span>',
    f'<span class="persona__avatar">{svg_avatar}</span>',
    content
)
print(f"Replaced {avatar_count} persona__avatar spans")

# 4. Replace ALL persona__photo-wrap divs (garbled emojis) with SVG user icon
svg_photo = ('<svg width="40" height="40" viewBox="0 0 24 24" fill="none" '
             'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round" style="color: var(--brand);">'
             '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
             '<circle cx="12" cy="7" r="4"/></svg>')

photo_count = len(re.findall(r'<div class="persona__photo-wrap">', content))
content = re.sub(
    r'<div class="persona__photo-wrap">[^<]*</div>',
    f'<div class="persona__photo-wrap">{svg_photo}</div>',
    content
)
print(f"Replaced {photo_count} persona__photo-wrap divs")

# 5. Fix about section garbled icons with SVGs
# Green icon (was lightning bolt)
content = re.sub(
    r'<div class="about__goal-icon about__goal-icon--green">[^<]*</div>',
    '<div class="about__goal-icon about__goal-icon--green">'
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
    '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>',
    content
)
# Blue icon (was target)
content = re.sub(
    r'<div class="about__goal-icon about__goal-icon--blue">[^<]*</div>',
    '<div class="about__goal-icon about__goal-icon--blue">'
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
    '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></div>',
    content
)
# Brand icon (was leaf)
content = re.sub(
    r'<div class="about__goal-icon about__goal-icon--brand">[^<]*</div>',
    '<div class="about__goal-icon about__goal-icon--brand">'
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
    '<path d="M6 3v12"/><path d="M18 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>'
    '<path d="M6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/><path d="M18 9a9 9 0 0 1-9 9"/></svg></div>',
    content
)
print("Fixed about section icons")

# Count garbled chars after
garbled_after = len(re.findall(r'[\xc0-\xff]', content))
print(f"\nNon-ASCII chars after fix: {garbled_after}")

# Write as proper UTF-8
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! File written. Lines: {content.count(chr(10))}")
