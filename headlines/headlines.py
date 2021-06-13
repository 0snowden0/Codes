from flask import Flask,render_template,request,redirect,url_for
import requests
import urllib

app = Flask(__name__)

FEEDS={'hindu':"https://www.thehindu.com/news/national/kerala/feeder/default.rss",
	 'timesofindia': "https://timesofindia.indiatimes.com/rssfeeds/878156304.cms"}
	 
@app.route('/',methods=['POST','GET'])
def log():
	if request.method=='POST' :
		print(request.form['type'])
		if request.form['type']=='login' :
		     return redirect(url_for('user', name=request.form['username']))
	return render_template("login.html")
	
@app.route('/user/<name>')
def user(name):
	return "hey man"
	
#@app.route('/hindu')
#def hind():
	
	
#@app.route('/timesofindia')
#def times():
#	return get_news(FEEDS['timesofindia'])
#	
#def get_news(publication):
#	feed=feedparser.parse(publication)
#	first_article= feed['entries'][9]
#	return render_template("tem.html", article=first_article)
#	
#def get_weather(query)
	
 	
	
if __name__=='__main__':
	app.run(debug=True)
