from model.video_detail_list import VideoDetailList , Video

class YoutubeDataServiceImpl:
    def fetch_videos(query , max_results) -> VideoDetailList:
        dummy_response = VideoDetailList(Video("test video" , "This is an dummy Video" , "thumb_def" , "thumb_med" , "thumb_high" , "video_link", "today"))
        return dummy_response;