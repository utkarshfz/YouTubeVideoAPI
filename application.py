from flask import Flask
from controller.you_tube_videos_controller import you_tube_videos_controller

app = Flask(__name__)
app.register_blueprint(you_tube_videos_controller)

if __name__ == "__main__":
    app.run()