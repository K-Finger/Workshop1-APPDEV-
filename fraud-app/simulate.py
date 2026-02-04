import requests
import random
from datetime import datetime, timedelta

URL = "http://localhost:8080/transactions"

users = ["alice", "bob", "charlie", "dave", "eve"]
base_time = datetime.now()

for i in range(50):
    txn = {
        "user_id": random.choice(users),
        "price": round(random.uniform(5, 500), 2),
        "timestamp": (base_time - timedelta(hours=random.randint(0, 72))).isoformat(),
    }
    requests.post(URL, json=txn)
    print(f"Sent: {txn}")

print("Done!")
