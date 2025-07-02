from django.shortcuts import render
from . import models

def home(request):
    return render(request,"home_app/index.html")

