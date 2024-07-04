# myblog_project


## Installation

1. Create a virtual environment and activate it (optional but recommended):

    ```bash
    python -m venv myenv
    ```
    #### On Windows use
   `env\Scripts\activate`
    
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Note: Run redis and celery

Environment variables, including sensitive data like SECRET_KEY, are managed directly in the settings.py file and are not hidden. The Redis URL, email SMTP settings, and others can be changed directly in settings.py

`For detailed API documentation, refer to the API.md file.`

