# Kudos Backend Setup

This guide will help you set up the Kudos Backend project locally.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10+
- PostgreSQL
- pip (Python package manager)
- Virtualenv (optional but recommended)

---

## Steps to Run the Project Locally

### 1. Clone the Repository

```bash
git clone <repository-url>
cd kudos-backend
```

### 2. Set Up Environment Variables

1. Create a `.env` file from the provided `.env.example` file:
   ```bash
   cp .env.example .env
   ```
2. Update the `.env` file with your local configuration (e.g., database credentials, secret keys).

---

### 3. Set Up PostgreSQL Database

1. Start your PostgreSQL server.
2. Create a database named `django_kudos` using DBeaver or any other database management tool:
   ```sql
   CREATE DATABASE django_kudos;
   ```
   Alternatively, you can use the command line:
   ```bash
   createdb -U <your-username> django_kudos
   ```
3. Import the provided SQL dump file to populate the database with initial data. If using DBeaver:
   - Open the `django_kudos` database in DBeaver.
   - Right-click on the database and select `Tools > Restore`.
   - Choose the `django_kudos-202508082330-dump.sql` file and follow the prompts.
     Alternatively, use the command line:
   ```bash
   psql -U <your-username> -d django_kudos -f django_kudos-202508082330-dump.sql
   ```

---

### 4. Install Dependencies

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### 5. Run the Project

1. Apply migrations (if needed):
   ```bash
   python manage.py migrate
   ```
2. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

### 6. Access the Admin Portal

1. Open the admin portal in your browser:
   ```
   http://127.0.0.1:8000/admin
   ```
2. Use the following credentials to log in:
   - **Username:** root
   - **Password:** root

---

### 7. Sample Users for Testing

You can use the following sample users to test the Kudos functionality:

| Username | Password  |
| -------- | --------- |
| Lucy     | Admin@123 |
| Jay      | Admin@123 |

---

### 8. Run the Frontend Server

Once the backend server is up and running, start the frontend server as per the frontend project instructions.
