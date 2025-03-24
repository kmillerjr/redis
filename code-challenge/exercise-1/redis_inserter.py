import redis
import time

def insert_data():
    # Connect to source Redis database
    source_redis = redis.Redis(
        host="localhost",
        port=13300,
        decode_responses=True  # This ensures we get strings rather than bytes
    )

    # Connect to replica Redis database
    replica_redis = redis.Redis(
        host="localhost",
        port=19777,
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