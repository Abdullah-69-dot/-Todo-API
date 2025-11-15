#  Todo API – Django REST Framework

A simple **Todo application** built with **Django** and **Django REST Framework**.  
This project allows you to manage todo items with full CRUD operations.

---

##  Features
- Create new todo items
- Retrieve all todo items
- Retrieve a single todo item
- Update an existing todo item
- Delete a todo item

---

##  Tech Stack
- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **SQLite** (default)
- Optional: **django-cors-headers** for cross-origin requests

---

## 📦 Installation & Setup
cd D:\TodoAPI

python -m venv .venv

.venv\Scripts\activate
#Linux / macOS
# source .venv/bin/activate

pip install django djangorestframework django-cors-headers

# pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

# http://127.0.0.1:8000/

