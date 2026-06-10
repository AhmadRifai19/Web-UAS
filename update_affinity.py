# -*- coding: utf-8 -*-
"""
update_affinity.py - Replace Affinity Map using marker-based approach
"""
import re

src = r'c:\semester 2\Web UAS\index.html'
with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

# Column color classes (matching existing CSS)
# c1=green, c2=blue, c3=green-light/teal, c4=purple, c5=orange, c6=pink/red
COL = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']

# ---- HEADERS (6 categories) ----
header_items = [
    ('Main Problem', True),
    ('Visibilitas Stok', False),
    ('Pemasaran &amp; Literasi Digital', False),
    ('Reputasi &amp; Kepercayaan', False),
    ('UI/UX &amp; Navigasi Aplikasi', False),
    ('Stabilitas Transaksi', False),
]

# ---- INSIGHT (1 row x 6 cols) ----
insights = [
    'User mengelola seluruh operasional warung sendiri setiap hari secara mandiri.',
    'User rutin mengecek serta menata stok barang di toko dan gudang.',
    'User masih mengandalkan promosi secara langsung dan melalui WhatsApp.',
    'User khawatir ulasan negatif dapat memengaruhi performa toko dan kepercayaan pelanggan.',
    'User merasa tampilan aplikasi yang terlalu ramai membuat navigasi sulit dipahami.',
    'User membatalkan pembelian karena ongkos kirim mahal, stok habis, atau error pembayaran.',
]

# ---- PROBLEM ROWS (4 rows x 6 cols) ----
problem_rows = [
    [
        'User mengelola seluruh operasional warung sendiri setiap hari secara mandiri.',
        'User rutin mengecek serta menata stok barang di toko dan gudang.',
        'User masih mengandalkan promosi secara langsung dan melalui WhatsApp.',
        'User khawatir ulasan negatif dapat memengaruhi performa toko dan kepercayaan pelanggan.',
        'User merasa tampilan aplikasi yang terlalu ramai membuat navigasi sulit dipahami.',
        'User membatalkan pembelian karena ongkos kirim mahal, stok habis, atau error pembayaran.',
    ],
    [
        'User memiliki aktivitas operasional toko yang padat setiap hari.',
        'User sering mengalami kesalahan dalam memperkirakan jumlah stok barang.',
        'User belum memahami cara menjangkau pelanggan lebih luas secara efektif di platform digital.',
        'User mencari ulasan pembeli lain untuk memastikan kualitas produk.',
        'User sering terganggu oleh komentar, stiker, dan pop-up saat menonton live streaming.',
        'User pernah mengalami kendala sistem yang menyebabkan transaksi gagal.',
    ],
    [
        'User mengalami kesulitan membagi waktu antara revisi klien dan tugas kuliah.',
        'User merasa khawatir ketika barang yang dicari pelanggan tidak tersedia.',
        'User membutuhkan panduan penggunaan platform saat mulai berjualan jasa.',
        'User pernah mengalami pengalaman buruk ketika kualitas barang tidak sesuai dengan promosi penjual.',
        'User kesulitan melihat detail produk karena tampilan layar terlalu ramai.',
        'User mengharapkan proses pencarian, pembayaran, dan checkout yang cepat serta mudah digunakan.',
    ],
    [
        'User membutuhkan aplikasi untuk memantau stok barang dan harga supplier secara akurat.',
        'User menginginkan aplikasi sederhana untuk membantu menjangkau pelanggan baru.',
        'User menginginkan pengawasan produk yang lebih ketat agar mengurangi barang yang mengecewakan pembeli.',
        'User mengalami kesulitan mencari barang di keranjang belanja yang terlalu panjang.',
        'User mengalami kesulitan mencari barang di keranjang belanja yang terlalu panjang.',
        '',
    ],
]

# ---- Build HTML blocks ----
def build_headers():
    lines = ['<div class="affinity__headers">']
    for title, is_main in header_items:
        cls = ' affinity__header--main' if is_main else ''
        lines.append(f'<div class="affinity__header{cls}">{title}</div>')
    lines.append('</div>')
    return '\n'.join(lines)

def build_insight():
    lines = ['<div class="affinity__box affinity__box--insight">',
             '<div class="affinity__box-badge affinity__box-badge--insight">Insight</div>',
             '<div class="affinity__row affinity__row--6col">']
    for text in insights:
        lines.append(f'<div class="affinity__note affinity__note--dark">{text}</div>')
    lines.extend(['</div>', '</div>'])
    return '\n'.join(lines)

def build_problem():
    lines = ['<div class="affinity__box affinity__box--problem">',
             '<div class="affinity__box-badge affinity__box-badge--problem">Problem</div>', '']
    for i, row in enumerate(problem_rows, 1):
        lines.append(f'<!-- Problem Row {i} -->')
        lines.append('<div class="affinity__row affinity__row--6col">')
        for col, text in enumerate(row):
            if text:
                lines.append(f'<div class="affinity__note affinity__note--{COL[col]}">{text}</div>')
            else:
                lines.append('<div class="affinity__note affinity__note--empty"></div>')
        lines.extend(['</div>', ''])
    lines.append('</div>')
    return '\n'.join(lines)

def build_legend():
    return '''<div class="affinity__legend">
<span class="affinity__legend-title">Keterangan:</span>
<span class="affinity__legend-pill" style="background:#4CAF50;">Fikri Ramadhan</span>
<span class="affinity__legend-pill" style="background:#2196F3;">Susanto Hari Wibowo</span>
<span class="affinity__legend-pill" style="background:#9C27B0;">Haris Ridho Ramadhan</span>
<span class="affinity__legend-pill" style="background:#FF9800;">Zaskiya Sandi A.A</span>
<span class="affinity__legend-pill" style="background:#607D8B;">Widya Ony Yusnita Rahayu</span>
</div>'''

# ---- REPLACE using unique markers ----

# 1. Replace headers: from BOX 1 comment to closing </div> of affinity__headers
m = re.search(r'(<!-- ===== BOX 1:.*?-->).*?(<!-- ===== BOX 2:)', html, re.DOTALL)
if m:
    new_block = m.group(1) + '\n' + build_headers() + '\n\n            ' + m.group(2)
    html = html[:m.start()] + new_block + html[m.end():]
    print('1. Headers replaced')
else:
    print('ERROR: Headers not found')

# 2. Replace insight box: from BOX 2 comment to BOX 3 comment
m = re.search(r'(<!-- ===== BOX 2:.*?-->).*?(<!-- ===== BOX 3:)', html, re.DOTALL)
if m:
    new_block = m.group(1) + '\n' + build_insight() + '\n\n            ' + m.group(2)
    html = html[:m.start()] + new_block + html[m.end():]
    print('2. Insight replaced')
else:
    print('ERROR: Insight not found')

# 3. Replace problem box: from BOX 3 comment to closing </div> before legend
m = re.search(r'(<!-- ===== BOX 3:.*?-->).*?(</div>\s*</div>\s*\n\s*<!-- Legend)', html, re.DOTALL)
if m:
    new_block = m.group(1) + '\n' + build_problem() + '\n\n          ' + m.group(2)
    html = html[:m.start()] + new_block + html[m.end():]
    print('3. Problem replaced')
else:
    print('ERROR: Problem not found')

# 4. Replace legend
m = re.search(r'<div class="affinity__legend">.*?</div>', html, re.DOTALL)
if m:
    html = html[:m.start()] + build_legend() + html[m.end():]
    print('4. Legend replaced')
else:
    print('ERROR: Legend not found')

# ---- Add CSS for 6-col if not present ----
if 'affinity__row--6col' not in html:
    print('WARNING: CSS class affinity__row--6col needs to be added to style.css')

with open(src, 'w', encoding='utf-8') as f:
    f.write(html)
print('\nDone!')
