import requests
import streamlit as st
RAPIDAPI_KEY = st.secrets["RAPIDAPI_KEY"]
BASE_URL = "https://scraptik.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "scraptik.p.rapidapi.com"
}

def extract_sound_id(tiktok_url: str):
    """Extract the sound ID from a TikTok sound URL"""
    if "music/" not in tiktok_url:
        return None
    try:
        return tiktok_url.split("music/")[1].split("?")[0].split("-")[-1]
    except:
        return None

def get_sound_data(sound_id: str):
    """Fetch sound metadata + UGC info from Scraptik"""
    endpoint = f"{BASE_URL}/sound/info"
    params = {"sound_id": sound_id}
    response = requests.get(endpoint, headers=HEADERS, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Scraptik failed: {response.status_code}")
    
    return response.json()
