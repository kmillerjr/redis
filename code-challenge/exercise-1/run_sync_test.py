from redis_sync_verifier import verify_sync
from redis_inserter import insert_data
import time
from config import (
    REDIS_SOURCE_HOST,
    REDIS_SOURCE_PORT,
    REDIS_REPLICA_HOST,
    REDIS_REPLICA_PORT,
    REDIS_SOURCE_PASSWORD,
    REDIS_REPLICA_PASSWORD
)

def main():
    print("Starting sync test sequence...")
    
    # First sync verification
    print("\n1. Running initial sync verification...")
    verify_sync(
        REDIS_SOURCE_HOST,
        REDIS_SOURCE_PORT,
        REDIS_REPLICA_HOST,
        REDIS_REPLICA_PORT,
        REDIS_SOURCE_PASSWORD,
        REDIS_REPLICA_PASSWORD
    )

    # Run the inserter
    print("\n2. Running Redis inserter...")
    insert_data()

    # Wait a moment for replication
    print("\nWaiting for replication to complete...")
    time.sleep(2)

    # Second sync verification
    print("\n3. Running final sync verification...")
    verify_sync(
        REDIS_SOURCE_HOST,
        REDIS_SOURCE_PORT,
        REDIS_REPLICA_HOST,
        REDIS_REPLICA_PORT,
        REDIS_SOURCE_PASSWORD,
        REDIS_REPLICA_PASSWORD
    )

    print("\nSync test sequence completed successfully!")
    print("\n")

if __name__ == "__main__":
    main() 