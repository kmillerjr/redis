# Redis Replication Exercise

This exercise demonstrates Redis replication and verification between a source and replica Redis instance.

## Components

- `redis_inserter.py`: Inserts test data into the source Redis instance and verifies it appears in the replica
- `redis_sync_verifier.py`: A comprehensive tool to verify synchronization between source and replica Redis instances
- `config.py`: Configuration file for Redis connection settings
- `run_sync_test.py`: Orchestrates a complete test sequence including initial verification, data insertion, and final verification

## Prerequisites

- Python 3.x
- Redis Python client (`redis-py`)
- Access to two Redis instances (source and replica)

## Installation

1. Install the required Python package:
```bash
pip install redis
```

## Configuration

The Redis connection settings can be configured through environment variables or will use default values:

```bash
# Default values (if not set):
REDIS_SOURCE_HOST=localhost
REDIS_SOURCE_PORT=13300
REDIS_REPLICA_HOST=localhost
REDIS_REPLICA_PORT=19777
```

To override these settings, set the environment variables before running the scripts:

```bash
export REDIS_SOURCE_HOST=redis.example.com
export REDIS_SOURCE_PORT=6379
export REDIS_REPLICA_HOST=redis-replica.example.com
export REDIS_REPLICA_PORT=6379
```

If your Redis instances require authentication, you can set the passwords:

```bash
export REDIS_SOURCE_PASSWORD=your_source_password
export REDIS_REPLICA_PASSWORD=your_replica_password
```

## Usage

You can run the scripts individually or use the complete test sequence:

### Individual Scripts

1. First, run the inserter to populate the source Redis instance:
```bash
python redis_inserter.py
```

2. Then, verify the synchronization between source and replica:
```bash
python redis_sync_verifier.py
```

### Complete Test Sequence

Run the complete test sequence that includes initial verification, data insertion, and final verification:
```bash
python run_sync_test.py
```

The verifier will:
- Compare all keys between source and replica
- Check for missing or extra keys
- Verify data types match
- Compare values for each key
- Provide a detailed summary of any mismatches

## Output

The inserter will:
- Insert values 1-100 into the source database
- Wait for replication
- Read and display values in reverse order from the replica

The verifier will provide:
- Connection status for both instances
- List of missing or extra keys
- Detailed comparison of common keys
- Summary statistics
- List of any mismatches found

The complete test sequence will:
1. Perform an initial verification
2. Insert test data
3. Wait for replication
4. Perform a final verification
5. Provide a summary of the entire process 