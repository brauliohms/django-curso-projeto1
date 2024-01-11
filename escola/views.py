from django.shortcuts import render


# Create your views here.
def home(request):
    data = {}
    data["frutas"] = ["banana", "morango", "pera", "maça"]
    return render(request, "escola/home.html", data)


def alunosList(request):
    return render(request, "escola/lista.html")
