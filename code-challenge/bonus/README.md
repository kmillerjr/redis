# Semantic Router

A Python application that performs semantic routing for incoming queries, directing them to the most relevant topic based on semantic similarity. This implementation uses RedisVL for vector storage and search.

## Features

- Routes queries to three predefined topics:
  - GenAI Programming Topics
  - Science Fiction Entertainment
  - Classical Music
- Uses vector embeddings from Sentence Transformers for semantic similarity
- Configurable Redis connection
- Simple to extend with new routes or reference examples

## Requirements

- Python 3.8+
- Redis with Search module enabled (Redis Stack)
- Dependencies:
  - redisvl
  - sentence-transformers
  - python-dotenv
  - requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/semantic-router.git
cd semantic-router
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Redis with Search module is running:
```bash
# Using Docker
docker run -p 6379:6379 redis/redis-stack:latest
```

4. Create a `.env` file in the project directory with your Redis configuration:
```env
REDIS_URL=redis://localhost:14000
REDIS_SOCKET_CONNECT_TIMEOUT=30
REDIS_SOCKET_TIMEOUT=120
ROUTER_NAME=topic-router
```

## Usage

The semantic router is implemented as a Python module that can be imported and used in your applications. Here's how to use it:

```python
from semantic_router import router

# Test a query
query = "How to implement RAG with Python and vector databases"
response = router.route_many(query)

if response:
    print(f"Matched route: {response[0].name}")
    print(f"Similarity score: {response[0].distance}")
else:
    print("No matching route found")
```

## How It Works

1. Reference examples for each route are embedded using a Sentence Transformer model and stored in Redis
2. When a query is received, it's also embedded with the same model
3. The system performs a vector search to find the most semantically similar reference examples
4. Based on the majority of matching examples in the results, the query is routed to the appropriate topic

## Customization

You can customize the routes by modifying the route definitions in `semantic_router.py`. Each route is defined using the `Route` class from RedisVL:

```python
from redisvl.extensions.router import Route

new_route = Route(
    name="your_new_route",
    description="Your New Route Name",
    references=[
        "Example sentence 1 related to your route",
        "Example sentence 2 related to your route",
        # Add more references...
    ],
    metadata={"category": "your_category", "priority": 1},
    distance_threshold=0.1
)
```
