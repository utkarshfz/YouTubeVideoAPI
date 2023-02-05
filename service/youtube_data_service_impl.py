from db.model.video import Video
import os
import googleapiclient.discovery
import googleapiclient.errors
from dateutil import parser

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyCf9_Y6GoIaEJvM_WuPRvg0i5IMDs6PttU"

class YoutubeDataServiceImpl:
    def fetch_videos(query , max_results) -> list:
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = api_key)
        request = youtube.search().list(part="snippet",maxResults=max_results,q=query)
        data = request.execute()
        data_items = data["items"]
        video_list = []
        for item in data_items:
            video_id = item["id"]["videoId"]
            thumbnail_default = item["snippet"]["thumbnails"]["default"]["url"]
            thumbnail_medium = item["snippet"]["thumbnails"]["medium"]["url"]
            thumbnail_high = item["snippet"]["thumbnails"]["high"]["url"]
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            published_at = parser.parse(item["snippet"]["publishedAt"])
            video = Video(video_id = video_id , thumbnail_default = thumbnail_default , thumbnail_medium = thumbnail_medium , thumbnail_high = thumbnail_high,
            title = title , description = description , published_at = published_at)
            video_list.append(video)
        return video_list
        