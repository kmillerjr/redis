# Semantic Router

A Python application that performs semantic routing for incoming queries, directing them to the most relevant topic based on semantic similarity. This implementation uses RedisVL for vector storage and search.

## Features

- Routes queries to three predefined topics:
  - GenAI Programming Topics
  - Science Fiction Entertainment
  - Classical Music
- Uses vector embeddings from Sentence Transformers for semantic similarity
- Provides both a REST API and command-line interface
- Configurable Redis connection
- Simple to extend with new routes or reference examples

## Requirements

- Python 3.8+
- Redis with Search module enabled (Redis Stack)
- Dependencies:
  - redisvl
  - sentence-transformers
  - flask
  - numpy
  - scipy

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

## Usage

### API Server

Start the API server:

```bash
python semantic_router.py --redis-host localhost --redis-port 6379
```

Send a query:

```bash
curl -X POST http://localhost:5000/route \
  -H "Content-Type: application/json" \
  -d '{"query": "How to implement transformer models with PyTorch"}'
```

Example response:

```json
{
  "confidence": 0.8,
  "query": "How to implement transformer models with PyTorch",
  "route": "genai_programming",
  "route_name": "GenAI Programming Topics",
  "success": true
}
```

### Command Line Interface

For interactive mode:

```bash
python semantic_router_cli.py -i
```

For a single query:

```bash
python semantic_router_cli.py "What are the main themes in Blade Runner 2049?"
```

## How It Works

1. Reference examples for each route are embedded using a Sentence Transformer model and stored in Redis
2. When a query is received, it's also embedded with the same model
3. The system performs a vector search to find the most semantically similar reference examples
4. Based on the majority of matching examples in the results, the query is routed to the appropriate topic

## Customization

You can easily customize the routes and reference examples by modifying the `routes` dictionary in the `SemanticRouter` class:

```python
self.routes = {
    "your_new_route": {
        "name": "Your New Route Name",
        "references": [
            "Example sentence 1 related to your route",
            "Example sentence 2 related to your route",
            # Add more references...
        ]
    },
    # Your other routes...
}
```
