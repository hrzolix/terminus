import requests

url = 'https://api.carbonintensity.org.uk/intensity'

headers = {
  'Accept': 'application/json'
}

r = requests.get(url, headers=headers)

r.json()