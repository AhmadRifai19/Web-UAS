import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if interview data already exists to avoid duplicates
if "persona__interview-row" in content:
    print("Interview data already exists.")
else:
    # Build the template for 10 Q&A pairs
    qa_items = ""
    for i in range(1, 11):
        qa_items += f'''
                  <div class="interview__qa-item">
                    <div class="interview__sticky--red">
                      <strong>Question {i}:</strong><br>
                      [Isi Pertanyaan {i} di sini]
                    </div>
                    <div class="interview__sticky--yellow">
                      <strong>Answer:</strong><br>
                      [Isi Jawaban {i} di sini]
                    </div>
                  </div>'''

    interview_template = f'''
            <!-- Interview Data -->
            <div class="persona__interview-row">
              <div class="persona__section-box">
                <h4 class="persona__section-title persona__section-title--blue">Interview Data</h4>
                <div class="interview__qa-list">{qa_items}
                </div>
              </div>
            </div>
'''

    # Replace '<!-- User Journey Map -->' with the interview data followed by the journey map
    new_content = content.replace('<!-- User Journey Map -->', interview_template + '\n            <!-- User Journey Map -->')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected interview data templates.")
