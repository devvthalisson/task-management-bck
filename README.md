# Task Manager API

API REST developed with **DJANGO + DJANGO REST FRAMEWORK**, focused on personal task management with JWT authentication, permission control, and backend best practices.

This project was created for **educational purposes**, as part of a recurring back-end training routine, prioritinzing clean archicture, security, and clear business rules.

---

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite (development environment)
- Django Silk
- Django Filter
- Django Spectacular

---

## Features

### Authentication
- User registration
- JWT Login
- Token refresh
- Protected routes

### Tasks
- Create tasks
- List authenticated user tesks
- Retreve task details
- Update tasks
- Delete tasks
- Mark tasks as completed (dedicated endpoint)

### Security
- Users can only access their own tasks
- Custom permission classes
- Completion endpoint allows updating **only** the `completed` field

---

## Installation and Setup

### Clone the repository
```bash
git clone https://github.com/devvthalisson/task-management-bck.git
cd task-management-bck
```

### Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate # Linux / MAC
.venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
python manage.py migrate
```

### Start the server
```bash
python manage.py runserver
```

---

## Routes

### Auth
<img width="1292" height="487" alt="image" src="https://github.com/user-attachments/assets/64537071-19c5-4404-b50a-8851ee4b8c97" />

### Tasks
<img width="1292" height="432" alt="image" src="https://github.com/user-attachments/assets/0bc7a2a6-313b-49f2-b6d4-33c29ad0f7b6" />

---

## Testing

Manual tests performed using:
- Postman
- Insomnia
(Automated tests can be added in future iterations.)

## Author
Developed by Thalisson Menezes
Back-end focused studies with Django, REST APIs and clean architecture.
