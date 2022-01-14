from yt_dlp import YoutubeDL

ydl_opts = {'format': '18'}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])