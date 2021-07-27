from . import db


class Scan(db.Model):
    # primary keys are required by SQLAlchemy
    ID = db.Column(db.Integer, primary_key=True)
    Hostname = db.Column(db.String(100))
    IP = db.Column(db.String(100))
    MAC = db.Column(db.String(100))
    Lastseen = db.Column(db.String(100))
    Status = db.Column(db.String(100))
