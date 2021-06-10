from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Prakash:pass123@localhost/naukri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	user_id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique= True)
	password = db.Column(db.String(64))
	
db.create_all()
	
@app.route('/', methods = ['GET', 'POST' ])
def log():
	if request.method == 'POST':
		a = request.form.get('ac')
		if a=='signup' :
			newuser = User(username=request.form['username'],password=request.form['password'])
			db.session.add(newuser)
			db.session.commit()
			return render_template('re_login.html')
		elif a=='login' :
			q = User.query.filter_by(username = request.form['username']).first()
			if (q.password == request.form['password']):
				return  render_template('success_login.html', name=request.form['username'])
			else:
				return render_template('re_enter_credentials.html')
	return render_template('login.html')	
	
	
