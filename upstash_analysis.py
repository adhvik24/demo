import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Database details
db_info = {
    "database_name": "Test",
    "database_type": "free",
    "region": "global",
    "primary_region": "us-east-1",
    "creation_time": "12/3/2025, 6:34:36 PM UTC",
    "state": "active",
    "endpoint": "organic-pika-44003.upstash.io",
    "db_disk_threshold": 268435456,  # bytes
    "db_memory_threshold": 67108864,  # bytes
    "db_monthly_bandwidth_limit": 50,  # MB
    "db_request_limit": 500000,
    "db_max_commands_per_second": 10000
}

# Usage data (last 5 days)
usage_data = {
    "days": ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
    "dates": ["2025-11-28", "2025-11-29", "2025-11-30", "2025-12-01", "2025-12-02", "2025-12-03", "2025-12-04"],
    "command_usage": [0, 0, 0, 0, 0, 49, 2],
    "bandwidth_usage": [0, 0, 0, 0, 0, 1436, 2]  # bytes
}

# Redis data structure
redis_data = {
    "total_keys": 7,
    "keys": {
        "jobs": {
            "type": "list",
            "data": ["job3", "job2", "job1"],
            "count": 3
        },
        "profile:1": {
            "type": "hash",
            "data": {"name": "Alice", "age": "25"},
            "fields": 2
        },
        "profile:2": {
            "type": "hash",
            "data": {"name": "Bob", "age": "30"},
            "fields": 2
        },
        "user:1": {
            "type": "string",
            "data": "User 1"
        },
        "user:100": {
            "type": "string",
            "data": "User 100"
        },
        "user:2": {
            "type": "string",
            "data": "User Two"
        },
        "user:3": {
            "type": "string",
            "data": "User Three"
        }
    }
}

# Throughput data (sampled)
throughput_data = [
    [1764792480000, 0.0046957135379996455],
    [1764802560000, 0.00009970089730807578],
    [1764873120000, 0.00019974670592336826]
]

# Create output directory for images
os.makedirs('upstash_charts', exist_ok=True)

print("Generating Upstash Redis Database Analysis...")

# Chart 1: Database Overview Dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Upstash Redis Database Overview - "Test"', fontsize=16, fontweight='bold')

# 1.1: Key Distribution by Type
ax1 = axes[0, 0]
key_types = {}
for key, info in redis_data['keys'].items():
    key_type = info['type']
    key_types[key_type] = key_types.get(key_type, 0) + 1

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
ax1.pie(key_types.values(), labels=key_types.keys(), autopct='%1.1f%%', 
        colors=colors, startangle=90)
ax1.set_title('Key Distribution by Data Type', fontweight='bold')

# 1.2: Database Limits Overview
ax2 = axes[0, 1]
limits = ['Disk\n(256 MB)', 'Memory\n(64 MB)', 'Bandwidth\n(50 MB/mo)', 'Requests\n(500K)', 'Cmds/sec\n(10K)']
values = [256, 64, 50, 500, 10]
bars = ax2.barh(limits, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#95E1D3', '#F38181'])
ax2.set_xlabel('Limit Value', fontweight='bold')
ax2.set_title('Database Resource Limits', fontweight='bold')
ax2.grid(axis='x', alpha=0.3)

# 1.3: Command Usage (Last 7 Days)
ax3 = axes[1, 0]
ax3.bar(usage_data['days'], usage_data['command_usage'], color='#4ECDC4', alpha=0.8)
ax3.set_xlabel('Day', fontweight='bold')
ax3.set_ylabel('Commands', fontweight='bold')
ax3.set_title('Command Usage (Last 7 Days)', fontweight='bold')
ax3.tick_params(axis='x', rotation=45)
ax3.grid(axis='y', alpha=0.3)

# 1.4: Bandwidth Usage (Last 7 Days)
ax4 = axes[1, 1]
bandwidth_kb = [b / 1024 for b in usage_data['bandwidth_usage']]
ax4.bar(usage_data['days'], bandwidth_kb, color='#FF6B6B', alpha=0.8)
ax4.set_xlabel('Day', fontweight='bold')
ax4.set_ylabel('Bandwidth (KB)', fontweight='bold')
ax4.set_title('Bandwidth Usage (Last 7 Days)', fontweight='bold')
ax4.tick_params(axis='x', rotation=45)
ax4.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('upstash_charts/01_database_overview.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Detailed Command and Bandwidth Analysis
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Usage Trends Analysis', fontsize=16, fontweight='bold')

# 2.1: Command Usage Timeline
ax1 = axes[0]
ax1.plot(usage_data['dates'], usage_data['command_usage'], marker='o', 
         linewidth=2, markersize=8, color='#4ECDC4', label='Commands')
ax1.fill_between(usage_data['dates'], usage_data['command_usage'], alpha=0.3, color='#4ECDC4')
ax1.set_xlabel('Date', fontweight='bold')
ax1.set_ylabel('Number of Commands', fontweight='bold')
ax1.set_title('Command Usage Timeline', fontweight='bold')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Add annotations for non-zero values
for i, (date, cmd) in enumerate(zip(usage_data['dates'], usage_data['command_usage'])):
    if cmd > 0:
        ax1.annotate(f'{cmd}', xy=(i, cmd), xytext=(0, 10), 
                    textcoords='offset points', ha='center', fontweight='bold')

# 2.2: Bandwidth Usage Timeline
ax2 = axes[1]
ax2.plot(usage_data['dates'], bandwidth_kb, marker='s', 
         linewidth=2, markersize=8, color='#FF6B6B', label='Bandwidth (KB)')
ax2.fill_between(usage_data['dates'], bandwidth_kb, alpha=0.3, color='#FF6B6B')
ax2.set_xlabel('Date', fontweight='bold')
ax2.set_ylabel('Bandwidth (KB)', fontweight='bold')
ax2.set_title('Bandwidth Usage Timeline', fontweight='bold')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)
ax2.legend()

# Add annotations for non-zero values
for i, (date, bw) in enumerate(zip(usage_data['dates'], bandwidth_kb)):
    if bw > 0:
        ax2.annotate(f'{bw:.2f}', xy=(i, bw), xytext=(0, 10), 
                    textcoords='offset points', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('upstash_charts/02_usage_trends.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Data Structure Analysis
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Redis Data Structure Analysis', fontsize=16, fontweight='bold')

# 3.1: Keys by Pattern
ax1 = axes[0, 0]
key_patterns = {}
for key in redis_data['keys'].keys():
    if ':' in key:
        pattern = key.split(':')[0]
    else:
        pattern = key
    key_patterns[pattern] = key_patterns.get(pattern, 0) + 1

ax1.bar(key_patterns.keys(), key_patterns.values(), color=['#4ECDC4', '#FF6B6B', '#45B7D1'])
ax1.set_xlabel('Key Pattern', fontweight='bold')
ax1.set_ylabel('Count', fontweight='bold')
ax1.set_title('Keys Grouped by Pattern', fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# 3.2: Data Type Distribution (Detailed)
ax2 = axes[0, 1]
type_details = []
for key, info in redis_data['keys'].items():
    type_details.append({
        'key': key,
        'type': info['type'],
        'size': info.get('count', info.get('fields', 1))
    })

df_types = pd.DataFrame(type_details)
type_colors = {'list': '#FF6B6B', 'hash': '#4ECDC4', 'string': '#45B7D1'}
for i, (key, row) in enumerate(df_types.iterrows()):
    ax2.barh(i, row['size'], color=type_colors[row['type']], alpha=0.8)
    ax2.text(row['size'] + 0.1, i, f"{row['key']} ({row['type']})", 
             va='center', fontsize=9)

ax2.set_yticks([])
ax2.set_xlabel('Size/Count', fontweight='bold')
ax2.set_title('Key Details with Data Types', fontweight='bold')
ax2.grid(axis='x', alpha=0.3)

# 3.3: User Keys Analysis
ax3 = axes[1, 0]
user_keys = [k for k in redis_data['keys'].keys() if k.startswith('user:')]
user_ids = [k.split(':')[1] for k in user_keys]
user_values = [redis_data['keys'][k]['data'] for k in user_keys]

ax3.bar(range(len(user_keys)), [1]*len(user_keys), color='#95E1D3', alpha=0.8)
ax3.set_xticks(range(len(user_keys)))
ax3.set_xticklabels(user_ids)
ax3.set_xlabel('User ID', fontweight='bold')
ax3.set_ylabel('Exists', fontweight='bold')
ax3.set_title('User Keys Distribution', fontweight='bold')
ax3.set_ylim(0, 1.5)

# Add value labels
for i, val in enumerate(user_values):
    ax3.text(i, 1.1, val, ha='center', va='bottom', fontsize=8, rotation=0)

# 3.4: Profile Keys Analysis
ax4 = axes[1, 1]
profile_keys = [k for k in redis_data['keys'].keys() if k.startswith('profile:')]
profile_data = []
for pk in profile_keys:
    data = redis_data['keys'][pk]['data']
    profile_data.append({
        'Profile': pk,
        'Name': data.get('name', 'N/A'),
        'Age': int(data.get('age', 0))
    })

df_profiles = pd.DataFrame(profile_data)
x_pos = range(len(df_profiles))
bars = ax4.bar(x_pos, df_profiles['Age'], color=['#FF6B6B', '#4ECDC4'], alpha=0.8)
ax4.set_xticks(x_pos)
ax4.set_xticklabels(df_profiles['Name'])
ax4.set_xlabel('Profile Name', fontweight='bold')
ax4.set_ylabel('Age', fontweight='bold')
ax4.set_title('Profile Ages Comparison', fontweight='bold')
ax4.grid(axis='y', alpha=0.3)

# Add value labels
for i, (bar, age) in enumerate(zip(bars, df_profiles['Age'])):
    ax4.text(bar.get_x() + bar.get_width()/2, age + 0.5, str(age), 
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('upstash_charts/03_data_structure.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 4: Throughput Analysis
fig, ax = plt.subplots(1, 1, figsize=(14, 6))
fig.suptitle('Throughput Analysis (Commands per Second)', fontsize=16, fontweight='bold')

# Convert timestamps to datetime
timestamps = [datetime.fromtimestamp(t[0]/1000) for t in throughput_data]
throughput_values = [t[1] for t in throughput_data]

ax.plot(timestamps, throughput_values, marker='o', linewidth=2, markersize=10, 
        color='#4ECDC4', label='Throughput (cmds/sec)')
ax.fill_between(timestamps, throughput_values, alpha=0.3, color='#4ECDC4')
ax.set_xlabel('Time (UTC)', fontweight='bold')
ax.set_ylabel('Commands per Second', fontweight='bold')
ax.set_title('Sampled Throughput Over Time', fontweight='bold')
ax.tick_params(axis='x', rotation=45)
ax.grid(True, alpha=0.3)
ax.legend()

# Add value annotations
for ts, val in zip(timestamps, throughput_values):
    ax.annotate(f'{val:.6f}', xy=(ts, val), xytext=(0, 10), 
                textcoords='offset points', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('upstash_charts/04_throughput.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 5: Resource Utilization Summary
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Resource Utilization & Capacity', fontsize=16, fontweight='bold')

# 5.1: Total Commands (5-day summary)
ax1 = axes[0, 0]
total_commands = sum(usage_data['command_usage'])
remaining_commands = db_info['db_request_limit'] - total_commands
labels = ['Used', 'Remaining']
sizes = [total_commands, remaining_commands]
colors = ['#FF6B6B', '#E8E8E8']
explode = (0.1, 0)

ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', 
        colors=colors, startangle=90, shadow=True)
ax1.set_title(f'Command Limit Usage\n(Total: {total_commands:,} / {db_info["db_request_limit"]:,})', 
              fontweight='bold')

# 5.2: Total Bandwidth (5-day summary)
ax2 = axes[0, 1]
total_bandwidth_mb = sum(usage_data['bandwidth_usage']) / (1024 * 1024)
remaining_bandwidth = db_info['db_monthly_bandwidth_limit'] - total_bandwidth_mb
labels = ['Used', 'Remaining']
sizes = [total_bandwidth_mb, remaining_bandwidth]
colors = ['#4ECDC4', '#E8E8E8']
explode = (0.1, 0)

ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.4f%%', 
        colors=colors, startangle=90, shadow=True)
ax2.set_title(f'Bandwidth Limit Usage\n(Total: {total_bandwidth_mb:.4f} / {db_info["db_monthly_bandwidth_limit"]} MB)', 
              fontweight='bold')

# 5.3: Database Activity Heatmap
ax3 = axes[1, 0]
activity_matrix = []
activity_matrix.append(usage_data['command_usage'])
activity_matrix.append(bandwidth_kb)

sns.heatmap(activity_matrix, annot=True, fmt='.1f', cmap='YlOrRd', 
            xticklabels=usage_data['days'], 
            yticklabels=['Commands', 'Bandwidth (KB)'],
            cbar_kws={'label': 'Activity Level'}, ax=ax3)
ax3.set_title('Activity Heatmap (Last 7 Days)', fontweight='bold')

# 5.4: Key Statistics Summary
ax4 = axes[1, 1]
ax4.axis('off')

stats_text = f"""
DATABASE STATISTICS SUMMARY

Database Name: {db_info['database_name']}
Type: {db_info['database_type'].upper()}
Region: {db_info['primary_region']}
Status: {db_info['state'].upper()}
Created: {db_info['creation_time']}

STORAGE & LIMITS:
• Total Keys: {redis_data['total_keys']}
• Disk Limit: {db_info['db_disk_threshold'] / (1024**2):.0f} MB
• Memory Limit: {db_info['db_memory_threshold'] / (1024**2):.0f} MB
• Max Commands/sec: {db_info['db_max_commands_per_second']:,}

USAGE (LAST 5 DAYS):
• Total Commands: {total_commands}
• Total Bandwidth: {total_bandwidth_mb:.4f} MB
• Peak Commands: {max(usage_data['command_usage'])} (Dec 3)
• Peak Bandwidth: {max(bandwidth_kb):.2f} KB (Dec 3)

DATA STRUCTURE:
• String Keys: {key_types.get('string', 0)}
• Hash Keys: {key_types.get('hash', 0)}
• List Keys: {key_types.get('list', 0)}
"""

ax4.text(0.1, 0.9, stats_text, transform=ax4.transAxes, 
         fontsize=11, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig('upstash_charts/05_resource_utilization.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Generated 5 comprehensive visualization charts")

# Generate PDF Report
print("\nGenerating PDF report...")

pdf_filename = 'upstash_analysis_report.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
story = []
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor='#2C3E50',
    spaceAfter=30,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor='#34495E',
    spaceAfter=12,
    spaceBefore=12
)

# Title
story.append(Paragraph("Upstash Redis Database Analysis Report", title_style))
story.append(Spacer(1, 0.3*inch))

# Database Info
story.append(Paragraph("Database Information", heading_style))
story.append(Paragraph(f"<b>Name:</b> {db_info['database_name']}", styles['Normal']))
story.append(Paragraph(f"<b>Type:</b> {db_info['database_type'].upper()}", styles['Normal']))
story.append(Paragraph(f"<b>Region:</b> {db_info['primary_region']}", styles['Normal']))
story.append(Paragraph(f"<b>Status:</b> {db_info['state'].upper()}", styles['Normal']))
story.append(Paragraph(f"<b>Endpoint:</b> {db_info['endpoint']}", styles['Normal']))
story.append(Spacer(1, 0.2*inch))

# Chart 1
story.append(Paragraph("Database Overview Dashboard", heading_style))
story.append(Image('upstash_charts/01_database_overview.png', width=7*inch, height=5*inch))
story.append(PageBreak())

# Chart 2
story.append(Paragraph("Usage Trends Analysis", heading_style))
story.append(Image('upstash_charts/02_usage_trends.png', width=7*inch, height=3*inch))
story.append(Spacer(1, 0.2*inch))

# Chart 3
story.append(Paragraph("Data Structure Analysis", heading_style))
story.append(Image('upstash_charts/03_data_structure.png', width=7*inch, height=5*inch))
story.append(PageBreak())

# Chart 4
story.append(Paragraph("Throughput Analysis", heading_style))
story.append(Image('upstash_charts/04_throughput.png', width=7*inch, height=3*inch))
story.append(Spacer(1, 0.2*inch))

# Chart 5
story.append(Paragraph("Resource Utilization & Capacity", heading_style))
story.append(Image('upstash_charts/05_resource_utilization.png', width=7*inch, height=5*inch))

# Build PDF
doc.build(story)

print(f"✓ PDF report generated: {pdf_filename}")
print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print(f"\nGenerated files:")
print(f"  • PDF Report: {pdf_filename}")
print(f"  • Chart Images: upstash_charts/ (5 images)")
print("\nKey Findings:")
print(f"  • Total Keys: {redis_data['total_keys']}")
print(f"  • Total Commands (5 days): {total_commands}")
print(f"  • Total Bandwidth (5 days): {total_bandwidth_mb:.4f} MB")
print(f"  • Peak Activity: December 3, 2025")
print(f"  • Data Types: {len(key_types)} types (string, hash, list)")
