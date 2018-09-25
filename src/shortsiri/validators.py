from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	u=URLValidator()
	v1=False
	v2=False
	try:
		u(value)
	except:
		v1=True
	v2='http://' + value

	try:
		u(v2)
	except:
		v2=True
	if v1== False and v2==False:
		raise ValidationError("Invalid URL")
	return value

def validate_dot_com(value):

	if not 'com' in value:
		raise ValidationError('Need .com at the end')
	return value



