from django import forms
from . import views
from django.core.validators import RegexValidator

class checkin_vis(forms.Form):
	firstname= forms.CharField(validators=[RegexValidator(regex=r'^\w+$',message='Enter valid first name',code='invalid_firstname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter your first name'}))
	lastname= forms.CharField(validators=[RegexValidator(regex=r'^\w+$',message='Enter valid last name',code='invalid_lastname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter your last name'}))
	email= forms.CharField(validators=[RegexValidator(regex=r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',message='Enter valid email',code='invalid_email')],max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	phonenumber= forms.CharField(validators=[RegexValidator(regex=r'^[2-9]{2}[0-9]{8}',message='Enter valid phone number',code='invalid_firstname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter phone number'}))

	#def clean_firstname(self,*args,**kwargs):
	#	firstname = self.cleaned_data.get('firstname')
	#	if '3rx' not in firstname:
	#		raise forms.ValidationError("NOT Valid first name")
	#	return firstname

class checkin_host(forms.Form):
	firstname= forms.CharField(validators=[RegexValidator(regex=r'^\w+$',message='Enter valid first name',code='invalid_firstname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter your first name'}))
	lastname= forms.CharField(validators=[RegexValidator(regex=r'^\w+$',message='Enter valid last name',code='invalid_lastname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter your last name'}))
	email= forms.CharField(validators=[RegexValidator(regex=r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',message='Enter valid email',code='invalid_email')],max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	phonenumber= forms.CharField(validators=[RegexValidator(regex=r'[2-9]{2}[0-9]{8}',message='Enter valid phone number',code='invalid_firstname')],max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter phone number'}))
