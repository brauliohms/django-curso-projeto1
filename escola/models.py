from django.db import models

# Create your models here.


class Disciplina(models.Model):
    AREAS = [("BIO", "Biológicas"), ("EXA", "Exatas"), ("HUM", "Humanas")]

    nome = models.CharField(max_length=50, unique=True)
    area = models.CharField(max_length=3, choices=AREAS, null=True, blank=True)
    carga_horaria = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kargs):
        if self.nome:
            self.nome = self.nome.strip().upper()

        super().save(*args, *kargs)


class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=80)
    email = models.EmailField("E-mail", null=True, blank=True)
    telefone = models.CharField("Telefone", max_length=15, null=True, blank=True)
    nota1 = models.DecimalField(
        "Nota P1", max_digits=3, decimal_places=1, null=True, blank=True
    )
    nota2 = models.DecimalField(
        "Nota P2", max_digits=3, decimal_places=1, null=True, blank=True
    )
    mediafinal = models.DecimalField(
        "Media Final", max_digits=3, decimal_places=1, null=True, blank=True
    )
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def save(self, *args, **kargs):
        if self.nome:
            self.nome = self.nome.strip().upper()
        if self.email:
            self.email = self.email.strip().lower()

        if self.telefone:
            self.telefone = (
                self.telefone.strip().replace("-", "").replace("(", "").replace(")", "")
            )

        if self.nota1 and self.nota2:
            self.mediafinal = (self.nota1 + self.nota2) / 2

        super().save(*args, *kargs)
