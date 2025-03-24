# Redis Synchronization Verification Exercise

This exercise demonstrates Redis replication and synchronization verification between a source and replica Redis instance. It includes tools to insert test data and verify that the data is properly synchronized between the Redis instances.

## Prerequisites
- Python 3.x
- Docker installed
- Redis server running in Docker
- source-db Redis instance on port 13300
- replica-db Redis instance on port 19777

## Setup
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


4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
## Files
- `requirements.txt`: Python package dependencies
- `redis_inserter.py`: Script to insert test data into the source Redis instance
- `redis_sync_verifier.py`: Script to verify synchronization between source and replica Redis instances
- `run_sync_test.py`: Main script that orchestrates the complete test sequence including initial verification, data insertion, and final verification


## Usage

Run the complete synchronization test sequence:
```bash
python run_sync_test.py
```

This script will:
1. Perform an initial verification of synchronization between source and replica
2. Insert test data into the source Redis instance
3. Wait for replication to complete
4. Perform a final verification to ensure all data is properly synchronized

The test sequence provides a comprehensive check of the Redis replication setup and will output detailed information about:
- Initial state of both databases
- Data insertion results
- Final synchronization status
- Any discrepancies found between source and replica

## Features

The verification script supports checking:
- String values
- Hash values
- List values
- Set values
- ZSet values

## Output

The verification script provides:
- Total number of keys in source and replica
- Number of common keys
- Missing keys in replica
- Extra keys in replica
- Detailed list of any value mismatches

## Error Handling

The scripts include error handling for:
- Connection failures
- Timeout issues
- Data type mismatches
- Value mismatches

## Notes

- The scripts assume Redis instances are running locally
- Default ports are 13300 for source and 19777 for replica
- A 2-second delay is included in the inserter script to allow for replication 