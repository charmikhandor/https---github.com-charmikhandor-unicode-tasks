from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from .forms import Covidstats
from.import forms,requests
 
finals=[]
# Create your views here.
def form(request):
    # return HttpResponse('about')
    return render(request, 'form.html')

def country(request):
    if request.method=='POST':
        cont=request.POST.get('country')
        form=Covidstats(request.post)
        if form.is_valid():
            final=form.cleaned_data['cont']
            finals.append(final)
            ## response = requests.request("GET", url, headers=headers)
        else:
            return render(request, 'form.html',{"form":form})
    return render(request, 'form.html',{"form":form})

def data(request):
    stat="india"
    return render(request,'forn2.html',)
    


