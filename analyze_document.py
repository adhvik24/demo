#!/usr/bin/env python3
"""
Phase 1: Document Structure Discovery
Extract and understand the document structure, content, and metadata
"""

import olefile
import os
import json
from collections import Counter
import re

def extract_text_from_ole(file_path):
    """Extract text from old-format DOC file using olefile"""
    try:
        ole = olefile.OleFileIO(file_path)
        
        # Try to find the WordDocument stream
        if ole.exists('WordDocument'):
            word_stream = ole.openstream('WordDocument')
            raw_data = word_stream.read()
            
            # Extract printable ASCII text (basic extraction)
            text = ''.join(chr(b) if 32 <= b < 127 else ' ' for b in raw_data)
            # Clean up multiple spaces
            text = re.sub(r'\s+', ' ', text)
            
            ole.close()
            return text
        else:
            ole.close()
            return None
    except Exception as e:
        print(f"Error extracting with olefile: {e}")
        return None

def analyze_document_structure(file_path):
    """Phase 1: Discover document structure and basic statistics"""
    
    print("=" * 80)
    print("PHASE 1: DOCUMENT STRUCTURE DISCOVERY")
    print("=" * 80)
    
    # File metadata
    file_size = os.path.getsize(file_path)
    print(f"\n📄 File Information:")
    print(f"   - File: {os.path.basename(file_path)}")
    print(f"   - Size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
    print(f"   - Format: Microsoft Word Document (Old Format - DOC)")
    
    # Extract text content
    print(f"\n🔍 Extracting text content...")
    text = extract_text_from_ole(file_path)
    
    if not text:
        print("   ❌ Could not extract text from document")
        return None
    
    # Basic text statistics
    print(f"\n📊 Basic Text Statistics:")
    
    # Clean text for analysis
    words = text.split()
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    
    # Character analysis
    total_chars = len(text)
    letters = sum(1 for c in text if c.isalpha())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    special = total_chars - letters - digits - spaces
    
    print(f"   - Total characters: {total_chars:,}")
    print(f"   - Letters: {letters:,} ({letters/total_chars*100:.1f}%)")
    print(f"   - Digits: {digits:,} ({digits/total_chars*100:.1f}%)")
    print(f"   - Spaces: {spaces:,} ({spaces/total_chars*100:.1f}%)")
    print(f"   - Special characters: {special:,} ({special/total_chars*100:.1f}%)")
    
    # Word analysis
    print(f"\n📝 Word Analysis:")
    print(f"   - Total words: {len(words):,}")
    print(f"   - Unique words: {len(set(words)):,}")
    print(f"   - Average word length: {sum(len(w) for w in words)/len(words):.2f} characters")
    
    # Sentence analysis
    print(f"\n📖 Sentence Analysis:")
    print(f"   - Total sentences: {len(sentences):,}")
    if sentences:
        print(f"   - Average sentence length: {len(words)/len(sentences):.2f} words")
        print(f"   - Shortest sentence: {min(len(s.split()) for s in sentences)} words")
        print(f"   - Longest sentence: {max(len(s.split()) for s in sentences)} words")
    
    # Save extracted text and basic stats
    data = {
        'file_info': {
            'name': os.path.basename(file_path),
            'size_bytes': file_size,
            'format': 'DOC (Old Microsoft Word Format)'
        },
        'text_content': text,
        'statistics': {
            'total_characters': total_chars,
            'letters': letters,
            'digits': digits,
            'spaces': spaces,
            'special_chars': special,
            'total_words': len(words),
            'unique_words': len(set(words)),
            'total_sentences': len(sentences)
        },
        'words': words,
        'sentences': sentences
    }
    
    # Save to JSON
    with open('/vercel/sandbox/document_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Phase 1 complete! Data saved to document_data.json")
    print(f"   - Extracted {len(words):,} words")
    print(f"   - Identified {len(sentences):,} sentences")
    
    return data

if __name__ == "__main__":
    file_path = "/vercel/sandbox/uploads/file-sample_100kB.docx"
    analyze_document_structure(file_path)
