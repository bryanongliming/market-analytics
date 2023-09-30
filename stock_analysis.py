import requests
import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&outputsize=full&apikey=MCTGIEGJS4B95PO4'
r = requests.get(url)
data = r.json()

df = pd.DataFrame(data['Time Series (Daily)']).transpose()
print(df.to_string())
