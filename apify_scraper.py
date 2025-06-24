import requests
import time

APIFY_TOKEN = "apify_api_a1tnukWTeeLLlQhdqVMdqf0aXrKOXy0XH5K2"
ACTOR_ID = "drobnikj~tiktok-scraper"  # Note the ~ instead of /

def run_tiktok_sound_scrape(sound_url: str, max_videos: int = 10):
    # 1. Start the actor directly (not via task)
    start_run = requests.post(
        f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={APIFY_TOKEN}",
        json={
            "memory": 2048,
            "timeoutSecs": 120,
            "input": {
                "proxy": {
                    "useApifyProxy": True
                },
                "search": sound_url,
                "type": "music",
                "max": max_videos
            }
        }
    )

    if start_run.status_code != 201:
        raise Exception(f"Failed to start Apify actor: {start_run.text}")

    run_data = start_run.json()
    run_id = run_data["data"]["id"]

    # 2. Poll until it's done
    while True:
        run_status = requests.get(
            f"https://api.apify.com/v2/actor-runs/{run_id}?token={APIFY_TOKEN}"
        ).json()
        status = run_status["data"]["status"]
        if status == "SUCCEEDED":
            break
        elif status in ["FAILED", "ABORTED", "TIMED-OUT"]:
            raise Exception(f"Apify actor failed: {status}")
        time.sleep(2)

    # 3. Get the dataset items
    dataset_id = run_status["data"]["defaultDatasetId"]
    dataset_items = requests.get(
        f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={APIFY_TOKEN}"
    ).json()

    return dataset_items
