from . import db

class Scan(db.Model):
    # primary keys are required by SQLAlchemy
    ID = db.Column(db.Integer, primary_key=True)
    IP = db.Column(db.String(100))
    MAC = db.Column(db.String(100))
    Hostname = db.Column(db.String(100))
    Domain = db.Column(db.String(100))
    OS = db.Column(db.String(100))
