from server import app, db
from server.models import User


@app.shell_context_processor

def make_shell_context():
    return {'db': db, 'User': User}