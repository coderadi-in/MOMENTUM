# ==================================================
# IMPORTS
# ==================================================

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

# ==================================================
# PLUGINS REFERENCE
# ==================================================

db = SQLAlchemy()
migrator = Migrate()
encrypt = Bcrypt()
logger = LoginManager()

# ==================================================
# FUNCTIONS
# ==================================================

# * FUNCTION TO BIND ALL PLUGINS TO THE SERVER
def bind_plugins(server):
    '''
    Binds all plugins to the server.
    '''

    db.init_app(server)
    migrator.init_app(server)
    encrypt.init_app(server)
    logger.init_app(server)