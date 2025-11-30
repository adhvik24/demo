import sys
import json

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

def analyze_pdf(pdf_path):
    """Analyze PDF file and extract comprehensive information"""
    
    analysis = {
        "file_path": pdf_path,
        "metadata": {},
        "structure": {},
        "content": {
            "text_by_page": [],
            "total_text_length": 0,
            "page_summaries": []
        }
    }
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract metadata
            if pdf_reader.metadata:
                analysis["metadata"] = {
                    "title": pdf_reader.metadata.get('/Title', 'N/A'),
                    "author": pdf_reader.metadata.get('/Author', 'N/A'),
                    "subject": pdf_reader.metadata.get('/Subject', 'N/A'),
                    "creator": pdf_reader.metadata.get('/Creator', 'N/A'),
                    "producer": pdf_reader.metadata.get('/Producer', 'N/A'),
                    "creation_date": pdf_reader.metadata.get('/CreationDate', 'N/A'),
                    "modification_date": pdf_reader.metadata.get('/ModDate', 'N/A')
                }
            
            # Extract structure information
            num_pages = len(pdf_reader.pages)
            analysis["structure"]["total_pages"] = num_pages
            analysis["structure"]["is_encrypted"] = pdf_reader.is_encrypted
            
            # Extract text from each page
            all_text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                analysis["content"]["text_by_page"].append({
                    "page_number": page_num + 1,
                    "text": text,
                    "character_count": len(text),
                    "word_count": len(text.split())
                })
                
                all_text += text + "\n"
            
            analysis["content"]["total_text_length"] = len(all_text)
            analysis["content"]["total_word_count"] = len(all_text.split())
            
            # Create summary
            print("\n" + "="*80)
            print("PDF ANALYSIS REPORT")
            print("="*80)
            print(f"\nFile: {pdf_path}")
            print(f"\n--- METADATA ---")
            for key, value in analysis["metadata"].items():
                print(f"{key.capitalize()}: {value}")
            
            print(f"\n--- STRUCTURE ---")
            print(f"Total Pages: {num_pages}")
            print(f"Encrypted: {analysis['structure']['is_encrypted']}")
            
            print(f"\n--- CONTENT OVERVIEW ---")
            print(f"Total Characters: {analysis['content']['total_text_length']:,}")
            print(f"Total Words: {analysis['content']['total_word_count']:,}")
            
            print(f"\n--- PAGE-BY-PAGE BREAKDOWN ---")
            for page_info in analysis["content"]["text_by_page"]:
                print(f"\nPage {page_info['page_number']}:")
                print(f"  Characters: {page_info['character_count']:,}")
                print(f"  Words: {page_info['word_count']:,}")
                
                # Show first 500 characters of each page
                preview = page_info['text'][:500].strip()
                if preview:
                    print(f"  Preview: {preview}...")
                else:
                    print(f"  Preview: [No text extracted]")
            
            print("\n" + "="*80)
            print("FULL TEXT CONTENT")
            print("="*80)
            print(all_text)
            
            # Save detailed analysis to JSON
            with open('/vercel/sandbox/pdf_analysis.json', 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            
            print("\n" + "="*80)
            print("Detailed analysis saved to: pdf_analysis.json")
            print("="*80)
            
    except Exception as e:
        print(f"Error analyzing PDF: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    analyze_pdf("/vercel/sandbox/uploads/lekl101.pdf")
