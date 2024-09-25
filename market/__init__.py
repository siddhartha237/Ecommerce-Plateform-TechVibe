from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '9428715562237dac12ba2d0f'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # Initialize Bcrypt instance in the app context
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
app.app_context().push()

from market import routes