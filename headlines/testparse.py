#import urllib
#import json
import requests

url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=192509fe34fcc0bbf3ce60f483d0d33b"
url=url.format("thiruvananthapuram")
response = requests.get(url)
data = response.json()
print(data)


#import feedparser
#
#FEEDS={'hindu':"https://www.thehindu.com/news/national/kerala/feeder/default.rss",
#	 'timesofindia': "https://timesofindia.indiatimes.com/rssfeeds/878156304.cms"}
#
#feed=feedparser.parse(FEEDS['hindu'])
#first= feed['entries'][9]
#print(first)
