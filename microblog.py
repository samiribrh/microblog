import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models.user import User
from app.models.post import Post


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
