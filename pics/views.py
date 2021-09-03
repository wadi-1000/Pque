from django.shortcuts import render
from django.htpp import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Welcome to Pque!!')