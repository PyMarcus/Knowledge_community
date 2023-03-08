from typing import List
from django import forms
from django.core.mail.message import EmailMessage
from .models import User
from .models import Posts


class UserLoginForm(forms.Form):
    email: str = forms.EmailField(label='E-mail', max_length=100)
    password: str = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=20)


class UserLoginModelForm(forms.ModelForm):
    class Meta:
        model: User = User
        fields: List[str] = ["email", "password"]


class UserRegisterForm(forms.Form):
    name: str = forms.CharField(label='Name', max_length=100)
    email: str = forms.EmailField(label='E-mail', max_length=100)
    password: str = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=20)


class UserRegisterModelForm(forms.ModelForm):
    class Meta:
        model: User = User
        fields: List[str] = ["name", "email", "password"]


class PostForm:
    """Content body of site"""
    title: str = forms.CharField(label='Title', max_length=30)
    content: str = forms.CharField(label='Content', max_length=200)


class PostModelForm:
    class Meta:
        model: Posts = Posts
        fields: List[str] = ["title", "image", "content"]
