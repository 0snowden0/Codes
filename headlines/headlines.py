from flask import Flask,render_template,request,redirect,url_for
import requests
import urllib
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


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
		print(request.form)
		if request.form['type']=='login':
			query = User.query.filter_by(username= request.form['username']).first()
			if query.password == request.form['password']:
				return redirect(url_for('user', name=request.form['username']))
		elif request.form['type'] == 'signup' :
			u = User(username= request.form['username'], password = request.form["password"], first=0)
			db.session.add(u)
			db.session.commit()
			return redirect(url_for('user', name=request.form['username']))
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
		return render_template("temp.html" , name=name)
		
		
			
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

