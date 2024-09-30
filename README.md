# MyProject

MyProject is a Flask-based web application that manages users and customers. It uses MySQL as its database and implements basic CRUD (Create, Read, Update, Delete) operations.

## Features

- User management
- Customer management
- MySQL database integration
- Flask-SQLAlchemy ORM
- Flask-Migrate for database migrations

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
2.  Create a virtual environment and activate it: python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate
3.   Install the required packages: pip install -r requirements.txt   
4. Set up your MySQL database and update the `.env` file with your database credentials: DATABASE_URL=mysql://username:password@localhost/database_name
5. Initialize the database: flask db upgrade
6. To run the application, use the following command: flask run
7. The application will be available at `http://127.0.0.1:5000/`.
8. ## Project Structure
9. myproject/ │ ├── app/ │ ├── init.py │ ├── models.py │ ├── routes.py │ ├── customers/ │ │ ├── init.py │ │ └── routes.py │ └── templates/ │ ├── index.html │ └── customers/ │ ├── list.html │ ├── create.html │ ├── update.html │ └── delete.html │ ├── migrations/ ├── .env ├── config.py ├── run.py └── requirements.txt
10. ## Contributing

Contributions to MyProject are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).
