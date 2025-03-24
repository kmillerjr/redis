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

## Getting Started

1. Clone this repository
2. Navigate to the specific exercise directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Follow the setup instructions in each exercise's README file

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