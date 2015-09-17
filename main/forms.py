from django import forms
from django.core.validators import RegexValidator

from main.models import Company

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')


class UserSignUp(forms.Form):
	name = forms.CharField(required=True, validators=[letter_validator])
	password = forms.CharField(required=True)
	email = forms.CharField(required=True)

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())