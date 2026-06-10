"""
Fix garbled UTF-8 characters in index.html using byte-level replacement.
The .bak file has mojibake from encoding mismatch.
"""
import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'rb') as f:
    raw = f.read()

# Common mojibake patterns (UTF-8 bytes interpreted as Latin-1 then re-encoded as UTF-8)
# We fix at the byte level

# Fix em dash: â€" -> —
raw = raw.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x94', b'\xe2\x80\x94')
# Simpler: just replace the visible garbled text
raw = raw.replace('â€"'.encode('utf-8'), '—'.encode('utf-8'))

# Fix all panel comments with garbled box-drawing chars
# Replace any garbled comment with clean version
panel_patterns = [
    (b'Panel 1: Fikri Ramadhan', b'<!-- === Panel 1: Fikri Ramadhan === -->'),
    (b'Panel 2: Susanto Hari Wibowo', b'<!-- === Panel 2: Susanto Hari Wibowo === -->'),
    (b'Panel 3: Haris Wahyu Ramadhani', b'<!-- === Panel 3: Haris Wahyu Ramadhani === -->'),
    (b'Panel 4: Widya', b'<!-- === Panel 4: Widya Dny Yuanika R. === -->'),
    (b'Panel 5: Zaskiya', b'<!-- === Panel 5: Zaskiya Soaldi A.A. === -->'),
]

for search_bytes, replacement in panel_patterns:
    # Find the HTML comment containing this panel text
    idx = raw.find(search_bytes)
    if idx > 0:
        # Find the <!-- before and --> after
        comment_start = raw.rfind(b'<!--', 0, idx)
        comment_end = raw.find(b'-->', idx) + 3
        if comment_start >= 0 and comment_end > 3:
            old_comment = raw[comment_start:comment_end]
            if old_comment != replacement:
                raw = raw[:comment_start] + replacement + raw[comment_end:]
                print(f"  Fixed comment: {search_bytes.decode('utf-8', errors='replace')}")

# Now decode to string and fix remaining issues with string replacements
content = raw.decode('utf-8')

# Replace ALL garbled emoji/avatar spans with SVG icons
# The garbled emojis look like: ðŸ'©â€ðŸ'¼ etc.
# Use regex to match any non-ASCII characters inside persona__avatar spans
content = re.sub(
    r'<span class="persona__avatar">[^<]*</span>',
    '<span class="persona__avatar"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>',
    content
)

# Replace garbled emojis in persona__photo-wrap divs
content = re.sub(
    r'<div class="persona__photo-wrap">[^<]*</div>',
    '<div class="persona__photo-wrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>',
    content
)

# Fix about section garbled icons
content = re.sub(
    r'<div class="about__goal-icon about__goal-icon--green">[^<]*</div>',
    '<div class="about__goal-icon about__goal-icon--green"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>',
    content
)
content = re.sub(
    r'<div class="about__goal-icon about__goal-icon--blue">[^<]*</div>',
    '<div class="about__goal-icon about__goal-icon--blue"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg></div>',
    content
)
content = re.sub(
    r'<div class="about__goal-icon about__goal-icon--brand">[^<]*</div>',
    '<div class="about__goal-icon about__goal-icon--brand"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 3v12"></path><path d="M18 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path><path d="M6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path><path d="M18 9a9 9 0 0 1-9 9"></path></svg></div>',
    content
)

# Fix title
content = content.replace('MarketSpace \u2014 Studi Kasus', 'MarketSpace - Studi Kasus')
# Also fix the mojibake version if still present
content = re.sub(r'MarketSpace [^\s]* Studi Kasus', 'MarketSpace - Studi Kasus', content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
remaining_garbled = len(re.findall(r'[Ã¢ÂðŸâ€˜¨©¼Â]', content))
print(f"\nDone! Remaining potential garbled chars: {remaining_garbled}")
print(f"Total lines: {content.count(chr(10))}")
