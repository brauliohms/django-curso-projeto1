from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def helloworld(request):
    hoje = datetime.now()
    return HttpResponse(f"<h1>Hello, World!</h1> <br>{hoje}")


def home(request):
    return render(request, "hello/home.html")
