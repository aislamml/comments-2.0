from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comm(db.Model):

    __tablename__ = 'comm'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
