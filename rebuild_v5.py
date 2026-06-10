import re

with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

SVG_SMALL = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
SVG_LARGE = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--brand);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'

interview_data = [
    [("Bisakah perkenalkan diri Anda secara singkat? (Nama, usia, dan pekerjaan)","Nama saya Fikri Ramadhan, usia 21 tahun, menjalankan usaha kecil di bidang penjualan produk secara online."),("Bisa ceritakan aktivitas sehari-hari Anda dan kapasitas bisnis Anda mengelola usaha?","Sehari-hari saya mengelola usaha, seperti menyiapkan produk, melayani pelanggan, dan promosi. Saya biasanya menggunakan aplikasi saat ingin promosi atau mengatur pesanan, terutama di waktu senggang."),("Platform atau fitur apa yang paling sering Anda gunakan?","Saya paling sering menggunakan WhatsApp dan Instagram untuk promosi dan komunikasi dengan pelanggan."),("Apa pengalaman paling menyenangkan Anda saat menjalankan usaha?","Pengalaman paling menyenangkan adalah ketika promosi yang saya lakukan berhasil menarik banyak pelanggan baru dan penjualan meningkat."),("Pernahkah Anda mengalami pengalaman kurang menyenangkan saat menjalankan usaha?","Ya, pernah. Kadang ada kendala saat proses promosi atau saat pelanggan membatalkan pesanan secara tiba-tiba."),("Hal apa yang biasanya membuat Anda merasa repot atau sulit saat mengelola usaha?","Yang sering terasa sulit adalah saat promosi, karena harus dilakukan manual dan memakan waktu, apalagi kalau harus kirim ke banyak pelanggan."),("Bagaimana perasaan Anda ketika mengalami kendala saat menggunakan aplikasi?","Biasanya saya merasa bingung dan sedikit kesal, tapi tetap mencoba pelan-pelan sampai bisa, atau kembali ke cara yang sudah biasa."),("Menurut Anda, fitur atau layanan apa yang membuat pengelolaan usaha menjadi lebih mudah?","Fitur yang mempermudah adalah yang bisa membantu promosi lebih cepat dan praktis, serta mudah digunakan tanpa perlu banyak belajar."),("Menurut Anda, apa yang sebaiknya ditingkatkan dari aplikasi bisnis?","Menurut saya, aplikasi sebaiknya dibuat lebih sederhana dan mudah dipahami, serta memiliki fitur otomatis agar tidak perlu banyak proses manual."),("Jika bisa menambahkan satu fitur pada aplikasi bisnis, apa yang ingin Anda tambahkan?","Saya ingin ada fitur promosi otomatis yang bisa membantu menjangkau lebih banyak pelanggan tanpa harus dilakukan secara manual.")],
    [("Bisa perkenalkan diri Anda terlebih dahulu?","Nama saya Susanto Hari Wibowo, pekerjaan wiraswasta, usia 44 tahun."),("Bisa ceritakan tentang keseharian Anda?","Keseharian saya mulai jam 6 pagi bersih-bersih toko dan menata stok yang masih ada di gudang menatanya ke display."),("Apa yang biasanya Anda lakukan ketika mengelola toko?","Kegiatan utama saya melayani pembeli eceran pagi hari."),("Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?","Hal paling penting bagi saya itu ketersediaan barang, jangan sampai pelanggan datang tapi stok kosong."),("Apa pengalaman terbaik Anda saat berjualan?","Pengalaman terbaik itu kalau ada yang borong banyak saat stok lagi penuh."),("Apa pengalaman terburuk yang pernah Anda alami?","Pengalaman terburuk itu kalau pesan stok online dari supplier baru di Facebook, fotonya bagus tapi pas datang kualitas plastiknya tipis dan gampang robek."),("Bagaimana cara Anda mengatasi kendala tersebut?","Saya mencoba mencari supplier lain yang lebih terpercaya dan memeriksa kualitas barang sebelum membeli dalam jumlah banyak."),("Kendala apa saja yang biasanya Anda hadapi saat mengelola stok?","Kendala paling sering itu stok tidak terukur."),("Mengapa hal ini menjadi masalah bagi Anda?","Ini jadi masalah karena saya bisa kehilangan pelanggan harian kalau barang yang mereka cari tidak ada terus."),("Menurut Anda, apa yang bisa membuat pengelolaan toko lebih mudah?","Saya perlu aplikasi yang mencatat jumlah stok barang serta harga dari setiap supplier.")],
    [("Perkenalkan diri Anda","Nama saya Haris Ridho Ramadhan, saya merupakan mahasiswa aktif di Institut Teknologi Sepuluh Nopember Jurusan Desain Produk."),("Bagaimana aktivitas anda sehari-hari sebagai mahasiswa?","Saya setiap hari Senin-Jumat melaksanakan kegiatan yang sama berulang, yaitu pergi kuliah, mengerjakan tugas, dan istirahat."),("Apakah anda memiliki perasaan jenuh?","Ya, maka dari itu saya membuka usaha kecil-kecilan bersama 5 orang teman saya yaitu menyediakan jasa editing dan desain, seperti pembuatan pamflet, logo, dan aset UI."),("Apa pengalaman terbaik dan terburuk selama menjalankan usaha?","Pengalaman terbaik adalah mendapatkan apresiasi balik dari klien dan mendapatkan hasil berupa uang. Kendala: pemasaran produk yang kurang berkembang, hanya di lingkup pertemanan."),("Mengapa kendala tersebut menjadi masalah?","Sepinya pesanan project yang menyebabkan saya dan teman mendapatkan pemasukan yang kurang."),("Bagaimana cara anda dan tim mengatasi permasalahan tersebut?","Berpikir untuk memasarkan produk di platform e-commerce seperti TikTok Shop, Shopee, Lazada. Namun masih awam dalam menjual jasa melalui platform e-commerce."),("Apakah anda tetap menggunakan metode pemasaran yang baru?","Ya, tetap menggunakan metode pemasaran yang baru, dengan belajar tentang algoritma e-commerce dan terus menumbuhkan inovasi."),("Apa harapanmu untuk aplikasi e-commerce?","Memberikan panduan cara memasang produk, dan diadakan fitur kategori sesuai jenis produk/jasa yang ditawarkan."),("Apakah anda tetap memberikan yang terbaik ke pelanggan?","Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain.")],
    [("Perkenalkan diri anda?","Widya Ony berusia 19 tahun, Mahasiswa semester 2 Politeknik Negeri Madiun."),("Apa yang biasa anda lakukan saat menggunakan TikTokShop?","Mencari barang yang diinginkan juga membandingkan harga dan ongkir, supaya dapat barang yang paling terjangkau."),("Apa yang paling penting bagi anda?","Kejujuran produk dan efisiensi biaya, gratis ongkir dan promo diskon sangat membantu menghemat uang saku."),("Apa hal yang paling penting saat melakukan aktivitas tersebut?",'Pengalaman terbaik saat mendapatkan harga jauh lebih murah karena promo "flash sale" saat Live, dan proses checkout yang sangat cepat.'),("Kendala apa yang sering anda hadapi?","Live chat sangat mengganggu, sulit mengatur komentar, stiker dan pop up promosi mengumpuk."),("Apakah anda pernah menggunakan fitur Live Streaming?","Sudah pernah, tapi hanya sebagai penonton."),("Apa yang bisa membuat TikTokShop lebih lebih mudah digunakan?","Fitur filter, sistem notifikasi spam, dan fokus pada status pengiriman."),("Apa yang paling anda harapkan saat menggunakan TikTokShop?",'Jaminan kualitas barang yang lebih ketat dari pihak aplikasi agar tidak ada produk yang "zonk".'),("Jika bisa memperbaiki satu hal apa yang akan anda ubah?","Sistem filter di keranjang, saat ini sulit menyaring barang berdasarkan kategori tertentu dari daftar yang panjang."),("Solusi ideal menurut anda?",'Fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan.')],
    [("Perkenalkan diri anda, pernahkah menggunakan aplikasi UMKM?","Saya Zaskiya Sandi A.A., pengguna aktif berbagai aplikasi digital. Pernah menggunakan Shopee, TikTok Shop, dan Gojek hampir setiap minggu."),("Pernah mengalami kendala pembelian gagal?","Ya, pernah. Penyebabnya: metode pembayaran error, ongkos kirim terlalu mahal, stok barang tiba-tiba habis."),("Kesulitan mencari fitur yang ingin digunakan?","Ya, terkadang. Tampilan terlalu ramai (banyak promo/banner) dan menu terlalu banyak namun tidak terorganisir."),("Apa yang harus ditambah/dirubah/dihapus di halaman depan?","Menyederhanakan tampilan, mengelompokkan fitur sesuai kategori yang jelas, mengurangi fitur yang jarang digunakan."),("Bagaimana alur pembelian yang ideal?","Pencarian produk cepat dan akurat, informasi produk jelas, pilihan pembayaran lengkap, checkout singkat, konfirmasi pesanan jelas.")],
]

def make_interview_table(qa_pairs):
    rows = []
    for q, a in qa_pairs:
        rows.append(f'                    <tr>\n                      <th>Question {q}</th>\n                      <td>{a}</td>\n                    </tr>')
    return (
        '<div class="persona__interview-row">\n'
        '              <div class="persona__section-box">\n'
        '                <h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>\n'
        '                <div class="persona__interview-grid">\n'
        '                  <div class="interview__table-wrapper">\n'
        '                    <table class="interview__table">\n'
        '                      <tbody>\n'
        + '\n'.join(rows) + '\n'
        '                      </tbody>\n'
        '                    </table>\n'
        '                  </div>\n'
        '                </div>\n'
        '              </div>\n'
        '            </div>'
    )

# Find persona section
persona_start = content.find('id="persona"')
persona_section_start = content.rfind('<section', 0, persona_start)
define_start = content.find('<!-- Define Problem Statement', persona_start)

persona_html = content[persona_section_start:define_start]

# Extract panels from persona_html
panels = []
for i in range(5):
    marker = f'data-panel="{i}"'
    p_start = persona_html.find(marker)
    if p_start == -1:
        continue
    p_start = persona_html.rfind('<div', 0, p_start)
    if i < 4:
        next_marker = f'data-panel="{i+1}"'
        p_end = persona_html.find(next_marker, p_start + 1)
        p_end = persona_html.rfind('<div', 0, p_end)
    else:
        p_end = len(persona_html)
    panels.append(persona_html[p_start:p_end])

# Process each panel
new_panels = []
for i, panel in enumerate(panels):
    # Count opens and closes
    opens = len(re.findall(r'<div[\s>]', panel))
    closes = panel.count('</div>')
    extra = closes - opens
    
    if extra > 0:
        # Remove trailing extra </div>
        for _ in range(extra):
            panel = re.sub(r'\s*</div>\s*$', '\n', panel, count=1)
    
    # Replace interview section if it exists as sticky notes
    interview_start = panel.find('Interview Data')
    if interview_start != -1:
        # Find the interview row
        int_row_start = panel.rfind('<div', 0, interview_start)
        # Find end using depth tracking
        depth = 0
        int_row_end = -1
        for m in re.finditer(r'<div[\s>]|</div>', panel[int_row_start:]):
            if m.group().startswith('<div'):
                depth += 1
            else:
                depth -= 1
            if depth == 0:
                int_row_end = int_row_start + m.end()
                break
        
        if int_row_end != -1:
            old_interview = panel[int_row_start:int_row_end]
            if 'persona__sticky' in old_interview:
                # Replace sticky notes with table
                panel = panel[:int_row_start] + make_interview_table(interview_data[i]) + panel[int_row_end:]
    
    new_panels.append(panel)

# Rebuild persona section
section_header = content[persona_section_start:content.find('data-panel="0"', persona_section_start)]
section_header = section_header[:section_header.rfind('<div')]

new_persona = section_header
for i, panel in enumerate(new_panels):
    new_persona += f'\n        <!-- === Panel {i+1} === -->\n'
    new_persona += '        ' + panel
    if i < 4:
        new_persona += '\n\n'
    else:
        new_persona += '\n\n      </div>\n    </section>\n\n'

# Replace in content
content = content[:persona_section_start] + new_persona + content[define_start:]

with open('c:/semester 2/Web UAS/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('c:/semester 2/Web UAS/index.html', 'r', encoding='utf-8') as f:
    result = f.read()

opens = len(re.findall(r'<div[\s>]', result))
closes = result.count('</div>')
print(f"Overall: opens={opens}, closes={closes}, diff={opens-closes}")

for i in range(5):
    marker = f'data-panel="{i}"'
    ps = result.find(marker)
    if ps == -1: continue
    ps = result.rfind('<div', 0, ps)
    if i < 4:
        pe = result.find(f'data-panel="{i+1}"', ps+1)
        pe = result.rfind('<div', 0, pe)
    else:
        pe = result.find('<!-- Define Problem Statement', ps)
    p = result[ps:pe]
    po = len(re.findall(r'<div[\s>]', p))
    pc = p.count('</div>')
    has_j = 'journey-table' in p
    has_i = 'interview__table' in p
    print(f"Panel {i}: opens={po}, closes={pc}, diff={po-pc}, journey={has_j}, interview={has_i}")

print("Done!")
