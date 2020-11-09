import moviepy.editor

vid=moviepy.editor.VideoFileClip(r"Enter path to your video file here")
audio=vid.audio
audio.write_audiofile("result.mp3")