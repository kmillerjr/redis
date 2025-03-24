import os

# Redis Enterprise API connection settings with environment variable support
REDIS_ENTERPRISE_HOST = os.getenv('REDIS_ENTERPRISE_HOST', 'localhost')
REDIS_ENTERPRISE_PORT = int(os.getenv('REDIS_ENTERPRISE_PORT', '9443'))
REDIS_ENTERPRISE_USERNAME = os.getenv('REDIS_ENTERPRISE_USERNAME', 'kmillerjr@gmail.com')
REDIS_ENTERPRISE_PASSWORD = os.getenv('REDIS_ENTERPRISE_PASSWORD', 'admin') 