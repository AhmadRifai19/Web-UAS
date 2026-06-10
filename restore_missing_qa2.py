import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Missing items for Haris (panel 2), Widya (panel 3), Zaskiya (panel 4)
# These weren't added due to position shifting
missing = [
    (2, "Apakah jika produk anda berhasil masuk ke dalam platform e-commerce, anda tetap memberikan yang terbaik ke pelanggan?",
     "Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain yang kami tawarkan."),
    (3, 'Kalau berandai-andai, apa solusi ideal menurut anda?',
     'Adanya fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan, jadi tidak perlu bolak-balik buka profil toko. Tidak ada aplikasi lain yang lebih baik dari TikTokShop karena bisa melihat produk secara "hidup" melalui video dan Live.'),
    (4, "Menurut anda untuk mempermudah dalam melakukan pembelian, bagaimana alur jalannya pembelian agar mempermudah anda dalam membeli?",
     "Pencarian produk yang cepat dan akurat, informasi produk yang jelas (harga, deskripsi, dan ulasan), pilihan metode pembayaran yang lengkap dan mudah, proses checkout yang singkat (tidak terlalu banyak langkah), konfirmasi pesanan yang jelas."),
]

# Insert from last to first to avoid position shifting
for panel_idx, q_text, a_text in reversed(missing):
    # Re-find tables each time
    tables = list(re.finditer(r'class="interview__table-wrapper"', content))
    if panel_idx < len(tables):
        match = tables[panel_idx]
        tbody_close = content.find('</tbody>', match.start())
        if tbody_close > 0:
            new_row = f'                    <tr>\n                      <th>Question {q_text}</th>\n                      <td>{a_text}</td>\n                    </tr>\n'
            content = content[:tbody_close] + new_row + content[tbody_close:]
            print(f"  OK: Added missing item for panel {panel_idx}")
    else:
        print(f"  ERROR: Panel {panel_idx} not found")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
