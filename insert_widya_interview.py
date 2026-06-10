import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Widya's interview data (10 Q&A pairs)
qa_data = [
    {
        "q": "Perkenalkan diri anda? nama, pekerjaan, dan usia.",
        "a": "Widya Ony berusia 19 tahun, Mahasiswa semester 2 Politeknik Negeri Madiun."
    },
    {
        "q": "Apa yang biasa anda lakukan saat menggunakan aplikasi TikTokShop?",
        "a": "Mencari barang yang diinginkan juga membandingkan harga dan ongkir, supaya dapat barang yang paling terjangkau buat kantong mahasiswa."
    },
    {
        "q": "Apa yang paling penting bagi anda?",
        "a": "Yang paling penting adalah kejujuran produk dan efisiensi biaya, gratis ongkir dan promo diskon sangat membantu menghemat uang saku, terutama untuk kebutuhan kuliah mendesak."
    },
    {
        "q": "Apa hal yang paling penting bagi Anda ketika melakukan aktivitas tersebut?",
        "a": 'Pengalaman terbaik itu saat mendapatkan harga yang jauh lebih murah karena dapat promo "flash sale" saat Live, dan juga proses checkout yang sangat cepat yang gak perlu pindah aplikasi.'
    },
    {
        "q": "Kendala apa yang sering anda hadapi saat menggunakan TikTokShop?",
        "a": "Sangat mengganggu live chat, sulit mengatur komentar, stiker dan pop up promosi mengumpuk."
    },
    {
        "q": "Apakah anda pernah menggunakan fitur 'Live Streaming'?",
        "a": "Sudah pernah, tapi hanya sebagai penonton."
    },
    {
        "q": "Apa yang bisa membuat TikTokShop lebih mudah digunakan?",
        "a": "Fitur filter, sistem notifikasi spam, dan fokus pada status pengiriman (dikirim dari wilayah), aplikasi terasa jauh lebih nyaman."
    },
    {
        "q": "Apa yang paling anda harapkan saat menggunakan TikTokShop?",
        "a": 'Harapannya ada jaminan kualitas barang yang lebih ketat dari pihak aplikasi agar tidak ada lagi produk yang "zonk".'
    },
    {
        "q": "Jika bisa memperbaiki satu hal apa yang akan anda ubah?",
        "a": 'Saya ingin mengubah sistem filter di keranjang, saat ini jika kita punya banyak barang dari toko berbeda, sulit untuk menyaring barang berdasarkan kategori tertentu tanpa harus mencarinya satu per satu di daftar yang panjang.'
    },
    {
        "q": "Kalau berandai-andai, apa solusi ideal menurut anda?",
        "a": 'Adanya fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan, jadi tidak perlu bolak-balik buka profil toko. Tidak ada aplikasi lain yang lebih baik dari TikTokShop karena bisa melihat produk secara "hidup" melalui video dan Live.'
    },
]

# Find Widya's interview grid (4th persona, data-panel="3")
# The grid starts after the panel comment
# Find the 4th occurrence of persona__interview-grid
grid_starts = [m.start() for m in re.finditer(r'<div class="persona__interview-grid">', content)]
widya_grid_start = grid_starts[3]  # 0-indexed, 4th panel

# Find the closing of this grid
grid_end_pattern = re.compile(r'</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
# Find the grid end after widya_grid_start
# The grid closes with: </div> (grid) </div> (bottom) </div> (persona__top or grid wrapper) 
# Let me find the matching </div> for persona__interview-grid
# I'll count the content between grid start and the next persona__panel or define section

# Simpler approach: find the placeholder block and replace it
placeholder_pattern = re.compile(
    r'(<div class="persona__interview-grid">)\s*\n(.*?)\n(\s*</div>\s*</div>\s*</div>\s*</div>)',
    re.DOTALL
)

# Find all matches
all_matches = list(placeholder_pattern.finditer(content))
print(f"Found {len(all_matches)} interview grids")

if len(all_matches) >= 4:
    match = all_matches[3]  # 4th grid (Widya's)
    print(f"Replacing Widya's grid at position {match.start()}-{match.end()}")
    
    # Build new HTML
    new_items = []
    for i, qa in enumerate(qa_data, 1):
        item = f'''
                  <div class="interview__qa-item">
                    <div class="interview__sticky--red">
                      <strong>Question {i}:</strong><br>
                      {qa["q"]}
                    </div>
                    <div class="interview__sticky--yellow">
                      <strong>Answer:</strong><br>
                      {qa["a"]}
                    </div>
                  </div>'''
        new_items.append(item)
    
    new_grid_content = '\n'.join(new_items)
    new_html = f'{match.group(1)}\n{new_grid_content}\n{match.group(3)}'
    
    content = content[:match.start()] + new_html + content[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Done! Widya's interview data inserted successfully.")
else:
    print("ERROR: Could not find enough interview grids")
