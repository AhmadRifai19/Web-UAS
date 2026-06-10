file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Data from image
narasumber = [
    {
        'name': 'Zaskiya Sandi A.A.',
        'role': 'Pelajar',
        'interviewer': 'Rifai',
        'color': 1,
        'stories': [
            'User aktif menggunakan berbagai aplikasi digital dalam kehidupan sehari-hari.',
            'User pernah menggunakan aplikasi seperti Shopee, TikTok Shop, dan Gojek.',
            'User menggunakan aplikasi digital secara rutin untuk memenuhi kebutuhan harian.',
            'User pernah mengalami kendala yang menyebabkan transaksi gagal.',
            'User membatalkan pembelian karena ongkos kirim mahal, stok habis, atau error pembayaran.',
            'User terkadang mengalami kesulitan saat menggunakan aplikasi.',
            'User merasa tampilan aplikasi yang terlalu ramai membuat navigasi sulit dipahami.',
            'User terkadang mengalami kesulitan saat menggunakan aplikasi.',
            'User mengharapkan proses pencarian, pembayaran, dan checkout yang cepat serta mudah digunakan.',
        ]
    },
    {
        'name': 'Widya Ony Yusnita Rahayu',
        'role': 'Mahasiswa',
        'interviewer': 'Hayyu',
        'color': 2,
        'stories': [
            'User merupakan mahasiswa yang aktif menggunakan aplikasi belanja online.',
            'User memilih produk berdasarkan harga terjangkau untuk menyesuaikan anggaran.',
            'User memanfaatkan promo dan diskon untuk memenuhi kebutuhan belanja.',
            'User merasa senang ketika mendapatkan harga murah melalui promo flash sale.',
            'User pernah mengalami pengalaman buruk ketika kualitas barang tidak sesuai dengan promosi penjual.',
            'User merasa puas setelah mendapatkan pengalaman belanja yang baik.',
            'User sering terganggu oleh komentar, sticker, dan pop-up saat menonton live streaming.',
            'User kesulitan melihat detail produk karena tampilan layar terlalu ramai.',
            'User mencari ulasan pembeli lain untuk memastikan kualitas produk.',
            'User mengharapkan notifikasi yang lebih relevan dan tidak mengganggu.',
            'User menginginkan pengawasan produk yang lebih ketat agar mengurangi barang yang mengecewakan pembeli.',
            'User mengalami kesulitan mencari barang di keranjang yang terlalu panjang.',
            'User membutuhkan fitur perbandingan produk dari toko berbeda dalam satu tampilan.',
            'User merasa fitur video dan live streaming membantu melihat produk secara lebih nyata.',
        ]
    },
    {
        'name': 'Fikri Ramadhan',
        'role': 'Wiraswasta',
        'interviewer': 'Gavin',
        'color': 3,
        'stories': [
            'User menjalankan usaha warung makanan kecil secara mandiri di dapur rumah.',
            'User mengelola seluruh operasional warung sendiri setiap hari.',
            'User masih mengandalkan promosi sederhana melalui WhatsApp.',
            'User merasa senang ketika warung ramai pembeli dan penjualan meningkat.',
            'User merasa kecewa ketika warung sepi pelanggan.',
            'User belum memahami cara menjangkau pelanggan dalam media sosial untuk promosi secara efektif.',
            'User masih bergantung pada pelanggan lama untuk menjaga pemasukan.',
            'User membutuhkan metode sederhana yang praktis dan mudah digunakan.',
            'User menginginkan aplikasi sederhana untuk membantu menjangkau pelanggan baru.',
        ]
    },
    {
        'name': 'Susanto Hari Wibowo',
        'role': 'Wiraswasta',
        'interviewer': 'David',
        'color': 4,
        'stories': [
            'User menjalankan usaha toko sembako dan plastik secara mandiri.',
            'User memiliki aktivitas operasional toko yang padat setiap hari.',
            'User melayani pembeli eceran dan pedagang makanan secara rutin.',
            'User merasa senang ketika penjualan meningkat dan stok barang banyak terjual.',
            'User rutin mengecek serta memantau stok barang di toko dan gudang.',
            'User sering mengalami kesalahan dalam memperkirakan jumlah stok barang.',
            'User merasa khawatir ketika barang yang dicari pelanggan tidak tersedia.',
            'User pernah mengalami pengalaman buruk saat memesan stok dari supplier online baru.',
            'User kurang memahami promosi menggunakan teknologi digital.',
            'User membutuhkan aplikasi untuk memantau stok barang dan harga supplier secara akurat.',
        ]
    },
    {
        'name': 'Haris Ridho Ramadhan',
        'role': 'Mahasiswa',
        'interviewer': 'Hafidh',
        'color': 5,
        'stories': [
            'User menjalankan usaha jasa desain bersama teman kuliah.',
            'User mendirikan usaha untuk mengisi waktu dan menambah pengalaman.',
            'User mengalami kesulitan membagi waktu antara revisi klien dan tugas kuliah.',
            'User merasa senang ketika mendapatkan apresiasi dan bayaran dari klien.',
            'User mengalami kendala pemasaran karena hanya mengandalkan relasi pertemanan.',
            'User berencana memasarkan jasa melalui platform e-commerce.',
            'User belum memahami cara pemasaran jasa di platform digital.',
            'User membutuhkan panduan penggunaan platform saat mulai berjualan jasa.',
            'User menyadari pentingnya reputasi digital bagi keberlangsungan usaha.',
            'User menginginkan fitur kategori jasa agar layanan lebih mudah ditemukan calon klien.',
            'User khawatir ulasan negatif dapat menurunkan performa toko dan kepercayaan pelanggan.',
        ]
    },
]


def build_card(nb, idx):
    c = nb['color']
    is_full = (len(nb['stories']) > 10)
    full_class = ' define__card--full' if is_full else ''

    html = f'''        <div class="define__card{full_class}">
          <div class="define__card-header">
            <div class="define__card-avatar define__card-avatar--{c}">
              {nb['name'][0]}
            </div>
            <div class="define__card-info">
              <h3 class="define__card-name">{nb['name']}</h3>
              <p class="define__card-role">Narasumber {idx} &mdash; {nb['role']}</p>
            </div>
            <span class="define__card-badge define__card-badge--{c}">{nb['interviewer']}</span>
          </div>
          <div class="define__card-body">
'''
    for story in nb['stories']:
        html += f'''            <div class="define__sticky">
              {story}
              <span class="define__sticky-interviewer">&mdash; {nb['interviewer']}</span>
            </div>
'''

    html += '''          </div>
        </div>
'''
    return html


# Build section HTML
section_html = '''
    <!-- ============================== DEFINE PROBLEM STATEMENT ============================== -->
    <section class="define" id="define">
      <div class="container">
        <header class="section-header">
          <p class="section-label">Define</p>
          <h2 class="section-title">Define Problem <span class="accent">Statement</span></h2>
          <p class="section-desc">Kumpulan temuan dan perilaku pengguna dari hasil wawancara yang mendefinisikan permasalahan utama.</p>
        </header>

        <div class="define__grid">
'''

for i, nb in enumerate(narasumber):
    section_html += build_card(nb, i + 1)

section_html += '''        </div>
      </div>
    </section>
'''

# Insert before Affinity Map section
insert_marker = '<!-- ============================== AFFINITY MAP / EMPATHIZE ============================== -->'
content = content.replace(insert_marker, section_html + '\n    ' + insert_marker)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Section 'Define Problem Statement' added successfully!")
print(f"Total narasumber: {len(narasumber)}")
for nb in narasumber:
    print(f"  - {nb['name']} ({nb['role']}): {len(nb['stories'])} stories")
