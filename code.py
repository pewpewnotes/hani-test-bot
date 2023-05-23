import requests
import json

with open("key.json", "r") as f:
    key = json.load(f)["key"]


print(f"{key}")
w = requests.get("http://www.google.com")
print(f"{w.status_code} ::->")
