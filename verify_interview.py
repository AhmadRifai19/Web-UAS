file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

interviewers = ['Gavin', 'David', 'Hafidh', 'Hayyu', 'Rifai']
for name in interviewers:
    count = content.count(f'Jawaban ({name})')
    print(f'{name}: {count} entries')

# Check for remaining placeholders
placeholder_count = content.count('[Isi Pertanyaan')
belum_count = content.count('[Belum ada data]')
print(f'\nRemaining old placeholders: {placeholder_count}')
print(f'Empty slots (Belum ada data): {belum_count}')
