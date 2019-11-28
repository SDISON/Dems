from django import forms
from . import views
from django.core.validators import RegexValidator

class logout(forms.Form):
	phonenumber= forms.CharField(validators=[RegexValidator(regex=r'^[2-9]{2}[0-9]{8}',message='Enter valid phone number',code='invalid_firstname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter phone number'}))
