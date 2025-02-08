from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.


def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')