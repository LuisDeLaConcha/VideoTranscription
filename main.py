import yt_dlp

# Replace this with the YouTube link of a mechanic video you like
video_url = "https://www.youtube.com/watch?v=LVLOZQYL_t4"  # Example: exhaust gasket replacement

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'mechanic_audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
