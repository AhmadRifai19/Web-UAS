html_path = r'c:\semester 2\Web UAS\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the extra </div> between Panel 3 and Panel 4
old = '''            </div>

            
            </div>




        <!-- === Panel 5: Zaskiya Soaldi A.A. === -->'''

new = '''            </div>

            </div>
            </div>

        <!-- === Panel 5: Zaskiya Soaldi A.A. === -->'''

if old in content:
    content = content.replace(old, new)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed gap between Panel 3 and Panel 4")
else:
    print("Pattern not found!")
