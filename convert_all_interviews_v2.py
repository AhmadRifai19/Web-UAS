import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Interview data for each panel (in order)
all_data = [
    # Panel 1: Fikri Ramadhan
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
    # Panel 2: Susanto Hari Wibowo
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
    # Panel 3: Haris Ridho Ramadhan
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
    # Panel 4: Widya Ony Yusnita Rahayu
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
    # Panel 5: Zaskiya Sandi A.A.
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

def build_table(qa_list):
    rows = []
    for q, a in qa_list:
        rows.append(f'                    <tr>\n                      <th>Question {q}</th>\n                      <td>{a}</td>\n                    </tr>')
    return '\n'.join(rows)

# Pattern to match the entire interview section in each panel
# From "<!-- Interview Data -->" through all the Q&A items and closing divs
interview_pattern = re.compile(
    r'(<!-- Interview Data -->\s*'
    r'<div class="persona__interview-row">\s*'
    r'<div class="persona__section-box">\s*'
    r'<h4 class="persona__section-title persona__section-title--blue">Interview Data</h4>\s*)'
    r'<div class="interview__qa-list">'
    r'.*?'  # all Q&A items
    r'</div>\s*'  # close interview__qa-list
    r'(\s*</div>\s*'  # close section-box
    r'</div>)',  # close interview-row
    re.DOTALL
)

matches = list(interview_pattern.finditer(content))
print(f"Found {len(matches)} interview sections")

# Replace from last to first
for i, match in enumerate(reversed(matches)):
    panel_idx = len(matches) - 1 - i
    qa_list = all_data[panel_idx]
    table_rows = build_table(qa_list)
    
    replacement = (
        match.group(1) +
        '<div class="persona__interview-grid">\n'
        '                <div class="interview__table-wrapper">\n'
        '                  <table class="interview__table">\n'
        '                    <tbody>\n' +
        table_rows + '\n'
        '                    </tbody>\n'
        '                  </table>\n'
        '                </div>\n'
        '              </div>' +
        match.group(2)
    )
    
    content = content[:match.start()] + replacement + content[match.end():]
    names = ['Fikri', 'Susanto', 'Haris', 'Widya', 'Zaskiya']
    print(f"  OK: Panel {panel_idx+1} ({names[panel_idx]}): {len(qa_list)} Q&A")

# Also update the section title color from blue to orange
content = content.replace(
    'persona__section-title--blue">Interview Data</h4>',
    'persona__section-title--orange">Interview Data</h4>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone! All interview sections converted to table format.")
print(f"Total lines: {content.count(chr(10))}")
