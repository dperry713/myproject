from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from app.models import User
from sqlalchemy.exc import ProgrammingError

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    try:
        users = User.query.all()
        return render_template('index.html', users=users)
    except ProgrammingError as e:
        print(f"Database error: {e}")
        return "There was an error accessing the database. Please check your database configuration."
