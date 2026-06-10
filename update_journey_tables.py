import re

html_path = r'c:\semester 2\Web UAS\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── Journey table data from images ───

journey_data = {
    0: {  # Fikri Ramadhan (Frame 116)
        "name": "FIKRI RAMADHAN",
        "aktivitas": [
            ["Merasa penjualan menurun atau tidak berkembang", "Mulai mencari cara promosi yang lebih efektif", "Mendengar atau melihat aplikasi bisnis dari media sosial/teman"],
            ["Mencari dan mencoba beberapa aplikasi", "Membandingkan fitur dan kemudahan penggunaan", "Bertanya ke teman atau melihat review"],
            ["Download dan daftar akun", "Mulai eksplorasi fitur dasar", "Mencoba menjalankan fungsi utama aplikasi"],
            ["Mulai upload produk", "Mengatur informasi usaha", "Mencoba fitur promosi atau penjualan"],
            ["Menggunakan aplikasi secara rutin", "Mulai merasakan manfaat", "Merekomendasikan ke teman sesama UMKM"],
        ],
        "emosi": [
            ["Khawatir usaha tidak berkembang", "Takut salah aplikasi", "Bingung harus mulai dari mana", "Ada harapan menemukan solusi"],
            ["Ragu dalam memilih", "Takut salah aplikasi", "Sedikit tertarik tapi belum yakin"],
            ["Penasaran dengan hasilnya", "Sedikit bingung saat awal penggunaan", "Berharap aplikasi membantu usaha"],
            ["Mulai memahami sistem", "Sedikit lebih percaya diri", "Masih butuh ajaran"],
            ["Puas dengan hasil", "Senang karena usaha berkembang", "Percaya pada aplikasi"],
        ],
        "pain_point": [
            ["Tidak tahu strategi promosi yang tepat", "Promosi masih manual dan kurang efektif", "Minim pengetahuan digital marketing"],
            ["Terlalu banyak pilihan aplikasi", "Tidak paham fungsi tiap fitur", "Tampilan aplikasi kadang membingungkan"],
            ["Tidak tahu langkah awal penggunaan", "Takut salah klik atau salah setting", "Kurang panduan saat pertama kali masuk"],
            ["Proses input data terasa lama", "Beberapa fitur belum dipahami sepenuhnya", "Hasil belum langsung terlihat"],
            ["Butuh fitur lanjutan untuk scale up", "Ingin performa lebih optimal", "Mulai butuh analisis data"],
        ],
        "peluang_solusi": [
            ["Edukasi dasar bisnis & promosi dalam aplikasi", "Rekomendasi fitur sesuai kebutuhan user", "Konten tips sederhana (tidak terlalu teknis)"],
            ["Tampilan UI sederhana & intuitif", "Penjelasan fitur dengan bahasa mudah", "Demo atau preview penggunaan aplikasi"],
            ["Tutorial step-by-step yang interaktif", "Onboarding sederhana dan tidak membingungkan", "Bantuan langsung (tooltip / panduan cepat)"],
            ["Fitur otomatis (auto-fill / auto-promosi)", "Shortcut untuk proses cepat", "Panduan lanjutan berbasis kebutuhan user"],
            ["Program loyalitas atau reward", "Fitur advanced (opsional, tidak memaksa)", "Insight penjualan & laporan sederhana"],
        ],
    },
    1: {  # Susanto Hari Wibowo (Frame 115)
        "name": "SUSANTO HARI WIBOWO",
        "aktivitas": [
            ["Mengecek stok fisik di gudang.", "Menyadari stok plastik/sembako tertentu mulai habis."],
            ["Membuka Facebook untuk mencari supplier baru.", "Melihat foto-foto produk yang diposting."],
            ["Menghubungi supplier melalui inbox FB atau telepon.", "Melakukan kesepakatan harga dan jumlah pesanan."],
            ["Menunggu barang datang ke toko.", "Menerima paket dari kurir/supplier."],
            ["Mengecek kualitas fisik barang (ketebalan plastik).", "Menata barang baru ke rak display."],
        ],
        "emosi": [
            ["Waspada (takut stok kosong saat pelanggan datang)."],
            ["Berharap (ingin menemukan harga dan kualitas terbaik)."],
            ["Ragu (takut tertipu atau kualitas tidak sesuai foto)."],
            ["Tidak Sabar (menunggu kepastian waktu sampai)."],
            ["Kecewa/Marah (jika kualitas plastik tipis/gampang robek)."],
        ],
        "pain_point": [
            ["Stok tidak terukur secara akurat karena manual.", "Tumpukan barang di gudang menghalangi pandangan."],
            ["Banyak penipuan di platform Facebook.", "Representasi foto seringkali tidak jujur."],
            ["Proses pemesanan manual lewat chat/telp sangat melelahkan.", "Data pesanan sering hilang di chat."],
            ["Tidak ada kepastian waktu kapan barang sampai."],
            ["Kualitas barang yang datang seringkali jauh di bawah standar."],
        ],
        "peluang_solusi": [
            ["Aplikasi pencatatan stok otomatis."],
            ["Sistem rating dan ulasan supplier yang asli."],
            ['Fitur "One-Click Ordering" tanpa harus chat panjang lebar.', "Pencatatan riwayat transaksi yang rapi."],
            ["Fitur pelacakan pengiriman secara real-time."],
            ["Jaminan kualitas atau fitur komplain jika barang rusak/jelek."],
        ],
    },
    2: {  # Haris Ridho Ramadhan (Frame 118)
        "name": "HARIS RIDHO RAMADHAN",
        "aktivitas": [
            ["Mulai sadar kalau pemasaran usahanya masih kurang luas dan hanya dikenal di lingkungan teman"],
            ["Cari-cari platform jualan / e-commerce yang cocok untuk usaha jasa dan produknya"],
            ["Daftar akun dan mulai setup toko / profil usaha"],
            ["Upload jasa/produk lalu mulai menerima dan mengelola pesanan"],
            ["Menggunakan platform secara rutin untuk jualan dan promosi"],
        ],
        "emosi": [
            ["Khawatir usahanya sulit berkembang kalau promosi tetap seperti sekarang"],
            ["Bingung memilih platform yang paling cocok, tapi penasaran untuk mencoba"],
            ["Semangat karena mulai mencoba hal baru, tapi agak bingung di awal"],
            ["Mulai merasa terbantu, tapi masih belajar memahami semua fitur"],
            ["Senang karena usaha lebih berkembang dan merasa platform membantu"],
        ],
        "pain_point": [
            ["Tidak tahu cara promosi digital yang efektif"],
            ["Banyak pilihan platform, jadi susah menentukan mana yang terbaik"],
            ["Bingung saat awal setup toko dan upload produk/jasa"],
            ["Sulit membagi waktu antara kuliah, tugas, dan order pelanggan"],
            ["Harus menjaga rating/reputasi toko agar pelanggan tetap percaya"],
        ],
        "peluang_solusi": [
            ["Berikan edukasi tentang manfaat platform untuk membantu usaha kecil berkembang"],
            ["Sediakan penjelasan fitur platform dengan bahasa sederhana dan mudah dipahami"],
            ["Buat onboarding yang simpel dan step-by-step untuk pemula"],
            ["Tambahkan fitur yang membantu pengelolaan pesanan lebih praktis"],
            ["Berikan insight penjualan dan tips pengembangan usaha lanjutan"],
        ],
    },
    3: {  # Widya Ony / Lasmini (Frame 117)
        "name": "WIDYA DNY YUANIKA R.",
        "aktivitas": [
            ["Merasakan kebutuhan mendesak (bawa suami ke RS), ingat rekomendasi anak/tetangga tentang Gojek, mencari dan membuka aplikasi Gojek di HP."],
            ["Mencoba memahami perbedaan GoCar dan GoRide, membaca-baca tulisan kecil pada ikon, membuka aplikasi, melihat layar penuh ikon."],
            ["Mengetuk ikon GoCar, bingung mengisi alamat (lokasi saat ini & tujuan), memilih \"Bayar Tunai\" karena tidak paham GoPay, menunggu konfirmasi driver menerima pesanan."],
            ["Menerima telepon/chat dari driver, menunggu driver tiba, naik ke kendaraan, memantau perjalanan lewat map di aplikasi."],
            ["Turun di tujuan, menerima notifikasi untuk memberi rating, bingung dan menutup notifikasi."],
        ],
        "emosi": [
            ["Khawatir, Cemas, Panik"],
            ["Kewalahan, Frustrasi, Bingung"],
            ["Harap-harap Cemas, Tidak Sabar, Tegang"],
            ["Berharap driver sopan, Sedikit Lega tapi masih Cemas"],
            ["Bersyukur, Lega"],
        ],
        "pain_point": [
            ["Teknologi bukanlah pilihan pertama, butuh dorongan situasi darurat; tidak hafal letak aplikasi."],
            ["Tampilan aplikasi terlalu ramai dan banyak ikon; banyak layanan tidak relevan (GoMassage, dll); tulisan dan ikon terlalu kecil, sulit dibaca."],
            ["Bingung cara input alamat yang benar; takut salah memencet tombol; tidak percaya dengan pembayaran digital (GoPay)."],
            ["Gugup jika driver tidak bisa menemukan lokasinya; takut dengan driver yang tidak dikenal."],
            ["Tidak mengerti tujuan memberi rating; menganggapnya merepotkan."],
        ],
        "peluang_solusi": [
            ['Fitur "SOS" atau "Darurat" di layar utama yang langsung memesan GoCar ke rumah sakit terdekat; ikon yang besar dan jelas.'],
            ['"Simple Mode" untuk user seperti Lasmini: hanya menampilkan 3 layanan utama (GoCar, GoFood, GoSend); gunakan tulisan dan ikon yang lebih besar; voice command ("OK Google, pesankan GoCar").'],
            ['Deteksi lokasi otomatis yang lebih akurat; tombol "Gunakan Lokasi Saya Sekarang" yang sangat menonjol; opsi "Bayar Tunai" sebagai default untuk user tertentu; konfirmasi pesanan dengan suara "Pesanan Anda Diterima!".'],
            ['Fitur "Bagikan Perjalanan" otomatis ke keluarga; notifikasi: "Driver Anda, Pak Budi, sedang menuju lokasi Anda."; tampilan map yang sederhana dengan foto driver yang besar.'],
            ['Rating yang lebih sederhana, misal hanya "\u263a" atau "\u2639"; pesan: "Terima kasih Ibu Lasmini, semoga suami lekas sembuh." (Personal & empatik).'],
        ],
    },
    4: {  # Zaskiya Sandi A.A. (Frame 114)
        "name": "ZASKIYA SANDI A.A.",
        "aktivitas": [
            ["Membuka aplikasi, melihat halaman utama, dan mencari fitur atau produk yang ingin dibeli."],
            ["Mengecek ketersediaan barang dan membaca detail informasi produk sebelum memutuskan."],
            ["Melanjutkan pesanan ke tahap pengiriman, melihat rincian biaya, dan mengecek ongkos kirim."],
            ["Memilih metode pembayaran yang tersedia dan mencoba menyelesaikan transaksi."],
            ["Menerima bukti bahwa transaksi telah berhasil dan pesanan sedang diproses."],
        ],
        "emosi": [
            ["Bingung / Kewalahan"],
            ["Kecewa (jika barang habis)"],
            ["Kesal (jika ongkir mahal)"],
            ["Frustrasi (jika error)"],
            ["Lega"],
        ],
        "pain_point": [
            ["Tampilan aplikasi terlalu ramai (banyak promo/banner).", "Menu terlalu banyak tapi tidak terorganisir dengan baik.", "Kesulitan mencari fitur yang ingin digunakan."],
            ["Stok barang tiba-tiba habis saat sedang dipertimbangkan untuk dibeli."],
            ["Ongkos kirim sering kali dirasa terlalu mahal.", "Alur pembelian berisiko terasa berbelit jika terlalu banyak langkah."],
            ["Metode pembayaran sering mengalami error.", "Pilihan metode pembayaran terkadang tidak tersedia."],
            ["Sering merasa khawatir jika status pesanan setelah membayar tidak langsung diperbarui."],
        ],
        "peluang_solusi": [
            ["Sederhanakan tampilan (hapus banner berlebih).", "Kelompokkan fitur sesuai kategori yang jelas.", "Sembunyikan/hapus fitur yang jarang dipakai di halaman utama.", "Buat pencarian produk yang cepat dan akurat."],
            ["Tampilkan informasi produk yang jelas dan lengkap (harga, deskripsi, ulasan).", "Sinkronisasi sistem agar stok barang selalu real-time."],
            ["Buat proses checkout yang singkat (tidak terlalu banyak langkah).", "Sediakan subsidi/promo ongkos kirim yang mudah diklaim."],
            ["Sediakan pilihan metode pembayaran yang lengkap dan mudah digunakan.", "Pastikan stabilitas server saat memproses pembayaran."],
            ["Berikan halaman dan notifikasi konfirmasi pesanan yang sangat jelas segera setelah pembayaran berhasil."],
        ],
    },
}

def make_journey_table(panel_idx):
    """Build the journey table HTML for a given panel."""
    d = journey_data[panel_idx]
    name = d["name"]
    
    stages = ["STAGE 1<br>AWARENESS", "STAGE 2<br>CONSIDERATION", "STAGE 3<br>BOOKING", "STAGE 4<br>RIDE", "STAGE 5<br>AFTER USE"]
    rows = ["AKTIVITAS", "EMOSI", "PAIN POINT", "PELUANG SOLUSI"]
    keys = ["aktivitas", "emosi", "pain_point", "peluang_solusi"]
    
    lines = []
    lines.append('                                                <div class="persona__journey-table-wrapper">')
    lines.append('                  <table class="persona__journey-table">')
    lines.append('                    <thead>')
    lines.append('                      <tr>')
    lines.append(f'                        <th>{name}</th>')
    for s in stages:
        lines.append(f'                        <th>{s}</th>')
    lines.append('                      </tr>')
    lines.append('                    </thead>')
    lines.append('                    <tbody>')
    
    for row_label, key in zip(rows, keys):
        lines.append('                      <tr>')
        lines.append(f'                        <td>{row_label}</td>')
        for stage_data in d[key]:
            items = "".join(f"<li>{item}</li>" for item in stage_data)
            lines.append(f'                        <td><ul>{items}</ul></td>')
        lines.append('                      </tr>')
    
    lines.append('                    </tbody>')
    lines.append('                  </table>')
    lines.append('                </div>')
    
    return "\n".join(lines)

# ─── Replace journey sections in all 5 panels ───

changes = 0

for panel_idx in range(5):
    table_html = make_journey_table(panel_idx)
    name = journey_data[panel_idx]["name"]
    
    if panel_idx <= 1:
        # Panels 0 and 1 already have tables - replace the entire table wrapper section
        # Find the journey section by name
        pattern = re.compile(
            r'(<h4 class="persona__section-title persona__section-title--green">User Journey Map</h4>\s*)'
            r'<div class="persona__journey-table-wrapper">.*?</div>\s*(?=\n)',
            re.DOTALL
        )
        
        # Find all matches and replace the right one
        matches = list(pattern.finditer(content))
        if panel_idx < len(matches):
            m = matches[panel_idx]
            replacement = m.group(1) + table_html
            content = content[:m.start()] + replacement + content[m.end():]
            changes += 1
            print(f"Panel {panel_idx} ({name}): replaced existing journey table")
        else:
            print(f"Panel {panel_idx} ({name}): ERROR - could not find journey table")
    else:
        # Panels 2, 3, 4 have empty journey sections
        # Find the empty journey section (just h4 + whitespace + closing tags)
        pattern = re.compile(
            r'(<h4 class="persona__section-title persona__section-title--green">User Journey Map</h4>)\s*'
            r'(</div>\s*</div>\s*</div>)',
            re.DOTALL
        )
        
        matches = list(pattern.finditer(content))
        target_idx = panel_idx - 2  # 0th empty = panel 2, 1st empty = panel 3, etc.
        if target_idx < len(matches):
            m = matches[target_idx]
            replacement = m.group(1) + "\n" + table_html + "\n              " + m.group(2)
            content = content[:m.start()] + replacement + content[m.end():]
            changes += 1
            print(f"Panel {panel_idx} ({name}): added journey table")
        else:
            print(f"Panel {panel_idx} ({name}): ERROR - could not find empty journey section (found {len(matches)} empty sections)")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone! Made {changes} changes.")
