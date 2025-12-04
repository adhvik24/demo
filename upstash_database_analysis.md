# Upstash MongoDB Database Analysis

**Analysis Date:** December 4, 2025  
**Database Type:** MongoDB (Upstash-hosted)  
**Access Mode:** Read-only

---

## Executive Summary

The Upstash MongoDB instance contains **4 databases** with a total storage size of approximately **17.2 GB**. The primary database is `sample_mflix`, a movie streaming application dataset with 67,661 documents across 6 collections. Additionally, there's a `test` database with product data containing 1,000 documents.

---

## Database Overview

| Database | Collections | Total Objects | Data Size | Storage Size | Indexes |
|----------|-------------|---------------|-----------|--------------|---------|
| **sample_mflix** | 6 | 67,661 | 96.4 MB | 98.3 MB | 10 |
| **test** | 1 | 1,000 | 211 KB | 112 KB | 1 |
| **admin** | - | - | 348 KB | 348 KB | - |
| **local** | - | - | 16.7 GB | 16.7 GB | - |

---

## Database 1: sample_mflix (Movie Streaming Platform)

### Overview
A comprehensive movie database containing information about movies, user comments, theaters, and user accounts. This appears to be a sample dataset for a Netflix-like streaming platform.

### Collections Detail

#### 1. **movies** Collection
- **Document Count:** 21,349
- **Purpose:** Core movie catalog with detailed metadata
- **Indexes:** 
  - `_id_` (default)
  - `cast_text_fullplot_text_genres_text_title_text` (full-text search index)

**Schema Fields (22 total):**
- `_id` (ObjectId) - Unique identifier
- `title` (String) - Movie title
- `plot` (String) - Short plot summary
- `fullplot` (String) - Detailed plot description
- `genres` (Array[String]) - Movie genres
- `runtime` (Number) - Duration in minutes
- `cast` (Array[String]) - Actor names
- `directors` (Array[String]) - Director names
- `writers` (Array[String]) - Writer names
- `year` (Number) - Release year
- `released` (Date) - Release date
- `rated` (String) - MPAA rating (G, PG, R, etc.)
- `languages` (Array[String]) - Available languages
- `countries` (Array[String]) - Production countries
- `type` (String) - Content type (movie, series)
- `poster` (String) - Poster image URL
- `num_mflix_comments` (Number) - Comment count
- `lastupdated` (String) - Last update timestamp
- `imdb` (Document) - IMDb ratings and votes
  - `rating` (Number)
  - `votes` (Number)
  - `id` (Number)
- `tomatoes` (Document) - Rotten Tomatoes data
  - `viewer` (Document) - Viewer ratings
  - `critic` (Document) - Critic ratings
  - `fresh` (Number)
  - `rotten` (Number)
  - `lastUpdated` (Date)
- `awards` (Document) - Award information
  - `wins` (Number)
  - `nominations` (Number)
  - `text` (String)
- `metacritic` (Number) - Metacritic score

**Sample Movie:**
```json
{
  "_id": "573a1390f29313caabcd42e8",
  "title": "The Great Train Robbery",
  "year": 1903,
  "runtime": 11,
  "genres": ["Short", "Western"],
  "rated": "TV-G",
  "imdb": {"rating": 7.4, "votes": 9847},
  "plot": "A group of bandits stage a brazen train hold-up..."
}
```

**Genre Distribution (Top 10):**
| Genre | Count | Avg Rating |
|-------|-------|------------|
| Drama | 12,385 | 6.80 |
| Comedy | 6,532 | 6.45 |
| Romance | 3,318 | 6.66 |
| Crime | 2,457 | 6.69 |
| Thriller | 2,454 | 6.30 |
| Action | 2,381 | 6.35 |
| Adventure | 1,900 | 6.49 |
| Documentary | 1,834 | 7.37 ⭐ |
| Horror | 1,470 | 5.78 |
| Biography | 1,269 | 7.09 |

**Key Insights:**
- Documentaries have the highest average rating (7.37)
- Horror movies have the lowest average rating (5.78)
- Drama is the most common genre (12,385 movies)
- Dataset spans from 1903 to 2014+

---

#### 2. **comments** Collection
- **Document Count:** 41,079
- **Purpose:** User comments on movies
- **Indexes:** `_id_` only

**Schema Fields (6 total):**
- `_id` (ObjectId)
- `name` (String) - Commenter name
- `email` (String) - Commenter email
- `movie_id` (ObjectId) - Reference to movies collection
- `text` (String) - Comment content
- `date` (Date) - Comment timestamp

**Sample Comment:**
```json
{
  "_id": "5a9427648b0beebeb69579e7",
  "name": "Mercedes Tyler",
  "email": "mercedes_tyler@fakegmail.com",
  "movie_id": "573a1390f29313caabcd4323",
  "text": "Eius veritatis vero facilis quaerat fuga temporibus...",
  "date": "2002-08-18T04:56:07Z"
}
```

**Top Commenters:**
| Email | Comment Count |
|-------|---------------|
| roger_ashton-griffiths@gameofthron.es | 277 |
| ron_donachie@gameofthron.es | 260 |
| jonathan_pryce@gameofthron.es | 260 |
| nathalie_emmanuel@gameofthron.es | 258 |
| robert_jordan@fakegmail.com | 257 |

**Key Insights:**
- Many commenters use Game of Thrones actor emails (test data)
- Comments span from 1975 to recent dates
- Average ~1.9 comments per movie

---

#### 3. **users** Collection
- **Document Count:** 185
- **Purpose:** User account information
- **Indexes:** `_id_` only

**Schema Fields (4 total):**
- `_id` (ObjectId)
- `name` (String) - User full name
- `email` (String) - User email (unique identifier)
- `password` (String) - Bcrypt hashed password

**Sample User:**
```json
{
  "_id": "59b99db4cfa9a34dcd7885b6",
  "name": "Ned Stark",
  "email": "sean_bean@gameofthron.es",
  "password": "$2b$12$UREFwsRUoyF0CRqGNK0LzO0HM/jLhgUCNNIJ9RJAqMUQ74crlJ1Vu"
}
```

**Key Insights:**
- Passwords are properly hashed using bcrypt ($2b$12$)
- Test data uses Game of Thrones character names
- Small user base (185 users)

---

#### 4. **theaters** Collection
- **Document Count:** 1,564
- **Purpose:** Theater location information
- **Indexes:** `_id_` only

**Schema Fields (3 total):**
- `_id` (ObjectId)
- `theaterId` (Number) - Unique theater identifier
- `location` (Document)
  - `address` (Document)
    - `street1` (String)
    - `street2` (String/Null)
    - `city` (String)
    - `state` (String)
    - `zipcode` (String)
  - `geo` (Document) - GeoJSON format
    - `type` (String) - "Point"
    - `coordinates` (Array[Number]) - [longitude, latitude]

**Sample Theater:**
```json
{
  "_id": "59a47286cfa9a3a73e51e72c",
  "theaterId": 1000,
  "location": {
    "address": {
      "street1": "340 W Market",
      "city": "Bloomington",
      "state": "MN",
      "zipcode": "55425"
    },
    "geo": {
      "type": "Point",
      "coordinates": [-93.24565, 44.85466]
    }
  }
}
```

**Theater Distribution by State (Top 10):**
| State | Theater Count |
|-------|---------------|
| CA | 169 |
| TX | 160 |
| FL | 111 |
| NY | 81 |
| IL | 70 |
| PA | 55 |
| OH | 52 |
| MI | 45 |
| VA | 45 |
| GA | 45 |

**Key Insights:**
- GeoJSON format enables geospatial queries
- California has the most theaters (169)
- Covers theaters across the United States

---

#### 5. **sessions** Collection
- **Document Count:** 1
- **Purpose:** User session management
- **Note:** Minimal data, likely for authentication tokens

---

#### 6. **embedded_movies** Collection
- **Document Count:** 3,483
- **Purpose:** Alternative movie data structure (possibly denormalized)
- **Note:** Appears to be a subset of the main movies collection

---

## Database 2: test (E-commerce Products)

### Overview
A test database containing product catalog data for an e-commerce application.

### Collections Detail

#### **products** Collection
- **Document Count:** 1,000
- **Purpose:** Product catalog with pricing and inventory
- **Indexes:** `_id_` only

**Schema Fields (9 total):**
- `_id` (ObjectId)
- `title` (String) - Product name
- `description` (String) - Product description
- `price` (Number) - Product price
- `category` (String) - Product category
- `rating` (Number) - Customer rating (0-5)
- `stock` (Number) - Available inventory
- `tags` (Array[String]) - Product tags
- `createdAt` (Date) - Creation timestamp

**Sample Product:**
```json
{
  "_id": "693081fc1abce39aff79fefe",
  "title": "Product 1",
  "description": "Sample description for product 1",
  "price": 170.73,
  "category": "beauty",
  "rating": 1.5,
  "stock": 131,
  "tags": ["sample", "seed"],
  "createdAt": "2025-12-03T18:31:24.683Z"
}
```

**Category Analysis:**
| Category | Products | Avg Price | Avg Rating | Total Stock |
|----------|----------|-----------|------------|-------------|
| Home | 184 | $103.77 | 2.59 | 16,381 |
| Beauty | 168 | $102.26 | 2.54 | 16,710 |
| Clothing | 165 | $99.74 | 2.47 | 15,902 |
| Books | 162 | $102.88 | 2.61 | 14,852 |
| Electronics | 161 | $103.51 | 2.59 | 16,173 |
| Sports | 160 | $104.87 | 2.51 | 15,233 |

**Key Insights:**
- Well-balanced distribution across 6 categories
- Average price: ~$102.84
- Average rating: ~2.55 (out of 5)
- Total inventory: 95,251 units
- All products created on December 3, 2025 (seed data)
- All products tagged with "sample" and "seed"

---

## Database 3: admin

System administration database. Contains MongoDB internal metadata and configuration.

---

## Database 4: local

Local database used by MongoDB for replication and internal operations. Size: 16.7 GB (largest database).

---

## Key Findings & Recommendations

### Data Quality
✅ **Strengths:**
- Well-structured schemas with consistent field types
- Proper password hashing (bcrypt) in users collection
- GeoJSON format for location data enables spatial queries
- Rich metadata in movies collection (IMDb, Rotten Tomatoes, awards)

⚠️ **Areas for Improvement:**
- Missing indexes on frequently queried fields (e.g., `movie_id` in comments, `email` in users)
- No foreign key constraints (MongoDB limitation, but could use validation)
- Some data quality issues in year field (e.g., "2014è", "2006è2012")

### Performance Optimization Recommendations

1. **Add Indexes:**
   ```javascript
   // Comments collection
   db.comments.createIndex({ "movie_id": 1 })
   db.comments.createIndex({ "email": 1 })
   db.comments.createIndex({ "date": -1 })
   
   // Users collection
   db.users.createIndex({ "email": 1 }, { unique: true })
   
   // Movies collection
   db.movies.createIndex({ "year": 1 })
   db.movies.createIndex({ "genres": 1 })
   db.movies.createIndex({ "imdb.rating": -1 })
   
   // Theaters collection
   db.theaters.createIndex({ "location.geo": "2dsphere" })
   
   // Products collection
   db.products.createIndex({ "category": 1 })
   db.products.createIndex({ "price": 1 })
   db.products.createIndex({ "rating": -1 })
   ```

2. **Data Cleanup:**
   - Fix malformed year values in movies collection
   - Standardize date formats
   - Remove or archive the `sessions` collection if unused

3. **Schema Validation:**
   - Implement MongoDB schema validation rules
   - Ensure email format validation
   - Add required field constraints

### Use Cases

**sample_mflix Database:**
- Movie recommendation engine
- User review and rating system
- Theater location finder (geospatial queries)
- Content management system for streaming platform
- Analytics on movie trends and user engagement

**test.products Database:**
- E-commerce product catalog
- Inventory management
- Price comparison and analytics
- Product recommendation system
- Category-based filtering and search

### Security Considerations

🔒 **Current Security:**
- Passwords are bcrypt-hashed (good)
- Read-only access configured (good for analysis)

⚠️ **Recommendations:**
- Implement field-level encryption for sensitive data
- Add rate limiting for comment submissions
- Implement email verification for user accounts
- Consider masking or removing test email addresses in production

---

## Statistics Summary

### Overall Database Metrics
- **Total Databases:** 4
- **Total Collections:** 7 (excluding admin/local)
- **Total Documents:** 68,661
- **Total Storage:** ~17.2 GB
- **Total Indexes:** 11

### Collection Size Breakdown
| Collection | Documents | Percentage |
|------------|-----------|------------|
| Comments | 41,079 | 59.8% |
| Movies | 21,349 | 31.1% |
| Embedded Movies | 3,483 | 5.1% |
| Theaters | 1,564 | 2.3% |
| Products | 1,000 | 1.5% |
| Users | 185 | 0.3% |
| Sessions | 1 | 0.0% |

---

## Conclusion

The Upstash MongoDB instance is well-structured and contains rich, production-ready sample data for both a movie streaming platform and an e-commerce application. The `sample_mflix` database is particularly comprehensive with detailed movie metadata, user interactions, and geospatial theater data.

**Primary Strengths:**
- Clean, consistent data structures
- Rich metadata and relationships
- Proper security practices (password hashing)
- Geospatial capabilities

**Recommended Next Steps:**
1. Add strategic indexes for query performance
2. Clean up data quality issues (year field)
3. Implement schema validation
4. Consider archiving or removing unused collections
5. Monitor the large `local` database (16.7 GB)

This database is suitable for development, testing, and demonstration purposes for movie streaming and e-commerce applications.
