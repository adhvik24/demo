/**
 * Sample MongoDB Queries for Generated Sample Data
 * 
 * This file contains example queries you can run against the sample data
 * after importing it into MongoDB.
 */

// ============================================================================
// MOVIES COLLECTION QUERIES
// ============================================================================

// 1. Find all movies with high IMDb ratings (8.0+)
db.movies.find(
  { "imdb.rating": { $gte: 8.0 } },
  { title: 1, year: 1, "imdb.rating": 1, genres: 1 }
).sort({ "imdb.rating": -1 });

// 2. Find movies by specific genre
db.movies.find(
  { genres: "Documentary" },
  { title: 1, year: 1, "imdb.rating": 1 }
).sort({ "imdb.rating": -1 });

// 3. Find movies released in a specific year range
db.movies.find(
  { year: { $gte: 2010, $lte: 2020 } },
  { title: 1, year: 1, genres: 1 }
).sort({ year: -1 });

// 4. Find movies with specific actors
db.movies.find(
  { cast: "Tom Hanks" },
  { title: 1, year: 1, cast: 1 }
);

// 5. Find movies by director
db.movies.find(
  { directors: "Christopher Nolan" },
  { title: 1, year: 1, directors: 1, "imdb.rating": 1 }
);

// 6. Find movies with multiple genres
db.movies.find(
  { genres: { $all: ["Action", "Thriller"] } },
  { title: 1, genres: 1, "imdb.rating": 1 }
);

// 7. Find movies with high Metacritic scores
db.movies.find(
  { metacritic: { $gte: 80 } },
  { title: 1, metacritic: 1, "imdb.rating": 1 }
).sort({ metacritic: -1 });

// 8. Find movies with many comments
db.movies.find(
  { num_mflix_comments: { $gte: 30 } },
  { title: 1, num_mflix_comments: 1, "imdb.rating": 1 }
).sort({ num_mflix_comments: -1 });

// 9. Text search (requires text index)
// First create index: db.movies.createIndex({ title: "text", plot: "text" })
db.movies.find(
  { $text: { $search: "love journey" } },
  { title: 1, plot: 1, score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } });

// 10. Find movies with awards
db.movies.find(
  { "awards.wins": { $gte: 5 } },
  { title: 1, "awards.wins": 1, "awards.nominations": 1 }
).sort({ "awards.wins": -1 });

// ============================================================================
// AGGREGATION QUERIES - MOVIES
// ============================================================================

// 1. Average rating by genre
db.movies.aggregate([
  { $unwind: "$genres" },
  { $group: {
    _id: "$genres",
    avgRating: { $avg: "$imdb.rating" },
    avgMetacritic: { $avg: "$metacritic" },
    count: { $sum: 1 }
  }},
  { $sort: { avgRating: -1 } }
]);

// 2. Movies per year
db.movies.aggregate([
  { $group: {
    _id: "$year",
    count: { $sum: 1 },
    avgRating: { $avg: "$imdb.rating" }
  }},
  { $sort: { _id: -1 } }
]);

// 3. Top directors by average rating
db.movies.aggregate([
  { $unwind: "$directors" },
  { $group: {
    _id: "$directors",
    avgRating: { $avg: "$imdb.rating" },
    movieCount: { $sum: 1 }
  }},
  { $match: { movieCount: { $gte: 2 } } },
  { $sort: { avgRating: -1 } },
  { $limit: 10 }
]);

// 4. Top actors by movie count
db.movies.aggregate([
  { $unwind: "$cast" },
  { $group: {
    _id: "$cast",
    movieCount: { $sum: 1 },
    avgRating: { $avg: "$imdb.rating" }
  }},
  { $sort: { movieCount: -1 } },
  { $limit: 10 }
]);

// 5. Runtime statistics by genre
db.movies.aggregate([
  { $unwind: "$genres" },
  { $group: {
    _id: "$genres",
    avgRuntime: { $avg: "$runtime" },
    minRuntime: { $min: "$runtime" },
    maxRuntime: { $max: "$runtime" }
  }},
  { $sort: { avgRuntime: -1 } }
]);

// 6. Movies by rating category
db.movies.aggregate([
  { $group: {
    _id: "$rated",
    count: { $sum: 1 },
    avgRating: { $avg: "$imdb.rating" }
  }},
  { $sort: { count: -1 } }
]);

// 7. Top countries by movie production
db.movies.aggregate([
  { $unwind: "$countries" },
  { $group: {
    _id: "$countries",
    count: { $sum: 1 },
    avgRating: { $avg: "$imdb.rating" }
  }},
  { $sort: { count: -1 } },
  { $limit: 10 }
]);

// ============================================================================
// COMMENTS COLLECTION QUERIES
// ============================================================================

// 1. Find all comments for a specific movie
db.comments.find(
  { movie_id: "6931ba8c603803a839c0cb52" },
  { name: 1, text: 1, date: 1 }
).sort({ date: -1 });

// 2. Find comments by a specific user
db.comments.find(
  { email: "jon_snow@gameofthron.es" },
  { movie_id: 1, text: 1, date: 1 }
).sort({ date: -1 });

// 3. Recent comments
db.comments.find(
  {},
  { name: 1, text: 1, date: 1 }
).sort({ date: -1 }).limit(10);

// 4. Comments in a date range
db.comments.find(
  { date: { 
    $gte: new ISODate("2020-01-01"),
    $lte: new ISODate("2024-12-31")
  }},
  { name: 1, text: 1, date: 1 }
).sort({ date: -1 });

// ============================================================================
// AGGREGATION QUERIES - COMMENTS
// ============================================================================

// 1. Top commenters
db.comments.aggregate([
  { $group: {
    _id: "$email",
    name: { $first: "$name" },
    commentCount: { $sum: 1 }
  }},
  { $sort: { commentCount: -1 } },
  { $limit: 10 }
]);

// 2. Comments per movie
db.comments.aggregate([
  { $group: {
    _id: "$movie_id",
    commentCount: { $sum: 1 }
  }},
  { $sort: { commentCount: -1 } },
  { $limit: 10 }
]);

// 3. Comments by year
db.comments.aggregate([
  { $project: {
    year: { $year: { $toDate: "$date" } }
  }},
  { $group: {
    _id: "$year",
    count: { $sum: 1 }
  }},
  { $sort: { _id: -1 } }
]);

// 4. Join comments with movies
db.comments.aggregate([
  { $lookup: {
    from: "movies",
    localField: "movie_id",
    foreignField: "_id",
    as: "movie"
  }},
  { $unwind: "$movie" },
  { $project: {
    name: 1,
    text: 1,
    date: 1,
    movieTitle: "$movie.title",
    movieRating: "$movie.imdb.rating"
  }},
  { $limit: 10 }
]);

// ============================================================================
// USERS COLLECTION QUERIES
// ============================================================================

// 1. Find user by email
db.users.findOne({ email: "jon_snow@gameofthron.es" });

// 2. List all users
db.users.find({}, { name: 1, email: 1 }).sort({ name: 1 });

// 3. Count total users
db.users.countDocuments();

// ============================================================================
// THEATERS COLLECTION QUERIES
// ============================================================================

// 1. Find theaters in a specific state
db.theaters.find(
  { "location.address.state": "CA" },
  { theaterId: 1, "location.address": 1 }
).sort({ theaterId: 1 });

// 2. Find theaters in a specific city
db.theaters.find(
  { "location.address.city": "Los Angeles" },
  { theaterId: 1, "location.address": 1 }
);

// 3. Count theaters by state
db.theaters.aggregate([
  { $group: {
    _id: "$location.address.state",
    count: { $sum: 1 }
  }},
  { $sort: { count: -1 } }
]);

// 4. Geospatial query - theaters near a location
// First create index: db.theaters.createIndex({ "location.geo": "2dsphere" })
db.theaters.find({
  "location.geo": {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [-118.2437, 34.0522]  // Los Angeles coordinates
      },
      $maxDistance: 50000  // 50km radius
    }
  }
});

// 5. Find theaters within a polygon (e.g., California)
db.theaters.find({
  "location.geo": {
    $geoWithin: {
      $geometry: {
        type: "Polygon",
        coordinates: [[
          [-124.0, 32.0],
          [-114.0, 32.0],
          [-114.0, 42.0],
          [-124.0, 42.0],
          [-124.0, 32.0]
        ]]
      }
    }
  }
});

// ============================================================================
// PRODUCTS COLLECTION QUERIES
// ============================================================================

// 1. Find products by category
db.products.find(
  { category: "electronics" },
  { title: 1, price: 1, rating: 1, stock: 1 }
).sort({ price: -1 });

// 2. Find products in price range
db.products.find(
  { price: { $gte: 50, $lte: 150 } },
  { title: 1, price: 1, category: 1 }
).sort({ price: 1 });

// 3. Find highly rated products
db.products.find(
  { rating: { $gte: 4.0 } },
  { title: 1, rating: 1, price: 1, category: 1 }
).sort({ rating: -1 });

// 4. Find products in stock
db.products.find(
  { stock: { $gt: 0 } },
  { title: 1, stock: 1, price: 1 }
).sort({ stock: -1 });

// 5. Find out of stock products
db.products.find(
  { stock: 0 },
  { title: 1, category: 1, price: 1 }
);

// 6. Search products by title
db.products.find(
  { title: /Smart/i },
  { title: 1, price: 1, category: 1 }
);

// 7. Find products with specific tags
db.products.find(
  { tags: "electronics" },
  { title: 1, tags: 1, price: 1 }
);

// ============================================================================
// AGGREGATION QUERIES - PRODUCTS
// ============================================================================

// 1. Products by category with statistics
db.products.aggregate([
  { $group: {
    _id: "$category",
    count: { $sum: 1 },
    avgPrice: { $avg: "$price" },
    avgRating: { $avg: "$rating" },
    totalStock: { $sum: "$stock" },
    minPrice: { $min: "$price" },
    maxPrice: { $max: "$price" }
  }},
  { $sort: { count: -1 } }
]);

// 2. Price ranges
db.products.aggregate([
  { $bucket: {
    groupBy: "$price",
    boundaries: [0, 50, 100, 150, 200, 300],
    default: "300+",
    output: {
      count: { $sum: 1 },
      avgRating: { $avg: "$rating" }
    }
  }}
]);

// 3. Rating distribution
db.products.aggregate([
  { $bucket: {
    groupBy: "$rating",
    boundaries: [0, 1, 2, 3, 4, 5],
    default: "5+",
    output: {
      count: { $sum: 1 },
      avgPrice: { $avg: "$price" }
    }
  }}
]);

// 4. Top 10 most expensive products
db.products.aggregate([
  { $sort: { price: -1 } },
  { $limit: 10 },
  { $project: {
    title: 1,
    price: 1,
    category: 1,
    rating: 1
  }}
]);

// 5. Top 10 highest rated products
db.products.aggregate([
  { $sort: { rating: -1, price: -1 } },
  { $limit: 10 },
  { $project: {
    title: 1,
    rating: 1,
    price: 1,
    category: 1
  }}
]);

// 6. Products with low stock (inventory alert)
db.products.aggregate([
  { $match: { stock: { $lt: 50, $gt: 0 } } },
  { $sort: { stock: 1 } },
  { $project: {
    title: 1,
    stock: 1,
    category: 1,
    price: 1
  }}
]);

// 7. Total inventory value by category
db.products.aggregate([
  { $group: {
    _id: "$category",
    totalValue: { $sum: { $multiply: ["$price", "$stock"] } },
    totalStock: { $sum: "$stock" },
    productCount: { $sum: 1 }
  }},
  { $sort: { totalValue: -1 } }
]);

// ============================================================================
// COMPLEX CROSS-COLLECTION QUERIES
// ============================================================================

// 1. Movies with their comment counts
db.movies.aggregate([
  { $lookup: {
    from: "comments",
    localField: "_id",
    foreignField: "movie_id",
    as: "comments"
  }},
  { $project: {
    title: 1,
    year: 1,
    "imdb.rating": 1,
    commentCount: { $size: "$comments" }
  }},
  { $sort: { commentCount: -1 } },
  { $limit: 10 }
]);

// 2. User activity - comments per user with movie details
db.users.aggregate([
  { $lookup: {
    from: "comments",
    localField: "email",
    foreignField: "email",
    as: "comments"
  }},
  { $project: {
    name: 1,
    email: 1,
    commentCount: { $size: "$comments" }
  }},
  { $sort: { commentCount: -1 } }
]);

// 3. Movies by genre with average ratings and comment counts
db.movies.aggregate([
  { $unwind: "$genres" },
  { $lookup: {
    from: "comments",
    localField: "_id",
    foreignField: "movie_id",
    as: "comments"
  }},
  { $group: {
    _id: "$genres",
    movieCount: { $sum: 1 },
    avgRating: { $avg: "$imdb.rating" },
    totalComments: { $sum: { $size: "$comments" } }
  }},
  { $sort: { movieCount: -1 } }
]);

// ============================================================================
// INDEXES TO CREATE FOR BETTER PERFORMANCE
// ============================================================================

// Movies collection
db.movies.createIndex({ "imdb.rating": -1 });
db.movies.createIndex({ year: 1 });
db.movies.createIndex({ genres: 1 });
db.movies.createIndex({ cast: 1 });
db.movies.createIndex({ directors: 1 });
db.movies.createIndex({ title: "text", plot: "text", fullplot: "text" });

// Comments collection
db.comments.createIndex({ movie_id: 1 });
db.comments.createIndex({ email: 1 });
db.comments.createIndex({ date: -1 });

// Users collection
db.users.createIndex({ email: 1 }, { unique: true });

// Theaters collection
db.theaters.createIndex({ "location.geo": "2dsphere" });
db.theaters.createIndex({ "location.address.state": 1 });
db.theaters.createIndex({ "location.address.city": 1 });

// Products collection
db.products.createIndex({ category: 1 });
db.products.createIndex({ price: 1 });
db.products.createIndex({ rating: -1 });
db.products.createIndex({ stock: 1 });
db.products.createIndex({ tags: 1 });
db.products.createIndex({ title: "text", description: "text" });

console.log("Sample queries loaded! Use these queries to explore your sample data.");
