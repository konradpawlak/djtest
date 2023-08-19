from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Hunterek. You are at the polls index. Take a look!")

def konrad(reqest):
    return HttpResponse("Hello Konrad")