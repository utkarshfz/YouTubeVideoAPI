from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty@db:5432/postgres'
db = SQLAlchemy(app)

class Video(db.Model):
    video_id = db.Column(db.String(100) ,  primary_key = True , nullable = False)
    thumbnail_default = db.Column(db.String(250))
    thumbnail_medium = db.Column(db.String(250))
    thumbnail_high = db.Column(db.String(250))
    title = db.Column(db.String(250))
    description = db.Column(db.String(500))
    published_at = db.Column(db.DateTime)
    timestamp = db.Column(db.DateTime , default = datetime.datetime.now)

    def __init__(self , video_id , thumbnail_default , thumbnail_medium , thumbnail_high , title , description , published_at):
        super().__init__()
        self.video_id = video_id
        self.thumbnail_default = thumbnail_default
        self.thumbnail_medium = thumbnail_medium
        self.thumbnail_high = thumbnail_high
        self.title = title
        self.description = description
        self.published_at = published_at

with app.app_context():
    db.create_all()