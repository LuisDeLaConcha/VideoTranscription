import yt_dlp

video_url = "https://www.youtube.com/watch?v=LVLOZQYL_t4"

ydl_opts = {
    'format': 'best[ext=mp4][vcodec^=avc1][acodec^=mp4a]/best',
    'outtmpl': 'mechanic_video.%(ext)s',
    'merge_output_format': 'mp4',
    'noplaylist': True,
    'quiet': False,
    'verbose': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
