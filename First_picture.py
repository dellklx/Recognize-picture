import os
import subprocess
video_folder = input('Input video folder:')
videos = []
for dirpath,dirs,files in os.walk(video_folder):
    if files:
        for file in files:
            if len(file.split(".")) == 2:
                videos.append("%s\%s"%(dirpath,file))
for video in videos:
    command = r'D:\ffmpeg-3.3.1-win64-static\bin\ffmpeg -i %s -vframes 1 D:\temp\picture\%s.jpg'%(video,video.split('\\')[-1].split('.')[0])
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
