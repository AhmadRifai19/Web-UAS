import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_about_section = '''<section class="about" id="features">
      <div class="about__inner container" style="align-items: flex-start;">

        <!-- Left: Explanation -->
        <div class="about__text" style="flex: 1.2;">
          <h2 class="about__title">Studi Kasus: <span class="accent">MarketSpace</span></h2>
          
          <div style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.1rem; color: var(--black); margin-bottom: 0.5rem; font-family: var(--font-heading);">Latar Belakang Masalah</h3>
            <p class="about__paragraph">
              Ekosistem e-commerce saat ini sering kali terlalu kompleks dan membingungkan bagi pengguna awam maupun pelaku UMKM tradisional. Tingkat literasi digital yang beragam menjadi tantangan besar, di mana tampilan antarmuka yang terlalu ramai justru memicu rasa frustrasi saat bertransaksi dan menyulitkan proses manajemen inventaris operasional harian.
            </p>
          </div>

          <div style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.1rem; color: var(--black); margin-bottom: 0.5rem; font-family: var(--font-heading);">Solusi yang Ditawarkan</h3>
            <p class="about__paragraph">
              MarketSpace hadir dengan pendekatan desain inklusif (<em>Inclusive Design</em>). Kami secara strategis mendekonstruksi setiap hambatan visual, menyederhanakan alur antarmuka, dan memangkas kompleksitas navigasi hingga 50%. Dipadukan dengan identitas palet warna hijau segar yang menenangkan, aplikasi ini menawarkan pengalaman transaksi yang <em>frictionless</em> dan sangat andal bagi seluruh kalangan.
            </p>
          </div>

          <div>
            <h3 style="font-size: 1.1rem; color: var(--black); margin-bottom: 0.5rem; font-family: var(--font-heading);">Peran &amp; Eksekusi Teknis</h3>
            <p class="about__paragraph about__paragraph--muted">
              Bertindak sebagai UX/UI Designer &amp; Web Developer, saya mengartikulasikan visi solusi ini melalui metodologi <em>Design Thinking</em>. Proses ini merangkum <em>Empathize</em> (Pemetaan Persona &amp; Affinity Diagram), <em>Ideation</em>, hingga <em>Prototyping</em> tingkat tinggi di Figma. Seluruh aset tersebut kemudian dieksekusi secara presisi menjadi struktur kode antarmuka yang dinamis, bersih, dan siap untuk skema web modern.
            </p>
          </div>
        </div>

        <!-- Right: Design Goals Card (Fitur & Inovasi) -->
        <div class="about__goals" style="flex: 1; position: sticky; top: 100px;">
          <h3 class="about__goals-title">Fitur &amp; Inovasi Utama</h3>

          <div class="about__goal">
            <div class="about__goal-icon about__goal-icon--green">🎯</div>
            <div>
              <h4 class="about__goal-name">Simplicity First Navigation</h4>
              <p class="about__goal-desc">Menghapus <em>banner</em> berlebih dan menerapkan "Simple Mode" agar pengguna fokus murni pada fitur inti tanpa distraksi.</p>
            </div>
          </div>

          <div class="about__goal">
            <div class="about__goal-icon about__goal-icon--brand">⚡</div>
            <div>
              <h4 class="about__goal-name">One-Click Checkout &amp; Akses Cepat</h4>
              <p class="about__goal-desc">Mereduksi <em>friction</em> bertransaksi secara drastis serta menyematkan visibilitas ekstra tinggi untuk fungsi utama yang mendesak.</p>
            </div>
          </div>

          <div class="about__goal">
            <div class="about__goal-icon about__goal-icon--blue">📊</div>
            <div>
              <h4 class="about__goal-name">Smart Inventory Tracker</h4>
              <p class="about__goal-desc">Sistem pencatatan inventaris cerdas dengan fitur pengisian otomatis (<em>auto-fill</em>) untuk meminimalisasi beban UMKM.</p>
            </div>
          </div>
          
          <div class="about__goal">
            <div class="about__goal-icon" style="background: #FFF3E0; color: #FF9800;">🔄</div>
            <div>
              <h4 class="about__goal-name">Real-time Synchronization</h4>
              <p class="about__goal-desc">Sinkronisasi data stok secara <em>real-time</em> dengan server backend untuk memastikan keakuratan pada tingkat tertinggi.</p>
            </div>
          </div>
        </div>

      </div>
    </section>'''

# Replace the section
new_content = re.sub(r'<section class="about" id="features">.*?</section>', new_about_section, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated about section.")
