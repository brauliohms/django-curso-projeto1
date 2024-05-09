# from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AlunoForm, DisciplinasForm
from .models import Aluno, Disciplina


def teste(request):
    print(request.user)
    # assunto = "Teste de E-mail"
    # send_mail(
    #     assunto,
    #     "Mensagem do meu email teste",
    #     "webmaster@meusistema.com",
    #     [
    #         "aluno1@zmail.com",
    #     ],
    #     fail_silently=False,
    # )
    if request.user.is_authenticated:
        print("Usuario esta autenticado")
    else:
        print("Usuario NÃO esta autenticado")

    return render(request, "escola/teste.html")


def home(request):
    data = {}
    data["frutas"] = ["banana", "morango", "pera", "maça"]
    return render(request, "escola/home.html", data)


@login_required
def alunosList(request):
    alunosListaRecebida = Aluno.objects.all()
    return render(request, "escola/lista.html", {"alunos": alunosListaRecebida})


@login_required
def alunosNovo(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("alunosList")

    return render(request, "escola/aluno_novo.html", {"formAlunoNovo": form})


@login_required
def alunosUpdate(request, id):
    aluno = Aluno.objects.get(pk=id)

    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect("alunosList")

    return render(
        request, "escola/aluno_novo.html", {"formAlunoNovo": form, "aluno": aluno}
    )


@login_required
def alunosDelete(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect("alunosList")


@login_required
def disciplinas(request):
    if request.method == "POST":
        # print(request.POST)

        form = DisciplinasForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get("nome")  # nome = request.POST["nome"]
            area = form.cleaned_data.get("area")  # nome = request.POST["nome"]
            carga_horaria = form.cleaned_data.get(
                "carga_horaria"
            )  # nome = request.POST["nome"]
            # area = request.POST["area"]
            # carga_horaria = request.POST["carga_horaria"]
            # #
            novaDisciplina = Disciplina(
                nome=nome, area=area, carga_horaria=carga_horaria
            )
            #
            # print(nome, area, carga_horaria)
            novaDisciplina.save()
            return redirect("disciplinas")

    elif request.method == "GET":
        disciplinas = Disciplina.objects.all().order_by("nome")
        form = DisciplinasForm()

    return render(
        request, "escola/disciplinas.html", {"disciplinas": disciplinas, "form": form}
    )
