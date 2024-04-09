# Multi User Auth System

This Django project demonstrates multi-user authentication with different user types (regular user, staff member, and superuser).

# Main Features

- Supports login with email, username, or phone number.
- Different dashboard views based on user roles.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/matrix-bro/multi-user-auth-system.git
```

2. Go to project's folder

```bash
cd multi-user-auth-system
```

3. Create a virtual environment and activate it

```bash
python -m venv venv

(In windows)
source .\venv\Scripts\activate

(In linux)
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Apply database migrations

```bash
python manage.py migrate
```

6. Start the development server

```bash
python manage.py runserver
```
