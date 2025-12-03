import json
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Database details
db_details = {
    "database_name": "Test",
    "database_type": "free",
    "region": "global",
    "primary_region": "us-east-1",
    "creation_time": "12/3/2025, 6:34:36 PM UTC",
    "state": "active",
    "endpoint": "organic-pika-44003.upstash.io",
    "tls": True,
    "eviction": False,
    "db_disk_threshold": 268435456,  # bytes
    "db_memory_threshold": 67108864,  # bytes
    "db_max_request_size": 10485760,  # bytes
    "db_request_limit": 500000,
    "db_max_commands_per_second": 10000,
    "db_monthly_bandwidth_limit": 50  # GB
}

# Usage statistics
usage_stats = {
    "days": ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"],
    "dates": ["2025-11-27", "2025-11-28", "2025-11-29", "2025-11-30", "2025-12-01", "2025-12-02", "2025-12-03"],
    "command_usage": [0, 0, 0, 0, 0, 0, 21],
    "bandwidth_usage": [0, 0, 0, 0, 0, 0, 1016]  # bytes
}

# Data structure analysis
data_structure = {
    "total_keys": 7,
    "keys": {
        "jobs": {"type": "list", "value": ["job3", "job2", "job1"]},
        "profile:1": {"type": "hash", "value": {"name": "Alice", "age": "25"}},
        "profile:2": {"type": "hash", "value": {"name": "Bob", "age": "30"}},
        "user:1": {"type": "string", "value": "User 1"},
        "user:2": {"type": "string", "value": "User Two"},
        "user:3": {"type": "string", "value": "User Three"},
        "user:100": {"type": "string", "value": "User 100"}
    }
}

# Analyze data types
data_types = {}
key_patterns = {}
for key, info in data_structure["keys"].items():
    dtype = info["type"]
    data_types[dtype] = data_types.get(dtype, 0) + 1
    
    # Extract key pattern
    if ":" in key:
        pattern = key.split(":")[0]
    else:
        pattern = key
    key_patterns[pattern] = key_patterns.get(pattern, 0) + 1

# Create PDF with visualizations
pdf_filename = '/vercel/sandbox/upstash_analysis_report.pdf'

with PdfPages(pdf_filename) as pdf:
    # Page 1: Overview Dashboard
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Upstash Redis Database Analysis - Overview', fontsize=16, fontweight='bold')
    
    # Database info text
    ax1 = plt.subplot(3, 2, 1)
    ax1.axis('off')
    info_text = f"""DATABASE INFORMATION
    
Name: {db_details['database_name']}
Type: {db_details['database_type'].upper()}
Region: {db_details['primary_region']}
Status: {db_details['state'].upper()}
Created: {db_details['creation_time']}
Endpoint: {db_details['endpoint']}
TLS Enabled: {db_details['tls']}

LIMITS & THRESHOLDS
Disk Threshold: {db_details['db_disk_threshold'] / (1024**2):.0f} MB
Memory Threshold: {db_details['db_memory_threshold'] / (1024**2):.0f} MB
Max Request Size: {db_details['db_max_request_size'] / (1024**2):.0f} MB
Request Limit: {db_details['db_request_limit']:,}
Max Commands/sec: {db_details['db_max_commands_per_second']:,}
Monthly Bandwidth: {db_details['db_monthly_bandwidth_limit']} GB"""
    
    ax1.text(0.05, 0.95, info_text, transform=ax1.transAxes, 
             fontsize=9, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    # Data type distribution pie chart
    ax2 = plt.subplot(3, 2, 2)
    colors = sns.color_palette('Set2', len(data_types))
    wedges, texts, autotexts = ax2.pie(data_types.values(), labels=data_types.keys(), 
                                         autopct='%1.1f%%', colors=colors, startangle=90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    ax2.set_title('Data Types Distribution', fontweight='bold', pad=20)
    
    # Key patterns bar chart
    ax3 = plt.subplot(3, 2, 3)
    patterns = list(key_patterns.keys())
    counts = list(key_patterns.values())
    bars = ax3.bar(patterns, counts, color=sns.color_palette('viridis', len(patterns)))
    ax3.set_title('Key Patterns Distribution', fontweight='bold', pad=10)
    ax3.set_xlabel('Key Pattern')
    ax3.set_ylabel('Count')
    ax3.grid(axis='y', alpha=0.3)
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    # Total keys metric
    ax4 = plt.subplot(3, 2, 4)
    ax4.axis('off')
    ax4.text(0.5, 0.5, f'{data_structure["total_keys"]}', 
             transform=ax4.transAxes, fontsize=72, fontweight='bold',
             ha='center', va='center', color='#2E86AB')
    ax4.text(0.5, 0.2, 'TOTAL KEYS', transform=ax4.transAxes, 
             fontsize=16, ha='center', va='center', color='#555')
    
    # Command usage over time
    ax5 = plt.subplot(3, 2, 5)
    ax5.plot(usage_stats['days'], usage_stats['command_usage'], 
             marker='o', linewidth=2, markersize=8, color='#E63946')
    ax5.fill_between(range(len(usage_stats['days'])), usage_stats['command_usage'], 
                      alpha=0.3, color='#E63946')
    ax5.set_title('Command Usage (Last 7 Days)', fontweight='bold', pad=10)
    ax5.set_xlabel('Day')
    ax5.set_ylabel('Commands')
    ax5.grid(True, alpha=0.3)
    ax5.tick_params(axis='x', rotation=45)
    
    # Bandwidth usage over time
    ax6 = plt.subplot(3, 2, 6)
    ax6.plot(usage_stats['days'], usage_stats['bandwidth_usage'], 
             marker='s', linewidth=2, markersize=8, color='#06A77D')
    ax6.fill_between(range(len(usage_stats['days'])), usage_stats['bandwidth_usage'], 
                      alpha=0.3, color='#06A77D')
    ax6.set_title('Bandwidth Usage (Last 7 Days)', fontweight='bold', pad=10)
    ax6.set_xlabel('Day')
    ax6.set_ylabel('Bytes')
    ax6.grid(True, alpha=0.3)
    ax6.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    pdf.savefig(fig, dpi=300, bbox_inches='tight')
    plt.close()
    
    # Page 2: Data Structure Details
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Upstash Redis Database - Data Structure Analysis', fontsize=16, fontweight='bold')
    
    # String keys analysis
    ax1 = plt.subplot(2, 2, 1)
    string_keys = {k: v for k, v in data_structure["keys"].items() if v["type"] == "string"}
    string_key_names = list(string_keys.keys())
    string_values = [len(v["value"]) for v in string_keys.values()]
    
    bars = ax1.barh(string_key_names, string_values, color=sns.color_palette('Blues_r', len(string_keys)))
    ax1.set_title('String Keys - Value Length', fontweight='bold', pad=10)
    ax1.set_xlabel('Value Length (characters)')
    ax1.grid(axis='x', alpha=0.3)
    for i, (bar, val) in enumerate(zip(bars, string_values)):
        ax1.text(val, bar.get_y() + bar.get_height()/2, f' {val}', 
                va='center', fontweight='bold')
    
    # Hash keys analysis
    ax2 = plt.subplot(2, 2, 2)
    hash_keys = {k: v for k, v in data_structure["keys"].items() if v["type"] == "hash"}
    hash_key_names = list(hash_keys.keys())
    hash_field_counts = [len(v["value"]) for v in hash_keys.values()]
    
    bars = ax2.barh(hash_key_names, hash_field_counts, color=sns.color_palette('Oranges_r', len(hash_keys)))
    ax2.set_title('Hash Keys - Field Count', fontweight='bold', pad=10)
    ax2.set_xlabel('Number of Fields')
    ax2.grid(axis='x', alpha=0.3)
    for i, (bar, val) in enumerate(zip(bars, hash_field_counts)):
        ax2.text(val, bar.get_y() + bar.get_height()/2, f' {val}', 
                va='center', fontweight='bold')
    
    # List keys analysis
    ax3 = plt.subplot(2, 2, 3)
    list_keys = {k: v for k, v in data_structure["keys"].items() if v["type"] == "list"}
    list_key_names = list(list_keys.keys())
    list_lengths = [len(v["value"]) for v in list_keys.values()]
    
    bars = ax3.barh(list_key_names, list_lengths, color=sns.color_palette('Greens_r', len(list_keys)))
    ax3.set_title('List Keys - Element Count', fontweight='bold', pad=10)
    ax3.set_xlabel('Number of Elements')
    ax3.grid(axis='x', alpha=0.3)
    for i, (bar, val) in enumerate(zip(bars, list_lengths)):
        ax3.text(val, bar.get_y() + bar.get_height()/2, f' {val}', 
                va='center', fontweight='bold')
    
    # Detailed data table
    ax4 = plt.subplot(2, 2, 4)
    ax4.axis('off')
    
    table_data = []
    for key, info in data_structure["keys"].items():
        dtype = info["type"]
        if dtype == "string":
            value_preview = info["value"][:30] + "..." if len(info["value"]) > 30 else info["value"]
        elif dtype == "hash":
            value_preview = f"{len(info['value'])} fields"
        elif dtype == "list":
            value_preview = f"{len(info['value'])} items"
        else:
            value_preview = str(info["value"])[:30]
        
        table_data.append([key, dtype, value_preview])
    
    table = ax4.table(cellText=table_data, 
                     colLabels=['Key', 'Type', 'Value/Info'],
                     cellLoc='left',
                     loc='center',
                     colWidths=[0.3, 0.2, 0.5])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Style header
    for i in range(3):
        table[(0, i)].set_facecolor('#2E86AB')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(table_data) + 1):
        for j in range(3):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#F0F0F0')
    
    ax4.set_title('All Keys Overview', fontweight='bold', pad=20, fontsize=12)
    
    plt.tight_layout()
    pdf.savefig(fig, dpi=300, bbox_inches='tight')
    plt.close()
    
    # Page 3: Usage Metrics
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Upstash Redis Database - Usage Metrics', fontsize=16, fontweight='bold')
    
    # Daily command usage with annotations
    ax1 = plt.subplot(2, 2, 1)
    bars = ax1.bar(usage_stats['days'], usage_stats['command_usage'], 
                   color=['#CCCCCC' if x == 0 else '#E63946' for x in usage_stats['command_usage']])
    ax1.set_title('Daily Command Usage', fontweight='bold', pad=10)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Number of Commands')
    ax1.grid(axis='y', alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    for bar, val in zip(bars, usage_stats['command_usage']):
        if val > 0:
            ax1.text(bar.get_x() + bar.get_width()/2., val,
                    f'{int(val)}', ha='center', va='bottom', fontweight='bold')
    
    # Daily bandwidth usage with annotations
    ax2 = plt.subplot(2, 2, 2)
    bars = ax2.bar(usage_stats['days'], usage_stats['bandwidth_usage'], 
                   color=['#CCCCCC' if x == 0 else '#06A77D' for x in usage_stats['bandwidth_usage']])
    ax2.set_title('Daily Bandwidth Usage', fontweight='bold', pad=10)
    ax2.set_xlabel('Day')
    ax2.set_ylabel('Bytes')
    ax2.grid(axis='y', alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    for bar, val in zip(bars, usage_stats['bandwidth_usage']):
        if val > 0:
            ax2.text(bar.get_x() + bar.get_width()/2., val,
                    f'{int(val)}', ha='center', va='bottom', fontweight='bold')
    
    # Usage summary metrics
    ax3 = plt.subplot(2, 2, 3)
    ax3.axis('off')
    
    total_commands = sum(usage_stats['command_usage'])
    total_bandwidth = sum(usage_stats['bandwidth_usage'])
    avg_commands = total_commands / 7
    avg_bandwidth = total_bandwidth / 7
    active_days = sum(1 for x in usage_stats['command_usage'] if x > 0)
    
    metrics_text = f"""USAGE SUMMARY (Last 7 Days)

Total Commands: {total_commands}
Total Bandwidth: {total_bandwidth} bytes ({total_bandwidth/1024:.2f} KB)
Average Commands/Day: {avg_commands:.2f}
Average Bandwidth/Day: {avg_bandwidth:.2f} bytes
Active Days: {active_days} / 7

PEAK USAGE
Peak Commands: {max(usage_stats['command_usage'])} (Wednesday)
Peak Bandwidth: {max(usage_stats['bandwidth_usage'])} bytes (Wednesday)

RESOURCE UTILIZATION
Commands Used: {total_commands} / {db_details['db_request_limit']:,} ({total_commands/db_details['db_request_limit']*100:.4f}%)
Bandwidth Used: {total_bandwidth/1024/1024:.4f} MB / {db_details['db_monthly_bandwidth_limit']*1024:.0f} MB
Keys Stored: {data_structure['total_keys']}"""
    
    ax3.text(0.05, 0.95, metrics_text, transform=ax3.transAxes, 
             fontsize=10, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    # Cumulative usage
    ax4 = plt.subplot(2, 2, 4)
    cumulative_commands = np.cumsum(usage_stats['command_usage'])
    cumulative_bandwidth = np.cumsum(usage_stats['bandwidth_usage'])
    
    ax4_twin = ax4.twinx()
    
    line1 = ax4.plot(usage_stats['days'], cumulative_commands, 
                     marker='o', linewidth=2, markersize=8, color='#E63946', label='Commands')
    line2 = ax4_twin.plot(usage_stats['days'], cumulative_bandwidth, 
                          marker='s', linewidth=2, markersize=8, color='#06A77D', label='Bandwidth')
    
    ax4.set_title('Cumulative Usage Over Time', fontweight='bold', pad=10)
    ax4.set_xlabel('Day')
    ax4.set_ylabel('Cumulative Commands', color='#E63946')
    ax4_twin.set_ylabel('Cumulative Bandwidth (bytes)', color='#06A77D')
    ax4.tick_params(axis='x', rotation=45)
    ax4.tick_params(axis='y', labelcolor='#E63946')
    ax4_twin.tick_params(axis='y', labelcolor='#06A77D')
    ax4.grid(True, alpha=0.3)
    
    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax4.legend(lines, labels, loc='upper left')
    
    plt.tight_layout()
    pdf.savefig(fig, dpi=300, bbox_inches='tight')
    plt.close()

print(f"PDF report generated: {pdf_filename}")

# Save detailed analysis to JSON
analysis_output = {
    "database_details": db_details,
    "usage_statistics": usage_stats,
    "data_structure": data_structure,
    "analysis": {
        "data_types": data_types,
        "key_patterns": key_patterns,
        "total_keys": data_structure["total_keys"],
        "total_commands_7d": sum(usage_stats['command_usage']),
        "total_bandwidth_7d": sum(usage_stats['bandwidth_usage']),
        "active_days": sum(1 for x in usage_stats['command_usage'] if x > 0)
    }
}

with open('/vercel/sandbox/upstash_analysis.json', 'w') as f:
    json.dump(analysis_output, f, indent=2)

print("JSON analysis saved: /vercel/sandbox/upstash_analysis.json")
