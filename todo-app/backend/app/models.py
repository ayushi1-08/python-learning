from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    status = db.Column(db.String(20), default='Open')
    isFavorite = db.Column(db.Boolean, default=False)
    assignee = db.Column(db.String(50))
    dueDate = db.Column(db.Date)
    priority = db.Column(db.String(20))  # or Integer, if you want numbers

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'isFavorite': self.isFavorite,
            'assignee': self.assignee,
            'dueDate': self.dueDate.isoformat() if self.dueDate else None,
            'priority': self.priority  
        }