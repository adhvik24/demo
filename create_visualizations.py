#!/usr/bin/env python3
"""
Phase 4: Create Comprehensive Visualizations and PDF Report
Generate beautiful charts and compile into a visual PDF report
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np
from fpdf import FPDF
import os

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = '#f8f9fa'

def create_visualizations(data_file):
    """Create comprehensive visualizations"""
    
    print("=" * 80)
    print("PHASE 4: CREATING VISUALIZATIONS")
    print("=" * 80)
    
    # Load data
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    os.makedirs('/vercel/sandbox/charts', exist_ok=True)
    
    # 1. Document Overview Dashboard
    print("\n📊 Creating Document Overview Dashboard...")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Document Analysis Overview', fontsize=20, fontweight='bold', y=0.995)
    
    # Character composition pie chart
    ax = axes[0, 0]
    stats = data['statistics']
    sizes = [stats['letters'], stats['digits'], stats['spaces'], stats['special_chars']]
    labels = ['Letters', 'Digits', 'Spaces', 'Special Chars']
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    explode = (0.05, 0.05, 0.05, 0.05)
    
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
    ax.set_title('Character Composition', fontsize=14, fontweight='bold', pad=20)
    
    # Word statistics bar chart
    ax = axes[0, 1]
    word_stats = {
        'Total Words': stats['total_words'],
        'Unique Words': stats['unique_words'],
        'Sentences': stats['total_sentences']
    }
    bars = ax.bar(word_stats.keys(), word_stats.values(), color=['#3498db', '#9b59b6', '#1abc9c'])
    ax.set_title('Content Statistics', fontsize=14, fontweight='bold', pad=20)
    ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Word length distribution
    ax = axes[1, 0]
    word_lengths = data['deep_analysis']['word_length_distribution']
    lengths = sorted([int(k) for k in word_lengths.keys()])[:15]
    counts = [word_lengths[str(l)] for l in lengths]
    
    ax.bar(lengths, counts, color='#3498db', alpha=0.7, edgecolor='black')
    ax.set_title('Word Length Distribution', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Word Length (characters)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Sentence length distribution
    ax = axes[1, 1]
    sent_lengths = data['deep_analysis']['sentence_length_distribution']
    
    # Group into ranges
    ranges = [(0, 5), (6, 10), (11, 20), (21, 30), (31, 50), (51, 100), (100, 500)]
    range_labels = [f'{s}-{e}' for s, e in ranges]
    range_counts = []
    
    for start, end in ranges:
        count = sum(int(c) for l, c in sent_lengths.items() if start <= int(l) <= end)
        range_counts.append(count)
    
    bars = ax.barh(range_labels, range_counts, color='#2ecc71', alpha=0.7, edgecolor='black')
    ax.set_title('Sentence Length Distribution', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Number of Sentences', fontsize=12, fontweight='bold')
    ax.set_ylabel('Words per Sentence', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        if width > 0:
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                    f' {int(width)}',
                    ha='left', va='center', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/charts/01_overview_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Overview dashboard saved")
    
    # 2. Word Frequency Chart
    print("\n📊 Creating Word Frequency Chart...")
    fig, ax = plt.subplots(figsize=(14, 8))
    
    word_freq = data['deep_analysis']['word_frequency']
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:20]
    words, counts = zip(*top_words)
    
    bars = ax.barh(range(len(words)), counts, color=plt.cm.viridis(np.linspace(0.3, 0.9, len(words))))
    ax.set_yticks(range(len(words)))
    ax.set_yticklabels(words, fontsize=11, fontweight='bold')
    ax.set_xlabel('Frequency', fontsize=13, fontweight='bold')
    ax.set_title('Top 20 Most Frequent Words', fontsize=16, fontweight='bold', pad=20)
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f' {int(width)}',
                ha='left', va='center', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/charts/02_word_frequency.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Word frequency chart saved")
    
    # 3. Word Cloud
    print("\n☁️  Creating Word Cloud...")
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Create word cloud from frequency data
    wordcloud = WordCloud(width=1600, height=1000, 
                         background_color='white',
                         colormap='viridis',
                         relative_scaling=0.5,
                         min_font_size=10).generate_from_frequencies(word_freq)
    
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Word Cloud - Most Frequent Terms', fontsize=18, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/charts/03_word_cloud.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Word cloud saved")
    
    # 4. Special Characters Analysis
    print("\n📊 Creating Special Characters Chart...")
    fig, ax = plt.subplots(figsize=(14, 8))
    
    special_chars = data['deep_analysis']['special_characters']
    top_special = sorted(special_chars.items(), key=lambda x: x[1], reverse=True)[:15]
    chars, counts = zip(*top_special)
    
    # Escape special characters for display
    display_chars = [f"'{c}'" for c in chars]
    
    bars = ax.bar(range(len(chars)), counts, color='#e74c3c', alpha=0.7, edgecolor='black')
    ax.set_xticks(range(len(chars)))
    ax.set_xticklabels(display_chars, fontsize=11, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=13, fontweight='bold')
    ax.set_title('Top 15 Special Characters', fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/charts/04_special_characters.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Special characters chart saved")
    
    # 5. Document Structure Visualization
    print("\n📊 Creating Document Structure Chart...")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Content type distribution
    ax = axes[0]
    structure = data['structure_analysis']
    categories = structure['detected_categories']
    
    if categories:
        cat_names = [k.replace('_', ' ').title() for k in categories.keys()]
        cat_counts = list(categories.values())
        
        bars = ax.barh(cat_names, cat_counts, color=['#3498db', '#9b59b6', '#e74c3c', '#f39c12'][:len(cat_names)])
        ax.set_xlabel('Occurrences', fontsize=12, fontweight='bold')
        ax.set_title('Content Categories Detected', fontsize=14, fontweight='bold', pad=20)
        ax.grid(axis='x', alpha=0.3)
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                    f' {int(width)}',
                    ha='left', va='center', fontweight='bold', fontsize=11)
    
    # Readability analysis
    ax = axes[1]
    readable = structure['readable_sections']
    data_sections = structure['data_sections']
    
    sizes = [readable, data_sections]
    labels = ['Readable\nSections', 'Data/Binary\nSections']
    colors = ['#2ecc71', '#e74c3c']
    explode = (0.1, 0)
    
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax.set_title('Document Composition', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/charts/05_document_structure.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Document structure chart saved")
    
    # 6. Phrase Analysis
    print("\n📊 Creating Phrase Analysis Chart...")
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    
    # Top bigrams
    ax = axes[0]
    bigrams = data['deep_analysis']['top_bigrams']
    top_bigrams = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)[:10]
    
    if top_bigrams:
        phrases, counts = zip(*top_bigrams)
        bars = ax.barh(range(len(phrases)), counts, color='#3498db', alpha=0.7, edgecolor='black')
        ax.set_yticks(range(len(phrases)))
        ax.set_yticklabels(phrases, fontsize=10, fontweight='bold')
        ax.set_xlabel('Frequency', fontsize=12, fontweight='bold')
        ax.set_title('Top 10 Two-Word Phrases', fontsize=14, fontweight='bold', pad=20)
        ax.invert_yaxis()
        ax.grid(axis='x', alpha=0.3)
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                    f' {int(width)}',
                    ha='left', va='center', fontweight='bold', fontsize=10)
    
    # Top trigrams
    ax = axes[1]
    trigrams = data['deep_analysis']['top_trigrams']
    top_trigrams = sorted(trigrams.items(), key=lambda x: x[1], reverse=True)[:10]
    
    if top_trigrams:
        phrases, counts = zip(*top_trigrams)
        bars = ax.barh(range(len(phrases)), counts, color='#2ecc71', alpha=0.7, edgecolor='black')
        ax.set_yticks(range(len(phrases)))
        ax.set_yticklabels(phrases, fontsize=10, fontweight='bold')
        ax.set_xlabel('Frequency', fontsize=12, fontweight='bold')
        ax.set_title('Top 10 Three-Word Phrases', fontsize=14, fontweight='bold', pad=20)
        ax.invert_yaxis()
        ax.grid(axis='x', alpha=0.3)
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                    f' {int(width)}',
                    ha='left', va='center', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/charts/06_phrase_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Phrase analysis chart saved")
    
    print("\n✅ All visualizations created successfully!")
    return data

def create_pdf_report(data):
    """Create comprehensive PDF report with visualizations"""
    
    print("\n" + "=" * 80)
    print("CREATING PDF REPORT")
    print("=" * 80)
    
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, 'Document Analysis Report', 0, 1, 'C')
            self.ln(5)
        
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
        def chapter_title(self, title):
            self.set_font('Arial', 'B', 14)
            self.set_fill_color(52, 152, 219)
            self.set_text_color(255, 255, 255)
            self.cell(0, 10, title, 0, 1, 'L', 1)
            self.ln(4)
            self.set_text_color(0, 0, 0)
        
        def chapter_body(self, body):
            self.set_font('Arial', '', 11)
            self.multi_cell(0, 6, body)
            self.ln()
    
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Page 1: Title and Summary
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.ln(20)
    pdf.cell(0, 15, 'Document Analysis Report', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"File: {data['file_info']['name']}", 0, 1, 'C')
    pdf.cell(0, 10, f"Size: {data['file_info']['size_bytes']:,} bytes", 0, 1, 'C')
    pdf.ln(20)
    
    # Executive Summary
    pdf.chapter_title('Executive Summary')
    summary = f"""This report presents a comprehensive analysis of the document '{data['file_info']['name']}'.

Key Findings:
- Total Characters: {data['statistics']['total_characters']:,}
- Total Words: {data['statistics']['total_words']:,}
- Unique Words: {data['statistics']['unique_words']:,}
- Total Sentences: {data['statistics']['total_sentences']:,}

Document Classification:
- Type: {data['structure_analysis']['classification']['primary_type']}
- Content: {data['structure_analysis']['classification']['content_type']}
- Readability Score: {data['structure_analysis']['readability_score']*100:.1f}%

The document appears to be a technical file containing color profile information (sRGB, XYZ, IEC) 
and embedded metadata. The content is primarily composed of data structures rather than readable text."""
    
    pdf.chapter_body(summary)
    
    # Page 2: Overview Dashboard
    pdf.add_page()
    pdf.chapter_title('1. Document Overview Dashboard')
    pdf.image('/vercel/sandbox/charts/01_overview_dashboard.png', x=10, w=190)
    
    # Page 3: Word Frequency
    pdf.add_page()
    pdf.chapter_title('2. Word Frequency Analysis')
    pdf.image('/vercel/sandbox/charts/02_word_frequency.png', x=10, w=190)
    
    # Page 4: Word Cloud
    pdf.add_page()
    pdf.chapter_title('3. Word Cloud Visualization')
    pdf.image('/vercel/sandbox/charts/03_word_cloud.png', x=10, w=190)
    
    # Page 5: Special Characters
    pdf.add_page()
    pdf.chapter_title('4. Special Characters Analysis')
    pdf.image('/vercel/sandbox/charts/04_special_characters.png', x=10, w=190)
    
    # Page 6: Document Structure
    pdf.add_page()
    pdf.chapter_title('5. Document Structure')
    pdf.image('/vercel/sandbox/charts/05_document_structure.png', x=10, w=190)
    
    # Page 7: Phrase Analysis
    pdf.add_page()
    pdf.chapter_title('6. Phrase Analysis')
    pdf.image('/vercel/sandbox/charts/06_phrase_analysis.png', x=10, w=190)
    
    # Save PDF
    pdf.output('/vercel/sandbox/document_analysis_report.pdf')
    print("\n✅ PDF report created: document_analysis_report.pdf")

if __name__ == "__main__":
    data = create_visualizations('/vercel/sandbox/document_data.json')
    create_pdf_report(data)
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE!")
    print("=" * 80)
    print("\n📁 Generated Files:")
    print("   • document_data.json - Complete analysis data")
    print("   • document_analysis_report.pdf - Visual PDF report")
    print("   • charts/ - Individual visualization images")
