#!/usr/bin/env python3
"""
Phase 2: Deep Content Analysis
Analyze word frequency, patterns, and content themes
"""

import json
import re
from collections import Counter

def analyze_content_deeply(data_file):
    """Phase 2: Deep analysis of content patterns"""
    
    print("=" * 80)
    print("PHASE 2: DEEP CONTENT ANALYSIS")
    print("=" * 80)
    
    # Load data from Phase 1
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    text = data['text_content']
    words = data['words']
    sentences = data['sentences']
    
    # Word frequency analysis
    print(f"\n📊 Word Frequency Analysis:")
    
    # Clean words (remove single characters and non-alphabetic)
    clean_words = [w.lower() for w in words if len(w) > 2 and w.isalpha()]
    word_freq = Counter(clean_words)
    
    print(f"   - Analyzed {len(clean_words):,} meaningful words")
    print(f"\n   Top 20 Most Frequent Words:")
    for i, (word, count) in enumerate(word_freq.most_common(20), 1):
        print(f"      {i:2d}. '{word}' - {count:,} times ({count/len(clean_words)*100:.2f}%)")
    
    # Word length distribution
    print(f"\n📏 Word Length Distribution:")
    length_dist = Counter(len(w) for w in clean_words)
    for length in sorted(length_dist.keys())[:15]:
        count = length_dist[length]
        bar = '█' * int(count / max(length_dist.values()) * 50)
        print(f"   {length:2d} chars: {count:5,} words {bar}")
    
    # Sentence length distribution
    print(f"\n📖 Sentence Length Distribution:")
    sent_lengths = [len(s.split()) for s in sentences if s]
    sent_length_dist = Counter(sent_lengths)
    
    # Group into ranges
    ranges = [(0, 5), (6, 10), (11, 20), (21, 30), (31, 50), (51, 100), (100, 500)]
    print(f"   Sentence length ranges:")
    for start, end in ranges:
        count = sum(c for l, c in sent_length_dist.items() if start <= l <= end)
        if count > 0:
            bar = '█' * int(count / len(sentences) * 50)
            print(f"   {start:3d}-{end:3d} words: {count:4,} sentences {bar}")
    
    # Pattern detection
    print(f"\n🔍 Pattern Detection:")
    
    # Find repeated phrases (2-3 word combinations)
    bigrams = []
    trigrams = []
    for i in range(len(clean_words) - 2):
        bigrams.append(f"{clean_words[i]} {clean_words[i+1]}")
        trigrams.append(f"{clean_words[i]} {clean_words[i+1]} {clean_words[i+2]}")
    
    bigram_freq = Counter(bigrams)
    trigram_freq = Counter(trigrams)
    
    print(f"\n   Top 10 Two-Word Phrases:")
    for i, (phrase, count) in enumerate(bigram_freq.most_common(10), 1):
        if count > 2:  # Only show if appears more than twice
            print(f"      {i:2d}. '{phrase}' - {count} times")
    
    print(f"\n   Top 10 Three-Word Phrases:")
    for i, (phrase, count) in enumerate(trigram_freq.most_common(10), 1):
        if count > 2:
            print(f"      {i:2d}. '{phrase}' - {count} times")
    
    # Numeric patterns
    numbers = re.findall(r'\b\d+\b', text)
    if numbers:
        print(f"\n🔢 Numeric Content:")
        print(f"   - Found {len(numbers):,} numbers in document")
        number_values = [int(n) for n in numbers if n.isdigit()]
        if number_values:
            print(f"   - Range: {min(number_values)} to {max(number_values)}")
            print(f"   - Most common numbers: {', '.join(str(n) for n, _ in Counter(number_values).most_common(10))}")
    
    # Special characters and formatting
    print(f"\n✨ Special Characters:")
    special_chars = [c for c in text if not c.isalnum() and not c.isspace()]
    special_freq = Counter(special_chars)
    print(f"   Top special characters:")
    for char, count in special_freq.most_common(10):
        print(f"      '{char}' - {count:,} times")
    
    # Save enhanced data
    data['deep_analysis'] = {
        'word_frequency': dict(word_freq.most_common(100)),
        'word_length_distribution': dict(length_dist),
        'sentence_length_distribution': dict(sent_length_dist),
        'top_bigrams': dict(bigram_freq.most_common(50)),
        'top_trigrams': dict(trigram_freq.most_common(50)),
        'special_characters': dict(special_freq),
        'numbers_found': numbers[:100] if numbers else []
    }
    
    with open('/vercel/sandbox/document_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Phase 2 complete! Enhanced data saved to document_data.json")
    
    return data

if __name__ == "__main__":
    analyze_content_deeply('/vercel/sandbox/document_data.json')
