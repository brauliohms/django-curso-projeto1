from django.urls import path

from escola.views import (
    alunosDelete,
    alunosList,
    alunosNovo,
    alunosUpdate,
    disciplinas,
    home,
    teste,
)

urlpatterns = [
    path("", home, name="escola"),
    path("alunos/", alunosList, name="alunosList"),
    path("alunos/novo", alunosNovo, name="alunosNovo"),
    path("alunos/<int:id>", alunosUpdate, name="alunosUpdate"),
    path("alunos/delete/<int:pk>", alunosDelete, name="alunosDelete"),
    path("disciplinas/", disciplinas, name="disciplinas"),
    path("teste/", teste),
]
