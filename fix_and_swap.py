import re

file_path = 'c:/semester 2/Web UAS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# For each panel, we want to ensure Interview Data comes AFTER User Journey Map.
# We also want to fix the malformed </div></div> from the previous journey injection.
# First, let's fix the malformed </div></div> in the journey table wrappers.
content = content.replace('</div></div>\n                </div>\n              </div>\n            </div>', '</div>\n              </div>\n            </div>')
content = content.replace('</div></div>\n                </div>', '</div>\n                </div>')

# Now let's do the swapping
panels = re.split(r'(<div class="persona__panel.*?>)', content)

new_content = panels[0]

for i in range(1, len(panels), 2):
    panel_start = panels[i]
    panel_body = panels[i+1]
    
    interview_match = re.search(r'(<!-- Interview Data -->.*?)(?=<!-- User Journey Map -->)', panel_body, re.DOTALL)
    
    if interview_match:
        interview_str = interview_match.group(1)
        # Remove it from its current position
        panel_body = panel_body.replace(interview_str, '', 1)
        
        # Now find the end of the Journey Map.
        # It's bounded by <!-- User Journey Map --> and the closing tags of the persona grid.
        # Let's insert the interview_str right before the last closing tags of the grid.
        # The panel ends with:
        #           </div> (persona__grid)
        #         </div> (persona__panel)
        # We can find the last '          </div>\n        </div>'
        # Or simply, we insert it after the end of the persona__journey-row.
        # Let's find:
        journey_end_match = re.search(r'(<!-- User Journey Map -->.*?</div>\s*</div>\s*</div>)', panel_body, re.DOTALL)
        
        if journey_end_match:
            journey_full_str = journey_end_match.group(1)
            # Replace the journey block with itself + interview_str
            panel_body = panel_body.replace(journey_full_str, journey_full_str + '\n' + interview_str, 1)
        
    new_content += panel_start + panel_body

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Swapped all blocks and fixed HTML.")
