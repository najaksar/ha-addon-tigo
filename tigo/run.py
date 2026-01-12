import requests
import json
import time

cfg = json.load(open("/data/options.json"))

r = requests.get(
    "https://api2.tigoenergy.com/api/v3/users/login",
    auth=(cfg["username"], cfg["password"]),
)
r.raise_for_status()

print("Tigo login OK")

while True:
    time.sleep(3600)
