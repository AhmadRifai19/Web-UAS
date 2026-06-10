"""
Fix all garbled UTF-8 characters in index.html that came from the .bak file.
The .bak file has mojibake - UTF-8 bytes reinterpreted as Windows-1252/Latin-1.
"""

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all known mojibake patterns
replacements = {
    # Em dash
    'â€"': '\u2014',  # —
    # Box drawing characters in comments
    'â•"': '\u2550',  # ═
    'â•': '\u2550',   # ═
    'â•—': '\u2550',  # ═
    'â•˜': '\u2550',  # ═
    'â•™': '\u2550',  # ═
    'â•š': '\u2550',  # ═
    'â•›': '\u2550',  # ═
    'â•œ': '\u2550',  # ═
    # Emoji: ⚡ (high voltage)
    'âš¡': '\u26A1',
    # Emoji: 🎯 (dart)
    'ðŸŽ¯': '\U0001F3AF',
    # Emoji: 🌿 (herb)
    'ðŸŒ¿': '\U0001F33F',
    # Emoji: 👩‍💼 (woman office worker)
    'ðŸ'©â€\u008dðŸ'¼': '\U0001F469\u200D\U0001F4BC',
    # Emoji: 👨‍💼 (man office worker)
    'ðŸ'¨â€\u008dðŸ'¼': '\U0001F468\u200D\U0001F4BC',
    # Emoji: 👨‍🎨 (man artist)
    'ðŸ'¨â€\u008dðŸŽ¨': '\U0001F468\u200D\U0001F3A8',
    # Emoji: 👩‍🎓 (woman student)
    'ðŸ'©â€\u008dðŸŽ"': '\U0001F469\u200D\U0001F393',
    # Emoji: 👩‍💻 (woman technologist)
    'ðŸ'©â€\u008dðŸ'»': '\U0001F469\u200D\U0001F4BB',
}

count = 0
for garbled, correct in replacements.items():
    if garbled in content:
        old_count = content.count(garbled)
        content = content.replace(garbled, correct)
        count += old_count
        print(f"  Fixed {old_count}x: {repr(garbled)} -> {repr(correct)}")

# Additional: fix the panel comment lines which have garbled box-drawing chars
# Pattern: <!-- â•"â•"â•" Panel X: Name â•"â•"â•" -->
# Replace with: <!-- === Panel X: Name === -->
import re
content = re.sub(
    r'<!-- [═\u2550]+ Panel (\d+): ([^=]+) [═\u2550]+ -->',
    r'<!-- === Panel \1: \2 === -->',
    content
)

# Also fix any remaining garbled patterns with a broader approach
# Replace the specific panel comments
panel_comments = [
    ('Panel 1: Fikri Ramadhan', '<!-- === Panel 1: Fikri Ramadhan === -->'),
    ('Panel 2: Susanto Hari Wibowo', '<!-- === Panel 2: Susanto Hari Wibowo === -->'),
    ('Panel 3: Haris Wahyu Ramadhani', '<!-- === Panel 3: Haris Wahyu Ramadhani === -->'),
    ('Panel 4: Widya Dny Yuanika R.', '<!-- === Panel 4: Widya Dny Yuanika R. === -->'),
    ('Panel 5: Zaskiya Soaldi A.A.', '<!-- === Panel 5: Zaskiya Soaldi A.A. === -->'),
]

for panel_text, correct_comment in panel_comments:
    # Find any garbled version of this comment
    pattern = re.compile(r'<!-- [^>]*' + re.escape(panel_text) + r'[^>]*-->')
    match = pattern.search(content)
    if match and match.group() != correct_comment:
        content = content[:match.start()] + correct_comment + content[match.end():]
        print(f"  Fixed panel comment: {panel_text}")

# Use SVG icons instead of emojis for persona avatars (more reliable)
# Replace emoji avatars with simple SVG user icons
avatar_replacements = [
    ('<span class="persona__avatar">\U0001F469\u200D\U0001F4BC</span>',
     '<span class="persona__avatar"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>'),
    ('<span class="persona__avatar">\U0001F468\u200D\U0001F4BC</span>',
     '<span class="persona__avatar"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>'),
    ('<span class="persona__avatar">\U0001F468\u200D\U0001F3A8</span>',
     '<span class="persona__avatar"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>'),
    ('<span class="persona__avatar">\U0001F469\u200D\U0001F393</span>',
     '<span class="persona__avatar"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>'),
    ('<span class="persona__avatar">\U0001F469\u200D\U0001F4BB</span>',
     '<span class="persona__avatar"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>'),
]

for old, new in avatar_replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"  Fixed avatar emoji")

# Fix photo-wrap divs that have emojis
photo_emoji_fixes = [
    ('<div class="persona__photo-wrap">\U0001F469\u200D\U0001F4BC</div>',
     '<div class="persona__photo-wrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>'),
    ('<div class="persona__photo-wrap">\U0001F468\u200D\U0001F4BC</div>',
     '<div class="persona__photo-wrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>'),
    ('<div class="persona__photo-wrap">\U0001F468\u200D\U0001F3A8</div>',
     '<div class="persona__photo-wrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>'),
    ('<div class="persona__photo-wrap">\U0001F469\u200D\U0001F393</div>',
     '<div class="persona__photo-wrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>'),
    ('<div class="persona__photo-wrap">\U0001F469\u200D\U0001F4BB</div>',
     '<div class="persona__photo-wrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>'),
]

for old, new in photo_emoji_fixes:
    if old in content:
        content = content.replace(old, new)
        print(f"  Fixed photo-wrap emoji")

# Fix about section icons
about_fixes = [
    ('<div class="about__goal-icon about__goal-icon--green">\u26A1</div>',
     '<div class="about__goal-icon about__goal-icon--green"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>'),
    ('<div class="about__goal-icon about__goal-icon--blue">\U0001F3AF</div>',
     '<div class="about__goal-icon about__goal-icon--blue"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg></div>'),
    ('<div class="about__goal-icon about__goal-icon--brand">\U0001F33F</div>',
     '<div class="about__goal-icon about__goal-icon--brand"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 3v12"></path><path d="M18 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path><path d="M6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path><path d="M18 9a9 9 0 0 1-9 9"></path></svg></div>'),
]

for old, new in about_fixes:
    if old in content:
        content = content.replace(old, new)
        print(f"  Fixed about section icon")

# Fix title em dash
content = content.replace('MarketSpace \u2014 Studi Kasus', 'MarketSpace - Studi Kasus')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal fixes applied: {count}")
print("Encoding fixes complete!")
