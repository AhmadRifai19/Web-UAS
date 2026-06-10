import re

html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Widya journey table data (from Frame 117)
widya_table = '''                                                <div class="persona__journey-table-wrapper">
                  <table class="persona__journey-table">
                    <thead>
                      <tr>
                        <th>WIDYA DNY YUANIKA R.</th>
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
                        <td><ul><li>Merasakan kebutuhan mendesak (bawa suami ke RS), ingat rekomendasi anak/tetangga tentang Gojek, mencari dan membuka aplikasi Gojek di HP.</li></ul></td>
                        <td><ul><li>Mencoba memahami perbedaan GoCar dan GoRide, membaca-baca tulisan kecil pada ikon, membuka aplikasi, melihat layar penuh ikon.</li></ul></td>
                        <td><ul><li>Mengetuk ikon GoCar, bingung mengisi alamat (lokasi saat ini &amp; tujuan), memilih "Bayar Tunai" karena tidak paham GoPay, menunggu konfirmasi driver menerima pesanan.</li></ul></td>
                        <td><ul><li>Menerima telepon/chat dari driver, menunggu driver tiba, naik ke kendaraan, memantau perjalanan lewat map di aplikasi.</li></ul></td>
                        <td><ul><li>Turun di tujuan, menerima notifikasi untuk memberi rating, bingung dan menutup notifikasi.</li></ul></td>
                      </tr>
                      <tr>
                        <td>EMOSI</td>
                        <td><ul><li>Khawatir, Cemas, Panik</li></ul></td>
                        <td><ul><li>Kewalahan, Frustrasi, Bingung</li></ul></td>
                        <td><ul><li>Harap-harap Cemas, Tidak Sabar, Tegang</li></ul></td>
                        <td><ul><li>Berharap driver sopan, Sedikit Lega tapi masih Cemas</li></ul></td>
                        <td><ul><li>Bersyukur, Lega</li></ul></td>
                      </tr>
                      <tr>
                        <td>PAIN POINT</td>
                        <td><ul><li>Teknologi bukanlah pilihan pertama, butuh dorongan situasi darurat; tidak hafal letak aplikasi.</li></ul></td>
                        <td><ul><li>Tampilan aplikasi terlalu ramai dan banyak ikon; banyak layanan tidak relevan (GoMassage, dll); tulisan dan ikon terlalu kecil, sulit dibaca.</li></ul></td>
                        <td><ul><li>Bingung cara input alamat yang benar; takut salah memencet tombol; tidak percaya dengan pembayaran digital (GoPay).</li></ul></td>
                        <td><ul><li>Gugup jika driver tidak bisa menemukan lokasinya; takut dengan driver yang tidak dikenal.</li></ul></td>
                        <td><ul><li>Tidak mengerti tujuan memberi rating; menganggapnya merepotkan.</li></ul></td>
                      </tr>
                      <tr>
                        <td>PELUANG SOLUSI</td>
                        <td><ul><li>Fitur "SOS" atau "Darurat" di layar utama yang langsung memesan GoCar ke rumah sakit terdekat; ikon yang besar dan jelas.</li></ul></td>
                        <td><ul><li>"Simple Mode" untuk user seperti Lasmini: hanya menampilkan 3 layanan utama (GoCar, GoFood, GoSend); gunakan tulisan dan ikon yang lebih besar; voice command ("OK Google, pesankan GoCar").</li></ul></td>
                        <td><ul><li>Deteksi lokasi otomatis yang lebih akurat; tombol "Gunakan Lokasi Saya Sekarang" yang sangat menonjol; opsi "Bayar Tunai" sebagai default untuk user tertentu; konfirmasi pesanan dengan suara "Pesanan Anda Diterima!".</li></ul></td>
                        <td><ul><li>Fitur "Bagikan Perjalanan" otomatis ke keluarga; notifikasi: "Driver Anda, Pak Budi, sedang menuju lokasi Anda."; tampilan map yang sederhana dengan foto driver yang besar.</li></ul></td>
                        <td><ul><li>Rating yang lebih sederhana, misal hanya "\u263a" atau "\u2639"; pesan: "Terima kasih Ibu Lasmini, semoga suami lekas sembuh." (Personal &amp; empatik).</li></ul></td>
                      </tr>
                    </tbody>
                  </table>
                </div>'''

# Find the LAST empty journey section (Widya's - the only remaining one)
# It's preceded by "Rekomendasi akurat dari history pembelian pengguna"
old = '''                <h4 class="persona__section-title persona__section-title--green">User Journey Map</h4>
                                </div>
                </div>
              </div>
<!-- Interview Data -->'''

new = '''                <h4 class="persona__section-title persona__section-title--green">User Journey Map</h4>
''' + widya_table + '''
              </div>
            </div>
<!-- Interview Data -->'''

# Count occurrences
count = content.count(old)
print(f"Found {count} occurrence(s) of the pattern")

if count == 1:
    content = content.replace(old, new)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced Widya's journey table successfully!")
else:
    print("ERROR: Expected exactly 1 match, got", count)
