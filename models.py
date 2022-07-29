from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    groupID = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def to_dict(self):
        return {
            'id':self.id,
            'name': self.name,
            'groupID': self.groupID,
            'email': self.email,
            'password': password
        }