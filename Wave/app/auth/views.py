from flask import render_template,request,flash,url_for
from . import auth
from flask_login import login_user, logout_user,login_required
from .models import User
from .. import db

@auth.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		user = User.query.filter_by(email=request.form['email']).first()
		if user is not None and user.verify_password(request.form['password']) :
			login_user(user,request.form['remember_me'])
			next = request.args.get('next')
			if next is None or not next.startswith('/'):
				next = url_for('main.index')
			return redirect(next)
		flash('Invalid username or password')
	return render_template('auth/login.html')
	
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('main.index')
	
@auth.route('/register' methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		user = User(username = request.form['username'], password=request.form['password'] ,email= request.form['email'])
		db.session.add(user)
		db.session.commit()
		flash('You can login now')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html')
		
	
	
	
	
