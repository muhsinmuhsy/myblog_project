# myblog_project


## Installation

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

3. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Note: Run redis and celery

Environment variables, including sensitive data like SECRET_KEY, are managed directly in the settings.py file not hidden, redis url, email smpt can change directly in settings.py

`For detailed API documentation, refer to the API.md file.`

