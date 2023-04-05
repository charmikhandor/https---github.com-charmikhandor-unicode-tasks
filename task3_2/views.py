from django.shortcuts import render, HttpResponse
import requests
# Create your views here.
def index(request):
    result = request.GET.get('https://api.covid19api.com/summary')
    print(result)
    return render(request, 'index.html',{'result':result})