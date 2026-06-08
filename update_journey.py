import re

file_path = r'c:\semester 2\Web UAS\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

table_html = """                <div class="persona__journey-table-wrapper">
                  <table class="persona__journey-table">
                    <thead>
                      <tr>
                        <th>Customer Phase</th>
                        <th>Stage 1<br>Awareness</th>
                        <th>Stage 2<br>Consideration</th>
                        <th>Stage 3<br>Booking</th>
                        <th>Stage 4<br>Ride</th>
                        <th>Stage 5<br>After Use</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Aktivitas</td>
                        <td><ul><li>[Isi Aktivitas]</li></ul></td>
                        <td><ul><li>[Isi Aktivitas]</li></ul></td>
                        <td><ul><li>[Isi Aktivitas]</li></ul></td>
                        <td><ul><li>[Isi Aktivitas]</li></ul></td>
                        <td><ul><li>[Isi Aktivitas]</li></ul></td>
                      </tr>
                      <tr>
                        <td>Emosi</td>
                        <td><ul><li>[Isi Emosi]</li></ul></td>
                        <td><ul><li>[Isi Emosi]</li></ul></td>
                        <td><ul><li>[Isi Emosi]</li></ul></td>
                        <td><ul><li>[Isi Emosi]</li></ul></td>
                        <td><ul><li>[Isi Emosi]</li></ul></td>
                      </tr>
                      <tr>
                        <td>Pain Point</td>
                        <td><ul><li>[Isi Pain Point]</li></ul></td>
                        <td><ul><li>[Isi Pain Point]</li></ul></td>
                        <td><ul><li>[Isi Pain Point]</li></ul></td>
                        <td><ul><li>[Isi Pain Point]</li></ul></td>
                        <td><ul><li>[Isi Pain Point]</li></ul></td>
                      </tr>
                      <tr>
                        <td>Peluang Solusi</td>
                        <td><ul><li>[Isi Peluang Solusi]</li></ul></td>
                        <td><ul><li>[Isi Peluang Solusi]</li></ul></td>
                        <td><ul><li>[Isi Peluang Solusi]</li></ul></td>
                        <td><ul><li>[Isi Peluang Solusi]</li></ul></td>
                        <td><ul><li>[Isi Peluang Solusi]</li></ul></td>
                      </tr>
                    </tbody>
                  </table>
                </div>"""

# Replace all `<div class="persona__journey-stages">...</div>` correctly
# The content is structured like:
#                 <div class="persona__journey-stages">
#                   <div class="persona__jstage">...</div>
#                   ... 5 of these ...
#                 </div>

pattern = re.compile(r'<div class="persona__journey-stages">.*?</div>\s*</div>', re.DOTALL)
# Wait, let's just find the exact block since the indentations are known.
# Actually, the closing div for persona__journey-stages is followed by </div> for persona__section-box.
# Better regex:
pattern = re.compile(r'<div class="persona__journey-stages">.*?(?=</div>\s*</div>\s*</div>)', re.DOTALL)

# Let's count how many we find
matches = pattern.findall(content)
print(f"Found {len(matches)} matches")

new_content = pattern.sub(table_html, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html")
