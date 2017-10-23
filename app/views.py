from django.shortcuts import render
from app.models import User
# Create your views here.

def index(request):
    return render(request, "app/index.html")

def users(request):
    return render(request, "app/users.html")
