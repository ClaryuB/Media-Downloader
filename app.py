import streamlit as st
from utils.config import APP_TITLE, APP_DESCRIPTION, SERVICES, FORMATS
from downloader.media import download_media_to_memory

st.set_page_config(page_title=APP_TITLE)
st.title(APP_TITLE)
st.write(APP_DESCRIPTION)

service = st.selectbox("Select platform", SERVICES)
url = st.text_input("🔗 Enter video URL")
format_choice = st.radio("Choose format", FORMATS)
audio_only = format_choice == "Audio (MP3)"

if st.button("Download"):
    if url:
        try:
            st.info("Starting download...")
            result = download_media_to_memory(url, audio_only)
            st.success(f"✅ Download complete: {result['title']}")
            st.download_button(
                label="⬇️ Download file",
                data=result['data'],
                file_name=result['filename'],
                mime=result['mime']
            )
        except Exception:
            st.error("❌ A critical error occurred. Please check the URL or try again.")
    else:
        st.warning("⚠️ Please enter a valid URL.")
