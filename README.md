# LittleLemon API

A Django REST Framework API for managing restaurant menu items and bookings.

## Setup Instructions

### Step 1: Clone the Project
```bash
git clone https://github.com/Kanissthebest/LittleLemon.git
cd littlelemon
```

### Step 2: Set Up Virtual Environment (PowerShell)
```bash
# Install Python 3.12 dependencies
pipenv install

# Activate the virtual environment
pipenv shell
```

### Step 3: Configure Django Interpreter in VS Code
1. Press `Ctrl + Shift + P`
2. Select "Python: Select Interpreter"
3. Choose the virtual environment (usually named after your project folder)

### Step 4: Database Setup
Ensure MySQL is running, then apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

## Testing the APIs

### Get Authentication Token

1. **Start the server:**
   ```bash
   python manage.py runserver
   ```

2. **Generate a token using Insomnia:**
   - Open Insomnia
   - Create a **POST** request to: `http://127.0.0.1:8000/api-token-auth/`
   - Set the request body (JSON):
     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```
   - Send the request and copy the token from the response

### Use Token for Authenticated Requests

For any protected endpoint in Insomnia:
1. Go to the **Auth** tab
2. Click the dropdown menu and select **Bearer Token**
3. In the **TOKEN** field, paste your token
4. In the **PREFIX** field, type: `Token`
5. Send your request - the Authorization header will be automatically added

The token will be formatted as: `Token YOUR_TOKEN_HERE`

## Available Endpoints

### Authentication
- `POST /api-token-auth/` - Get authentication token

### Menu Items (Protected - requires token)
- `GET /api/menu-items/` - List all menu items
- `POST /api/menu-items/` - Create a new menu item

### Protected Message
- `GET /api/message/` - Get protected message (requires token)

### Restaurant Menu (Public)
- `GET /restaurant/menu/menu/` - List all restaurant menu items
- `GET /restaurant/menu/menu/<id>` - Get specific menu item
- `PUT /restaurant/menu/menu/<id>` - Update menu item
- `DELETE /restaurant/menu/menu/<id>` - Delete menu item

### Bookings
- `GET /restaurant/booking/tables/` - List all bookings
- `POST /restaurant/booking/tables/` - Create new booking
- `GET /restaurant/booking/tables/<id>` - Get specific booking
- `PUT /restaurant/booking/tables/<id>` - Update booking
- `DELETE /restaurant/booking/tables/<id>` - Delete booking

## Notes
- Always include the authentication token for protected endpoints
- The token format in headers is: `Token YOUR_TOKEN_HERE` (not "Bearer")


