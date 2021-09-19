import requests
import json
import time

url = 'https://api.coingecko.com/api/v3/coins/list'

response = requests.get(url)

d = response.json()

for i in d:
    if i['name'] == 'Bitcoin':
        json_object = json.dumps(i, indent = 4)
        with open("Bitcoin.json", "w") as outfile:
            outfile.write(json_object)

def price_get(di):
    ls = []
    for id in di:
        dd = id['id']
        url2 = f"https://api.coingecko.com/api/v3/coins/bitcoin/"
        rs = requests.get(url2)
        d = rs.json()
        ls.append(d)
        
    return ls


