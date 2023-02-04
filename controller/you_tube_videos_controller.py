from flask import Blueprint, Flask , request

you_tube_videos_controller = Blueprint('you_tube_videos_controller',__name__)

@you_tube_videos_controller.route('/getVideos')
def get_videos():
    page = request.args.get('page')
    pass
