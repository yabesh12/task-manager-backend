# Django Task Manager

## Objective

Backend application implemented using Django and Django Rest Framework, with MongoDB as the database(from MongoDb Atlas Cluster). User authentication and authorization are also implemented.

## Functionalities

- User signup with username, email, and password.
- User login with username and password.
- User logout with token expiration.
- CRUD operations for tasks (Create, Read, Update, Delete).
- Each task has a title, description, due date, and status.
- Users can only access their own tasks.
- MongoDB integration for task storage.

## Endpoints

### User Signup
- **Endpoint:** `/api/signup/`
- **Method:** POST
- **Parameters:** username, email, password
- **Authorization:** AllowAny

### User Login
- **Endpoint:** `/api/login/`
- **Method:** POST
- **Parameters:** username, password
- **Authorization:** AllowAny

### User Logout
- **Endpoint:** `/api/logout/`
- **Method:** POST
- **Authorization:** IsAuthenticated

### Task CRUD
- **Endpoint:** `/api/tasks/`
- **Methods:** GET, POST
- **Parameters (POST):** title, description, due_date, status
- **Authorization:** IsAuthenticated

### Status Choices
- **Endpoint:** `/api/status-choices/`
- **Method:** GET
- **Authorization:** AllowAny

## Instructions to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yabesh12/task-manager-backend.git

2. Create Python Virtualenvironment
    ```bash
    python -m venv venv

3. Activate python virtualenvironment:
    ```bash
    source venv/bin/activate

4. Install packages and dependencies:
    ```bash
    pip install -r requirements.txt

5. Apply the Migrations:
    ```bash
    python manage.py migrate

6. Create a Superuser (optional):
     ```bash
    python manage.py createsuperuser

7. Start the development server:
    ```bash
    python manage.py runserver


### Note
default super-admin user:-
username - yabesh
password - yabesh

