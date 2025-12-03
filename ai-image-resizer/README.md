# AI Image Resizer

A modern, AI-powered image resizing and optimization tool built with Next.js, TypeScript, and Sharp.

## Features

- 🎯 **AI Smart Cropping** - Content-aware resizing using Sharp's attention algorithm
- 📸 **Drag & Drop Upload** - Easy file selection interface
- 🎨 **Multiple Formats** - Convert to JPEG, PNG, or WebP
- ⚡ **Quality Control** - Adjustable compression settings
- 🔄 **Real-time Preview** - See changes before downloading
- 📱 **Responsive Design** - Works on all devices
- 🌙 **Dark Mode** - Automatic dark mode support

## Getting Started

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the app.

### Build

```bash
npm run build
npm start
```

## How to Use

1. **Upload an Image** - Drag and drop or click to select an image
2. **Set Dimensions** - Enter desired width and height
3. **Choose Format** - Select JPEG, PNG, or WebP
4. **Adjust Quality** - Use the slider to set compression level
5. **Select Fit Mode** - Choose how the image should be resized:
   - **Cover (AI Smart Crop)** - Uses AI to detect and preserve important content
   - **Contain** - Fit within dimensions, maintaining aspect ratio
   - **Fill** - Stretch to fill dimensions
   - **Inside** - Resize to fit inside dimensions
   - **Outside** - Resize to fit outside dimensions
6. **Resize** - Click the resize button
7. **Download** - Download your optimized image

## Technology Stack

- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Sharp** - High-performance image processing
- **AI Features** - Content-aware cropping using attention detection

## License

MIT
