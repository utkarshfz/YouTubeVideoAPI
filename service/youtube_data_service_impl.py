from db.model.video import Video
import os
import googleapiclient.discovery
import googleapiclient.errors
from dateutil import parser
from constants.constants import ITEMS , ID , VIDEOID , SNIPPET , THUMBNAILS , DEFAULT , URL , MEDIUM , HIGH , TITLE , DESCRIPTION , PUBLISHED_AT , PUBLISHED_AFTER , VIDEO , DATE , API_SERVICE_NAME ,API_VERSION
import threading
from dotenv import load_dotenv


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = API_SERVICE_NAME
api_version = API_VERSION
load_dotenv("apiKey.env")
class YoutubeDataServiceImpl:
    __singleton_lock = threading.Lock()
    __youtube_data_service_instance = None
    __api_keys =  os.getenv('API_KEYS').split(",")
    __key_count = len(__api_keys)
    __key_index = 0
    

    @classmethod
    def get_instance(self):
        if not self.__youtube_data_service_instance:
            with self.__singleton_lock:
                if not self.__youtube_data_service_instance:
                    self.__video_data_base_service_instance = YoutubeDataServiceImpl()
        return self.__video_data_base_service_instance

    def __init__(self):
        if not self.__youtube_data_service_instance:
            self.__youtube_data_service_instance = self
        else:
            raise Exception("This is a SingletonClass :: instance already exists, pls use get_instance Method")
    

    # Queries youtuble api to fetch video results and returns them as a list
    def fetch_videos(self , query , max_results) -> list:
        
        

        try:
            youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = self.__api_keys[self.__key_index])
            request = youtube.search().list(part=SNIPPET,maxResults=max_results,q=query,type=VIDEO,order=DATE,publishedAfter=PUBLISHED_AFTER)
            data = request.execute()
        except Exception as e:
            print("Exception : " + str(e) + " occured while interacting with you tube api --- retrying with another API key")
            self.__key_index = (self.__key_index + 1) % self.__key_count
            raise e
        data_items = data[ITEMS]
        video_list = []
        for item in data_items:
            try:
                video_id = item[ID][VIDEOID]
                thumbnail_default = item[SNIPPET][THUMBNAILS][DEFAULT][URL]
                thumbnail_medium = item[SNIPPET][THUMBNAILS][MEDIUM][URL]
                thumbnail_high = item[SNIPPET][THUMBNAILS][HIGH][URL]
                title = item[SNIPPET][TITLE]
                description = item[SNIPPET][DESCRIPTION]
                published_at = parser.parse(item[SNIPPET][PUBLISHED_AT])
                video = Video(video_id = video_id , thumbnail_default = thumbnail_default , thumbnail_medium = thumbnail_medium , thumbnail_high = thumbnail_high,
                title = title , description = description , published_at = published_at)
                video_list.append(video)
            except Exception as e:
                print("Exception " + str(e) + " encountred while parsing video: Skipping current video")
        return video_list
        