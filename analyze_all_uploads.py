import os
import json
from pathlib import Path

def analyze_all_images():
    """Analyze all images in the uploads directory"""
    
    uploads_dir = Path("/vercel/sandbox/uploads")
    
    # Get all image files
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp']:
        image_files.extend(uploads_dir.glob(ext))
    
    print(f"Found {len(image_files)} images to analyze")
    print("=" * 80)
    
    analysis_results = {}
    
    for img_path in sorted(image_files):
        print(f"\n📸 Analyzing: {img_path.name}")
        print("-" * 80)
        
        # Basic file info
        file_size = img_path.stat().st_size
        print(f"File size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
        
        # Try to get image dimensions using PIL
        try:
            from PIL import Image
            with Image.open(img_path) as img:
                width, height = img.size
                mode = img.mode
                format_type = img.format
                
                print(f"Dimensions: {width} x {height} pixels")
                print(f"Format: {format_type}")
                print(f"Color mode: {mode}")
                
                # Analyze content based on filename
                filename = img_path.name.lower()
                
                content_analysis = ""
                if "error" in filename:
                    content_analysis = "Error/Debug Screenshot - Likely contains error messages or debugging information"
                elif "test" in filename:
                    content_analysis = "Test Screenshot - Likely contains testing interface or test results"
                elif "commit" in filename:
                    content_analysis = "Commit History - Likely shows git commit logs or version control information"
                elif "screenshot" in filename:
                    content_analysis = "General Screenshot - Application or interface capture"
                else:
                    content_analysis = "Image file - Content type unknown"
                
                print(f"Content type: {content_analysis}")
                
                analysis_results[img_path.name] = {
                    "filename": img_path.name,
                    "file_size_bytes": file_size,
                    "file_size_kb": round(file_size/1024, 2),
                    "dimensions": f"{width}x{height}",
                    "width": width,
                    "height": height,
                    "format": format_type,
                    "color_mode": mode,
                    "content_type": content_analysis
                }
                
        except ImportError:
            print("PIL not available, installing...")
            os.system("pip install -q Pillow")
            print("Please run the script again")
            return
        except Exception as e:
            print(f"Error analyzing image: {e}")
            analysis_results[img_path.name] = {
                "filename": img_path.name,
                "file_size_bytes": file_size,
                "error": str(e)
            }
    
    # Save results to JSON
    output_file = "/vercel/sandbox/all_uploads_analysis.json"
    with open(output_file, 'w') as f:
        json.dump(analysis_results, f, indent=2)
    
    print("\n" + "=" * 80)
    print(f"✅ Analysis complete! Results saved to: {output_file}")
    print(f"Total images analyzed: {len(analysis_results)}")
    
    return analysis_results

if __name__ == "__main__":
    analyze_all_images()
