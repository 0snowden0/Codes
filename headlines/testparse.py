import urllib
import requests

url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=192509fe34fcc0bbf3ce60f483d0d33b"
url=url.format("tvm")
response = requests.get(url)
data = response.json()
if 'message' in data:
	print(data['message'])
else:
	print(data)


#import feedparser

#FEEDS={'hindu':"https://www.thehindu.com/news/national/kerala/feeder/default.rss",
	# 'manorama' :"https://www.onmanorama.com/news/kerala.feeds.onmrss.xml"}

#feed=feedparser.parse(FEEDS['manorama'])
#first= feed['entries'][9]
#print(feed['entries'][0])
