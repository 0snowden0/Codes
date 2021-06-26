from . import auth
from flask import render_template

@auth.app_errorhandler(404)
def page_not_fount(e):
	return render_template('404.html') , 404
	
@auth.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
	

