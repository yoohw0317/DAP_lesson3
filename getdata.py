import requests
import pandas as pd

url = 'http://apis.data.go.kr/B551172/Lung06/luPastSmokeByType'
params ={'serviceKey' : '7f3Sv/MWAuG1nfC6Yh1Djk2jK3u9dr7xploM/R5k6xuy/71Pgo2rOQWYkpEJDL6yVQyTj4KbTf2f/ww7S52N5w==', 'pageNo' : '1', 'numOfRows' : '100', 'centerNm' : '국립암센터', 'fromYear' : '2010', 'toYear' : '2019', 'type' : 'json' }

response = requests.get(url, params=params).json()
items = response.get('response').get('items').get('item')
df = pd.DataFrame(items)
df.to_excel('./data.xlsx')
print (df)
