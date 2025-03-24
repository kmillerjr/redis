# Redis Replication Exercise

This exercise demonstrates Redis replication and verification between a source and replica Redis instance.

## Components

- `redis_inserter.py`: Inserts test data into the source Redis instance and verifies it appears in the replica
- `redis_sync_verifier.py`: A comprehensive tool to verify synchronization between source and replica Redis instances
- `config.py`: Configuration file for Redis connection settings
- `run_sync_test.py`: Orchestrates a complete test sequence including initial verification, data insertion, and final verification

## Prerequisites
- Python 3.x
- Docker installed
- Redis server running in Docker
- source-db Redis instance on port 13300
- replica-db Redis instance on port 19777

## Setup - (to run locally with Docker)
1. Follow the [redis quickstart](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart/#run-the-container) link:
- run redis enterprise in docker with the exposed ports for the 2 databases:   
$ `docker run -d --cap-add sys_resource --name redis-enterprise -p 8443:8443 -p 9443:9443 -p 12000:12000 -p 13300:13300 -p 19777:19777 redislabs/redis`

2. Setup dbs: source-db and replica-db
- source-db:
    - port: 13300
- replica-db:
    - port: 19777   
    - _*Note:* change the connection for the replica of connection to 172.17.0.2:13300_

3. Generate test data using memtier-benchmark:
    ```bash
    # Build the benchmark container
    docker build -t redis-benchmark .

    # Run the benchmark and save results
    docker run --rm -v ${PWD}/output:/tmp redis-benchmark 
    ```
    This will generate test data in the source Redis instance and save the  benchmark results to `./output/memtier_benchmark.txt`.

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
## Data Loader
If you are using a load node that already has  memtier_benchmark installed, you can use the following command to load data:

```memtier_benchmark -s 172.17.0.2 -p 13300 --protocol=redis --clients=50 --threads=4 --requests=10000 --data-size=1024 --pipeline=1 --key-pattern=R:R --ratio=1:1```
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