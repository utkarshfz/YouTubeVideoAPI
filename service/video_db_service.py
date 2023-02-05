import db.model.video as video_db
from flask import Flask
from db.model.video import app , Video

video_db_instance = video_db.db
session = video_db_instance.session;


class VideoDataBaseService:
    def addVideo(self , video):
        with app.app_context():
            if not session.get(Video , video.video_id):
                session.add(video)
                session.commit()        
