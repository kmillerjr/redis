import redis
import time
from config import (
    REDIS_SOURCE_HOST,
    REDIS_SOURCE_PORT,
    REDIS_REPLICA_HOST,
    REDIS_REPLICA_PORT,
    REDIS_SOURCE_PASSWORD,
    REDIS_REPLICA_PASSWORD
)

def insert_data():
    # Connect to source Redis database
    source_redis = redis.Redis(
        host=REDIS_SOURCE_HOST,
        port=REDIS_SOURCE_PORT,
        password=REDIS_SOURCE_PASSWORD,
        decode_responses=True  # This ensures we get strings rather than bytes
    )

    # Connect to replica Redis database
    replica_redis = redis.Redis(
        host=REDIS_REPLICA_HOST,
        port=REDIS_REPLICA_PORT,
        password=REDIS_REPLICA_PASSWORD,
        decode_responses=True
    )

    # Insert values 1-100 into source database
    print("Inserting values 1-100 into source database...")
    for i in range(1, 101):
        source_redis.set(f"num:{i}", i)
    
    # Give some time for replication to occur
    print("Waiting for replication...")
    time.sleep(2)

    # Read and print values in reverse order from replica
    print("\nReading values in reverse order from replica database:")
    for i in range(100, 0, -1):
        value = replica_redis.get(f"num:{i}")
        print(f"num:{i} = {value}")

if __name__ == "__main__":
    insert_data() 