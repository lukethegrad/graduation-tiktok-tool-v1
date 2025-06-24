from apify_scraper import run_tiktok_sound_scrape

sound_url = st.text_input("Paste a TikTok sound URL:")

if st.button("Analyze Sound"):
    with st.spinner("Scraping data..."):
        try:
            data = run_tiktok_sound_scrape(sound_url)
            st.success(f"Found {len(data)} UGC videos")

            for video in data:
                st.markdown(f"**Author:** {video.get('authorMeta', {}).get('name')}")
                st.markdown(f"**Likes:** {video.get('diggCount')}")
                st.markdown(f"[Watch video]({video.get('webVideoUrl')})")
                st.markdown("---")
        except Exception as e:
            st.error(f"❌ Failed to scrape: {e}")
