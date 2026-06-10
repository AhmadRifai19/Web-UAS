import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The correct structure for each interview section should be:
# <div class="persona__interview-grid">
#   <div class="interview__table-wrapper">
#     <table class="interview__table">
#       <tbody>...</tbody>
#     </table>
#   </div>    <!-- close interview__table-wrapper -->
# </div>      <!-- close persona__interview-grid -->
# </div>      <!-- close persona__section-box -->
# </div>      <!-- close persona__interview-row -->

# Find each interview section and fix the closing tags
# Pattern: find from "Interview Data" comment to the end of the interview section
# The section should end before the next panel or the define section

# Strategy: For each persona__interview-grid, find everything between
# the closing </table></div> and the next <!-- comment or next panel

# Find all interview grid closings (after </table>\n...\n</div> for table-wrapper)
# Then fix the extra </div> tags

# Let's find each "Interview Data" section and fix it
panels_fixed = 0

# Find all occurrences of persona__interview-row sections
# We'll match from "<!-- Interview Data -->" to the closing structure
pattern = re.compile(
    r'(<!-- Interview Data -->\s*'
    r'<div class="persona__interview-row">\s*'
    r'<div class="persona__section-box">\s*'
    r'<h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>\s*'
    r'<div class="persona__interview-grid">\s*'
    r'<div class="interview__table-wrapper">\s*'
    r'<table class="interview__table">\s*'
    r'<tbody>.*?</tbody>\s*'
    r'</table>\s*'
    r'</div>)'  # close interview__table-wrapper
    r'(\s*</div>\s*</div>\s*</div>)',  # the 3 correct closing divs
    re.DOTALL
)

# First, let's identify what comes AFTER the broken closing tags
# to know where to stop removing divs

# Alternative approach: Find each interview section, then replace all 
# </div> tags between </div> (table-wrapper close) and the next meaningful content

# Let me use a different approach - find and fix each section individually
sections = list(re.finditer(r'<!-- Interview Data -->', content))
print(f"Found {len(sections)} Interview Data sections")

for i, match in enumerate(sections):
    start = match.start()
    
    # Find the table wrapper close after this section
    table_wrapper_close = content.find('</div>\n', content.find('</table>', start))
    
    # After table-wrapper </div>, we need exactly:
    # </div>  (close persona__interview-grid)
    # </div>  (close persona__section-box)
    # </div>  (close persona__interview-row)
    
    # Find what comes after the interview section
    # Look for the next section: either next panel, or define section, or persona tab buttons
    if i < len(sections) - 1:
        # Find the next panel start or the define section
        next_section = content.find('<!-- ', match.end())
        if next_section == -1:
            next_section = content.find('<section class="define"', start)
    else:
        # Last interview section - find the define section
        next_section = content.find('<section class="define"', start)
        if next_section == -1:
            next_section = content.find('<!-- DEFINE', start)
    
    if next_section == -1:
        # Try to find the end of the persona section
        next_section = content.find('</section>', start)
    
    # Extract the messy closing divs between table-wrapper close and next section
    messy_region = content[table_wrapper_close:next_section]
    
    # Count </div> tags in the messy region
    div_count = messy_region.count('</div>')
    print(f"  Panel {i+1}: Found {div_count} closing </div> tags (should be 3)")
    
    # Build the correct closing structure
    correct_closing = '</div>\n              </div>\n            </div>\n          </div>\n\n'
    
    # Replace the messy region with correct closing
    content = content[:table_wrapper_close] + correct_closing + content[next_section:]
    panels_fixed += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nFixed {panels_fixed} panels!")
