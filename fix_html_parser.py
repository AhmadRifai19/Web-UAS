import re
from html.parser import HTMLParser

class PersonaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.tags = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.depth += 1
            self.tags.append(('start', tag, attrs, self.depth))
            
    def handle_endtag(self, tag):
        if tag == 'div':
            self.tags.append(('end', tag, None, self.depth))
            self.depth -= 1

# Let's write a simpler script. We just need to replace the entire bottom part of each panel.
# We know the journey map starts with "<!-- User Journey Map -->"
# We know the interview data starts with "<!-- Interview Data -->"
# Let's just find the start of the Journey Map or Interview Data, and clear everything from there until the end of the persona__grid.
# Then we reconstruct it properly!
