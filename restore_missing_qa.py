import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The last Q&A items that were lost during conversion
# Each panel's last question
missing_items = [
    # (panel_name, last_question_text, answer_text)
    ("Fikri", "Jika bisa mengubah atau menambahkan satu fitur pada aplikasi bisnis, apa yang ingin Anda tambahkan?",
     "Saya ingin ada fitur promosi otomatis yang bisa membantu menjangkau lebih banyak pelanggan tanpa harus dilakukan secara manual, supaya lebih praktis dan hemat waktu."),
    ("Susanto", "Menurut Anda, apa yang bisa membuat pengelolaan toko lebih mudah?",
     "Saya perlu aplikasi yang mencatat jumlah stok barang serta harga dari setiap supplier."),
    ("Haris", "Apakah jika produk anda berhasil masuk ke dalam platform e-commerce, anda tetap memberikan yang terbaik ke pelanggan?",
     "Ya, saya bersama rekan tim tetap memberikan yang terbaik ke pelanggan dan terus meningkatkan kualitas jasa desain yang kami tawarkan."),
    ("Widya", "Kalau berandai-andai, apa solusi ideal menurut anda?",
     'Adanya fitur "Quick Comparison" untuk membandingkan dua produk dari toko berbeda dalam satu tampilan, jadi tidak perlu bolak-balik buka profil toko. Tidak ada aplikasi lain yang lebih baik dari TikTokShop karena bisa melihat produk secara "hidup" melalui video dan Live.'),
    ("Zaskiya", "Menurut anda untuk mempermudah dalam melakukan pembelian, bagaimana alur jalannya pembelian agar mempermudah anda dalam membeli?",
     "Pencarian produk yang cepat dan akurat, informasi produk yang jelas (harga, deskripsi, dan ulasan), pilihan metode pembayaran yang lengkap dan mudah, proses checkout yang singkat (tidak terlalu banyak langkah), konfirmasi pesanan yang jelas."),
]

# Find all interview tables and add the missing row before </tbody>
tables = list(re.finditer(r'class="interview__table-wrapper"', content))

for i, match in enumerate(tables):
    if i < len(missing_items):
        name, q_text, a_text = missing_items[i]
        
        # Find the </tbody> after this table
        tbody_close_pos = content.find('</tbody>', match.start())
        
        if tbody_close_pos > 0:
            new_row = f'''                    <tr>
                      <th>Question {q_text}</th>
                      <td>{a_text}</td>
                    </tr>
'''
            content = content[:tbody_close_pos] + new_row + content[tbody_close_pos:]
            print(f"  OK: Added missing Q10 for {name}")
        else:
            print(f"  ERROR: Could not find </tbody> for {name}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! All missing Q&A items restored.")
