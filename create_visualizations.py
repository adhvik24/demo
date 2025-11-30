import json
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Load all analysis data
with open('/vercel/sandbox/pdf_structure.json', 'r', encoding='utf-8') as f:
    structure = json.load(f)

with open('/vercel/sandbox/pdf_analysis.json', 'r', encoding='utf-8') as f:
    analysis = json.load(f)

with open('/vercel/sandbox/pdf_structure_analysis.json', 'r', encoding='utf-8') as f:
    structure_analysis = json.load(f)

print("Creating visualizations...")

# Create output directory for images
os.makedirs('/vercel/sandbox/visualizations', exist_ok=True)

# 1. Page Word Distribution
plt.figure(figsize=(14, 6))
pages = list(range(1, len(analysis['page_word_distribution']) + 1))
plt.bar(pages, analysis['page_word_distribution'], color='steelblue', alpha=0.7, edgecolor='black')
plt.xlabel('Page Number', fontsize=12, fontweight='bold')
plt.ylabel('Word Count', fontsize=12, fontweight='bold')
plt.title('Word Distribution Across Pages', fontsize=14, fontweight='bold', pad=20)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(analysis['page_word_distribution']):
    plt.text(i + 1, v + 5, str(v), ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('/vercel/sandbox/visualizations/page_word_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Top 20 Most Common Words
plt.figure(figsize=(14, 8))
words = [w[0] for w in analysis['most_common_words'][:20]]
counts = [w[1] for w in analysis['most_common_words'][:20]]
colors = sns.color_palette('viridis', len(words))
bars = plt.barh(words[::-1], counts[::-1], color=colors[::-1], edgecolor='black', linewidth=0.5)
plt.xlabel('Frequency', fontsize=12, fontweight='bold')
plt.ylabel('Words', fontsize=12, fontweight='bold')
plt.title('Top 20 Most Frequent Words', fontsize=14, fontweight='bold', pad=20)
plt.grid(axis='x', alpha=0.3)
for i, (bar, count) in enumerate(zip(bars, counts[::-1])):
    plt.text(count + 2, bar.get_y() + bar.get_height()/2, str(count), 
             va='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('/vercel/sandbox/visualizations/top_words.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Document Statistics Overview
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Document Statistics Overview', fontsize=16, fontweight='bold', y=0.995)

# Total pages and word count
stats_labels = ['Total Pages', 'Total Words', 'Unique Words', 'Sentences']
stats_values = [
    structure['total_pages'],
    analysis['total_words'],
    analysis['unique_words'],
    analysis['total_sentences']
]
colors_stats = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
axes[0, 0].bar(stats_labels, stats_values, color=colors_stats, edgecolor='black', linewidth=1.5)
axes[0, 0].set_title('Basic Statistics', fontweight='bold', fontsize=12)
axes[0, 0].set_ylabel('Count', fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)
for i, v in enumerate(stats_values):
    axes[0, 0].text(i, v + max(stats_values)*0.02, str(v), ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)

# Vocabulary richness
vocab_rich = analysis['vocabulary_richness'] * 100
axes[0, 1].pie([vocab_rich, 100-vocab_rich], labels=['Unique', 'Repeated'], 
               autopct='%1.1f%%', startangle=90, colors=['#95E1D3', '#F38181'],
               explode=(0.05, 0), shadow=True, textprops={'fontsize': 11, 'fontweight': 'bold'})
axes[0, 1].set_title(f'Vocabulary Richness\n({analysis["unique_words"]} unique / {analysis["total_words"]} total)', 
                     fontweight='bold', fontsize=12)

# Average metrics
avg_labels = ['Avg Words\nper Page', 'Avg Sentence\nLength', 'Avg Paragraph\nLength']
avg_values = [
    analysis['avg_words_per_page'],
    analysis['avg_sentence_length'],
    analysis['avg_paragraph_length']
]
colors_avg = ['#A8E6CF', '#FFD3B6', '#FFAAA5']
bars = axes[1, 0].bar(avg_labels, avg_values, color=colors_avg, edgecolor='black', linewidth=1.5)
axes[1, 0].set_title('Average Metrics', fontweight='bold', fontsize=12)
axes[1, 0].set_ylabel('Word Count', fontweight='bold')
axes[1, 0].grid(axis='y', alpha=0.3)
for i, v in enumerate(avg_values):
    axes[1, 0].text(i, v + max(avg_values)*0.02, f'{v:.1f}', ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)

# Content features
features = ['Introduction', 'Comprehension\nQuestions', 'Sections', 'Themes']
feature_values = [
    1 if structure_analysis['content_structure']['has_introduction'] else 0,
    1 if structure_analysis['has_comprehension_questions'] else 0,
    1 if structure_analysis['section_count'] > 0 else 0,
    1 if len(structure_analysis['themes']) > 0 else 0
]
colors_features = ['#90EE90' if v == 1 else '#FFB6C1' for v in feature_values]
axes[1, 1].bar(features, feature_values, color=colors_features, edgecolor='black', linewidth=1.5)
axes[1, 1].set_title('Content Features Present', fontweight='bold', fontsize=12)
axes[1, 1].set_ylabel('Present (1) / Absent (0)', fontweight='bold')
axes[1, 1].set_ylim(0, 1.2)
axes[1, 1].grid(axis='y', alpha=0.3)
for i, v in enumerate(feature_values):
    label = 'Yes' if v == 1 else 'No'
    axes[1, 1].text(i, v + 0.05, label, ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('/vercel/sandbox/visualizations/statistics_overview.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Character/Entity Mentions
if structure_analysis['potential_characters']:
    plt.figure(figsize=(12, 7))
    chars = list(structure_analysis['potential_characters'].keys())[:10]
    char_counts = list(structure_analysis['potential_characters'].values())[:10]
    colors_chars = sns.color_palette('rocket', len(chars))
    plt.bar(chars, char_counts, color=colors_chars, edgecolor='black', linewidth=1.5)
    plt.xlabel('Entity/Character Name', fontsize=12, fontweight='bold')
    plt.ylabel('Mention Count', fontsize=12, fontweight='bold')
    plt.title('Top Mentioned Entities/Characters', fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    for i, v in enumerate(char_counts):
        plt.text(i, v + 0.3, str(v), ha='center', va='bottom', fontweight='bold', fontsize=10)
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/visualizations/character_mentions.png', dpi=300, bbox_inches='tight')
    plt.close()

# 5. Section Distribution
plt.figure(figsize=(10, 6))
section_types = {}
for section in structure_analysis['sections']:
    stype = section['type']
    section_types[stype] = section_types.get(stype, 0) + 1

if section_types:
    labels = list(section_types.keys())
    sizes = list(section_types.values())
    colors_sections = sns.color_palette('Set2', len(labels))
    explode = [0.05] * len(labels)
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
            colors=colors_sections, explode=explode, shadow=True,
            textprops={'fontsize': 11, 'fontweight': 'bold'})
    plt.title('Document Section Types Distribution', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('/vercel/sandbox/visualizations/section_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

print("Visualizations created successfully!")
print(f"Total visualizations: 5")
