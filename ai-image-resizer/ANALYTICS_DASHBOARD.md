# Analytics Dashboard Documentation

## Overview
A comprehensive analytics dashboard has been added to the AI Image Resizer application to track and visualize image processing metrics.

## Features Implemented

### 1. Analytics Tracking
- **Automatic Tracking**: Every image resize operation is automatically tracked
- **Metrics Captured**:
  - Original file size
  - Processed file size
  - Output format (JPEG, PNG, WebP)
  - Quality setting
  - Target dimensions (width x height)
  - Fit mode used
  - Processing time (milliseconds)
  - Compression ratio

### 2. Analytics API Endpoints

#### POST `/api/analytics`
Stores analytics data for each image processing operation.

**Request Body**:
```json
{
  "originalSize": 2048000,
  "processedSize": 512000,
  "format": "webp",
  "quality": 80,
  "width": 800,
  "height": 600,
  "fit": "cover",
  "processingTime": 245
}
```

#### GET `/api/analytics?days=30`
Retrieves analytics data with aggregated statistics.

**Query Parameters**:
- `days`: Number of days to retrieve data for (default: 30)

**Response**:
```json
{
  "summary": {
    "totalProcessed": 5,
    "totalOriginalSize": 10548000,
    "totalProcessedSize": 2612000,
    "totalSaved": 7936000,
    "avgProcessingTime": "259.00",
    "avgCompressionRatio": "75.24"
  },
  "formatDistribution": {
    "webp": 2,
    "jpeg": 2,
    "png": 1
  },
  "dailyStats": {
    "2025-12-11": 5
  },
  "recentProcessing": [...]
}
```

### 3. Analytics Dashboard Page

Access the dashboard at: `/analytics`

**Dashboard Components**:

1. **Summary Cards**:
   - Total images processed
   - Total data saved (with compression percentage)
   - Average processing time
   - Total original size

2. **Format Distribution Chart**:
   - Pie chart showing distribution of output formats
   - Percentage breakdown of JPEG, PNG, and WebP usage

3. **Daily Processing Chart**:
   - Line chart showing processing activity over time
   - Tracks number of images processed per day

4. **Recent Processing Table**:
   - Detailed table of the 10 most recent operations
   - Shows timestamp, format, sizes, compression ratio, and processing time

5. **Time Range Filter**:
   - Filter data by last 7, 30, or 90 days
   - Real-time data refresh

### 4. Navigation
- **Main Page**: Added "📊 View Analytics" button in the header
- **Analytics Page**: "Back to Resizer" button to return to main page

## Technical Implementation

### Data Storage
- Uses file-based JSON storage (`analytics-data.json`)
- Persistent across server restarts
- No database setup required

### Technologies Used
- **Recharts**: For data visualization (pie charts, line charts)
- **Next.js API Routes**: For backend endpoints
- **TypeScript**: Type-safe implementation
- **Tailwind CSS**: Responsive styling with dark mode support

### File Structure
```
ai-image-resizer/
├── app/
│   ├── analytics/
│   │   └── page.tsx          # Analytics dashboard page
│   ├── api/
│   │   ├── analytics/
│   │   │   └── route.ts      # Analytics API endpoints
│   │   └── resize/
│   │       └── route.ts      # Modified to track analytics
│   └── page.tsx              # Main page with navigation link
├── lib/
│   └── mongodb.ts            # MongoDB connection utility (optional)
└── analytics-data.json       # Analytics data storage
```

## Usage

### Starting the Application
```bash
cd ai-image-resizer
npm run dev
```

### Accessing the Dashboard
1. Navigate to `http://localhost:3000`
2. Click "📊 View Analytics" button in the header
3. View real-time analytics and metrics

### Processing Images
1. Upload and process images through the main interface
2. Analytics are automatically tracked in the background
3. View updated metrics in the analytics dashboard

## Features

### Responsive Design
- Mobile-friendly layout
- Adaptive charts and tables
- Touch-friendly controls

### Dark Mode Support
- Automatic dark mode detection
- Consistent styling across light and dark themes

### Real-time Updates
- Data refreshes when changing time range
- No page reload required

## Future Enhancements
- Export analytics data to CSV
- More detailed filtering options
- Comparison between time periods
- Performance optimization metrics
- User-specific analytics (with authentication)

## Testing

The analytics system has been tested with:
- ✅ API endpoint functionality
- ✅ Data persistence
- ✅ Chart rendering
- ✅ Responsive design
- ✅ TypeScript compilation
- ✅ Build process

## Notes
- Analytics data is stored locally in `analytics-data.json`
- No external database required
- Lightweight and fast
- Privacy-friendly (no external tracking)
