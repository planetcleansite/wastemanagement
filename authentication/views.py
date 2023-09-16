from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")
def signup(request):
    return render(request,"authentication/signup.html")
def login(request):
    return render(request,"authentication/login.html")
def style(request):
    return render(request,"authentication/style.css")
def signout(request):
    pass