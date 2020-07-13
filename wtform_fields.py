# Modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from passlib.hash import pbkdf2_sha256
from validate_email import validate_email
import re

# local files
from models import User

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'




# username and Password Check
def invalid_password(form, field):

	username_entered = form.username.data 	# Because the func is called from password field
	password_entered = field.data

	# Check username match
	user_object = User.query.filter_by(username=username_entered).first()
	if user_object is None:
		raise ValidationError("Username or Password is incorrect")
	elif not pbkdf2_sha256.verify(password_entered, user_object.password): 	# Verifying password based on hash
		raise ValidationError("Username or Password is incorrect")


def InvalidEmail(email):  

    if(re.search(regex, email)):
        
        domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com"]

        maildom = re.search("@[\w.]+", email)
        for dom in domains:
            if dom == maildom.group():
                return False

    return True



class RegForm(FlaskForm):
	'''Registration Form'''

	email = StringField('email_label',
		validators = [InputRequired(message = "Required")])

	username = StringField('username_label',
		validators = [InputRequired(message = "Required"),
		Length(min = 4, max = 18, message = "Username must be betweem 4-18")])

	password = PasswordField('password_label',
		validators = [InputRequired(message = "Required"),
		Length(min = 4, max = 18, message = "Password must be betweem 4-18")])

	confirm_pswd = PasswordField('confirm_pswd_label',
		validators = [InputRequired(message = "Required"),
		EqualTo('password', message = "Password does not match")])


	# Check unique username
	def validate_username(self, username):
		user_object = User.query.filter_by(username=username.data).first()
		if user_object:
			raise ValidationError("Username Exists")

	# Email validation & unique
	def validate_email(self, email):
		
		email_object = User.query.filter_by(email=email.data).first()
		if email_object:
			raise ValidationError("Email Already Exists")
		elif InvalidEmail(email.data) == True:
			raise  ValidationError("Invalid/Unsupported Email Address")



class LoginForm(FlaskForm):
	'''Login Form'''

	username = StringField('username_label',
		validators = [InputRequired(message = "Required")])
	password = PasswordField('password_label',
		validators = [InputRequired(message = "Required"),
		invalid_password]) 	# The values will be passed automatically by Flask WTF Validations

