import yt_dlp
import streamlit as st
import re
import os
from io import BytesIO
import imageio_ffmpeg

class StreamlitLogger:
    def __init__(self):
        self.progress_bar = st.progress(0)
        self.status_text = st.empty()
        self.error_text = st.empty()

    def debug(self, msg):
        clean_msg = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', msg)
        if "[download]" in clean_msg:
            self.status_text.text(clean_msg)
            match = re.search(r"(\d+\.\d+)%", clean_msg)
            if match:
                percent = float(match.group(1))
                self.progress_bar.progress(min(int(percent), 100))

    def warning(self, msg): pass
    def error(self, msg):
        if "ffmpeg not found" in msg:
            self.error_text.error("❌ FFmpeg is missing. Conversion failed.")
        elif "fragment not found" in msg:
            self.error_text.warning("⚠️ Some fragments were skipped. File may still be usable.")
        else:
            self.error_text.error("❌ An unexpected error occurred.")

def download_media_to_memory(url: str, audio_only: bool = True) -> dict:
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    logger = StreamlitLogger()

    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
        'logger': logger,
        'quiet': True,
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get('title')
        ext = 'mp3' if audio_only else info.get('ext', 'mp4')
        filename = f"{title}.{ext}"

        with open(filename, "rb") as f:
            data = BytesIO(f.read())

        os.remove(filename)

        return {
            'title': title,
            'filename': filename,
            'data': data,
            'mime': 'audio/mpeg' if audio_only else 'video/mp4'
        }
