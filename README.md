# Vehicle Renting System

Welcome to the Vehicle Renting System project! This README will guide you through setting up the project on your local machine and collaborating using Git and GitHub.

---

## 📋 Project Structure

- **Frontend/** — HTML, CSS, JavaScript files, templates, and static assets
- **Backend/** — Python Flask backend, database logic, APIs
- **Docs/** — Documentation, reports, diagrams

---

## 🚀 Getting Started: Clone the Repository

1. Open your terminal or PowerShell.
2. Run this command to copy the project to your computer:
   
```bash
git clone https://github.com/Otienokaiser/car_rental_system.git
````

3. Move into the project folder:
   
```bash
cd car_rental_system
````

🌿 Creating and Working on a Feature Branch

We use feature branches to work on new features or fixes without affecting the main code.

Step 1: Update your local main branch

Make sure your local main branch is up to date:

```bash
git checkout main
git pull origin main
````
Step 2: Create a new feature branch

Feature branch names should be descriptive. For example:

```bash
git checkout -b feature/login-system
````

This creates and switches you to a new branch called feature/login-system.

Step 3: Work on your feature

Make changes to files as needed.

💾 Saving Your Work
Step 1: Check which files have changed

```bash
git status
````
Step 2: Stage your changes (prepare them to be saved)

```bash
git add .
````

This stages all your changes.

Step 3: Commit your changes with a message

```bash
git commit -m "Add user login functionality"
````

Write clear commit messages explaining what you did.

📤 Uploading Your Changes to GitHub

Push your feature branch so others can see it:

```bash
git push origin feature/login-system
````

🛑 Important Collaboration Rules

. Do NOT commit or push directly to the main branch.
. Always create a feature branch for your work.
. Keep feature branches focused on one task.
. Use clear commit messages.
. Wait for code review before merging your PR.

🧹 Keeping Your Branch Updated

If main changes while you’re working:

```bash
git checkout main
git pull origin main

git checkout feature/login-system
git merge main
````

Fix any conflicts, then push your updated feature branch:

```bash
git push origin feature/login-system
````

Proposed folder structure

car_rental_sysem/
│
├── Backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── vehicle.py
│   │   ├── lease.py
│   │   └── vehicle_image.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── admin_routes.py
│   │   ├── client_routes.py
│   │   └── public_routes.py
│   │
├── Frontend/
│   ├── base.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   │   
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── add_vehicle.html
│   │   └── manage_vehicles.html
│   │   
│   ├── client/
│   │   ├── dashboard.html
│   │   ├── lease_vehicle.html
│   │   └── return_vehicle.html
│   │   
│   │   └── public/
│   │       ├── landing.html
│   │       └── vehicle_detail.html
│   
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │
│   ├── uploads/
│   │   └── vehicles/
│   │
│   └── utils/
│       ├── __init__.py
│       ├── decorators.py
│       └── helpers.py
│
├── Docs/
│   ├── README.md
│   └── database_schema.md
│
└── README.md
