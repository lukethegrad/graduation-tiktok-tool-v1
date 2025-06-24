import streamlit as st
from scraptik_api import extract_sound_id, get_sound_data

st.set_page_config(page_title="TikTok Sound Scraper", layout="centered")
st.title("🎵 TikTok Sound Analyzer")

url = st.text_input("Paste TikTok Sound URL")

if url:
    sound_id = extract_sound_id(url)
    if sound_id:
        with st.spinner("Fetching TikTok data..."):
            try:
                data = get_sound_data(sound_id)
                st.success("✅ Data loaded")

                st.write("### 📌 Sound Info")
                st.write("**Title:**", data.get("title"))
                st.write("**Author:**", data.get("authorName"))
                st.write("**Duration (s):**", data.get("duration"))
                st.write("**Video count (UGC):**", data.get("videoCount"))

                st.write("### 🎥 Top Videos")
                top_videos = data.get("topVideos", [])[:5]
                for vid in top_videos:
                    st.markdown(f"[{vid['authorName']} - {vid['desc']}]({vid['videoUrl']})")
                    st.write(f"❤️ {vid['diggCount']} | 💬 {vid['commentCount']} | 🔁 {vid['shareCount']}")
                    st.markdown("---")

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.error("Invalid TikTok sound link.")


