import json
import random
import time
from datetime import datetime

while True:
    entry = {
        "timestamp": datetime.now().isoformat(),
        "speed": round(random.uniform(0, 200), 2),
        "rpm": round(random.uniform(1000, 8000), 0),
        "fuel": round(random.uniform(0, 100), 1),
        "temperature": round(random.uniform(70, 120), 1),
        "gps": {
            "lat": round(random.uniform(-90, 90), 6),
            "lon": round(random.uniform(-180, 180), 6)
        },
        "camera_frame": f"frame_{random.randint(1,1000)}.jpg"
    }

    try:
        with open("dashcam_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)
    data = data[-100:]  # keep last 100 entries

    with open("dashcam_data.json", "w") as f:
        json.dump(data, f, indent=4)

    time.sleep(1)
