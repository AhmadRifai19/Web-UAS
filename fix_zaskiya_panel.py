import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# PROBLEM 1: Zaskiya's Interview Data is outside the panel
# The interview data at line ~965 needs to be inside the panel
# Currently the structure is:
#   </div>  (line 960 - closes journey section)
#   </div>  (line 961 - closes persona__grid)
#   </div>  (line 962 - closes persona__panel) 
#   </div>  (line 963 - extra)
#   <!-- Interview Data -->  <-- OUTSIDE!
#
# It should be:
#   </div>  (closes journey section)
#   <!-- Interview Data -->  <-- INSIDE persona__grid
#   </div>  (closes persona__grid)
#   </div>  (closes persona__panel)

# Find Zaskiya's panel (data-panel="4") and its interview data
# The interview data for Zaskiya starts with "<!-- Interview Data -->"
# and needs to be moved inside the panel

# Find the pattern: the panel 4 closing divs followed by Interview Data
# Look for: </div>\n...<!-- Interview Data -->\n...<div class="persona__interview-row">
panel5_pattern = re.compile(
    r'(            </div>\s*'  # closes journey section-box or bottom
    r'          </div>\s*'     # closes persona__grid  
    r'        </div>\s*'       # closes persona__panel
    r'      </div>\s*'         # extra close
    r')(<!-- Interview Data -->\s*'
    r'<div class="persona__interview-row">.*?</table>\s*</div>)\s*\n',
    re.DOTALL
)

match5 = panel5_pattern.search(content)
if match5:
    # Move interview data inside the panel
    # Remove the extra </div> and restructure
    journey_close = "            </div>\n"  # closes journey section
    grid_close = "          </div>\n"  # closes persona__grid
    panel_close = "        </div>\n"  # closes persona__panel
    
    interview_block = match5.group(2)
    
    # Build correct structure:
    # journey_close
    # interview_block (properly indented inside persona__grid)
    # grid_close
    # panel_close
    replacement = journey_close + '\n' + interview_block + '\n' + grid_close + panel_close
    
    content = content[:match5.start()] + replacement + content[match5.end():]
    print("OK: Moved Zaskiya's Interview Data inside the panel")
else:
    print("Pattern not found, trying alternative approach...")
    # Alternative: manually find and restructure
    # Find "<!-- Interview Data -->" that's at the wrong position
    interview_markers = [m.start() for m in re.finditer(r'<!-- Interview Data -->', content)]
    print(f"  Found {len(interview_markers)} Interview Data markers")
    
    if len(interview_markers) >= 5:
        # The 5th marker is Zaskiya's
        zaskiya_interview = interview_markers[4]
        
        # Find the end of Zaskiya's table
        zaskiya_table_end = content.find('</table>', zaskiya_interview)
        zaskiya_table_wrapper_end = content.find('</div>', zaskiya_table_end) + len('</div>')
        
        # Find the closing divs before this interview section
        # Go backward from zaskiya_interview to find the panel closing divs
        before_interview = content[zaskiya_interview-200:zaskiya_interview]
        print(f"  Before Zaskiya interview: {repr(before_interview[-80:])}")

# PROBLEM 2: Missing closing tags for persona section before define
# After the last panel, we need:
#   </div>  ← close persona__tabs
#   </div>  ← close container
# </section>  ← close persona section
# 
# <section class="define"...

define_pos = content.find('<section class="define"')
if define_pos > 0:
    # Check what's right before the define section
    before_define = content[define_pos-100:define_pos].rstrip()
    
    if '</section>' not in before_define:
        # Find the last </div> before define
        last_div = content.rfind('</div>', 0, define_pos)
        
        if last_div > 0:
            # Insert closing tags after the last </div>
            insert_pos = last_div + len('</div>')
            section_closing = '\n      </div>\n    </section>\n\n'
            content = content[:insert_pos] + section_closing + content[insert_pos:]
            print("OK: Added persona section closing tags before Define section")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone!")
