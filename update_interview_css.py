file_path = 'c:/semester 2/Web UAS/css/style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """/* =========================================
   Interview Data
   ========================================= */
.persona__interview-row {
  margin-top: 1.5rem;
}

.interview__qa-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

.interview__qa-item {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 1rem;
}

.interview__sticky--red {
  background-color: #fca5a5;
  padding: 0.75rem;
  border-radius: 4px;
  color: #7f1d1d;
  box-shadow: 1px 2px 4px rgba(0,0,0,.06);
  font-size: 0.75rem;
  line-height: 1.45;
}

.interview__sticky--yellow {
  background-color: #fef08a;
  padding: 0.75rem;
  border-radius: 4px;
  color: #713f12;
  box-shadow: 1px 2px 4px rgba(0,0,0,.06);
  font-size: 0.75rem;
  line-height: 1.45;
}


.persona__interview-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  padding: 1.5rem;
}"""

new_css = """/* =========================================
   Interview Data (Table Style)
   ========================================= */
.persona__interview-row {
  margin-top: 1.5rem;
}

.persona__interview-grid {
  margin-top: 1rem;
}

.interview__table-wrapper {
  width: 100%;
  overflow-x: auto;
  border-radius: 8px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.interview__table {
  width: 100%;
  border-collapse: collapse;
  background: var(--white);
  font-size: 0.85rem;
}

.interview__table th,
.interview__table td {
  border: 1px solid var(--border);
  padding: .85rem 1rem;
  vertical-align: top;
  line-height: 1.5;
}

.interview__table th {
  background-color: #fca5a5;
  color: #7f1d1d;
  font-weight: 700;
  width: 35%;
  font-size: 0.85rem;
  text-align: left;
}

.interview__table td {
  background-color: #fef9c3;
  color: #713f12;
  font-size: 0.85rem;
}

.interview__table tr:hover td {
  background-color: #fef08a;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("OK: Interview CSS replaced with table style")
else:
    print("ERROR: Could not find old CSS block")
    # Debug: print nearby text
    idx = content.find("Interview Data")
    if idx > -1:
        print(f"Found 'Interview Data' at pos {idx}")
        print(repr(content[idx-50:idx+200]))
    else:
        print("'Interview Data' not found")
