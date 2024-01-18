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
