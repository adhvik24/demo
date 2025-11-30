import json
import re
import pdfplumber
from collections import Counter

# Phase 3: Content structure and thematic analysis
print("Phase 3: Identifying document structure and themes...")

# Load previous analysis
with open('/vercel/sandbox/pdf_structure.json', 'r', encoding='utf-8') as f:
    structure = json.load(f)

with open('/vercel/sandbox/pdf_analysis.json', 'r', encoding='utf-8') as f:
    analysis = json.load(f)

# Extract full text
full_text = ""
for page in structure['pages']:
    full_text += page['text'] + "\n"

# Identify document type and sections
document_type = "Unknown"
if "short story" in full_text.lower() or "short stories" in full_text.lower():
    document_type = "Literature/Short Story Collection"

# Find all section headers and their positions
sections = []
lines = full_text.split('\n')
for i, line in enumerate(lines):
    line_stripped = line.strip()
    # Look for section markers
    if re.match(r'^\d+/[IVX]+\s+', line_stripped):
        sections.append({
            'type': 'story_title',
            'line_number': i,
            'content': line_stripped
        })
    elif line_stripped.isupper() and len(line_stripped) > 3 and len(line_stripped) < 50:
        sections.append({
            'type': 'heading',
            'line_number': i,
            'content': line_stripped
        })
    elif re.match(r'^[A-Z][a-z]+ing\s+', line_stripped):
        sections.append({
            'type': 'activity_section',
            'line_number': i,
            'content': line_stripped
        })

# Identify key themes and topics
themes = []
if "dream" in full_text.lower():
    themes.append("Dreams")
if "story" in full_text.lower():
    themes.append("Storytelling")
if "character" in full_text.lower():
    themes.append("Character Development")
if "plot" in full_text.lower():
    themes.append("Plot Structure")

# Look for author mentions
authors = re.findall(r'by\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', full_text)
authors = list(set(authors))

# Identify if there are comprehension questions
has_comprehension = "understanding the text" in full_text.lower() or "comprehension" in full_text.lower()

# Character analysis - find proper nouns (potential character names)
proper_nouns = re.findall(r'\b[A-Z][a-z]+\b', full_text)
proper_noun_freq = Counter(proper_nouns)
# Filter out common words that might be capitalized
common_caps = {'The', 'A', 'An', 'I', 'In', 'It', 'This', 'That', 'These', 'Those', 'She', 'He', 'They', 'We'}
potential_characters = {name: count for name, count in proper_noun_freq.items() 
                       if count > 3 and name not in common_caps}

structure_analysis = {
    'document_type': document_type,
    'sections': sections,
    'section_count': len(sections),
    'themes': themes,
    'authors_mentioned': authors,
    'has_comprehension_questions': has_comprehension,
    'potential_characters': dict(sorted(potential_characters.items(), key=lambda x: x[1], reverse=True)[:10]),
    'content_structure': {
        'has_introduction': 'introduction' in full_text.lower(),
        'has_glossary': 'glossary' in full_text.lower(),
        'has_exercises': 'exercise' in full_text.lower() or 'activity' in full_text.lower(),
        'has_references': 'reference' in full_text.lower() or 'bibliography' in full_text.lower()
    }
}

with open('/vercel/sandbox/pdf_structure_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(structure_analysis, f, indent=2, ensure_ascii=False)

print(f"Document type: {document_type}")
print(f"Sections identified: {len(sections)}")
print(f"Themes: {', '.join(themes)}")
print(f"Authors mentioned: {', '.join(authors) if authors else 'None'}")
print(f"Has comprehension questions: {has_comprehension}")
print(f"\nPotential main characters:")
for char, count in list(potential_characters.items())[:5]:
    print(f"  {char}: {count} mentions")
print(f"\nContent structure:")
for key, value in structure_analysis['content_structure'].items():
    print(f"  {key}: {value}")
