from pytube import YouTube
#downloads the video
# class Download:
#     def __init__(self, download_video):
#         self.download_video = download_video

#     def get_video(self):
#         print(self.download_video.title())
# class Info:
#     def __init__(self, progressive_stream, dash_stream, audio_stream, mp4_stream):
#         self.progressive_stream = progressive_stream
#         self.dash_stream = dash_stream
#         self.audio_stream = audio_stream
#         self.mp4_stream = mp4_stream
# class Storage:
#     storage = {
        
#     }
#     pass


# #all of the function and class calls for video download


# print(first_vid)

def get_video(get_video_id):
    vid = YouTube(get_video_id)
    print(vid.title)

get_video("https://www.youtube.com/watch?v=uJFdylfY-5Y")