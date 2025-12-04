#!/usr/bin/env python3
"""
Script to upload structured data to Upstash Redis
Extracts data from the screenshot and stores it in Redis with proper structure
"""

import json

# Data extracted from the screenshot
users_data = [
    {
        "id": "1",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "role": "Student",
        "department": "Computer Science",
        "enrollment_date": "2023-09-01",
        "status": "Active"
    },
    {
        "id": "2",
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "role": "Faculty",
        "department": "Mathematics",
        "enrollment_date": "2020-08-15",
        "status": "Active"
    },
    {
        "id": "3",
        "name": "Bob Johnson",
        "email": "bob.johnson@example.com",
        "role": "Student",
        "department": "Physics",
        "enrollment_date": "2024-01-10",
        "status": "Active"
    }
]

# Generate Redis commands for uploading
print("=" * 60)
print("REDIS COMMANDS TO UPLOAD DATA TO UPSTASH")
print("=" * 60)
print()

# Method 1: Store each user as a hash
print("# Method 1: Store users as Redis Hashes")
print("# Each user is stored with key pattern: user:{id}")
print()
for user in users_data:
    user_id = user['id']
    print(f"# User {user_id}")
    fields = []
    for key, value in user.items():
        if key != 'id':
            fields.extend([key, value])
    print(f"HSET user:{user_id} {' '.join(fields)}")
    print()

print()
print("# Add user IDs to a set for easy retrieval")
user_ids = ' '.join([user['id'] for user in users_data])
print(f"SADD users:all {user_ids}")
print()

print()
print("=" * 60)
print("# Method 2: Store as JSON strings")
print("=" * 60)
print()
for user in users_data:
    user_id = user['id']
    json_str = json.dumps(user).replace('"', '\\"')
    print(f"SET user:{user_id}:json \"{json_str}\"")
    print()

print()
print("=" * 60)
print("# Method 3: Store entire dataset as single JSON")
print("=" * 60)
print()
all_users_json = json.dumps(users_data).replace('"', '\\"')
print(f"SET users:all:json \"{all_users_json}\"")
print()

print()
print("=" * 60)
print("# Additional indexes for querying")
print("=" * 60)
print()
print("# Index by department")
for user in users_data:
    dept = user['department'].replace(' ', '_').lower()
    print(f"SADD dept:{dept} {user['id']}")
print()

print("# Index by role")
for user in users_data:
    role = user['role'].lower()
    print(f"SADD role:{role} {user['id']}")
print()

print()
print("=" * 60)
print("PYTHON LIST FORMAT FOR UPSTASH MCP TOOL")
print("=" * 60)
print()
print("# Use this format with redis_database_run_redis_commands tool:")
print()
print("commands = [")
for user in users_data:
    user_id = user['id']
    cmd = ['HSET', f'user:{user_id}']
    for key, value in user.items():
        if key != 'id':
            cmd.extend([key, value])
    print(f"    {cmd},")
print(f"    ['SADD', 'users:all', {', '.join([repr(u['id']) for u in users_data])}],")
print("]")
print()

# Save structured data to JSON file
output_file = '/vercel/sandbox/upstash_data.json'
with open(output_file, 'w') as f:
    json.dump({
        'users': users_data,
        'metadata': {
            'total_users': len(users_data),
            'extracted_from': 'Screenshot 2025-12-04 at 2.00.33 PM.png',
            'date': '2025-12-04'
        }
    }, f, indent=2)

print()
print(f"✓ Structured data saved to: {output_file}")
print()
