from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Здесь мы расположим все доступные курсы')

def create(request):
    return HttpResponse('Здесь мы разместим форму для создания своего курса')

def delete(request, course_id):
    return HttpResponse(f'Здесь мы будем удалять {course_id} курс')

def detail(request, course_id):
    return HttpResponse(f'Страница для получения информации о {course_id} курсе')

def enroll(request, course_id):
    return HttpResponse(f'Здесь мы сможем записаться на выбранный {course_id} курс')
