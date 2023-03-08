from typing import List
from django import forms
from django.core.mail.message import EmailMessage
from .models import User


class UserLoginForm(forms.Form):
    email: str = forms.EmailField(label='E-mail', max_length=100)
    password: str = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=20)


class UserLoginModelForm(forms.ModelForm):
    class Meta:
        model: User = User
        fields: List[str] = ["email", "password"]
