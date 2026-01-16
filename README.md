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
git clone 
```
