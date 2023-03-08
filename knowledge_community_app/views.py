from typing import Dict
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserLoginModelForm, UserRegisterModelForm, UserRegisterForm
from .models import User


LOGGED: bool = False


def index(request: HttpRequest) -> HttpResponse:
    if LOGGED:
        return render(request, 'index.html')
    return redirect('login')


def login(request: HttpRequest) -> HttpResponse:
    global LOGGED
    LOGGED = False
    form: UserLoginModelForm = UserLoginModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            check_if_exist = None
            try:
                check_if_exist = User.objects.get(email=email)
                password_if_exits = User.objects.get(password=password)
                if password == password_if_exits.password and check_if_exist is not None:
                    LOGGED = True
                    messages.success(request, "You have been successfully logged!")
                    return redirect('index')
            except User.DoesNotExist:
                messages.warning(request, "User is not registered or incorrect credentials!")
        else:
            messages.error(request,
                           "Fail to login!\nPlease, verify your e-mail or password!")
    form2 = UserLoginForm()
    context: Dict[str, UserLoginForm | UserLoginModelForm] = {
        "form": form2
    }
    return render(request, 'login.html', context)


def register(request: HttpRequest) -> HttpResponse:
    global LOGGED
    LOGGED = False
    form: UserRegisterModelForm = UserRegisterModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            check_if_exist = None
            try:
                check_if_exist = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            finally:
                if check_if_exist is None:
                    new_user = User(name=name, email=email, password=password)
                    new_user.save()
                    messages.success(request, "You have been successfully registered!")
                else:
                    messages.warning(request, "User already exists!")
    form2 = UserRegisterForm()
    context: Dict[str, UserRegisterForm | UserRegisterModelForm] = {
        "form": form2
    }
    return render(request, 'register.html', context)
