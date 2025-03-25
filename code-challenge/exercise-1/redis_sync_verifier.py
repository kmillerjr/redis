#!/usr/bin/env python3

import redis
import sys
from typing import Dict, List, Set, Tuple
import time
from config import (
    REDIS_SOURCE_HOST,
    REDIS_SOURCE_PORT,
    REDIS_REPLICA_HOST,
    REDIS_REPLICA_PORT,
    REDIS_SOURCE_PASSWORD,
    REDIS_REPLICA_PASSWORD
)

def connect_to_redis(host: str, port: int, password: str = None) -> redis.Redis:
    """Establish connection to Redis instance."""
    try:
        client = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=True,
            socket_timeout=5
        )
        # Test connection
        client.ping()
        return client
    except redis.ConnectionError as e:
        print(f"Failed to connect to Redis at {host}:{port}: {e}")
        sys.exit(1)

def get_all_keys(client: redis.Redis) -> List[str]:
    """Get all keys from Redis instance."""
    return client.keys('*')

def get_key_type(client: redis.Redis, key: str) -> str:
    """Get the type of a key."""
    key_type = client.type(key)
    return key_type.decode('utf-8') if isinstance(key_type, bytes) else key_type

def compare_values(source: redis.Redis, replica: redis.Redis, key: str, key_type: str) -> Tuple[bool, str]:
    """Compare values between source and replica for a given key."""
    if key_type == 'string':
        source_val = source.get(key)
        replica_val = replica.get(key)
        return source_val == replica_val, f"String value mismatch: source={source_val}, replica={replica_val}"
    
    elif key_type == 'hash':
        source_val = source.hgetall(key)
        replica_val = replica.hgetall(key)
        return source_val == replica_val, f"Hash value mismatch: source={source_val}, replica={replica_val}"
    
    elif key_type == 'list':
        source_val = source.lrange(key, 0, -1)
        replica_val = replica.lrange(key, 0, -1)
        return source_val == replica_val, f"List value mismatch: source={source_val}, replica={replica_val}"
    
    elif key_type == 'set':
        source_val = source.smembers(key)
        replica_val = replica.smembers(key)
        return source_val == replica_val, f"Set value mismatch: source={source_val}, replica={replica_val}"
    
    elif key_type == 'zset':
        source_val = source.zrange(key, 0, -1, withscores=True)
        replica_val = replica.zrange(key, 0, -1, withscores=True)
        return source_val == replica_val, f"ZSet value mismatch: source={source_val}, replica={replica_val}"
    
    return True, "Unsupported key type"

def verify_sync(source_host: str, source_port: int, replica_host: str, replica_port: int, 
                source_password: str = None, replica_password: str = None) -> None:
    """Verify synchronization between source and replica Redis instances."""
    print(f"Connecting to source Redis at {source_host}:{source_port}")
    source = connect_to_redis(source_host, source_port, source_password)
    
    print(f"Connecting to replica Redis at {replica_host}:{replica_port}")
    replica = connect_to_redis(replica_host, replica_port, replica_password)
    
    # Get all keys from both instances
    source_keys = set(get_all_keys(source))
    replica_keys = set(get_all_keys(replica))
    
    # Check for missing keys
    missing_in_replica = source_keys - replica_keys
    extra_in_replica = replica_keys - source_keys
    
    if missing_in_replica:
        print(f"\nKeys missing in replica: {missing_in_replica}")
    if extra_in_replica:
        print(f"\nExtra keys in replica: {extra_in_replica}")
    
    # Compare values for common keys
    common_keys = source_keys & replica_keys
    mismatches = []
    
    print(f"\nComparing {len(common_keys)} common keys...")
    for key in common_keys:
        source_type = get_key_type(source, key)
        replica_type = get_key_type(replica, key)
        
        if source_type != replica_type:
            mismatches.append(f"Type mismatch for key '{key}': source={source_type}, replica={replica_type}")
            continue
        
        is_sync, message = compare_values(source, replica, key, source_type)
        if not is_sync:
            mismatches.append(f"Key '{key}': {message}")
    
    # Print summary
    print("\nVerification Summary:")
    print(f"Total keys in source: {len(source_keys)}")
    print(f"Total keys in replica: {len(replica_keys)}")
    print(f"Common keys: {len(common_keys)}")
    print(f"Keys missing in replica: {len(missing_in_replica)}")
    print(f"Extra keys in replica: {len(extra_in_replica)}")
    print(f"Value mismatches: {len(mismatches)}")
    
    if mismatches:
        print("\nDetailed Mismatches:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
    else:
        print("\nAll common keys are synchronized!")

if __name__ == "__main__":
    verify_sync(
        REDIS_SOURCE_HOST,
        REDIS_SOURCE_PORT,
        REDIS_REPLICA_HOST,
        REDIS_REPLICA_PORT,
        REDIS_SOURCE_PASSWORD,
        REDIS_REPLICA_PASSWORD
    ) 
   