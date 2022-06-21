from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')

def Aboutme(request):
    return render(request,"aboutme.html")

def Map(request):
    return render(request,"map.html")

def Story(request):
    return render(request,"story.html")

def Aboutstory(request):
    return render(request,"aboutstory.html")