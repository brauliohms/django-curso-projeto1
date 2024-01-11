from django.contrib import admin

from .models import Aluno, Disciplina

# Register your models here.
admin.site.register(Disciplina)
admin.site.register(Aluno)
