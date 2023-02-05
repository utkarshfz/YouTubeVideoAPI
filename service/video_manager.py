from model.video_detail_list import VideoDetailList
from model.video_detail_list import Video
import threading
import time
from constants.constants import REFRESH_INTERVAL_SEC , YOUTUBE_QUERY_KEY_WORD , PAGE_SIZE
from service.youtube_data_service_impl import YoutubeDataServiceImpl;
from service.video_db_service import VideoDataBaseService

class VideoManager:
    __singleton_lock = threading.Lock()
    __video_manager_instance = None
    __youtube_data_service_api = YoutubeDataServiceImpl

    @classmethod
    def get_instance(self):
        if not self.__video_manager_instance:
            with self.__singleton_lock:
                if not self.__video_manager_instance:
                    self.__video_manager_instance = VideoManager()
        return self.__video_manager_instance

    def __init__(self):
        if not self.__video_manager_instance:
            self.__video_manager_instance = self
        else:
            raise Exception("This is a SingletonClass :: instance already exists, pls use get_instance Method")

    def query_videos(self , page) -> VideoDetailList:
        dummy_video = Video("test video" , "This is an dummy Video" , "thumb_def" , "thumb_med" , "thumb_high" , "video_link", "today")
        return VideoDetailList(dummy_video)

    def start_async_video_fetch_job(self):
        job = threading.Thread(target = self.__async_fetch_videos , daemon = True)
        job.start()

    def __async_fetch_videos(self):
            while True:
                video_detail_list = YoutubeDataServiceImpl.fetch_videos(YOUTUBE_QUERY_KEY_WORD , PAGE_SIZE)
                video_db_service = VideoDataBaseService()
                for video in video_detail_list:
                    video_db_service.addVideo(video)
                time.sleep(REFRESH_INTERVAL_SEC)             
    

    


