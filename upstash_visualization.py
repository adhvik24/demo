#!/usr/bin/env python3
"""
Upstash MongoDB Data Visualization Script
Generates comprehensive visualizations and PDF report
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from datetime import datetime

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Data from MongoDB aggregations
genre_data = [
    {"genre": "Drama", "count": 12385, "avgRating": 6.80},
    {"genre": "Comedy", "count": 6532, "avgRating": 6.45},
    {"genre": "Romance", "count": 3318, "avgRating": 6.66},
    {"genre": "Crime", "count": 2457, "avgRating": 6.69},
    {"genre": "Thriller", "count": 2454, "avgRating": 6.30},
    {"genre": "Action", "count": 2381, "avgRating": 6.35},
    {"genre": "Adventure", "count": 1900, "avgRating": 6.49},
    {"genre": "Documentary", "count": 1834, "avgRating": 7.37},
    {"genre": "Horror", "count": 1470, "avgRating": 5.78},
    {"genre": "Biography", "count": 1269, "avgRating": 7.09},
    {"genre": "Family", "count": 1249, "avgRating": 6.33},
    {"genre": "Mystery", "count": 1139, "avgRating": 6.53},
    {"genre": "Fantasy", "count": 1055, "avgRating": 6.38},
    {"genre": "Sci-Fi", "count": 958, "avgRating": 6.12},
    {"genre": "Animation", "count": 912, "avgRating": 6.90}
]

country_data = [
    {"country": "USA", "count": 10921},
    {"country": "UK", "count": 2652},
    {"country": "France", "count": 2647},
    {"country": "Germany", "count": 1494},
    {"country": "Canada", "count": 1260},
    {"country": "Italy", "count": 1217},
    {"country": "Japan", "count": 786},
    {"country": "Spain", "count": 675},
    {"country": "India", "count": 564},
    {"country": "Australia", "count": 470}
]

director_data = [
    {"director": "Woody Allen", "count": 40, "avgRating": 7.22},
    {"director": "Martin Scorsese", "count": 32, "avgRating": 7.64},
    {"director": "Takashi Miike", "count": 31, "avgRating": 6.84},
    {"director": "Steven Spielberg", "count": 29, "avgRating": 7.48},
    {"director": "John Ford", "count": 29, "avgRating": 7.12},
    {"director": "Sidney Lumet", "count": 29, "avgRating": 6.93},
    {"director": "Clint Eastwood", "count": 27, "avgRating": 7.13},
    {"director": "Michael Apted", "count": 27, "avgRating": 7.02},
    {"director": "Robert Altman", "count": 27, "avgRating": 6.76},
    {"director": "Spike Lee", "count": 27, "avgRating": 6.74}
]

product_category_data = [
    {"category": "Home", "count": 184, "avgPrice": 103.77, "avgRating": 2.59, "stock": 16381},
    {"category": "Beauty", "count": 168, "avgPrice": 102.26, "avgRating": 2.54, "stock": 16710},
    {"category": "Clothing", "count": 165, "avgPrice": 99.74, "avgRating": 2.47, "stock": 15902},
    {"category": "Books", "count": 162, "avgPrice": 102.88, "avgRating": 2.61, "stock": 14852},
    {"category": "Electronics", "count": 161, "avgPrice": 103.51, "avgRating": 2.59, "stock": 16173},
    {"category": "Sports", "count": 160, "avgPrice": 104.87, "avgRating": 2.51, "stock": 15233}
]

price_bucket_data = [
    {"range": "$0-50", "count": 227, "avgRating": 2.44},
    {"range": "$50-100", "count": 254, "avgRating": 2.51},
    {"range": "$100-150", "count": 248, "avgRating": 2.49},
    {"range": "$150-200", "count": 271, "avgRating": 2.73}
]

def create_title_page(pdf):
    """Create title page for PDF report"""
    fig = plt.figure(figsize=(12, 8))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111)
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.7, 'Upstash MongoDB', 
            ha='center', va='center', fontsize=48, fontweight='bold',
            color='#2C3E50')
    ax.text(0.5, 0.6, 'Data Analysis & Visualization Report', 
            ha='center', va='center', fontsize=32,
            color='#34495E')
    
    # Stats box
    stats_text = f"""
    📊 Database Statistics
    
    • 21,349 Movies Analyzed
    • 41,079 User Comments
    • 1,000 Products Catalogued
    • 15 Genres Covered
    • 10 Countries Represented
    
    Generated: {datetime.now().strftime('%B %d, %Y')}
    """
    
    ax.text(0.5, 0.3, stats_text, 
            ha='center', va='center', fontsize=16,
            bbox=dict(boxstyle='round,pad=1', facecolor='#ECF0F1', edgecolor='#BDC3C7', linewidth=2),
            family='monospace')
    
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

def plot_genre_distribution(pdf):
    """Create genre distribution visualizations"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Movie Genre Analysis', fontsize=20, fontweight='bold', y=0.995)
    
    genres = [g['genre'] for g in genre_data]
    counts = [g['count'] for g in genre_data]
    ratings = [g['avgRating'] for g in genre_data]
    
    # 1. Bar chart - Genre counts
    ax1 = axes[0, 0]
    colors = sns.color_palette('viridis', len(genres))
    bars = ax1.barh(genres, counts, color=colors)
    ax1.set_xlabel('Number of Movies', fontsize=12, fontweight='bold')
    ax1.set_title('Movies by Genre', fontsize=14, fontweight='bold')
    ax1.invert_yaxis()
    
    # Add value labels
    for i, (bar, count) in enumerate(zip(bars, counts)):
        ax1.text(count + 200, i, f'{count:,}', va='center', fontsize=9)
    
    # 2. Horizontal bar - Average ratings
    ax2 = axes[0, 1]
    colors_rating = ['#27AE60' if r >= 7.0 else '#E67E22' if r >= 6.5 else '#E74C3C' for r in ratings]
    bars2 = ax2.barh(genres, ratings, color=colors_rating)
    ax2.set_xlabel('Average IMDB Rating', fontsize=12, fontweight='bold')
    ax2.set_title('Average Rating by Genre', fontsize=14, fontweight='bold')
    ax2.set_xlim(5, 8)
    ax2.invert_yaxis()
    ax2.axvline(x=6.66, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Overall Avg (6.66)')
    ax2.legend()
    
    # Add value labels
    for i, (bar, rating) in enumerate(zip(bars2, ratings)):
        ax2.text(rating + 0.05, i, f'{rating:.2f}', va='center', fontsize=9)
    
    # 3. Scatter plot - Count vs Rating
    ax3 = axes[1, 0]
    scatter = ax3.scatter(counts, ratings, s=[c/10 for c in counts], 
                         c=ratings, cmap='RdYlGn', alpha=0.6, edgecolors='black', linewidth=1.5)
    
    # Add genre labels
    for i, genre in enumerate(genres):
        ax3.annotate(genre, (counts[i], ratings[i]), 
                    fontsize=8, ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
    
    ax3.set_xlabel('Number of Movies', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Average Rating', fontsize=12, fontweight='bold')
    ax3.set_title('Genre Popularity vs Quality', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax3, label='Rating')
    
    # 4. Pie chart - Top 8 genres
    ax4 = axes[1, 1]
    top_8_genres = genres[:8]
    top_8_counts = counts[:8]
    other_count = sum(counts[8:])
    
    pie_labels = top_8_genres + ['Others']
    pie_values = top_8_counts + [other_count]
    
    colors_pie = sns.color_palette('Set3', len(pie_labels))
    wedges, texts, autotexts = ax4.pie(pie_values, labels=pie_labels, autopct='%1.1f%%',
                                        colors=colors_pie, startangle=90,
                                        textprops={'fontsize': 10})
    
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')
    
    ax4.set_title('Genre Distribution (Top 8 + Others)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight', dpi=300)
    plt.close()

def plot_country_analysis(pdf):
    """Create country distribution visualizations"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Movie Production by Country', fontsize=20, fontweight='bold')
    
    countries = [c['country'] for c in country_data]
    counts = [c['count'] for c in country_data]
    
    # 1. Bar chart
    ax1 = axes[0]
    colors = sns.color_palette('coolwarm', len(countries))
    bars = ax1.bar(countries, counts, color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Number of Movies', fontsize=12, fontweight='bold')
    ax1.set_title('Top 10 Movie-Producing Countries', fontsize=14, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 150,
                f'{count:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # 2. Treemap-style visualization using nested rectangles
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Proportional Country Representation', fontsize=14, fontweight='bold')
    
    total = sum(counts)
    percentages = [(c/total)*100 for c in counts]
    
    # Create rectangles
    y_pos = 9
    colors_map = sns.color_palette('Spectral', len(countries))
    
    for i, (country, pct, color) in enumerate(zip(countries, percentages, colors_map)):
        height = pct / 10
        rect = plt.Rectangle((0.5, y_pos - height), 9, height, 
                            facecolor=color, edgecolor='black', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, y_pos - height/2, f'{country}: {pct:.1f}%', 
                ha='center', va='center', fontsize=11, fontweight='bold',
                color='white' if pct > 5 else 'black')
        y_pos -= height
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight', dpi=300)
    plt.close()

def plot_director_analysis(pdf):
    """Create director analysis visualizations"""
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    fig.suptitle('Top Directors Analysis', fontsize=20, fontweight='bold')
    
    directors = [d['director'] for d in director_data]
    counts = [d['count'] for d in director_data]
    ratings = [d['avgRating'] for d in director_data]
    
    # 1. Grouped bar chart
    ax1 = axes[0]
    x = np.arange(len(directors))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, counts, width, label='Movie Count', 
                   color='#3498DB', edgecolor='black', linewidth=1.5)
    
    ax1_twin = ax1.twinx()
    bars2 = ax1_twin.bar(x + width/2, ratings, width, label='Avg Rating',
                        color='#E74C3C', edgecolor='black', linewidth=1.5)
    
    ax1.set_xlabel('Director', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Movies', fontsize=12, fontweight='bold', color='#3498DB')
    ax1_twin.set_ylabel('Average Rating', fontsize=12, fontweight='bold', color='#E74C3C')
    ax1.set_title('Director Productivity vs Quality', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(directors, rotation=45, ha='right')
    ax1.tick_params(axis='y', labelcolor='#3498DB')
    ax1_twin.tick_params(axis='y', labelcolor='#E74C3C')
    
    ax1.legend(loc='upper left')
    ax1_twin.legend(loc='upper right')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # 2. Bubble chart
    ax2 = axes[1]
    
    # Calculate bubble sizes (productivity * quality)
    bubble_sizes = [c * r * 20 for c, r in zip(counts, ratings)]
    
    scatter = ax2.scatter(counts, ratings, s=bubble_sizes, 
                         c=ratings, cmap='RdYlGn', alpha=0.6,
                         edgecolors='black', linewidth=2)
    
    # Add director labels
    for i, director in enumerate(directors):
        ax2.annotate(director, (counts[i], ratings[i]), 
                    fontsize=9, ha='center', va='center',
                    fontweight='bold', color='white',
                    bbox=dict(boxstyle='round,pad=0.4', facecolor='black', alpha=0.7))
    
    ax2.set_xlabel('Number of Movies', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Average Rating', fontsize=12, fontweight='bold')
    ax2.set_title('Director Impact Analysis (bubble size = productivity × quality)', 
                 fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(6.5, 7.8)
    
    plt.colorbar(scatter, ax=ax2, label='Rating')
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight', dpi=300)
    plt.close()

def plot_product_analysis(pdf):
    """Create product analysis visualizations"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('E-Commerce Product Analysis', fontsize=20, fontweight='bold', y=0.995)
    
    categories = [p['category'] for p in product_category_data]
    counts = [p['count'] for p in product_category_data]
    prices = [p['avgPrice'] for p in product_category_data]
    ratings = [p['avgRating'] for p in product_category_data]
    stocks = [p['stock'] for p in product_category_data]
    
    # 1. Category distribution
    ax1 = axes[0, 0]
    colors = sns.color_palette('pastel', len(categories))
    bars = ax1.bar(categories, counts, color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Number of Products', fontsize=12, fontweight='bold')
    ax1.set_title('Products by Category', fontsize=14, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{count}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # 2. Average price by category
    ax2 = axes[0, 1]
    colors_price = sns.color_palette('YlOrRd', len(categories))
    bars2 = ax2.barh(categories, prices, color=colors_price, edgecolor='black', linewidth=1.5)
    ax2.set_xlabel('Average Price ($)', fontsize=12, fontweight='bold')
    ax2.set_title('Average Price by Category', fontsize=14, fontweight='bold')
    ax2.invert_yaxis()
    
    for i, (bar, price) in enumerate(zip(bars2, prices)):
        ax2.text(price + 1, i, f'${price:.2f}', va='center', fontsize=10, fontweight='bold')
    
    # 3. Stock levels
    ax3 = axes[1, 0]
    colors_stock = sns.color_palette('Greens', len(categories))
    bars3 = ax3.bar(categories, stocks, color=colors_stock, edgecolor='black', linewidth=1.5)
    ax3.set_ylabel('Total Stock Units', fontsize=12, fontweight='bold')
    ax3.set_title('Inventory by Category', fontsize=14, fontweight='bold')
    ax3.tick_params(axis='x', rotation=45)
    
    for bar, stock in zip(bars3, stocks):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 200,
                f'{stock:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # 4. Multi-metric comparison
    ax4 = axes[1, 1]
    
    x = np.arange(len(categories))
    width = 0.25
    
    # Normalize values for comparison
    norm_counts = [c/max(counts)*100 for c in counts]
    norm_prices = [p/max(prices)*100 for p in prices]
    norm_ratings = [r/5*100 for r in ratings]
    
    bars1 = ax4.bar(x - width, norm_counts, width, label='Products (normalized)',
                   color='#3498DB', edgecolor='black', linewidth=1)
    bars2 = ax4.bar(x, norm_prices, width, label='Avg Price (normalized)',
                   color='#E74C3C', edgecolor='black', linewidth=1)
    bars3 = ax4.bar(x + width, norm_ratings, width, label='Avg Rating (normalized)',
                   color='#2ECC71', edgecolor='black', linewidth=1)
    
    ax4.set_ylabel('Normalized Value (%)', fontsize=12, fontweight='bold')
    ax4.set_title('Multi-Metric Category Comparison', fontsize=14, fontweight='bold')
    ax4.set_xticks(x)
    ax4.set_xticklabels(categories, rotation=45, ha='right')
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight', dpi=300)
    plt.close()

def plot_price_rating_analysis(pdf):
    """Create price vs rating analysis"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Price vs Rating Analysis', fontsize=20, fontweight='bold')
    
    price_ranges = [p['range'] for p in price_bucket_data]
    counts = [p['count'] for p in price_bucket_data]
    ratings = [p['avgRating'] for p in price_bucket_data]
    
    # 1. Stacked visualization
    ax1 = axes[0]
    colors = sns.color_palette('Blues', len(price_ranges))
    bars = ax1.bar(price_ranges, counts, color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Number of Products', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Price Range', fontsize=12, fontweight='bold')
    ax1.set_title('Product Distribution by Price Range', fontsize=14, fontweight='bold')
    
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 3,
                f'{count}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # 2. Line plot - Rating trend
    ax2 = axes[1]
    line = ax2.plot(price_ranges, ratings, marker='o', linewidth=3, 
                   markersize=12, color='#E74C3C', markerfacecolor='#E74C3C',
                   markeredgecolor='black', markeredgewidth=2)
    
    ax2.set_ylabel('Average Rating', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Price Range', fontsize=12, fontweight='bold')
    ax2.set_title('Rating Trend Across Price Ranges', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(2.3, 2.8)
    
    # Add value labels
    for i, (pr, rating) in enumerate(zip(price_ranges, ratings)):
        ax2.text(i, rating + 0.02, f'{rating:.2f}', ha='center', va='bottom',
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                         edgecolor='black', linewidth=1.5))
    
    # Add trend annotation
    ax2.annotate('Higher prices correlate\nwith better ratings', 
                xy=(3, ratings[3]), xytext=(2, 2.45),
                arrowprops=dict(arrowstyle='->', lw=2, color='green'),
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7))
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight', dpi=300)
    plt.close()

def plot_summary_dashboard(pdf):
    """Create comprehensive summary dashboard"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
    fig.suptitle('Executive Dashboard - Key Metrics', fontsize=22, fontweight='bold')
    
    # Key metrics boxes
    metrics = [
        {'title': 'Total Movies', 'value': '21,349', 'color': '#3498DB'},
        {'title': 'Avg Movie Rating', 'value': '6.66/10', 'color': '#E74C3C'},
        {'title': 'Total Comments', 'value': '41,079', 'color': '#9B59B6'},
        {'title': 'Total Products', 'value': '1,000', 'color': '#2ECC71'},
        {'title': 'Avg Product Price', 'value': '$102.84', 'color': '#F39C12'},
        {'title': 'Total Inventory', 'value': '95,251', 'color': '#1ABC9C'},
    ]
    
    for i, metric in enumerate(metrics):
        row = i // 3
        col = i % 3
        ax = fig.add_subplot(gs[row, col])
        ax.axis('off')
        
        # Create metric box
        ax.text(0.5, 0.6, metric['value'], 
               ha='center', va='center', fontsize=32, fontweight='bold',
               color=metric['color'])
        ax.text(0.5, 0.3, metric['title'], 
               ha='center', va='center', fontsize=14,
               color='#34495E')
        
        # Add border
        rect = plt.Rectangle((0.05, 0.1), 0.9, 0.8, 
                            fill=False, edgecolor=metric['color'], 
                            linewidth=3, transform=ax.transAxes)
        ax.add_patch(rect)
    
    # Top genres mini chart
    ax_genre = fig.add_subplot(gs[2, :2])
    top_5_genres = [g['genre'] for g in genre_data[:5]]
    top_5_counts = [g['count'] for g in genre_data[:5]]
    colors = sns.color_palette('Set2', 5)
    
    bars = ax_genre.barh(top_5_genres, top_5_counts, color=colors, edgecolor='black', linewidth=1.5)
    ax_genre.set_xlabel('Number of Movies', fontsize=11, fontweight='bold')
    ax_genre.set_title('Top 5 Genres', fontsize=13, fontweight='bold')
    ax_genre.invert_yaxis()
    
    for i, (bar, count) in enumerate(zip(bars, top_5_counts)):
        ax_genre.text(count + 200, i, f'{count:,}', va='center', fontsize=10, fontweight='bold')
    
    # Top countries mini chart
    ax_country = fig.add_subplot(gs[2, 2])
    top_5_countries = [c['country'] for c in country_data[:5]]
    top_5_country_counts = [c['count'] for c in country_data[:5]]
    
    colors_country = sns.color_palette('Set3', 5)
    wedges, texts, autotexts = ax_country.pie(top_5_country_counts, labels=top_5_countries,
                                               autopct='%1.0f%%', colors=colors_country,
                                               textprops={'fontsize': 9})
    
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')
    
    ax_country.set_title('Top 5 Countries', fontsize=13, fontweight='bold')
    
    pdf.savefig(fig, bbox_inches='tight', dpi=300)
    plt.close()

def main():
    """Main function to generate PDF report"""
    print("🎬 Starting Upstash MongoDB Visualization Generation...")
    
    pdf_filename = '/vercel/sandbox/upstash_analysis_report.pdf'
    
    with PdfPages(pdf_filename) as pdf:
        print("📄 Creating title page...")
        create_title_page(pdf)
        
        print("📊 Generating genre analysis charts...")
        plot_genre_distribution(pdf)
        
        print("🌍 Generating country analysis charts...")
        plot_country_analysis(pdf)
        
        print("🎥 Generating director analysis charts...")
        plot_director_analysis(pdf)
        
        print("🛍️ Generating product analysis charts...")
        plot_product_analysis(pdf)
        
        print("💰 Generating price-rating analysis charts...")
        plot_price_rating_analysis(pdf)
        
        print("📈 Generating executive dashboard...")
        plot_summary_dashboard(pdf)
        
        # Set PDF metadata
        d = pdf.infodict()
        d['Title'] = 'Upstash MongoDB Data Analysis Report'
        d['Author'] = 'Blackbox AI'
        d['Subject'] = 'Comprehensive analysis of Upstash MongoDB data'
        d['Keywords'] = 'MongoDB, Upstash, Data Analysis, Visualization'
        d['CreationDate'] = datetime.now()
    
    print(f"✅ PDF report generated successfully: {pdf_filename}")
    print(f"📊 Total pages: 7")
    print("🎉 Visualization complete!")

if __name__ == "__main__":
    main()
