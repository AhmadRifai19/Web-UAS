import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# All interview data mapped to panel index
# Panel 0: Fikri Ramadhan
# Panel 1: Susanto Hari Wibowo
# Panel 2: Haris Ridho Ramadhan (Haris Wahyu Ramadhani in HTML)
# Panel 3: Widya (already done)
# Panel 4: Zaskiya Sandi A.A.

panels = {
    0: [  # Fikri Ramadhan - 10 Q&A
        ("Bisakah perkenalkan diri Anda secara singkat? (Nama, usia, dan pekerjaan)",
         "Nama saya Fikri Ramadhan, usia 21 tahun, menjalankan usaha kecil di bidang penjualan produk secara online."),
        ("Bisa ceritakan aktivitas sehari-hari Anda dan kapasitas bisnis Anda mengelola usaha?",
         "Sehari-hari saya mengelola usaha, seperti menyiapkan produk, melayani pelanggan, dan promosi. Saya biasanya menggunakan aplikasi saat ingin promosi atau mengatur pesanan, terutama di waktu senggang."),
        ("Platform atau fitur apa yang paling sering Anda gunakan? (WhatsApp, Instagram, marketplace, dll?)",
         "Saya paling sering menggunakan WhatsApp dan Instagram untuk promosi dan komunikasi dengan pelanggan."),
        ("Apa pengalaman paling menyenangkan Anda saat menjalankan usaha?",
         "Pengalaman paling menyenangkan adalah ketika promosi yang saya lakukan berhasil menarik banyak pelanggan baru dan penjualan meningkat. Apalagi jika prosesnya terasa lebih mudah dan tidak terlalu rumit, itu sangat membantu dalam mengelola usaha."),
        ("Pernahkah Anda mengalami pengalaman kurang menyenangkan saat menjalankan usaha? Bisa ceritakan?",
         "Ya, pernah. Kadang ada kendala saat proses promosi atau saat pelanggan membatalkan pesanan secara tiba-tiba, yang membuat usaha menjadi kurang lancar."),
        ("Hal apa yang biasanya membuat Anda merasa repot atau sulit saat mengelola usaha?",
         "Yang sering terasa sulit adalah saat promosi, karena harus dilakukan manual dan memakan waktu, apalagi kalau harus kirim ke banyak pelanggan."),
        ("Bagaimana perasaan Anda ketika mengalami kendala saat menggunakan aplikasi atau menjalankan usaha?",
         "Biasanya saya merasa bingung dan sedikit kesal, tapi tetap mencoba pelan-pelan sampai bisa, atau kembali ke cara yang sudah biasa."),
        ("Menurut Anda, fitur atau layanan apa yang membuat pengelolaan usaha menjadi lebih mudah?",
         "Fitur yang mempermudah adalah yang bisa membantu promosi lebih cepat dan praktis, serta mudah digunakan tanpa perlu banyak belajar."),
        ("Menurut Anda, apa yang sebaiknya ditingkatkan dari aplikasi bisnis agar lebih membantu usaha Anda?",
         "Menurut saya, aplikasi sebaiknya dibuat lebih sederhana dan mudah dipahami, serta memiliki fitur otomatis agar tidak perlu banyak proses manual."),
        ("Jika bisa mengubah atau menambahkan satu fitur pada aplikasi bisnis, apa yang ingin Anda tambahkan?",
         "Saya ingin ada fitur promosi otomatis yang bisa membantu menjangkau lebih banyak pelanggan tanpa harus dilakukan secara manual, supaya lebih praktis dan hemat waktu."),
    ],
    1: [  # Susanto Hari Wibowo - 10 Q&A
        ("Bisa perkenalkan diri Anda terlebih dahulu? (Nama, pekerjaan, dan usia)",
         "Nama saya Susanto Hari Wibowo, pekerjaan wiraswasta, usia 44 tahun."),
        ("Bisa ceritakan tentang keseharian Anda?",
         "Keseharian saya mulai jam 6 pagi bersih-bersih toko dan menata stok yang masih ada di gudang menatanya ke display."),
        ("Apa yang biasanya Anda lakukan ketika mengelola toko sembako dan plastik?",
         "Kegiatan utama saya melayani pembeli eceran pagi hari."),
        ("Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?",
         "Hal paling penting bagi saya itu ketersediaan barang, jangan sampai pelanggan datang tapi stok plastik atau sembako yang dicari kosong."),
        ("Apa pengalaman terbaik Anda saat berjualan sembako dan plastik?",
         "Pengalaman terbaik itu kalau ada yang borong banyak saat stok lagi penuh."),
        ("Apa pengalaman terburuk yang pernah Anda alami?",
         "Pengalaman terburuk itu kalau pesan stok online dari supplier baru di Facebook, fotonya bagus tapi pas datang kualitas plastiknya tipis dan gampang robek."),
        ("Bagaimana cara Anda mengatasi kendala tersebut?",
         "Saya mencoba mencari supplier lain yang lebih terpercaya dan memeriksa kualitas barang sebelum membeli dalam jumlah banyak."),
        ("Kendala apa saja yang biasanya Anda hadapi saat mengelola stok dan supplier?",
         "Kendala paling sering itu stok tidak terukur."),
        ("Mengapa hal ini menjadi masalah bagi Anda?",
         "Ini jadi masalah karena saya bisa kehilangan pelanggan harian kalau barang yang mereka cari tidak ada terus."),
        ("Menurut Anda, apa yang bisa membuat pengelolaan toko lebih mudah?",
         "Saya perlu aplikasi yang mencatat jumlah stok barang serta harga dari setiap supplier."),
    ],
    2: [  # Haris Ridho Ramadhan - 9 Q&A (fill 10th with placeholder)
        ("Perkenalkan diri Anda (Nama dan aktivitas yang anda lakukan setiap hari)",
         "Nama saya Haris Ridho Ramadhan, saya merupakan mahasiswa aktif di Institut Teknologi Sepuluh Nopember Jurusan Desain Produk."),
        ("Bagaimana aktivitas anda sehari-hari dalam menjalankan kewajiban sebagai mahasiswa?",
         "Saya setiap hari Senin-Jumat melaksanakan kegiatan yang sama berulang, yaitu pergi kuliah, mengerjakan tugas, dan istirahat."),
        ("Apakah anda memiliki perasaan jenuh karena melaksanakan kegiatan yang berulang?",
         "Ya, maka dari itu saya membuka usaha kecil-kecilan bersama 5 orang teman saya yaitu menyediakan jasa editing dan desain, seperti pembuatan pamflet, logo, dan aset UI."),
        ("Apa pengalaman terbaik dan terburuk serta kendala yang anda alami selama menjalankan usaha?",
         "Pengalaman terbaik tentunya adalah jika mendapatkan apresiasi balik dari klien dan mendapatkan hasil berupa uang. Kendala yang dihadapi mungkin pemasaran produk yang kurang bisa berkembang, sebab hanya di lingkup pertemanan dan dari mulut ke mulut."),
        ("Mengapa kendala tersebut menjadi masalah?",
         "Hal tersebut dapat menjadi kendala sebab sepinya pesanan project yang menyebabkan saya dan teman mendapatkan pemasukan yang kurang."),
        ("Bagaimana cara anda dan tim dalam mengatasi permasalahan tersebut?",
         "Saya bersama rekan saya berpikir untuk memulai memasarkan produk di platform e-commerce seperti TikTok Shop, Shopee, Lazada, dan Dill. Namun saya bersama rekan tim saya masih awam dalam menjual dan memasarkan jasa usaha melalui platform e-commerce."),
        ("Lalu apakah anda tetap menggunakan metode pemasaran yang lama atau menggunakan metode pemasaran yang baru?",
         "Saya bersama rekan tim tetap menggunakan metode pemasaran yang baru, dengan belajar tentang algoritma e-commerce dan terus menumbuhkan inovasi yang update untuk menarik pelanggan dan meningkatkan produktivitas pesanan."),
        ("Apa harapanmu untuk aplikasi e-commerce agar lebih mudah dipahami dan digunakan untuk pengguna baru?",
         "Mungkin memberikan panduan terkait cara memasang produk, dan diadakan fitur 'kategori' sesuai jenis produk/jasa yang ditawarkan, agar memudahkan pengguna untuk mengetahui produk/jasa yang kita tawarkan."),
        ("Apakah jika produk anda berhasil masuk ke dalam platform e-commerce, anda tetap memberikan yang terbaik ke pelanggan?",
         "Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain yang kami tawarkan."),
    ],
    4: [  # Zaskiya Sandi A.A. - 5 Q&A (fill rest with placeholder)
        ("Perkenalkan diri anda, dan apakah anda pernah menggunakan aplikasi UMKM seperti Shopee, Tokopedia, TikTok Shop ataupun Gojek?",
         "Perkenalkan saya Zaskiya Sandi A.A. Saya termasuk pengguna aktif berbagai aplikasi digital. Saya pernah menggunakan aplikasi UMKM seperti Shopee, TikTok Shop, dan Gojek. Saya menggunakan aplikasi-aplikasi tersebut cukup sering, hampir setiap minggu, terutama untuk membeli kebutuhan sehari-hari, makanan, dan barang online."),
        ("Pada saat ingin melakukan pembelian apakah anda pernah mengalami kendala yang membuat pembelian gagal? Apa yang biasanya membuat anda batal membeli?",
         "Ya, saya pernah mengalami kendala yang membuat pembelian gagal. Beberapa hal yang biasanya menyebabkan saya batal membeli yaitu metode pembayaran error atau tidak tersedia, ongkos kirim terlalu mahal, dan stok barang tiba-tiba habis."),
        ("Dengan banyak fitur yang tersedia apakah anda mengalami kesulitan dalam mencari fitur yang ingin anda gunakan?",
         "Ya, terkadang saya mengalami kesulitan. Hal yang menurut saya menyulitkan adalah tampilan terlalu ramai (banyak promo/banner) dan menu terlalu banyak namun tidak terorganisir dengan baik."),
        ("Menurut anda untuk mempermudah aplikasi tersebut untuk digunakan apakah yang harus ditambahkan, dirubah atau bahkan dihapus di halaman depan aplikasi?",
         "Menurut saya, agar aplikasi lebih mudah digunakan perlu menyederhanakan tampilan (tidak terlalu banyak banner), selanjutnya mengelompokkan fitur sesuai kategori yang jelas, dan yang terakhir menghapus atau mengurangi fitur yang jarang digunakan di halaman utama."),
        ("Menurut anda untuk mempermudah dalam melakukan pembelian, bagaimana alur jalannya pembelian agar mempermudah anda dalam membeli?",
         "Pencarian produk yang cepat dan akurat, informasi produk yang jelas (harga, deskripsi, dan ulasan), pilihan metode pembayaran yang lengkap dan mudah, proses checkout yang singkat (tidak terlalu banyak langkah), konfirmasi pesanan yang jelas."),
    ],
}

def build_qa_html(qa_list):
    """Build HTML for Q&A items, filling up to 10 with placeholders"""
    items = []
    for i in range(10):
        if i < len(qa_list):
            q, a = qa_list[i]
        else:
            q, a = "[Isi Pertanyaan {} di sini]".format(i + 1), "[Isi Jawaban {} di sini]".format(i + 1)
        
        item = '''
                  <div class="interview__qa-item">
                    <div class="interview__sticky--red">
                      <strong>Question {}:</strong><br>
                      {}
                    </div>
                    <div class="interview__sticky--yellow">
                      <strong>Answer:</strong><br>
                      {}
                    </div>
                  </div>'''.format(i + 1, q, a)
        items.append(item)
    return '\n'.join(items)

# Find all interview grids
placeholder_pattern = re.compile(
    r'(<div class="persona__interview-grid">)\s*\n(.*?)\n(\s*</div>\s*</div>\s*</div>\s*</div>)',
    re.DOTALL
)

all_matches = list(placeholder_pattern.finditer(content))
print(f"Found {len(all_matches)} interview grids")

# Replace from highest index to lowest to avoid position shifting
for panel_idx in sorted(panels.keys(), reverse=True):
    if panel_idx < len(all_matches):
        match = all_matches[panel_idx]
        qa_list = panels[panel_idx]
        
        new_grid_content = build_qa_html(qa_list)
        new_html = f'{match.group(1)}\n{new_grid_content}\n{match.group(3)}'
        
        content = content[:match.start()] + new_html + content[match.end():]
        
        name_map = {0: "Fikri Ramadhan", 1: "Susanto Hari Wibowo", 2: "Haris Ridho Ramadhan", 4: "Zaskiya Sandi A.A."}
        print(f"OK: Inserted {len(qa_list)} Q&A for {name_map[panel_idx]} (Panel {panel_idx})")
    else:
        print(f"ERROR: Panel index {panel_idx} out of range")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! All interview data inserted.")
