file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Step 1: Remove the misplaced Q&A row from Zaskiya's journey table (lines 951-954, 0-indexed: 950-953)
# Find the misplaced row - it's the Q&A row inside the journey table
misplaced_start = None
misplaced_end = None
for i, line in enumerate(lines):
    if 'Question Menurut anda untuk mempermudah dalam melakukan pembelian' in line and i < 960:
        # This is in the journey table area - it's misplaced
        # Find the start of this <tr>
        j = i
        while j > 0 and '<tr>' not in lines[j]:
            j -= 1
        misplaced_start = j
        # Find the end </tr>
        k = i
        while k < len(lines) and '</tr>' not in lines[k]:
            k += 1
        misplaced_end = k + 1
        break

if misplaced_start is not None:
    print(f"Found misplaced Q&A row at lines {misplaced_start+1}-{misplaced_end}")
    # Remove these lines
    del lines[misplaced_start:misplaced_end]
    print("Removed misplaced Q&A row from journey table")

# Write back for now to re-index
content = ''.join(lines)

# Step 2: Fix the Interview Data section structure
# The interview data for Zaskiya needs to be inside the panel
# Current structure around Zaskiya's interview:
#   </table> (journey table)
#   </div>   (journey table-wrapper)
#   </div>   (extra?)
#   </div>   (closes journey-row section-box)
#   </div>   (closes journey-row)
#
#   <!-- Interview Data -->
#   <div class="persona__interview-row">...
#   </div>   (closes interview-row)
#
# We need the interview to be inside the panel, before panel/grid close

# Find the Zaskiya interview section
zaskiya_interview_start = content.find('<!-- Interview Data -->\n            <div class="persona__interview-row">\n              <div class="persona__section-box">\n                <h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>\n                <div class="persona__interview-grid">\n                <div class="interview__table-wrapper">\n                  <table class="interview__table">\n                    <tbody>\n                    <tr>\n                      <th>Question Perkenalkan diri anda')

if zaskiya_interview_start == -1:
    # Try a broader search
    # Find the 5th "Interview Data" comment
    import re
    markers = [m.start() for m in re.finditer(r'<!-- Interview Data -->', content)]
    if len(markers) >= 5:
        zaskiya_interview_start = markers[4]
        print(f"Found 5th Interview Data at position {zaskiya_interview_start}")

# Find the journey table close before Zaskiya's interview data
# Look for the last </table> before the interview section
last_table_close = content.rfind('</table>', 0, zaskiya_interview_start)
after_journey = last_table_close + len('</table>')

# Find the closing divs between journey table and interview section
between = content[after_journey:zaskiya_interview_start]
print(f"Between journey table and interview: {repr(between)}")

# Find the end of Zaskiya's interview section
# Look for the last </div> of the interview section
zaskiya_table_close = content.find('</table>', zaskiya_interview_start)
# After </table>, find closing divs up to persona section closing
after_interview_table = zaskiya_table_close + len('</table>')

# Find where the persona section closes or define section starts
define_pos = content.find('<section class="define"')
# Everything from after_interview_table to define_pos needs to be restructured
end_region = content[after_interview_table:define_pos]
print(f"\nEnd region ({len(end_region)} chars):")
print(repr(end_region[:300]))
print("...")
print(repr(end_region[-200:]))

# Build the correct replacement
# The correct structure after the journey </table> should be:
# </div>           ← close journey table-wrapper
# </div>           ← close journey section-box
# </div>           ← close journey-row
#
# <!-- Interview Data -->
# <div class="persona__interview-row">
#   <div class="persona__section-box">
#     <h4>Interview Data</h4>
#     <div class="persona__interview-grid">
#       <div class="interview__table-wrapper">
#         <table>...existing interview rows...</table>
#       </div>
#     </div>
#   </div>
# </div>
# </div>           ← close persona__grid
# </div>           ← close persona__panel
# </div>           ← close persona__tabs
# </div>           ← close container
# </section>       ← close persona

# Extract the interview table content (rows)
interview_table_start = content.find('<table class="interview__table">', zaskiya_interview_start)
interview_tbody_start = content.find('<tbody>', interview_table_start)
interview_tbody_end = content.find('</tbody>', interview_table_start)
interview_rows = content[interview_tbody_start:interview_tbody_end + len('</tbody>')]

# Build the complete correct ending
correct_ending = """</div>
              </div>
            </div>

            <!-- Interview Data -->
            <div class="persona__interview-row">
              <div class="persona__section-box">
                <h4 class="persona__section-title persona__section-title--orange">Interview Data</h4>
                <div class="persona__interview-grid">
                <div class="interview__table-wrapper">
                  <table class="interview__table">
                    """ + interview_rows + """
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</section>

"""

# Replace everything from after_journey to define_pos
content = content[:after_journey] + '\n' + correct_ending + content[define_pos:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! Zaskiya's panel structure fixed.")
