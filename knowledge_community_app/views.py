from typing import Dict
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import UserLoginForm, UserLoginModelForm, UserRegisterModelForm, UserRegisterForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def login(request: HttpRequest) -> HttpResponse:
    form: UserLoginForm = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
        else:
            messages.error(request,
                           "Fail to login!\nPlease, verify your e-mail or password!")
    form = UserLoginForm()
    context: Dict[str, UserLoginForm | UserLoginModelForm] = {
        "form": form
    }
    return render(request, 'login.html', context)


def register(request: HttpRequest) -> HttpResponse:
    form: UserRegisterForm = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(request.POST)
            messages.success(request, "You have been successfully registered!")
    form = UserRegisterForm()
    context: Dict[str, UserRegisterForm | UserRegisterModelForm] = {
        "form": form
    }
    return render(request, 'register.html', context)
