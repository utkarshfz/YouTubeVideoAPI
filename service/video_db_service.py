import db.model.video as video_db
from flask import Flask
from db.model.video import app , Video
from constants.constants import PAGE_SIZE
import threading

video_db_instance = video_db.db
session = video_db_instance.session;


class VideoDataBaseService:

    __singleton_lock = threading.Lock()
    __video_data_base_service_instance = None

    @classmethod
    def get_instance(self):
        if not self.__video_data_base_service_instance:
            with self.__singleton_lock:
                if not self.__video_data_base_service_instance:
                    self.__video_data_base_service_instance = VideoDataBaseService()
        return self.__video_data_base_service_instance

    def __init__(self):
        if not self.__video_data_base_service_instance:
            self.__video_data_base_service_instance = self
        else:
            raise Exception("This is a SingletonClass :: instance already exists, pls use get_instance Method")

    # Persists video details in DB.
    def addVideo(self , video):
        with app.app_context():
            if not session.get(Video , video.video_id):
                session.add(video)
                session.commit()
    
    # Fetches paginated video detail list.
    def getVideoList(self , page):
        with app.app_context():
            page_object = session.query(Video).order_by(Video.published_at.desc()).paginate(page = int(page) , per_page = PAGE_SIZE , error_out = False )
        return page_object.items
        
    
