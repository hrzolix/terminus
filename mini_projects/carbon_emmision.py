from pandas.core.indexes.base import Index
import requests
import pandas as pd
import plotly as pty


url = 'https://api.carbonintensity.org.uk/intensity/2021-08-05/2021-09-04'

headers = {
  'Accept': 'application/json'
}

r = requests.get(url, headers=headers)

di = r.json()
df = pd.DataFrame.from_dict(di, orient='index')

rows = []
for i in di.values():
      for j in i:
            fro = j['from']
            to = j['to']
            for row in i:
              row['from']= fro
              row['to'] = to    
              rows.append(row)

      



