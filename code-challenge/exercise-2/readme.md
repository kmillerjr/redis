# Exercise 2: Redis Enterprise Role and User Management

This exercise demonstrates the implementation of role and user management functionality for Redis Enterprise using the REST API. The code provides a Python-based solution for creating and managing roles and users in a Redis Enterprise cluster.

## Features

- Role Management:
  - Create roles with specific management permissions
  - Check for existing roles before creation
  - Support for multiple role types (admin, db_viewer, db_member)

- User Management:
  - Create users with specific roles
  - Check for existing users before creation
  - Support for multiple users with different role assignments

- Database Management:
  - Create databases with specified configurations
  - Check for existing databases
  - Delete databases when needed

## Prerequisites

- Python 3.6 or higher
- Redis Enterprise cluster running and accessible
- Required Python packages (install using `pip install -r requirements.txt`):
  - requests==2.31.0

## Configuration

The script uses the following default configuration:
- Host: localhost
- Port: 9443
- Username: admin
- Password: admin

You can modify these settings in the `main()` function of `redis_enterprise_api.py` or pass them as parameters when initializing the `RedisEnterpriseAPI` class.

## Usage

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python redis_enterprise_api.py
   ```

The script will:
1. Check for and delete any existing database named "exercise2-db"
2. Create a new database
3. Create three roles (db_viewer, db_member, admin)
4. Create three users with different roles:
   - John Doe (db_viewer)
   - Mike Smith (db_member)
   - Cary Johnson (admin)
5. List all users
6. Delete the created database

## Role Details

The script creates three predefined roles:

1. `db_viewer`:
   - Membership: db_viewer
   - Permissions: View database information

2. `db_member`:
   - Membership: db_member
   - Permissions: Basic database operations

3. `admin`:
   - Membership: admin
   - Permissions: Full administrative access

## User Details

The script creates three users with different roles:

1. John Doe:
   - Email: john.doe@example.com
   - Role: db_viewer
   - Password: password123

2. Mike Smith:
   - Email: mike.smith@example.com
   - Role: db_member
   - Password: password123

3. Cary Johnson:
   - Email: cary.johnson@example.com
   - Role: admin
   - Password: password123

## Error Handling

The script includes comprehensive error handling for:
- API request failures
- Existing resource conflicts
- Invalid responses
- Network issues

## Security Notes

- SSL verification is disabled by default for development purposes
- Passwords are transmitted in plain text (consider using environment variables or secure configuration in production)
- Basic authentication is used for API access

## API Endpoints Used

- `/v1/roles` - Role management
- `/v1/users` - User management
- `/v1/bdbs` - Database management

## Development

To modify the script:
1. Update the role definitions in the `roles` list
2. Modify user information in the `users` list
3. Adjust database configuration in the `create_database` method
4. Update error handling as needed

## Testing

The script includes basic error handling and validation. Prior to using this for production, the following will need to be added:
- Unit tests
- Integration tests
- Input validation
- Secure password handling
- Environment variable support for sensitive data 