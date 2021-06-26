import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
	MAIL_PORT = int(os.environ.get('MAIL_PORT')) or 587
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	WAVE_ADMIN = os.environ.get('WAVE_ADMIN')
	WAVE_MAIL_SUBJECT_PREFIX = '[WAVE]'
	WAVE_MAIL_SENDER = ''
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	@staticmethod
	def init_app(app):
		pass
		
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
	
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('PRO_DATABASE_URI')
	
config= {
	'development' = DevelopmentConfig,
	'production' = ProductionConfig,
	'default' = DevelopmentConfig
	}	
	

		
		
