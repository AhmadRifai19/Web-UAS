import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Zaskiya journey table HTML
zaskiya_table = '''                                                <div class="persona__journey-table-wrapper">
                  <table class="persona__journey-table">
                    <thead>
                      <tr>
                        <th>ZASKIYA SANDI A.A.</th>
                        <th>STAGE 1<br>AWARENESS</th>
                        <th>STAGE 2<br>CONSIDERATION</th>
                        <th>STAGE 3<br>BOOKING</th>
                        <th>STAGE 4<br>RIDE</th>
                        <th>STAGE 5<br>AFTER USE</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>AKTIVITAS</td>
                        <td><ul><li>Membuka aplikasi, melihat halaman utama, dan mencari fitur atau produk yang ingin dibeli.</li></ul></td>
                        <td><ul><li>Mengecek ketersediaan barang dan membaca detail informasi produk sebelum memutuskan.</li></ul></td>
                        <td><ul><li>Melanjutkan pesanan ke tahap pengiriman, melihat rincian biaya, dan mengecek ongkos kirim.</li></ul></td>
                        <td><ul><li>Memilih metode pembayaran yang tersedia dan mencoba menyelesaikan transaksi.</li></ul></td>
                        <td><ul><li>Menerima bukti bahwa transaksi telah berhasil dan pesanan sedang diproses.</li></ul></td>
                      </tr>
                      <tr>
                        <td>EMOSI</td>
                        <td><ul><li>Bingung / Kewalahan</li></ul></td>
                        <td><ul><li>Kecewa (jika barang habis)</li></ul></td>
                        <td><ul><li>Kesal (jika ongkir mahal)</li></ul></td>
                        <td><ul><li>Frustrasi (jika error)</li></ul></td>
                        <td><ul><li>Lega</li></ul></td>
                      </tr>
                      <tr>
                        <td>PAIN POINT</td>
                        <td><ul><li>Tampilan aplikasi terlalu ramai (banyak promo/banner).</li><li>Menu terlalu banyak tapi tidak terorganisir dengan baik.</li><li>Kesulitan mencari fitur yang ingin digunakan.</li></ul></td>
                        <td><ul><li>Stok barang tiba-tiba habis saat sedang dipertimbangkan untuk dibeli.</li></ul></td>
                        <td><ul><li>Ongkos kirim sering kali dirasa terlalu mahal.</li><li>Alur pembelian berisiko terasa berbelit jika terlalu banyak langkah.</li></ul></td>
                        <td><ul><li>Metode pembayaran sering mengalami error.</li><li>Pilihan metode pembayaran terkadang tidak tersedia.</li></ul></td>
                        <td><ul><li>Sering merasa khawatir jika status pesanan setelah membayar tidak langsung diperbarui.</li></ul></td>
                      </tr>
                      <tr>
                        <td>PELUANG SOLUSI</td>
                        <td><ul><li>Sederhanakan tampilan (hapus banner berlebih).</li><li>Kelompokkan fitur sesuai kategori yang jelas.</li><li>Sembunyikan/hapus fitur yang jarang dipakai di halaman utama.</li><li>Buat pencarian produk yang cepat dan akurat.</li></ul></td>
                        <td><ul><li>Tampilkan informasi produk yang jelas dan lengkap (harga, deskripsi, ulasan).</li><li>Sinkronisasi sistem agar stok barang selalu real-time.</li></ul></td>
                        <td><ul><li>Buat proses checkout yang singkat (tidak terlalu banyak langkah).</li><li>Sediakan subsidi/promo ongkos kirim yang mudah diklaim.</li></ul></td>
                        <td><ul><li>Sediakan pilihan metode pembayaran yang lengkap dan mudah digunakan.</li><li>Pastikan stabilitas server saat memproses pembayaran.</li></ul></td>
                        <td><ul><li>Berikan halaman dan notifikasi konfirmasi pesanan yang sangat jelas segera setelah pembayaran berhasil.</li></ul></td>
                      </tr>
                    </tbody>
                  </table>
                </div>'''

# Find the LAST occurrence of the Widya journey table wrapper (which is wrongly in Zaskiya's panel)
# We search for the table that starts with <th>WIDYA and replace it
# Find all occurrences of the Widya table header
pattern = r'<th>WIDYA DNY YUANIKA R\.</th>'
matches = list(re.finditer(pattern, content))
print(f"Found {len(matches)} occurrences of 'WIDYA DNY YUANIKA R.'")

if len(matches) == 2:
    # We need to replace the SECOND occurrence's entire table
    # Find the table wrapper around the second match
    second_match = matches[1]
    
    # Find the start of the journey-table-wrapper div before this match
    wrapper_start = content.rfind('<div class="persona__journey-table-wrapper">', 0, second_match.start())
    # Find the end of the wrapper div after the table
    # The table ends with </table>, then </div> closes the wrapper
    table_end = content.find('</table>', second_match.start())
    wrapper_end = content.find('</div>', table_end) + len('</div>')
    
    old_section = content[wrapper_start:wrapper_end]
    content = content[:wrapper_start] + zaskiya_table + content[wrapper_end:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced Zaskiya's journey table!")
else:
    print(f"ERROR: Expected 2 occurrences, found {len(matches)}")
