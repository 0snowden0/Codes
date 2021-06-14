from flask import Flask,render_template,request,redirect,url_for,flash
import requests
import urllib
from flask_sqlalchemy import SQLAlchemy
import feedparser

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Prakash:pass123@localhost/appwork'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
	__tablename__='users'
	user_id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64),unique = True)
	password = db.Column(db.String(64))
	first = db.Column(db.Integer)
	city = db.Column(db.String())
	
db.create_all()
	
	
FEEDS={'hindu':"https://www.thehindu.com/news/national/kerala/feeder/default.rss",
	 'manorama' :"https://www.onmanorama.com/news/kerala.feeds.onmrss.xml"}
	 
@app.route('/',methods=['POST','GET'])
def log():
	if request.method=='POST' :
		query = User.query.filter_by(username= request.form['username']).first()
		if request.form['type']=='login':
			if query is None :
				flash("Seems like you are a new user try signingup !")
			elif query.password != request.form['password']:
				flash("Looks like the username or password you entered is incorrect !")
			elif query.password == request.form['password']:
				return redirect(url_for('feed', name=request.form['username']))
		elif request.form['type'] == 'signup' :
			if query is None:
				u = User(username= request.form['username'], password = request.form["password"], first=0)
				db.session.add(u)
				db.session.commit()
				return redirect(url_for('user', name=request.form['username']))
			else:
				flash("That username is taken , Try again!")
	return render_template("login.html")


@app.route('/user/<name>', methods=['POST', 'GET'])
def user(name):
	q = User.query.filter_by(username=name).first()
	if q.first==0:
	 	q.first=1
	 	db.session.commit()
	 	return render_template("inputcity.html", name= name)
	elif request.method == 'POST':
		q.city = request.form['city']
		db.session.commit()
		return redirect(url_for('feed', name=name))
		
@app.route('/user/feed/<name>', methods=['GET' , 'POST'])
def feed(name):
	url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=192509fe34fcc0bbf3ce60f483d0d33b"
	qu = User.query.filter_by(username=name).first()
	cit = qu.city
	url=url.format(cit)
	response = requests.get(url)
	data = response.json()
	feedhindu=feedparser.parse(FEEDS['hindu'])
	feedmanorama = feedparser.parse(FEEDS['manorama'])
	
	return render_template("loggeduser.html" , data=data , hindu=feedhindu['entries'] , manorama=feedmanorama['entries'])
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
	
if __name__ == '__main__' :
	app.run()

