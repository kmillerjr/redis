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

# Redis Enterprise API connection settings with environment variable support
REDIS_ENTERPRISE_HOST = os.getenv('REDIS_ENTERPRISE_HOST', 'localhost')
REDIS_ENTERPRISE_PORT = int(os.getenv('REDIS_ENTERPRISE_PORT', '9443'))
REDIS_ENTERPRISE_USERNAME = os.getenv('REDIS_ENTERPRISE_USERNAME')
REDIS_ENTERPRISE_PASSWORD = os.getenv('REDIS_ENTERPRISE_PASSWORD') 