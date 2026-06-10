import re

file_path = 'c:/semester 2/Web UAS/index.html'

# Data from image: user stories per persona
interview_data = {
    'Fikri Ramadhan': {
        'interviewer': 'Gavin',
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
    'Susanto Hari Wibowo': {
        'interviewer': 'David',
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
    'Haris Wahyu Ramadhani': {
        'interviewer': 'Hafidh',
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
    'Widya Dny Yuanika R.': {
        'interviewer': 'Hayyu',
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
    'Zaskiya Soaldi A.A.': {
        'interviewer': 'Rifai',
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
}


def build_interview_html(interviewer, stories):
    """Build 10 Q&A items from user stories."""
    items = []

    # If more than 10 stories, combine extras into the 10th slot
    if len(stories) > 10:
        display_stories = stories[:9]
        combined = ' '.join(stories[9:])
        display_stories.append(combined)
    else:
        display_stories = list(stories)

    # Pad to 10 if needed
    while len(display_stories) < 10:
        display_stories.append(None)

    for i in range(10):
        story = display_stories[i]
        if story:
            items.append(f'''                  <div class="interview__qa-item">
                    <div class="interview__sticky--red">
                      <strong>Pertanyaan {i+1}:</strong><br>
                      Ceritakan pengalaman Anda sebagai pengguna.
                    </div>
                    <div class="interview__sticky--yellow">
                      <strong>Jawaban ({interviewer}):</strong><br>
                      {story}
                    </div>
                  </div>''')
        else:
            items.append(f'''                  <div class="interview__qa-item">
                    <div class="interview__sticky--red">
                      <strong>Pertanyaan {i+1}:</strong><br>
                      [Belum ada data]
                    </div>
                    <div class="interview__sticky--yellow">
                      <strong>Jawaban:</strong><br>
                      [Belum ada data]
                    </div>
                  </div>''')

    return '\n'.join(items)


# Read HTML
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace interview grids for each persona
replaced_count = 0
for persona_name, data in interview_data.items():
    interviewer = data['interviewer']
    stories = data['stories']

    new_grid_content = build_interview_html(interviewer, stories)

    # Pattern: find the interview section for this specific persona
    # The persona name appears in the section-title (blue for Haris has "Wahyu", etc.)
    # We use the <h3> name to anchor, then find the next interview grid
    escaped_name = re.escape(persona_name)

    # Match from persona name to the interview grid closing
    pattern = (
        r'(<h3 class="persona__name">' + escaped_name + r'</h3>'
        r'.*?'  # everything up to the interview section (non-greedy)
        r'<h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>\s*'
        r'<div class="persona__interview-grid">\s*)'
        r'.*?'  # the current grid content (non-greedy)
        r'(\s*</div>\s*</div>\s*</div>)'
    )

    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + match.group(1) + '\n' + new_grid_content + '\n' + match.group(2) + content[match.end():]
        replaced_count += 1
        print(f"OK: Replaced interview data for {persona_name} (interviewer: {interviewer}, stories: {len(stories)})")
    else:
        print(f"MISS: Could not find interview section for {persona_name}")

print(f"\nDone! Replaced {replaced_count}/{len(interview_data)} personas.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved.")
