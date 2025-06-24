
import os
os.system("playwright install chromium")  # <-- This line forces install at runtime

import streamlit as st
from scraper import scrape_tiktok_sound


st.set_page_config(page_title="TikTok Sound Scraper", layout="centered")

st.title("🎵 TikTok Sound Scraper")
url = st.text_input("Paste TikTok Sound URL")

if url:
    with st.spinner("Scraping TikTok..."):
        try:
            data = scrape_tiktok_sound(url)
            st.success("✅ Scrape complete!")
            st.write("**Sound Title:**", data["title"])
            st.write("**UGC Count:**", data["ugc_count"])
        except Exception as e:
            st.error(f"❌ Failed to scrape: {e}")
