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


class PostForm(forms.Form):
    """Content body of site"""
    title: str = forms.CharField(label='Title', max_length=30)
    content: str = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':8, 'cols':5}))
    image: str = forms.ImageField()


class PostModelForm(forms.ModelForm):
    class Meta:
        model: Posts = Posts
        fields: List[str] = ["title", "image", "content"]
