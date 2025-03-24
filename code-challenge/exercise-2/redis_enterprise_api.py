import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from typing import List, Dict, Optional
from config import (
    REDIS_ENTERPRISE_HOST,
    REDIS_ENTERPRISE_PORT,
    REDIS_ENTERPRISE_USERNAME,
    REDIS_ENTERPRISE_PASSWORD
)

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class RedisEnterpriseAPI:
    def __init__(self, host: str, port: int, username: str, password: str):
        """Initialize Redis Enterprise API client."""
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        
        self.base_url = f"https://{self.host}:{self.port}/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self._get_basic_auth(self.username, self.password)}"
        }
        # Disable SSL verification warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.verify_ssl = False

    def _get_basic_auth(self, username: str, password: str) -> str:
        """Generate basic auth header value."""
        import base64
        return base64.b64encode(f"{username}:{password}".encode()).decode()

    def get_role(self, role_name: str) -> Optional[Dict]:
        """Get role details if it exists."""
        try:
            response = requests.get(
                f"{self.base_url}/roles",
                headers=self.headers,
                verify=self.verify_ssl
            )
            if response.status_code == 200:
                roles = response.json()
                for role in roles:
                    if role.get('name') == role_name:
                        return role
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error getting role {role_name}: {str(e)}")
            return None

    def create_role(self, role_name: str, membership: str = "admin") -> Optional[Dict]:
        """Create a role if it doesn't exist."""
        role_data = {
            "name": role_name,
            "management": membership
        }

        try:
            # First check if role exists
            existing_role = self.get_role(role_name)
            if existing_role:
                print(f"Role {role_name} already exists")
                return existing_role

            # Create the role
            response = requests.post(
                f"{self.base_url}/roles",
                headers=self.headers,
                json=role_data,
                verify=self.verify_ssl
            )
            
            if response.status_code == 200:
                print(f"Successfully created role: {role_name} with membership: {membership}")
                return response.json()
            else:
                print(f"Failed to create role {role_name}. Status code: {response.status_code}")
                print(f"Response: {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error creating role {role_name}: {str(e)}")
            return None

    def create_roles(self, roles: List[Dict[str, str]]) -> List[Dict]:
        """Create multiple roles with their respective memberships and return their details."""
        created_roles = []
        for role in roles:
            created_role = self.create_role(role['name'], role['membership'])
            if created_role:
                created_roles.append(created_role)
        return created_roles

    def create_database(self, name, memory_size=1024):
        """Create a new database"""
        endpoint = f"{self.base_url}/bdbs"
        payload = {
            "name": name,
            "memory_size": memory_size,
            "type": "redis",
            "replication": False
        }
        
        response = requests.post(endpoint, json=payload, headers=self.headers, verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()
    
    def get_user(self, email: str) -> Optional[Dict]:
        """Get user details if they exist."""
        try:
            response = requests.get(
                f"{self.base_url}/users",
                headers=self.headers,
                verify=self.verify_ssl
            )
            if response.status_code == 200:
                users = response.json()
                for user in users:
                    if user.get('email') == email:
                        return user
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error getting user {email}: {str(e)}")
            return None

    def create_user(self, email: str, password: str, name: str, role_uid: int):
        """Create a new user if they don't exist."""
        # First check if user exists
        existing_user = self.get_user(email)
        if existing_user:
            print(f"User with email {email} already exists")
            return existing_user

        endpoint = f"{self.base_url}/users"
        payload = {
            "email": email,
            "password": password,
            "name": name,
            "role_uids": [role_uid],
            "auth_method": "regular"
        }
        
        response = requests.post(endpoint, json=payload, headers=self.headers, verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()
    
    def list_users(self):
        """List all users"""
        endpoint = f"{self.base_url}/users"
        response = requests.get(endpoint, headers=self.headers, verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()
    
    def delete_database(self, uid: int):
        """Delete a database by UID"""
        endpoint = f"{self.base_url}/bdbs/{uid}"
        response = requests.delete(endpoint, headers=self.headers, verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()

    def get_database(self, name: str) -> List[Dict]:
        """Get all databases with the specified name."""
        try:
            response = requests.get(
                f"{self.base_url}/bdbs",
                headers=self.headers,
                verify=self.verify_ssl
            )
            if response.status_code == 200:
                databases = response.json()
                matching_dbs = []
                for db in databases:
                    if db.get('name') == name:
                        # Extract relevant information
                        matching_dbs.append({
                            'name': db.get('name'),
                            'uid': db.get('uid'),
                            'port': db.get('port'),
                            'memory_size': db.get('memory_size'),
                            'status': db.get('status'),
                            'type': db.get('type'),
                            'endpoints': db.get('endpoints', []),
                            'replication': db.get('replication', False),
                            'replica_sync': db.get('replica_sync', 'disabled'),
                            'replica_sources': db.get('replica_sources', [])
                        })
                return matching_dbs
            return []
        except requests.exceptions.RequestException as e:
            print(f"Error getting database {name}: {str(e)}")
            return []

def main():
    # Initialize the API client with config values from config.py
    api = RedisEnterpriseAPI(
        host=REDIS_ENTERPRISE_HOST,
        port=REDIS_ENTERPRISE_PORT,
        username=REDIS_ENTERPRISE_USERNAME,
        password=REDIS_ENTERPRISE_PASSWORD
    )
    
    try:
        # 1. Check if database exists before creating
        db_name = "exercise2-db"
        existing_dbs = api.get_database(db_name)
        if existing_dbs:
            print(f"Found {len(existing_dbs)} existing database(s) with name {db_name}, deleting them...")
            for db in existing_dbs:
                api.delete_database(db['uid'])
            print("Existing databases deleted successfully")
        
        print("Creating new database...")
        db = api.create_database(db_name)
        print(f"Database created successfully: {db['name']}")
        
        # 2. Create three new users
        #2.1 Make sure all the roles exist
        # List of roles to create with their memberships
        roles = [
            {"name": "db_viewer", "membership": "db_viewer"},
            {"name": "db_member", "membership": "db_member"},
            {"name": "admin", "membership": "admin"}
        ]
        print("Starting role creation process...")
        # Create all roles and get their details
        created_roles = api.create_roles(roles)
        if created_roles:
            print("\nAll roles were created successfully!")
            # Create a mapping of role names to their UIDs
            role_uid_map = {role['name']: role['uid'] for role in created_roles}
        else:
            print("\nFailed to create roles. Check the logs above for details.")
            return

        users = [
            {
                "email": "john.doe@example.com",
                "password": "password123",
                "name": "John Doe",
                "role_uid": role_uid_map["db_viewer"]
            },
            {
                "email": "mike.smith@example.com",
                "password": "password123",
                "name": "Mike Smith",
                "role_uid": role_uid_map["db_member"]
            },
            {
                "email": "cary.johnson@example.com",
                "password": "password123",
                "name": "Cary Johnson",
                "role_uid": role_uid_map["admin"]
            }
        ]
        
        print("\nCreating users...")
        for user_data in users:
            user = api.create_user(**user_data)
            print(f"User {'already exists' if user.get('uid') else 'created successfully'}: {user['name']}")
        
        # 3. List and display all users
        print("\nListing all users:")
        users = api.list_users()
        for user in users:
            print(f"Name: {user['name']}, Role: {user['role']}, Email: {user['email']}")
        
        # 4. Delete the database
        print("\nDeleting database...")
        # Get the database UID before deleting
        db_to_delete = api.get_database(db_name)
        if db_to_delete:
            api.delete_database(db_to_delete[0]['uid'])
            print("Database deleted successfully")
        else:
            print("Database not found for deletion")
        
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response details: {e.response.text}")

if __name__ == "__main__":
    main() 