from django.urls import path
from .views import index, login, register, make_post


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('make_post', make_post, name='make_post')
]
