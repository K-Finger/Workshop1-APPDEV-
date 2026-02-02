import requests
import matplotlib.pyplot as plt
from datetime import datetime
import sys

data = requests.get("http://localhost:8080/transactions").json()

if not data:
    sys.exit(1)

times = [datetime.fromisoformat(t["timestamp"]) for t in data]
prices = [t["price"] for t in data]

plt.figure(figsize=(10, 6))
plt.scatter(times, prices)
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
# If we never save it. we encounter an error
plt.savefig("chart.png")

