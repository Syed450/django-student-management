# 🎓 Student Management System

A Django-based web application to manage student records with authentication and REST API support.

---

## 🚀 Live Demo
🔗 https://django-student-management-vkyh.onrender.com

---

## 📂 GitHub Repository
🔗 https://github.com/Syed450/django-student-management

---

## ✨ Features

- 🔐 User Registration & Login
- 📋 Add, Edit, Delete Students (CRUD)
- 🌐 REST API using Django REST Framework
- 🔒 Authentication-protected routes
- 🎯 Clean UI with HTML & CSS

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML, CSS
- Gunicorn
- Render (Deployment)

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| GET | /api/students/ | Get all students |
| POST | /api/students/ | Create student |
| PUT | /api/update/<id>/ | Update student |
| DELETE | /api/delete/<id>/ | Delete student |

---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/Syed450/django-student-management.git
cd django-student-management
pip install -r requirements.txt
cd myproject
python manage.py migrate
python manage.py runserver



