# ==================================================
# IMPORTS
# ==================================================

from plugins import UserMixin, db

# ==================================================
# USER DATABASE MODEL
# ==================================================

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(48), nullable=False)
    password = db.Column(db.String, nullable=False)