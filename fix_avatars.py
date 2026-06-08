import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Default user avatar SVG (small for tabs)
tab_svg = '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);">
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
  <circle cx="12" cy="7" r="4"></circle>
</svg>'''

# Default user avatar SVG (large for profile picture)
profile_svg = '''<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);">
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
  <circle cx="12" cy="7" r="4"></circle>
</svg>'''

# Replace all <span class="persona__avatar">...</span> with the tab SVG
new_content = re.sub(r'<span class="persona__avatar">.*?</span>', f'<span class="persona__avatar">{tab_svg}</span>', content, flags=re.DOTALL)

# Replace all <div class="persona__photo-wrap">...</div> with the profile SVG
new_content = re.sub(r'<div class="persona__photo-wrap">.*?</div>', f'<div class="persona__photo-wrap">{profile_svg}</div>', new_content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Avatars replaced successfully!")
