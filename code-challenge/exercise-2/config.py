import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Redis Enterprise API connection settings with environment variable support
REDIS_ENTERPRISE_HOST = os.getenv('REDIS_ENTERPRISE_HOST', '172.16.22.21')
REDIS_ENTERPRISE_PORT = int(os.getenv('REDIS_ENTERPRISE_PORT', '9443'))
REDIS_ENTERPRISE_USERNAME = os.getenv('REDIS_ENTERPRISE_USERNAME', 'admin@rl.org')
REDIS_ENTERPRISE_PASSWORD = os.getenv('REDIS_ENTERPRISE_PASSWORD', '9JCp58r') 