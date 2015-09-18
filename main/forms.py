from django import forms
from django.core.validators import RegexValidator

from main.models import Company


class UserSignUp(forms.Form):
    name = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    email = forms.CharField(required=True)


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class CreateTender(forms.Form):
    name = forms.CharField(required=True)
    company = forms.IntegerField(required=True)
    description = forms.CharField(required=True, widget=forms.Textarea)
    opening_date = forms.DateField(required=True)


class EditTender(forms.Form):
    description = forms.CharField(required=True, widget=forms.Textarea)
    opening_date = forms.DateField(required=True)


class CreateItem(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True)
    image = forms.ImageField(required=False)


class EditItem(forms.Form):
    description = forms.CharField(required=False)
    quantity = forms.IntegerField(required=False)


class CreateQuote(forms.Form):
    tender = forms.IntegerField(required=True)
    comapny = forms.IntegerField(required=True)
    item = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)
    unit_price = forms.CharField(required=True)
    total_price = forms.CharField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class EditQuote(forms.Form):
    tender = forms.IntegerField(required=True)
    comapny = forms.IntegerField(required=True)
    item = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)
    unit_price = forms.CharField(required=True)
    total_price = forms.CharField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)


