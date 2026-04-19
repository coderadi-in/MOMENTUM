# ==================================================
# IMPORTS
# ==================================================

from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import login_required, db

# ==================================================
# ROUTER INIT
# ==================================================

auth = Blueprint('auth', __name__, url_prefix='/auth')

# & SIGNUP ROUTE
@auth.route('/signup/')
def signup():
    return "Signup"