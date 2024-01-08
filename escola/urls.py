from django.urls import path

from escola.views import alunosList, home

urlpatterns = [
    path("", home),
    path("aluno/", alunosList),
]
