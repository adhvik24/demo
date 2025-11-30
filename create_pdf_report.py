from fpdf import FPDF
import json
import os

# Load analysis data
with open('/vercel/sandbox/pdf_structure.json', 'r', encoding='utf-8') as f:
    structure = json.load(f)

with open('/vercel/sandbox/pdf_analysis.json', 'r', encoding='utf-8') as f:
    analysis = json.load(f)

with open('/vercel/sandbox/pdf_structure_analysis.json', 'r', encoding='utf-8') as f:
    structure_analysis = json.load(f)

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, 'PDF Document Analysis Report', 0, 1, 'C')
        self.set_text_color(0, 0, 0)
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(230, 240, 250)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(3)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln()

print("Creating PDF report...")

pdf = PDFReport()
pdf.set_auto_page_break(auto=True, margin=15)

# Page 1: Cover and Summary
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(0, 51, 102)
pdf.ln(40)
pdf.cell(0, 15, 'Document Analysis Report', 0, 1, 'C')
pdf.set_font('Arial', 'I', 14)
pdf.set_text_color(64, 64, 64)
pdf.cell(0, 10, 'lekl101.pdf', 0, 1, 'C')
pdf.ln(20)

pdf.set_font('Arial', '', 12)
pdf.set_text_color(0, 0, 0)
summary_text = f"""
Document Type: {structure_analysis['document_type']}

Total Pages: {structure['total_pages']}
Total Words: {analysis['total_words']:,}
Unique Words: {analysis['unique_words']:,}
Total Sentences: {analysis['total_sentences']}

Vocabulary Richness: {analysis['vocabulary_richness']*100:.1f}%
Average Words per Page: {analysis['avg_words_per_page']:.1f}
Average Sentence Length: {analysis['avg_sentence_length']:.1f} words
"""
pdf.multi_cell(0, 8, summary_text.strip())

# Page 2: Document Overview
pdf.add_page()
pdf.chapter_title('1. Document Overview')
overview_text = f"""
This document is identified as a {structure_analysis['document_type']}.

Key Characteristics:
- Contains {structure['total_pages']} pages
- Total word count: {analysis['total_words']:,} words
- Vocabulary diversity: {analysis['unique_words']:,} unique words ({analysis['vocabulary_richness']*100:.1f}% richness)
- Structured into {structure_analysis['section_count']} distinct sections
- {'Includes' if structure_analysis['has_comprehension_questions'] else 'Does not include'} comprehension questions

Content Structure:
- Introduction: {'Yes' if structure_analysis['content_structure']['has_introduction'] else 'No'}
- Glossary: {'Yes' if structure_analysis['content_structure']['has_glossary'] else 'No'}
- Exercises: {'Yes' if structure_analysis['content_structure']['has_exercises'] else 'No'}
- References: {'Yes' if structure_analysis['content_structure']['has_references'] else 'No'}
"""
pdf.chapter_body(overview_text.strip())

# Themes
if structure_analysis['themes']:
    pdf.chapter_title('2. Identified Themes')
    themes_text = "The following themes were identified in the document:\n\n"
    for i, theme in enumerate(structure_analysis['themes'], 1):
        themes_text += f"{i}. {theme}\n"
    pdf.chapter_body(themes_text.strip())

# Authors
if structure_analysis['authors_mentioned']:
    pdf.chapter_title('3. Authors Mentioned')
    authors_text = "The following authors are mentioned in the document:\n\n"
    for author in structure_analysis['authors_mentioned']:
        authors_text += f"- {author}\n"
    pdf.chapter_body(authors_text.strip())

# Page 3: Statistics Overview Visualization
pdf.add_page()
pdf.chapter_title('4. Statistical Overview')
if os.path.exists('/vercel/sandbox/visualizations/statistics_overview.png'):
    pdf.image('/vercel/sandbox/visualizations/statistics_overview.png', x=10, y=None, w=190)

# Page 4: Word Distribution
pdf.add_page()
pdf.chapter_title('5. Word Distribution Across Pages')
pdf.chapter_body(f"The document shows varying word density across its {structure['total_pages']} pages, with an average of {analysis['avg_words_per_page']:.1f} words per page.")
if os.path.exists('/vercel/sandbox/visualizations/page_word_distribution.png'):
    pdf.image('/vercel/sandbox/visualizations/page_word_distribution.png', x=10, y=None, w=190)

# Page 5: Top Words
pdf.add_page()
pdf.chapter_title('6. Most Frequent Words')
pdf.chapter_body("The following chart shows the 20 most frequently occurring words in the document, providing insight into the document's focus and subject matter.")
if os.path.exists('/vercel/sandbox/visualizations/top_words.png'):
    pdf.image('/vercel/sandbox/visualizations/top_words.png', x=10, y=None, w=190)

# Page 6: Character Mentions
pdf.add_page()
pdf.chapter_title('7. Entity and Character Mentions')
if structure_analysis['potential_characters']:
    char_text = "The following entities, names, or characters appear frequently throughout the document:\n\n"
    for char, count in list(structure_analysis['potential_characters'].items())[:10]:
        char_text += f"- {char}: {count} mentions\n"
    pdf.chapter_body(char_text.strip())
    if os.path.exists('/vercel/sandbox/visualizations/character_mentions.png'):
        pdf.image('/vercel/sandbox/visualizations/character_mentions.png', x=10, y=None, w=190)

# Page 7: Section Distribution
pdf.add_page()
pdf.chapter_title('8. Document Structure')
section_text = f"The document is organized into {structure_analysis['section_count']} sections of various types:\n\n"
section_types = {}
for section in structure_analysis['sections']:
    stype = section['type']
    section_types[stype] = section_types.get(stype, 0) + 1

for stype, count in section_types.items():
    section_text += f"- {stype.replace('_', ' ').title()}: {count}\n"

pdf.chapter_body(section_text.strip())
if os.path.exists('/vercel/sandbox/visualizations/section_distribution.png'):
    pdf.image('/vercel/sandbox/visualizations/section_distribution.png', x=10, y=None, w=190)

# Page 8: Detailed Findings
pdf.add_page()
pdf.chapter_title('9. Detailed Findings')

findings_text = f"""
Linguistic Analysis:
- The document contains {analysis['total_sentences']} sentences
- Average sentence length: {analysis['avg_sentence_length']:.1f} words
- Paragraph count: {analysis['paragraph_count']}
- Average paragraph length: {analysis['avg_paragraph_length']:.1f} words

Reading Level:
- Vocabulary richness of {analysis['vocabulary_richness']*100:.1f}% suggests {'a diverse and sophisticated' if analysis['vocabulary_richness'] > 0.25 else 'a moderate'} vocabulary
- Average sentence length of {analysis['avg_sentence_length']:.1f} words indicates {'complex' if analysis['avg_sentence_length'] > 20 else 'moderate' if analysis['avg_sentence_length'] > 15 else 'simple'} sentence structures

Content Type:
- Identified as: {structure_analysis['document_type']}
- Contains {'educational/instructional' if structure_analysis['has_comprehension_questions'] else 'narrative'} elements
- {'Includes' if structure_analysis['content_structure']['has_introduction'] else 'Lacks'} formal introduction
"""
pdf.chapter_body(findings_text.strip())

# Save PDF
output_path = '/vercel/sandbox/document_analysis_report.pdf'
pdf.output(output_path)
print(f"PDF report created successfully: {output_path}")
