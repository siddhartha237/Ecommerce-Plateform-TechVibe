# TechVibe-Flask-App

## Overview

**TechVibe** is a Flask-based web application designed as a marketplace for buying and selling electronics. It allows users to register, log in, view available items, purchase items, and sell them back to the marketplace. The app uses Flask for backend development, SQLAlchemy for database interactions, Jinja2 for templating, and Bootstrap for a responsive front-end design.

## Features

- **User Registration & Login**: Users can create accounts and securely log in.
- **Marketplace**: Browse available electronics, purchase, and sell items.
- **Budget Tracking**: Each user starts with a fixed budget that is updated in real-time after purchases or sales.
- **Flashing Messages**: Instant feedback on transactions and login operations via flash messages.
- **Responsive UI**: The app's front-end is styled using Bootstrap for mobile and desktop views.

## Tech Stack

- **Backend**: Flask
- **Templating**: Jinja2
- **Database**: SQLAlchemy (SQLite by default, easily configurable for other databases)
- **Front-end**: Bootstrap, HTML
- **Authentication**: Flask-Login
- **Password Security**: Flask-Bcrypt

## Installation

### Prerequisites
- Python 3.x
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/techvibe.git
   cd techvibe
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Visit the app at: `http://127.0.0.1:5000/`

## Folder Structure

techvibe/
│
├── instance/              # Instance folder for configuration and database
│   └── database.db        # Database file
│
├── market/
│   ├── __init__.py        # App setup and config
│   ├── routes.py          # All application routes
│   ├── models.py          # SQLAlchemy models (User, Item)
│   ├── forms.py           # Flask-WTF forms (Registration, Login, Purchase, Sell)
│   ├── templates/         # HTML templates
│   │   ├── base.html      # Base template for the site
│   │   ├── home.html      # Home page template
│   │   ├── market.html    # Market page template
│   │   ├── login.html     # Login form
│   │   ├── register.html  # Registration form
│   │   └── includes/      # Includes for reusable components
│   │       ├── item_modals.html        # Modals for item details
│   │       └── owned_items_modals.html  # Modals for owned items
│   └── static/            # Static files (CSS, images)
│
├── venv/                  # Virtual environment folder
│
├── requirements.txt       # Python dependencies
├── run.py                 # Script to run the application
└── README.md              # Project documentation





## Database Models

- **User**: Contains user information such as username, email, password, and budget.
- **Item**: Represents items in the marketplace with fields for name, price, barcode, description, and owner.

## Key Functionality

- **Buying Items**: Users can purchase items if their budget allows it.
- **Selling Items**: Users can sell items back to the market and increase their budget.
- **User Authentication**: Secure login and registration system with password hashing.

## Flash Messages

Feedback messages for user actions such as successful login, purchase completion, insufficient funds, etc.

---
