from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "Login/login.html")

def register(request):
    return render(request, "Login/register.html")

def home(request):
    return render(request, "Login/home.html")