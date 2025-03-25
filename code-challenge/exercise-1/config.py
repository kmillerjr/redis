import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
# Redis connection settings with environment variable support
REDIS_SOURCE_HOST = os.getenv('REDIS_SOURCE_HOST', '172.16.22.21')
REDIS_SOURCE_PORT = int(os.getenv('REDIS_SOURCE_PORT', '13300'))
REDIS_REPLICA_HOST = os.getenv('REDIS_REPLICA_HOST', '172.16.22.22')
REDIS_REPLICA_PORT = int(os.getenv('REDIS_REPLICA_PORT', '19777'))
REDIS_SOURCE_PASSWORD = os.getenv('REDIS_SOURCE_PASSWORD')
REDIS_REPLICA_PASSWORD = os.getenv('REDIS_REPLICA_PASSWORD') 
