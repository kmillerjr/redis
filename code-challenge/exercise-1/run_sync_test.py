from redis_sync_verifier import verify_sync
from redis_inserter import insert_data
import time

def main():
    # Configuration
    SOURCE_HOST = "localhost"
    SOURCE_PORT = 13300
    REPLICA_HOST = "localhost"
    REPLICA_PORT = 19777

    print("Starting sync test sequence...")
    
    # First sync verification
    print("\n1. Running initial sync verification...")
    verify_sync(SOURCE_HOST, SOURCE_PORT, REPLICA_HOST, REPLICA_PORT)

    # Run the inserter
    print("\n2. Running Redis inserter...")
    insert_data()

    # Wait a moment for replication
    print("\nWaiting for replication to complete...")
    time.sleep(2)

    # Second sync verification
    print("\n3. Running final sync verification...")
    verify_sync(SOURCE_HOST, SOURCE_PORT, REPLICA_HOST, REPLICA_PORT)

    print("\nSync test sequence completed successfully!")
    print("\n")

if __name__ == "__main__":
    main() 