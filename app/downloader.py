import os
from yt_dlp import YoutubeDL
from app.config import ffmpeg_path


def download_audio(video_url, save_directory, title, progress_callback):
    def hook(d):
        if d["status"] == "downloading":
            total_bytes = d.get("total_bytes", 0) or d.get("total_bytes_estimate", 1)
            downloaded_bytes = d.get("downloaded_bytes", 0)
            progress = int((downloaded_bytes / total_bytes) * 100)
            progress_callback(progress)
        elif d["status"] == "finished":
            progress_callback(100, "Concluído!")

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": os.path.join(save_directory, f"{title or '%(title)s'}.%(ext)s"),
        "ffmpeg_location": ffmpeg_path,
        "progress_hooks": [hook],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
