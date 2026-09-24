# 🍽️ Kitchen Service

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.1-green?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4-purple?style=for-the-badge&logo=bootstrap)

---

## 📌 Project Description

**Kitchen Service** is a Django web application for managing a restaurant kitchen.

The project allows authenticated users to manage cooks, dish types, and dishes. Users can create, view, update, delete, and search kitchen-related records through a simple and convenient web interface.

This application can be used as a basic internal management system for a restaurant, cafe, or kitchen team.

---

## 🚀 Features

- 🔐 User authentication and authorization
- 👨‍🍳 Cook management
- 🍲 Dish management
- 🗂️ Dish type management
- 🔎 Search by:
  - dish type name
  - dish name
  - cook username
- 📄 Pagination for list pages
- 🛠️ Django admin panel
- 🎨 Bootstrap 4 styling
- 🧾 Crispy Forms integration
- ⚙️ Environment variables support with `.env`
- ✅ Tests for models, forms, views, admin, and search functionality

---

## 🧰 Technologies Used

- **Python 3.13**
- **Django**
- **SQLite**
- **HTML**
- **CSS**
- **Bootstrap 4**
- **Django Crispy Forms**
- **python-dotenv**

---

## 📁 Project Structure

```text
kitchen-service/
├── kitchen/
│   ├── migrations/
│   ├── templatetags/
│   ├── tests/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── kitchen_service/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
├── templates/
├── .env.example
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/agridenko/kitchen-service.git
cd kitchen-service
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

---

### 3. Activate the virtual environment

#### On macOS/Linux:

```bash
source .venv/bin/activate
```

#### On Windows:

```bash
.venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Create `.env` file

Create a `.env` file in the project root directory based on `.env.example`.

```bash
cp .env.example .env
```

Example `.env` file:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
```

You can generate a new Django secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then paste the generated key into your `.env` file.

> ⚠️ Never commit your real `.env` file to GitHub.

---

### 6. Apply database migrations

```bash
python manage.py migrate
```

---

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

---

### 8. Run the development server

```bash
python manage.py runserver
```

Open the project in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Authentication

Most pages are available only for authenticated users.

You can log in using:

```text
http://127.0.0.1:8000/accounts/login/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 🧪 Running Tests

To run all tests:

```bash
python manage.py test
```

The project includes tests for:

- models
- forms
- views
- admin configuration
- search functionality

---

## 🌍 Environment Variables

The project uses environment variables for sensitive configuration.

Required variables:

| Variable | Description | Example |
|---|---|---|
| `DJANGO_SECRET_KEY` | Secret key used by Django | `your-secret-key-here` |
| `DJANGO_DEBUG` | Enables or disables debug mode | `True` |

Example `.env.example`:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
```

---

## 📸 Screenshots

You can add screenshots here later.

Example:

```markdown
![Home page](static/images/screenshot-home.png)
```

---

## 👤 Author

Created by [agridenko](https://github.com/agridenko)

---

## 📄 License

This project is created for educational purposes.

---