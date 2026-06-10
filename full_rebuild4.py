"""
Rebuild v4: Fix panel structure by removing trailing extra </div> per panel.
"""
import re

with open('c:/semester 2/Web UAS/index.html.bak', 'r', encoding='utf-8') as f:
    bak = f.read()
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    current = f.read()

SVG_SMALL = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
SVG_LARGE = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'

interview_data = [
    [("Bisakah perkenalkan diri Anda secara singkat? (Nama, usia, dan pekerjaan)","Nama saya Fikri Ramadhan, usia 21 tahun, menjalankan usaha kecil di bidang penjualan produk secara online."),("Bisa ceritakan aktivitas sehari-hari Anda dan kapasitas bisnis Anda mengelola usaha?","Sehari-hari saya mengelola usaha, seperti menyiapkan produk, melayani pelanggan, dan promosi. Saya biasanya menggunakan aplikasi saat ingin promosi atau mengatur pesanan, terutama di waktu senggang."),("Platform atau fitur apa yang paling sering Anda gunakan?","Saya paling sering menggunakan WhatsApp dan Instagram untuk promosi dan komunikasi dengan pelanggan."),("Apa pengalaman paling menyenangkan Anda saat menjalankan usaha?","Pengalaman paling menyenangkan adalah ketika promosi yang saya lakukan berhasil menarik banyak pelanggan baru dan penjualan meningkat."),("Pernahkah Anda mengalami pengalaman kurang menyenangkan saat menjalankan usaha?","Ya, pernah. Kadang ada kendala saat proses promosi atau saat pelanggan membatalkan pesanan secara tiba-tiba."),("Hal apa yang biasanya membuat Anda merasa repot atau sulit saat mengelola usaha?","Yang sering terasa sulit adalah saat promosi, karena harus dilakukan manual dan memakan waktu, apalagi kalau harus kirim ke banyak pelanggan."),("Bagaimana perasaan Anda ketika mengalami kendala saat menggunakan aplikasi?","Biasanya saya merasa bingung dan sedikit kesal, tapi tetap mencoba pelan-pelan sampai bisa, atau kembali ke cara yang sudah biasa."),("Menurut Anda, fitur atau layanan apa yang membuat pengelolaan usaha menjadi lebih mudah?","Fitur yang mempermudah adalah yang bisa membantu promosi lebih cepat dan praktis, serta mudah digunakan tanpa perlu banyak belajar."),("Menurut Anda, apa yang sebaiknya ditingkatkan dari aplikasi bisnis?","Menurut saya, aplikasi sebaiknya dibuat lebih sederhana dan mudah dipahami, serta memiliki fitur otomatis agar tidak perlu banyak proses manual."),("Jika bisa menambahkan satu fitur pada aplikasi bisnis, apa yang ingin Anda tambahkan?","Saya ingin ada fitur promosi otomatis yang bisa membantu menjangkau lebih banyak pelanggan tanpa harus dilakukan secara manual.")],
    [("Bisa perkenalkan diri Anda terlebih dahulu?","Nama saya Susanto Hari Wibowo, pekerjaan wiraswasta, usia 44 tahun."),("Bisa ceritakan tentang keseharian Anda?","Keseharian saya mulai jam 6 pagi bersih-bersih toko dan menata stok yang masih ada di gudang menatanya ke display."),("Apa yang biasanya Anda lakukan ketika mengelola toko?","Kegiatan utama saya melayani pembeli eceran pagi hari."),("Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?","Hal paling penting bagi saya itu ketersediaan barang, jangan sampai pelanggan datang tapi stok kosong."),("Apa pengalaman terbaik Anda saat berjualan?","Pengalaman terbaik itu kalau ada yang borong banyak saat stok lagi penuh."),("Apa pengalaman terburuk yang pernah Anda alami?","Pengalaman terburuk itu kalau pesan stok online dari supplier baru di Facebook, fotonya bagus tapi pas datang kualitas plastiknya tipis dan gampang robek."),("Bagaimana cara Anda mengatasi kendala tersebut?","Saya mencoba mencari supplier lain yang lebih terpercaya dan memeriksa kualitas barang sebelum membeli dalam jumlah banyak."),("Kendala apa saja yang biasanya Anda hadapi saat mengelola stok?","Kendala paling sering itu stok tidak terukur."),("Mengapa hal ini menjadi masalah bagi Anda?","Ini jadi masalah karena saya bisa kehilangan pelanggan harian kalau barang yang mereka cari tidak ada terus."),("Menurut Anda, apa yang bisa membuat pengelolaan toko lebih mudah?","Saya perlu aplikasi yang mencatat jumlah stok barang serta harga dari setiap supplier.")],
    [("Perkenalkan diri Anda","Nama saya Haris Ridho Ramadhan, saya merupakan mahasiswa aktif di Institut Teknologi Sepuluh Nopember Jurusan Desain Produk."),("Bagaimana aktivitas anda sehari-hari sebagai mahasiswa?","Saya setiap hari Senin-Jumat melaksanakan kegiatan yang sama berulang, yaitu pergi kuliah, mengerjakan tugas, dan istirahat."),("Apakah anda memiliki perasaan jenuh?","Ya, maka dari itu saya membuka usaha kecil-kecilan bersama 5 orang teman saya yaitu menyediakan jasa editing dan desain, seperti pembuatan pamflet, logo, dan aset UI."),("Apa pengalaman terbaik dan terburuk selama menjalankan usaha?","Pengalaman terbaik adalah mendapatkan apresiasi balik dari klien dan mendapatkan hasil berupa uang. Kendala: pemasaran produk yang kurang berkembang, hanya di lingkup pertemanan."),("Mengapa kendala tersebut menjadi masalah?","Sepinya pesanan project yang menyebabkan saya dan teman mendapatkan pemasukan yang kurang."),("Bagaimana cara anda dan tim mengatasi permasalahan tersebut?","Berpikir untuk memasarkan produk di platform e-commerce seperti TikTok Shop, Shopee, Lazada. Namun masih awam dalam menjual jasa melalui platform e-commerce."),("Apakah anda tetap menggunakan metode pemasaran yang baru?","Ya, tetap menggunakan metode pemasaran yang baru, dengan belajar tentang algoritma e-commerce dan terus menumbuhkan inovasi."),("Apa harapanmu untuk aplikasi e-commerce?","Memberikan panduan cara memasang produk, dan diadakan fitur kategori sesuai jenis produk/jasa yang ditawarkan."),("Apakah anda tetap memberikan yang terbaik ke pelanggan?","Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain.")],
    [("Perkenalkan diri anda?","Widya Ony berusia 19 tahun, Mahasiswa semester 2 Politeknik Negeri Madiun."),("Apa yang biasa anda lakukan saat menggunakan TikTokShop?","Mencari barang yang diinginkan juga membandingkan harga dan ongkir, supaya dapat barang yang paling terjangkau."),("Apa yang paling penting bagi anda?","Kejujuran produk dan efisiensi biaya, gratis ongkir dan promo diskon sangat membantu menghemat uang saku."),("Apa hal yang paling penting saat melakukan aktivitas tersebut?",'Pengalaman terbaik saat mendapatkan harga jauh lebih murah karena promo "flash sale" saat Live, dan proses checkout yang sangat cepat.'),("Kendala apa yang sering anda hadapi?","Live chat sangat mengganggu, sulit mengatur komentar, stiker dan pop up promosi mengumpuk."),("Apakah anda pernah menggunakan fitur Live Streaming?","Sudah pernah, tapi hanya sebagai penonton."),("Apa yang bisa membuat TikTokShop lebih mudah digunakan?","Fitur filter, sistem notifikasi spam, dan fokus pada status pengiriman."),("Apa yang paling anda harapkan saat menggunakan TikTokShop?",'Jaminan kualitas barang yang lebih ketat dari pihak aplikasi agar tidak ada produk yang "zonk".'),("Jika bisa memperbaiki satu hal apa yang akan anda ubah?","Sistem filter di keranjang, saat ini sulit menyaring barang berdasarkan kategori tertentu dari daftar yang panjang."),("Solusi ideal menurut anda?",'Fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan.')],
    [("Perkenalkan diri anda, pernahkah menggunakan aplikasi UMKM?","Saya Zaskiya Sandi A.A., pengguna aktif berbagai aplikasi digital. Pernah menggunakan Shopee, TikTok Shop, dan Gojek hampir setiap minggu."),("Pernah mengalami kendala pembelian gagal?","Ya, pernah. Penyebabnya: metode pembayaran error, ongkos kirim terlalu mahal, stok barang tiba-tiba habis."),("Kesulitan mencari fitur yang ingin digunakan?","Ya, terkadang. Tampilan terlalu ramai (banyak promo/banner) dan menu terlalu banyak namun tidak terorganisir."),("Apa yang harus ditambah/dirubah/dihapus di halaman depan?","Menyederhanakan tampilan, mengelompokkan fitur sesuai kategori yang jelas, mengurangi fitur yang jarang digunakan."),("Bagaimana alur pembelian yang ideal?","Pencarian produk cepat dan akurat, informasi produk jelas, pilihan pembayaran lengkap, checkout singkat, konfirmasi pesanan jelas.")],
]

# Extract panels
panel_starts_pos = [m.start() for m in re.finditer(r'<div class="persona__panel', bak)]
persona_sec_end = bak.find('</section>', panel_starts_pos[-1]) + len('</section>')

fixed_panels = []
log = []

for i, start in enumerate(panel_starts_pos):
    end = panel_starts_pos[i+1] if i+1 < len(panel_starts_pos) else persona_sec_end
    html = bak[start:end]
    
    # Step 1: Count opens and closes, find extra count
    opens = len(re.findall(r'<div[\s>]', html))
    closes = len(re.findall(r'</div>', html))
    extra = closes - opens  # number of extra </div> to remove
    
    name_m = re.search(r'persona__name">([^<]+)', html)
    name = name_m.group(1) if name_m else f'Panel {i}'
    log.append(f"Panel {i} ({name}): before fix opens={opens} closes={closes} extra={extra}")
    
    # Step 2: Remove extra </div> from the end
    # Find the trailing </div> lines and remove the last `extra` ones
    if extra > 0:
        # Find all </div> that are on their own line at the end
        trailing_divs = []
        search_pos = len(html)
        for _ in range(extra + 10):  # search for more than needed
            pos = html.rfind('</div>', 0, search_pos)
            if pos < 0:
                break
            # Check if this </div> is on its own line (only whitespace before it on the line)
            line_start = html.rfind('\n', 0, pos) + 1
            before = html[line_start:pos].strip()
            if before == '':
                line_end = html.find('\n', pos + len('</div>'))
                if line_end < 0:
                    line_end = len(html)
                trailing_divs.append((line_start, line_end))
            search_pos = pos
        
        # Remove the last `extra` trailing divs (they're in reverse order)
        trailing_divs = sorted(trailing_divs, reverse=True)
        for j in range(min(extra, len(trailing_divs))):
            ls, le = trailing_divs[j]
            html = html[:ls] + html[le:]
            log.append(f"  Removed trailing </div> at pos {ls}")
    
    # Step 3: Replace interview sticky with table
    qa_start = html.find('<div class="interview__qa-list">')
    if qa_start >= 0:
        interview_row_start = html.rfind('<div class="persona__interview-row">', 0, qa_start)
        
        # Find where interview-row closes (depth returns to 0)
        depth = 0
        end_pos = -1
        for m2 in re.finditer(r'<div[\s>]|</div>', html[interview_row_start:]):
            abs_end = interview_row_start + m2.end()
            if m2.group().startswith('<div'):
                depth += 1
            else:
                depth -= 1
            if depth == 0:
                end_pos = abs_end
                break
        
        if end_pos > 0:
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
    
    # Step 4: Fix garbled emojis
    html = re.sub(
        r'<div class="persona__photo-wrap">[^<]*</div>',
        f'<div class="persona__photo-wrap">{SVG_LARGE}</div>', html)
    
    # Verify balance
    o = len(re.findall(r'<div[\s>]', html))
    c = len(re.findall(r'</div>', html))
    log.append(f"  After fix: opens={o} closes={c} diff={o-c}")
    fixed_panels.append(html)

# Build persona section
persona_sec_start = bak.find('<section class="persona"')
tabs_start = bak.find('<div class="persona__tabs"', persona_sec_start)
section_header = bak[persona_sec_start:tabs_start]

# Get tabs
depth = 0
tabs_end = tabs_start
for m in re.finditer(r'<div[\s>]|</div>', bak[tabs_start:]):
    if m.group().startswith('<div'): depth += 1
    else: depth -= 1
    if depth == 0:
        tabs_end = tabs_start + m.end()
        break
tabs_html = bak[tabs_start:tabs_end]
tabs_html = re.sub(r'<span class="persona__avatar">[^<]*</span>',
    f'<span class="persona__avatar">{SVG_SMALL}</span>', tabs_html)

comments = [
    '<!-- === Panel 1: Fikri Ramadhan === -->',
    '<!-- === Panel 2: Susanto Hari Wibowo === -->',
    '<!-- === Panel 3: Haris Wahyu Ramadhani === -->',
    '<!-- === Panel 4: Widya Dny Yuanika R. === -->',
    '<!-- === Panel 5: Zaskiya Soaldi A.A. === -->',
]

parts = [section_header, tabs_html, '\n']
for i, ph in enumerate(fixed_panels):
    parts.append(f'\n        {comments[i]}\n        {ph.strip()}\n')
parts.append('\n      </div>\n    </section>')
new_persona = ''.join(parts)

# Replace in current file
curr_p_start = current.find('<section class="persona"')
curr_p_end = current.find('</section>', curr_p_start) + len('</section>')
new_content = current[:curr_p_start] + new_persona + current[curr_p_end:]

with open('c:/semester 2/Web UAS/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Final verify
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    result = f.read()
nps = [m.start() for m in re.finditer(r'<div class="persona__panel', result)]
for i, s in enumerate(nps):
    e = nps[i+1] if i+1 < len(nps) else result.find('</section>', s)
    ph = result[s:e]
    o = len(re.findall(r'<div[\s>]', ph))
    c = len(re.findall(r'</div>', ph))
    nm = re.search(r'persona__name">([^<]+)', ph)
    n = nm.group(1) if nm else f'P{i}'
    ht = 'interview__table' in ph
    rows = len(re.findall(r'<tr>', ph))
    log.append(f"VERIFY P{i} ({n}): diff={o-c}, table={ht}, rows={rows}")
ps = result.find('<section class="persona"')
pe = result.find('</section>', ps) + len('</section>')
ph = result[ps:pe]
log.append(f"Persona: diff={len(re.findall(r'<div[\\s>]', ph)) - len(re.findall(r'</div>', ph))}")
log.append(f"Lines: {result.count(chr(10))}")

with open('c:/semester 2/Web UAS/rebuild_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print("Done")
