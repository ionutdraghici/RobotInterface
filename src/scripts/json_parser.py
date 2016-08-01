import json
import csv

with open("data.json", "rt") as f:
    str = f.read()
    jsonObj = json.loads(str)
    navData = jsonObj['0']['data']

with open("data.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(navData[0].keys())
    for data in navData:
        writer.writerow([v for k, v in data.items()])