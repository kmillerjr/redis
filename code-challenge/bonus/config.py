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

# Redis Configuration
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:14000")
REDIS_SOCKET_CONNECT_TIMEOUT = int(os.getenv("REDIS_SOCKET_CONNECT_TIMEOUT", "30"))
REDIS_SOCKET_TIMEOUT = int(os.getenv("REDIS_SOCKET_TIMEOUT", "120"))

# Semantic Router Configuration
ROUTER_NAME = os.getenv("ROUTER_NAME", "topic-router") 