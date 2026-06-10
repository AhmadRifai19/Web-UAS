import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── Persona data from images ───
personas = {
    0: {
        "key_attribute": [
            "Wirausahawan muda usia 21 tahun.",
            "Penjual produk secara online.",
            "Pengguna aktif WhatsApp dan Instagram untuk bisnis.",
            "Mengelola usaha secara mandiri.",
            "Menghargai efisiensi waktu dan kemudahan akses fitur.",
        ],
        "short_description": (
            "Fikri adalah seorang wirausahawan muda berusia 21 tahun yang menjalankan usaha penjualan produk secara online. "
            "Ia mengelola seluruh operasional bisnisnya sendiri, mulai dari penyiapan produk hingga promosi melalui media sosial. "
            "Fikri sangat menghargai efisiensi dan kemudahan penggunaan aplikasi, serta mendambakan sistem otomatisasi untuk mengurangi beban kerja manual yang menyita waktu."
        ),
        "needs": [
            "Layanan yang membantu proses promosi menjadi lebih praktis dan instan.",
            "Fitur otomatis agar tidak perlu melakukan banyak proses manual yang berulang.",
            "Antarmuka yang mudah dipahami tanpa memerlukan waktu lama untuk mempelajarinya.",
            "Kemampuan untuk menjaring banyak pelanggan baru dengan usaha minimal.",
            "Alat yang memudahkan pengaturan pesanan di waktu senggang.",
        ],
        "challenges": [
            "Merasa repot karena promosi harus dilakukan secara manual satu per satu kepada banyak pelanggan.",
            "Pengelolaan usaha yang memakan banyak waktu, terutama saat hari-hari penuh dengan banyak orderan.",
            "Merasa bingung dan kesulitan saat harus mempelajari spesifikasi fitur baru dalam menjalankan usaha.",
            "Terkadang terpaksa kembali ke cara manual yang biasa karena kesulitan dengan fitur baru yang rumit.",
        ],
        "opportunities": [
            "Menciptakan fitur promosi otomatis yang bisa menjangkau banyak pelanggan sekaligus untuk menghemat waktu.",
            "Mendesain ulang aplikasi bisnis agar lebih intuitif bagi pengguna muda yang sibuk.",
            "Memastikan stok penuh dapat langsung terhubung dengan notifikasi promosi untuk meningkatkan penjualan.",
            "Menyajikan data berapa banyak waktu yang bisa dihemat oleh pengguna melalui fitur otomatisasi.",
        ],
    },
    1: {
        "key_attribute": [
            "Wirausaha pemilik toko sembako dan plastik.",
            "Berorientasi pada pelayanan pelanggan dan perputaran uang yang cepat.",
            "Memiliki keterbatasan dalam pemahaman teknologi promosi.",
        ],
        "short_description": (
            "Susanto Hari Wibowo adalah seorang wiraswasta berusia 44 tahun yang mengelola toko sembako dan plastik. "
            "Kesehariannya dihabiskan dengan mengelola stok barang dari gudang ke display serta melayani pembeli eceran dan pedagang makanan. "
            "Fokus utamanya adalah memastikan ketersediaan barang agar tidak mengecewakan pelanggan, namun ia masih menghadapi kendala dalam pengukuran stok yang akurat dan pemanfaatan teknologi untuk promosi."
        ),
        "needs": [
            "Memastikan stok plastik dan sembako selalu tersedia saat pelanggan datang.",
            "Aplikasi yang mampu mencatat jumlah stok barang secara akurat agar tidak kehabisan stok.",
            "Pencatatan harga dari setiap supplier untuk perbandingan atau dokumentasi.",
            "Proses pencatatan stok yang lebih terukur dari gudang ke display.",
            "Strategi penjualan seperti borongan yang mempercepat perputaran uang.",
        ],
        "challenges": [
            "Sering mengira stok masih ada di tumpukan bawah, padahal sudah habis.",
            "Kehilangan pelanggan harian jika barang yang dicari sering kosong.",
            "Pengalaman buruk mendapatkan kualitas barang plastik tipis/mudah robek yang tidak sesuai foto saat memesan online dari supplier baru.",
            "Kurang memahami cara melakukan promosi dengan menggunakan teknologi.",
            "Seluruh proses pengelolaan stok di gudang masih dilakukan secara manual di sela-sela melayani pembeli.",
        ],
        "opportunities": [
            "Pengembangan fitur pencatatan stok yang memberikan peringatan saat barang mencapai batas minimum.",
            "Fitur untuk membundel dan mencatat rincian harga serta kualitas barang dari berbagai supplier.",
            "Integrasi sistem gudang dan display untuk mempermudah monitoring ketersediaan barang tanpa harus cek fisik terus-menerus.",
            "Fitur rating terhadap supplier untuk memastikan order barang berkualitas di masa depan.",
        ],
    },
    2: {
        "key_attribute": [
            "Mahasiswa aktif.",
            "Mulai membuat aset UI, logo, serta prototip.",
            "Visioner namun menyesuaikan diri terhadap teknis pemasaran e-commerce.",
            "Memiliki rutinitas padat (belajar, organisasi, dan usaha).",
        ],
        "short_description": (
            "Haris adalah seorang mahasiswa aktif jurusan Desain Produk di Institut Teknologi Sepuluh Nopember yang memiliki semangat kewirausahaan. "
            "Untuk mengatasi kejenuhan dari rutinitas kuliah yang berulang, ia mendirikan usaha jasa kreatif bersama lima orang temannya. "
            "Meskipun memiliki keahlian teknis dalam desain, Haris menghadapi tantangan besar dalam memperluas jangkauan pasar dan merasa awam dalam mengoperasikan platform e-commerce untuk menjual jasa profesionalnya."
        ),
        "needs": [
            "Pemahaman untuk beralih dari pemasaran konvensional ke platform e-commerce (Shopee, Tokopedia, Lazada).",
            "Membutuhkan panduan terkait cara memasang produk jasa di platform digital agar mudah dipahami pengguna baru.",
            "Adanya fitur kategori yang sesuai dengan jenis produk/jasa untuk memudahkan calon pelanggan.",
            "Memahami algoritma e-commerce untuk meningkatkan produktivitas pesanan.",
            "Membutuhkan alur kerja yang tidak bertentangan antara proyek akhir dengan tugas kuliah.",
        ],
        "challenges": [
            "Lingkup pemasaran saat ini hanya terbatas pada pertemanan dan mata kuliah, sehingga pesanan sering sepi.",
            "Pemrosesan yang kurang efektif terhadap proses pemasaran.",
            "Merasa awam dan tidak tahu cara menjual jasa melalui platform belanja online.",
            "Kesulitan mencari cara baru untuk melakukan promosi proyek, di tengah kesibukan tugas kuliah yang menumpuk.",
        ],
        "opportunities": [
            "Memanfaatkan algoritma platform digital untuk memantau tren pasar secara real-time.",
            "Menciptakan aset UI dan desain ke dalam kategori produk yang ideal di e-commerce agar terlihat profesional.",
            "Menggunakan fitur kategori untuk membantu pelanggan mengenali dengan cepat jasa apa yang ditawarkan tanpa harus banyak bertanya.",
            "Pemanfaatan panduan aplikasi untuk mempermudah transisi dari metode pemasaran lama ke metode baru yang lebih digital.",
        ],
    },
    3: {
        "key_attribute": [
            "Mahasiswa aktif semester 2.",
            "Pekerjaan sementara.",
            "Pengguna aktif fitur Live Shopping.",
            "Paham fitur teknis.",
            "Menggunakan fitur checkout dalam satu aplikasi.",
        ],
        "short_description": (
            "Widya adalah pengguna yang cerdas dan selektif dalam berbelanja online. "
            "Ia terbiasa membandingkan harga antar toko, mencari promo terbaik, dan memanfaatkan fitur live untuk melihat produk secara lebih nyata dan mendapatkan promo sebelum membeli."
        ),
        "needs": [
            "Fitur pembanding harga dan ongkir yang praktis.",
            "Tampilan live yang bersih dari gangguan komentar agar detail produk terlihat jelas.",
            "Sistem manajemen keranjang yang bisa difilter berdasarkan kategori atau toko.",
            "Jaminan kualitas barang agar sesuai dengan yang ditampilkan saat live streaming.",
            "Notifikasi yang hanya relevan dengan situasi pengiriman atau diskon wishlist.",
        ],
        "challenges": [
            "Detail produk tertutup oleh tumpukan komentar dan pop-up promo saat menonton live.",
            "Bisa menerima barang yang tidak sesuai ekspektasi (zonk).",
            "Kesulitan membedakan barang di keranjang jika jumlahnya banyak dan dari toko berbeda.",
            "Gangguan spam notifikasi promo saat live yang tidak relevan.",
            "Harus berpindah-pindah profil toko untuk membandingkan satu produk.",
        ],
        "opportunities": [
            'Mengembangkan fitur "Quick Compare" untuk membandingkan produk secara side-by-side.',
            'Optimalisasi fitur "Clear Mode" agar lebih mudah dilihat saat menonton live.',
            "Penerapan sistem filter cerdas di keranjang berdasarkan kategori produk.",
            "Peningkatan standarisasi kualitas produk bagi seller live.",
            "Personalisasi sistem notifikasi agar lebih fokus pada kebutuhan pengguna (logistik & wishlist).",
        ],
    },
    4: {
        "key_attribute": [
            "Pengguna aktif berbagai aplikasi digital.",
            "Pengguna rutin Shopee, TikTok Shop, dan Gojek.",
            "Berbelanja setiap minggu.",
            "Mengutamakan efisiensi alur pembelian.",
            "Terganggu oleh tampilan yang terlalu ramai.",
        ],
        "short_description": (
            "Zaskiya adalah seorang pengguna aktif berbagai aplikasi digital yang cukup sering berbelanja online setiap minggunya, terutama untuk memenuhi kebutuhan sehari-hari dan makanan. "
            "Ia menginginkan pengalaman belanja yang efisien dengan tampilan aplikasi yang bersih serta proses transaksi yang cepat tanpa banyak hambatan teknis atau gangguan visual."
        ),
        "needs": [
            "Antarmuka yang bersih tanpa terlalu banyak banner promo yang mengganggu.",
            "Alur pembelian yang praktis dan tidak terhalang banyak langkah.",
            "Tersedianya berbagai pilihan pembayaran yang berfungsi dengan baik.",
            "Fitur pencarian produk yang cepat dan memberikan hasil akurat.",
            "Pengurangan fitur yang jarang digunakan di halaman utama.",
            "Pengelompokan fitur sesuai kategori yang paling umum digunakan.",
            "Detail produk yang jelas mencakup harga, deskripsi, dan ulasan.",
        ],
        "challenges": [
            "Tampilan aplikasi terlalu ramai oleh promo dan banner yang menyulitkan pencarian fitur.",
            "Menu yang terlalu banyak namun tidak terorganisir dengan baik.",
            "Ongkos kirim yang dirasa terlalu mahal.",
            "Barang tiba-tiba habis saat akan melakukan pembayaran.",
            "Kendala pada metode pembayaran atau pilihan pembayaran yang tidak tersedia.",
        ],
        "opportunities": [
            "Menyederhanakan UI dengan konsep minimalis untuk mengurangi beban kognitif pengguna.",
            "Mengoptimalkan penempatan banner agar tidak menutupi fitur utama.",
            "Menata ulang arsitektur informasi fitur berdasarkan kategori penggunaan.",
            "Mempercepat proses dari keranjang ke checkout dan konfirmasi pesanan.",
            "Menyembunyikan fitur yang jarang diakses oleh pengguna secara otomatis di halaman depan.",
            "Memberikan informasi stok yang real-time dan opsi pengiriman yang lebih kompetitif.",
        ],
    },
}


def make_stickies(items):
    """Generate sticky note divs from a list of strings."""
    lines = []
    for item in items:
        lines.append(f'                  <div class="persona__sticky">{item}</div>')
    return '\n'.join(lines)


changes = 0

for panel_idx, data in personas.items():
    # Find the panel boundaries
    panel_start = content.find(f'data-panel="{panel_idx}"')
    if panel_start == -1:
        print(f"Panel {panel_idx}: NOT FOUND")
        continue
    
    if panel_idx < 4:
        panel_end = content.find(f'data-panel="{panel_idx + 1}"', panel_start + 1)
    else:
        panel_end = content.find('<!-- Define Problem Statement', panel_start)
    
    panel_html = content[panel_start:panel_end]
    
    # Replace each sticky section - CORRECT regex with 3 closing </div>
    for title_class, title_text, data_key in [
        ('blue', 'Key Attribute', 'key_attribute'),
        ('blue', 'Needs', 'needs'),
        ('blue', 'Challenges', 'challenges'),
        ('orange', 'Opportunities', 'opportunities'),
    ]:
        # Use regex that captures ALL closing </div> after stickies
        pattern = re.compile(
            rf'(<h4 class="persona__section-title persona__section-title--{title_class}">{title_text}</h4>\s*'
            r'<div class="persona__stickies">)\s*'
            r'.*?'
            r'\s*(</div>\s*</div>\s*</div>)',
            re.DOTALL
        )
        match = pattern.search(panel_html)
        if match:
            new_stickies = make_stickies(data[data_key])
            replacement = match.group(1) + '\n' + new_stickies + '\n' + match.group(2)
            panel_html = panel_html[:match.start()] + replacement + panel_html[match.end():]
            changes += 1
        else:
            print(f"Panel {panel_idx}: {title_text} NOT FOUND")
    
    # Replace Short Description (uses <p> tag, not stickies)
    sd_pattern = re.compile(
        r'(<h4 class="persona__section-title persona__section-title--blue">Short Description</h4>\s*'
        r'<p class="persona__desc-text">)'
        r'.*?'
        r'(</p>)',
        re.DOTALL
    )
    sd_match = sd_pattern.search(panel_html)
    if sd_match:
        replacement = sd_match.group(1) + data["short_description"] + sd_match.group(2)
        panel_html = panel_html[:sd_match.start()] + replacement + panel_html[sd_match.end():]
        changes += 1
    else:
        print(f"Panel {panel_idx}: Short Description NOT FOUND")
    
    # Replace the panel content back
    content = content[:panel_start] + panel_html + content[panel_end:]
    print(f"Panel {panel_idx}: Updated all sections")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone! Made {changes} changes total.")
