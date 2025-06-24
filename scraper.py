from playwright.sync_api import sync_playwright

def scrape_tiktok_sound(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
        page = context.new_page()
        page.goto(url, timeout=60000)

        # Wait longer for full load
        page.wait_for_timeout(8000)

        # 🔍 Save a screenshot to see what Playwright sees
        page.screenshot(path="screenshot.png", full_page=True)

        try:
            title = page.locator("h1").first.inner_text()
        except:
            title = "Sound title not found"

        try:
            ugc_count = page.locator('div[data-e2e="music-video-count"]').inner_text()
        except:
            ugc_count = "UGC count not found"

        browser.close()
        return {
            "title": title,
            "ugc_count": ugc_count,
            "screenshot_path": "screenshot.png"
        }
