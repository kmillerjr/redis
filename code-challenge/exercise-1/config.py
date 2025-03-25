import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Get the directory where this config file is located
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))

# Debug current working directory and .env file location
logger.debug(f"Current working directory: {os.getcwd()}")
logger.debug(f"Config file directory: {CONFIG_DIR}")
logger.debug(f"Looking for .env file in: {CONFIG_DIR}")

# Load environment variables from the same directory as this config file
load_dotenv(os.path.join(CONFIG_DIR, '.env'), verbose=True)

# Redis connection settings with environment variable support
REDIS_SOURCE_HOST = os.getenv('REDIS_SOURCE_HOST', 'localhost')
REDIS_SOURCE_PORT = int(os.getenv('REDIS_SOURCE_PORT', '13300'))
REDIS_REPLICA_HOST = os.getenv('REDIS_REPLICA_HOST', 'localhost')
REDIS_REPLICA_PORT = int(os.getenv('REDIS_REPLICA_PORT', '19777'))
REDIS_SOURCE_PASSWORD = os.getenv('REDIS_SOURCE_PASSWORD')
REDIS_REPLICA_PASSWORD = os.getenv('REDIS_REPLICA_PASSWORD') 
