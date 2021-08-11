from my_app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    complete = db.Column(db.Boolean)

    def __init__(self, title, complete):
        self.title = title
        self.complete = complete

    def __repr__(self):
        return '<Todo %d>' % self.id