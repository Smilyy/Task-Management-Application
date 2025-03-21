# 📋 Django Task Manager

This is a Django-based web application for task management.


## 🚀 Features

- ✅ Create, view, and filter tasks by category.
- 🔒 Only **admins** can manage categories.
- 🎨 Clean and responsive UI styled with **Bootstrap**.
- 🔐 **Login required** for accessing the admin panel.


## ⚡ Quick Start

pip install pipenv
pipenv install django 
pipenv shell
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

🔐 Security

    Admin users are automatically logged out after leaving the admin panel.
    Full CSRF protection is implemented.
    Custom 404 and 500 error pages prevent sensitive information leakage.

🧪 Test This App

Use test.http (included in the task_management/ folder) with the VS Code REST Client to test all project URLs.

✨ Live Demo

👉 Click here to view the GitHub Pages version: https://smilyy.github.io/Task-Management-Application/


✨ Created by Laura all rights reserved ✨
