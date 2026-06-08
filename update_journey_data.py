import json
import re

personas = [
    {
        'id': 'fikri',
        'name': 'Fikri Ramadhan',
        'stages': [
            {
                'act': ['Merasa penjualan menurun atau tidak berkembang', 'Mulai mencari cara promosi yang lebih efektif', 'Mendengar atau melihat aplikasi bisnis dari media sosial/teman'],
                'emo': ['Khawatir usaha tidak berkembang', 'Bingung harus mulai dari mana', 'Ada harapan menemukan solusi'],
                'pain': ['Tidak tahu strategi promosi yang tepat', 'Promosi masih manual dan kurang efektif', 'Minim pengetahuan digital marketing'],
                'opp': ['Edukasi dasar bisnis & promosi dalam aplikasi', 'Rekomendasi fitur sesuai kebutuhan user', 'Konten tips sederhana (tidak terlalu teknis)']
            },
            {
                'act': ['Mencari dan mencoba beberapa aplikasi', 'Membandingkan fitur dan kemudahan penggunaan', 'Bertanya ke teman atau melihat review'],
                'emo': ['Ragu dalam memilih', 'Takut salah aplikasi', 'Sedikit tertarik tapi belum yakin'],
                'pain': ['Terlalu banyak pilihan aplikasi', 'Tidak paham fungsi tiap fitur', 'Tampilan aplikasi kadang membingungkan'],
                'opp': ['Tampilan UI sederhana & intuitif', 'Penjelasan fitur dengan bahasa mudah', 'Demo atau preview penggunaan aplikasi']
            },
            {
                'act': ['Download dan daftar akun', 'Mulai eksplorasi fitur dasar', 'Mencoba menjalankan fungsi utama aplikasi'],
                'emo': ['Penasaran dengan hasilnya', 'Sedikit bingung saat awal penggunaan', 'Berharap aplikasi membantu usaha'],
                'pain': ['Tidak tahu langkah awal penggunaan', 'Takut salah klik atau salah setting', 'Kurang panduan saat pertama kali masuk'],
                'opp': ['Tutorial step-by-step yang interaktif', 'Onboarding sederhana dan tidak membingungkan', 'Bantuan langsung (tooltip / panduan cepat)']
            },
            {
                'act': ['Mulai upload produk', 'Mengatur informasi usaha', 'Mencoba fitur promosi atau penjualan'],
                'emo': ['Mulai memahami sistem', 'Sedikit lebih percaya diri', 'Masih butuh arahan'],
                'pain': ['Proses input data terasa lama', 'Beberapa fitur belum dipahami sepenuhnya', 'Hasil belum langsung terlihat'],
                'opp': ['Fitur otomatis (auto-fill / auto-promosi)', 'Shortcut untuk proses cepat', 'Panduan lanjutan berbasis kebutuhan user']
            },
            {
                'act': ['Menggunakan aplikasi secara rutin', 'Mulai merasakan manfaat', 'Merekomendasikan ke teman sesama UMKM'],
                'emo': ['Puas dengan hasil', 'Senang karena usaha berkembang', 'Percaya pada aplikasi'],
                'pain': ['Butuh fitur lanjutan untuk scale up', 'Ingin performa lebih optimal', 'Mulai butuh analisis data'],
                'opp': ['Program loyalitas atau reward', 'Fitur advanced (opsional, tidak memaksa)', 'Insight penjualan & laporan sederhana']
            }
        ]
    },
    {
        'id': 'zaskiya',
        'name': 'Zaskiya Sandi A.A.',
        'stages': [
            {
                'act': ['Membuka aplikasi, melihat halaman utama, dan mencari fitur atau produk yang ingin dibeli.'],
                'emo': ['Bingung / Kewalahan'],
                'pain': ['Tampilan aplikasi terlalu ramai (banyak promo/banner).', 'Menu terlalu banyak tapi tidak terorganisir dengan baik.', 'Kesulitan mencari fitur yang ingin digunakan.'],
                'opp': ['Sederhanakan tampilan (hapus banner berlebih).', 'Kelompokkan fitur sesuai kategori yang jelas.', 'Sembunyikan/hapus fitur yang jarang dipakai di halaman utama.', 'Buat pencarian produk yang cepat dan akurat.']
            },
            {
                'act': ['Mengecek ketersediaan barang dan membaca detail informasi produk sebelum memutuskan.'],
                'emo': ['Kecewa (jika barang habis)'],
                'pain': ['Stok barang tiba-tiba habis saat sedang dipertimbangkan untuk dibeli.'],
                'opp': ['Tampilkan informasi produk yang jelas dan lengkap (harga, deskripsi, ulasan).', 'Sinkronisasi sistem agar stok barang selalu real-time.']
            },
            {
                'act': ['Melanjutkan pesanan ke tahap pengiriman, melihat rincian biaya, dan mengecek ongkos kirim.'],
                'emo': ['Kesal (jika ongkir mahal)'],
                'pain': ['Ongkos kirim seringkali dirasa terlalu mahal.', 'Alur pembelian berisiko terasa berbelit jika terlalu banyak langkah.'],
                'opp': ['Buat proses checkout yang singkat (tidak terlalu banyak langkah).', 'Sediakan subsidi/promo ongkos kirim yang mudah diklaim.']
            },
            {
                'act': ['Memilih metode pembayaran yang tersedia dan mencoba menyelesaikan transaksi.'],
                'emo': ['Frustrasi (jika error)'],
                'pain': ['Metode pembayaran sering mengalami error.', 'Pilihan metode pembayaran terkadang tidak tersedia.'],
                'opp': ['Sediakan pilihan metode pembayaran yang lengkap dan mudah digunakan.', 'Pastikan stabilitas server saat memproses pembayaran.']
            },
            {
                'act': ['Menerima bukti bahwa transaksi telah berhasil dan pesanan sedang diproses.'],
                'emo': ['Lega'],
                'pain': ['Sering merasa khawatir jika status pesanan setelah membayar tidak langsung diperbarui.'],
                'opp': ['Berikan halaman dan notifikasi konfirmasi pesanan yang sangat jelas segera setelah pembayaran berhasil.']
            }
        ]
    },
    {
        'id': 'widya',
        'name': 'Widya Ony',
        'stages': [
            {
                'act': ['Merasakan kebutuhan mendesak (bawa suami ke RS).', 'Ingat rekomendasi anak/tetangga tentang Gojek.', 'Mencari dan membuka aplikasi Gojek di HP.'],
                'emo': ['Khawatir', 'Cemas', 'Panik'],
                'pain': ['Teknologi bukanlah pilihan pertama, butuh dorongan situasi darurat.', 'Tidak hafal letak aplikasi.'],
                'opp': ['Fitur "SOS" atau "Darurat" di layar utama yang langsung memesan GoCar ke rumah sakit terdekat.', 'Ikon yang besar dan jelas.']
            },
            {
                'act': ['Mencoba memahami perbedaan GoCar dan GoRide.', 'Membaca-baca tulisan kecil pada ikon.', 'Membuka aplikasi, melihat layar penuh ikon.'],
                'emo': ['Kewalahan', 'Frustrasi', 'Bingung'],
                'pain': ['Tampilan aplikasi terlalu ramai dan banyak ikon.', 'Banyak layanan tidak relevan (GoMassage, dll).', 'Tulisan dan ikon terlalu kecil, sulit dibaca.'],
                'opp': ['"Simple Mode" untuk user seperti Lasmini: hanya menampilkan 3 layanan utama (GoCar, GoFood, GoSend).', 'Gunakan tulisan dan ikon yang lebih besar.', 'Voice command ("OK Google, pesankan GoCar").']
            },
            {
                'act': ['Mengetuk ikon GoCar.', 'Bingung mengisi alamat (lokasi saat ini & tujuan).', 'Memilih "Bayar Tunai" karena tidak paham GoPay.', 'Menunggu konfirmasi driver menerima pesanan.'],
                'emo': ['Harap-harap Cemas', 'Tidak Sabar', 'Tegang'],
                'pain': ['Bingung cara input alamat yang benar.', 'Takut salah memencet tombol.', 'Tidak percaya dengan pembayaran digital (GoPay).'],
                'opp': ['Deteksi lokasi otomatis yang lebih akurat.', 'Tombol "Gunakan Lokasi Saya Sekarang" yang sangat menonjol.', 'Opsi "Bayar Tunai" sebagai default untuk user tertentu.', 'Konfirmasi pesanan dengan suara "Pesanan Anda Diterima!".']
            },
            {
                'act': ['Menerima telepon/chat dari driver.', 'Menunggu driver tiba.', 'Naik ke kendaraan.', 'Memantau perjalanan lewat map di aplikasi.'],
                'emo': ['Berharap driver sopan', 'Sedikit Lega tapi masih Cemas'],
                'pain': ['Gugup jika driver tidak bisa menemukan lokasinya.', 'Takut dengan driver yang tidak dikenal.'],
                'opp': ['Fitur "Bagikan Perjalanan" otomatis ke keluarga.', 'Notifikasi: "Driver Anda, Pak Budi, sedang menuju lokasi Anda."', 'Tampilan map yang sederhana dengan foto driver yang besar.']
            },
            {
                'act': ['Turun di tujuan.', 'Menerima notifikasi untuk memberi rating.', 'Bingung dan menutup notifikasi.'],
                'emo': ['Bersyukur', 'Lega'],
                'pain': ['Tidak mengerti tujuan memberi rating.', 'Menganggapnya merepotkan.'],
                'opp': ['Rating yang lebih sederhana, misal hanya "😊" atau "😞".', 'Pesan: "Terima kasih Ibu Lasmini, semoga suami lekas sembuh." (Personal & empatik).']
            }
        ]
    },
    {
        'id': 'susanto',
        'name': 'Susanto Hari Wibowo',
        'stages': [
            {
                'act': ['Mengecek stok fisik di gudang.', 'Menyadari stok plastik/sembako tertentu mulai habis.'],
                'emo': ['Waspada (takut stok kosong saat pelanggan datang).'],
                'pain': ['Stok tidak terukur secara akurat karena manual.', 'Tumpukan barang di gudang menghalangi pandangan.'],
                'opp': ['Aplikasi pencatatan stok otomatis.']
            },
            {
                'act': ['Membuka Facebook untuk mencari supplier baru.', 'Melihat foto-foto produk yang diposting.'],
                'emo': ['Berharap (ingin menemukan harga dan kualitas terbaik).'],
                'pain': ['Banyak penipuan di platform Facebook.', 'Representasi foto seringkali tidak jujur.'],
                'opp': ['Sistem rating dan ulasan supplier yang asli.']
            },
            {
                'act': ['Menghubungi supplier melalui inbox FB atau telepon.', 'Melakukan kesepakatan harga dan jumlah pesanan.'],
                'emo': ['Ragu (takut tertipu atau kualitas tidak sesuai foto).'],
                'pain': ['Proses pemesanan manual lewat chat/telp sangat melelahkan.', 'Data pesanan sering hilang di chat.'],
                'opp': ['Fitur "One-Click Ordering" tanpa harus chat panjang lebar.', 'Pencatatan riwayat transaksi yang rapi.']
            },
            {
                'act': ['Menunggu barang datang ke toko.', 'Menerima paket dari kurir/supplier.'],
                'emo': ['Tidak Sabar (menunggu kepastian waktu sampai).'],
                'pain': ['Tidak ada kepastian waktu kapan barang sampai.'],
                'opp': ['Fitur pelacakan pengiriman secara real-time.']
            },
            {
                'act': ['Mengecek kualitas fisik barang (ketebalan plastik).', 'Menata barang baru ke rak display.'],
                'emo': ['Kecewa/Marah (jika kualitas plastik tipis/gampang robek).'],
                'pain': ['Kualitas barang yang datang seringkali jauh di bawah standar.'],
                'opp': ['Jaminan kualitas atau fitur komplain jika barang rusak/jelek.']
            }
        ]
    },
    {
        'id': 'haris',
        'name': 'Haris Rido Ramadhan',
        'stages': [
            {
                'act': ['Mulai sadar kalau pemasaran usahanya masih kurang luas dan hanya dikenal di lingkungan teman'],
                'emo': ['Khawatir usahanya sulit berkembang kalau promosi tetap seperti sekarang'],
                'pain': ['Tidak tahu cara promosi digital yang efektif'],
                'opp': ['Berikan edukasi tentang manfaat platform untuk membantu usaha kecil berkembang']
            },
            {
                'act': ['Cari-cari platform jualan / e-commerce yang cocok untuk usaha jasa dan produknya'],
                'emo': ['Bingung memilih platform yang paling cocok, tapi penasaran untuk mencoba'],
                'pain': ['Banyak pilihan platform, jadi susah menentukan mana yang terbaik'],
                'opp': ['Sediakan penjelasan fitur platform dengan bahasa sederhana dan mudah dipahami']
            },
            {
                'act': ['Daftar akun dan mulai setup toko / profil usaha'],
                'emo': ['Semangat karena mulai mencoba hal baru, tapi agak bingung di awal'],
                'pain': ['Bingung saat awal setup toko dan upload produk/jasa'],
                'opp': ['Buat onboarding yang simpel dan step-by-step untuk pemula']
            },
            {
                'act': ['Upload jasa/produk lalu mulai menerima dan mengelola pesanan'],
                'emo': ['Mulai merasa terbantu, tapi masih belajar memahami semua fitur'],
                'pain': ['Sulit membagi waktu antara kuliah, tugas, dan order pelanggan'],
                'opp': ['Tambahkan fitur yang membantu pengelolaan pesanan lebih praktis']
            },
            {
                'act': ['Menggunakan platform secara rutin untuk jualan dan promosi'],
                'emo': ['Senang karena usaha lebih berkembang dan merasa platform membantu'],
                'pain': ['Harus menjaga rating/reputasi toko agar pelanggan tetap percaya'],
                'opp': ['Berikan insight penjualan dan tips pengembangan usaha lanjutan']
            }
        ]
    }
]

import os
file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

panels = re.split(r'(<h3 class=\"persona__name\">.*?</h3>)', content)
new_content = panels[0]

def build_table(persona_name):
    # find persona data
    p_data = None
    for p in personas:
        if p['name'] == persona_name:
            p_data = p
            break
            
    if not p_data:
        return "" # Should not happen
    
    html = f'''                <div class=\"persona__journey-table-wrapper\">
                  <table class=\"persona__journey-table\">
                    <thead>
                      <tr>
                        <th>{p_data['name'].upper()}</th>
                        <th>STAGE 1<br>AWARENESS</th>
                        <th>STAGE 2<br>CONSIDERATION</th>
                        <th>STAGE 3<br>BOOKING</th>
                        <th>STAGE 4<br>RIDE</th>
                        <th>STAGE 5<br>AFTER USE</th>
                      </tr>
                    </thead>
                    <tbody>
'''
    rows = [('Aktivitas', 'act'), ('Emosi', 'emo'), ('Pain Point', 'pain'), ('Peluang Solusi', 'opp')]
    
    for r_title, r_key in rows:
        html += f'                      <tr>\n                        <td>{r_title.upper()}</td>\n'
        for i in range(5):
            items = p_data['stages'][i][r_key]
            li_str = ''.join(f'<li>{item}</li>' for item in items)
            html += f'                        <td><ul>{li_str}</ul></td>\n'
        html += '                      </tr>\n'
    
    html += '''                    </tbody>
                  </table>
                </div>'''
    return html

for i in range(1, len(panels), 2):
    h3_str = panels[i]
    panel_content = panels[i+1]
    
    # Extract name
    m = re.search(r'<h3 class=\"persona__name\">(.*?)</h3>', h3_str)
    name = m.group(1).strip()
    
    # Replace the table wrapper in panel_content
    table_pattern = re.compile(r'<div class=\"persona__journey-table-wrapper\">.*?</div>', re.DOTALL)
    new_panel_content = table_pattern.sub(build_table(name), panel_content)
    
    new_content += h3_str + new_panel_content

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done applying data')
