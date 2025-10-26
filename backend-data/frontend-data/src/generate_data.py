import json
import random
from datetime import datetime
import time

NUM_ENTRIES = 50  # number of random data points

data = []

for _ in range(NUM_ENTRIES):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "speed": round(random.uniform(0, 200), 2),  # km/h
        "gps": {
            "lat": round(random.uniform(-90, 90), 6),
            "lon": round(random.uniform(-180, 180), 6)
        },
        "camera_frame": f"frame_{random.randint(1,1000)}.jpg"
    }
    data.append(entry)
    time.sleep(0.01)

# Save to JSON in the same folder
with open("dashcam_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Dashcam data generated!")
