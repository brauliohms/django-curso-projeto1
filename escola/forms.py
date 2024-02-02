from django import forms
from django.forms import ModelForm

from .models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "nome",
            "email",
            "telefone",
            "nota1",
            "nota2",
            "mediafinal",
            "disciplina",
        ]
        # exclude = ["mediafinal"]


class DisciplinasForm(forms.Form):
    AREAS = [("BIO", "Biológicas"), ("EXA", "Exatas"), ("HUM", "Humanas")]

    nome = forms.CharField(label="Nome:", max_length=10)
    area = forms.ChoiceField(label="Area:", choices=AREAS)
    carga_horaria = forms.IntegerField(label="Carga Horaria:", required=False)
