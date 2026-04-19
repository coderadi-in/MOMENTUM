# ==================================================
# IMPORTS
# ==================================================

from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import login_required, db

# ==================================================
# ROUTER INIT
# ==================================================

app = Blueprint('app', __name__, url_prefix='/app')

# & DASHBOARD ROUTE
@app.route('/dashboard/')
@login_required
def dashboard():
    return "Dashboard"