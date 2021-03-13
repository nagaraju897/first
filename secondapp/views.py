from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func(request):
    s='<h1>hi friends.....orakane vahanu friends...byee friends..</h1>'
    return HttpResponse(s)
