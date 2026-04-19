# ==================================================
# IMPORTS
# ==================================================

from .app import app
from .auth import auth

# ==================================================
# FUNCTIONS
# ==================================================

# * FUNCTION TO BIND ALL ROUTERS TO THE SERVER
def bind_routers(server):
    '''
    Binds all routers to the server
    '''

    server.register_blueprint(app)
    server.register_blueprint(auth)