# Redis Professional Services Consultant Technical Challenge

This project contains a series of exercises demonstrating different aspects of Redis functionality, including replication, enterprise features, and semantic search capabilities.

## Exercise Overview

### Exercise 1: [Redis Synchronization Verification](code-challenge/exercise-2)
This exercise focuses on Redis replication and synchronization verification between source and replica Redis instances. It includes:
- Tools for inserting test data
- Verification of data synchronization
- Support for multiple Redis data types (strings, hashes, lists, sets, zsets)
- Comprehensive error handling and reporting

**Key Features:**
- Docker-based setup with Redis Enterprise
- Automated test data generation using memtier-benchmark
- Detailed synchronization verification
- Support for multiple data types

### Exercise 2: [Redis Enterprise Role and User Management](code-challenge/exercise-2)
This exercise demonstrates role and user management functionality for Redis Enterprise using the REST API. It includes:
- Role creation and management
- User creation and assignment
- Database management capabilities
- REST API integration

**Key Features:**
- Role-based access control
- User management with different permission levels
- Database creation and management
- REST API implementation

### Bonus Exercise: [Semantic Search Implementation](code-challenge/bonus)
This exercise demonstrates advanced semantic routing capabilities using Redis Vector Search. It includes:
- Semantic routing for incoming queries
- Vector embeddings for text similarity
- Multiple topic classification
- REST API and CLI interfaces

**Key Features:**
- Vector-based semantic search using RedisVL
- Support for multiple topic domains (GenAI, SciFi, Classical Music)
- Real-time query routing based on semantic similarity
- Configurable Redis connection and search parameters
- Easy to extend with new routes and reference examples

## Project Structure

```
.
├── code-challenge/
│   ├── exercise-1/     # Redis Replication Exercise
│   ├── exercise-2/     # Redis Enterprise API Exercise
│   ├── bonus/         # Semantic Search Implementation
│   └── requirements.txt
└── .gitignore
```

## Prerequisites

- Python 3.x
- Docker installed
- Redis Enterprise cluster running and accessible
- Required Python packages (install using `pip install -r requirements.txt`)

## Project Components

### Exercise 1: [Redis Replication](code-challenge/exercise-1\README.md)
Demonstrates Redis replication and verification between source and replica Redis instances.

Key components:
- `redis_inserter.py`: Inserts test data into source Redis
- `redis_sync_verifier.py`: Verifies synchronization between instances
- `run_sync_test.py`: Orchestrates complete test sequence
- `config.py`: Configuration settings

### Exercise 2: [Redis Enterprise API](code-challenge/exercise-2/readme.md)
Implements Redis Enterprise API functionality for database management.

Key components:
- `redis_enterprise_api.py`: Core API implementation
- `config.py`: Configuration settings

### Bonus Exercise: [Semantic Search](code-challenge/bonus/README.md)
Implements semantic search capabilities using Redis.

Key components:
- `semantic_router.py`: Semantic search implementation
- `config.py`: Configuration settings

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/kmillerjr/redis.git
cd redis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  
# On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd code-challenge
pip install -r requirements.txt
```

4. Set up Redis Enterprise:
```bash
docker run -d --cap-add sys_resource --name redis-enterprise \
  -p 8443:8443 -p 9443:9443 -p 12000:12000 -p 13300:13300 -p 14000:14000 -p 19777:19777 \
  redislabs/redis
```

## Configuration

The project uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:
### Exercise 1 Configuration
The `exercise-1/config.py` manages Redis source and replica connection settings:
- `REDIS_SOURCE_HOST`: Source Redis host (default: 172.16.22.21)
- `REDIS_SOURCE_PORT`: Source Redis port (default: 13300)
- `REDIS_REPLICA_HOST`: Replica Redis host (default: 172.16.22.22)
- `REDIS_REPLICA_PORT`: Replica Redis port (default: 19777)
- `REDIS_SOURCE_PASSWORD`: Source Redis password (optional)
- `REDIS_REPLICA_PASSWORD`: Replica Redis password (optional)

### Exercise 2 Configuration
The `exercise-2/config.py` manages Redis Enterprise API connection settings:
- `REDIS_ENTERPRISE_HOST`: Redis Enterprise host (default: localhost)
- `REDIS_ENTERPRISE_PORT`: Redis Enterprise API port (default: 9443)
- `REDIS_ENTERPRISE_USERNAME`: API username (default: kmillerjr@gmail.com)
- `REDIS_ENTERPRISE_PASSWORD`: API password (default: admin)

### Bonus Exercise Configuration
The `bonus/config.py` manages Redis Vector Search connection settings:
- `REDIS_URL`: Redis connection URL (default: redis://localhost:14000)
- `REDIS_SOCKET_CONNECT_TIMEOUT`: Socket connection timeout in seconds (default: 30)
- `REDIS_SOCKET_TIMEOUT`: Socket operation timeout in seconds (default: 120)
- `ROUTER_NAME`: Name of the semantic router instance (default: topic-router)

To use environment variables, set them before running the scripts:
```bash
export REDIS_SOURCE_HOST=your_source_host
export REDIS_ENTERPRISE_PASSWORD=your_password
...
```

### Using .env File
For easier configuration management, you can create a `.env` file in each exercise directory. This method is recommended over setting environment variables directly.

1. Create a `.env` file in the exercise directory:
```bash
# Exercise 1 (.env in exercise-1/)
REDIS_SOURCE_HOST=localhost
REDIS_SOURCE_PORT=13300
REDIS_REPLICA_HOST=localhost
REDIS_REPLICA_PORT=19777
REDIS_SOURCE_PASSWORD=<your_secure_password>
REDIS_REPLICA_PASSWORD=<your_secure_password>

# Exercise 2 (.env in exercise-2/)
REDIS_ENTERPRISE_HOST=localhost
REDIS_ENTERPRISE_PORT=9443
REDIS_ENTERPRISE_USERNAME=<your_username>
REDIS_ENTERPRISE_PASSWORD=<your_secure_password>

# Bonus Exercise (.env in bonus/)
REDIS_URL=redis://localhost:14000
REDIS_SOCKET_CONNECT_TIMEOUT=30
REDIS_SOCKET_TIMEOUT=120
ROUTER_NAME=topic-router
```

2. The `.env` file will be automatically loaded by the application when you run the scripts
3. Make sure to add `.env` to your `.gitignore` file to prevent committing sensitive information
4. For production deployments, ensure proper permissions are set on the `.env` file:
```bash
chmod 600 .env  # Restrict read/write to owner only
```

## Getting Started

1. Clone this repository
2. Set up a Python virtual environment:
   ```bash
   pip3 install --user virtualenv
   virtualenv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Navigate to the specific exercise directory
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Follow the setup instructions in each exercise's README file


## Security Notes

- SSL verification is disabled by default for development purposes
- Passwords are transmitted in plain text (consider using environment variables or secure configuration in production)
- Basic authentication is used for API access

## Development

Each exercise can be modified and extended based on specific requirements:
- Exercise 1: Add support for additional data types or verification methods
- Exercise 2: Extend role definitions or add more user management features
- Bonus Exercise: Add new topic domains or enhance semantic routing capabilities with additional features like:
  - Custom embedding models
  - Additional routing strategies

## Testing

Both exercises include basic error handling and validation. For production use, consider adding:
- Unit tests
- Integration tests
- Input validation
- Secure password handling
- Environment variable support for sensitive data