from . import db
from werkzeug.security import generate_password_hash , check_password_hash
from flask login import Usermixin
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(db.Model,Usermixin):
	__tablename__='users'
	user_id = db.Column(db.Integer , primary_key=True)
	username = db.Column(db.String(64) , unique=True, index=True)
	email = db.Column(db.String(128) , unique=True , index = True)
	password_hash = db.column(db.String(128))
	role_id=db.Column(db.Integer , db.ForeignKey('roles.id')
	confirmed = db.Column(db.Boolean, default=False)
	
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
		
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
		
	def generate_conformation_token(self, expiration=3600)
		s= Serializer(current_app['SECRET_KEY'], expiration)
		return s.dumps({'confirm' : self.id}).decode('utf-8')
		
	def confirmed(self
		
		
		
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
	
