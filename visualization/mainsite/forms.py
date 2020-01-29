from django import forms
from .models import userModel


class loginForm(forms.Form):
    userName = forms.CharField(label='用户名', max_length=32)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
