from django.shortcuts import render
from django.http import HttpResponse
from.import task1

def function(request, x, y):
    return HttpResponse(task1.check(x,y))

# Create your views here.
