import json
import re
from collections import Counter
import pdfplumber

# Phase 2: Deep content analysis
print("Phase 2: Deep content analysis...")

# Load structure data
with open('/vercel/sandbox/pdf_structure.json', 'r', encoding='utf-8') as f:
    structure = json.load(f)

# Extract full text
full_text = ""
for page in structure['pages']:
    full_text += page['text'] + "\n"

# Text analysis
words = re.findall(r'\b[a-zA-Z]+\b', full_text.lower())
word_freq = Counter(words)
most_common_words = word_freq.most_common(50)

# Find sentences
sentences = re.split(r'[.!?]+', full_text)
sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

# Identify sections/headings (typically in uppercase or title case)
headings = re.findall(r'^[A-Z][A-Z\s]+$', full_text, re.MULTILINE)
headings = [h.strip() for h in headings if len(h.strip()) > 3]

# Look for story titles or chapter markers
story_markers = re.findall(r'^\d+/[IVX]+\s+(.+)$', full_text, re.MULTILINE)

# Identify questions (for comprehension sections)
questions = re.findall(r'^.*\?$', full_text, re.MULTILINE)

# Count paragraphs
paragraphs = [p.strip() for p in full_text.split('\n\n') if len(p.strip()) > 20]

# Analyze page distribution
page_word_counts = [len(page['text'].split()) for page in structure['pages']]

analysis_data = {
    'total_words': len(words),
    'unique_words': len(set(words)),
    'vocabulary_richness': len(set(words)) / len(words) if words else 0,
    'most_common_words': most_common_words[:30],
    'total_sentences': len(sentences),
    'avg_sentence_length': sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0,
    'headings': headings,
    'story_markers': story_markers,
    'questions_found': len(questions),
    'sample_questions': questions[:10],
    'paragraph_count': len(paragraphs),
    'avg_paragraph_length': sum(len(p.split()) for p in paragraphs) / len(paragraphs) if paragraphs else 0,
    'page_word_distribution': page_word_counts,
    'avg_words_per_page': sum(page_word_counts) / len(page_word_counts) if page_word_counts else 0
}

with open('/vercel/sandbox/pdf_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(analysis_data, f, indent=2, ensure_ascii=False)

print(f"Total words: {analysis_data['total_words']}")
print(f"Unique words: {analysis_data['unique_words']}")
print(f"Vocabulary richness: {analysis_data['vocabulary_richness']:.2%}")
print(f"Total sentences: {analysis_data['total_sentences']}")
print(f"Headings found: {len(headings)}")
print(f"Story markers: {story_markers}")
print(f"Questions found: {len(questions)}")
print(f"Paragraphs: {len(paragraphs)}")
print("\nTop 10 most common words:")
for word, count in most_common_words[:10]:
    print(f"  {word}: {count}")
