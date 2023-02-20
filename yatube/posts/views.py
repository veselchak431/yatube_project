from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('главная страница')


def group_posts(request, slug):
    return HttpResponse(f'slug равен {slug}')
