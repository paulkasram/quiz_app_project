# Quiz Application

A Django-based quiz application where users can answer multiple-choice or True/False questions. The app allows users to register, take quizzes, and view their results.

## Features
- User registration and authentication (sign up, log in, and log out)
- Admin interface for adding and managing quiz questions
- Support for True/False and multiple-choice questions
- User-specific results tracking with score display
- Backend validation to ensure valid options and correct answers

## Technologies Used
- **Django** - Web framework for rapid development
- **Bootstrap** - Front-end framework for responsive design
- **Phonenumber-field** - Library for handling phone number fields
- **SQLite** (default) - Database for storing questions, quiz results, and user data
- **HTML/CSS** - For front-end styling
- **Python 3.13** - Backend programming language

## Getting Started

### Prerequisites
Ensure you have Python 3.13+ and pip installed.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/paulkasram/quiz_app_project.git 
    ```

2. Navigate into the project directory:
    ```bash
    cd quiz-app
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Setting Up the Database
Run the following commands to set up the database and apply migrations:

1. Apply migrations:
    ```bash
    python manage.py migrate
    ```

2. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

### Running the Application
1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and go to:
    ```bash
    http://127.0.0.1:8000/
    ```

3. To access the Django admin interface, go to:
    ```bash
    http://127.0.0.1:8000/admin/
    ```
    Log in with the superuser credentials you created earlier.

### Adding Questions via Admin
In the Django admin interface, you can add quiz questions by navigating to the `Questions` section. The `correct_option` field should be filled with the name of the correct option (e.g., `option_1`, `option_2`).

## Customizing the App
- **Question types:** Currently, the app supports both multiple-choice and True/False questions.
- **Result tracking:** Each user's quiz results are saved, and you can query them from the database.
- **Styling:** You can customize the Bootstrap theme or add custom styles in the `static` folder.

## Contributing

If you'd like to contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request with a description of your changes

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- Django framework (https://www.djangoproject.com/)
- Bootstrap (https://getbootstrap.com/)
- Phonenumber-field (https://github.com/stefanfoulis/django-phonenumber-field)