from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    data = {}
    data["frutas"] = ["banana", "morango", "pera", "maça"]
    return render(request, "escola/home.html", data)


def alunosList(request):
    return HttpResponse("Cheguei em Aluno Listagem")
