# ==================================================
# IMPORTS
# ==================================================

from flask import Flask, redirect, url_for
from plugins import db, logger, bind_plugins, current_user
from routers import bind_routers
from models import *
import os

# ==================================================
# LOAD VIRTUAL ENVIRONMENT
# ==================================================

from dotenv import load_dotenv
load_dotenv('.venv/vars.env')

# ==================================================
# SERVER INIT
# ==================================================

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('KEY')

# ==================================================
# BINDING
# ==================================================

bind_plugins(server)
bind_routers(server)

# ==================================================
# DB INIT
# ==================================================

with server.app_context():
    db.create_all()

# ==================================================
# LOADERS
# ==================================================

# & USER LOADER
@logger.user_loader
def load_user(user):
    return User.query.get(user)

# & APP LOADER
@server.route('/')
def load_app():
    if (current_user.is_authenticated):
        return redirect(url_for('app.dashboard'))
    return redirect(url_for('auth.signup'))