# app/models.py
from app import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    sell_mode = db.Column(db.String)

    def __repr__(self):
        return f'<Event {self.name}>'
