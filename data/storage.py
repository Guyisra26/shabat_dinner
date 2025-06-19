import json
import os

DATA_FILE = "data/rsvps.json"

def load_data()-> dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r",encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data: dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
