from django.shortcuts import redirect, render

from .forms import AlunoForm
from .models import Aluno


# Create your views here.
def home(request):
    data = {}
    data["frutas"] = ["banana", "morango", "pera", "maça"]
    return render(request, "escola/home.html", data)


def alunosList(request):
    alunosListaRecebida = Aluno.objects.all()
    return render(request, "escola/lista.html", {"alunos": alunosListaRecebida})


def alunosNovo(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("alunosList")

    return render(request, "escola/aluno_novo.html", {"formAlunoNovo": form})


def alunosUpdate(request, id):
    aluno = Aluno.objects.get(pk=id)

    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect("alunosList")

    return render(
        request, "escola/aluno_novo.html", {
            "formAlunoNovo": form, "aluno": aluno}
    )


def alunosDelete(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect("alunosList")
