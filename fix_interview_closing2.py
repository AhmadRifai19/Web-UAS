import re

file_path = 'c:/semester 2/Web UAS/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The correct closing structure after each interview table should be:
# </table>
#               </div>   ← close interview__table-wrapper  (14 spaces)
#             </div>     ← close persona__interview-grid  (12 spaces)  
#           </div>       ← close persona__section-box     (10 spaces)
#         </div>         ← close persona__interview-row   (8 spaces)
#       </div>           ← close persona__grid            (6 spaces)
#     </div>             ← close persona__panel           (4 spaces)
#
# Then: blank line + next panel comment or section closing tags

# For the LAST panel, also need:
#     </div>             ← close persona__tabs
#   </div>               ← close container
# </section>             ← close persona section

correct_closing = """                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

"""

# Find all Interview Data sections
sections = list(re.finditer(r'<!-- Interview Data -->', content))
print(f"Found {len(sections)} Interview Data sections")

for i, match in enumerate(sections):
    start = match.start()
    
    # Find </table> after this section
    table_close = content.find('</table>', start)
    
    # Find the first </div> after </table> (this closes interview__table-wrapper)
    # Actually the </table> is followed by \n then </div> for the table-wrapper
    # Let me find the position right after </table>\n and any whitespace up to first </div>
    after_table = table_close + len('</table>')
    
    # Skip whitespace and find first </div>
    rest = content[after_table:]
    first_div_match = re.match(r'\s*</div>', rest)
    if first_div_match:
        # This </div> closes the interview__table-wrapper
        table_wrapper_end = after_table + first_div_match.end()
    else:
        print(f"  ERROR: Could not find table-wrapper close for panel {i+1}")
        continue
    
    # Now find where the next section starts
    if i < len(sections) - 1:
        # Find the next panel comment
        next_marker = content.find('<!-- Panel', table_wrapper_end)
        if next_marker == -1:
            next_marker = content.find('<!-- ', table_wrapper_end)
    else:
        # Last panel - find the define section or end of persona section
        next_marker = content.find('<section class="define"', table_wrapper_end)
        if next_marker == -1:
            next_marker = content.find('<!-- =', table_wrapper_end)
    
    if next_marker == -1:
        print(f"  ERROR: Could not find next section marker for panel {i+1}")
        continue
    
    # Replace everything between table_wrapper_end and next_marker
    # with the correct closing divs
    old_region = content[table_wrapper_end:next_marker]
    old_div_count = old_region.count('</div>')
    
    content = content[:table_wrapper_end] + '\n' + correct_closing + content[next_marker:]
    
    print(f"  Panel {i+1}: Replaced {old_div_count} closing divs with 5 correct ones")

# Now fix the LAST panel - it needs extra closing tags for persona__tabs, container, and section
# Find the last panel's correct_closing and add the section closers

# Find the define section
define_pos = content.find('<section class="define"')
if define_pos > 0:
    # Check what's before the define section
    before_define = content[define_pos-200:define_pos]
    
    # We need to add closing tags for persona__tabs, container, and section
    # The correct structure should be:
    #       </div>  ← close persona__panel (already in correct_closing)
    #     </div>    ← close persona__tabs
    #   </div>      ← close container  
    # </section>    ← close persona section
    # 
    # <section class="define"...
    
    # Find the last "correct_closing" block before define section
    # Look for the pattern of the correct closing
    last_closing_pattern = r'(        </div>\n      </div>\n\n)(<section class="define")'
    last_match = re.search(last_closing_pattern, content)
    
    if last_match:
        # Add persona section closing tags
        section_close = """        </div>
      </div>
    </section>

"""
        content = content[:last_match.start()] + section_close + content[last_match.start(2):]
        print("  Added persona section closing tags before Define section")
    else:
        print("  WARNING: Could not find last closing to add section tags")
        # Let's try a simpler approach
        # Just check if </section> exists before define section
        section_check = content[define_pos-100:define_pos]
        if '</section>' not in section_check:
            print("  No </section> found before define, adding it")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone fixing all interview panel closing tags!")
