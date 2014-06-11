__author__ = 'koke07'
from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
