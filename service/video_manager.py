from model.video_detail_list import VideoDetailList
from model.video_detail_list import Video
import threading
import time
from constants.constants import REFRESH_INTERVAL_SEC , YOUTUBE_QUERY_KEY_WORD , MAX_YOUTUBE_VIDEO_RESPONSE_SIZE , YOU_TUBE_VIDEO_PLAYER_PREFIX , DATE_TIME_FORMAT
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

    # Queries VideoDataBaseService and returns VideoDetialsList for the inputed page.
    def query_videos(self , page) -> VideoDetailList:
        video_list = VideoDataBaseService().getVideoList(page)
        video_detail_list = []
        for video in video_list:
            title = video.title
            description = video.description
            thumbnail_default = video.thumbnail_default
            thumbnail_medium = video.thumbnail_medium
            thumbnail_high = video.thumbnail_high
            video_link = YOU_TUBE_VIDEO_PLAYER_PREFIX + video.video_id
            published_at = video.published_at.strftime(DATE_TIME_FORMAT)
            video_detail_list.append(Video(title = title , description = description , thumbnail_default = thumbnail_default , thumbnail_medium = thumbnail_medium 
            , thumbnail_high = thumbnail_high , video_link= video_link , published_at = published_at))

        return VideoDetailList(video_detail_list)

    # Starts asycn video fetch job via threading.
    def start_async_video_fetch_job(self):
        job = threading.Thread(target = self.__async_fetch_videos , daemon = True)
        job.start()

    def __async_fetch_videos(self):
            while True:
                video_detail_list = YoutubeDataServiceImpl.fetch_videos(YOUTUBE_QUERY_KEY_WORD , MAX_YOUTUBE_VIDEO_RESPONSE_SIZE)
                video_db_service = VideoDataBaseService()
                for video in video_detail_list:
                    video_db_service.addVideo(video)
                time.sleep(REFRESH_INTERVAL_SEC)             
    

    


