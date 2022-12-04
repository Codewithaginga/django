from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello world')


def brian(request):
    return HttpResponse("hello brian")

def darwin(request):
    return HttpResponse("hello darwin")
