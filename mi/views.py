from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
def boomra(request):
    return HttpResponse('<center><h1> Brromraaa is a good player</h1><center>')
