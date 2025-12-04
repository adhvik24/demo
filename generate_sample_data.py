#!/usr/bin/env python3
"""
Generate sample data based on Upstash MongoDB analysis
Creates realistic sample datasets for:
1. Movie streaming platform (sample_mflix)
2. E-commerce products (test.products)
"""

import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
import hashlib

# Set random seed for reproducibility
random.seed(42)

# ============================================================================
# MOVIE STREAMING PLATFORM DATA
# ============================================================================

# Movie data
GENRES = ["Drama", "Comedy", "Romance", "Crime", "Thriller", "Action", 
          "Adventure", "Documentary", "Horror", "Biography", "Sci-Fi", 
          "Fantasy", "Mystery", "Animation", "Family", "Musical", "War", "Western"]

RATINGS = ["G", "PG", "PG-13", "R", "NC-17", "TV-G", "TV-PG", "TV-14", "TV-MA", "UNRATED"]

MOVIE_TITLES = [
    "The Last Horizon", "Midnight in Paris", "The Silent Echo", "Breaking Dawn",
    "City of Dreams", "The Lost Kingdom", "Shadows of Tomorrow", "The Final Act",
    "Whispers in the Dark", "The Golden Age", "Beyond the Stars", "The Hidden Truth",
    "Echoes of War", "The Great Escape", "Dancing with Destiny", "The Perfect Storm",
    "Voices from the Past", "The Forgotten Hero", "Chasing Shadows", "The Last Stand",
    "Dreams of Tomorrow", "The Secret Garden", "Midnight Express", "The Rising Sun",
    "Tales of the Unexpected", "The Dark Knight Returns", "The Lost City",
    "Beneath the Surface", "The Final Countdown", "Whispers of Love"
]

ACTORS = [
    "Emma Stone", "Ryan Gosling", "Jennifer Lawrence", "Chris Pratt",
    "Scarlett Johansson", "Tom Hanks", "Meryl Streep", "Leonardo DiCaprio",
    "Natalie Portman", "Brad Pitt", "Cate Blanchett", "Robert Downey Jr.",
    "Anne Hathaway", "Christian Bale", "Amy Adams", "Matt Damon"
]

DIRECTORS = [
    "Christopher Nolan", "Martin Scorsese", "Quentin Tarantino", "Steven Spielberg",
    "Greta Gerwig", "Denis Villeneuve", "Wes Anderson", "Ridley Scott",
    "James Cameron", "David Fincher", "Kathryn Bigelow", "Ava DuVernay"
]

COUNTRIES = ["USA", "UK", "France", "Germany", "Canada", "Australia", "Japan", "South Korea", "Italy", "Spain"]

LANGUAGES = ["English", "French", "Spanish", "German", "Japanese", "Korean", "Italian", "Mandarin"]

# User names (Game of Thrones themed)
USER_NAMES = [
    "Jon Snow", "Daenerys Targaryen", "Tyrion Lannister", "Arya Stark",
    "Sansa Stark", "Cersei Lannister", "Jaime Lannister", "Ned Stark",
    "Catelyn Stark", "Robb Stark", "Bran Stark", "Theon Greyjoy",
    "Jorah Mormont", "Samwell Tarly", "Brienne of Tarth", "Petyr Baelish",
    "Varys", "Melisandre", "Davos Seaworth", "Margaery Tyrell"
]

# US States for theaters
US_STATES = {
    "CA": "California", "TX": "Texas", "FL": "Florida", "NY": "New York",
    "IL": "Illinois", "PA": "Pennsylvania", "OH": "Ohio", "MI": "Michigan",
    "VA": "Virginia", "GA": "Georgia", "NC": "North Carolina", "AZ": "Arizona",
    "WA": "Washington", "MA": "Massachusetts", "CO": "Colorado", "OR": "Oregon"
}

CITIES = {
    "CA": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "San Jose"],
    "TX": ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth"],
    "FL": ["Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale"],
    "NY": ["New York", "Buffalo", "Rochester", "Albany", "Syracuse"],
    "IL": ["Chicago", "Aurora", "Naperville", "Joliet", "Rockford"]
}

# ============================================================================
# E-COMMERCE DATA
# ============================================================================

CATEGORIES = ["Electronics", "Clothing", "Home", "Beauty", "Books", "Sports"]

PRODUCT_PREFIXES = {
    "Electronics": ["Smart", "Wireless", "Digital", "HD", "Pro", "Ultra"],
    "Clothing": ["Premium", "Classic", "Modern", "Vintage", "Designer", "Casual"],
    "Home": ["Luxury", "Comfort", "Essential", "Deluxe", "Premium", "Modern"],
    "Beauty": ["Natural", "Organic", "Professional", "Radiant", "Pure", "Glow"],
    "Books": ["The Art of", "Guide to", "Mastering", "Introduction to", "Complete", "Essential"],
    "Sports": ["Pro", "Elite", "Performance", "Training", "Advanced", "Professional"]
}

PRODUCT_ITEMS = {
    "Electronics": ["Headphones", "Speaker", "Camera", "Monitor", "Keyboard", "Mouse", "Tablet", "Smartwatch"],
    "Clothing": ["Jacket", "Jeans", "Dress", "Shirt", "Sweater", "Coat", "Pants", "Shoes"],
    "Home": ["Lamp", "Pillow", "Blanket", "Rug", "Chair", "Table", "Vase", "Mirror"],
    "Beauty": ["Serum", "Cream", "Lotion", "Mask", "Oil", "Cleanser", "Toner", "Moisturizer"],
    "Books": ["Photography", "Cooking", "Design", "Business", "Leadership", "Marketing", "Writing", "Programming"],
    "Sports": ["Yoga Mat", "Dumbbells", "Running Shoes", "Fitness Tracker", "Water Bottle", "Resistance Bands"]
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def random_date(start_year: int, end_year: int) -> str:
    """Generate random date between start_year and end_year"""
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).isoformat() + "Z"

def generate_object_id() -> str:
    """Generate a MongoDB-like ObjectId"""
    timestamp = hex(int(datetime.now().timestamp()))[2:]
    random_part = ''.join(random.choices('0123456789abcdef', k=16))
    return timestamp + random_part

def hash_password(password: str) -> str:
    """Generate bcrypt-like hash (simplified for demo)"""
    return f"$2b$12${hashlib.sha256(password.encode()).hexdigest()[:53]}"

# ============================================================================
# MOVIE DATA GENERATORS
# ============================================================================

def generate_movies(count: int = 50) -> List[Dict[str, Any]]:
    """Generate sample movie documents"""
    movies = []
    
    for i in range(count):
        year = random.randint(1990, 2024)
        runtime = random.randint(80, 180)
        genres = random.sample(GENRES, random.randint(1, 3))
        cast = random.sample(ACTORS, random.randint(3, 6))
        directors = random.sample(DIRECTORS, random.randint(1, 2))
        
        movie = {
            "_id": generate_object_id(),
            "title": random.choice(MOVIE_TITLES) + f" {i+1}" if i > 0 else random.choice(MOVIE_TITLES),
            "plot": f"A compelling story about {genres[0].lower()} that takes place in {random.choice(COUNTRIES)}.",
            "fullplot": f"An epic {genres[0].lower()} film that follows the journey of its protagonists through challenges and triumphs. Set against the backdrop of {random.choice(COUNTRIES)}, this {runtime}-minute masterpiece explores themes of love, loss, and redemption.",
            "genres": genres,
            "runtime": runtime,
            "cast": cast,
            "directors": directors,
            "writers": [f"{random.choice(['John', 'Jane', 'Michael', 'Sarah'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown'])}"],
            "year": year,
            "released": random_date(year, year),
            "rated": random.choice(RATINGS),
            "languages": random.sample(LANGUAGES, random.randint(1, 2)),
            "countries": random.sample(COUNTRIES, random.randint(1, 2)),
            "type": "movie",
            "poster": f"https://example.com/posters/movie_{i+1}.jpg",
            "num_mflix_comments": random.randint(0, 50),
            "lastupdated": datetime.now().isoformat(),
            "imdb": {
                "rating": round(random.uniform(5.0, 9.5), 1),
                "votes": random.randint(1000, 500000),
                "id": random.randint(100000, 9999999)
            },
            "tomatoes": {
                "viewer": {
                    "rating": round(random.uniform(2.5, 5.0), 1),
                    "numReviews": random.randint(100, 50000)
                },
                "critic": {
                    "rating": round(random.uniform(2.0, 5.0), 1),
                    "numReviews": random.randint(50, 500)
                },
                "fresh": random.randint(10, 100),
                "rotten": random.randint(0, 50),
                "lastUpdated": random_date(year, 2024)
            },
            "awards": {
                "wins": random.randint(0, 20),
                "nominations": random.randint(0, 50),
                "text": f"Won {random.randint(0, 5)} Oscars. {random.randint(0, 15)} wins & {random.randint(0, 30)} nominations total."
            },
            "metacritic": random.randint(40, 95)
        }
        
        movies.append(movie)
    
    return movies

def generate_comments(count: int = 100, movie_ids: List[str] = None) -> List[Dict[str, Any]]:
    """Generate sample comment documents"""
    if not movie_ids:
        movie_ids = [generate_object_id() for _ in range(10)]
    
    comments = []
    
    for i in range(count):
        name = random.choice(USER_NAMES)
        email = name.lower().replace(" ", "_") + "@gameofthron.es"
        
        comment = {
            "_id": generate_object_id(),
            "name": name,
            "email": email,
            "movie_id": random.choice(movie_ids),
            "text": random.choice([
                "Absolutely loved this movie! The cinematography was stunning.",
                "Great performances by the entire cast. Highly recommended!",
                "Not what I expected, but still enjoyable. Worth watching.",
                "The plot was a bit slow, but the ending made up for it.",
                "One of the best films I've seen this year. Masterpiece!",
                "Decent movie, but could have been better with tighter editing.",
                "The director's vision really shines through in every scene.",
                "Amazing soundtrack and beautiful visuals throughout.",
                "A must-watch for fans of the genre. Exceeded expectations!",
                "Interesting concept but the execution fell a bit flat."
            ]),
            "date": random_date(2015, 2024)
        }
        
        comments.append(comment)
    
    return comments

def generate_users(count: int = 20) -> List[Dict[str, Any]]:
    """Generate sample user documents"""
    users = []
    
    for i, name in enumerate(USER_NAMES[:count]):
        email = name.lower().replace(" ", "_") + "@gameofthron.es"
        
        user = {
            "_id": generate_object_id(),
            "name": name,
            "email": email,
            "password": hash_password(f"password{i+1}")
        }
        
        users.append(user)
    
    return users

def generate_theaters(count: int = 30) -> List[Dict[str, Any]]:
    """Generate sample theater documents"""
    theaters = []
    
    for i in range(count):
        state_code = random.choice(list(US_STATES.keys()))
        city = random.choice(CITIES.get(state_code, ["Springfield"]))
        
        theater = {
            "_id": generate_object_id(),
            "theaterId": 1000 + i,
            "location": {
                "address": {
                    "street1": f"{random.randint(100, 9999)} {random.choice(['Main', 'Market', 'Broadway', 'Oak', 'Maple'])} St",
                    "street2": None if random.random() > 0.3 else f"Suite {random.randint(100, 500)}",
                    "city": city,
                    "state": state_code,
                    "zipcode": f"{random.randint(10000, 99999)}"
                },
                "geo": {
                    "type": "Point",
                    "coordinates": [
                        round(random.uniform(-124.0, -67.0), 5),  # Longitude (US range)
                        round(random.uniform(25.0, 49.0), 5)      # Latitude (US range)
                    ]
                }
            }
        }
        
        theaters.append(theater)
    
    return theaters

# ============================================================================
# E-COMMERCE DATA GENERATORS
# ============================================================================

def generate_products(count: int = 100) -> List[Dict[str, Any]]:
    """Generate sample product documents"""
    products = []
    
    for i in range(count):
        category = random.choice(CATEGORIES)
        prefix = random.choice(PRODUCT_PREFIXES[category])
        item = random.choice(PRODUCT_ITEMS[category])
        
        product = {
            "_id": generate_object_id(),
            "title": f"{prefix} {item}",
            "description": f"High-quality {item.lower()} perfect for everyday use. Features premium materials and excellent craftsmanship.",
            "price": round(random.uniform(19.99, 299.99), 2),
            "category": category.lower(),
            "rating": round(random.uniform(1.0, 5.0), 1),
            "stock": random.randint(0, 500),
            "tags": ["sample", "seed", category.lower()],
            "createdAt": datetime.now().isoformat() + "Z"
        }
        
        products.append(product)
    
    return products

# ============================================================================
# MAIN GENERATION FUNCTION
# ============================================================================

def generate_all_sample_data():
    """Generate all sample data and save to JSON files"""
    
    print("🎬 Generating Movie Streaming Platform Data...")
    movies = generate_movies(50)
    movie_ids = [m["_id"] for m in movies]
    comments = generate_comments(100, movie_ids)
    users = generate_users(20)
    theaters = generate_theaters(30)
    
    print(f"  ✓ Generated {len(movies)} movies")
    print(f"  ✓ Generated {len(comments)} comments")
    print(f"  ✓ Generated {len(users)} users")
    print(f"  ✓ Generated {len(theaters)} theaters")
    
    print("\n🛍️  Generating E-commerce Product Data...")
    products = generate_products(100)
    print(f"  ✓ Generated {len(products)} products")
    
    # Save to JSON files
    print("\n💾 Saving data to JSON files...")
    
    sample_data = {
        "sample_mflix": {
            "movies": movies,
            "comments": comments,
            "users": users,
            "theaters": theaters
        },
        "test": {
            "products": products
        }
    }
    
    # Save combined file
    with open('/vercel/sandbox/sample_data_complete.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=2, ensure_ascii=False)
    print("  ✓ Saved: sample_data_complete.json")
    
    # Save individual collection files
    with open('/vercel/sandbox/sample_movies.json', 'w', encoding='utf-8') as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)
    print("  ✓ Saved: sample_movies.json")
    
    with open('/vercel/sandbox/sample_comments.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, indent=2, ensure_ascii=False)
    print("  ✓ Saved: sample_comments.json")
    
    with open('/vercel/sandbox/sample_users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
    print("  ✓ Saved: sample_users.json")
    
    with open('/vercel/sandbox/sample_theaters.json', 'w', encoding='utf-8') as f:
        json.dump(theaters, f, indent=2, ensure_ascii=False)
    print("  ✓ Saved: sample_theaters.json")
    
    with open('/vercel/sandbox/sample_products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)
    print("  ✓ Saved: sample_products.json")
    
    # Generate summary statistics
    print("\n📊 Sample Data Summary:")
    print("=" * 60)
    print(f"Total Documents Generated: {len(movies) + len(comments) + len(users) + len(theaters) + len(products)}")
    print(f"\nMovie Streaming Platform (sample_mflix):")
    print(f"  - Movies: {len(movies)}")
    print(f"  - Comments: {len(comments)}")
    print(f"  - Users: {len(users)}")
    print(f"  - Theaters: {len(theaters)}")
    print(f"\nE-commerce (test.products):")
    print(f"  - Products: {len(products)}")
    
    # Genre distribution
    genre_count = {}
    for movie in movies:
        for genre in movie['genres']:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    
    print(f"\n🎭 Top 5 Movie Genres:")
    for genre, count in sorted(genre_count.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  - {genre}: {count}")
    
    # Category distribution
    category_count = {}
    for product in products:
        category_count[product['category']] = category_count.get(product['category'], 0) + 1
    
    print(f"\n🏷️  Product Categories:")
    for category, count in sorted(category_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {category.title()}: {count}")
    
    # Price statistics
    prices = [p['price'] for p in products]
    print(f"\n💰 Product Price Statistics:")
    print(f"  - Average: ${sum(prices)/len(prices):.2f}")
    print(f"  - Min: ${min(prices):.2f}")
    print(f"  - Max: ${max(prices):.2f}")
    
    print("\n✅ Sample data generation complete!")
    print("\nFiles created:")
    print("  - sample_data_complete.json (all data)")
    print("  - sample_movies.json")
    print("  - sample_comments.json")
    print("  - sample_users.json")
    print("  - sample_theaters.json")
    print("  - sample_products.json")

if __name__ == "__main__":
    generate_all_sample_data()
