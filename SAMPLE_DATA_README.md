# Sample Data Generation - Based on Upstash Database Analysis

## Overview

This sample dataset was generated based on the comprehensive analysis of the Upstash MongoDB database. It replicates the structure and characteristics of the original database while providing realistic test data for development and testing purposes.

## Generated Files

### Complete Dataset
- **`sample_data_complete.json`** (181 KB) - All collections in a single file

### Individual Collections

#### Movie Streaming Platform (sample_mflix)
1. **`sample_movies.json`** (75 KB) - 50 movie documents
2. **`sample_comments.json`** (27 KB) - 100 user comments
3. **`sample_users.json`** (4 KB) - 20 user accounts
4. **`sample_theaters.json`** (12 KB) - 30 theater locations

#### E-commerce Platform (test.products)
5. **`sample_products.json`** (40 KB) - 100 product documents

## Data Statistics

### Total Documents: 300

| Collection | Documents | Description |
|------------|-----------|-------------|
| Movies | 50 | Movie catalog with metadata |
| Comments | 100 | User reviews and comments |
| Users | 20 | User accounts (Game of Thrones themed) |
| Theaters | 30 | Theater locations across US |
| Products | 100 | E-commerce product catalog |

## Data Characteristics

### Movies Collection

**Schema Fields (22 total):**
- Basic Info: `_id`, `title`, `plot`, `fullplot`, `year`, `released`, `runtime`, `rated`, `type`, `poster`
- People: `cast`, `directors`, `writers`
- Classification: `genres`, `languages`, `countries`
- Ratings: `imdb`, `tomatoes`, `metacritic`
- Engagement: `num_mflix_comments`, `awards`, `lastupdated`

**Genre Distribution:**
- Documentary: 11 movies
- War: 10 movies
- Comedy: 10 movies
- Romance: 7 movies
- Family: 7 movies
- Others: Drama, Horror, Thriller, Action, etc.

**Sample Movie Titles:**
- "Tales of the Unexpected"
- "The Last Horizon"
- "Midnight in Paris"
- "The Silent Echo"
- "City of Dreams"

**Cast & Crew:**
- Actors: Emma Stone, Ryan Gosling, Jennifer Lawrence, Chris Pratt, Tom Hanks, Meryl Streep, etc.
- Directors: Christopher Nolan, Martin Scorsese, Quentin Tarantino, Steven Spielberg, etc.

**Ratings:**
- IMDb ratings: 5.0 - 9.5
- Rotten Tomatoes scores included
- Metacritic scores: 40 - 95

### Comments Collection

**Schema Fields (6 total):**
- `_id`, `name`, `email`, `movie_id`, `text`, `date`

**Characteristics:**
- User names: Game of Thrones characters (Jon Snow, Daenerys Targaryen, etc.)
- Email format: `character_name@gameofthron.es`
- Date range: 2015 - 2024
- Realistic comment text with varied sentiments

**Sample Comments:**
- "Absolutely loved this movie! The cinematography was stunning."
- "Great performances by the entire cast. Highly recommended!"
- "One of the best films I've seen this year. Masterpiece!"

### Users Collection

**Schema Fields (4 total):**
- `_id`, `name`, `email`, `password`

**Characteristics:**
- 20 Game of Thrones themed users
- Bcrypt-hashed passwords (SHA256-based for demo)
- Email format: `character_name@gameofthron.es`

**Sample Users:**
- Jon Snow (jon_snow@gameofthron.es)
- Daenerys Targaryen (daenerys_targaryen@gameofthron.es)
- Tyrion Lannister (tyrion_lannister@gameofthron.es)

### Theaters Collection

**Schema Fields (3 total):**
- `_id`, `theaterId`, `location` (with address and geo coordinates)

**Characteristics:**
- 30 theaters across US states
- GeoJSON format for location data
- Real US cities and states
- Coordinates within US geographic bounds

**State Distribution:**
- California, Texas, Florida, New York, Illinois, etc.

**Address Format:**
```json
{
  "street1": "340 W Market",
  "street2": null,
  "city": "Bloomington",
  "state": "MN",
  "zipcode": "55425"
}
```

**Geo Format (GeoJSON):**
```json
{
  "type": "Point",
  "coordinates": [-93.24565, 44.85466]
}
```

### Products Collection

**Schema Fields (9 total):**
- `_id`, `title`, `description`, `price`, `category`, `rating`, `stock`, `tags`, `createdAt`

**Category Distribution:**
- Books: 22 products
- Clothing: 21 products
- Sports: 18 products
- Beauty: 15 products
- Home: 14 products
- Electronics: 10 products

**Price Statistics:**
- Average: $155.84
- Min: $21.41
- Max: $293.71

**Sample Products:**
- "The Art of Leadership" (Books, $86.12)
- "Digital Speaker" (Electronics, $149.91)
- "Premium Jacket" (Clothing, $89.99)
- "Pro Yoga Mat" (Sports, $45.50)

**Product Naming Convention:**
- Format: `[Prefix] [Item]`
- Electronics: Smart, Wireless, Digital, HD, Pro, Ultra
- Clothing: Premium, Classic, Modern, Vintage, Designer
- Books: The Art of, Guide to, Mastering, Introduction to

## Usage Examples

### Import into MongoDB

```bash
# Import movies
mongoimport --db sample_mflix --collection movies --file sample_movies.json --jsonArray

# Import comments
mongoimport --db sample_mflix --collection comments --file sample_comments.json --jsonArray

# Import users
mongoimport --db sample_mflix --collection users --file sample_users.json --jsonArray

# Import theaters
mongoimport --db sample_mflix --collection theaters --file sample_theaters.json --jsonArray

# Import products
mongoimport --db test --collection products --file sample_products.json --jsonArray
```

### Load in Python

```python
import json

# Load all data
with open('sample_data_complete.json', 'r') as f:
    data = json.load(f)
    movies = data['sample_mflix']['movies']
    comments = data['sample_mflix']['comments']
    users = data['sample_mflix']['users']
    theaters = data['sample_mflix']['theaters']
    products = data['test']['products']

# Or load individual collections
with open('sample_movies.json', 'r') as f:
    movies = json.load(f)
```

### Load in Node.js

```javascript
const fs = require('fs');

// Load all data
const data = JSON.parse(fs.readFileSync('sample_data_complete.json', 'utf8'));
const movies = data.sample_mflix.movies;
const comments = data.sample_mflix.comments;
const users = data.sample_mflix.users;
const theaters = data.sample_mflix.theaters;
const products = data.test.products;

// Or load individual collections
const movies = JSON.parse(fs.readFileSync('sample_movies.json', 'utf8'));
```

## Data Relationships

### Movie ↔ Comments
- Comments reference movies via `movie_id` field
- Each movie can have 0-50 comments
- Comments include user email and name

### Users ↔ Comments
- Comments include user `name` and `email`
- Users can be matched by email address
- Enables user activity tracking

### Movies ↔ Theaters
- No direct relationship in schema
- Can be linked via geospatial queries
- Theaters provide location-based movie availability

## Query Examples

### MongoDB Queries

```javascript
// Find highly rated movies
db.movies.find({ "imdb.rating": { $gte: 8.0 } })

// Find comments for a specific movie
db.comments.find({ "movie_id": "6931ba8c603803a839c0cb52" })

// Find theaters in California
db.theaters.find({ "location.address.state": "CA" })

// Find products under $50
db.products.find({ "price": { $lt: 50 } })

// Find movies by genre
db.movies.find({ "genres": "Documentary" })

// Find products by category with high ratings
db.products.find({ 
  "category": "electronics", 
  "rating": { $gte: 4.0 } 
})

// Geospatial query - theaters near a location
db.theaters.find({
  "location.geo": {
    $near: {
      $geometry: { type: "Point", coordinates: [-118.2437, 34.0522] },
      $maxDistance: 50000  // 50km
    }
  }
})
```

### Aggregation Examples

```javascript
// Average rating by genre
db.movies.aggregate([
  { $unwind: "$genres" },
  { $group: {
    _id: "$genres",
    avgRating: { $avg: "$imdb.rating" },
    count: { $sum: 1 }
  }},
  { $sort: { avgRating: -1 } }
])

// Top commenters
db.comments.aggregate([
  { $group: {
    _id: "$email",
    commentCount: { $sum: 1 }
  }},
  { $sort: { commentCount: -1 } },
  { $limit: 10 }
])

// Products by category with stats
db.products.aggregate([
  { $group: {
    _id: "$category",
    avgPrice: { $avg: "$price" },
    avgRating: { $avg: "$rating" },
    totalStock: { $sum: "$stock" },
    count: { $sum: 1 }
  }},
  { $sort: { count: -1 } }
])
```

## Data Quality Features

✅ **Realistic Data:**
- Proper date formats (ISO 8601)
- Valid email addresses
- Realistic names and titles
- Appropriate value ranges

✅ **Schema Compliance:**
- Matches original Upstash database structure
- All required fields included
- Proper data types

✅ **Security:**
- Passwords are hashed (bcrypt-style)
- No sensitive real data
- Test email domains used

✅ **Relationships:**
- Valid ObjectId references
- Consistent foreign keys
- Logical data connections

## Use Cases

### Development & Testing
- API endpoint testing
- Database query optimization
- Application feature development
- Integration testing

### Learning & Training
- MongoDB query practice
- Aggregation pipeline examples
- Geospatial query learning
- Schema design study

### Prototyping
- Movie streaming app prototype
- E-commerce platform demo
- Review system implementation
- Location-based services

### Data Analysis
- Genre popularity analysis
- Price optimization studies
- User engagement metrics
- Geographic distribution analysis

## Generation Script

The data was generated using `generate_sample_data.py`, which includes:
- Configurable data counts
- Realistic random data generation
- Proper MongoDB ObjectId generation
- Bcrypt-style password hashing
- GeoJSON coordinate generation
- Relationship maintenance

To regenerate or modify the data:

```bash
python3 generate_sample_data.py
```

## Notes

- All data is synthetic and for testing purposes only
- Email addresses use fake domains (@gameofthron.es, @fakegmail.com)
- Passwords are hashed but use simple test passwords
- ObjectIds are generated to look like MongoDB ObjectIds
- Dates are randomized within realistic ranges
- Geographic coordinates are within US bounds

## License

This sample data is provided for educational and testing purposes. Feel free to use, modify, and distribute as needed.

---

**Generated:** December 4, 2025  
**Based on:** Upstash MongoDB Database Analysis  
**Total Documents:** 300  
**Total Size:** ~181 KB (JSON format)
