import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Redis Configuration
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:14000")
REDIS_SOCKET_CONNECT_TIMEOUT = int(os.getenv("REDIS_SOCKET_CONNECT_TIMEOUT", "30"))
REDIS_SOCKET_TIMEOUT = int(os.getenv("REDIS_SOCKET_TIMEOUT", "120"))

# Semantic Router Configuration
ROUTER_NAME = os.getenv("ROUTER_NAME", "topic-router") 