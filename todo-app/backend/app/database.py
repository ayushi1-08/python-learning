from app.models import db
from app.main import app

with app.app_context():
    db.init_app(app)
    db.create_all()