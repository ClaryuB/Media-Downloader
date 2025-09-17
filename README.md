# 🎬 Media Downloader

A lightweight Streamlit app to download audio or video from YouTube and Twitch — with live progress, direct download, and no server-side file storage.

## 🚀 Features

- ✅ Download from YouTube and Twitch
- 🎧 Choose between MP3 (audio) or MP4 (video)
- 📊 Live progress bar and status updates
- 📥 Direct download via browser (no files stored on server)
- ⚙️ Automatic FFmpeg integration via `imageio-ffmpeg`
- 📱 Mobile-friendly interface

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg)

## 🌍 Live Demo

The app is publicly available at:

👉 [https://media-downloader-9q6h.onrender.com](https://media-downloader-9q6h.onrender.com)

Feel free to test it by pasting a YouTube or Twitch video URL and choosing your preferred format.

## 📦 Installation (Local)

```bash
git clone https://github.com/your-username/media-downloader.git
cd media-downloader
pip install -r requirements.txt
streamlit run app.py

