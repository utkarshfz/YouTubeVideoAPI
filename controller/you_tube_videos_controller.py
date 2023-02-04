from flask import Blueprint , request
from service.video_manager import VideoManager
import json

you_tube_videos_controller = Blueprint('you_tube_videos_controller',__name__)

class YouTubeVideoController:
    @you_tube_videos_controller.route('/getVideos')
    def __get_videos():
        page = int(request.args.get('page'))
        video_manager = VideoManager.get_instance()
        response = video_manager.query_videos(page)
        return  json.dumps(response , default = lambda o: o.__dict__)
    
