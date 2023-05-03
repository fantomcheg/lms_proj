from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('Эта страница для входа пользователя на сайт')

def register(request):
    return HttpResponse('Эта страница для регистрации пользователя на сайте')

def login(request):
    return HttpResponse('Эта страница для входа пользователя на сайт')

def logout(request):
    return HttpResponse('Эта страница для выхода пользователя с сайта и редиректа на главную')

def change_password(request):
    return HttpResponse('Эта страница для изменения пароля пользователя на сайте')

def reset_password(request):
    return HttpResponse('Этот обработчик для сброса пароля пользователя на сайте')


# Create your views here.
