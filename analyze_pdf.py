import pdfplumber
import json
import re
from collections import Counter

# Phase 1: Extract and understand PDF structure
pdf_path = '/vercel/sandbox/uploads/lekl101.pdf'

print("Phase 1: Extracting PDF content and structure...")

with pdfplumber.open(pdf_path) as pdf:
    total_pages = len(pdf.pages)
    print(f"Total pages: {total_pages}")
    
    # Extract all text
    full_text = ""
    page_texts = []
    
    for i, page in enumerate(pdf.pages):
        page_text = page.extract_text()
        if page_text:
            page_texts.append({
                'page_number': i + 1,
                'text': page_text,
                'char_count': len(page_text)
            })
            full_text += page_text + "\n"
    
    # Extract tables if any
    tables_data = []
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        if tables:
            for j, table in enumerate(tables):
                tables_data.append({
                    'page': i + 1,
                    'table_index': j,
                    'rows': len(table),
                    'columns': len(table[0]) if table else 0,
                    'data': table
                })
    
    # Basic statistics
    word_count = len(full_text.split())
    char_count = len(full_text)
    line_count = len(full_text.split('\n'))
    
    print(f"Word count: {word_count}")
    print(f"Character count: {char_count}")
    print(f"Line count: {line_count}")
    print(f"Tables found: {len(tables_data)}")

# Save initial structure
structure_data = {
    'total_pages': total_pages,
    'word_count': word_count,
    'char_count': char_count,
    'line_count': line_count,
    'tables_count': len(tables_data),
    'pages': page_texts,
    'tables': tables_data
}

with open('/vercel/sandbox/pdf_structure.json', 'w', encoding='utf-8') as f:
    json.dump(structure_data, f, indent=2, ensure_ascii=False)

print("\nStructure saved to pdf_structure.json")
print(f"\nFirst 500 characters of content:\n{full_text[:500]}")
