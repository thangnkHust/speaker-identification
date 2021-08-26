from . import db

class Speaker(db.Model):
    __tablename__ = "speaker"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    file_path = db.Column(db.String(255))

    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path

    def __repr__(self):
        return '<Speaker %d>' % self.id
