"""
Complete rebuild v3: Extract persona from .bak, fix structure, add interview tables.
Key fix: correct number of closing divs after interview table replacement.
"""
import re

with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    current = f.read()

# --- SVG icons ---
SVG_SMALL = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" style="color: var(--text);">'
    '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
    '<circle cx="12" cy="7" r="4"/></svg>')

SVG_LARGE = ('<svg width="40" height="40" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" style="color: var(--brand);">'
    '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
    '<circle cx="12" cy="7" r="4"/></svg>')

# --- Interview data ---
interview_data = [
    # Panel 0: Fikri (10)
    [("Bisakah perkenalkan diri Anda secara singkat? (Nama, usia, dan pekerjaan)","Nama saya Fikri Ramadhan, usia 21 tahun, menjalankan usaha kecil di bidang penjualan produk secara online."),("Bisa ceritakan aktivitas sehari-hari Anda dan kapasitas bisnis Anda mengelola usaha?","Sehari-hari saya mengelola usaha, seperti menyiapkan produk, melayani pelanggan, dan promosi. Saya biasanya menggunakan aplikasi saat ingin promosi atau mengatur pesanan, terutama di waktu senggang."),("Platform atau fitur apa yang paling sering Anda gunakan?","Saya paling sering menggunakan WhatsApp dan Instagram untuk promosi dan komunikasi dengan pelanggan."),("Apa pengalaman paling menyenangkan Anda saat menjalankan usaha?","Pengalaman paling menyenangkan adalah ketika promosi yang saya lakukan berhasil menarik banyak pelanggan baru dan penjualan meningkat."),("Pernahkah Anda mengalami pengalaman kurang menyenangkan saat menjalankan usaha?","Ya, pernah. Kadang ada kendala saat proses promosi atau saat pelanggan membatalkan pesanan secara tiba-tiba."),("Hal apa yang biasanya membuat Anda merasa repot atau sulit saat mengelola usaha?","Yang sering terasa sulit adalah saat promosi, karena harus dilakukan manual dan memakan waktu, apalagi kalau harus kirim ke banyak pelanggan."),("Bagaimana perasaan Anda ketika mengalami kendala saat menggunakan aplikasi?","Biasanya saya merasa bingung dan sedikit kesal, tapi tetap mencoba pelan-pelan sampai bisa, atau kembali ke cara yang sudah biasa."),("Menurut Anda, fitur atau layanan apa yang membuat pengelolaan usaha menjadi lebih mudah?","Fitur yang mempermudah adalah yang bisa membantu promosi lebih cepat dan praktis, serta mudah digunakan tanpa perlu banyak belajar."),("Menurut Anda, apa yang sebaiknya ditingkatkan dari aplikasi bisnis?","Menurut saya, aplikasi sebaiknya dibuat lebih sederhana dan mudah dipahami, serta memiliki fitur otomatis agar tidak perlu banyak proses manual."),("Jika bisa menambahkan satu fitur pada aplikasi bisnis, apa yang ingin Anda tambahkan?","Saya ingin ada fitur promosi otomatis yang bisa membantu menjangkau lebih banyak pelanggan tanpa harus dilakukan secara manual.")],
    # Panel 1: Susanto (10)
    [("Bisa perkenalkan diri Anda terlebih dahulu?","Nama saya Susanto Hari Wibowo, pekerjaan wiraswasta, usia 44 tahun."),("Bisa ceritakan tentang keseharian Anda?","Keseharian saya mulai jam 6 pagi bersih-bersih toko dan menata stok yang masih ada di gudang menatanya ke display."),("Apa yang biasanya Anda lakukan ketika mengelola toko?","Kegiatan utama saya melayani pembeli eceran pagi hari."),("Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?","Hal paling penting bagi saya itu ketersediaan barang, jangan sampai pelanggan datang tapi stok kosong."),("Apa pengalaman terbaik Anda saat berjualan?","Pengalaman terbaik itu kalau ada yang borong banyak saat stok lagi penuh."),("Apa pengalaman terburuk yang pernah Anda alami?","Pengalaman terburuk itu kalau pesan stok online dari supplier baru di Facebook, fotonya bagus tapi pas datang kualitas plastiknya tipis dan gampang robek."),("Bagaimana cara Anda mengatasi kendala tersebut?","Saya mencoba mencari supplier lain yang lebih terpercaya dan memeriksa kualitas barang sebelum membeli dalam jumlah banyak."),("Kendala apa saja yang biasanya Anda hadapi saat mengelola stok?","Kendala paling sering itu stok tidak terukur."),("Mengapa hal ini menjadi masalah bagi Anda?","Ini jadi masalah karena saya bisa kehilangan pelanggan harian kalau barang yang mereka cari tidak ada terus."),("Menurut Anda, apa yang bisa membuat pengelolaan toko lebih mudah?","Saya perlu aplikasi yang mencatat jumlah stok barang serta harga dari setiap supplier.")],
    # Panel 2: Haris (9)
    [("Perkenalkan diri Anda","Nama saya Haris Ridho Ramadhan, saya merupakan mahasiswa aktif di Institut Teknologi Sepuluh Nopember Jurusan Desain Produk."),("Bagaimana aktivitas anda sehari-hari sebagai mahasiswa?","Saya setiap hari Senin-Jumat melaksanakan kegiatan yang sama berulang, yaitu pergi kuliah, mengerjakan tugas, dan istirahat."),("Apakah anda memiliki perasaan jenuh?","Ya, maka dari itu saya membuka usaha kecil-kecilan bersama 5 orang teman saya yaitu menyediakan jasa editing dan desain, seperti pembuatan pamflet, logo, dan aset UI."),("Apa pengalaman terbaik dan terburuk selama menjalankan usaha?","Pengalaman terbaik adalah mendapatkan apresiasi balik dari klien dan mendapatkan hasil berupa uang. Kendala: pemasaran produk yang kurang berkembang, hanya di lingkup pertemanan."),("Mengapa kendala tersebut menjadi masalah?","Sepinya pesanan project yang menyebabkan saya dan teman mendapatkan pemasukan yang kurang."),("Bagaimana cara anda dan tim mengatasi permasalahan tersebut?","Berpikir untuk memasarkan produk di platform e-commerce seperti TikTok Shop, Shopee, Lazada. Namun masih awam dalam menjual jasa melalui platform e-commerce."),("Apakah anda tetap menggunakan metode pemasaran yang baru?","Ya, tetap menggunakan metode pemasaran yang baru, dengan belajar tentang algoritma e-commerce dan terus menumbuhkan inovasi."),("Apa harapanmu untuk aplikasi e-commerce?","Memberikan panduan cara memasang produk, dan diadakan fitur kategori sesuai jenis produk/jasa yang ditawarkan."),("Apakah anda tetap memberikan yang terbaik ke pelanggan?","Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain.")],
    # Panel 3: Widya (10)
    [("Perkenalkan diri anda?","Widya Ony berusia 19 tahun, Mahasiswa semester 2 Politeknik Negeri Madiun."),("Apa yang biasa anda lakukan saat menggunakan TikTokShop?","Mencari barang yang diinginkan juga membandingkan harga dan ongkir, supaya dapat barang yang paling terjangkau."),("Apa yang paling penting bagi anda?","Kejujuran produk dan efisiensi biaya, gratis ongkir dan promo diskon sangat membantu menghemat uang saku."),("Apa hal yang paling penting saat melakukan aktivitas tersebut?",'Pengalaman terbaik saat mendapatkan harga jauh lebih murah karena promo "flash sale" saat Live, dan proses checkout yang sangat cepat.'),("Kendala apa yang sering anda hadapi?","Live chat sangat mengganggu, sulit mengatur komentar, stiker dan pop up promosi mengumpuk."),("Apakah anda pernah menggunakan fitur Live Streaming?","Sudah pernah, tapi hanya sebagai penonton."),("Apa yang bisa membuat TikTokShop lebih mudah digunakan?","Fitur filter, sistem notifikasi spam, dan fokus pada status pengiriman."),("Apa yang paling anda harapkan saat menggunakan TikTokShop?",'Jaminan kualitas barang yang lebih ketat dari pihak aplikasi agar tidak ada produk yang "zonk".'),("Jika bisa memperbaiki satu hal apa yang akan anda ubah?","Sistem filter di keranjang, saat ini sulit menyaring barang berdasarkan kategori tertentu dari daftar yang panjang."),("Solusi ideal menurut anda?",'Fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan.')],
    # Panel 4: Zaskiya (5)
    [("Perkenalkan diri anda, pernahkah menggunakan aplikasi UMKM?","Saya Zaskiya Sandi A.A., pengguna aktif berbagai aplikasi digital. Pernah menggunakan Shopee, TikTok Shop, dan Gojek hampir setiap minggu."),("Pernah mengalami kendala pembelian gagal?","Ya, pernah. Penyebabnya: metode pembayaran error, ongkos kirim terlalu mahal, stok barang tiba-tiba habis."),("Kesulitan mencari fitur yang ingin digunakan?","Ya, terkadang. Tampilan terlalu ramai (banyak promo/banner) dan menu terlalu banyak namun tidak terorganisir."),("Apa yang harus ditambah/dirubah/dihapus di halaman depan?","Menyederhanakan tampilan, mengelompokkan fitur sesuai kategori yang jelas, mengurangi fitur yang jarang digunakan."),("Bagaimana alur pembelian yang ideal?","Pencarian produk cepat dan akurat, informasi produk jelas, pilihan pembayaran lengkap, checkout singkat, konfirmasi pesanan jelas.")],
]

# --- Extract each panel from .bak ---
panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', bak)]
persona_sec_end = bak.find('</section>', panel_starts[-1]) + len('</section>')

results = []
fixed_panels = []

for i, start in enumerate(panel_starts):
    end = panel_starts[i+1] if i+1 < len(panel_starts) else persona_sec_end
    html = bak[start:end]
    
    # Step A: Replace interview sticky with table
    # The interview section starts with interview__qa-list
    qa_start = html.find('<div class="interview__qa-list">')
    if qa_start >= 0:
        # Find the exact structure: interview-row > section-box > qa-list > qa-items > closes
        # We need to find where the interview section STARTS (the comment or the interview-row div)
        interview_row_start = html.rfind('<div class="persona__interview-row">', 0, qa_start)
        
        # Find the end: after qa-list closes, we need section-box close, interview-row close
        # Then grid close and panel close
        # Let's find all closing </div> after the interview data
        # Count divs from interview_row_start to find where it closes
        
        # Find the correct end: trace depth from interview_row_start
        depth = 0
        pos = interview_row_start
        end_pos = -1
        for m2 in re.finditer(r'<div[\s>]|</div>', html[pos:]):
            abs_pos = pos + m2.start()
            if m2.group().startswith('<div'):
                depth += 1
            else:
                depth -= 1
            if depth == 0:
                end_pos = pos + m2.end()
                break
        
        if end_pos > 0:
            # Build replacement
            qa_data = interview_data[i]
            table_rows = '\n'.join(
                f'                    <tr>\n                      <th>Question {q}</th>\n                      <td>{a}</td>\n                    </tr>'
                for q, a in qa_data
            )
            
            replacement = (
                '<div class="persona__interview-row">\n'
                '              <div class="persona__section-box">\n'
                '                <h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>\n'
                '                <div class="persona__interview-grid">\n'
                '                  <div class="interview__table-wrapper">\n'
                '                    <table class="interview__table">\n'
                '                      <tbody>\n' +
                table_rows + '\n'
                '                      </tbody>\n'
                '                    </table>\n'
                '                  </div>\n'
                '                </div>\n'
                '              </div>\n'
                '            </div>'
            )
            
            html = html[:interview_row_start] + replacement + html[end_pos:]
    
    # Step B: Fix garbled emojis
    html = re.sub(
        r'<div class="persona__photo-wrap">[^<]*</div>',
        f'<div class="persona__photo-wrap">{SVG_LARGE}</div>',
        html
    )
    
    # Step C: Verify balance
    opens = len(re.findall(r'<div[\s>]', html))
    closes = len(re.findall(r'</div>', html))
    diff = opens - closes
    name_m = re.search(r'persona__name">([^<]+)', html)
    name = name_m.group(1) if name_m else f'Panel {i}'
    has_table = 'interview__table' in html
    rows = len(re.findall(r'<tr>', html))
    
    results.append(f"Panel {i} ({name}): opens={opens}, closes={closes}, diff={diff}, table={has_table}, rows={rows}")
    fixed_panels.append(html)

# --- Build persona section ---
# Get section header (before tabs)
persona_sec_start = bak.find('<section class="persona"')
tabs_start = bak.find('<div class="persona__tabs"', persona_sec_start)
section_header = bak[persona_sec_start:tabs_start]

# Get tabs block
tabs_depth = 0
tabs_end = tabs_start
for m in re.finditer(r'<div[\s>]|</div>', bak[tabs_start:]):
    if m.group().startswith('<div'):
        tabs_depth += 1
    else:
        tabs_depth -= 1
    if tabs_depth == 0:
        tabs_end = tabs_start + m.end()
        break
tabs_html = bak[tabs_start:tabs_end]
# Fix garbled emojis in tabs
tabs_html = re.sub(
    r'<span class="persona__avatar">[^<]*</span>',
    f'<span class="persona__avatar">{SVG_SMALL}</span>',
    tabs_html
)

# Panel comments
comments = [
    '<!-- === Panel 1: Fikri Ramadhan === -->',
    '<!-- === Panel 2: Susanto Hari Wibowo === -->',
    '<!-- === Panel 3: Haris Wahyu Ramadhani === -->',
    '<!-- === Panel 4: Widya Dny Yuanika R. === -->',
    '<!-- === Panel 5: Zaskiya Soaldi A.A. === -->',
]

# Assemble
parts = [section_header, tabs_html, '\n']
for i, panel_html in enumerate(fixed_panels):
    parts.append(f'\n        {comments[i]}\n        ')
    parts.append(panel_html.strip())
    parts.append('\n')
parts.append('\n      </div>\n    </section>')

new_persona = ''.join(parts)

# --- Replace in current file ---
curr_p_start = current.find('<section class="persona"')
curr_p_end = current.find('</section>', curr_p_start) + len('</section>')
new_content = current[:curr_p_start] + new_persona + current[curr_p_end:]

with open('c:/semester 2/Web UAS/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Final verification
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    result = f.read()

new_panel_starts = [m.start() for m in re.finditer(r'<div class="persona__panel', result)]
for i, start in enumerate(new_panel_starts):
    end = new_panel_starts[i+1] if i+1 < len(new_panel_starts) else result.find('</section>', start)
    ph = result[start:end]
    o = len(re.findall(r'<div[\s>]', ph))
    c = len(re.findall(r'</div>', ph))
    nm = re.search(r'persona__name">([^<]+)', ph)
    n = nm.group(1) if nm else f'Panel {i}'
    results.append(f"VERIFY Panel {i} ({n}): opens={o}, closes={c}, diff={o-c}")

ps = result.find('<section class="persona"')
pe = result.find('</section>', ps) + len('</section>')
ph = result[ps:pe]
po = len(re.findall(r'<div[\s>]', ph))
pc = len(re.findall(r'</div>', ph))
results.append(f"Persona section: opens={po}, closes={pc}, diff={po-pc}")
results.append(f"Total lines: {result.count(chr(10))}")

with open('c:/semester 2/Web UAS/rebuild_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))
print("Done")
