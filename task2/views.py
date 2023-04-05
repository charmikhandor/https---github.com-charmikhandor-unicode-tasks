from django.shortcuts import render
from django.http import JsonResponse
from.import task1

def function(request, x, y):
    return JsonResponse(task1.check(x,y))

# Create your views here.
