
# Hello World Django App

This is a simple Django web application that returns a "Hello World" message in JSON format, and optionally in HTML if requested. It contains a single route that responds with `{"Message": "Hello World!"}`.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Git
- Django (you can install it using pip)

## How to Run

Follow these steps to clone and run the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mohan070707/LabAssignment5/helloworld_project
   cd helloworld_project
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Django:**
   If Django is not installed yet, install it with:
   ```bash
   pip install django
   ```

4. **Run the migrations (if necessary):**
   ```bash
   python manage.py migrate
   ```

5. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   - Open your browser and navigate to `http://127.0.0.1:8000/`.
   - You should see the JSON response: 
     ```json
     {
       "Message": "Hello World!"
     }
     ```

## Accessing the HTML Response (Optional)

If you want to access the "Hello World" message in HTML format, visit the URL with a `?format=html` query parameter:

```bash
http://127.0.0.1:8000/?format=html
```

This will display a simple HTML page with the "Hello World!" message in bold.

## Project Structure

```plaintext
helloworld_project/
├── hello/                 # Django app folder
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── views.py           # Views for the app
│   ├── urls.py            # URL configuration for the app
├── helloworld_project/     # Django project settings
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
└── manage.py              # Django management command-line tool
```

## License

This project is open-source and free to use. No specific license applied.
