from flask import Flask
from controller.you_tube_videos_controller import you_tube_videos_controller
from service.video_manager import VideoManager

__app = Flask(__name__)
__app.register_blueprint(you_tube_videos_controller)
video_manager = VideoManager() # Singleton Method. 
video_manager.start_async_video_fetch_job() # Starts video fetch job.
if __name__ == "__main__":
    __app.run(debug = False)