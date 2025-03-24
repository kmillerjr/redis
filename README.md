# Redis Code Challenge

This repository contains two exercises demonstrating different aspects of Redis functionality and management.

## Exercise Overview

### Exercise 1: Redis Synchronization Verification
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

### Exercise 2: Redis Enterprise Role and User Management
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

## Prerequisites

- Python 3.6 or higher
- Docker installed
- Redis Enterprise cluster running and accessible
- Required Python packages (install using `pip install -r requirements.txt` in each exercise directory)

## Directory Structure

```
.
├── exercise-1/           # Redis Synchronization Verification
│   ├── redis_inserter.py
│   ├── redis_sync_verifier.py
│   ├── run_sync_test.py
│   └── requirements.txt
│
└── exercise-2/           # Redis Enterprise Role and User Management
    ├── redis_enterprise_api.py
    └── requirements.txt
```

## Configuration

Both exercises use configuration files (`config.py`) to manage connection settings. These files support environment variables for secure configuration:

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

To use environment variables, set them before running the scripts:
```bash
export REDIS_SOURCE_HOST=your_source_host
export REDIS_ENTERPRISE_PASSWORD=your_password
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

## Testing

Both exercises include basic error handling and validation. For production use, consider adding:
- Unit tests
- Integration tests
- Input validation
- Secure password handling
- Environment variable support for sensitive data 