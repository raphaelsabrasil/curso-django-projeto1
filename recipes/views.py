from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('HOME')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('meu contato')