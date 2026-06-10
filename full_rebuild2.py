"""
Complete rebuild of persona section from .bak with:
1. Fixed div nesting (remove extra </div> per panel)
2. Interview data as tables instead of sticky notes
3. SVG icons instead of garbled emojis
"""
import re

# Read .bak file
with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()

# Read current index.html
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    current = f.read()

# === STEP 1: Extract persona section from .bak ===
persona_start = bak.find('<section class="persona"')
persona_section_end = bak.find('</section>', persona_start) + len('</section>')

# Get everything before persona section and after tabs
tabs_end_marker = '</div>\n'  # after persona__tabs closing

# === STEP 2: Extract each panel and fix structure ===
panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', bak)]

# For each panel, extract HTML and count nesting
panels_data = []
for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else persona_section_end
    html = bak[start:end]
    
    # Count opens to determine correct depth
    opens = len(re.findall(r'<div[\s>]', html))
    closes = len(re.findall(r'</div>', html))
    extra_closes = closes - opens
    
    # Remove extra </div> from the END
    if extra_closes > 0:
        # Remove last `extra_closes` occurrences of </div>
        for _ in range(extra_closes):
            last_close = html.rfind('</div>')
            if last_close >= 0:
                # Remove this </div> and any whitespace around it
                # Find the line containing this </div>
                line_start = html.rfind('\n', 0, last_close) + 1
                line_end = html.find('\n', last_close)
                if line_end == -1:
                    line_end = len(html)
                line = html[line_start:line_end]
                if line.strip() == '</div>':
                    html = html[:line_start] + html[line_end:]
                else:
                    html = html[:last_close] + html[last_close + len('</div>'):]
    
    # Verify
    new_opens = len(re.findall(r'<div[\s>]', html))
    new_closes = len(re.findall(r'</div>', html))
    name_match = re.search(r'persona__name">([^<]+)', html)
    name = name_match.group(1) if name_match else f'Panel {i}'
    
    panels_data.append({
        'html': html,
        'opens': new_opens,
        'closes': new_closes,
        'diff': new_opens - new_closes,
        'name': name,
        'extra_removed': extra_closes
    })

# === STEP 3: Replace interview sticky notes with tables ===
all_interview_data = [
    # Panel 0: Fikri Ramadhan (10 Q&A)
    [
        ("Bisakah perkenalkan diri Anda secara singkat? (Nama, usia, dan pekerjaan)",
         "Nama saya Fikri Ramadhan, usia 21 tahun, menjalankan usaha kecil di bidang penjualan produk secara online."),
        ("Bisa ceritakan aktivitas sehari-hari Anda dan kapasitas bisnis Anda mengelola usaha?",
         "Sehari-hari saya mengelola usaha, seperti menyiapkan produk, melayani pelanggan, dan promosi. Saya biasanya menggunakan aplikasi saat ingin promosi atau mengatur pesanan, terutama di waktu senggang."),
        ("Platform atau fitur apa yang paling sering Anda gunakan?",
         "Saya paling sering menggunakan WhatsApp dan Instagram untuk promosi dan komunikasi dengan pelanggan."),
        ("Apa pengalaman paling menyenangkan Anda saat menjalankan usaha?",
         "Pengalaman paling menyenangkan adalah ketika promosi yang saya lakukan berhasil menarik banyak pelanggan baru dan penjualan meningkat."),
        ("Pernahkah Anda mengalami pengalaman kurang menyenangkan saat menjalankan usaha?",
         "Ya, pernah. Kadang ada kendala saat proses promosi atau saat pelanggan membatalkan pesanan secara tiba-tiba."),
        ("Hal apa yang biasanya membuat Anda merasa repot atau sulit saat mengelola usaha?",
         "Yang sering terasa sulit adalah saat promosi, karena harus dilakukan manual dan memakan waktu, apalagi kalau harus kirim ke banyak pelanggan."),
        ("Bagaimana perasaan Anda ketika mengalami kendala saat menggunakan aplikasi?",
         "Biasanya saya merasa bingung dan sedikit kesal, tapi tetap mencoba pelan-pelan sampai bisa, atau kembali ke cara yang sudah biasa."),
        ("Menurut Anda, fitur atau layanan apa yang membuat pengelolaan usaha menjadi lebih mudah?",
         "Fitur yang mempermudah adalah yang bisa membantu promosi lebih cepat dan praktis, serta mudah digunakan tanpa perlu banyak belajar."),
        ("Menurut Anda, apa yang sebaiknya ditingkatkan dari aplikasi bisnis?",
         "Menurut saya, aplikasi sebaiknya dibuat lebih sederhana dan mudah dipahami, serta memiliki fitur otomatis agar tidak perlu banyak proses manual."),
        ("Jika bisa menambahkan satu fitur pada aplikasi bisnis, apa yang ingin Anda tambahkan?",
         "Saya ingin ada fitur promosi otomatis yang bisa membantu menjangkau lebih banyak pelanggan tanpa harus dilakukan secara manual."),
    ],
    # Panel 1: Susanto Hari Wibowo (10 Q&A)
    [
        ("Bisa perkenalkan diri Anda terlebih dahulu?",
         "Nama saya Susanto Hari Wibowo, pekerjaan wiraswasta, usia 44 tahun."),
        ("Bisa ceritakan tentang keseharian Anda?",
         "Keseharian saya mulai jam 6 pagi bersih-bersih toko dan menata stok yang masih ada di gudang menatanya ke display."),
        ("Apa yang biasanya Anda lakukan ketika mengelola toko?",
         "Kegiatan utama saya melayani pembeli eceran pagi hari."),
        ("Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?",
         "Hal paling penting bagi saya itu ketersediaan barang, jangan sampai pelanggan datang tapi stok kosong."),
        ("Apa pengalaman terbaik Anda saat berjualan?",
         "Pengalaman terbaik itu kalau ada yang borong banyak saat stok lagi penuh."),
        ("Apa pengalaman terburuk yang pernah Anda alami?",
         "Pengalaman terburuk itu kalau pesan stok online dari supplier baru di Facebook, fotonya bagus tapi pas datang kualitas plastiknya tipis dan gampang robek."),
        ("Bagaimana cara Anda mengatasi kendala tersebut?",
         "Saya mencoba mencari supplier lain yang lebih terpercaya dan memeriksa kualitas barang sebelum membeli dalam jumlah banyak."),
        ("Kendala apa saja yang biasanya Anda hadapi saat mengelola stok?",
         "Kendala paling sering itu stok tidak terukur."),
        ("Mengapa hal ini menjadi masalah bagi Anda?",
         "Ini jadi masalah karena saya bisa kehilangan pelanggan harian kalau barang yang mereka cari tidak ada terus."),
        ("Menurut Anda, apa yang bisa membuat pengelolaan toko lebih mudah?",
         "Saya perlu aplikasi yang mencatat jumlah stok barang serta harga dari setiap supplier."),
    ],
    # Panel 2: Haris Wahyu Ramadhani (9 Q&A)
    [
        ("Perkenalkan diri Anda",
         "Nama saya Haris Ridho Ramadhan, saya merupakan mahasiswa aktif di Institut Teknologi Sepuluh Nopember Jurusan Desain Produk."),
        ("Bagaimana aktivitas anda sehari-hari sebagai mahasiswa?",
         "Saya setiap hari Senin-Jumat melaksanakan kegiatan yang sama berulang, yaitu pergi kuliah, mengerjakan tugas, dan istirahat."),
        ("Apakah anda memiliki perasaan jenuh?",
         "Ya, maka dari itu saya membuka usaha kecil-kecilan bersama 5 orang teman saya yaitu menyediakan jasa editing dan desain, seperti pembuatan pamflet, logo, dan aset UI."),
        ("Apa pengalaman terbaik dan terburuk selama menjalankan usaha?",
         "Pengalaman terbaik adalah mendapatkan apresiasi balik dari klien dan mendapatkan hasil berupa uang. Kendala: pemasaran produk yang kurang berkembang, hanya di lingkup pertemanan."),
        ("Mengapa kendala tersebut menjadi masalah?",
         "Sepinya pesanan project yang menyebabkan saya dan teman mendapatkan pemasukan yang kurang."),
        ("Bagaimana cara anda dan tim mengatasi permasalahan tersebut?",
         "Berpikir untuk memasarkan produk di platform e-commerce seperti TikTok Shop, Shopee, Lazada. Namun masih awam dalam menjual jasa melalui platform e-commerce."),
        ("Apakah anda tetap menggunakan metode pemasaran yang baru?",
         "Ya, tetap menggunakan metode pemasaran yang baru, dengan belajar tentang algoritma e-commerce dan terus menumbuhkan inovasi."),
        ("Apa harapanmu untuk aplikasi e-commerce?",
         "Memberikan panduan cara memasang produk, dan diadakan fitur kategori sesuai jenis produk/jasa yang ditawarkan."),
        ("Apakah anda tetap memberikan yang terbaik ke pelanggan?",
         "Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain."),
    ],
    # Panel 3: Widya (10 Q&A)
    [
        ("Perkenalkan diri anda?",
         "Widya Ony berusia 19 tahun, Mahasiswa semester 2 Politeknik Negeri Madiun."),
        ("Apa yang biasa anda lakukan saat menggunakan TikTokShop?",
         "Mencari barang yang diinginkan juga membandingkan harga dan ongkir, supaya dapat barang yang paling terjangkau."),
        ("Apa yang paling penting bagi anda?",
         "Kejujuran produk dan efisiensi biaya, gratis ongkir dan promo diskon sangat membantu menghemat uang saku."),
        ("Apa hal yang paling penting saat melakukan aktivitas tersebut?",
         'Pengalaman terbaik saat mendapatkan harga jauh lebih murah karena promo "flash sale" saat Live, dan proses checkout yang sangat cepat.'),
        ("Kendala apa yang sering anda hadapi?",
         "Live chat sangat mengganggu, sulit mengatur komentar, stiker dan pop up promosi mengumpuk."),
        ("Apakah anda pernah menggunakan fitur Live Streaming?",
         "Sudah pernah, tapi hanya sebagai penonton."),
        ("Apa yang bisa membuat TikTokShop lebih mudah digunakan?",
         "Fitur filter, sistem notifikasi spam, dan fokus pada status pengiriman."),
        ("Apa yang paling anda harapkan saat menggunakan TikTokShop?",
         'Jaminan kualitas barang yang lebih ketat dari pihak aplikasi agar tidak ada produk yang "zonk".'),
        ("Jika bisa memperbaiki satu hal apa yang akan anda ubah?",
         "Sistem filter di keranjang, saat ini sulit menyaring barang berdasarkan kategori tertentu dari daftar yang panjang."),
        ("Solusi ideal menurut anda?",
         'Fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan.'),
    ],
    # Panel 4: Zaskiya (5 Q&A)
    [
        ("Perkenalkan diri anda, pernahkah menggunakan aplikasi UMKM?",
         "Saya Zaskiya Sandi A.A., pengguna aktif berbagai aplikasi digital. Pernah menggunakan Shopee, TikTok Shop, dan Gojek hampir setiap minggu."),
        ("Pernah mengalami kendala pembelian gagal?",
         "Ya, pernah. Penyebabnya: metode pembayaran error, ongkos kirim terlalu mahal, stok barang tiba-tiba habis."),
        ("Kesulitan mencari fitur yang ingin digunakan?",
         "Ya, terkadang. Tampilan terlalu ramai (banyak promo/banner) dan menu terlalu banyak namun tidak terorganisir."),
        ("Apa yang harus ditambah/dirubah/dihapus di halaman depan?",
         "Menyederhanakan tampilan, mengelompokkan fitur sesuai kategori yang jelas, mengurangi fitur yang jarang digunakan."),
        ("Bagaimana alur pembelian yang ideal?",
         "Pencarian produk cepat dan akurat, informasi produk jelas, pilihan pembayaran lengkap, checkout singkat, konfirmasi pesanan jelas."),
    ],
]

def build_interview_table(qa_list):
    rows = []
    for q, a in qa_list:
        rows.append(f'                    <tr>\n                      <th>Question {q}</th>\n                      <td>{a}</td>\n                    </tr>')
    return '\n'.join(rows)

# Replace interview sections in each panel
for i, pdata in enumerate(panels_data):
    html = pdata['html']
    
    # Replace interview sticky notes with table
    # Match from interview__qa-list to its closing </div>
    interview_pattern = re.compile(
        r'(<div class="interview__qa-list">)'
        r'.*?'
        r'(</div>\s*</div>\s*</div>)',  # close qa-list, section-box, interview-row
        re.DOTALL
    )
    
    qa_data = all_interview_data[i]
    table_html = build_interview_table(qa_data)
    
    replacement = (
        '<div class="persona__interview-grid">\n'
        '                <div class="interview__table-wrapper">\n'
        '                  <table class="interview__table">\n'
        '                    <tbody>\n' +
        table_html + '\n'
        '                    </tbody>\n'
        '                  </table>\n'
        '                </div>\n'
        '              </div>\n'
        '            </div>\n'
        '          </div>\n'
        '        </div>'
    )
    
    match = interview_pattern.search(html)
    if match:
        # Replace from interview__qa-list opening div through the 3 closing divs
        html = html[:match.start()] + replacement + html[match.end():]
        panels_data[i]['html'] = html
    
    # Also fix the Interview Data title color from blue to orange
    html = panels_data[i]['html']
    html = html.replace(
        'persona__section-title--blue">Interview Data</h4>',
        'persona__section-title--orange">Interview Data</h4>'
    )
    panels_data[i]['html'] = html

# === STEP 4: Fix garbled emojis with SVG icons ===
svg_avatar_small = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" style="color: var(--text);">'
    '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
    '<circle cx="12" cy="7" r="4"/></svg>')

svg_avatar_large = ('<svg width="40" height="40" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" style="color: var(--brand);">'
    '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
    '<circle cx="12" cy="7" r="4"/></svg>')

# Fix tabs
bak_tabs = bak[bak.find('<div class="persona__tabs"'):bak.find('</div>', bak.find('persona__tabs') + 200) + 6]
# Actually, let me get the full tabs block
tabs_start = bak.find('<div class="persona__tabs"')
# Find closing of tabs div - it's a single </div> at the right depth
tabs_region = bak[tabs_start:]
depth = 0
tabs_end_offset = 0
for m in re.finditer(r'<div[\s>]|</div>', tabs_region):
    if m.group().startswith('<div'):
        depth += 1
    else:
        depth -= 1
    if depth == 0:
        tabs_end_offset = m.end()
        break
bak_tabs = bak[tabs_start:tabs_start + tabs_end_offset]

# Replace garbled emojis in tabs
bak_tabs = re.sub(
    r'<span class="persona__avatar">[^<]*</span>',
    f'<span class="persona__avatar">{svg_avatar_small}</span>',
    bak_tabs
)

# Fix each panel's photo-wrap
for i in range(len(panels_data)):
    html = panels_data[i]['html']
    html = re.sub(
        r'<div class="persona__photo-wrap">[^<]*</div>',
        f'<div class="persona__photo-wrap">{svg_avatar_large}</div>',
        html
    )
    panels_data[i]['html'] = html

# === STEP 5: Reconstruct the persona section ===
# Get section header (from before tabs)
section_header_start = bak.find('<section class="persona"')
tabs_start_in_bak = bak.find('<div class="persona__tabs"', section_header_start)

# Section header: from <section to before tabs
section_header = bak[section_header_start:tabs_start_in_bak]

# Fix panel comments
panel_comments = [
    '<!-- === Panel 1: Fikri Ramadhan === -->',
    '<!-- === Panel 2: Susanto Hari Wibowo === -->',
    '<!-- === Panel 3: Haris Wahyu Ramadhani === -->',
    '<!-- === Panel 4: Widya Dny Yuanika R. === -->',
    '<!-- === Panel 5: Zaskiya Soaldi A.A. === -->',
]

# Build the full persona section
persona_section_parts = [section_header, bak_tabs, '\n']

for i, pdata in enumerate(panels_data):
    persona_section_parts.append(f'\n        {panel_comments[i]}')
    persona_section_parts.append(f'\n        {pdata["html"]}')

# Close section
persona_section_parts.append('\n\n      </div>\n    </section>')

new_persona_section = ''.join(persona_section_parts)

# === STEP 6: Replace persona section in current index.html ===
# Find persona section boundaries in current file
curr_persona_start = current.find('<section class="persona"')
curr_persona_end = current.find('</section>', curr_persona_start) + len('</section>')

# Replace
new_content = current[:curr_persona_start] + new_persona_section + current[curr_persona_end:]

# Fix any remaining garbled characters in non-persona sections
# (the current file should already be clean from previous fixes)

with open('c:/semester 2/Web UAS/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    result = f.read()

# Check panel balance
new_panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', result)]
results = []
for i, start in enumerate(new_panel_starts):
    end = new_panel_starts[i+1] if i+1 < len(new_panel_starts) else result.find('</section>', start)
    panel_html = result[start:end]
    opens = len(re.findall(r'<div[\s>]', panel_html))
    closes = len(re.findall(r'</div>', panel_html))
    name_match = re.search(r'persona__name">([^<]+)', panel_html)
    name = name_match.group(1) if name_match else f'Panel {i}'
    has_table = 'interview__table' in panel_html
    rows = len(re.findall(r'<tr>', panel_html))
    results.append(f"Panel {i} ({name}): opens={opens}, closes={closes}, diff={opens-closes}, table={has_table}, rows={rows}")

# Overall persona section
ps = result.find('<section class="persona"')
pe = result.find('</section>', ps) + len('</section>')
ph = result[ps:pe]
po = len(re.findall(r'<div[\s>]', ph))
pc = len(re.findall(r'</div>', ph))
results.append(f"\nPersona section: opens={po}, closes={pc}, diff={po-pc}")
results.append(f"Total lines: {result.count(chr(10))}")

with open('c:/semester 2/Web UAS/rebuild_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))
print("Done - check rebuild_result.txt")
