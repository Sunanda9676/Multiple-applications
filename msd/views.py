from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def msd(request):
    return render(request,'msd.html')
def dhoni(request):
    return HttpResponse('<h1> dhoni is a good player</h1>')
