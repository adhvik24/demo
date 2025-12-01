import json
from PIL import Image
import os

def analyze_image(image_path):
    """Analyze an image and extract detailed information"""
    try:
        with Image.open(image_path) as img:
            analysis = {
                "filename": os.path.basename(image_path),
                "format": img.format,
                "mode": img.mode,
                "size": {
                    "width": img.width,
                    "height": img.height
                },
                "aspect_ratio": round(img.width / img.height, 2),
                "file_size_bytes": os.path.getsize(image_path),
                "file_size_kb": round(os.path.getsize(image_path) / 1024, 2)
            }
            
            # Get color information
            if img.mode == "RGB" or img.mode == "RGBA":
                extrema = img.getextrema()
                analysis["color_info"] = {
                    "mode": img.mode,
                    "channels": len(extrema)
                }
            
            return analysis
    except Exception as e:
        return {"error": str(e), "filename": os.path.basename(image_path)}

def main():
    images = [
        "/vercel/sandbox/uploads/error.png",
        "/vercel/sandbox/uploads/test.png"
    ]
    
    results = {}
    
    for img_path in images:
        if os.path.exists(img_path):
            print(f"\nAnalyzing: {os.path.basename(img_path)}")
            analysis = analyze_image(img_path)
            results[os.path.basename(img_path)] = analysis
            
            # Print formatted output
            if "error" not in analysis:
                print(f"  Format: {analysis['format']}")
                print(f"  Dimensions: {analysis['size']['width']}x{analysis['size']['height']} pixels")
                print(f"  Aspect Ratio: {analysis['aspect_ratio']}")
                print(f"  File Size: {analysis['file_size_kb']} KB")
                print(f"  Color Mode: {analysis['mode']}")
            else:
                print(f"  Error: {analysis['error']}")
        else:
            print(f"\nFile not found: {img_path}")
            results[os.path.basename(img_path)] = {"error": "File not found"}
    
    # Save to JSON
    with open("/vercel/sandbox/image_analysis.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n✓ Analysis saved to image_analysis.json")

if __name__ == "__main__":
    main()
