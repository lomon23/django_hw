from django.shortcuts import render
from django.http import HttpResponse

def hello_app1(request):
    return HttpResponse("Hello World")
