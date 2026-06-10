"""
Full reconstruction script:
1. Start from .bak (has all 5 panels with old format)
2. Re-apply: interview table conversion for all 5 panels
3. Re-apply: Define Problem Statement section (already in current file)
4. Re-apply: proper closing tags
"""
import re

# Read the backup file (has correct panel structure with all 5 panels)
bak = open('index.html.bak', 'r', encoding='utf-8').read()

# Read the current broken file (has Define section and updated CSS)
current = open('index.html', 'r', encoding='utf-8').read()

# ============================================================
# Step 1: Extract the Define section from the current file
# ============================================================
define_start = current.find('    <!-- ============================== DEFINE')
if define_start == -1:
    define_start = current.find('<section class="define"')
define_section = current[define_start:]

print(f"Define section extracted: {len(define_section)} chars")

# ============================================================
# Step 2: Extract the persona section from .bak (all 5 panels intact)
# ============================================================
persona_start = bak.find('<!-- ============================== USER PERSONA')
persona_section_end_marker = bak.find('</section>', persona_start)
persona_section = bak[persona_start:persona_section_end_marker + len('</section>')]

# Everything before persona section
header_section = bak[:persona_start]

print(f"Persona section extracted: {len(persona_section)} chars")
print(f"Header section: {len(header_section)} chars")

# ============================================================
# Step 3: Reconstruct the file = header + persona + define
# ============================================================
new_content = header_section + persona_section + '\n\n' + define_section

# ============================================================
# Step 4: Convert interview data to table format for all 5 panels
# ============================================================

# Interview data for each panel
interview_data = {
    'Fikri Ramadhan': [
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
    'Susanto Hari Wibowo': [
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
    'Haris': [
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
    'Widya': [
        ("Perkenalkan diri anda? nama, pekerjaan, dan usia.",
         "Widya Ony berusia 19 tahun, Mahasiswa semester 2 Politeknik Negeri Madiun."),
        ("Apa yang biasa anda lakukan saat menggunakan aplikasi TikTokShop?",
         "Mencari barang yang diinginkan juga membandingkan harga dan ongkir, supaya dapat barang yang paling terjangkau buat kantong mahasiswa."),
        ("Apa yang paling penting bagi anda?",
         "Yang paling penting adalah kejujuran produk dan efisiensi biaya, gratis ongkir dan promo diskon sangat membantu menghemat uang saku, terutama untuk kebutuhan kuliah mendesak."),
        ("Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?",
         'Pengalaman terbaik itu saat mendapatkan harga yang jauh lebih murah karena dapat promo "flash sale" saat Live, dan juga proses checkout yang sangat cepat yang gak perlu pindah aplikasi.'),
        ("Kendala apa yang sering anda hadapi saat menggunakan TikTokShop?",
         "Sangat mengganggu live chat, sulit mengatur komentar, stiker dan pop up promosi mengumpuk."),
        ("Apakah anda pernah menggunakan fitur 'Live Streaming'?",
         "Sudah pernah, tapi hanya sebagai penonton."),
        ("Apa yang bisa membuat TikTokShop lebih mudah digunakan?",
         "Fitur filter, sistem notifikasi spam, dan fokus pada status pengiriman (dikirim dari wilayah), aplikasi terasa jauh lebih nyaman."),
        ("Apa yang paling anda harapkan saat menggunakan TikTokShop?",
         'Harapannya ada jaminan kualitas barang yang lebih ketat dari pihak aplikasi agar tidak ada lagi produk yang "zonk".'),
        ("Jika bisa memperbaiki satu hal apa yang akan anda ubah?",
         'Saya ingin mengubah sistem filter di keranjang, saat ini jika kita punya banyak barang dari toko berbeda, sulit untuk menyaring barang berdasarkan kategori tertentu tanpa harus mencarinya satu per satu di daftar yang panjang.'),
        ("Kalau berandai-andai, apa solusi ideal menurut anda?",
         'Adanya fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan, jadi tidak perlu bolak-balik buka profil toko.'),
    ],
    'Zaskiya': [
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

# For each panel, replace the interview grid placeholder with table
def build_table_html(qa_list):
    rows = []
    for q, a in qa_list:
        rows.append(f'                    <tr>\n                      <th>Question {q}</th>\n                      <td>{a}</td>\n                    </tr>')
    
    return '''<div class="persona__interview-grid">
                <div class="interview__table-wrapper">
                  <table class="interview__table">
                    <tbody>
''' + '\n'.join(rows) + '''
                    </tbody>
                  </table>
                </div>
              </div>'''

# Replace interview grids in each panel
# Find each panel's interview grid and replace
panels_done = 0
for panel_name, qa_list in interview_data.items():
    # Find the panel by name pattern
    # Each panel has an "Interview Data" section with placeholder grid
    table_html = build_table_html(qa_list)
    
    # Find and replace the interview grid for this panel
    # Pattern: from "<!-- Interview Data -->" to the closing of persona__interview-grid
    old_pattern = re.compile(
        r'(<!-- Interview Data -->\s*'
        r'<div class="persona__interview-row">\s*'
        r'<div class="persona__section-box">\s*'
        r'<h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>\s*)'
        r'(<div class="persona__interview-grid">.*?</div>\s*</div>\s*</div>\s*</div>)',
        re.DOTALL
    )
    
    match = old_pattern.search(new_content)
    if match:
        replacement = match.group(1) + table_html
        new_content = new_content[:match.start()] + replacement + new_content[match.end():]
        panels_done += 1
        print(f"  OK: Replaced interview data for panel {panels_done} ({panel_name}: {len(qa_list)} Q&A)")
    else:
        print(f"  SKIP: No more placeholder grids found (done {panels_done}/5)")
        break

# ============================================================
# Step 5: Write the reconstructed file
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nReconstruction complete!")
print(f"Panels with interview data: {panels_done}/5")
print(f"Total lines: {new_content.count(chr(10))}")

# Verify
markers = [m.start() for m in re.finditer(r'<!-- Interview Data -->', new_content)]
print(f"Interview Data markers: {len(markers)}")
print(f"Panel 5 present: {'Panel 5' in new_content}")
print(f"Define section: {'class=\"define\"' in new_content}")
