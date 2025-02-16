import csv
import json
import time
import requests

url = "https://pultegroup.wd1.myworkdayjobs.com/wday/cxs/pultegroup/PGI/jobs"

def get_data(url, offset, limit):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
    }
    data = {
        "appliedFacets": {},
        "limit": limit,
        "offset": offset,
        "searchText": ""
    }
    response = requests.post(url, json=data, headers=headers)
    return json.loads(response.text)

total = get_data(url, 0, 1)["total"]
i = 0
while i < total:
    time.sleep(1)
    print(i)
    jobPostings = get_data(url, i, 20)["jobPostings"]
    i += 20
    with open('jobs.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'externalPath', 'locationsText', 'postedOn', 'bulletFields']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()

        for item in jobPostings:
            item['bulletFields'] = ', '.join(item['bulletFields'])
            writer.writerow(item)









