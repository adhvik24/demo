#!/usr/bin/env python3
"""
Phase 3: Structure Detection and Content Classification
Identify document type, structure, and content themes
"""

import json
import re
from collections import Counter

def detect_structure_and_themes(data_file):
    """Phase 3: Detect document structure and classify content"""
    
    print("=" * 80)
    print("PHASE 3: STRUCTURE DETECTION & CONTENT CLASSIFICATION")
    print("=" * 80)
    
    # Load data
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    text = data['text_content']
    
    # Content type detection
    print(f"\n🔍 Document Type Detection:")
    
    # Look for technical indicators
    technical_terms = {
        'color_profile': ['srgb', 'rgb', 'xyz', 'iec', 'colour', 'color', 'profile'],
        'metadata': ['desc', 'view', 'meas', 'default'],
        'encoding': ['jfif', 'utf', 'ascii'],
        'technical': ['condition', 'viewing', 'space']
    }
    
    detected_categories = {}
    for category, terms in technical_terms.items():
        count = sum(text.lower().count(term) for term in terms)
        if count > 0:
            detected_categories[category] = count
    
    print(f"\n   Detected content categories:")
    for category, count in sorted(detected_categories.items(), key=lambda x: x[1], reverse=True):
        print(f"      - {category.replace('_', ' ').title()}: {count} occurrences")
    
    # Analyze text segments
    print(f"\n📄 Content Structure:")
    
    # Split into chunks and analyze
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    print(f"   - Document divided into {len(chunks)} segments (~1000 chars each)")
    
    # Identify readable vs binary-like content
    readable_ratio = []
    for chunk in chunks:
        words = chunk.split()
        readable = sum(1 for w in words if len(w) > 2 and w.isalpha())
        readable_ratio.append(readable / len(words) if words else 0)
    
    avg_readable = sum(readable_ratio) / len(readable_ratio) if readable_ratio else 0
    print(f"   - Average readability: {avg_readable*100:.1f}% (words vs. data)")
    
    # Identify sections with high readability
    readable_sections = sum(1 for r in readable_ratio if r > 0.3)
    data_sections = sum(1 for r in readable_ratio if r <= 0.3)
    
    print(f"   - Readable sections: {readable_sections} ({readable_sections/len(chunks)*100:.1f}%)")
    print(f"   - Data/Binary sections: {data_sections} ({data_sections/len(chunks)*100:.1f}%)")
    
    # Extract potential meaningful text
    print(f"\n📝 Extracting Meaningful Content:")
    
    # Find sequences of readable words
    words = text.split()
    meaningful_sequences = []
    current_sequence = []
    
    for word in words:
        if len(word) > 2 and word.isalpha():
            current_sequence.append(word)
        else:
            if len(current_sequence) >= 3:  # At least 3 consecutive words
                meaningful_sequences.append(' '.join(current_sequence))
            current_sequence = []
    
    if current_sequence and len(current_sequence) >= 3:
        meaningful_sequences.append(' '.join(current_sequence))
    
    print(f"   - Found {len(meaningful_sequences)} meaningful text sequences")
    
    if meaningful_sequences:
        print(f"\n   Sample meaningful sequences:")
        for i, seq in enumerate(meaningful_sequences[:10], 1):
            if len(seq) > 20:
                print(f"      {i}. {seq[:80]}...")
            else:
                print(f"      {i}. {seq}")
    
    # Character encoding analysis
    print(f"\n🔤 Character Encoding Analysis:")
    
    # Count different character types
    ascii_printable = sum(1 for c in text if 32 <= ord(c) < 127)
    extended_ascii = sum(1 for c in text if 127 <= ord(c) < 256)
    unicode_chars = sum(1 for c in text if ord(c) >= 256)
    
    print(f"   - ASCII printable: {ascii_printable:,} ({ascii_printable/len(text)*100:.1f}%)")
    print(f"   - Extended ASCII: {extended_ascii:,} ({extended_ascii/len(text)*100:.1f}%)")
    print(f"   - Unicode: {unicode_chars:,} ({unicode_chars/len(text)*100:.1f}%)")
    
    # Document classification
    print(f"\n🏷️  Document Classification:")
    
    classification = {
        'primary_type': 'Technical Document',
        'content_type': 'Mixed (Text + Embedded Data)',
        'likely_contains': []
    }
    
    if 'color_profile' in detected_categories:
        classification['likely_contains'].append('Color Profile Information')
    if data_sections > readable_sections:
        classification['likely_contains'].append('Embedded Binary/Metadata')
    if len(meaningful_sequences) > 0:
        classification['likely_contains'].append('Readable Text Content')
    
    print(f"   - Primary Type: {classification['primary_type']}")
    print(f"   - Content Type: {classification['content_type']}")
    print(f"   - Likely Contains:")
    for item in classification['likely_contains']:
        print(f"      • {item}")
    
    # Save structure analysis
    data['structure_analysis'] = {
        'detected_categories': detected_categories,
        'total_segments': len(chunks),
        'readable_sections': readable_sections,
        'data_sections': data_sections,
        'meaningful_sequences': meaningful_sequences[:50],  # Save top 50
        'classification': classification,
        'readability_score': avg_readable
    }
    
    with open('/vercel/sandbox/document_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Phase 3 complete! Structure analysis saved to document_data.json")
    
    return data

if __name__ == "__main__":
    detect_structure_and_themes('/vercel/sandbox/document_data.json')
